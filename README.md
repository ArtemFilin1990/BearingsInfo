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

## 📂 Что где лежит — подробная структура папок и файлов

Ниже приведена полная развёрнутая структура репозитория с описанием каждой папки и ключевых файлов: каталоги производителей, таблицы обозначений (ГОСТ/ISO/DIN), справочники, схемы БД, исходный код, тесты и инфраструктура.

### 📁 `docs/` — Документация и контент справочника

Главный каталог с текстовым контентом (Markdown): энциклопедия, учебники, статьи, руководства, wiki, технические материалы.

```
docs/
├── encyclopedia/                              # 📖 Основная энциклопедия (9 разделов)
│   ├── 01-podshipniki-obshaya-informatsiya/   # Общая информация, термины, выбор
│   │   ├── 1.1. Назначение и границы/
│   │   ├── 1.2. Как пользоваться базой/
│   │   ├── 1.3. Термины и определения RU EN/
│   │   ├── 1.4. Из чего состоит подшипник/
│   │   ├── 1.5. Классификация подшипников/
│   │   ├── 1.6. Ключевые параметры выбора/
│   │   ├── 1.7. Алгоритм выбора и чек-лист ошибок/
│   │   ├── 1.8. Источники и верификация/
│   │   ├── 1.9. Структура данных для БД/
│   │   ├── 1.10. Статусы материалов и обновления/
│   │   └── README.md
│   ├── 02-standarty-i-markirovka/             # 🏷 Стандарты, маркировка, обозначения
│   │   ├── 2.1. Карта стандартов ГОСТ, ISO, DIN, ANSI/
│   │   ├── 2.2. Система обозначений базовая модель/
│   │   ├── 2.3. ГОСТ правила формирования обозначения/
│   │   ├── 2.4. ISO DIN ANSI правила и отличия/
│   │   ├── 2.5. Сопоставление ГОСТ и ISO аналоги/
│   │   ├── 2.6. Классы точности ГОСТ, ISO, ABEC/
│   │   ├── 2.7. Зазоры и группы маркировка и влияние/
│   │   ├── 2.8. Уплотнения и защита обозначения/
│   │   ├── 2.9. Клетки и сепараторы обозначения/
│   │   ├── 2.10. Скорость, температура, смазка обозначения/
│   │   ├── 2.11. Примеры расшифровки обозначений/
│   │   ├── 2.12. ТН ВЭД коды по типам/
│   │   ├── gost/
│   │   └── README.md
│   ├── 03-tipy-i-elementy/                    # 🔩 Типы и элементы конструкции
│   │   ├── 3.1. Шариковые подшипники/
│   │   ├── 3.2. Радиально-упорные углы контакта и комплекты/
│   │   ├── 3.3. Роликовые цилиндрические N, NU, NJ, NUP/
│   │   ├── 3.4. Роликовые конические/
│   │   ├── 3.5. Роликовые сферические/
│   │   ├── 3.6. Игольчатые/
│   │   ├── 3.7. Самоустанавливающиеся/
│   │   ├── 3.8. Исполнения и модификации/
│   │   ├── 3.9. Сепараторы материалы и ограничения/
│   │   ├── 3.10. Узлы и корпуса UC, UCP, UCF, UCFL/
│   │   ├── 3.11. Крепёж втулки, гайки, стопора/
│   │   ├── 3.12. Прецизионные, шпиндельные, высокоскоростные/
│   │   ├── 3.13. Гибридные и керамические/
│   │   ├── 3.14. Подшипники скольжения/
│   │   └── README.md
│   ├── 04-raschet-i-parametry/                # 📐 Нагрузки, ресурс, зазоры, преднатяг
│   ├── 05-ekspluatatsiya-i-obsluzhivanie/     # 🛠 Смазка, посадки, монтаж, хранение
│   ├── 06-otkazy-i-diagnostika/               # 🔍 Дефекты, причины, диагностика
│   ├── 07-brendy-i-proizvoditeli/             # 🏭 SKF, FAG, NSK, NTN, ГПЗ, China brands
│   ├── 08-spetsialnye-ispolneniya-i-spravka/  # ⚙ Миниатюрные, керамические, высокотемп.
│   └── 09-soputstvuyushchie-izdeliya/         # 🔧 Крепёж, втулки, уплотнения, передачи
│
├── kb/                                        # 🎓 База знаний и обучающие материалы
│   ├── knowledge-base/                        #     Структурированная БЗ (номенклатура, учебники, тесты)
│   ├── uchebnik/                              #     Учебник (часть-1 … часть-4)
│   ├── uchebnik-akademichesky/                #     Учебник академический
│   ├── vvodny-kurs-dlya-novichkov/            #     Вводный курс для новичков
│   └── testy/                                 #     Тесты для проверки знаний
│
├── podshipniki/                               # 📚 Тематические разделы (обозначения, типы, маркировка)
│   ├── 1.1. Система условных обозначений подшипников/
│   ├── 1.2. Класс точности подшипников ГОСТ, ISO, ABEC/
│   ├── 1.3. Зазоры в подшипниках качения/
│   ├── 1.4. Обозначение момента трения подшипников/
│   ├── 1.5. Обозначение категорий подшипников/
│   ├── 1.6. Обозначение внутреннего диаметра подшипников/
│   ├── 1.7. Обозначение размерных серий подшипников/
│   ├── 1.8. Типы подшипников/
│   ├── 1.9. Сепараторы подшипников качения/
│   ├── 1.10. Смазка подшипников/
│   ├── 1.11. Примеры условного обозначения подшипников/
│   ├── 2.1.–2.8. ГОСТ, ISO, ЕТУ, ТН ВЭД, аналоги/
│   ├── 3.1.–3.28. Конструкция, расчёт, монтаж, диагностика/
│   ├── 4.1.–4.16. Типы подшипников (сферические, игольчатые, упорные, …)/
│   ├── 5.1.–5.5. Узлы, SKF Y-тип, гибридные, шпиндельные/
│   ├── 6.1.–6.4.x. Заводы СНГ, бренды (SKF/FAG/NSK/NTN/SNFA/KOYO/GMN/BARDEN/FKL/BBC-R/MPZ)/
│   ├── 7.1.–7.4. Шарики, ролики, тела качения, втулки/
│   └── 8.1.–8.3. Втулки скольжения, тапербуш/
│
├── articles/                                  # 📝 Статьи по сопутствующим изделиям
│   ├── 2_ball_joints/                         #   Шарнирные соединения
│   ├── 3_linear_guides_and_ball_screws/       #   Линейные направляющие и ШВП
│   ├── 4_rti_gost/                            #   РТИ по ГОСТ
│   ├── 5_drive_belts/                         #   Приводные ремни
│   ├── 6_seals_and_cuffs/                     #   Сальники и манжеты
│   ├── 7_hoses_and_rvd/                       #   Рукава и РВД
│   ├── 8_o_rings/                             #   O-ring кольца
│   ├── 9_pulleys/                             #   Шкивы
│   ├── 10_chains_and_sprockets/               #   Цепи и звёздочки
│   ├── 11_accessories/                        #   Аксессуары
│   └── bearings/                              #   Статьи по подшипникам
│
├── bearings/                                  # 🔎 Расширенный справочник
│   ├── analogues/                             #   Аналоги
│   ├── brands/                                #   Бренды
│   ├── catalog/                               #   Каталог
│   ├── classification/                        #   Классификация
│   ├── designations/                          #   Обозначения
│   ├── faq/                                   #   FAQ
│   ├── glossary.md                            #   Глоссарий
│   ├── gost_comprehensive_guide.md            #   Полный гайд по ГОСТ
│   ├── guides/, standards/, training/
│   ├── MASTER_INDEX.md
│   └── README.md
│
├── wiki/                                      # 📑 Wiki-формат
│   ├── 1-osnovy-terminologiya-vybor/          #   Основы, терминология, выбор
│   ├── 2-standarty-i-markirovka/              #   Стандарты и маркировка
│   └── Home.md
│
├── prakticheskie-rukovodstva/                 # ✅ Практические руководства, кейсы, чек-листы
│                                              #   (~150 файлов: расшифровка маркировки, подбор аналогов,
│                                              #    монтаж, посадки, смазка, диагностика, и т.д.)
├── instrumenty-i-spravochniki/                # 🛠 Калькуляторы и справочники
│   ├── FAQ.md
│   ├── Кросс_ссылки_производителей.md
│   ├── Словарь_терминов.md
│   ├── Суффиксы_префиксы.md                   #   Расшифровка суффиксов и префиксов
│   ├── Таблицы_соответствий.md
│   └── README.md
├── karty-znany-i-navigatsiya/                 # 🗺 Карты знаний и навигационные схемы
├── images/                                    # 🖼 Изображения, фотографии, чертежи, схемы
├── gost/                                      # Материалы по ГОСТ
├── iso/                                       # Материалы по ISO
├── en/                                        # Англоязычные материалы (en/bearings/)
├── analogs/                                   # Аналоги (текстовая часть)
├── brands/                                    # Бренды (текстовая часть)
├── appendices/                                # Приложения (90_Приложения_таблицы_БД, legacy-appendix)
├── supplementary/                             # Дополнительные материалы (Каталоги, Номенклатура)
├── technical/                                 # Технические материалы по разделам:
│   ├── 00_ВСПОМОГАТЕЛЬНЫЕ/00_DATA/
│   ├── 01_basics/, 02_standards_marking/, 03_types_components/, 04_parameters_calculations/
│   ├── 05_operation_maintenance/, 06_failures_diagnostics/, 07_brands_manufacturers/, 08_special_reference/
│   ├── 02_Термины_и_основы/, 03_ГОСТ_подшипники_и_нормативка/
│   ├── 04_ISO_и_международные_обозначения/, 05_Маркировка_суффиксы_серии/
│   ├── 06_Аналоги_и_взаимозаменяемость/, 07_Бренды_и_каталоги/
│   ├── 08_Автомобильные_комплекты/, 09_Линейные_системы_и_передачи/
│   ├── 10_Ремни_шкивы_цепи/, 11_РТИ_рукава_уплотнения/, 12_Прочее_сопутствующее/
├── extracted/                                 # Текст, извлечённый из источников (PDF и т. д.)
├── examples/                                  # Примеры
├── it-infrastructure/                         # IT-инфраструктура (it-infrastructure/IT/)
├── archive/                                   # Архивные документы (trash_review/)
├── meta/                                      # Метаданные документации
│
├── AGENT.md                                   # Инструкции для AI-агентов
├── ARTICLE_CREATION_GUIDE.md                  # Гайд по созданию статей
├── DEMO.md                                    # Демонстрация
├── EXTRACTED_KNOWLEDGE_INDEX.md               # Индекс извлечённых знаний
├── KNOWLEDGE_BASE_BUILDER.md                  # Сборка базы знаний
├── NAVIGATION_GUIDE.md                        # Гайд по навигации
├── QUICK_REFERENCE.md                         # Краткая справка
├── QUICK_START.md                             # Быстрый старт
├── REPOSITORY_STRUCTURE.md                    # Структура репозитория
├── automation.md / automation_ru.md           # Автоматизация
```

