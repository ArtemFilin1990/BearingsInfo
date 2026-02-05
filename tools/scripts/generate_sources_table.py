#!/usr/bin/env python3
"""
Generate sources table for SOURCES.md.

This script reads all meta.yaml files from sources/ subdirectories
and generates a markdown table with source information.

Requirements:
    - PyYAML (install with: pip install pyyaml)

Usage:
    python tools/scripts/generate_sources_table.py [--output SOURCES.md]

Examples:
    python tools/scripts/generate_sources_table.py
    python tools/scripts/generate_sources_table.py --output sources_report.md
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("❌ Error: PyYAML is not installed")
    print("Install it with: pip install pyyaml")
    sys.exit(1)


def load_sources_metadata(sources_dir):
    """Load all source metadata from meta.yaml files."""
    sources_data = {}
    categories = ["gost", "iso", "analogs", "brands", "skf"]

    for category in categories:
        meta_file = sources_dir / category / "meta.yaml"
        if meta_file.exists():
            try:
                with open(meta_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if data and "sources" in data:
                        sources_data[category] = data["sources"]
            except Exception as e:
                print(f"⚠️  Warning: Could not read {meta_file}: {e}")
                sources_data[category] = []
        else:
            sources_data[category] = []

    return sources_data


def count_files_in_category(sources_dir, category):
    """Count actual files in a category directory."""
    category_dir = sources_dir / category
    if not category_dir.exists():
        return 0

    # Count PDF, DOCX, and other document files
    extensions = [".pdf", ".docx", ".doc", ".xlsx", ".xls"]
    count = 0
    for ext in extensions:
        count += len(list(category_dir.glob(f"*{ext}")))
    return count


def generate_sources_table(sources_data, sources_dir):
    """Generate markdown table from sources data."""
    lines = []

    # Header
    lines.append("| Категория | Файлов | Проверено | Не проверено | Назначение |")
    lines.append("|-----------|--------|-----------|--------------|------------|")

    # Category rows
    category_names = {"gost": "ГОСТ", "iso": "ISO", "analogs": "Аналоги", "brands": "Бренды", "skf": "SKF"}

    for category, name in category_names.items():
        sources = sources_data.get(category, [])
        total = count_files_in_category(sources_dir, category)
        verified = sum(1 for s in sources if s.get("status") == "verified")
        unverified = len(sources) - verified

        # Get common purpose or first purpose
        purposes = [s.get("purpose", "N/A") for s in sources if s.get("purpose")]
        purpose = purposes[0] if purposes else "N/A"
        if len(set(purposes)) > 1:
            purpose = "Различные"

        lines.append(f"| {name} | {total} | {verified} | {unverified} | {purpose} |")

    return "\n".join(lines)


def generate_detailed_table(sources_data):
    """Generate detailed markdown table with individual files."""
    lines = []

    lines.append("\n## Подробный список источников\n")

    category_names = {"gost": "ГОСТ", "iso": "ISO", "analogs": "Аналоги", "brands": "Бренды", "skf": "SKF"}

    for category, name in category_names.items():
        sources = sources_data.get(category, [])
        if not sources:
            continue

        lines.append(f"\n### {name}\n")
        lines.append("| Файл | Статус | Назначение | Год | Страниц |")
        lines.append("|------|--------|-----------|-----|---------|")

        for source in sources:
            file = source.get("file", "unknown")
            status = "✅" if source.get("status") == "verified" else "⏳"
            purpose = source.get("purpose", "N/A")
            year = source.get("year", "N/A")
            pages = source.get("pages", "N/A")

            lines.append(f"| {file} | {status} | {purpose} | {year} | {pages} |")

    return "\n".join(lines)


def update_sources_md(table, detailed_table, output_file):
    """Update SOURCES.md with the generated tables."""
    # Read current SOURCES.md if it exists
    if output_file.exists():
        with open(output_file, encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    # Build new content
    header = f"""# SOURCES — размещение исходников

> **Последнее обновление:** {datetime.now().strftime('%d %B %Y г.')}

## Категории
- `sources/gost/` — ГОСТ стандарты и учебные материалы (meta: `sources/gost/meta.yaml`)
- `sources/iso/` — материалы по системе ISO и суффиксам (meta: `sources/iso/meta.yaml`)
- `sources/analogs/` — документ с таблицей аналогов ГОСТ ↔ ISO (meta: `sources/analogs/meta.yaml`)
- `sources/brands/` — каталоги производителей (NSK/NTN/FAG/INA/Schaeffler и др.) (meta: `sources/brands/meta.yaml`)
- `sources/skf/` — каталоги SKF (meta: `sources/skf/meta.yaml`)

## Сводная таблица источников

{table}

> **Примечание:** Для получения актуального списка используйте:
> ```bash
> python tools/scripts/generate_sources_table.py
> ```

{detailed_table}
"""

    # Find where to keep the rest of the content (How to use section onwards)
    import re

    match = re.search(r"(## Проверка статусов.*)", content, re.DOTALL)
    if match:
        footer = match.group(1)
    else:
        footer = """
## Проверка статусов
- Каждый `meta.yaml` содержит статус `unverified`/`verified`. При добавлении нового источника
  обновляйте статус и цель (`purpose`).
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
3. Запустите `python tools/scripts/update_repo.py` для пересборки CSV.
4. Зафиксируйте изменения вместе с новым отчётом в `data/reports/`.

## Автоматизация

### Генерация списка источников
Автоматически обновить этот файл на основе meta.yaml:
```bash
python tools/scripts/generate_sources_table.py
```

### Извлечение данных из PDF
```bash
python sources/pdf_text_extractor.py sources/gost/ГОСТ_520-2002.pdf
```

### Парсинг онлайн-каталогов
```bash
python sources/table_scraper.py
```
"""

    new_content = header + "\n" + footer

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate sources table for SOURCES.md")
    parser.add_argument("--output", default="SOURCES.md", help="Output file (default: SOURCES.md)")
    parser.add_argument("--detailed", action="store_true", help="Include detailed table with all files")

    args = parser.parse_args()

    # Locate directories
    repo_root = Path(__file__).parent.parent
    sources_dir = repo_root / "sources"
    output_file = repo_root / args.output

    if not sources_dir.exists():
        print(f"❌ Error: sources/ directory not found at {sources_dir}")
        return 1

    # Load metadata
    print("📖 Loading source metadata...")
    sources_data = load_sources_metadata(sources_dir)

    # Generate table
    print("📊 Generating sources table...")
    table = generate_sources_table(sources_data, sources_dir)

    detailed_table = ""
    if args.detailed:
        print("📋 Generating detailed table...")
        detailed_table = generate_detailed_table(sources_data)

    # Update file
    print(f"✍️  Updating {output_file}...")
    update_sources_md(table, detailed_table, output_file)

    print(f"\n✅ Successfully updated {output_file}")
    print("\nGenerated table:")
    print(table)

    if detailed_table:
        print(detailed_table)

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
