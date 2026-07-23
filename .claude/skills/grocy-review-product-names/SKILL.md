---
name: grocy-review-product-names
description: Use when the user asks to review, clean up, or normalize Grocy product names from an exported products CSV. Applies when product names contain embedded brand names that should be separated into the format "<generic product> [<brand>]".
---

# Grocy: Review Product Names

## Overview

Drives the full loop with the `grocy-tools` CLI: **export** products to a CSV, detect brand names embedded in product names, rewrite them as `<generic product> [<brand>]`, **show the delta to the user**, and **import** the reviewed CSV back into Grocy. Rows with no detectable brand are left unchanged.

Always use the CLI for the export and import steps — never call the Grocy API directly. Never run the final import until the user has seen the delta and confirmed.

Write all CSV files into the `out/` directory (create it if missing) — e.g. `out/products.csv` and `out/reviewed_products.csv`. `out/` is gitignored, so these working files stay untracked.

The CLI needs `--grocy-api-url` and `--grocy-api-key`. Resolve them in this order before running any command:

1. **Check `.env`** in the repo root for `GROCY_API_URL` and `GROCY_API_KEY` (load with `set -a; . ./.env; set +a`).
2. Fall back to the `$GROCY_API_URL` / `$GROCY_API_KEY` / `$GROCY_HOST` environment variables.
3. If still missing, ask the user.

Never print the API key.

## Target Format

```
<generic product name> [<Brand>]
```

Examples:
| Before | After |
|--------|-------|
| `Gullon Zero Zuccheri Fibra` | `Zero Zuccheri Fibra [Gullon]` |
| `Latte Di Nocciola (Alpro)` | `Latte Di Nocciola [Alpro]` |
| `Panna Chef Leggera` | `Panna Leggera [Chef]` |
| `Orzo Da Cuocere Lidl` | `Orzo Da Cuocere [Lidl]` |
| `Besciamella Leggera` | *(unchanged — no brand)* |

## Brand Detection Rules

Apply these in order. Stop at first match.

1. **Existing parenthetical** — name contains `(Brand)` or `[Brand]` anywhere → extract it, rewrite as `<rest> [Brand]`. Strip trailing/leading whitespace from the generic part.

2. **Brand at start** — first word(s) are a manufacturer/company name and the rest describes the product → move brand to end as `[Brand]`. Most common pattern in Italian products (e.g. *Gullon*, *Barilla*, *Mulino Bianco*).

3. **Brand at end** — last word is a retailer or manufacturer that doesn't describe the product (e.g. *Lidl*, *Coop*, *Esselunga*, *Scotti*) → keep generic part, append `[Brand]`.

4. **Brand in middle** — a known brand word appears mid-name surrounded by generic descriptors (e.g. `Panna Chef Leggera`) → remove it from position, append `[Brand]`.

5. **No brand found** → skip. Do not modify the name.

## What Counts as a Brand

Use judgment. A brand is a **company or manufacturer name**, not a product descriptor.

**Is a brand:** Gullon, Alpro, Chef, Lidl, Coop, Barilla, Mutti, Scotti, De Cecco, Mulino Bianco, Ferrero, Activia, Danone, Lidl, Esselunga, Valfrutta, San Benedetto

**Is NOT a brand:** Leggera (light), Zero (diet/zero sugar), Biologico (organic), Integrale (whole grain), Bottiglia (bottle type), Piccante (spicy), Classico (classic), Di/Del/Della/Dei (prepositions), size descriptors

When uncertain → skip (don't modify).

## Process

Run the steps in order. Do not skip the export or the delta confirmation.

**1. Export via the CLI.** Never read products straight from the API — always go through the CLI so the on-disk format matches what `import-products` expects.

```bash
uv run grocy-tools export-products --grocy-api-url $URL --grocy-api-key $KEY -f out/products.csv
```

**2. Review names.** Read `out/products.csv` (columns: `id`, `name`; there may be more columns in the future — preserve them all). For each row, apply the brand detection rules above.

**3. Build the reviewed CSV.** Write a new CSV (`out/reviewed_products.csv`) with the same columns. For unchanged rows, copy the original values exactly.

**4. Show the delta to the user — STOP and confirm.** Before importing anything, print every proposed rename and wait for explicit approval:

```
id  42: "Gullon Zero Zuccheri Fibra" -> "Zero Zuccheri Fibra [Gullon]"
id  87: "Latte Di Nocciola (Alpro)" -> "Latte Di Nocciola [Alpro]"
...
N renames proposed, M rows unchanged.
```

Do not run step 5 or 6 until the user confirms. If there are zero renames, say so and stop.

**5. Dry-run the import.** After confirmation, preview the changes the CLI itself would make (this is the delta from Grocy's live state):

```bash
uv run grocy-tools import-products --grocy-api-url $URL --grocy-api-key $KEY \
  -f out/reviewed_products.csv --dry-run
```

**6. Apply the import.** Only after the dry-run looks correct, run the real import:

```bash
uv run grocy-tools import-products --grocy-api-url $URL --grocy-api-key $KEY \
  -f out/reviewed_products.csv
```

## Common Mistakes

- **Over-aggressively detecting brands** — "Roma" in "Riso Superfino Roma" is a variety name, not a brand. When in doubt, skip.
- **Stripping part of the product name** — the generic part must remain meaningful. `Panna Chef Leggera` → `Panna Leggera [Chef]`, not just `Panna [Chef]`.
- **Double-bracketing** — if the name is already in the correct `<name> [Brand]` format, do not modify it.
- **Changing capitalisation** — preserve the original capitalisation of both the generic part and the brand.