### 📁 `data/` — Данные, таблицы, базы

Структурированные данные: каталоги производителей, размерные таблицы, **таблицы обозначений и аналогов**, схемы БД.

```
data/
├── katalogi/                                  # 🏭 Каталоги производителей (97 файлов .md)
│   ├── Каталог_подшипников_SKF.md             #   SKF (общий, высокотемпературные, и др.)
│   ├── Каталог_подшипников_FAG.md             #   FAG / INA / Schaeffler
│   ├── Каталог_подшипников_NSK.md             #   NSK
│   ├── Каталог_подшипников_NTN.md             #   NTN, NTN ULTAGE (высокопрецизионные)
│   ├── Каталог_подшипников_KOYO.md, IKO.md    #   KOYO, IKO (игольчатые)
│   ├── Каталог_подшипников_AKE.md, APB.md     #   Высокоточные, для станкостроения
│   ├── Каталог_подшипников_CRAFT.md, CX.md    #   CRAFT, CX, DAS_LAGER, EMS, FBJ, FKL, и др.
│   ├── Каталог_подшипников_Fersa.md           #   Fersa (легковые автомобили)
│   ├── Каталог_подшипников_GAMET_BEARINGS.md  #   GAMET, HARP, IBB, IBC, IBU, …
│   ├── Каталог_подшипников_HCH/HRB/HYA/INA/…  #   Китайские/европейские бренды
│   ├── Каталог_десятого_подшипникового_завода.md  # 10-ГПЗ
│   ├── Генеральный_каталог_EPK.md             #   ЕПК (Европейская подшипниковая корпорация)
│   ├── Каталог_корпусных_подшипников_FYH.md   #   FYH (корпусные)
│   ├── Каталог_игольчатых_подшипников_NBS.md  #   NBS
│   ├── Каталог_обгонных_муфт_CTS.md           #   Обгонные муфты
│   ├── Каталог_MARKES_Ролики_конвейерные.md   #   Конвейерные ролики
│   ├── Каталог_MEGADYNE.md                    #   Ремни MEGADYNE
│   ├── Ассортимент_продукции_ROLLON.md        #   Линейные направляющие ROLLON
│   ├── catalog-legacy/CAT-6205.md             #   Устаревшие версии каталогов
│   └── README.md
│
├── gost/                                      # 📋 Таблицы по ГОСТ (CSV)
│   ├── bearings.csv                           #   Подшипники по ГОСТ
│   ├── dimensions.csv                         #   Размеры
│   ├── series.csv                             #   Серии
│   └── tolerances.csv                         #   Допуски
│
├── iso/                                       # 📋 Таблицы по ISO (CSV)
│   ├── bearings.csv
│   ├── dimensions.csv
│   ├── prefixes.csv                           #   Префиксы обозначений
│   └── suffixes.csv                           #   Суффиксы обозначений
│
├── brands/                                    # 🏷 Справочники брендов (CSV)
│   ├── brands.csv                             #   Все бренды
│   ├── brand_comparison.csv                   #   Сравнение брендов
│   ├── manufacturers_asia.csv                 #   Азия
│   ├── manufacturers_china.csv                #   Китай
│   ├── manufacturers_cis.csv                  #   СНГ
│   └── manufacturers_europe.csv               #   Европа
│
├── dimensions/                                # 📏 Размерные таблицы
│   └── bearing_dimensions.csv                 #   d, D, B, r, масса
│
├── nomenclature/                              # 📜 Номенклатура (86 файлов .md по брендам)
│   ├── 10-ГПЗ.md, AAA.md, ABC.md, ADR.md,
│   ├── AKE.md, APB.md, BARDEN.md, BBC.md,
│   ├── CRAFT.md, DKF.md, EER.md, FAG.md,
│   ├── FERSA.md, FLT.md, GMN.md, GPL.md,
│   ├── GRW.md, HCH.md, HYA.md, INA.md, …      #   и т. д. (по одному на бренд)
│
├── analogs/                                   # 🔁 Таблицы аналогов
│   ├── gost_iso.csv                           #   ГОСТ ↔ ISO
│   ├── gost_to_iso.csv                        #   ГОСТ → ISO
│   ├── iso_to_gost.csv                        #   ISO → ГОСТ
│   ├── additional_designations.csv            #   Дополнительные обозначения
│   ├── import_analogs.csv                     #   Импортные аналоги
│   ├── housings.csv                           #   Корпуса
│   └── units.csv                              #   Узлы
│
├── csv/                                       # 📊 Сводные CSV-таблицы
│   ├── master_catalog.csv                     #   Главный сводный каталог
│   ├── bearing_units.csv                      #   Подшипниковые узлы
│   ├── tn_ved_codes.csv                       #   Коды ТН ВЭД ЕАЭС
│   ├── tolerance_classes.csv                  #   Классы точности
│   ├── analogs/, brands/, gost/, iso/         #   Подпапки по доменам
│
├── database/                                  # 🗄 База данных
│   ├── schema.sql                             #   Схема БД
│   └── README.md
├── schema/                                    # 🗃 SQL-схемы
│   ├── bearings_db_schema.sql                 #   Основная схема
│   └── d1_schema.sql                          #   Схема для Cloudflare D1
├── schemas/                                   # 📐 YAML-схемы валидации
│   ├── analogs.yaml, brand_descriptions.yaml,
│   ├── brands.yaml, gost.yaml, iso.yaml,
│   ├── nomenclature.yaml
│   └── README.md
├── sql/                                       # 💾 SQL-скрипты
│   └── init_catalog.sql                       #   Инициализация каталога
│
├── tables/                                    # Таблицы (Markdown)
├── raw/                                       # Сырые данные
├── inbox/                                     # Входящие файлы для обработки (inbox/inbox/)
├── reports/                                   # Отчёты (например, 2025-12-30_source.json)
├── assets/                                    # Ассеты для данных
├── sources-legacy/                            # Устаревшие источники
│   ├── EXTRACTION_STATUS.md                   #   Статус извлечения
│   ├── PDF_EXTRACTION_METHODOLOGY.md          #   Методология извлечения из PDF
│   ├── RAW_INDEX.md, VERSION_CONTROL.md
│   ├── analogs/, brands/, catalogs/, gost/,
│   ├── iso/, skf/, vendor_catalogs/
│   └── bearing_dimensions_*.json              #   Серии 6000/6200/6300/angular_contact
│
├── articles.xlsx                              # 📊 Excel: список статей
├── bearing_directory.xlsx                     # 📊 Excel: справочник подшипников
├── articles_list.csv                          # CSV: список статей
├── brands.csv                                 # CSV: бренды (корневой)
├── nomenclature.csv                           # CSV: номенклатура (корневая)
└── README.md
```

