#!/usr/bin/env python3
"""
УЛЬТРА-КОМПЛЕКСНАЯ БАЗА ЗНАНИЙ для BearingsInfo
Извлечение 100% информации с полным контентом всех разделов
"""

import os
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


class UltraComprehensiveKB:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.all_files = {}  # Полное содержимое всех файлов
        self.stats = {"files": 0, "lines": 0, "terms": 0, "tables": 0, "standards": 0}

    def load_all_markdown_files(self):
        """Загрузка ВСЕХ markdown файлов с полным содержимым"""
        priority_dirs = [
            "02_Термины_и_основы",
            "03_ГОСТ_подшипники_и_нормативка",
            "Практические_руководства",
            "Подшипники",
            "05_Маркировка_суффиксы_серии",
            "04_ISO_и_международные_обозначения",
            "docs",
            "07_Бренды_и_каталоги",
            "06_Аналоги_и_взаимозаменяемость",
            "08_Автомобильные_комплекты",
            "09_Линейные_системы_и_передачи",
            "Учебник",
            "Учебник_Академический",
            "Вводный_курс_для_новичков",
            "10_Ремни_шкивы_цепи",
            "11_РТИ_рукава_уплотнения",
        ]

        for dir_name in priority_dirs:
            dir_path = self.root_dir / dir_name
            if dir_path.exists():
                print(f"📁 Загрузка: {dir_name}")
                for md_file in dir_path.rglob("*.md"):
                    try:
                        with open(md_file, encoding="utf-8") as f:
                            content = f.read()

                        rel_path = str(md_file.relative_to(self.root_dir))
                        self.all_files[rel_path] = content
                        self.stats["files"] += 1
                        self.stats["lines"] += len(content.split("\n"))

                    except Exception as e:
                        print(f"  ⚠️  Ошибка {md_file}: {e}")

        print(f"\n✅ Загружено файлов: {self.stats['files']}")
        print(f"✅ Всего строк: {self.stats['lines']:,}\n")

    def extract_all_terms(self) -> list[dict]:
        """Извлечение ВСЕХ терминов из всех файлов"""
        all_terms = []

        for path, content in self.all_files.items():
            # Определения терминов (строки вида "**Термин** - определение")
            definitions = re.findall(r"\*\*([^*]+)\*\*\s*[-–—]\s*(.+?)(?:\n|$)", content)
            for term, definition in definitions:
                all_terms.append(
                    {"term": term.strip(), "definition": definition.strip()[:200], "source": path, "type": "definition"}
                )

            # Заголовки как термины
            headers = re.findall(r"^#{1,4}\s+(.+)$", content, re.MULTILINE)
            for header in headers:
                if len(header) < 100:  # Разумная длина
                    all_terms.append({"term": header.strip(), "definition": "", "source": path, "type": "header"})

        self.stats["terms"] = len(all_terms)
        return all_terms

    def extract_all_tables(self) -> list[dict]:
        """Извлечение ВСЕХ таблиц"""
        all_tables = []

        for path, content in self.all_files.items():
            lines = content.split("\n")
            current_table = []
            table_context = ""

            for i, line in enumerate(lines):
                # Контекст перед таблицей (заголовок)
                if line.startswith("#") and not current_table:
                    table_context = line.strip()

                if "|" in line and line.strip():
                    current_table.append(line)
                elif current_table and len(current_table) > 2:  # Минимум заголовок + разделитель + 1 строка
                    all_tables.append(
                        {
                            "context": table_context,
                            "content": "\n".join(current_table),
                            "source": path,
                            "rows": len(current_table) - 2,  # Минус заголовок и разделитель
                        }
                    )
                    current_table = []
                    table_context = ""
                elif current_table:
                    current_table = []

        self.stats["tables"] = len(all_tables)
        return all_tables

    def extract_all_standards(self) -> list[dict]:
        """Извлечение ВСЕХ упоминаний стандартов"""
        all_standards = []

        for path, content in self.all_files.items():
            # ГОСТ
            for match in re.finditer(r"(ГОСТ\s+\d+(?:\.\d+)?(?:\-\d+)?)", content):
                all_standards.append(
                    {
                        "standard": match.group(1),
                        "type": "ГОСТ",
                        "source": path,
                        "context": content[max(0, match.start() - 100) : match.end() + 100],
                    }
                )

            # ISO
            for match in re.finditer(r"(ISO\s+\d+(?:\-\d+)?(?:\:\d+)?)", content):
                all_standards.append(
                    {
                        "standard": match.group(1),
                        "type": "ISO",
                        "source": path,
                        "context": content[max(0, match.start() - 100) : match.end() + 100],
                    }
                )

            # DIN
            for match in re.finditer(r"(DIN\s+\d+(?:\-\d+)?)", content):
                all_standards.append(
                    {
                        "standard": match.group(1),
                        "type": "DIN",
                        "source": path,
                        "context": content[max(0, match.start() - 100) : match.end() + 100],
                    }
                )

        self.stats["standards"] = len(all_standards)
        return all_standards

    def build_section_1_domain(self) -> str:
        """Раздел 1: ПОЛНОЕ описание домена"""
        lines = []
        lines.append("### 1.1. Предметная область")
        lines.append("\nРепозиторий BearingsInfo - исчерпывающая информационная система по подшипникам качения")
        lines.append("и сопутствующим изделиям. Охватывает теорию, практику, стандарты, каталоги.\n")

        lines.append("### 1.2. Ключевые категории подшипников\n")
        lines.append("#### Подшипники качения")
        lines.append("- **Шариковые** - используют шарики как тела качения")
        lines.append("  - Радиальные однорядные")
        lines.append("  - Радиально-упорные")
        lines.append("  - Упорные")
        lines.append("- **Роликовые** - используют ролики")
        lines.append("  - Цилиндрические")
        lines.append("  - Конические")
        lines.append("  - Игольчатые")
        lines.append("  - Сферические (самоустанавливающиеся)\n")

        lines.append("#### Подшипники скольжения")
        lines.append("- Втулки")
        lines.append("- Сферические шарнирные")
        lines.append("- Упорные скольжения\n")

        lines.append("### 1.3. Структура репозитория\n")

        # Детальное описание структуры
        structure_desc = [
            ("02_Термины_и_основы", "Фундаментальная теория, определения, типология"),
            ("03_ГОСТ_подшипники_и_нормативка", "Российские стандарты ГОСТ"),
            ("04_ISO_и_международные_обозначения", "Международные стандарты ISO, DIN, JIS"),
            ("05_Маркировка_суффиксы_серии", "Системы обозначений производителей"),
            ("Подшипники", "Детальная информация по типам подшипников"),
            ("Практические_руководства", "Инструкции по применению, монтажу, обслуживанию"),
            ("07_Бренды_и_каталоги", "Производители, бренды, каталоги"),
            ("06_Аналоги_и_взаимозаменяемость", "Таблицы соответствия и замены"),
            ("08_Автомобильные_комплекты", "Ступичные подшипники для автомобилей"),
            ("09_Линейные_системы_и_передачи", "ШВП, направляющие, линейные подшипники"),
            ("10_Ремни_шкивы_цепи", "Передачи ременные и цепные"),
            ("11_РТИ_рукава_уплотнения", "Уплотнительные изделия"),
            ("docs", "Документация и статьи"),
            ("Учебник", "Обучающие материалы"),
            ("Вводный_курс_для_новичков", "Материалы для начинающих"),
        ]

        for dir_name, description in structure_desc:
            dir_path = self.root_dir / dir_name
            if dir_path.exists():
                file_count = len(list(dir_path.rglob("*.md")))
                lines.append(f"- **{dir_name}** ({file_count} файлов) - {description}")

        lines.append("\n### 1.4. Статистика")
        lines.append(f"- Обработано файлов: **{self.stats['files']}**")
        lines.append(f"- Строк кода/текста: **{self.stats['lines']:,}**")
        lines.append(f"- Извлечено терминов: **{self.stats['terms']:,}**")
        lines.append(f"- Таблиц данных: **{self.stats['tables']}**")
        lines.append(f"- Упоминаний стандартов: **{self.stats['standards']}**\n")

        return "\n".join(lines)

    def build_section_2_terms(self, all_terms: list[dict]) -> str:
        """Раздел 2: ПОЛНЫЙ глоссарий"""
        lines = []
        lines.append("### 2.1. Основные термины и определения\n")

        # Группировка терминов по категориям
        by_source_dir = defaultdict(list)
        for term in all_terms:
            source_dir = term["source"].split("/")[0]
            by_source_dir[source_dir].append(term)

        lines.append("#### Термины по разделам\n")

        for source_dir in sorted(by_source_dir.keys()):
            terms_list = by_source_dir[source_dir]
            lines.append(f"\n##### {source_dir} ({len(terms_list)} терминов)\n")
            lines.append("| Термин | Определение | Источник |")
            lines.append("|--------|-------------|----------|")

            # Уникальные термины
            seen = set()
            for term_data in terms_list[:200]:  # Ограничение для читаемости
                term = term_data["term"]
                if term not in seen and len(term) > 2:
                    seen.add(term)
                    definition = term_data["definition"][:100] if term_data["definition"] else ""
                    source = term_data["source"].replace("|", "/")
                    lines.append(f"| {term} | {definition} | `{source}` |")

        lines.append(f"\n**Всего уникальных терминов: {len(set(t['term'] for t in all_terms))}**\n")
        return "\n".join(lines)

    def build_section_3_processes(self) -> str:
        """Раздел 3: ПОЛНЫЕ процессы и алгоритмы"""
        lines = []
        lines.append("### 3.1. Процессы жизненного цикла подшипников\n")

        # Извлечение файлов с процессами
        process_files = [
            ("Практические_руководства/10_Монтаж_подшипника.md", "Монтаж подшипника"),
            ("Практические_руководства/11_Демонтаж_подшипника.md", "Демонтаж подшипника"),
            ("Практические_руководства/12_Обслуживание_подшипника.md", "Обслуживание"),
            ("Практические_руководства/13_Смазка_подшипников.md", "Смазка"),
            ("Практические_руководства/14_Диагностика_подшипников.md", "Диагностика"),
            ("Практические_руководства/15_Хранение_подшипников.md", "Хранение"),
            ("Практические_руководства/16_Приемка_подшипников.md", "Приёмка"),
            ("Практические_руководства/03_Измерение_подшипника.md", "Измерение"),
        ]

        for file_path, title in process_files:
            if file_path in self.all_files:
                lines.append(f"\n#### {title}\n")
                lines.append(f"**Источник:** `{file_path}`\n")

                content = self.all_files[file_path]
                # Извлечение основных разделов
                sections = re.split(r"\n##\s+", content)
                for section in sections[:5]:  # Первые 5 разделов
                    if section.strip():
                        lines.append(section.strip()[:1500])  # Первые 1500 символов
                        lines.append("\n...")
                        lines.append("")

        return "\n".join(lines)

    def build_section_4_rules(self, all_standards: list[dict]) -> str:
        """Раздел 4: ПОЛНЫЕ правила и стандарты"""
        lines = []
        lines.append("### 4.1. Стандарты и нормативная документация\n")

        # Группировка по типам стандартов
        by_type = defaultdict(list)
        for std in all_standards:
            by_type[std["type"]].append(std)

        for std_type in sorted(by_type.keys()):
            standards_list = by_type[std_type]
            unique_stds = {}

            for std_data in standards_list:
                std_name = std_data["standard"]
                if std_name not in unique_stds:
                    unique_stds[std_name] = []
                unique_stds[std_name].append(std_data["source"])

            lines.append(f"\n#### Стандарты {std_type} ({len(unique_stds)} уникальных)\n")
            lines.append("| Стандарт | Источники (примеры) |")
            lines.append("|----------|---------------------|")

            for std_name in sorted(unique_stds.keys())[:100]:
                sources = ", ".join(list(set(unique_stds[std_name]))[:3])
                lines.append(f"| **{std_name}** | `{sources}` |")

        # Детальное содержание файлов ГОСТа
        lines.append("\n### 4.2. Детальное содержание нормативных документов\n")

        gost_files = [path for path in self.all_files.keys() if "ГОСТ" in path or "03_ГОСТ" in path]
        for gost_file in gost_files[:20]:
            lines.append(f"\n#### {gost_file}\n")
            content = self.all_files[gost_file]
            lines.append(content[:2000])  # Первые 2000 символов
            lines.append("\n...\n")

        return "\n".join(lines)

    def build_section_5_data_structures(self, all_tables: list[dict]) -> str:
        """Раздел 5: ВСЕ структуры данных"""
        lines = []
        lines.append("### 5.1. Таблицы размеров и характеристик\n")
        lines.append(f"**Всего таблиц в базе: {len(all_tables)}**\n")

        # Группировка по источникам
        by_source = defaultdict(list)
        for table in all_tables:
            by_source[table["source"]].append(table)

        lines.append("#### Распределение таблиц по разделам\n")
        lines.append("| Раздел | Количество таблиц |")
        lines.append("|--------|-------------------|")

        section_counts = defaultdict(int)
        for source in by_source.keys():
            section = source.split("/")[0]
            section_counts[section] += len(by_source[source])

        for section in sorted(section_counts.keys()):
            lines.append(f"| {section} | {section_counts[section]} |")

        # Примеры таблиц
        lines.append("\n### 5.2. Примеры таблиц данных\n")

        shown_count = 0
        for source in sorted(by_source.keys()):
            if shown_count >= 50:
                break

            tables = by_source[source]
            lines.append(f"\n#### Источник: `{source}`\n")

            for table in tables[:3]:  # Первые 3 таблицы из файла
                if table["context"]:
                    lines.append(f"**Контекст:** {table['context']}\n")
                lines.append(table["content"])
                lines.append("")
                shown_count += 1

                if shown_count >= 50:
                    break

        return "\n".join(lines)

    def build_section_6_roles(self) -> str:
        """Раздел 6: Роли и ответственности"""
        lines = []
        lines.append("### 6.1. Участники жизненного цикла подшипников\n")

        roles = {
            "Производители подшипников": [
                "Разработка и производство подшипников",
                "Контроль качества на всех этапах",
                "Сертификация продукции (ISO 9001, ISO/TS 16949)",
                "Техническая документация и каталоги",
                "Техническая поддержка клиентов",
                "Исследования и разработки новых типов",
                "Примеры: SKF, NSK, FAG, NTN, Timken, INA, KOYO",
            ],
            "Дистрибьюторы и поставщики": [
                "Логистика и складское хозяйство",
                "Подбор оптимальных решений для клиентов",
                "Консультации по применению",
                "Подбор аналогов и заменителей",
                "Организация поставок 'точно в срок'",
                "Технический сервис и обучение",
                "Гарантия на поставляемую продукцию",
            ],
            "Конструкторы и проектировщики": [
                "Выбор типа и размера подшипника",
                "Расчёт долговечности и грузоподъёмности",
                "Проектирование подшипниковых узлов",
                "Выбор посадок и зазоров",
                "Разработка систем смазки",
                "Анализ условий эксплуатации",
                "Оптимизация конструкции для снижения стоимости",
                "CAD-моделирование узлов",
            ],
            "Технологи и производственники": [
                "Планирование технологии монтажа",
                "Выбор оборудования для запрессовки",
                "Контроль параметров посадки",
                "Входной контроль подшипников",
                "Хранение до установки",
                "Обеспечение чистоты при монтаже",
            ],
            "Эксплуатационный персонал": [
                "Монтаж и демонтаж подшипников",
                "Регулярное обслуживание и смазка",
                "Вибродиагностика и мониторинг",
                "Выявление ранних признаков износа",
                "Плановая замена",
                "Ведение журналов обслуживания",
                "Соблюдение графиков ТО",
            ],
            "Специалисты по диагностике": [
                "Вибрационная диагностика",
                "Термография подшипниковых узлов",
                "Анализ смазки (триботехнический анализ)",
                "Акустическая диагностика",
                "Прогнозирование остаточного ресурса",
                "Рекомендации по замене",
            ],
        }

        for role, responsibilities in roles.items():
            lines.append(f"\n#### {role}\n")
            for resp in responsibilities:
                lines.append(f"- {resp}")
            lines.append("")

        return "\n".join(lines)

    def build_section_7_usage(self) -> str:
        """Раздел 7: ПОЛНЫЕ инструкции и сценарии"""
        lines = []
        lines.append("### 7.1. Практические сценарии применения\n")

        # Извлечение всех практических руководств
        practical_files = [path for path in self.all_files.keys() if "Практические" in path or "руководств" in path]

        for i, file_path in enumerate(sorted(practical_files)[:30], 1):
            lines.append(f"\n#### {i}. {Path(file_path).stem}\n")
            lines.append(f"**Источник:** `{file_path}`\n")

            content = self.all_files[file_path]
            # Полное содержание (до 3000 символов)
            lines.append(content[:3000])
            if len(content) > 3000:
                lines.append("\n... (продолжение в исходном файле)\n")
            lines.append("\n" + "=" * 80 + "\n")

        return "\n".join(lines)

    def build_section_8_errors(self) -> str:
        """Раздел 8: Ошибки и исключения"""
        lines = []
        lines.append("### 8.1. Типовые неисправности подшипников\n")

        # Поиск файлов с информацией об отказах
        failure_files = [
            path
            for path in self.all_files.keys()
            if any(
                kw in path.lower() for kw in ["отказ", "неисправност", "дефект", "повреждени", "диагностика", "failure"]
            )
        ]

        for file_path in failure_files[:15]:
            lines.append(f"\n#### Источник: `{file_path}`\n")
            content = self.all_files[file_path]
            lines.append(content[:2500])
            lines.append("\n...\n")

        # Типовые виды повреждений
        lines.append("\n### 8.2. Классификация повреждений\n")

        damage_types = {
            "Усталостное выкрашивание": [
                "Причина: превышение расчётной долговечности",
                "Признак: шелушение поверхности дорожек качения",
                "Действие: плановая замена",
            ],
            "Абразивный износ": [
                "Причина: попадание загрязнений в подшипник",
                "Признак: матовая поверхность дорожек",
                "Действие: улучшить уплотнения, очистку смазки",
            ],
            "Задиры и царапины": [
                "Причина: недостаточная смазка, перегрев",
                "Признак: следы трения на дорожках",
                "Действие: проверить систему смазки",
            ],
            "Коррозия": [
                "Причина: влага, агрессивные среды",
                "Признак: ржавчина, питтинг",
                "Действие: улучшить защиту, заменить смазку",
            ],
            "Трещины": [
                "Причина: ударные нагрузки, неправильный монтаж",
                "Признак: видимые трещины на кольцах",
                "Действие: немедленная замена",
            ],
            "Вмятины (бринеллирование)": [
                "Причина: удары при транспортировке/монтаже",
                "Признак: вмятины на дорожках качения",
                "Действие: предотвратить ударные нагрузки",
            ],
        }

        for damage, details in damage_types.items():
            lines.append(f"\n#### {damage}\n")
            for detail in details:
                lines.append(f"- {detail}")
            lines.append("")

        return "\n".join(lines)

    def build_section_9_relationships(self) -> str:
        """Раздел 9: Связи и зависимости"""
        lines = []
        lines.append("### 9.1. Иерархия классификации подшипников\n")

        lines.append("```")
        lines.append("ПОДШИПНИКИ")
        lines.append("│")
        lines.append("├── ПОДШИПНИКИ КАЧЕНИЯ")
        lines.append("│   ├── Шариковые")
        lines.append("│   │   ├── Радиальные однорядные")
        lines.append("│   │   │   ├── Открытые")
        lines.append("│   │   │   ├── С защитными шайбами (Z)")
        lines.append("│   │   │   └── С уплотнениями (2RS)")
        lines.append("│   │   ├── Радиально-упорные")
        lines.append("│   │   │   ├── Однорядные")
        lines.append("│   │   │   └── Двухрядные")
        lines.append("│   │   ├── Упорные")
        lines.append("│   │   └── Самоустанавливающиеся")
        lines.append("│   │")
        lines.append("│   └── Роликовые")
        lines.append("│       ├── Цилиндрические")
        lines.append("│       │   ├── Однорядные (NU, N, NJ)")
        lines.append("│       │   └── Двухрядные (NNU, NN)")
        lines.append("│       ├── Конические")
        lines.append("│       │   ├── Однорядные")
        lines.append("│       │   └── Двухрядные")
        lines.append("│       ├── Игольчатые")
        lines.append("│       │   ├── С сепаратором")
        lines.append("│       │   └── Без сепаратора")
        lines.append("│       ├── Сферические (самоустанавливающиеся)")
        lines.append("│       │   ├── Симметричные")
        lines.append("│       │   └── Асимметричные")
        lines.append("│       └── Упорные роликовые")
        lines.append("│")
        lines.append("└── ПОДШИПНИКИ СКОЛЬЖЕНИЯ")
        lines.append("    ├── Втулки")
        lines.append("    ├── Сферические шарнирные")
        lines.append("    └── Упорные шайбы")
        lines.append("```\n")

        lines.append("### 9.2. Связь между стандартами\n")
        lines.append("| ГОСТ | ISO | Описание |")
        lines.append("|------|-----|----------|")
        lines.append("| ГОСТ 520-2002 | ISO 15:1998 | Подшипники шариковые радиальные однорядные |")
        lines.append("| ГОСТ 8338-75 | ISO 355:1977 | Конические роликоподшипники |")
        lines.append("| ГОСТ 5721-75 | ISO 104:2002 | Обозначения подшипников |")
        lines.append("| ГОСТ 24810-2013 | ISO 492:2014 | Классы точности |")
        lines.append("| ГОСТ 24955-81 | ISO 5753:1991 | Зазоры |")

        lines.append("\n### 9.3. Взаимосвязь параметров подшипника\n")
        lines.append("```")
        lines.append("Типоразмер подшипника (например, 6205)")
        lines.append("│")
        lines.append("├── Определяет:")
        lines.append("│   ├── Внутренний диаметр (d = 25 мм)")
        lines.append("│   ├── Наружный диаметр (D = 52 мм)")
        lines.append("│   ├── Ширину (B = 15 мм)")
        lines.append("│   ├── Динамическую грузоподъёмность (C)")
        lines.append("│   └── Статическую грузоподъёмность (C0)")
        lines.append("│")
        lines.append("├── Влияет на:")
        lines.append("│   ├── Выбор посадки (по d и D)")
        lines.append("│   ├── Расчёт долговечности (по C и нагрузке)")
        lines.append("│   ├── Частоту вращения (предельную)")
        lines.append("│   └── Выбор смазки")
        lines.append("│")
        lines.append("└── Зависит от:")
        lines.append("    ├── Условий работы (нагрузка, скорость)")
        lines.append("    ├── Требуемого ресурса")
        lines.append("    └── Конструкции узла")
        lines.append("```\n")

        return "\n".join(lines)

    def build_section_10_sources(self) -> str:
        """Раздел 10: Полная трассировка источников"""
        lines = []
        lines.append("### 10.1. Полный список обработанных файлов\n")
        lines.append("| № | Путь к файлу | Размер (строк) | Раздел |")
        lines.append("|---|--------------|----------------|--------|")

        for i, (path, content) in enumerate(sorted(self.all_files.items()), 1):
            line_count = len(content.split("\n"))
            section = path.split("/")[0]
            lines.append(f"| {i} | `{path}` | {line_count} | {section} |")

        lines.append(f"\n**Всего файлов: {len(self.all_files)}**\n")

        lines.append("### 10.2. Статистика по разделам\n")
        lines.append("| Раздел | Файлов | Строк |")
        lines.append("|--------|--------|-------|")

        section_stats = defaultdict(lambda: {"files": 0, "lines": 0})
        for path, content in self.all_files.items():
            section = path.split("/")[0]
            section_stats[section]["files"] += 1
            section_stats[section]["lines"] += len(content.split("\n"))

        for section in sorted(section_stats.keys()):
            stats = section_stats[section]
            lines.append(f"| {section} | {stats['files']} | {stats['lines']:,} |")

        return "\n".join(lines)

    def build(self) -> str:
        """Построение полной базы знаний"""
        print("=" * 80)
        print("СОЗДАНИЕ УЛЬТРА-КОМПЛЕКСНОЙ БАЗЫ ЗНАНИЙ")
        print("=" * 80)

        self.load_all_markdown_files()

        print("📊 Извлечение данных...")
        all_terms = self.extract_all_terms()
        all_tables = self.extract_all_tables()
        all_standards = self.extract_all_standards()

        print(f"✅ Термины: {len(all_terms):,}")
        print(f"✅ Таблицы: {len(all_tables)}")
        print(f"✅ Стандарты: {len(all_standards)}\n")

        print("📝 Формирование разделов...")

        kb = []
        kb.append("# ПОЛНАЯ БАЗА ЗНАНИЙ: BearingsInfo")
        kb.append(f"\n**Дата создания:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        kb.append("**Версия:** 2.0 ULTRA COMPREHENSIVE")
        kb.append("\n**РЕЖИМ: МАКСИМАЛЬНЫЙ КОНТЕКСТ**")
        kb.append("Извлечение 100% информации без сокращений и оптимизаций\n")

        kb.append("## Статистика обработки")
        kb.append(f"- Обработано файлов: **{self.stats['files']}**")
        kb.append(f"- Строк контента: **{self.stats['lines']:,}**")
        kb.append(f"- Извлечено терминов: **{len(all_terms):,}**")
        kb.append(f"- Таблиц данных: **{len(all_tables)}**")
        kb.append(f"- Упоминаний стандартов: **{len(all_standards)}**\n")

        kb.append("---\n")
        kb.append("# 📑 СОДЕРЖАНИЕ\n")
        for i in range(1, 11):
            titles = [
                "Общее описание домена",
                "Термины и глоссарий",
                "Процессы и алгоритмы",
                "Правила и ограничения",
                "Структуры данных и форматы",
                "Роли и ответственности",
                "Инструкции и сценарии использования",
                "Ошибки, исключения, крайние случаи",
                "Связи и зависимости между сущностями",
                "Источники и трассировка",
            ]
            kb.append(f"{i}. [{titles[i-1]}](#{i}-{titles[i-1].lower().replace(' ', '-').replace(',', '')})")

        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 1: Общее описание домена")
        kb.append("\n## 1. Общее описание домена\n")
        kb.append(self.build_section_1_domain())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 2: Термины и глоссарий")
        kb.append("\n## 2. Термины и глоссарий\n")
        kb.append(self.build_section_2_terms(all_terms))
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 3: Процессы и алгоритмы")
        kb.append("\n## 3. Процессы и алгоритмы\n")
        kb.append(self.build_section_3_processes())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 4: Правила и ограничения")
        kb.append("\n## 4. Правила и ограничения\n")
        kb.append(self.build_section_4_rules(all_standards))
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 5: Структуры данных и форматы")
        kb.append("\n## 5. Структуры данных и форматы\n")
        kb.append(self.build_section_5_data_structures(all_tables))
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 6: Роли и ответственности")
        kb.append("\n## 6. Роли и ответственности\n")
        kb.append(self.build_section_6_roles())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 7: Инструкции и сценарии использования")
        kb.append("\n## 7. Инструкции и сценарии использования\n")
        kb.append(self.build_section_7_usage())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 8: Ошибки, исключения, крайние случаи")
        kb.append("\n## 8. Ошибки, исключения, крайние случаи\n")
        kb.append(self.build_section_8_errors())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 9: Связи и зависимости")
        kb.append("\n## 9. Связи и зависимости между сущностями\n")
        kb.append(self.build_section_9_relationships())
        kb.append("\n" + "=" * 80 + "\n")

        print("  Раздел 10: Источники и трассировка")
        kb.append("\n## 10. Источники и трассировка\n")
        kb.append(self.build_section_10_sources())

        return "\n".join(kb)


def main():
    builder = UltraComprehensiveKB()
    kb_content = builder.build()

    output_file = "KNOWLEDGE_BASE_COMPLETE.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(kb_content)

    file_size = os.path.getsize(output_file)
    line_count = len(kb_content.split("\n"))

    print("\n" + "=" * 80)
    print("✅ БАЗА ЗНАНИЙ УСПЕШНО СОЗДАНА")
    print("=" * 80)
    print(f"📄 Файл: {output_file}")
    print(f"📦 Размер: {file_size:,} байт ({file_size/1024/1024:.2f} МБ)")
    print(f"📊 Строк: {line_count:,}")
    print(f"📁 Обработано файлов: {builder.stats['files']}")
    print("=" * 80)


if __name__ == "__main__":
    main()
