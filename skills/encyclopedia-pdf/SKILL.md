---
name: encyclopedia-pdf
description: Use when generating the bearing encyclopedia PDF book. Collects data from all repository sources (nomenclature, GOST/ISO, brands, analogs, articles, catalog markdowns), assembles chapter content via sub-agents, and renders a formatted Russian-language PDF using reportlab.
---

# Encyclopedia PDF Skill

## Purpose

Generate `out/encyclopedia_bearings.pdf` — a complete Russian-language reference book on bearings from all repository data sources.

## Chapter structure

1. Введение — что такое подшипник, история, применение
2. Классификация и типы подшипников
3. Система обозначений (ГОСТ, ISO, DIN)
4. Классы точности и зазоры
5. Размеры и параметры (таблицы из nomenclature.csv)
6. Материалы, смазка, сепараторы
7. Аналоги и взаимозаменяемость (gost_iso.csv, import_analogs.csv)
8. Производители и бренды (brands.csv)
9. Эксплуатация, монтаж, ресурс
10. Справочные таблицы (допуски, посадки, ТН ВЭД)

## Entry point

```bash
python tools/scripts/generate_encyclopedia_pdf.py
```

Output: `out/encyclopedia_bearings.pdf`

## Rules

- All text in Russian.
- Cyrillic font: DejaVuSans (bundled with reportlab or from /usr/share/fonts).
- Tables from CSV files go into chapters 5, 7, 8, 10.
- Markdown articles from data/inbox/inbox/ and data/katalogi/ feed chapters 1–4, 6, 9.
- Page numbers, TOC, and chapter headings required.
- Max rows per table page: 40.
