# Bearings Info — Справочник по подшипникам

Систематизация информации о подшипниках: устройство, классификация, выбор, эксплуатация и сопутствующая документация.

## 📁 Структура репозитория

После реорганизации репозиторий имеет следующую структуру:

```
BearingsInfo/
├── docs/                    # 📚 Вся документация
│   ├── 01-podshipniki-obshaya-informatsiya/
│   ├── 02-standarty-i-markirovka/
│   ├── 03-tipy-i-elementy/
│   ├── 04-raschet-i-parametry/
│   ├── 05-ekspluatatsiya-i-obsluzhivanie/
│   ├── 06-otkazy-i-diagnostika/
│   ├── 07-brendy-i-proizvoditeli/
│   ├── 08-spetsialnye-ispolneniya-i-spravka/
│   ├── 09-soputstvuyushchie-izdeliya/
│   ├── images/              # Изображения и схемы
│   ├── prakticheskie-rukovodstva/
│   └── ...
├── data/                    # 📊 Данные, базы, таблицы
│   ├── katalogi/
│   ├── schemas/
│   ├── sql/
│   └── *.csv, *.xlsx
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

## Навигация по репозиторию

### Основные разделы

- **[1. Подшипники. Общая информация](<docs/01-podshipniki-obshaya-informatsiya/README.md>)** — Термины, классификация, устройство, алгоритм выбора
- **[2. Стандарты и маркировка](<docs/02-standarty-i-markirovka/README.md>)** — ГОСТ, ISO, DIN, система обозначений, аналоги
- **[3. Типы и элементы](<docs/03-tipy-i-elementy/README.md>)** — Шариковые, роликовые, конические, сепараторы, узлы
- **[4. Расчёт и параметры](<docs/04-raschet-i-parametry/README.md>)** — Нагрузки, ресурс, зазоры, преднатяг, комплекты
- **[5. Эксплуатация и обслуживание](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)** — Смазка, посадки, монтаж, хранение
- **[6. Отказы и диагностика](<docs/06-otkazy-i-diagnostika/README.md>)** — Дефекты, причины, коррозия, электроэрозия
- **[7. Бренды и производители](<docs/07-brendy-i-proizvoditeli/README.md>)** — SKF, FAG, NSK, NTN, российские ГПЗ, аналоги
- **[8. Специальные исполнения и справка](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)** — Высокоточные, керамические, высокотемпературные
- **[9. Сопутствующие изделия](<docs/09-soputstvuyushchie-izdeliya/README.md>)** — Смазки, крепёж, передачи, уплотнения

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

1.1 [Основные термины и определения](<docs/01-podshipniki-obshaya-informatsiya/1.3. Термины и определения RU EN/README.md>)  
1.2 [Из чего состоит подшипник (элементы, функции, материалы)](<docs/01-podshipniki-obshaya-informatsiya/1.4. Из чего состоит подшипник/README.md>)  
1.3 [Терминология конструкции подшипников](<docs/01-podshipniki-obshaya-informatsiya/README.md>)  
1.4 [Классификация подшипников (по нагрузке, направлению, конструкции)](<docs/01-podshipniki-obshaya-informatsiya/1.5. Классификация подшипников/README.md>)  
1.5 [Конструктивные разновидности подшипников](<docs/03-tipy-i-elementy/README.md>)  
1.6 [Как делают подшипники (этапы производства, контроль качества)](docs/QUICK_START.md)  
1.7 [Взаимозаменяемость подшипников качения и скольжения](<docs/03-tipy-i-elementy/README.md>)  
1.8 [Алгоритм выбора подшипника (нагрузка → скорость → ресурс → среда → стандарт)](<docs/01-podshipniki-obshaya-informatsiya/1.7. Алгоритм выбора и чек-лист ошибок/README.md>)

## 2. Стандарты и маркировка (ядро справочника)

2.1 [ГОСТ. Подшипники. Перечень и область применения стандартов](<docs/02-standarty-i-markirovka/2.1. Карта стандартов ГОСТ, ISO, DIN, ANSI/README.md>)  
2.2 [ISO / DIN / ANSI. Международные стандарты подшипников](<docs/02-standarty-i-markirovka/2.4. ISO DIN ANSI правила и отличия/README.md>)  
2.3 [Условное обозначение подшипников по ЕТУ 100, ЕТУ 500 и ТУ](<docs/02-standarty-i-markirovka/README.md>)  
2.4 [Система условных обозначений подшипников (декомпозиция по символам)](<docs/02-standarty-i-markirovka/2.2. Система обозначений базовая модель/README.md>)  
2.5 [Примеры условных обозначений (разбор по шагам)](<docs/02-standarty-i-markirovka/2.11. Примеры расшифровки обозначений/README.md>)  
2.6 [Маркировка подшипников: заводская, торговая, экспортная](<docs/02-standarty-i-markirovka/README.md>)  
2.7 [Обозначение внутреннего диаметра (правила, исключения, спецсерии)](<docs/02-standarty-i-markirovka/2.3. ГОСТ правила формирования обозначения/README.md>)  
2.8 [Обозначение размерных серий и серий ширины](<docs/02-standarty-i-markirovka/2.2. Система обозначений базовая модель/README.md>)  
2.9 [Обозначение момента трения и скоростных характеристик](<docs/02-standarty-i-markirovka/2.10. Скорость, температура, смазка обозначения/README.md>)  
2.10 [Категории и группы подшипников по назначению](<docs/01-podshipniki-obshaya-informatsiya/1.5. Классификация подшипников/README.md>)  
2.11 [Классы точности ГОСТ / ISO / ABEC (таблица соответствий)](<docs/02-standarty-i-markirovka/2.6. Классы точности ГОСТ, ISO, ABEC/README.md>)  
2.12 [Таблица аналогов ГОСТ → ISO (базовые и расширенные серии)](<docs/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
2.13 [Таблица аналогов ISO → ГОСТ](<docs/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
2.14 [Таблица соответствия дополнительных обозначений ГОСТ ↔ ISO ↔ бренды](<docs/02-standarty-i-markirovka/README.md>)  
2.15 [Импортные аналоги российских подшипников (с ограничениями применяемости)](<docs/07-brendy-i-proizvoditeli/README.md>)  
2.16 [Коды ТН ВЭД ЕАЭС для подшипников (по типам)](<docs/02-standarty-i-markirovka/2.12. ТН ВЭД коды по типам/README.md>)

## 3. Типы, узлы и элементы конструкции

3.1 [Типы подшипников (шариковые, роликовые, игольчатые, сферические)](<docs/03-tipy-i-elementy/README.md>)  
3.2 [Типы и конструктивные модификации](<docs/03-tipy-i-elementy/README.md>)  
3.3 [Сепараторы: материалы, исполнение, ограничения](<docs/02-standarty-i-markirovka/2.9. Клетки и сепараторы обозначения/README.md>)  
3.4 [Тела качения: применяемость и сравнительный анализ](<docs/03-tipy-i-elementy/README.md>)  
3.4.1 [Шарики](<docs/03-tipy-i-elementy/README.md>)  
3.4.2 [Ролики (цилиндрические, конические, сферические, игольчатые)](<docs/03-tipy-i-elementy/README.md>)  
3.5 [Подшипниковые узлы и корпусные подшипники (UCP, UCF, UCFL и аналоги)](<docs/03-tipy-i-elementy/README.md>)  
3.6 [Шпиндельные и высокоточные подшипники](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
3.7 [Гибридные и керамические подшипники](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
3.8 [Подшипники SKF Y-типа: обозначения и размеры](<docs/07-brendy-i-proizvoditeli/README.md>)  
3.9 [Крестовины карданных валов](<docs/09-soputstvuyushchie-izdeliya/README.md>)  
3.10 [Закрепительные и стяжные втулки, гайки, стопорные элементы](<docs/09-soputstvuyushchie-izdeliya/README.md>)  
3.11 [Втулки и подшипники скольжения](<docs/03-tipy-i-elementy/README.md>)

## 4. Расчетные и технические параметры

4.1 [Радиальные и осевые нагрузки](<docs/04-raschet-i-parametry/README.md>)  
4.2 [Углы контакта радиально-упорных подшипников](<docs/04-raschet-i-parametry/README.md>)  
4.3 [Предельные и рабочие частоты вращения](<docs/04-raschet-i-parametry/README.md>)  
4.4 [Радиальные зазоры и группы зазоров](<docs/02-standarty-i-markirovka/2.7. Зазоры и группы маркировка и влияние/README.md>)  
4.5 [Предварительный натяг: цели, методы, риски](<docs/04-raschet-i-parametry/README.md>)  
4.6 [Комплекты подшипников (DF / DB / DT)](<docs/04-raschet-i-parametry/README.md>)

## 5. Эксплуатация и обслуживание

5.1 [Смазки: типы, классы, совместимость](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.2 [Посадки колец подшипников (вал / корпус)](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.3 [Монтаж и демонтаж (ошибки и последствия)](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.4 [Ревизия и диагностика состояния](<docs/06-otkazy-i-diagnostika/README.md>)  
5.5 [Хранение, упаковка, транспортировка](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)  
5.6 [Переконсервация и повторный ввод в эксплуатацию](<docs/05-ekspluatatsiya-i-obsluzhivanie/README.md>)

## 6. Отказы и диагностика

6.1 [Основные причины повреждений](<docs/06-otkazy-i-diagnostika/README.md>)  
6.2 [Терминология дефектов (фото + описание + причина)](<docs/06-otkazy-i-diagnostika/README.md>)  
6.3 [Подшипники в электродвигателях и типовые отказы](<docs/06-otkazy-i-diagnostika/README.md>)

## 7. Каталог производителей и брендов (расширенный)

7.1 [Производители СНГ (ГПЗ, СПЗ, ВПЗ, MPZ и др.)](<docs/07-brendy-i-proizvoditeli/README.md>)  
7.2 [Европейские производители (SKF, FAG/INA, NSK Europe, NKE)](<docs/07-brendy-i-proizvoditeli/README.md>)  
7.3 [Азиатские производители (NSK, NTN, KOYO, Nachi, ZWZ, C&U)](<docs/07-brendy-i-proizvoditeli/README.md>)  
7.4 [Китайские OEM и aftermarket бренды (LYC, HRB, ZKL и др.)](<docs/07-brendy-i-proizvoditeli/README.md>)  
7.5 [Особенности маркировки и обозначений по брендам](<docs/07-brendy-i-proizvoditeli/README.md>)  
7.6 [Сопоставление брендов: премиум / индустриальные / бюджетные](<docs/07-brendy-i-proizvoditeli/README.md>)

## 8. Специальные исполнения и справочная информация

8.1 [Миниатюрные и тонкостенные подшипники](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.2 [Высокотемпературные и криогенные подшипники](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.3 [Виброустойчивые и ударостойкие исполнения](<docs/08-spetsialnye-ispolneniya-i-spravka/README.md>)  
8.4 [Таблица расшифровки кодов даты выпуска](docs/QUICK_REFERENCE.md)  
8.5 [Библиография и нормативная литература](docs/QUICK_REFERENCE.md)  
8.6 [Практические заметки и нетиповые кейсы](<docs/prakticheskie-rukovodstva/README.md>)

## Приложения: таблицы и базы данных

A.1 [Таблица ГОСТ ↔ ISO ↔ Бренд ↔ Тип ↔ Размеры](<data/README.md>)  
A.2 [Таблица аналогов ГОСТ → ISO → SKF / FAG / NSK / NTN](<docs/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
A.3 [Таблица аналогов ISO → ГОСТ → российские заводы](<docs/02-standarty-i-markirovka/2.5. Сопоставление ГОСТ и ISO аналоги/README.md>)  
A.4 [Таблица дополнительных обозначений ГОСТ / ISO / бренд](<docs/02-standarty-i-markirovka/README.md>)  
A.5 [Размерные таблицы (d, D, B, r, масса)](<data/README.md>)  
A.6 [Таблица производителей (страна, специализация, уровень качества)](<docs/07-brendy-i-proizvoditeli/README.md>)

## Указатели

I.1 [Алфавитный указатель терминов](<docs/01-podshipniki-obshaya-informatsiya/1.3. Термины и определения RU EN/README.md>)  
I.2 [Указатель обозначений/серий подшипников](<docs/02-standarty-i-markirovka/README.md>)  
I.3 [Указатель стандартов](<docs/02-standarty-i-markirovka/2.1. Карта стандартов ГОСТ, ISO, DIN, ANSI/README.md>)  
I.4 [Указатель производителей и брендов](<docs/07-brendy-i-proizvoditeli/README.md>)

## О проекте

P.1 [Предисловие](docs/QUICK_START.md)  
P.2 [Как пользоваться справочником (логика разделов, поиск, навигация)](<docs/01-podshipniki-obshaya-informatsiya/1.2. Как пользоваться базой/README.md>)  
P.3 [Список сокращений и условных обозначений](docs/QUICK_REFERENCE.md)  
P.4 [Принципы идентификации статей (ID/slug), готовность к интеграции в БД/AI](<docs/01-podshipniki-obshaya-informatsiya/1.9. Структура данных для БД/README.md>)  
P.5 [Список таблиц и иллюстраций (если применимо)](<docs/images/README.md>)  
P.6 [История изменений (changelog)](docs/QUICK_START.md)  
P.7 [Политика источников, цитирование, лицензии](<docs/01-podshipniki-obshaya-informatsiya/1.8. Источники и верификация/README.md>)  
P.8 [Схемы импорта/экспорта данных (CSV/JSON), правила валидации](<data/schemas/README.md>)

---

## 🧭 Дополнительные материалы

- **[Вводный курс для новичков](<docs/vvodny-kurs-dlya-novichkov/README.md>)** — Обучающие материалы для начинающих
- **[Учебник](<docs/uchebnik/README.md>)** / **[Учебник академический](<docs/uchebnik-akademichesky/README.md>)** — Систематический курс изучения
- **[Практические руководства](<docs/prakticheskie-rukovodstva/README.md>)** — Пошаговые инструкции и кейсы
- **[Инструменты и справочники](<docs/instrumenty-i-spravochniki/README.md>)** — Калькуляторы, конвертеры, утилиты
- **[Карты знаний и навигация](<docs/karty-znany-i-navigatsiya/README.md>)** — Визуальные схемы и навигация по темам
- **[Каталоги](<data/katalogi/README.md>)** — Каталоги производителей и продукции
- **[Изображения](<docs/images/README.md>)** — Фотографии, схемы, чертежи
- **[Тесты](<Тесты/README.md>)** — Проверка знаний

---

## 🔧 Техническая инфраструктура

**Исходный код и данные:**
- **[src/](src/)** — Исходный код приложения
- **[scripts/](<scripts/README.md>)** — Утилиты и скрипты для обработки данных
- **[api/](<api/README.md>)** — API-интерфейс
- **[data/](<data/README.md>)** — Данные, базы данных, источники
- **[docs/](docs/)** — Техническая документация
- **[tests/](tests/)** — Тесты
- **[config/](config/)** — Конфигурационные файлы
- **[schemas/](<schemas/README.md>)** — Схемы баз данных
- **[sql/](sql/)** — SQL-скрипты
- **[tools/](<tools/README.md>)** — Инструменты и утилиты

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
   Ознакомьтесь с **[Вводным курсом для новичков](<Вводный_курс_для_новичков/README.md>)** для понимания основ

3. **Используйте навигацию:**  
   Используйте **[Карты знаний](<Карты_знаний_и_навигация/README.md>)** для поиска нужной информации

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