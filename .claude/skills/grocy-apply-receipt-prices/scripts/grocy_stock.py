#!/usr/bin/env python3
"""Reconcile today's Grocy stock entries with real receipt prices and purchase location.

Subcommands:
  locations                 List shopping_locations (id -> name)
  today [--date YYYY-MM-DD] List stock entries purchased on a date, with product names
  apply --updates-file F    Safely PUT price/shopping_location_id for a batch of stock
                            entries, round-tripping every other field so Grocy doesn't
                            null them out. Dry-run by default; pass --apply to commit.

Credentials: --grocy-api-url/--grocy-api-key, else GROCY_API_URL/GROCY_API_KEY env vars,
else a .env file in the current directory.

updates-file format (JSON list):
  [{"entry_id": 3189, "price": 0.94, "shopping_location_id": 2}, ...]
Either "price" or "shopping_location_id" may be omitted/null to leave that field as-is.
"""
import argparse
import datetime
import json
import os
import sys
import time
from pathlib import Path

import httpx

SHOPPING_LOCATIONS_CACHE = None


def load_dotenv_if_present():
    env_path = Path(".env")
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def resolve_credentials(args):
    load_dotenv_if_present()
    api_url = args.grocy_api_url or os.environ.get("GROCY_API_URL")
    api_key = args.grocy_api_key or os.environ.get("GROCY_API_KEY")
    if not api_url or not api_key:
        sys.exit(
            "Missing Grocy credentials. Pass --grocy-api-url/--grocy-api-key, set "
            "GROCY_API_URL/GROCY_API_KEY, or add them to a .env file in the cwd."
        )
    return api_url.rstrip("/"), api_key


def make_client(api_url, api_key):
    return httpx.Client(base_url=api_url, headers={"GROCY-API-KEY": api_key}, timeout=15)


def request_with_retry(client, method, path, retries=4, **kwargs):
    """Grocy/its reverse proxy occasionally answers a rate-limited request with
    HTTP 200 and a zero-byte body instead of an error. Retry a few times before
    giving up, rather than treating it as a real empty result."""
    delay = 2
    for attempt in range(retries):
        r = client.request(method, path, **kwargs)
        if r.status_code == 200 and len(r.content) == 0:
            if attempt == retries - 1:
                sys.exit(f"Empty response from {path} after {retries} attempts (likely rate-limited). Try again shortly.")
            time.sleep(delay)
            delay *= 2
            continue
        return r
    raise RuntimeError("unreachable")


def fetch_shopping_locations(client):
    global SHOPPING_LOCATIONS_CACHE
    if SHOPPING_LOCATIONS_CACHE is None:
        r = request_with_retry(client, "GET", "/objects/shopping_locations")
        r.raise_for_status()
        SHOPPING_LOCATIONS_CACHE = {d["id"]: d["name"] for d in r.json()}
    return SHOPPING_LOCATIONS_CACHE


def fetch_all_products(client):
    products = {}
    offset = 0
    while True:
        r = request_with_retry(
            client, "GET", "/objects/products",
            params={"limit": 200, "offset": offset},
        )
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        products.update({p["id"]: p["name"] for p in batch})
        offset += 200
    return products


def cmd_locations(args):
    api_url, api_key = resolve_credentials(args)
    client = make_client(api_url, api_key)
    for loc_id, name in sorted(fetch_shopping_locations(client).items()):
        print(f"{loc_id:4} {name}")


def cmd_today(args):
    api_url, api_key = resolve_credentials(args)
    client = make_client(api_url, api_key)
    date = args.date or datetime.date.today().isoformat()

    r = request_with_retry(
        client, "GET", "/objects/stock",
        params={"query[]": f"purchased_date={date}", "limit": 500},
    )
    r.raise_for_status()
    rows = r.json()
    if not rows:
        print(f"No stock entries with purchased_date={date}")
        return

    products = fetch_all_products(client)
    locations = fetch_shopping_locations(client)
    rows.sort(key=lambda d: d["row_created_timestamp"])

    print(f"{'id':>5} {'product':42} {'qty':>4} {'price':>7} {'shop':12} {'best_before':11}")
    for row in rows:
        name = products.get(row["product_id"], f"#{row['product_id']}")
        price = row.get("price")
        shop = locations.get(row.get("shopping_location_id"), "-")
        price_s = f"{price:.2f}" if price is not None else "MISSING"
        print(f"{row['id']:>5} {name[:42]:42} {row['amount']:>4} {price_s:>7} {shop:12} {row.get('best_before_date') or '-':11}")


