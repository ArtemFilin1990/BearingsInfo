# Bearings Info — Справочник по подшипникам

Систематизация информации о подшипниках: устройство, классификация, выбор, эксплуатация и сопутствующая документация.

## 📁 Структура репозитория

После реорганизации репозиторий имеет следующую структуру:

```
BearingsInfo/
├── docs/                    # 📚 Вся документация
│   ├── encyclopedia/
│   │   ├── 01-podshipniki-obshaya-informatsiya/
│   │   ├── 02-standarty-i-markirovka/
│   │   ├── 03-tipy-i-elementy/
│   │   ├── 04-raschet-i-parametry/
│   │   ├── 05-ekspluatatsiya-i-obsluzhivanie/
│   │   ├── 06-otkazy-i-diagnostika/
│   │   ├── 07-brendy-i-proizvoditeli/
│   │   ├── 08-spetsialnye-ispolneniya-i-spravka/
│   │   └── 09-soputstvuyushchie-izdeliya/
│   ├── kb/
│   │   ├── knowledge-base/
│   │   ├── uchebnik/
│   │   ├── uchebnik-akademichesky/
│   │   ├── vvodny-kurs-dlya-novichkov/
│   │   └── testy/
│   ├── images/              # Изображения и схемы
│   ├── prakticheskie-rukovodstva/
│   └── ...
├── data/                    # 📊 Данные, базы, таблицы
│   ├── katalogi/
│   ├── schemas/
│   ├── sql/
│   └── *.csv, *.xlsx
├── sources/                 # 📚 Источники данных
├── archive/                 # 🗄️ Архивные материалы
├── src/                     # 💻 Исходный код
│   ├── api/
│   ├── sources/
│   └── *.py
├── tools/                   # 🛠 Утилиты и скрипты
│   ├── scripts/
│   └── bin/
├── config/                  # ⚙️ Конфигурационные файлы
├── tests/                   # ✅ Тесты
└── README.md               # Этот файл
```

---

## 📂 Что где лежит — подробное описание каталогов и файлов

Ниже подробно расписано, что находится в каждой папке репозитория и какие там файлы (каталоги производителей, таблицы обозначений, справочники, схемы БД, исходный код и т. д.).

### 📁 `docs/` — Документация и контент справочника

Главный каталог с текстовым контентом (Markdown) — энциклопедия, учебники, статьи, руководства.

- **`docs/encyclopedia/`** — Основная энциклопедия по подшипникам, разбитая на 9 тематических разделов:
  - `01-podshipniki-obshaya-informatsiya/` — общая информация, термины, классификация, алгоритм выбора
  - `02-standarty-i-markirovka/` — **система обозначений** (ГОСТ, ISO, DIN, ANSI), маркировка, расшифровка кодов, классы точности, аналоги
  - `03-tipy-i-elementy/` — типы подшипников (шариковые, роликовые, игольчатые), сепараторы, тела качения, узлы
  - `04-raschet-i-parametry/` — нагрузки, ресурс, зазоры, преднатяг, комплекты DF/DB/DT
  - `05-ekspluatatsiya-i-obsluzhivanie/` — смазка, посадки, монтаж, хранение
  - `06-otkazy-i-diagnostika/` — дефекты, причины повреждений, диагностика
  - `07-brendy-i-proizvoditeli/` — производители (СКФ, FAG, NSK, NTN, ГПЗ, китайские бренды и т. д.)
  - `08-spetsialnye-ispolneniya-i-spravka/` — миниатюрные, керамические, высокотемпературные подшипники
  - `09-soputstvuyushchie-izdeliya/` — крепёж, втулки, уплотнения, передачи
- **`docs/kb/`** — База знаний и обучающие материалы:
  - `knowledge-base/` — структурированная база знаний
  - `uchebnik/`, `uchebnik-akademichesky/` — учебники (практический и академический)
  - `vvodny-kurs-dlya-novichkov/` — вводный курс
  - `testy/` — тесты для проверки знаний
