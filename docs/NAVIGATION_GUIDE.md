# Навигация по базе данных подшипников

> **Руководство по быстрому поиску нужной информации в репозитории**

[🏠 На главную](../../README.md) | [🗂️ Мастер-индекс](bearings/MASTER_INDEX.md)

---

## Быстрый доступ

### 🚀 Я хочу...

| Задача | Куда идти |
|--------|-----------|
| **Найти аналог подшипника ГОСТ** | → [Таблица аналогов](bearings/analogues/complete_analogues_table.md) |
| **Подобрать подшипник для оборудования** | → [Справочник подбора](bearings/selection_guide.md) |
| **Расшифровать обозначение** | → [Обозначения ГОСТ](bearings/designations/gost.md) / [ISO](bearings/designations/iso.md) |
| **Узнать о производителе** | → [Международные бренды](bearings/brands/international_brands.md) |
| **Понять суффиксы и префиксы** | → [Кросс-референс суффиксов](bearings/designations/manufacturer_suffixes_cross_reference.md) |
| **Найти стандарт ГОСТ** | → [Стандарты ГОСТ](bearings/standards/gost_standards.md) |
| **Изучить смазки и материалы** | → [Руководство ГОСТ](bearings/gost_comprehensive_guide.md) |
| **Посмотреть практические примеры** | → [Практические кейсы](bearings/practical_examples.md) |
| **Обучить менеджера** | → [Руководство для менеджеров](bearings/training/managers_guide.md) |

---

## Структура базы данных

### 📂 Основные разделы

```
docs/
├── encyclopedia/                       # Разделы 01-09
│   ├── 01-podshipniki-obshaya-informatsiya/
│   ├── 02-standarty-i-markirovka/
│   ├── 03-tipy-i-elementy/
│   ├── 04-raschet-i-parametry/
│   ├── 05-ekspluatatsiya-i-obsluzhivanie/
│   ├── 06-otkazy-i-diagnostika/
│   ├── 07-brendy-i-proizvoditeli/
│   ├── 08-spetsialnye-ispolneniya-i-spravka/
│   └── 09-soputstvuyushchie-izdeliya/
├── kb/                                  # Курсы и база знаний
│   ├── knowledge-base/
│   ├── uchebnik/
│   ├── uchebnik-akademichesky/
│   ├── vvodny-kurs-dlya-novichkov/
│   └── testy/
├── bearings/                           # Основная документация
│   ├── MASTER_INDEX.md                 # 🔍 Главный навигатор
│   ├── selection_guide.md              # 📖 Справочник подбора
│   ├── practical_examples.md           # 💡 Практические кейсы
│   ├── gost_comprehensive_guide.md     # 📘 Полное руководство ГОСТ
│   ├── glossary.md                     # 📚 Глоссарий терминов
│   │
│   ├── analogues/                      # Аналоги подшипников
│   │   ├── README.md                   # Обзор раздела
│   │   ├── complete_analogues_table.md # 📋 Полная таблица (2000+ записей)
│   │   ├── gost_iso_table.md           # Таблица ГОСТ ↔ ISO
│   │   ├── bearing_units.md            # Аналоги узлов
│   │   └── analog_examples.md          # Примеры подбора
│   │
│   ├── brands/                         # Производители и бренды
│   │   ├── international_brands.md     # 🏭 Классификация брендов
│   │   ├── supplier_directory.md       # Каталог поставщиков
│   │   ├── skf_overview.md             # Обзор SKF
│   │   ├── skf_designation_system.md   # 🔤 Система обозначений SKF
│   │   └── brands.md             # Бренды 
│   │
│   ├── designations/                   # Системы обозначений
│   │   ├── README.md                   # Обзор систем
│   │   ├── gost.md                     # 🇷🇺 Обозначения ГОСТ
│   │   ├── iso.md                      # 🌍 Обозначения ISO
│   │   ├── iso_suffixes.md             # Суффиксы ISO
│   │   └── manufacturer_suffixes_cross_reference.md  # 🔀 Кросс-референс (300+ записей)
│   │
│   ├── standards/                      # Стандарты
│   │   └── gost_standards.md           # Стандарты ГОСТ
│   │
│   ├── classification/                 # Классификация
│   │   └── README.md                   # Типы подшипников
│   │
│   ├── catalog/                        # Каталог подшипников
│   │   └── README.md                   # Каталог
│   │
│   ├── guides/                         # Практические руководства
│   │   └── README.md                   # Инструкции
│   │
│   ├── training/                       # Обучающие материалы
│   │   └── managers_guide.md           # 👨‍💼 Для менеджеров
│   │
│   └── faq/                            # Часто задаваемые вопросы
│       ├── README.md                   # Общие вопросы
│       └── imported_bearings.md        # Импортные подшипники
│
└── EXTRACTED_KNOWLEDGE_INDEX.md        # Индекс извлеченных знаний

sources/                                 # Источники данных
├── literature.md                        # 📚 Библиография
├── EXTRACTION_STATUS.md                 # ✅ Статус обработки источников
├── RAW_INDEX.md                         # Индекс сырых файлов
└── vendor_catalogs/                     # Метаданные каталогов производителей

Аналоги/                                 # Таблицы аналогов (дополнительно)
├── nsk_ntn_koyo_аналоги.md             # Японские производители

Таблицы/                                 # Справочные таблицы
├── размеры.md                          # Размеры подшипников
├── серии.md                            # Серии подшипников
└── суффиксы_производителей.md          # Суффиксы NSK/NTN/KOYO
```

