#!/usr/bin/env python3
"""Validate source data for the Everest knowledge base."""

from __future__ import annotations

from collections import Counter

from kb_common import (
    ANALOG_WARNING,
    BRAND_WARNING,
    FORBIDDEN_BRAND_PHRASES,
    OPERATION_WARNING,
    REPORTS_DIR,
    VALID_STATUSES,
    load_articles,
    load_sections,
)

REQUIRED_BODY_FIELDS = {
    "purpose",
    "description",
    "key_concepts",
    "verification_rules",
    "common_errors",
    "application_example",
}
EXPECTED_COUNTS = {"1": 17, "2": 14, "3": 15, "4": 22, "5": 20, "6": 20, "7": 20, "8": 20}


def add(errors: list[str], message: str) -> None:
    errors.append(f"ERROR: {message}")


def add_warning(warnings: list[str], message: str) -> None:
    warnings.append(f"WARNING: {message}")


def validate() -> tuple[list[str], list[str]]:
    sections = load_sections()
    articles = load_articles()
    errors: list[str] = []
    warnings: list[str] = []

    if len(sections) != 8:
        add(errors, f"Expected 8 sections, found {len(sections)}")

    section_numbers = [section["number"] for section in sections]
    if section_numbers != [str(number) for number in range(1, 9)]:
        add(errors, f"Section numbering mismatch: {section_numbers}")

    article_numbers = [article["number"] for article in articles]
    for number, count in Counter(article_numbers).items():
        if count > 1:
            add(errors, f"Duplicate article number: {number}")

    titles_by_section = Counter((article["section_number"], article["title"].casefold()) for article in articles)
    for (section_number, title), count in titles_by_section.items():
        if count > 1:
            add(errors, f"Duplicate article title in section {section_number}: {title}")

    articles_by_number = {article["number"]: article for article in articles}
    for section in sections:
        expected_count = EXPECTED_COUNTS.get(section["number"])
        if len(section["articles"]) != expected_count:
            add(
                errors,
                f"Section {section['number']} expected {expected_count} articles, "
                f"found {len(section['articles'])}",
            )
        expected_numbers = [f"{section['number']}.{idx}" for idx in range(1, len(section["articles"]) + 1)]
        if section["articles"] != expected_numbers:
            add(errors, f"Section {section['number']} article numbering mismatch")
        for article_number in section["articles"]:
            if article_number not in articles_by_number:
                add(errors, f"Section {section['number']} references missing article {article_number}")

    for article in articles:
        prefix = f"Article {article.get('number', '<unknown>')}"
        for field in (
            "number",
            "title",
            "section_number",
            "section_title",
            "order",
            "body",
            "related_articles",
            "warnings",
            "data_statuses",
        ):
            if field not in article:
                add(errors, f"{prefix} missing required field: {field}")
        body = article.get("body", {})
        for field in REQUIRED_BODY_FIELDS:
            if not body.get(field):
                add(errors, f"{prefix} missing body field: {field}")
        if len(body.get("key_concepts", [])) < 3:
            add(errors, f"{prefix} must contain at least 3 key concepts")
        if len(body.get("verification_rules", [])) < 3:
            add(errors, f"{prefix} must contain at least 3 verification rules")
        if len(body.get("common_errors", [])) < 3:
            add(errors, f"{prefix} must contain at least 3 common errors")
        statuses = set(article.get("data_statuses", []))
        if not statuses:
            add(errors, f"{prefix} has no data statuses")
        if not statuses.issubset(VALID_STATUSES):
            add(errors, f"{prefix} has invalid data statuses: {sorted(statuses - VALID_STATUSES)}")
        if not statuses.intersection(VALID_STATUSES):
            add(errors, f"{prefix} has no allowed uncertainty status")
        title_and_section = f"{article.get('title', '')} {article.get('section_title', '')}".lower()
        if "аналог" in title_and_section and ANALOG_WARNING not in article.get("warnings", []):
            add(errors, f"{prefix} analog warning is missing")
        if (
            article.get("section_title") == "Эксплуатация, монтаж и диагностика"
            and OPERATION_WARNING not in article.get("warnings", [])
        ):
            add(errors, f"{prefix} operation warning is missing")
        if article.get("section_title") == "Бренды и производители":
            if BRAND_WARNING not in article.get("warnings", []):
                add(errors, f"{prefix} brand restrictions warning is missing")
            searchable = " ".join(
                [
                    article.get("title", ""),
                    body.get("description", ""),
                    body.get("purpose", ""),
                    body.get("application_example", ""),
                ]
            ).casefold()
            for phrase in FORBIDDEN_BRAND_PHRASES:
                if phrase in searchable:
                    add(errors, f"{prefix} contains forbidden brand phrase: {phrase}")
        if "table" in body:
            table = body["table"]
            if table.get("columns") != ["Параметр", "Значение", "Источник", "Статус"]:
                add(errors, f"{prefix} table columns mismatch")
            if not table.get("rows"):
                add(errors, f"{prefix} table has no rows")
        if "латинский маркер незавершенности" in str(article).lower() or "технический маркер" in str(article).lower():
            add(errors, f"{prefix} contains a technical marker")

    source_article_numbers = set(article_numbers)
    for article in articles:
        related_articles = article.get("related_articles", [])
        if len(related_articles) != 3:
            add(errors, f"Article {article['number']} must contain exactly 3 related articles")
        if len(related_articles) != len(set(related_articles)):
            add(errors, f"Article {article['number']} contains duplicate related articles")
        for related in related_articles:
            if related not in source_article_numbers:
                add_warning(warnings, f"Article {article['number']} references missing related article {related}")

    return errors, warnings


def write_report(errors: list[str], warnings: list[str]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    sections = load_sections()
    articles = load_articles()
    lines = [
        "# Validation report — Технический справочник «Эверест»",
        "",
        f"- Разделов: {len(sections)}",
        f"- Статей: {len(articles)}",
        f"- Критических ошибок: {len(errors)}",
        f"- Предупреждений: {len(warnings)}",
        "",
        "## Результат",
        "Проверка пройдена." if not errors else "Проверка завершилась с критическими ошибками.",
        "",
        "## Ошибки",
    ]
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- нет")
    lines.append("")
    lines.append("## Предупреждения")
    lines.extend(f"- {warning}" for warning in warnings) if warnings else lines.append("- нет")
    lines.append("")
    (REPORTS_DIR / "validation-report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    errors, warnings = validate()
    write_report(errors, warnings)
    for message in errors + warnings:
        print(message)
    if errors:
        print("Validation failed. See reports/validation-report.md")
        return 1
    print("Validation passed. See reports/validation-report.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
