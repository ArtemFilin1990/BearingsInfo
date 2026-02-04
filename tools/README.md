# Инструменты и утилиты BearingsInfo

## Назначение

Данный раздел содержит набор инструментов, скриптов и утилит для работы с репозиторием BearingsInfo. Инструменты предназначены для автоматизации задач по валидации данных, импорту/экспорту информации, построению индексов для поиска, генерации документации и поддержки баз данных подшипников. Материал предназначен для разработчиков, контрибьюторов репозитория и администраторов баз данных.

## Содержание каталога

### 1. Скрипты валидации данных (Data Validation Scripts)

**Назначение:** Проверка корректности и полноты данных в справочных таблицах, каталогах подшипников и технических спецификациях.

**Основные скрипты:**

**1.1. `validate_bearing_data.py`**
- **Функция:** Проверка таблиц с размерами и характеристиками подшипников на соответствие стандартам (ГОСТ, ISO)
- **Проверки:**
  - Корректность диапазонов размеров (d, D, B)
  - Наличие всех обязательных полей (грузоподъемность C, C₀, частота вращения)
  - Соответствие обозначений правилам (например, 6205 должен иметь d=25 мм, D=52 мм)
  - Проверка на дублирующиеся записи
- **Использование:**
  ```bash
  python tools/validate_bearing_data.py --input data/bearings/radial_ball_bearings.csv --standard ISO
  ```
- **Выход:** Отчет с ошибками и предупреждениями (JSON или HTML)

**1.2. `check_cross_references.py`**
- **Функция:** Проверка перекрестных ссылок между разделами (например, ссылки на смежные темы в README.md)
- **Проверки:**
  - Все внутренние ссылки (Markdown links) ведут на существующие файлы
  - Ссылки на изображения корректны
  - Нет "мертвых" ссылок на внешние ресурсы (опционально)
- **Использование:**
  ```bash
  python tools/check_cross_references.py --root .
  ```

**1.3. `validate_tables.py`**
- **Функция:** Проверка форматирования таблиц в Markdown-файлах
- **Проверки:**
  - Одинаковое количество колонок во всех строках таблицы
  - Корректность разделителей (`|`)
  - Наличие заголовков таблиц
- **Использование:**
  ```bash
  python tools/validate_tables.py --file "4. Расчёт и параметры/4.1. Грузоподъемность и долговечность/README.md"
  ```

---

### 2. Импорт и экспорт данных (Import/Export Utilities)

**Назначение:** Конвертация данных между различными форматами (CSV, JSON, SQL, Excel) для интеграции с внешними системами.

**2.1. `import_manufacturer_catalog.py`**
- **Функция:** Импорт каталогов производителей (SKF, NSK, NTN, FAG) в унифицированный формат
- **Входные форматы:** PDF (через парсинг таблиц), Excel, CSV
- **Выходной формат:** JSON или CSV с полями:
  - Обозначение подшипника
  - Размеры (d, D, B)
  - Грузоподъемность (C, C₀)
  - Предельная частота вращения
  - Масса
  - Аналоги (опционально)
- **Использование:**
  ```bash
  python tools/import_manufacturer_catalog.py --input catalogs/SKF_2023.xlsx --manufacturer SKF --output data/bearings/skf_catalog.json
  ```

**2.2. `export_to_sql.py`**
- **Функция:** Экспорт данных подшипников в SQL-базу данных (SQLite, PostgreSQL, MySQL)
- **Схема базы данных:**
  - Таблица `bearings` (обозначение, тип, размеры, грузоподъемность)
  - Таблица `manufacturers` (производители)
  - Таблица `analogues` (кросс-таблица аналогов)
- **Использование:**
  ```bash
  python tools/export_to_sql.py --input data/bearings/ --database bearings.db --engine sqlite
  ```

**2.3. `generate_excel_catalog.py`**
- **Функция:** Создание Excel-каталога подшипников с фильтрами и сводными таблицами
- **Возможности:**
  - Автоматическое форматирование (цветовое кодирование по типам подшипников)
  - Встроенные формулы для расчета долговечности
  - Фильтры по размерам, типам, производителям
