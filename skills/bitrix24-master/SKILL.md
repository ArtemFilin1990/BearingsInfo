---
name: bitrix24-master
description: Use when working with Bitrix24 Cloud, CRM entities, DaData enrichment, REST API, webhooks, custom fields, product cards, catalog imports, duplicate checks, and B2B automation.
---

# Bitrix24 Master Skill

## When to use

Use this skill for:

- Bitrix24 CRM;
- companies, contacts, deals, products and requisites;
- DaData enrichment;
- custom fields and document variables;
- REST API and batch requests;
- duplicate checks;
- catalog import/export;
- automation, robots and business processes.

## Source of truth

1. Current task instruction.
2. Existing repository code and configs.
3. Current Bitrix24 export/API response.
4. Confirmed field map.
5. Official Bitrix24/VibeCode documentation.
6. Assumption only if marked as `requires verification`.

## Hard rules

- Do not invent API methods, field codes, entity IDs, webhook URLs, tokens or automation results.
- Do not expose secrets in code, logs, prompts or documentation.
- Read/list before write.
- For production changes, use dry-run or staging first when possible.
- Do not delete or merge CRM records without explicit task and backup plan.
- For bearing/product data, apply `bearings-catalog` and `xlsx-processing` rules.

## CRM duplicate rule

For company duplicates, prefer `ИНН` as the primary key.

Primary record selection should follow task-specific rules. If no rule is provided:

1. Prefer active responsible user record.
2. Prefer non-duplicate title over `[ДУБЛЬ]`.
3. Prefer newest `DATE_MODIFY` only as fallback.
4. Preserve phones, emails, web, contacts, deals, requisites and activities where possible.

## Workflow

1. Read current repository/config/API schema.
2. Identify target entity and field map.
3. Validate method names against current docs or existing code.
4. Build dry-run plan.
5. Execute only confirmed write actions.
6. Log before/after data.
7. Return verification commands or checks.

## Output pattern

```text
РЕШЕНИЕ
ШАГИ
КОД/КОНФИГ
ПРОВЕРКА
РИСКИ
АЛЬТЕРНАТИВА
```

## Validation checklist

- no secrets committed;
- no invented field names;
- write actions isolated;
- rollback or backup considered;
- API responses checked;
- product/catalog logic did not break bearing rules.
