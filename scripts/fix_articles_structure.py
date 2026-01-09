#!/usr/bin/env python3
"""Automatically fix articles structure validation errors."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_articles_structure import EXPECTED, TEMPLATE_MARKERS, read_first_h1  # noqa: E402


def fix_h1_mismatch(file_path: Path, expected_h1: str) -> bool:
    """Fix H1 title mismatch."""
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    if not lines:
        return False

    # Find first H1
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines[i] = f"# {expected_h1}\n"
            file_path.write_text("".join(lines), encoding="utf-8")
            return True

    return False


def add_missing_template_sections(file_path: Path) -> bool:
    """Add missing template sections to an article."""
    content = file_path.read_text(encoding="utf-8")

    # Check which markers are missing
    missing = [marker for marker in TEMPLATE_MARKERS if marker not in content]

    if not missing:
        return False

    # Find where to insert (after first H1)
    lines = content.splitlines(keepends=True)
    insert_pos = 0

    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_pos = i + 1
            # Skip any blank lines after H1
            while insert_pos < len(lines) and lines[insert_pos].strip() == "":
                insert_pos += 1
            break

    # Build sections to add
    sections_to_add = []
    for marker in TEMPLATE_MARKERS:
        if marker not in content:
            sections_to_add.append(marker)
            sections_to_add.append("")

            if marker == "## Цель":
                sections_to_add.append("(Описание цели и назначения статьи)")
            elif marker == "## Ключевые термины":
                sections_to_add.append("- **Термин** — определение")
            elif marker == "## Суть":
                sections_to_add.append("(Основное содержание статьи)")
            elif marker == "## Примеры":
                sections_to_add.append("(Примеры использования)")
            elif marker == "## Связанные данные":
                sections_to_add.append("- (Ссылки на связанные статьи)")
            elif marker == "## Источники":
                sections_to_add.append("- (Источники информации)")

            sections_to_add.append("")

    # Insert after H1
    if sections_to_add:
        lines.insert(insert_pos, "\n".join(sections_to_add) + "\n")
        file_path.write_text("".join(lines), encoding="utf-8")
        return True

    return False


def main() -> int:
    """Fix all validation errors."""
    fixed_count = 0
    error_count = 0

    for rel, expected_h1 in EXPECTED:
        file_path = REPO_ROOT / rel

        if not file_path.exists():
            print(f"⚠️  Missing file: {rel}")
            error_count += 1
            continue

        # Check H1
        actual_h1 = read_first_h1(file_path)
        if actual_h1 != expected_h1:
            print(f"🔧 Fixing H1 in {rel}")
            if fix_h1_mismatch(file_path, expected_h1):
                fixed_count += 1
            else:
                print(f"❌ Failed to fix H1 in {rel}")
                error_count += 1
                continue

        # Check template markers
        content = file_path.read_text(encoding="utf-8")
        missing_markers = [m for m in TEMPLATE_MARKERS if m not in content]

        if missing_markers:
            print(f"🔧 Adding missing template sections to {rel}")
            if add_missing_template_sections(file_path):
                fixed_count += 1
            else:
                print(f"❌ Failed to add templates to {rel}")
                error_count += 1

    print(f"\n✓ Fixed {fixed_count} articles")
    if error_count > 0:
        print(f"❌ {error_count} errors remain")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