### 📁 `src/` — Исходный код Python

Логика парсинга, обработки и API.

```
src/
├── __init__.py                                # Инициализация пакета
├── __main__.py                                # Точка входа `python -m src`
├── cli.py                                     # CLI-интерфейс
├── catalog.py                                 # Работа с каталогом подшипников
├── config.py                                  # Загрузка конфигурации
├── logger.py                                  # Логирование
├── parser.py                                  # Парсер обозначений
├── processor.py                               # Обработка данных
├── registry.py                                # Реестр
├── utils.py                                   # Утилиты
├── watcher.py                                 # Отслеживание изменений
│
├── api/                                       # 🌐 REST API
│   ├── main.py                                #   Точка входа API
│   ├── app/                                   #   Приложение (роуты, модели)
│   ├── examples/                              #   Примеры запросов
│   ├── scripts/                               #   Скрипты сопровождения
│   ├── sql/                                   #   SQL-запросы API
│   ├── tests/                                 #   Тесты API
│   ├── mar_Dockerfile, mar_requirements.txt
│   └── README.md
│
└── sources/                                   # 📥 Извлечение из источников
    ├── pdf_text_extractor.py                  #   Извлечение текста из PDF
    ├── table_scraper.py                       #   Скрапинг таблиц
    └── brands_json_to_csv.py                  #   Конвертация JSON → CSV брендов
```

