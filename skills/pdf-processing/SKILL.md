---
name: pdf-processing
description: Use when extracting, checking, rendering, OCR-processing, or validating PDF catalogs, manuals, datasheets, standards, invoices, and technical source documents.
---

# PDF Processing Skill

## When to use

Use this skill for:

- PDF catalogs and datasheets;
- manufacturer manuals;
- standards and scanned documents;
- extracting bearing tables;
- verifying dimensions, mass, suffixes and technical descriptions;
- converting PDF content into Markdown, CSV, JSON or knowledge base chunks.

## Source of truth

1. The PDF itself.
2. Page image/render when layout, tables, figures or scans matter.
3. Extracted text only after visual verification when the PDF is complex.
4. Repository rules and schemas.
5. External source only if explicitly required.

## Hard rules

- Do not trust extracted text blindly when the PDF contains tables, scans, diagrams or multi-column layout.
- Do not invent values from incomplete OCR.
- Do not silently fix unclear text.
- Keep page references for extracted facts.
- For bearing data, apply `bearings-catalog` analog and suffix rules.

## Workflow

1. Identify PDF type: text PDF, scanned PDF, mixed, table-heavy, diagram-heavy.
2. Extract text.
3. Render relevant pages for visual inspection.
4. Extract tables with page references.
5. Mark low-confidence OCR values.
6. Normalize only confirmed fields.
7. Return output with source page references.

## Output requirements

For extracted facts include:

```text
value
field
page
source_fragment
confidence
notes
```

## Validation checklist

- relevant pages rendered or visually checked;
- tables verified against layout;
- OCR errors marked;
- no page references missing for important extracted facts;
- unclear values marked `requires verification`.
