---
name: docx-processing
description: Use when creating, editing, formatting, validating, or cleaning DOCX documents, including reports, technical tasks, contracts, applications, manuals, and formal business documents.
---

# DOCX Processing Skill

## When to use

Use this skill for:

- reports and доклады;
- technical specifications;
- contracts and appendices;
- FRP / fund application documents;
- manuals and formal documents;
- cleaning document style and structure.

## Source of truth

1. Current user instruction.
2. Source DOCX file.
3. Attached data/tables/specifications.
4. Project rules.
5. General knowledge only for neutral drafting.

## Hard rules

- Preserve document structure unless the task requires redesign.
- Do not insert unknown dates, sums, names, requisites or legal facts.
- Do not use colored styling for formal documents unless requested.
- Do not remove sections without a change log.
- Keep tables readable and simple.
- For legal documents, apply `legal-contracts-everest` rules.
- For bearing tables, apply `bearings-catalog` rules.

## Workflow

1. Read the source document first.
2. Identify document purpose and recipient.
3. Preserve useful structure.
4. Remove visual noise and inconsistent formatting.
5. Fill only confirmed data.
6. Mark unknowns as empty or `[[TBD]]` only if placeholders are allowed.
7. Render/check the final document visually.
8. Return final file and change log.

## Formal style

Use:

- clear headings;
- simple tables;
- black/graphite text;
- restrained formatting;
- no decorative colors;
- no marketing noise.

## Change log format

```text
section
old_value
new_value
reason
status
```

## Validation checklist

- document opens correctly;
- headings consistent;
- tables are not broken;
- no unconfirmed values inserted;
- no unwanted colors/noise;
- result is ready for sending or review.
