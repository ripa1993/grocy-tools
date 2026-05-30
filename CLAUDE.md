# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv sync                          # install / reconcile dependencies
uv run grocy-tools --help        # list CLI commands
uv run grocy-tools bulk-image \
  --grocy-api-key $GROCY_API_KEY \
  --grocy-api-url https://$GROCY_HOST/api
uv run grocy-tools sanitize --dry-run \
  --grocy-api-key $GROCY_API_KEY \
  --grocy-api-url https://$GROCY_HOST/api
uv add <pkg>                     # add dependency (updates pyproject.toml + uv.lock)
uv remove <pkg>
```

No test suite exists yet. Linting via ruff (line-length 120, rules F/I/UP) but ruff is not in the project deps — install separately if needed (`uv tool install ruff`).

## Architecture

The repo has two top-level packages in a flat layout:

**`grocy_rest_api_client/`** — auto-generated OpenAPI client for the Grocy REST API (via `openapi-python-client`). Treat it as read-only generated code; regenerate rather than hand-edit. Provides `Client`, `AuthenticatedClient`, and typed models/API functions used throughout `grocy_tools`.

**`grocy_tools/`** — the actual application logic:

- `cli.py` — Click entry point (`grocy-tools` console script). Constructs services and wires them into orchestrators.
- `grocy/service.py` — thin wrapper over `grocy_rest_api_client`; all Grocy API calls go through `GrocyService`.
- `image_sources/__init__.py` — `ImageSourceInterface` with a single method `find_image_url(barcode, name) -> str | None`. All image providers implement this.
- `openfoodfacts/service.py` — `OpenFoodFactsService(ImageSourceInterface)`: barcode lookup with 2 s base delay and exponential backoff on 429s (up to 5 attempts).
- `duckduckgo/service.py` — `DuckDuckGoImageService(ImageSourceInterface)`: name-based image search via `ddgs`; used as fallback when OFF has no match.
- `orchestration/bulk_image_import.py` — `BulkImageImport` takes a `list[ImageSourceInterface]` and tries each source in order (OFF first, DDG second). Works with or without barcodes.
- `orchestration/bulk_renamer.py` — `BulkRenamer`: normalises product names (title-case, strips/relocates brand names to `[Brand]` suffix, applies `known_replacements`).
- `orchestration/constants.py` — `brands` list and `known_replacements` dict that drive the renamer rules.

## Adding a new image source

1. Create `grocy_tools/<source>/service.py` implementing `ImageSourceInterface.find_image_url`.
2. Add the source to the `sources` list in `cli.py` `bulk_image`.

## `grocy_rest_api_client` regeneration

The client is generated from the Grocy OpenAPI spec. To regenerate:
```bash
uvx openapi-python-client update --path <openapi-spec.json>
```
