---
name: bearings-catalog
description: Use when working with bearing catalogs, GOST/ISO mapping, bearing designation parsing, suffixes, analog verification, dimensions, mass, product cards, and technical reference data.
---

# Bearings Catalog Skill

## When to use

Use this skill for:

- bearing designation normalization;
- GOST / ISO / DIN / ANSI mapping;
- analog verification;
- prefix, base number, suffix parsing;
- dimensions `d`, `D`, `B/T`;
- mass and technical characteristics;
- catalog tables, product cards and reference data;
- preparation of data for database, CRM, API or website.

## Source of truth

1. Current task instruction.
2. Source table, PDF, DOCX, CSV, XLSX or database export.
3. Repository files under `data/`, `docs/`, `sources/`.
4. Confirmed manufacturer catalog or standard.
5. Project rules in this skill.
6. Assumption only if marked as `requires verification`.

## Hard rules

- Do not invent dimensions, mass, analogs, brands, suffixes, standards, source links or verification results.
- Analog is allowed only when type, series, geometry, execution, prefix, suffix and critical marks match.
- Do not treat similar numbers as direct equivalents.
- If direct equivalent is not confirmed, write `NO DIRECT EQUIV`.
- Do not transfer mass unless brand and execution match exactly.
- Do not change bearing designation formatting without a rule.
- Keep original source designation in a separate field when normalizing.

## Critical marks

Always preserve and compare:

- seals/shields: `ZZ`, `2Z`, `Z`, `2RS`, `RS`, `2RS1`, `DU`, `DDU`;
- clearance: `C2`, `C3`, `C4`, `C5`;
- tapered bore: `K`, `K30`;
- snap ring/groove: `N`, `NR`;
- precision: `P6`, `P5`, `P4`, `P2`, `ABEC`;
- cage/material: `M`, `MA`, `MB`, `TN`, `TN9`, `TVP`, `TVP2`, `E`;
- cylindrical roller types: `N`, `NU`, `NJ`, `NUP`, `NF`, `RNU`;
- angular contact / four-point: `QJ`, `AC`, `B`, `C` where applicable.

## ISO parsing rules

- `QJ`, `NU`, `NJ`, `NUP`, `N`, `NF`, `RNU` at the start of an ISO designation are part of the base ISO number, not a prefix.
- Examples of base ISO numbers: `QJ205`, `NU205`, `NJ205`, `NUP308`, `N205`, `NF208`, `RNU310`.
- Do not write `NJ-205`; write `NJ205`.
- `ISO prefix` is only a separate manufacturer or execution prefix before the base designation.
- `ISO suffix` is the part after the base number: `C3`, `C4`, `MA`, `M`, `E`, `TVP2`, `TN9`, `P6`, `2RS`, `ZZ`.
- Full ISO designation = `ISO number` + space + `ISO suffix`, if suffix exists.

## GOST parsing rules

- Preserve original GOST designation.
- Add hyphen after GOST prefix only when the source/rule requires it, for example `6-180204`.
- Do not infer GOST prefix from approximate match.
- Keep GOST and ISO fields separate unless the output explicitly requires a merged field.

## Analog verification logic

A direct analog requires all of the following:

1. Same bearing type.
2. Same dimensional series and geometry.
3. Same dimensions `d/D/B` or `d/D/T`.
4. Same execution and modification.
5. Same seals/shields.
6. Same clearance where relevant.
7. Same precision class where relevant.
8. Same cage/material where relevant.
9. No conflicting suffixes.

If any item is unknown, status is `requires verification`, not confirmed analog.

## Workflow

1. Read the source file or repository files first.
2. Identify the source of truth.
3. Preserve the original designation.
4. Parse prefix / base number / suffix.
5. Normalize only confirmed fields.
6. Verify dimensions and mass from trusted source.
7. Verify analogs using strict criteria.
8. Mark missing fields as empty, `NO DIRECT EQUIV`, or `requires verification` according to task rules.
9. Return output and change log.

## Output fields recommended

```text
brand
product_type
category
prefix
number
suffix
full_designation
original_designation
alternative_designations
gost_prefix
gost_number
gost_suffix
gost_full_designation
iso_prefix
iso_number
iso_suffix
iso_full_designation
d_mm
D_mm
B_T_mm
m_kg
analog_status
source
verification_status
notes
```

## Validation

Before final output check:

- no invented dimensions;
- no approximate analogs marked as direct;
- suffixes preserved;
- QJ/NU/NJ/NUP/N not split as prefixes;
- source fields preserved;
- table structure not broken;
- all unknowns clearly marked.
