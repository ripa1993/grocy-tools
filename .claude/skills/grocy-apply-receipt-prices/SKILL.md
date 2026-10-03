---
name: grocy-apply-receipt-prices
description: Use when the user has already logged today's grocery purchases into Grocy (with expiry dates, no prices) and now provides a receipt export (markdown or text, one or more stores) to backfill the real per-item price and shopping location onto those stock entries.
---

# Grocy: Apply Receipt Prices

## Overview

Grocy's Android app auto-fills a stock entry's price with "last known price," which is usually wrong. This skill reconciles that day's stock entries against the real receipt(s) and writes back the correct `price` and `shopping_location_id` — after showing the user a full before/after diff and getting explicit confirmation.

Use `scripts/grocy_stock.py` for all reads/writes — it already handles the gotchas below. Never hand-roll the PUT call.

## Process

1. **Resolve credentials** — `.env` in repo root (`GROCY_API_URL`/`GROCY_API_KEY`), else env vars, else ask.
2. **List today's stock entries**: `uv run python scripts/grocy_stock.py today [--date YYYY-MM-DD]`. Gives entry id, product name, qty, current price, current shop, best-before.
3. **List shopping locations** (once, to map store name → id): `uv run python scripts/grocy_stock.py locations`.
4. **Read the receipt file(s)** the user gave you. Each store is usually its own section/table; extract `(item name, price)` pairs.
5. **Match each Grocy entry to a receipt line** by product name (fuzzy — receipt names are abbreviated, Grocy names may have `[Brand]` suffixes or be more generic, Italian abbreviations are common e.g. "EVO" = Extravergine Oliva). For a receipt line marked `(N pz)`, divide by N to get the per-unit price matching Grocy's `amount` field, *unless* Grocy's `amount` for that product is 1 and the pack is tracked as a single package (e.g. a bag of potatoes, bio produce sold as one punnet) — then use the pack total as-is. Round divided prices to 2 decimals (standard rounding); don't invent extra precision Grocy won't store. Receipts use Italian comma decimals (`3,60`) — convert to dot (`3.60`) before writing JSON. When several stock-log entries for the same product share a `stock_id`, Grocy already merged them into one stock row with summed `amount`; treat it as one row.
   - **Use elimination as a confidence booster**: once a store section's unambiguous pairs are matched, a leftover Grocy entry and a leftover receipt line in the same section are very likely each other's match even if the name overlap is weak — but still surface the reasoning, don't present it as a sure thing.
6. **Flag anything that doesn't match cleanly** — do not guess silently:
   - A Grocy entry with no corresponding receipt line (ask: wrong product match? item not scanned by the cashier?).
   - A receipt line with no corresponding Grocy entry (fine — likely a non-tracked item like toiletries/drinks; no action needed).
   - A receipt amount with an ambiguous pack/unit split (e.g. a `qty=2` Grocy entry but the receipt doesn't say "(2 pz)" — ask whether the price is the total or per-unit).
   - **A Grocy entry whose current `shopping_location_id` names a different store than the receipt section it matched to** — this is exactly the kind of autofill error this skill exists to fix, but flipping the store is a bigger change than filling in a missing price; confirm with the user rather than overwriting silently.
   - **A receipt section whose store has no matching row in `locations`** — don't create a new `shopping_location` yourself; ask the user whether to create one or map it to an existing entry.
7. **Show the full diff and STOP for confirmation** — one row per entry: product, price old → new, shop old → new. Do not proceed to step 8 until the user confirms (and has answered any flags from step 6).
8. **Dry-run then apply**:
   ```bash
   uv run python scripts/grocy_stock.py apply --updates-file updates.json          # preview
   uv run python scripts/grocy_stock.py apply --updates-file updates.json --apply  # commit
   ```
   `updates.json` is a list of `{"entry_id": ..., "price": ..., "shopping_location_id": ...}` (either field optional/null to leave unchanged).
9. **Verify**: re-run `today` and confirm prices/shops match the plan, and that `best_before` dates are unchanged from step 2. `today`'s table doesn't show `purchased_date`/`location_id` — if you need to check those too (e.g. after hand-rolling a request instead of using the script), re-fetch `/objects/stock/{id}` and diff the full row against your step-2 snapshot.

## Critical Gotcha: Grocy's PUT overwrites omitted fields

`PUT /stock/entry/{id}` is **not** a partial patch. Any field you don't send — `best_before_date`, `purchased_date`, `location_id` — gets reset to null, silently destroying data the user entered this morning. `scripts/grocy_stock.py apply` already fetches the current row and round-trips every field; if you ever write a raw request yourself, always `GET /objects/stock/{id}` first and resend every field, not just the ones you're changing.

`amount` and `open` are also required by the endpoint even when unchanged — omitting `amount` gives a 400, omitting `open` gives a 500 (`BoolToInt(): ... null given`).

## Other Gotchas

- **`.env`'s `GROCY_API_URL` may already end in `/api`** — check it before concatenating a path, or you'll get a 404 or a silently-doubled `/api/api/...` (Grocy tolerates the latter, but don't rely on it).
- **Empty 200 responses = rate limiting**, not "no data" or auth failure. The script retries with backoff; if you query the API by hand and get a zero-byte 200 body, wait a few seconds and retry rather than concluding the endpoint is broken.
- **Don't guess brand/variant matches silently** — "Code Di Mazzancolle" ↔ "Gamberi Timone" or "Formaggio Grattuggiato" ↔ "Mix formaggi duri 100% ITA" are the kind of lower-confidence matches to call out in the diff, not just apply.

## Example updates.json

```json
[
  {"entry_id": 3190, "price": 3.79, "shopping_location_id": 2},
  {"entry_id": 3198, "price": null, "shopping_location_id": 2},
  {"entry_id": 3208, "price": 1.11, "shopping_location_id": 2}
]
```

(`3198`'s `price: null` and simply omitting the key are equivalent — both leave the current price untouched.)