### 📁 `tools/` — Утилиты, скрипты, автоматизация

```
tools/
├── scripts/                                   # 🐍 Python-скрипты сборки и обработки
│   ├── build_knowledge_base.py                #   Сборка базы знаний
│   ├── build_complete_knowledge_base.py       #   Полная сборка БЗ
│   ├── build_enhanced_knowledge_base.py       #   Расширенная сборка БЗ
│   ├── build_ultra_comprehensive_kb.py        #   Максимально полная БЗ
│   ├── build_search_index.py                  #   Сборка поискового индекса
│   ├── build_autocomplete_dict.py             #   Словарь автодополнения
│   ├── build_bearings_seed.py                 #   Сидирование подшипников
│   ├── check_data_sources.py                  #   Проверка источников данных
│   ├── deduplicate_nomenclature.py            #   Дедупликация номенклатуры
│   ├── generate_sources_table.py              #   Генерация таблицы источников
│   ├── import_bearings_to_db.py               #   Импорт в БД
│   ├── pdf_extractor_optimized.py             #   Оптимизированный PDF-экстрактор
│   ├── move_all_to_inbox.py                   #   Перемещение в inbox
│   ├── fix_articles_structure.py              #   Исправление структуры статей
│   ├── mar_manage.py                          #   Управление MAR-подпроектом
│   ├── extract/                               #   Скрипты извлечения
│   ├── validate/                              #   Скрипты валидации
│   └── examples/                              #   Примеры использования
├── bin/                                       # Бинарные/исполняемые утилиты
└── README.md
```

