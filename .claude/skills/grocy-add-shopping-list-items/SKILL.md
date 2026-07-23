---
name: grocy-add-shopping-list-items
description: Use when the user asks to add, insert, or put grocery items onto a Grocy shopping list ("lista della spesa") via the REST API, optionally matching items to existing Grocy products. Covers free-text note items and product-linked items.
---

# Grocy: Add Shopping List Items

## Overview

Adds items to a Grocy shopping list via the REST API. Items can be **free-text notes** (any text, e.g. `"Stracchino (250 g)"`) or **product-linked** (tied to a catalog product). Credentials come from `.env` (`GROCY_API_KEY`, `GROCY_API_URL`).

**Core principle:** add every item as a note first; then, if the user asks, match to existing products by name and link them — keeping the original text in `note` as detail.

## Non-Obvious Facts (read before starting)

- **Auth header is `GROCY-API-KEY: <key>`** — not `Authorization`.
- **Entity name is singular vs plural:**
  - `GET /objects/shopping_lists` → the **lists** (the "Lista della spesa" is **id 1** on this instance).
  - `GET /objects/shopping_list` → the **items** on lists. This is the entity you POST/PUT for items.
- **Query filter operator is `~` with `%` wildcards** (case-insensitive `LIKE`). `∋`/`contains` is rejected with `"Invalid query"`.
- A free-text item is just an item with `product_id: null` and text in `note`.

## Quick Reference

| Action | Method + endpoint |
|--------|-------------------|
| List the shopping lists | `GET /objects/shopping_lists` |
| List items on lists | `GET /objects/shopping_list` |
| Add an item | `POST /objects/shopping_list` |
| Update / link an item | `PUT /objects/shopping_list/{id}` |
| Search products by name | `GET /objects/products?query[]=name~%term%` |

Every request: header `GROCY-API-KEY: $GROCY_API_KEY`. POST/PUT also `Content-Type: application/json`.

## 1. Add items as free-text notes

`POST /objects/shopping_list`:
```json
{ "shopping_list_id": 1, "note": "Stracchino (250 g)", "amount": 1 }
```
Response: `{"created_object_id": <id>}`. Loop one POST per item. Use `jq -nc --arg note "$line" '...'` to build bodies so quotes/unicode (`–`, `'`) survive.

## 2. Match to existing products (only if asked)

The catalog is large (~1000+ products) and names often carry a `[Brand]` suffix. Match by the **generic term**:

1. Strip the trailing quantity annotation: `"Aceto balsamico"` from `"Aceto balsamico"`, `"Zucchine"` from `"Zucchine (2)"`.
2. Search: `GET /objects/products?query[]=name~%<term>%` (curl: `-G --data-urlencode "query[]=name~%aceto%"`).
3. Pick the **shortest / closest** name, or an exact `name=<term>` hit. Beware near-misses that are semantically different (e.g. *Spinacino* ≠ *Spinaci*; raw cut ≠ cooked deli). **When ambiguous or no real match: leave it as a note.**

## 3. Link a matched item to its product

Update the note-item you already created — don't delete it:

`PUT /objects/shopping_list/{item_id}`:
```json
{ "product_id": 495, "qu_id": 3 }
```
- **Keep the original `note`** — it preserves the quantity/detail the product record lacks.
- `qu_id`: use the product's `qu_id_purchase` (fall back to `qu_id_stock`). Get it from the product object.
- **Keep `amount: 1`.** Do NOT push the parenthetical quantity ("250 g", "2") into `amount` — the product's unit is usually a package/piece, so "250" would be wrong. The quantity lives in the note.

Quantity units on this instance: `2`=Pezzo, `3`=Pacco, `4`=Bottiglia, `6`=kg, `7`=g, `8`=l, `11`=ml.

## Common Mistakes

- **Posting to `shopping_lists` (plural)** — that's the lists, not items. Items go to singular `shopping_list`.
- **Using `Authorization` header** — Grocy wants `GROCY-API-KEY`.
- **`∋`/contains query operator** — invalid; use `name~%term%`.
- **Forcing the quantity into `amount`** — keep `amount: 1`, quantity stays in `note`.
- **Accepting a fuzzy name match** — *Spinacino* ≠ *Spinaci*. When unsure, leave as a note and tell the user.
- **Deleting the note to "convert" it to a product item** — instead PUT `product_id`/`qu_id` onto the existing item and keep the note.
