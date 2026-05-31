import csv
import sys
from abc import ABCMeta

import click

FIELDS = ["id", "name"]  # extend here to add more exportable/editable columns


class ProductsCsvInterface(metaclass=ABCMeta):
    def run_export(self, path: str) -> None:
        raise NotImplementedError

    def run_import(self, path: str, dry_run: bool = False) -> None:
        raise NotImplementedError


class ProductsCsv(ProductsCsvInterface):
    def __init__(self, grocy_svc):
        self.grocy_svc = grocy_svc

    def run_export(self, path: str) -> None:
        with open(path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
            writer.writeheader()
            count = 0
            for product in self.grocy_svc.get_products():
                writer.writerow({f: getattr(product, f, "") for f in FIELDS})
                count += 1
        click.echo(f"Exported {count} products to {path}")

    def run_import(self, path: str, dry_run: bool = False) -> None:
        live = {p.id: p for p in self.grocy_svc.get_products()}

        updated = unchanged = not_found = errors = 0

        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            update_columns = [f for f in (reader.fieldnames or []) if f != "id"]

            for row in reader:
                pid = int(row["id"])
                if pid not in live:
                    click.echo(f"id {pid} not found in Grocy, skipping", err=True)
                    not_found += 1
                    continue

                product = live[pid]
                changes = {
                    f: row[f]
                    for f in update_columns
                    if str(getattr(product, f, "")) != row[f]
                }

                if not changes:
                    unchanged += 1
                    continue

                for field, new_val in changes.items():
                    old_val = getattr(product, field, "")
                    click.echo(f"{pid}: {field} '{old_val}' -> '{new_val}'")

                if dry_run:
                    updated += 1
                    continue

                for field, new_val in changes.items():
                    setattr(product, field, new_val)

                res = self.grocy_svc.update_product(product)
                if res:
                    click.echo(f"Product {pid} not updated due to {res}", err=True)
                    errors += 1
                else:
                    updated += 1

        label = "would update" if dry_run else "updated"
        click.echo(
            f"{label}: {updated}  unchanged: {unchanged}  "
            f"not_found: {not_found}  errors: {errors}"
        )
