---
name: legal-contracts-everest
description: Use when drafting, reviewing, strengthening, or comparing supply contracts, specifications, protocols of disagreement, claims, letters, and legal documents for ООО «Эверест».
---

# Legal Contracts Everest Skill

## When to use

Use this skill for:

- supply contracts;
- specifications;
- protocols of disagreement;
- claims and letters;
- contract risk review;
- supplier-side legal wording for ООО «Эверест»;
- document generator variables and legal templates.

## Position

Unless the task says otherwise, work in the interest of ООО «Эверест» as supplier.

## Source of truth

1. Current task instruction.
2. Uploaded contract/template/specification.
3. Confirmed company and counterparty data.
4. Existing legal template.
5. Current law only after verification.
6. Assumption only if marked as `requires verification`.

## Hard rules

- Do not invent dates, amounts, реквизиты, names, positions, bank details, authorities, addresses, tax numbers or signatures.
- Do not weaken strong supplier-side clauses unless explicitly requested.
- Do not add legal facts without source.
- Do not use placeholders unless the task allows them.
- If data is missing, leave blank or mark status according to task.

## Clauses to protect

Strengthen or preserve:

- payment;
- delivery terms;
- acceptance procedure;
- quality and claims;
- documents;
- liability;
- jurisdiction;
- force majeure;
- unilateral changes and delays;
- ownership transfer and risk transfer.

## Risk format

Use:

```text
If X → then Y → close it this way: Z.
```

For Russian legal output:

```text
Если X → то Y → закрыть так: Z.
```

## Protocol of disagreements format

```text
Редакция контрагента:
...

Предлагаемая редакция:
...

Причина:
...
```

## Workflow

1. Read the source document first.
2. Determine side: supplier or buyer.
3. Identify missing confirmed data.
4. Check payment, delivery, acceptance, liability and jurisdiction.
5. Strengthen supplier-side clauses.
6. Mark risks and unknowns.
7. Return ready-to-use wording or change log.

## Validation checklist

- no invented legal facts;
- supplier position preserved;
- payment risk controlled;
- delivery and acceptance clear;
- liability not excessive for supplier;
- unknown data marked;
- output is ready to insert into document.
