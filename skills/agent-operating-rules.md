# Agent Operating Rules

## Purpose

These rules define how an AI agent should use the `skills/` package inside `BearingsInfo`.

## Skill selection

Use only the skill that matches the current task:

- Bearing data → `bearings-catalog`.
- Excel/CSV → `xlsx-processing`.
- PDF sources → `pdf-processing`.
- DOCX documents → `docx-processing`.
- B2B copy and website text → `everest-b2b-content`.
- Bitrix24/CRM/API → `bitrix24-master`.
- Contracts and legal text → `legal-contracts-everest`.

If multiple skills apply, use the smallest necessary set. Do not mix unrelated project rules.

## Read before write

Before modifying files:

1. Read the existing file.
2. Identify the exact target section.
3. Make the smallest necessary change.
4. Preserve formatting and structure where possible.
5. Return a change log.

## No hallucinated data

Never invent:

- bearing dimensions;
- bearing mass;
- analogs;
- suffix meaning;
- standards;
- prices;
- stock availability;
- company details;
- Bitrix24 field codes;
- API methods;
- legal facts;
- source links;
- test results.

If the value is not confirmed, mark it as:

```text
requires verification
```

or leave it empty when the task requires blank fields.

## Change log required

For every file/table/document change provide:

```text
file
section_or_row
old_value
new_value
reason
status
```

## Completion criteria

A task is complete only when:

- the result is directly usable;
- modified files are listed;
- validation steps are provided;
- risks and unknowns are explicit;
- no unrelated project rules were applied.
