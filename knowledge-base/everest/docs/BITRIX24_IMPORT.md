# Bitrix24 import — Технический справочник «Эверест»

## Режим безопасности

Импортёр `scripts/bitrix24-import.py` всегда запускается в dry-run режиме, если не передан флаг `--execute`. В dry-run режиме HTTP-запросы не выполняются.

Реальный импорт возможен только при одновременном выполнении условий:

1. Передан флаг `--execute`.
2. Установлен `BITRIX24_IMPORT_CONFIRM=true`.
3. Установлен `BITRIX24_WEBHOOK_URL`.
4. Установлен `BITRIX24_KB_IMPORT_METHOD`.
5. Webhook URL использует `https://`.

## Dry-run

```bash
python knowledge-base/everest/scripts/bitrix24-import.py
```

Ожидаемый результат: вывод `DRY-RUN: Bitrix24 API was not called.` и статистика по разделам и статьям.

## Реальный импорт

```bash
export BITRIX24_WEBHOOK_URL
export BITRIX24_KB_IMPORT_METHOD
BITRIX24_IMPORT_CONFIRM=true \
python knowledge-base/everest/scripts/bitrix24-import.py --execute
```

Значение `BITRIX24_KB_IMPORT_METHOD` должно быть согласовано с администратором Bitrix24 и выбранным способом создания или обновления страниц базы знаний. Скрипт не содержит production URL, токенов, паролей или webhook-ключей.

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

## Перед реальным импортом

- Проверить `reports/validation-report.md`.
- Согласовать целевой REST-метод и структуру payload с администратором Bitrix24.
- Выполнить dry-run.
- Сделать тестовый импорт на непроизводственной базе знаний или на ограниченном наборе статей.
- Проверить права webhook и журнал действий Bitrix24.