- **`docs/podshipniki/`** — Тематические разделы (обозначения, классы точности, зазоры, моменты трения, типы, смазка, примеры обозначений).
- **`docs/articles/`** — Статьи по сопутствующим изделиям (ШС, ремни, сальники, цепи, шкивы, РТИ, РВД, кольца и т. д.).
- **`docs/bearings/`** — Расширенный справочник: `MASTER_INDEX.md`, `glossary.md`, `gost_comprehensive_guide.md`, подкаталоги `analogues/`, `brands/`, `catalog/`, `classification/`, `designations/`, `faq/`.
- **`docs/wiki/`** — Wiki-формат: основы, терминология, стандарты, маркировка, `Home.md`.
- **`docs/prakticheskie-rukovodstva/`** — Практические руководства, кейсы, чек-листы.
- **`docs/instrumenty-i-spravochniki/`** — Калькуляторы, конвертеры, справочники.
- **`docs/karty-znany-i-navigatsiya/`** — Карты знаний и навигационные схемы.
- **`docs/images/`** — Изображения, фотографии, чертежи и схемы.
- **`docs/gost/`, `docs/iso/`, `docs/en/`** — Материалы по стандартам ГОСТ, ISO и англоязычные материалы.
- **`docs/analogs/`, `docs/brands/`** — Аналоги и бренды (текстовая часть).
- **`docs/appendices/`, `docs/supplementary/`, `docs/technical/`** — Приложения, дополнительные и технические материалы.
- **`docs/extracted/`** — Текст, извлечённый из источников (PDF и т. д.).
- **`docs/examples/`** — Примеры.
- **`docs/it-infrastructure/`** — Документация по IT-инфраструктуре проекта.
- **`docs/archive/`** — Архивные документы.
- **`docs/meta/`** — Метаданные документации.
- **Корневые `.md` файлы в `docs/`:** `QUICK_START.md`, `QUICK_REFERENCE.md`, `NAVIGATION_GUIDE.md`, `REPOSITORY_STRUCTURE.md`, `DEMO.md`, `ARTICLE_CREATION_GUIDE.md`, `KNOWLEDGE_BASE_BUILDER.md`, `EXTRACTED_KNOWLEDGE_INDEX.md`, `automation.md`, `automation_ru.md`, `AGENT.md`.

### 📁 `data/` — Данные, таблицы и базы

Структурированные данные: каталоги, размерные таблицы, обозначения, аналоги, схемы БД.

- **`data/katalogi/`** — **Каталоги производителей** в формате Markdown (более сотни файлов): SKF, FAG, NSK, NTN, IKO, EPK, ROLLON, MARKES, MEGADYNE, NBS, FYH, AKE, APB, CRAFT, CX, DAS LAGER, EMS, FBJ, FKL, Fersa, GAMET, HARP, IBB, IBC, IBU, 10-ГПЗ и др. Подкаталог `catalog-legacy/` содержит устаревшие версии.
- **`data/gost/`** — Таблицы по ГОСТ в формате CSV: `bearings.csv`, `dimensions.csv`, `series.csv`, `tolerances.csv`.
- **`data/iso/`** — Таблицы по ISO: `bearings.csv`, `dimensions.csv`, `prefixes.csv`, `suffixes.csv` (префиксы и **суффиксы обозначений**).
- **`data/brands/`** — Справочники брендов: `brands.csv`, `brand_comparison.csv`, `manufacturers_asia.csv`, `manufacturers_china.csv`, `manufacturers_cis.csv`, `manufacturers_europe.csv`.
- **`data/dimensions/`** — Размерные таблицы: `bearing_dimensions.csv` (d, D, B и др.).
- **`data/nomenclature/`** — Номенклатура по производителям (по одному файлу `.md` на бренд: AAA, ABC, ADR, AKE, APB, BARDEN, BBC, CRAFT, DKF, EER, FAG, FERSA, FLT, GMN, GPL, GRW, HCH, HYA, INA, 10-ГПЗ и др.).
- **`data/analogs/`** — **Таблицы аналогов**: `gost_iso.csv`, `gost_to_iso.csv`, `iso_to_gost.csv`, `additional_designations.csv`, `import_analogs.csv`, `housings.csv`, `units.csv`.
- **`data/csv/`** — Сводные CSV-таблицы: `master_catalog.csv`, `bearing_units.csv`, `tn_ved_codes.csv` (коды ТН ВЭД), `tolerance_classes.csv`, плюс подпапки `analogs/`, `brands/`, `gost/`, `iso/`.
- **`data/database/`** — База данных: `schema.sql` (схема), `README.md`.
- **`data/schema/`** — SQL-схемы: `bearings_db_schema.sql`, `d1_schema.sql`.
- **`data/schemas/`** — YAML-схемы валидации: `analogs.yaml`, `brand_descriptions.yaml`, `brands.yaml`, `gost.yaml`, `iso.yaml`, `nomenclature.yaml`.
- **`data/sql/`** — SQL-скрипты: `init_catalog.sql`.
- **`data/tables/`** — Таблицы (Markdown).
- **`data/raw/`** — Сырые данные.
- **`data/inbox/`** — Входящие файлы для обработки.
- **`data/reports/`** — Отчёты (например, `2025-12-30_source.json`).
- **`data/assets/`** — Ассеты для данных.
- **`data/sources-legacy/`** — Устаревшие источники: `EXTRACTION_STATUS.md`, `PDF_EXTRACTION_METHODOLOGY.md`, `RAW_INDEX.md`, `VERSION_CONTROL.md`, JSON-файлы с размерами по сериям 6000/6200/6300/angular_contact и т. д.
- **Корневые файлы `data/`:** `articles.xlsx`, `bearing_directory.xlsx` (Excel-справочники), `articles_list.csv`, `brands.csv`, `nomenclature.csv`.

