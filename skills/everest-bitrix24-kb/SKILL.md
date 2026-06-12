---
name: everest-bitrix24-kb
description: Use when creating, editing, validating, generating, or importing the Bitrix24 knowledge base 2.0 named «Технический справочник “Эверест”» for bearings, GOST/ISO, analogs, brands, operation, related products, catalogs, and tables.
---

# Everest Bitrix24 Knowledge Base Skill

## When to use

Use this skill for tasks touching `knowledge-base/everest/`, Bitrix24 knowledge-base imports for ООО «Эверест», or the content structure named `Технический справочник «Эверест»`.

## Source of truth

1. Current user request.
2. `knowledge-base/everest/source/sections.json` and `knowledge-base/everest/source/articles.json`.
3. `knowledge-base/everest/scripts/validate-knowledge-base.py`.
4. Repository instructions and tests.
5. Confirmed official catalogs, ГОСТ / ISO documents, Bitrix24 configuration, or operator-provided exports.

## Non-negotiable content rules

- Preserve all 8 section numbers and section titles.
- Preserve all subsection numbers and article titles.
- One subsection equals one article; never merge separate topics.
- Keep Russian titles.
- Use a concise technical business style: no advertising, hype, or unsupported claims.
- Do not invent ГОСТ numbers, ISO mappings, dimensions, loads, clearances, prices, brands, countries, ТН ВЭД codes, API methods, field IDs, webhook URLs, or credentials.
- Mark incomplete facts with statuses: `нет данных`, `уточнить`, `требует проверки`, `не подтверждено`.
- Every article must keep the unified article template and exactly three unique related articles where the source data allows it.

## Required article template

Every generated Markdown article must contain these headings in order:

```markdown
# <номер>. <название>

## Назначение статьи
## Краткое описание темы
## Ключевые понятия
## Правила проверки
## Типовые ошибки
## Предупреждения
## Таблица
## Пример применения
## Связанные статьи
## Статус данных
```

`## Предупреждения` and `## Таблица` may be omitted only when the source article has no warnings or table.

## Special warnings

- Analog articles must include: `Аналог требует проверки по размерам, нагрузке, зазору, исполнению, бренду и условиям эксплуатации.`
- Operation, mounting, and diagnostics articles must include: `Рекомендации требуют сверки с документацией производителя и условиями работы узла.`
- Brand articles must not contain unsupported quality ratings such as `лучший бренд`, `самый надёжный`, `плохой производитель`, or `низкое качество`.

## Tables

When a topic requires a table, use this draft structure until confirmed data is available:

```markdown
| Параметр | Значение | Источник | Статус |
|---|---|---|---|
| уточнить | уточнить | уточнить | требует проверки |
```

## Safe Bitrix24 import rules

- Dry-run is the default.
- Real import requires `--execute`, HTTPS `BITRIX24_WEBHOOK_URL`, `BITRIX24_KB_IMPORT_METHOD`, and `BITRIX24_IMPORT_CONFIRM=true`.
- Never commit webhook URLs, tokens, passwords, field IDs, or production credentials.
- Do not invent Bitrix24 REST methods; require admin-confirmed mapping before production import.

## Workflow

1. Inspect `sections.json`, `articles.json`, scripts, docs, and reports.
2. Edit source JSON or scripts; do not manually edit generated exports unless the generator is intentionally changed.
3. Run generation: `python knowledge-base/everest/scripts/generate-knowledge-base.py`.
4. Run validation: `python knowledge-base/everest/scripts/validate-knowledge-base.py`.
5. Run dry-run import: `python knowledge-base/everest/scripts/bitrix24-import.py`.
6. Run repo checks relevant to the change, including `python skills/scripts/validate_skills.py` when skills changed.
7. Confirm `reports/creation-report.md` and `reports/validation-report.md` match the current source data.

## Final report checklist

Include:

- creation status;
- sections created: 8 of 8;
- articles created: 148 of 148;
- numbering preserved;
- duplicates not found;
- invented technical data not used;
- status counts for `нет данных`, `уточнить`, `требует проверки`, `не подтверждено`;
- next actions for official catalog / ГОСТ / ISO verification and Bitrix24 production import readiness.