- **Использование:**
  ```bash
  python tools/generate_excel_catalog.py --input data/bearings/ --output BearingsInfo_Catalog_2024.xlsx
  ```

---

### 3. Инструменты для работы с базой данных (Database Tools)

**3.1. `init_database.py`**
- **Функция:** Инициализация базы данных подшипников с нуля
- **Создаваемые таблицы:**
  - `bearings` — основная таблица подшипников
  - `manufacturers` — справочник производителей
  - `bearing_types` — типы подшипников (радиальные, упорные, конические и т.д.)
  - `standards` — стандарты (ГОСТ, ISO, DIN)
  - `analogues` — таблица аналогов
- **Использование:**
  ```bash
  python tools/init_database.py --database bearings.db
  ```

**3.2. `query_bearings.py`**
- **Функция:** CLI-инструмент для поиска подшипников по параметрам
- **Примеры запросов:**
  ```bash
  # Найти все подшипники с внутренним диаметром 25 мм
  python tools/query_bearings.py --d 25
  
  # Найти конические роликоподшипники с C > 50 kN
  python tools/query_bearings.py --type "tapered roller" --C_min 50000
  
  # Найти аналог подшипника 6205
  python tools/query_bearings.py --analogue 6205
  ```

**3.3. `update_prices.py`**
- **Функция:** Обновление цен на подшипники из внешних источников (API дистрибьюторов, веб-скрейпинг)
- **Источники:** exist.ru, emex.ru, или CSV-файлы от поставщиков
- **Использование:**
  ```bash
  python tools/update_prices.py --source exist_api --api_key YOUR_API_KEY --database bearings.db
  ```

---

### 4. Построение поисковых индексов (Search and Autocomplete)

**4.1. `build_search_index.py`**
- **Функция:** Построение полнотекстового поискового индекса для быстрого поиска по обозначениям, производителям, описаниям
- **Технологии:** Elasticsearch, Whoosh (Python), или SQLite FTS (Full-Text Search)
- **Индексируемые поля:**
  - Обозначение подшипника
  - Описание (тип, серия)
  - Производитель
  - Теги (применение, отрасль)
- **Использование:**
  ```bash
  python tools/build_search_index.py --input data/bearings/ --output indexes/bearings_index
  ```

**4.2. `autocomplete_generator.py`**
- **Функция:** Генерация JSON-файла для автодополнения в веб-интерфейсах или мобильных приложениях
- **Выход:** Список всех обозначений подшипников для быстрого автодополнения при вводе
- **Пример выходного файла (`autocomplete.json`):**
  ```json
  {
    "bearings": [
      {"label": "6205", "type": "Deep Groove Ball Bearing", "d": 25, "D": 52},
      {"label": "6205-2RS", "type": "Deep Groove Ball Bearing (sealed)", "d": 25, "D": 52},
      {"label": "7210 B", "type": "Angular Contact Ball Bearing", "d": 50, "D": 90}
    ]
  }
  ```
- **Использование:**
  ```bash
  python tools/autocomplete_generator.py --input data/bearings/ --output web/autocomplete.json
  ```

---

### 5. Генерация документации (Documentation Generators)

**5.1. `generate_index.py`**
- **Функция:** Автоматическая генерация файла `INDEX.md` с навигацией по всем разделам репозитория
- **Возможности:**
  - Сканирование всех `README.md` файлов
  - Извлечение заголовков и краткого описания (из раздела "Назначение")
  - Построение дерева оглавления с ссылками
- **Использование:**
  ```bash
  python tools/generate_index.py --root . --output INDEX.md
  ```

**5.2. `generate_pdf_handbook.py`**
- **Функция:** Конвертация всех Markdown-файлов в единое PDF-руководство
- **Технологии:** Pandoc, WeasyPrint, или LaTeX
- **Использование:**
  ```bash
  python tools/generate_pdf_handbook.py --input . --output BearingsInfo_Handbook.pdf --template templates/handbook.tex
  ```