### 📁 `src/` — Исходный код Python

Логика парсинга, обработки и API.

- `__init__.py`, `__main__.py` — точки входа пакета.
- `cli.py` — интерфейс командной строки.
- `catalog.py` — работа с каталогом подшипников.
- `config.py` — загрузка конфигурации.
- `logger.py` — логирование.
- `parser.py` — парсер обозначений.
- `processor.py` — обработка данных.
- `registry.py` — реестр.
- `utils.py` — утилиты.
- `watcher.py` — отслеживание изменений.
- **`src/api/`** — REST API (FastAPI/Flask): `main.py`, `app/`, `examples/`, `scripts/`, `sql/`, `tests/`, `mar_Dockerfile`, `mar_requirements.txt`, `README.md`.
- **`src/sources/`** — Извлечение из источников: `pdf_text_extractor.py`, `table_scraper.py`, `brands_json_to_csv.py`.

### 📁 `tools/` — Утилиты, скрипты, автоматизация

- **`tools/scripts/`** — Большое количество Python-скриптов сборки и обработки: `build_knowledge_base.py`, `build_complete_knowledge_base.py`, `build_enhanced_knowledge_base.py`, `build_ultra_comprehensive_kb.py`, `build_search_index.py`, `build_autocomplete_dict.py`, `build_bearings_seed.py`, `check_data_sources.py`, `deduplicate_nomenclature.py`, `generate_sources_table.py`, `import_bearings_to_db.py`, `pdf_extractor_optimized.py`, `move_all_to_inbox.py`, `fix_articles_structure.py`, `mar_manage.py` и др.
- **`tools/bin/`** — Бинарные/исполняемые утилиты.
- Подпапки `extract/`, `examples/`, `run/`.
- `README.md` — описание инструментов.

### 📁 `config/` — Конфигурационные файлы

- `app.yaml` — конфигурация приложения.
- `brand_aliases.json` — синонимы и алиасы брендов.
- `parsing_rules.json` — правила парсинга обозначений.
- `mar_Dockerfile`, `mar_docker-compose.yml`, `mar_Makefile`, `mar_pyproject.toml`, `mar_requirements.txt` — конфиги под подпроект MAR.

### 📁 `sources/` — Источники данных

Исходные источники (PDF, документы, ссылки) — описание в `README.md`.

### 📁 `archive/` — Архив

- **`archive/zip/`** — Архивы (`book.zip`, `book.z01.zip`, `book.z02.zip`, `bearing_handbook_pkg.rar`).
- **`archive/docs-legacy/`** — Устаревшая документация: `01_basics/`, `03_types_components/`, `04_parameters_calculations/`, `README/`, плюс `README-api.md`, `README-baza.md`, `README-mar.md`.

### 📁 `tests/` — Тесты (pytest)