### 📁 `config/` — Конфигурационные файлы

```
config/
├── app.yaml                                   # Основная конфигурация приложения
├── brand_aliases.json                         # Синонимы и алиасы брендов
├── parsing_rules.json                         # Правила парсинга обозначений
├── mar_Dockerfile                             # Dockerfile подпроекта MAR
├── mar_docker-compose.yml                     # docker-compose MAR
├── mar_Makefile                               # Makefile MAR
├── mar_pyproject.toml                         # pyproject MAR
└── mar_requirements.txt                       # Зависимости MAR
```

### 📁 `tests/` — Тесты (pytest)

```
tests/
├── conftest.py                                # Общие фикстуры pytest
├── test_automation_pipeline.py                # Автоматизационный пайплайн
├── test_code_normalization.py                 # Нормализация кодов
├── test_dedup.py / test_deduplication.py      # Дедупликация
├── test_dimensions.py                         # Размеры
├── test_knowledge_base_builder.py             # Сборщик БЗ
├── test_processor.py                          # Процессор
├── test_schema_validation.py / test_schemas.py# Валидация схем
├── test_suffixes.py                           # Суффиксы обозначений
├── test_table_scraper.py                      # Скрапинг таблиц
└── test_validators.py                         # Валидаторы
```

### 📁 `archive/` — Архив

