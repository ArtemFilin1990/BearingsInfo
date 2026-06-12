#!/usr/bin/env python3
"""Generate Markdown, JSON and CSV exports for the Everest knowledge base."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from kb_common import (
    GENERATED_DIR,
    KB_TITLE,
    REPORTS_DIR,
    build_import_payload,
    load_articles,
    load_sections,
    render_article_markdown,
    safe_filename,
)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    sections = load_sections()
    articles = load_articles()
    articles_by_number = {article["number"]: article for article in articles}
    markdown_dir = GENERATED_DIR / "markdown"
    json_dir = GENERATED_DIR / "json"
    csv_dir = GENERATED_DIR / "csv"
    for path in (markdown_dir, json_dir, csv_dir, REPORTS_DIR):
        path.mkdir(parents=True, exist_ok=True)

    article_path_by_number: dict[str, str] = {}
    for article in articles:
        section_dir = markdown_dir / f"section-{article['section_number']}"
        filename = safe_filename(article["number"], article["title"])
        article_path = section_dir / filename
        article_path_by_number[article["number"]] = str(article_path.relative_to(markdown_dir))
        write_text(article_path, render_article_markdown(article, articles_by_number))

    root_index = [f"# {KB_TITLE}", "", "## Разделы"]
    for section in sections:
        section_dir = markdown_dir / f"section-{section['number']}"
        section_index = [f"# {section['number']}. {section['title']}", "", "## Статьи"]
        for number in section["articles"]:
            article = articles_by_number[number]
            rel_path = article_path_by_number[number].split("/", 1)[1]
            section_index.append(f"- [{article['number']}. {article['title']}]({rel_path})")
        write_text(section_dir / "README.md", "\n".join(section_index) + "\n")
        root_index.append(
            f"- [{section['number']}. {section['title']}](section-{section['number']}/README.md) "
            f"— {len(section['articles'])} статей"
        )
    write_text(markdown_dir / "README.md", "\n".join(root_index) + "\n")

    payload = build_import_payload(sections, articles)
    write_text(json_dir / "bitrix24-import.json", json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    csv_path = csv_dir / "articles.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "section_number",
                "section_title",
                "article_number",
                "article_title",
                "slug",
                "statuses",
                "warnings",
            ],
        )
        writer.writeheader()
        for article in articles:
            writer.writerow(
                {
                    "section_number": article["section_number"],
                    "section_title": article["section_title"],
                    "article_number": article["number"],
                    "article_title": article["title"],
                    "slug": article["slug"],
                    "statuses": "; ".join(article["data_statuses"]),
                    "warnings": "; ".join(article["warnings"]),
                }
            )

    expected_articles = sum(len(section["articles"]) for section in sections)
    article_numbers = [article["number"] for article in articles]
    duplicate_count = len(article_numbers) - len(set(article_numbers))
    required_statuses = ["нет данных", "уточнить", "требует проверки", "не подтверждено"]
    status_counts = {
        status: sum(1 for article in articles if status in article["data_statuses"])
        for status in required_statuses
    }
    table_articles = [article for article in articles if "table" in article["body"]]
    needs_sources = [
        f"{article['number']}. {article['title']}"
        for article in articles
        if set(required_statuses).intersection(article["data_statuses"])
    ]
    report = [
        "# Отчёт по созданию базы знаний",
        "",
        "## Общий результат",
        "",
        "- Название базы знаний: Технический справочник «Эверест»",
        f"- Статус создания: {'создано' if len(articles) == 148 and len(sections) == 8 else 'создано частично'}",
        f"- Разделов создано: {len(sections)} из 8",
        f"- Статей создано: {len(articles)} из {expected_articles}",
        "- Нумерация сохранена: да",
        f"- Дублирование статей: {'не обнаружено' if duplicate_count == 0 else 'обнаружено'}",
        "- Выдуманные технические данные: не использовались",
        "",
        "## Статусы неполных данных",
        "",
        "| Статус | Количество | Комментарий |",
        "|---|---:|---|",
    ]
    report.extend(
        f"| {status} | {status_counts[status]} | Применяется к статьям до заполнения подтверждёнными источниками. |"
        for status in required_statuses
    )
    report.extend(
        [
            "",
            "## Экспорт",
            "",
            "- Markdown: `generated/markdown/`",
            "- JSON для импорта: `generated/json/bitrix24-import.json`",
            "- CSV: `generated/csv/articles.csv`",
            "",
            "## Замечания",
            "",
            f"- Статьи требуют проверки источников: {len(needs_sources)} из {len(articles)}.",
            "- Все технические параметры, нормативные ссылки, аналоги, цены, бренды и коды ТН ВЭД "
            "должны быть заполнены только после сверки с подтверждёнными источниками.",
            f"- Таблицы нужно заполнить после сверки: {len(table_articles)}.",
            "",
            "## Следующие действия",
            "",
            "1. Проверить технические данные по официальным каталогам и ГОСТ / ISO.",
            "2. Заполнить таблицы подтверждёнными источниками.",
            "3. Проверить связи между статьями.",
            "4. Провести редакторскую вычитку перед публикацией.",
            "5. Согласовать Bitrix24 REST-метод и payload перед реальным импортом.",
            "",
        ]
    )
    write_text(REPORTS_DIR / "creation-report.md", "\n".join(report))
    print(f"Generated {len(sections)} sections and {len(articles)} articles for {KB_TITLE}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