**5.3. `stats_report.py`**
- **Функция:** Генерация статистического отчета по репозиторию
- **Метрики:**
  - Количество разделов и подразделов
  - Количество таблиц и строк данных
  - Количество подшипников в базе (по типам)
  - Полнота данных (процент заполненных полей)
- **Выход:** HTML или Markdown отчет
- **Использование:**
  ```bash
  python tools/stats_report.py --root . --output reports/stats_2024.html
  ```

---

### 6. Утилиты для контрибьюторов (Contributor Utilities)

**6.1. `new_section.py`**
- **Функция:** Создание новой секции репозитория по шаблону
- **Создаваемая структура:**
  ```
  Новая секция/
  ├── README.md (с заполненными разделами: Назначение, Ключевые вопросы, Содержание, Таблицы/данные, Источники)
  ├── images/ (пустая папка для изображений)
  └── data/ (пустая папка для CSV-файлов)
  ```
- **Использование:**
  ```bash
  python tools/new_section.py --name "10. Новый раздел" --title "Специальные подшипники для космической отрасли"
  ```

**6.2. `lint_markdown.py`**
- **Функция:** Проверка Markdown-файлов на соответствие стилевым соглашениям
- **Проверки:**
  - Единообразие заголовков (H1, H2, H3)
  - Корректность ссылок
  - Наличие пустых строк перед заголовками
  - Отсутствие trailing whitespace
- **Использование:**
  ```bash
  python tools/lint_markdown.py --file "1. Подшипники. Общая информация/README.md"
  ```

**6.3. `contributors_report.py`**
- **Функция:** Генерация отчета о вкладе контрибьюторов в репозиторий (на основе Git истории)
- **Метрики:**
  - Количество коммитов
  - Количество добавленных строк
  - Количество измененных файлов
- **Использование:**
  ```bash
  python tools/contributors_report.py --output CONTRIBUTORS.md
  ```

---

### 7. Скрипты для анализа данных (Data Analysis Scripts)

**7.1. `bearing_size_distribution.py`**
- **Функция:** Построение графиков распределения размеров подшипников (гистограммы по d, D, B)
- **Выход:** PNG, SVG или интерактивный HTML (Plotly)
- **Использование:**
  ```bash
  python tools/bearing_size_distribution.py --input data/bearings/radial_ball_bearings.csv --output reports/size_distribution.png
  ```

**7.2. `manufacturer_comparison.py`**
- **Функция:** Сравнение характеристик подшипников разных производителей (грузоподъемность, цена, доступность)
- **Визуализация:** Сравнительные таблицы, графики
- **Использование:**
  ```bash
  python tools/manufacturer_comparison.py --bearing 6205 --manufacturers SKF,NSK,FAG,Koyo --output reports/6205_comparison.html
  ```

---

## Установка и использование инструментов

### Требования

**Python 3.8+**

**Зависимости (установка):**
```bash
# Клонирование репозитория
git clone https://github.com/your-repo/BearingsInfo.git
cd BearingsInfo

# Установка зависимостей
pip install -r requirements-dev.txt
```

**Основные библиотеки:**
- `pandas` — работа с табличными данными
- `openpyxl` — импорт/экспорт Excel
- `SQLAlchemy` — работа с базами данных
- `markdown` — парсинг Markdown
- `beautifulsoup4` — парсинг HTML (для импорта каталогов)
- `plotly` / `matplotlib` — визуализация данных
- `click` — CLI-интерфейсы для скриптов

### Примеры использования

**Пример 1: Валидация всех данных перед коммитом**
```bash
# Запуск всех проверок
python tools/validate_bearing_data.py --input data/bearings/ --report validation_report.html
python tools/check_cross_references.py --root .
python tools/lint_markdown.py --root .
```