---

## Типы поиска

### 1. Поиск по задаче

#### Замена сломанного подшипника
1. [Идентифицируйте обозначение](bearings/designations/gost.md)
2. [Найдите аналог в таблице](bearings/analogues/complete_analogues_table.md)
3. [Выберите производителя](bearings/brands/international_brands.md)
4. [Проверьте технические характеристики](bearings/selection_guide.md)

#### Подбор подшипника для нового оборудования
1. [Определите тип нагрузки](bearings/classification/README.md)
2. [Выберите тип подшипника](bearings/selection_guide.md#шаг-1-определение-типа-и-размера-по-гост)
3. [Рассчитайте размер](bearings/selection_guide.md)
4. [Посмотрите примеры](bearings/practical_examples.md)

#### Обучение нового сотрудника
1. [Начните с руководства для менеджеров](bearings/training/managers_guide.md)
2. [Изучите основы ГОСТ](bearings/gost_comprehensive_guide.md)
3. [Практикуйтесь на примерах](bearings/practical_examples.md)
4. [Пользуйтесь глоссарием](bearings/glossary.md)

### 2. Поиск по типу подшипника

#### Шариковые радиальные (6xxx)
- [Классификация](bearings/classification/README.md)
- [Обозначения ГОСТ](bearings/designations/gost.md)
- [Таблица аналогов](bearings/analogues/complete_analogues_table.md)
- [Размеры](Таблицы/размеры.md)

#### Роликовые цилиндрические (NU, NJ, N)
- [Обозначения ISO](bearings/designations/iso.md)
- [Аналоги NSK/NTN/KOYO](Аналоги/nsk_ntn_koyo_аналоги.md)
- [Практические примеры](bearings/practical_examples.md#кейс-8)

#### Конические роликовые (3xxx, 7xxx)
- [Руководство ГОСТ](bearings/gost_comprehensive_guide.md)
- [Практический кейс](bearings/practical_examples.md#кейс-4)

#### Сферические роликовые (3xxx)
- [Практический кейс - дробилка](bearings/practical_examples.md#кейс-6)

#### Игольчатые (NA, NK, RNA, NKI)
- [Практический кейс - редуктор](bearings/practical_examples.md#кейс-2)

#### Упорные (8xxx)
- [Практический кейс - поворотный стол](bearings/practical_examples.md#кейс-7)

### 3. Поиск по производителю

#### SKF (Швеция)
- [Обзор бренда](bearings/brands/skf_overview.md)
- [Система обозначений SKF](bearings/brands/skf_designation_system.md)
- [Кросс-референс суффиксов](bearings/designations/manufacturer_suffixes_cross_reference.md)

#### NSK, NTN, KOYO (Япония)
- [Аналоги японских производителей](Аналоги/nsk_ntn_koyo_аналоги.md)
- [Суффиксы NSK/NTN/KOYO](Таблицы/суффиксы_производителей.md)
- [Общая таблица аналогов](bearings/analogues/complete_analogues_table.md)

#### FAG, INA (Schaeffler, Германия)
- [Международные бренды](bearings/brands/international_brands.md)
- [Кросс-референс суффиксов](bearings/designations/manufacturer_suffixes_cross_reference.md)

#### Все производители
- [Классификация по сегментам](bearings/brands/international_brands.md)
- [Каталог поставщиков](bearings/brands/supplier_directory.md)

### 4. Поиск по стандарту

#### ГОСТ
- [Обозначения ГОСТ](bearings/designations/gost.md)
- [Стандарты ГОСТ](bearings/standards/gost_standards.md)
- [Полное руководство ГОСТ](bearings/gost_comprehensive_guide.md)

#### ISO
- [Обозначения ISO](bearings/designations/iso.md)
- [Суффиксы ISO](bearings/designations/iso_suffixes.md)
- [Таблица ГОСТ ↔ ISO](bearings/analogues/gost_iso_table.md)

---

## Поиск по ключевым словам

### Технические термины

| Термин | Где найти |
|--------|-----------|
| Грузоподъемность | [Руководство ГОСТ](bearings/gost_comprehensive_guide.md#2-основные-параметры) |
| Класс точности | [Руководство ГОСТ](bearings/gost_comprehensive_guide.md#9-классы-точности) |
| Радиальный зазор | [Руководство ГОСТ](bearings/gost_comprehensive_guide.md#10-тепловые-зазоры) |
| Смазка | [Руководство ГОСТ](bearings/gost_comprehensive_guide.md#11-смазки) |
| Сепаратор | [Руководство ГОСТ](bearings/gost_comprehensive_guide.md#8-сепараторы) |
| Уплотнения | [Кросс-референс суффиксов](bearings/designations/manufacturer_suffixes_cross_reference.md) |
| Посадка | [Практические примеры](bearings/practical_examples.md) |

### Применения

| Применение | Где найти |
|------------|-----------|
| Электродвигатель | [Кейс 1](bearings/practical_examples.md#кейс-1) |
| Редуктор | [Кейс 2](bearings/practical_examples.md#кейс-2) |
| Шпиндель | [Кейс 3](bearings/practical_examples.md#кейс-3) |
| Конвейер | [Кейс 4](bearings/practical_examples.md#кейс-4) |
| Насос | [Кейс 5](bearings/practical_examples.md#кейс-5) |
| Дробилка | [Кейс 6](bearings/practical_examples.md#кейс-6) |

---

## Советы по эффективному поиску

### 1. Начните с Мастер-индекса
[Мастер-индекс](bearings/MASTER_INDEX.md) - это главный навигационный центр с тегами и фильтрами.

### 2. Используйте поиск по файлам
В GitHub можно использовать поиск по содержимому файлов:
- Нажмите `/` для открытия поиска
- Введите ключевое слово (например, "6205")
- Фильтруйте по типу файла (Markdown)

### 3. Следуйте перекрестным ссылкам
Все документы содержат ссылки на связанные разделы - используйте их для навигации.

### 4. Сохраните закладки
Добавьте в закладки часто используемые страницы:
- [Таблица аналогов](bearings/analogues/complete_analogues_table.md) - для ежедневной работы
- [Справочник подбора](bearings/selection_guide.md) - для консультаций клиентов
- [Практические примеры](bearings/practical_examples.md) - для решения нестандартных задач

### 5. Проверяйте статус источников
[Статус извлечения данных](../sources/EXTRACTION_STATUS.md) показывает, какие источники уже обработаны, а какие планируются.

---

## Часто задаваемые вопросы

### Как найти аналог подшипника ГОСТ?
1. Откройте [Таблицу аналогов](bearings/analogues/complete_analogues_table.md)
2. Найдите обозначение ГОСТ (Ctrl+F)
3. Посмотрите соответствующие импортные обозначения
4. Проверьте размеры (d, D, B) - они должны совпадать!

### Как расшифровать обозначение подшипника?
- **Для ГОСТ**: [Обозначения ГОСТ](bearings/designations/gost.md)
- **Для ISO**: [Обозначения ISO](bearings/designations/iso.md)
- **Для SKF**: [Система обозначений SKF](bearings/brands/skf_designation_system.md)

### Как выбрать производителя?
Смотрите [Классификацию по сегментам](bearings/brands/international_brands.md):
- Премиум: SKF, FAG, NSK
- Средний класс: NTN, KOYO, Timken
- Бюджет: Китайские, российские

### Где найти практические примеры?
[Практические кейсы](bearings/practical_examples.md) содержат 8 детальных примеров для различных применений.

### Как обучить нового сотрудника?
Начните с [Руководства для менеджеров](bearings/training/managers_guide.md), затем переходите к [Справочнику подбора](bearings/selection_guide.md).

---

## Обратная связь

Если вы не нашли нужную информацию или у вас есть предложения по улучшению навигации, создайте Issue в репозитории.

---

## Полезные ссылки

- [🏠 Главная страница](../../README.md)
- [🗂️ Мастер-индекс](bearings/MASTER_INDEX.md)
- [📖 Справочник подбора](bearings/selection_guide.md)
- [💡 Практические примеры](bearings/practical_examples.md)
- [📋 Таблица аналогов](bearings/analogues/complete_analogues_table.md)
- [📚 Библиография](../sources/literature.md)
- [✅ Статус извлечения](../sources/EXTRACTION_STATUS.md)

---

**Дата создания**: 2025-12-29  
**Последнее обновление**: 2025-12-29
