# SOURCES — размещение исходников

> **Последнее обновление:** 31 декабря 2025 г.

## Категории
- `sources/gost/` — ГОСТ стандарты и учебные материалы (meta: `sources/gost/meta.yaml`)
- `sources/iso/` — материалы по системе ISO и суффиксам (meta: `sources/iso/meta.yaml`)
- `sources/analogs/` — документ с таблицей аналогов ГОСТ ↔ ISO (meta: `sources/analogs/meta.yaml`)
- `sources/brands/` — каталоги производителей (NSK/NTN/FAG/INA/Schaeffler и др.) (meta: `sources/brands/meta.yaml`)
- `sources/skf/` — каталоги SKF (meta: `sources/skf/meta.yaml`)

## Таблица существующих источников

| Категория | Файл | Статус | Назначение |
|-----------|------|--------|-----------|
| gost | sources/gost/*.pdf | unverified | Стандарты ГОСТ по подшипникам |
| iso | sources/iso/*.pdf | unverified | Стандарты ISO и суффиксы |
| analogs | sources/analogs/*.xlsx | unverified | Таблицы соответствий |
| brands | sources/brands/*.pdf | unverified | Каталоги производителей |
| skf | sources/skf/*.pdf | verified | Официальные каталоги SKF |

> **Примечание:** Для получения актуального списка источников с детальными статусами используйте:
> ```bash
> python scripts/list_sources.py
> ```

## Проверка статусов
- Каждый `meta.yaml` содержит статус `unverified`/`verified`. При добавлении нового источника обновляйте статус и цель (`purpose`).
- Источники из корня и `tests/` перенесены в соответствующие подпапки `sources/`.

### Формат meta.yaml

```yaml
sources:
  - file: "ГОСТ_520-2002.pdf"
    purpose: "Основные технические условия на подшипники качения"
    status: "verified"
    year: 2002
    pages: 52
    url: "http://docs.cntd.ru/"
    notes: "Актуальная версия стандарта"
```

## Как использовать
1. Добавьте новый PDF/DOCX в нужный каталог `sources/<category>/`.
2. Обновите `meta.yaml` (название файла, purpose, status, year, pages, url, notes).
3. Запустите `python scripts/update_repo.py` для пересборки CSV.
4. Зафиксируйте изменения вместе с новым отчётом в `data/reports/`.

## Автоматизация

### Генерация списка источников
Автоматически обновить этот файл на основе meta.yaml:
```bash
python scripts/generate_sources_table.py
```

### Извлечение данных из PDF
```bash
python sources/pdf_text_extractor.py sources/gost/ГОСТ_520-2002.pdf
```

### Парсинг онлайн-каталогов
```bash
python sources/aprom_table_scraper.py
```
