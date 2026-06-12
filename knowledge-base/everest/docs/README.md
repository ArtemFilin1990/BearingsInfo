# Технический справочник «Эверест»

Система подготавливает машинно-читаемую базу знаний 2.0 для Bitrix24 по подшипникам, аналогам, ГОСТ / ISO, производителям, эксплуатации, смежным изделиям, каталогам и таблицам.

## Структура

- `source/sections.json` — 8 верхнеуровневых разделов, порядок и список статей.
- `source/articles.json` — отдельная запись для каждой статьи, тело по единому шаблону, статусы, предупреждения и связи.
- `generated/markdown/` — Markdown-экспорт: общий индекс, индексы разделов и отдельный файл каждой статьи.
- `generated/json/bitrix24-import.json` — единый JSON для dry-run импорта и будущего маппинга Bitrix24.
- `generated/csv/articles.csv` — CSV, совместимый с Excel / XLSX-пайплайном.
- `reports/validation-report.md` — отчёт валидатора.
- `reports/creation-report.md` — отчёт генератора.
- `reports/bitrix24-import-dry-run.md` — план действий импортёра без вызова Bitrix24 API.

## Генерация

```bash
python knowledge-base/everest/scripts/generate-knowledge-base.py
```

Генератор не обращается к внешним API. Он пересоздаёт Markdown, JSON, CSV и отчёт создания на основе `source/sections.json` и `source/articles.json`.

## Валидация

```bash
python knowledge-base/everest/scripts/validate-knowledge-base.py
```

Валидатор проверяет:

- наличие всех 8 разделов;
- наличие всех подпунктов;
- сохранение нумерации;
- отсутствие дубликатов;
- обязательные поля каждой статьи;
- предупреждения для аналогов;
- предупреждения для эксплуатации;
- ограничения для брендов;
- статусы неопределённых данных: `нет данных`, `уточнить`, `требует проверки`, `не подтверждено`;
- отсутствие технических плейсхолдеров.

При критических ошибках команда завершается с ненулевым кодом и обновляет `reports/validation-report.md`.

## Dry-run импорт в Bitrix24

```bash
python knowledge-base/everest/scripts/bitrix24-import.py
```

По умолчанию импорт работает через адаптер `landing`, но только в dry-run режиме. Bitrix24 API не вызывается, секреты не нужны, в консоль выводится количество разделов, статей и запланированных REST-действий.

Для абстрактного импорта в собственный обработчик вебхука:

```bash
python knowledge-base/everest/scripts/bitrix24-import.py --adapter generic
```

## Реальный импорт через входящий REST webhook

Реальный HTTP-импорт заблокирован без явного флага и переменных окружения.

### Вариант 1. Landing / база знаний Bitrix24

```bash
export BITRIX24_WEBHOOK_URL
export BITRIX24_KB_SITE_ID
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter landing --execute
```

Переменные окружения:

- `BITRIX24_WEBHOOK_URL` — HTTPS base URL входящего REST webhook Bitrix24. Не хранить в репозитории.
- `BITRIX24_KB_SITE_ID` — ID сайта базы знаний Bitrix24.
- `BITRIX24_KB_SCOPE` — область сайта, по умолчанию `knowledge`.
- `BITRIX24_KB_BLOCK_CODE` — код блока для контента, по умолчанию `0.menu_24`.
- `BITRIX24_IMPORT_CONFIRM=true` — обязательное подтверждение реального импорта.

Для безопасного теста можно ограничить количество REST-действий:

```bash
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter landing --execute --limit-actions 5
```

### Вариант 2. Generic webhook

```bash
export BITRIX24_WEBHOOK_URL
export BITRIX24_KB_IMPORT_METHOD
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter generic --execute
```

`BITRIX24_KB_IMPORT_METHOD` используется только для собственного REST-метода или промежуточного обработчика. Для стандартного наполнения базы знаний используйте `--adapter landing`.

## Ограничения по техническим данным

- В справочник не добавлены неподтверждённые размеры, нагрузки, зазоры, цены, бренды, коды ТН ВЭД или нормативные параметры.
- Спорные и пустые места отмечены статусами данных.
- Статьи про аналоги содержат обязательное предупреждение о проверке по размерам, нагрузке, зазору, исполнению, бренду и условиям эксплуатации.
- Статьи про эксплуатацию содержат предупреждение о сверке с документацией производителя и условиями работы узла.
- Статьи про бренды не содержат неподтверждённых оценок качества.