`conftest.py` и тестовые модули: `test_automation_pipeline.py`, `test_code_normalization.py`, `test_dedup.py`, `test_deduplication.py`, `test_dimensions.py`, `test_knowledge_base_builder.py`, `test_processor.py`, `test_schema_validation.py`, `test_schemas.py`, `test_suffixes.py`, `test_table_scraper.py`, `test_validators.py`.

### 📁 `Подшипники/` — Исходные русскоязычные материалы

Папки с тематическими подшипниковыми материалами (например, `4.16. Большие подшипники` и т. д.) — оригинальные исходники на русском.

### 📄 Файлы в корне репозитория

- **`README.md`** — этот файл (главная страница проекта и навигация).
- **`AGENT.md`** — инструкции для AI-агентов, работающих с репозиторием.
- **`CONTRIBUTING.md`** — правила контрибьюции.
- **`SECURITY.md`** — политика безопасности.
- **`CODEOWNERS`** — владельцы кода.
- **`LICENSE`** — лицензия MIT.
- **`QA_AUDIT_REPORT.md`** — отчёт по качеству репозитория.
- **`Makefile`** — задачи сборки/линтинга/тестов.
- **`manage.py`** — управляющий скрипт проекта.
- **`Dockerfile`**, **`docker-compose.yml`** — контейнеризация.
- **`pyproject.toml`** — конфигурация Python-проекта.
- **`requirements.txt`**, **`requirements-dev.txt`** — зависимости (runtime и dev).
- **`.editorconfig`**, **`.gitignore`**, **`.pre-commit-config.yaml`** — настройки разработки.
- **`.github/`** — workflow GitHub Actions, шаблоны issue/PR.
- **`.vscode/`** — настройки VS Code.

---

## Навигация по репозиторию

### Основные разделы

- **[1. Подшипники. Общая информация](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/README.md>)** — Термины, классификация, устройство, алгоритм выбора
- **[2. Стандарты и маркировка](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)** — ГОСТ, ISO, DIN, система обозначений, аналоги
- **[3. Типы и элементы](<docs/encyclopedia/03-tipy-i-elementy/README.md>)** — Шариковые, роликовые, конические, сепараторы, узлы
- **[4. Расчёт и параметры](<docs/encyclopedia/04-raschet-i-parametry/README.md>)** — Нагрузки, ресурс, зазоры, преднатяг, комплекты
- **[5. Эксплуатация и обслуживание](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)** — Смазка, посадки, монтаж, хранение
- **[6. Отказы и диагностика](<docs/encyclopedia/06-otkazy-i-diagnostika/README.md>)** — Дефекты, причины, коррозия, электроэрозия
- **[7. Бренды и производители](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)** — SKF, FAG, NSK, NTN, российские ГПЗ, аналоги
- **[8. Специальные исполнения и справка](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)** — Высокоточные, керамические, высокотемпературные
- **[9. Сопутствующие изделия](<docs/encyclopedia/09-soputstvuyushchie-izdeliya/README.md>)** — Смазки, крепёж, передачи, уплотнения

### Дополнительные материалы

- **[tools/](<tools/README.md>)** — Инструменты и утилиты для работы с репозиторием
- **[data/](<data/README.md>)** — Базы данных, таблицы, CSV-файлы
- **[Практические руководства](<docs/prakticheskie-rukovodstva/README.md>)** — Кейсы, примеры, чек-листы
- **[Изображения](<docs/images/README.md>)** — Фотографии, схемы, диаграммы

### Для контрибьюторов

- **[CONTRIBUTING.md](CONTRIBUTING.md)** — Как внести вклад в проект
- **[LICENSE](LICENSE)** — Лицензия MIT
- **[SECURITY.md](SECURITY.md)** — Политика безопасности
- **[QA_AUDIT_REPORT.md](QA_AUDIT_REPORT.md)** — Отчёт по качеству репозитория

---

# Содержание

## 1. Основы, терминология и выбор подшипников