def cmd_apply(args):
    api_url, api_key = resolve_credentials(args)
    client = make_client(api_url, api_key)
    updates = json.loads(Path(args.updates_file).read_text())

    products = fetch_all_products(client)
    plan = []
    for u in updates:
        entry_id = u["entry_id"]
        r = request_with_retry(client, "GET", f"/objects/stock/{entry_id}")
        if r.status_code != 200:
            print(f"SKIP {entry_id}: could not fetch current row ({r.status_code} {r.text[:120]})")
            continue
        current = r.json()
        if isinstance(current, list):  # some Grocy versions return a 1-item list
            current = current[0]

        # Omitted key AND explicit null both mean "leave unchanged" (dict.get's
        # default only kicks in when the key is absent, so None needs its own check).
        new_price = u["price"] if u.get("price") is not None else current.get("price")
        new_shop = (
            u["shopping_location_id"]
            if u.get("shopping_location_id") is not None
            else current.get("shopping_location_id")
        )

        # Full round-trip: Grocy's PUT /stock/entry/{id} overwrites every field it
        # accepts, including ones you omit (best_before_date, location_id, purchased_date
        # get reset to null if left out). Always resend the current value for anything
        # you don't intend to change.
        body = {
            "amount": current["amount"],
            "open": bool(current.get("open")),
            "best_before_date": current.get("best_before_date"),
            "purchased_date": current.get("purchased_date"),
            "price": new_price,
            "shopping_location_id": new_shop,
        }
        if current.get("location_id") is not None:
            body["location_id"] = current["location_id"]

        plan.append((entry_id, products.get(current["product_id"], f"#{current['product_id']}"), current, body))

    print(f"{'id':>5} {'product':35} {'price old->new':20} {'shop old->new'}")
    locations = fetch_shopping_locations(client)
    for entry_id, name, current, body in plan:
        old_price = current.get("price")
        old_shop = locations.get(current.get("shopping_location_id"), "-")
        new_shop_name = locations.get(body.get("shopping_location_id"), "-")
        price_change = f"{old_price} -> {body['price']}"
        shop_change = f"{old_shop} -> {new_shop_name}"
        print(f"{entry_id:>5} {name[:35]:35} {price_change:20} {shop_change}")

    if not args.apply:
        print(f"\nDRY RUN — {len(plan)} entries would be updated. Re-run with --apply to commit.")
        return

    ok, failed = 0, 0
    for entry_id, name, current, body in plan:
        r = client.put(f"/stock/entry/{entry_id}", json=body)
        if r.status_code == 200:
            ok += 1
        else:
            failed += 1
            print(f"FAILED {entry_id} ({name}): {r.status_code} {r.text[:200]}")
    print(f"\n{ok}/{len(plan)} updated, {failed} failed")


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--grocy-api-url")
    p.add_argument("--grocy-api-key")
    sub = p.add_subparsers(dest="command", required=True)

    sub.add_parser("locations").set_defaults(func=cmd_locations)

    p_today = sub.add_parser("today")
    p_today.add_argument("--date", help="YYYY-MM-DD, default: today")
    p_today.set_defaults(func=cmd_today)

    p_apply = sub.add_parser("apply")
    p_apply.add_argument("--updates-file", required=True)
    p_apply.add_argument("--apply", action="store_true", help="Actually write changes (default: dry-run preview)")
    p_apply.set_defaults(func=cmd_apply)

    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.func(args)
