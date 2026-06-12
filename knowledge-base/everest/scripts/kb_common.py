"""Shared helpers for the Everest Bitrix24 knowledge-base toolchain."""

from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

KB_TITLE = "Технический справочник «Эверест»"
ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "source"
GENERATED_DIR = ROOT / "generated"
REPORTS_DIR = ROOT / "reports"
VALID_STATUSES = {"нет данных", "уточнить", "требует проверки", "не подтверждено"}
ANALOG_WARNING = "Аналог требует проверки по размерам, нагрузке, зазору, исполнению, бренду и условиям эксплуатации."
OPERATION_WARNING = "Рекомендации требуют сверки с документацией производителя и условиями работы узла."
BRAND_WARNING = (
    "Запрещены неподтверждённые оценки качества бренда; допускаются только проверяемые сведения "
    "о сегменте, происхождении, специализации, оригинальности и признаках контрафакта."
)
FORBIDDEN_BRAND_PHRASES = {
    "лучший бренд",
    "самый надёжный",
    "самый надежный",
    "плохой производитель",
    "низкое качество",
}


def mask_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return "<invalid-url>"
    return f"{parsed.scheme}://{parsed.netloc}/***"


def require_https_webhook(env_var: str = "BITRIX24_WEBHOOK_URL") -> str:
    webhook_url = os.environ.get(env_var, "").strip()
    if not webhook_url:
        raise RuntimeError(f"Real request is blocked. Required environment: {env_var}")
    parsed = urlparse(webhook_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise RuntimeError(f"{env_var} must be a valid HTTPS webhook base URL")
    return webhook_url.rstrip("/")


def post_json(url: str, payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - explicit operator-provided webhook URL.
        return json.loads(response.read().decode("utf-8"))


def call_bitrix(webhook_url: str, method: str, params: dict[str, Any], timeout: float) -> dict[str, Any]:
    endpoint = f"{webhook_url}/{method}.json"
    response = post_json(endpoint, params, timeout)
    if "error" in response:
        error_description = response.get("error_description", response["error"])
        raise RuntimeError(f"{method}: {error_description}")
    return response


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_sections() -> list[dict[str, Any]]:
    return read_json(SOURCE_DIR / "sections.json")["sections"]


def load_articles() -> list[dict[str, Any]]:
    return read_json(SOURCE_DIR / "articles.json")["articles"]


def article_map() -> dict[str, dict[str, Any]]:
    return {article["number"]: article for article in load_articles()}


def slugify_number(number: str) -> str:
    return number.replace(".", "-")


def safe_filename(number: str, title: str) -> str:
    slug_title = re.sub(r"[^0-9A-Za-zА-Яа-яЁё]+", "-", title, flags=re.UNICODE).strip("-").lower()
    return f"{slugify_number(number)}-{slug_title}.md"


def markdown_table(table: dict[str, Any]) -> str:
    columns = table["columns"]
    lines = ["| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for row in table["rows"]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def render_article_markdown(article: dict[str, Any], articles_by_number: dict[str, dict[str, Any]]) -> str:
    body = article["body"]
    lines = [f"# {article['number']}. {article['title']}", ""]
    lines.extend([
        f"**Раздел:** {article['section_number']}. {article['section_title']}",
        f"**Статусы данных:** {', '.join(article['data_statuses'])}",
        "",
        "## Назначение статьи",
        body["purpose"],
        "",
        "## Краткое описание темы",
        body["description"],
        "",
        "## Ключевые понятия",
    ])
    lines.extend(f"- {concept}" for concept in body["key_concepts"])
    lines.extend(["", "## Правила проверки"])
    lines.extend(f"{idx}. {rule}" for idx, rule in enumerate(body["verification_rules"], start=1))
    lines.extend(["", "## Типовые ошибки"])
    lines.extend(f"- {error}" for error in body["common_errors"])
    if article["warnings"]:
        lines.extend(["", "## Предупреждения"])
        lines.extend(f"- {warning}" for warning in article["warnings"])
    if "table" in body:
        lines.extend(["", "## Таблица", markdown_table(body["table"])])
    lines.extend(["", "## Пример применения", body["application_example"], "", "## Связанные статьи"])
    for related_number in article["related_articles"]:
        related = articles_by_number[related_number]
        lines.append(f"- {related['number']}. {related['title']}")
    lines.extend(["", "## Статус данных"])
    lines.extend(f"- {status}" for status in article["data_statuses"])
    lines.append("")
    return "\n".join(lines)


def build_import_payload(sections: list[dict[str, Any]], articles: list[dict[str, Any]]) -> dict[str, Any]:
    by_section = {section["number"]: {**section, "articles": []} for section in sections}
    articles_by_number = {article["number"]: article for article in articles}
    for article in articles:
        markdown = render_article_markdown(article, articles_by_number)
        by_section[article["section_number"]]["articles"].append(
            {
                "number": article["number"],
                "title": article["title"],
                "order": article["order"],
                "slug": article["slug"],
                "markdown": markdown,
                "warnings": article["warnings"],
                "data_statuses": article["data_statuses"],
                "related_articles": article["related_articles"],
                "bitrix24_mapping": {
                    "section_title": article["section_title"],
                    "article_title": f"{article['number']}. {article['title']}",
                    "content_format": "markdown",
                    "import_mode": "create_or_update_candidate",
                },
            }
        )
    return {
        "knowledge_base": KB_TITLE,
        "target": "Bitrix24 Knowledge Base",
        "default_mode": "dry-run",
        "sections": list(by_section.values()),
    }