1.1 [Основные термины и определения](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.3. Термины и определения RU EN/README.md>)  
1.2 [Из чего состоит подшипник (элементы, функции, материалы)](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.4. Из чего состоит подшипник/README.md>)  
1.3 [Терминология конструкции подшипников](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/README.md>)  
1.4 [Классификация подшипников (по нагрузке, направлению, конструкции)](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.5. Классификация подшипников/README.md>)  
1.5 [Конструктивные разновидности подшипников](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
1.6 [Как делают подшипники (этапы производства, контроль качества)](docs/QUICK_START.md)  
1.7 [Взаимозаменяемость подшипников качения и скольжения](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
1.8 [Алгоритм выбора подшипника (нагрузка → скорость → ресурс → среда → стандарт)](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.7. Алгоритм выбора и чек-лист ошибок/README.md>)

## 2. Стандарты и маркировка (ядро справочника)

2.1 [ГОСТ. Подшипники. Перечень и область применения стандартов](<docs/encyclopedia/02-standarty-i-markirovka/2.1. Карта стандартов ГОСТ, ISO, DIN, ANSI/README.md>)  
2.2 [ISO / DIN / ANSI. Международные стандарты подшипников](<docs/encyclopedia/02-standarty-i-markirovka/2.4. ISO DIN ANSI правила и отличия/README.md>)  
2.3 [Условное обозначение подшипников по ЕТУ 100, ЕТУ 500 и ТУ](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)  
2.4 [Система условных обозначений подшипников (декомпозиция по символам)](<docs/encyclopedia/02-standarty-i-markirovka/2.2. Система обозначений базовая модель/README.md>)  
2.5 [Примеры условных обозначений (разбор по шагам)](<docs/encyclopedia/02-standarty-i-markirovka/2.11. Примеры расшифровки обозначений/README.md>)  
2.6 [Маркировка подшипников: заводская, торговая, экспортная](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)  
2.7 [Обозначение внутреннего диаметра (правила, исключения, спецсерии)](<docs/encyclopedia/02-standarty-i-markirovka/2.3. ГОСТ правила формирования обозначения/README.md>)  
2.8 [Обозначение размерных серий и серий ширины](<docs/encyclopedia/02-standarty-i-markirovka/2.2. Система обозначений базовая модель/README.md>)  
2.9 [Обозначение момента трения и скоростных характеристик](<docs/encyclopedia/02-standarty-i-markirovka/2.10. Скорость, температура, смазка обозначения/README.md>)  
2.10 [Категории и группы подшипников по назначению](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.5. Классификация подшипников/README.md>)  
2.11 [Классы точности ГОСТ / ISO / ABEC (таблица соответствий)](<docs/encyclopedia/02-standarty-i-markirovka/2.6. Классы точности ГОСТ, ISO, ABEC/README.md>)  
2.12 [Таблица аналогов ГОСТ → ISO (базовые и расширенные серии)](<docs/encyclopedia/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
2.13 [Таблица аналогов ISO → ГОСТ](<docs/encyclopedia/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
2.14 [Таблица соответствия дополнительных обозначений ГОСТ ↔ ISO ↔ бренды](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)  
2.15 [Импортные аналоги российских подшипников (с ограничениями применяемости)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
2.16 [Коды ТН ВЭД ЕАЭС для подшипников (по типам)](<docs/encyclopedia/02-standarty-i-markirovka/2.12. ТН ВЭД коды по типам/README.md>)

## 3. Типы, узлы и элементы конструкции

3.1 [Типы подшипников (шариковые, роликовые, игольчатые, сферические)](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.2 [Типы и конструктивные модификации](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.3 [Сепараторы: материалы, исполнение, ограничения](<docs/encyclopedia/02-standarty-i-markirovka/2.9. Клетки и сепараторы обозначения/README.md>)  
3.4 [Тела качения: применяемость и сравнительный анализ](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.4.1 [Шарики](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.4.2 [Ролики (цилиндрические, конические, сферические, игольчатые)](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.5 [Подшипниковые узлы и корпусные подшипники (UCP, UCF, UCFL и аналоги)](<docs/encyclopedia/03-tipy-i-elementy/README.md>)  
3.6 [Шпиндельные и высокоточные подшипники](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
3.7 [Гибридные и керамические подшипники](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
3.8 [Подшипники SKF Y-типа: обозначения и размеры](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
3.9 [Крестовины карданных валов](<docs/encyclopedia/09-soputstvuyushchie-izdeliya/README.md>)  
3.10 [Закрепительные и стяжные втулки, гайки, стопорные элементы](<docs/encyclopedia/09-soputstvuyushchie-izdeliya/README.md>)  
3.11 [Втулки и подшипники скольжения](<docs/encyclopedia/03-tipy-i-elementy/README.md>)

## 4. Расчетные и технические параметры

4.1 [Радиальные и осевые нагрузки](<docs/encyclopedia/04-raschet-i-parametry/README.md>)  
4.2 [Углы контакта радиально-упорных подшипников](<docs/encyclopedia/04-raschet-i-parametry/README.md>)  
4.3 [Предельные и рабочие частоты вращения](<docs/encyclopedia/04-raschet-i-parametry/README.md>)  
4.4 [Радиальные зазоры и группы зазоров](<docs/encyclopedia/02-standarty-i-markirovka/2.7. Зазоры и группы маркировка и влияние/README.md>)  
4.5 [Предварительный натяг: цели, методы, риски](<docs/encyclopedia/04-raschet-i-parametry/README.md>)  
4.6 [Комплекты подшипников (DF / DB / DT)](<docs/encyclopedia/04-raschet-i-parametry/README.md>)

## 5. Эксплуатация и обслуживание

5.1 [Смазки: типы, классы, совместимость](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.2 [Посадки колец подшипников (вал / корпус)](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.3 [Монтаж и демонтаж (ошибки и последствия)](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.4 [Ревизия и диагностика состояния](<docs/encyclopedia/06-otkazy-i-diagnostika/README.md>)  
5.5 [Хранение, упаковка, транспортировка](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.6 [Переконсервация и повторный ввод в эксплуатацию](<docs/encyclopedia/05-ekspluatatsiya-i-obsluzhivanie/README.md>)

## 6. Отказы и диагностика

6.1 [Основные причины повреждений](<docs/encyclopedia/06-otkazy-i-diagnostika/README.md>)  
6.2 [Терминология дефектов (фото + описание + причина)](<docs/encyclopedia/06-otkazy-i-diagnostika/README.md>)  
6.3 [Подшипники в электродвигателях и типовые отказы](<docs/encyclopedia/06-otkazy-i-diagnostika/README.md>)

## 7. Каталог производителей и брендов (расширенный)

7.1 [Производители СНГ (ГПЗ, СПЗ, ВПЗ, MPZ и др.)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
7.2 [Европейские производители (SKF, FAG/INA, NSK Europe, NKE)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
7.3 [Азиатские производители (NSK, NTN, KOYO, Nachi, ZWZ, C&U)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
7.4 [Китайские OEM и aftermarket бренды (LYC, HRB, ZKL и др.)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
7.5 [Особенности маркировки и обозначений по брендам](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)  
7.6 [Сопоставление брендов: премиум / индустриальные / бюджетные](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)

## 8. Специальные исполнения и справочная информация

8.1 [Миниатюрные и тонкостенные подшипники](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.2 [Высокотемпературные и криогенные подшипники](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.3 [Виброустойчивые и ударостойкие исполнения](<docs/encyclopedia/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.4 [Таблица расшифровки кодов даты выпуска](docs/QUICK_REFERENCE.md)  
8.5 [Библиография и нормативная литература](docs/QUICK_REFERENCE.md)  
8.6 [Практические заметки и нетиповые кейсы](<docs/prakticheskie-rukovodstva/README.md>)

## Приложения: таблицы и базы данных

A.1 [Таблица ГОСТ ↔ ISO ↔ Бренд ↔ Тип ↔ Размеры](<data/README.md>)  
A.2 [Таблица аналогов ГОСТ → ISO → SKF / FAG / NSK / NTN](<docs/encyclopedia/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
A.3 [Таблица аналогов ISO → ГОСТ → российские заводы](<docs/encyclopedia/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
A.4 [Таблица дополнительных обозначений ГОСТ / ISO / бренд](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)  
A.5 [Размерные таблицы (d, D, B, r, масса)](<data/README.md>)  
A.6 [Таблица производителей (страна, специализация, уровень качества)](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)

## Указатели

I.1 [Алфавитный указатель терминов](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.3. Термины и определения RU EN/README.md>)  
I.2 [Указатель обозначений/серий подшипников](<docs/encyclopedia/02-standarty-i-markirovka/README.md>)  
I.3 [Указатель стандартов](<docs/encyclopedia/02-standarty-i-markirovka/2.1. Карта стандартов ГОСТ, ISO, DIN, ANSI/README.md>)  
I.4 [Указатель производителей и брендов](<docs/encyclopedia/07-brendy-i-proizvoditeli/README.md>)

## О проекте

P.1 [Предисловие](docs/QUICK_START.md)  
P.2 [Как пользоваться справочником (логика разделов, поиск, навигация)](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.2. Как пользоваться базой/README.md>)  
P.3 [Список сокращений и условных обозначений](docs/QUICK_REFERENCE.md)  
P.4 [Принципы идентификации статей (ID/slug), готовность к интеграции в БД/AI](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.9. Структура данных для БД/README.md>)  
P.5 [Список таблиц и иллюстраций (если применимо)](<docs/images/README.md>)  
P.6 [История изменений (changelog)](docs/QUICK_START.md)  
P.7 [Политика источников, цитирование, лицензии](<docs/encyclopedia/01-podshipniki-obshaya-informatsiya/1.8. Источники и верификация/README.md>)  
P.8 [Схемы импорта/экспорта данных (CSV/JSON), правила валидации](<data/schemas/README.md>)

---

## 🧭 Дополнительные материалы

- **[Вводный курс для новичков](<docs/kb/vvodny-kurs-dlya-novichkov/README.md>)** — Обучающие материалы для начинающих
- **[Учебник](<docs/kb/uchebnik/README.md>)** / **[Учебник академический](<docs/kb/uchebnik-akademichesky/README.md>)** — Систематический курс изучения
- **[Практические руководства](<docs/prakticheskie-rukovodstva/README.md>)** — Пошаговые инструкции и кейсы
- **[Инструменты и справочники](<docs/instrumenty-i-spravochniki/README.md>)** — Калькуляторы, конвертеры, утилиты
- **[Карты знаний и навигация](<docs/karty-znany-i-navigatsiya/README.md>)** — Визуальные схемы и навигация по темам
- **[Каталоги](<data/katalogi/README.md>)** — Каталоги производителей и продукции
- **[Изображения](<docs/images/README.md>)** — Фотографии, схемы, чертежи
- **[Тесты](<docs/kb/testy/README.md>)** — Проверка знаний

---

## 🔧 Техническая инфраструктура

**Исходный код и данные:**
- **[src/api/README.md](src/api/README.md)** — API-интерфейс
- **[data/README.md](data/README.md)** — Данные и базы
- **[sources/README.md](sources/README.md)** — Источники данных
- **[docs/NAVIGATION_GUIDE.md](docs/NAVIGATION_GUIDE.md)** — Навигация по документации
- **[tools/README.md](tools/README.md)** — Инструменты и утилиты
- `tests/` — Тесты
- `config/` — Конфигурационные файлы
- **[data/schemas/README.md](data/schemas/README.md)** — Схемы баз данных
- `data/sql/` — SQL-скрипты

**Языковой состав:**
- Python: 89.6% (скрипты анализа данных)
- PLpgSQL: 5.5% (хранимые процедуры PostgreSQL)
- Shell: 3.8% (автоматизация)
- Other: 1.1%

---

## 🚀 Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ArtemFilin1990/BearingsInfo.git
   cd BearingsInfo
   ```

2. **Начните с вводного курса:**  
   Ознакомьтесь с **[Вводным курсом для новичков](<docs/kb/vvodny-kurs-dlya-novichkov/README.md>)** для понимания основ

3. **Используйте навигацию:**  
   Используйте **[Карты знаний](<docs/karty-znany-i-navigatsiya/README.md>)** для поиска нужной информации

4. **Изучите стандарты:**  
   Раздел **[Стандарты и маркировка](#2-стандарты-и-маркировка-ядро-справочника)** — ключевой для понимания обозначений

---

## 📄 Лицензия

См. [LICENSE](LICENSE)

---

## 🤝 Участие в проекте

Мы приветствуем вклад в развитие проекта! См. [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Проект активно развивается. Дополнительные материалы и улучшения будут добавляться в будущем.**