**Пример 2: Импорт нового каталога SKF**
```bash
# Импорт Excel-каталога SKF
python tools/import_manufacturer_catalog.py \
  --input catalogs/SKF_General_Catalogue_2024.xlsx \
  --manufacturer SKF \
  --output data/bearings/skf_2024.json

# Экспорт в базу данных
python tools/export_to_sql.py \
  --input data/bearings/skf_2024.json \
  --database bearings.db \
  --engine sqlite
```

**Пример 3: Построение поискового индекса для веб-приложения**
```bash
# Построение индекса
python tools/build_search_index.py \
  --input data/bearings/ \
  --output indexes/bearings_index

# Генерация автодополнения
python tools/autocomplete_generator.py \
  --input data/bearings/ \
  --output web/autocomplete.json
```

**Пример 4: Генерация PDF-руководства**
```bash
# Конвертация всех Markdown в PDF
python tools/generate_pdf_handbook.py \
  --input . \
  --output BearingsInfo_Handbook_2024.pdf \
  --toc \
  --cover templates/cover.png
```

---

## Структура каталога `tools/`

```
tools/
├── README.md                      # Этот файл (документация по инструментам)
├── requirements.txt               # Зависимости Python для инструментов
├── validate_bearing_data.py       # Валидация данных подшипников
├── check_cross_references.py      # Проверка ссылок
├── validate_tables.py             # Валидация таблиц в Markdown
├── import_manufacturer_catalog.py # Импорт каталогов производителей
├── export_to_sql.py               # Экспорт в SQL
├── generate_excel_catalog.py      # Генерация Excel-каталога
├── init_database.py               # Инициализация БД
├── query_bearings.py              # CLI-поиск подшипников
├── update_prices.py               # Обновление цен
├── build_search_index.py          # Построение поискового индекса
├── autocomplete_generator.py      # Генерация автодополнения
├── generate_index.py              # Генерация оглавления
├── generate_pdf_handbook.py       # Генерация PDF
├── stats_report.py                # Статистический отчет
├── new_section.py                 # Создание новой секции
├── lint_markdown.py               # Проверка Markdown
├── contributors_report.py         # Отчет о контрибьюторах
├── bearing_size_distribution.py   # Анализ распределения размеров
├── manufacturer_comparison.py     # Сравнение производителей
└── templates/                     # Шаблоны для генерации документов
    ├── README_template.md         # Шаблон для новой секции
    ├── handbook.tex               # LaTeX-шаблон для PDF
    └── cover.png                  # Обложка для PDF-руководства
```

---

## Вклад в развитие инструментов

Если вы хотите добавить новый инструмент или улучшить существующий:

1. **Создайте issue** в репозитории с описанием функциональности
2. **Напишите скрипт** в каталоге `tools/`
3. **Добавьте документацию** в этот README.md (раздел с описанием вашего инструмента)
4. **Добавьте тесты** (если применимо) в `tests/tools/`
5. **Создайте Pull Request**

**Требования к инструментам:**
- CLI-интерфейс с использованием библиотеки `click` или `argparse`
- Подробная help-справка (`--help`)
- Обработка ошибок с понятными сообщениями
- Логирование (с уровнями INFO, WARNING, ERROR)
- Документация в коде (docstrings)

---

## Лицензия

Все инструменты в каталоге `tools/` распространяются под той же лицензией, что и основной репозиторий BearingsInfo (см. LICENSE в корне репозитория).

---

## Контакты и поддержка

По вопросам работы инструментов обращайтесь:
- **Issues:** https://github.com/your-repo/BearingsInfo/issues
- **Discussions:** https://github.com/your-repo/BearingsInfo/discussions
- **Email:** support@bearingsinfo.example (замените на реальный)

---

## История изменений (Changelog)

### v1.0.0 (2024-01-15)
- Начальный набор инструментов: валидация, импорт/экспорт, генерация документации
- Поддержка SQLite, PostgreSQL, Excel, JSON

### v1.1.0 (планируется)
- Добавление веб-скрейперов для автоматического обновления цен
- Интеграция с API производителей (SKF, NSK)
- Инструменты машинного обучения для предсказания ресурса подшипников
