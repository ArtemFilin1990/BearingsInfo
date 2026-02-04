#!/usr/bin/env python3
"""Верификация полноты базы знаний"""

import re


def verify_knowledge_base(filename="KNOWLEDGE_BASE_COMPLETE.md"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    print("=" * 80)
    print("ВЕРИФИКАЦИЯ ПОЛНОТЫ БАЗЫ ЗНАНИЙ")
    print("=" * 80)

    # Проверка обязательных разделов
    required_sections = [
        (r"## 1\. Общее описание домена", "Раздел 1: Общее описание"),
        (r"## 2\. Термины и глоссарий", "Раздел 2: Термины"),
        (r"## 3\. Процессы и алгоритмы", "Раздел 3: Процессы"),
        (r"## 4\. Правила и ограничения", "Раздел 4: Правила"),
        (r"## 5\. Структуры данных и форматы", "Раздел 5: Структуры данных"),
        (r"## 6\. Роли и ответственности", "Раздел 6: Роли"),
        (r"## 7\. Инструкции и сценарии использования", "Раздел 7: Инструкции"),
        (r"## 8\. Ошибки, исключения, крайние случаи", "Раздел 8: Ошибки"),
        (r"## 9\. Связи и зависимости между сущностями", "Раздел 9: Связи"),
        (r"## 10\. Источники и трассировка", "Раздел 10: Источники"),
    ]

    print("\n✅ ПРОВЕРКА ОБЯЗАТЕЛЬНЫХ РАЗДЕЛОВ:\n")
    all_present = True
    for pattern, name in required_sections:
        if re.search(pattern, content):
            print(f"  ✓ {name}")
        else:
            print(f"  ✗ {name} - ОТСУТСТВУЕТ!")
            all_present = False

    # Статистика контента
    print("\n📊 СТАТИСТИКА КОНТЕНТА:\n")

    total_lines = len(content.split("\n"))
    print(f"  Всего строк: {total_lines:,}")

    # Подсчёт таблиц
    tables = len(re.findall(r"\|.*\|.*\|", content))
    print(f"  Строк с таблицами: {tables:,}")

    # Подсчёт заголовков
    h1 = len(re.findall(r"^# ", content, re.MULTILINE))
    h2 = len(re.findall(r"^## ", content, re.MULTILINE))
    h3 = len(re.findall(r"^### ", content, re.MULTILINE))
    h4 = len(re.findall(r"^#### ", content, re.MULTILINE))
    print(f"  Заголовков H1: {h1}")
    print(f"  Заголовков H2: {h2}")
    print(f"  Заголовков H3: {h3}")
    print(f"  Заголовков H4: {h4}")

    # Подсчёт ссылок на источники
    sources = len(re.findall(r"`[^`]+\.md`", content))
    print(f"  Ссылок на источники (.md): {sources:,}")

    # Подсчёт упоминаний стандартов
    gost = len(re.findall(r"ГОСТ\s+\d+", content))
    iso = len(re.findall(r"ISO\s+\d+", content))
    din = len(re.findall(r"DIN\s+\d+", content))
    print(f"  Упоминаний ГОСТ: {gost:,}")
    print(f"  Упоминаний ISO: {iso:,}")
    print(f"  Упоминаний DIN: {din:,}")

    # Оценка объёма разделов
    print("\n📏 ОБЪЁМ РАЗДЕЛОВ (строк):\n")

    sections = []
    for i in range(1, 11):
        if i < 10:
            pattern = f"^## {i}\\..*?(?=^## {i+1}\\.)"
        else:
            pattern = f"^## {i}\\..*"

        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if match:
            section_lines = len(match.group().split("\n"))
            sections.append((i, section_lines))
            status = "✓ ДОСТАТОЧНО" if section_lines > 50 else "⚠ МАЛО"
            print(f"  Раздел {i}: {section_lines:,} строк - {status}")

    # Проверка качества
    print("\n🎯 ОЦЕНКА КАЧЕСТВА:\n")

    quality_checks = [
        (total_lines > 20000, "Общий объём > 20,000 строк"),
        (tables > 100, "Таблиц > 100"),
        (sources > 500, "Ссылок на источники > 500"),
        (gost > 50, "Упоминаний ГОСТ > 50"),
        (all_present, "Все 10 разделов присутствуют"),
        (all(lines > 50 for _, lines in sections), "Все разделы содержательные (>50 строк)"),
    ]

    passed = sum(1 for check, _ in quality_checks if check)
    total_checks = len(quality_checks)

    for check, description in quality_checks:
        status = "✓" if check else "✗"
        print(f"  {status} {description}")

    print(f"\n📈 ИТОГОВАЯ ОЦЕНКА: {passed}/{total_checks} проверок пройдено")

    if passed == total_checks:
        print("\n🎉 БАЗА ЗНАНИЙ ПОЛНОСТЬЮ СООТВЕТСТВУЕТ ТРЕБОВАНИЯМ!")
    elif passed >= total_checks * 0.8:
        print("\n👍 База знаний в основном соответствует требованиям")
    else:
        print("\n⚠️  База знаний требует доработки")

    print("=" * 80)


if __name__ == "__main__":
    verify_knowledge_base()