```
archive/
├── zip/                                       # Zip-архивы исходников
│   ├── book.zip, book.z01.zip, book.z02.zip   #   Многотомный архив
│   ├── bearing_handbook_pkg.rar               #   RAR справочник
│   ├── 01_basics/                             #   Основы (распакованное)
│   ├── 03_types_components/                   #   Типы и компоненты
│   └── 04_parameters_calculations/            #   Параметры и расчёты
└── docs-legacy/                               # Устаревшая документация
    ├── README-api.md                          #   Старое README API
    ├── README-baza.md                         #   Старое README базы
    └── README-mar.md                          #   Старое README MAR
```

### 📁 `sources/` — Источники данных

Исходные источники (PDF, документы, ссылки) — описание в `sources/README.md`.

### 📁 `Подшипники/` — Исходные русскоязычные материалы

Оригинальные русскоязычные исходные материалы:
```
Подшипники/
└── 4.16. Большие подшипники/                  # Тематические подшипниковые материалы
```

### 📁 `.github/` — Конфигурация GitHub

GitHub Actions workflows, шаблоны issue/PR, конфигурация Dependabot и CodeQL.

### 📁 `.vscode/` — Настройки редактора

Настройки VS Code для проекта.

### 📄 Файлы в корне репозитория

| Файл | Назначение |
| --- | --- |
| `README.md` | Главная страница проекта и навигация (этот файл) |
| `AGENT.md` | Инструкции для AI-агентов, работающих с репозиторием |
| `CONTRIBUTING.md` | Правила контрибьюции |
| `SECURITY.md` | Политика безопасности |
| `CODEOWNERS` | Владельцы кода (review) |
| `LICENSE` | Лицензия MIT |
| `QA_AUDIT_REPORT.md` | Отчёт по качеству репозитория |
| `Makefile` | Задачи сборки/линтинга/тестов |
| `manage.py` | Управляющий скрипт проекта |
| `Dockerfile` | Контейнеризация приложения |
| `docker-compose.yml` | Compose-конфигурация |
| `pyproject.toml` | Конфигурация Python-проекта (зависимости, инструменты) |
| `requirements.txt` | Runtime-зависимости |
| `requirements-dev.txt` | Dev-зависимости |
| `.editorconfig` | Стиль кода для редакторов |
| `.gitignore` | Игнорируемые файлы Git |
| `.pre-commit-config.yaml` | Конфигурация pre-commit хуков |

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
