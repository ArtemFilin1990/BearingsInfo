# Bitrix24 import — Технический справочник «Эверест»

## Режим безопасности

Импортёр `scripts/bitrix24-import.py` всегда запускается в dry-run режиме, если не передан флаг `--execute`. В dry-run режиме HTTP-запросы не выполняются.

Реальный импорт возможен только при одновременном выполнении условий:

1. Передан флаг `--execute`.
2. Установлен `BITRIX24_IMPORT_CONFIRM=true`.
3. Установлен `BITRIX24_WEBHOOK_URL`.
4. Для режима `landing` установлен `BITRIX24_KB_SITE_ID`.
5. Для режима `generic` установлен `BITRIX24_KB_IMPORT_METHOD`.
6. Webhook URL использует `https://`.

## Dry-run

```bash
python knowledge-base/everest/scripts/bitrix24-import.py
```

Ожидаемый результат: вывод `DRY-RUN: Bitrix24 API was not called.`, статистика по разделам и статьям, а также отчёт `reports/bitrix24-import-dry-run.md`.

Dry-run для стандартной базы знаний Bitrix24:

```bash
python knowledge-base/everest/scripts/bitrix24-import.py --adapter landing
```

Dry-run для собственного промежуточного обработчика:

```bash
python knowledge-base/everest/scripts/bitrix24-import.py --adapter generic
```

## Реальный импорт через Landing / Knowledge Base

```bash
export BITRIX24_WEBHOOK_URL
export BITRIX24_KB_SITE_ID
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter landing --execute
```

Дополнительные переменные:

- `BITRIX24_KB_SCOPE` — область сайта. Значение по умолчанию: `knowledge`.
- `BITRIX24_KB_BLOCK_CODE` — код блока для добавления контента. Значение по умолчанию: `0.menu_24`.
- `BITRIX24_KB_SITE_CODE` — код сайта для dry-run поиска.
- `BITRIX24_KB_SITE_TITLE` — название сайта для dry-run поиска.

Для контролируемого теста используйте ограничение действий:

```bash
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter landing --execute --limit-actions 5
```

## Реальный импорт через generic webhook

```bash
export BITRIX24_WEBHOOK_URL
export BITRIX24_KB_IMPORT_METHOD
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --adapter generic --execute
```

Этот режим отправляет каждую статью в один указанный метод. Он нужен, если в Bitrix24 или на внешнем сервере есть собственный обработчик создания страниц.

## Формат данных

Источник импорта: `generated/json/bitrix24-import.json`.

Каждая статья содержит:

- номер;
- название;
- порядок;
- Markdown-контент;
- предупреждения;
- статусы данных;
- связанные статьи;
- блок `bitrix24_mapping` для будущего точного маппинга полей.

В режиме `landing` Markdown преобразуется в простой HTML. Скрипт создаёт план действий:

1. Проверка сайта базы знаний.
2. Создание разделов.
3. Создание страниц статей.
4. Добавление контентного блока.
5. Заполнение блока HTML-контентом.
6. Публикация страниц.
7. Публикация сайта.

## Перед реальным импортом

- Проверить `reports/validation-report.md`.
- Выполнить dry-run и проверить `reports/bitrix24-import-dry-run.md`.
- Проверить права входящего вебхука: доступ к методам `landing.*`.
- Уточнить `BITRIX24_KB_SITE_ID` целевой базы знаний.
- Сделать тестовый импорт с `--limit-actions 5`.
- Проверить внешний вид страниц в Bitrix24.
- После проверки запустить полный импорт.

## Запреты

- Не хранить `BITRIX24_WEBHOOK_URL` в репозитории.
- Не коммитить токены, пароли, webhook URL, ID пользователей и production credentials.
- Не запускать `--execute`, если dry-run не проверен.
- Не считать импорт успешным без визуальной проверки страниц в Bitrix24.
