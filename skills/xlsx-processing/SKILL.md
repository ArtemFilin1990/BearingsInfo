---
name: xlsx-processing
description: Use when processing Excel, CSV, price lists, bearing catalogs, database exports, duplicate checks, table normalization, and spreadsheet validation.
---

# XLSX / CSV Processing Skill

## When to use

Use this skill for:

- Excel and CSV catalogs;
- price lists;
- bearing tables;
- product imports and exports;
- duplicate detection;
- column validation;
- table normalization;
- preparing data for CRM, ERP, database or website.

## Source of truth

1. Current task instruction.
2. Uploaded spreadsheet or repository table.
3. Existing schema or README in `data/`, `docs/`, `src/`, `tools/`.
4. Rules from `bearings-catalog` when rows contain bearings.
5. Assumption only if explicitly marked.

## Hard rules

- Do not rename columns unless required by the task.
- Do not delete rows without a change log.
- Do not merge cells.
- Do not fill missing technical data without confirmed source.
- Do not break articles, bearing designations, brand names or suffixes.
- Do not convert identifiers to numbers if leading zeros or symbols matter.
- Preserve original values when creating normalized fields.

## Safe duplicate keys

Use only confirmed keys:

- `ИНН` for companies;
- `article` / `артикул` for exact product rows;
- `brand + article`;
- `designation + brand`;
- `GOST + ISO + dimensions`;
- task-specific key provided by the user.

If no safe key exists, do not merge automatically. Mark as `potential duplicate`.

## Bearing table rules

When the table contains bearings, apply `bearings-catalog` rules:

- analog only after strict verification;
- no approximate analogs;
- preserve suffixes;
- `QJ`, `NU`, `NJ`, `NUP`, `N`, `NF`, `RNU` remain inside ISO number;
- dimensions and mass require source confirmation.

## Workflow

1. Read headers and sample rows.
2. Detect file purpose and source of truth.
3. Identify required output columns.
4. Preserve raw fields.
5. Normalize only task-relevant fields.
6. Validate duplicates using safe keys.
7. Create change log.
8. Return processed file/table and validation notes.

## Change log format

```text
row
column
old_value
new_value
reason
status
```

## Validation checklist

- headers unchanged unless requested;
- row count preserved unless deletion/merge requested;
- no invented values;
- empty cells are not silently filled;
- numeric/text identifiers preserved;
- formulas and formats not damaged;
- changes documented.
