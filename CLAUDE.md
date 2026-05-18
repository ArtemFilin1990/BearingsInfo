# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

BearingsInfo is a Russian-language bearing (подшипник) knowledge base and data pipeline. It has two distinct parts:

1. **Data layer** — structured CSVs in `data/` (nomenclature, brands, analogs) validated against YAML schemas in `data/schemas/`.
2. **Processing pipeline** — Python code in `src/` that watches an inbox directory, parses incoming CSV/XLSX files, normalises bearing records, deduplicates them, and writes an output catalog. A FastAPI search API is layered on top in `src/api/`.

## Common Commands

```bash
# Install production dependencies
make install

# Install dev dependencies + pre-commit hooks
make install-dev

# Run all tests
pytest -v

# Run a single test file
pytest tests/test_processor.py -v

# Run a single test by name
pytest tests/test_processor.py::test_name -v

# Lint (ruff + mypy + black check)
make lint

# Auto-format
make format

# Deduplicate data/nomenclature.csv (required before commits touching it)
python tools/scripts/deduplicate_nomenclature.py

# Normalize all datasets (sort + dedup via schemas)
python tools/scripts/update_repo.py --no-report

# Validate all CSV files against schemas
python tools/scripts/validate/run_validations.py

# Full local CI pass (lint + test + validate)
make ci

# Run the processing pipeline (watch mode — monitors inbox/)
python -m src.cli watch

# Process existing files in inbox/ once and exit
python -m src.cli once

# Rebuild the output catalog from already-processed files
python -m src.cli rebuild

# Start the FastAPI search server
cd src/api && uvicorn main:app --reload

# manage.py convenience wrapper (validate / normalize / test / sources)
python manage.py test
python manage.py validate
python manage.py normalize
```

## Architecture

### Data pipeline (`src/`)

The pipeline follows a strict inbox → processed/error → out flow:

```
inbox/          (drop raw CSV/XLSX here)
    ↓  FileProcessor.process_file()
processed/      (successfully handled files, renamed with hash + row count)
error/          (files that failed parsing)
    ↓  CatalogManager.add_records()
out/catalog_target.csv   (deduplicated master catalog)
out/catalog_target.json
out/processed_registry.json  (Registry — sha256 → metadata, prevents reprocessing)
out/run_report.ndjson    (per-run audit log)
```

Key classes and their responsibilities:

| Class | File | Role |
|---|---|---|
| `Config` | `src/config.py` | Loads and strictly validates `config/app.yaml`, `config/brand_aliases.json`, `config/parsing_rules.json`. Raises `ConfigValidationError` on any schema mismatch. |
| `FileProcessor` | `src/processor.py` | Orchestrates the full lifecycle for one file: size check → hash → registry lookup → parse → normalise → catalog merge → move → registry update → report. |
| `DataParser` | `src/parser.py` | Reads CSV/XLSX via pandas; maps columns using `config/parsing_rules.json`; normalises text, dimensions, brands. |
| `CatalogManager` | `src/catalog.py` | Merges new records into the master catalog; detects dimension conflicts; outputs CSV + JSON atomically. Target schema columns: `Наименование, Артикул, Аналог, Бренд, D, d, H, m`. |
| `Registry` | `src/registry.py` | JSON-backed map of `sha256 → {status, n_records, …}`. Prevents duplicate processing; controlled by `registry.allow_reprocess_errors` config key. |
| `InboxWatcher` | `src/watcher.py` | Drives the `watch` mode using either `watchdog` (event-based) or a polling loop. |

### FastAPI search layer (`src/api/`)

`src/api/main.py` is the uvicorn entry point. It wraps the router defined in `src/api/app/api.py`. Key endpoints:

- `GET /autocomplete?q=…` — prefix search over bearing codes, brands, series
- `GET /search?q=…` — full-text search via `DocumentSearchEngine`
- `GET /similar/{document_id}` — find similar bearings
- `GET /search/export` — download search results as CSV/JSON

The engines (`AutocompleteEngine`, `DocumentSearchEngine`, `SearchHistory`) live in `src/api/app/logic.py` and load data from the catalog files at startup.

### Data validation (`tools/scripts/validate/`)

`run_validations.py` calls `csv_validator.py`, which reads YAML schemas from `data/schemas/` and validates every CSV file listed there. Schemas define required columns, types, uniqueKey, and sort_by. The CI pipeline runs this after every normalization step.

### Configuration files (`config/`)

| File | Purpose |
|---|---|
| `config/app.yaml` | Runtime settings: inbox/processed/error/out paths, watcher mode (`poll`/`watch`), file size limits, normalization rules, logging, registry path |
| `config/brand_aliases.json` | Maps variant brand spellings to canonical form (e.g. `"ГПЗ" → "10-ГПЗ"`) |
| `config/parsing_rules.json` | Column name aliases for incoming files, regex patterns for dimension extraction, required field policy |

All three files are validated at startup by `Config._validate_*` methods — invalid configs abort immediately with a descriptive message.

## Data Conventions

- `data/nomenclature.csv` is the primary dataset. Unique key is `(Brand, Product Name)`. Always run `python tools/scripts/deduplicate_nomenclature.py` after editing it — the pre-commit hook enforces this automatically.
- All CSV files use UTF-8 encoding, comma delimiter, no BOM.
- Brand names should match the canonical forms in `config/brand_aliases.json`.
- Technical data must cite a source standard (ГОСТ, ISO, DIN) per `AGENT.md`.
- Dimensions use `.` as the decimal separator; `×`, `х` (Cyrillic), `–`, `—`, `−` are all normalised to `x` and `-` respectively.

## Code Style

- Line length: 120 characters (black + ruff).
- Target Python: 3.11+.
- Linters: `ruff` (E, F, I, N, W, UP rules) + `mypy` + `black`. Run `make lint` before committing.
- `__init__.py` F401 (unused import) is suppressed by ruff config.
- Tests live in `tests/`, follow `test_*.py` / `Test*` / `test_*` naming. `conftest.py` provides `repo_root`, `data_dir`, and `schemas_dir` fixtures.
- Coverage is tracked for `tools/scripts` and `src/sources`.

## CI

GitHub Actions runs on every push/PR (`.github/workflows/ci.yml`):

1. Deduplicate nomenclature
2. Normalize datasets (`update_repo.py --no-report`)
3. Check for duplicate keys in `nomenclature.csv`
4. Validate all CSVs against schemas
5. Run `pytest` (Python 3.11 and 3.12 matrix)

Pre-commit hooks (`.pre-commit-config.yaml`) enforce trailing-whitespace, YAML/JSON validity, large-file guard (5 MB), black, ruff, deduplication, and CSV validation locally on every commit.
