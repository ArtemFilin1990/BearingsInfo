# Repository Structure Diagram

This document provides a visual overview of the Baza repository structure and how different components interact.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Baza Repository                           │
│                  (Bearing Database GOST/ISO)                     │
└─────────────────────────────────────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
         ▼                     ▼                     ▼
   ┌─────────┐          ┌──────────┐         ┌──────────┐
   │  DATA   │          │   DOCS   │         │ SOURCES  │
   │  (CSV)  │          │   (MD)   │         │(PDF/DOCX)│
   └─────────┘          └──────────┘         └──────────┘
         │                     │                     │
         └─────────┬───────────┴─────────────────────┘
                   ▼
            ┌─────────────┐
            │   SCHEMAS   │
            │   (YAML)    │
            └─────────────┘
                   │
                   ▼
            ┌─────────────┐
            │   SCRIPTS   │
            │   (Python)  │
            └─────────────┘
                   │
                   ▼
            ┌─────────────┐
            │    TESTS    │
            │   (Python)  │
            └─────────────┘
```

## Directory Structure Flow

```
Baza/
│
├── 📄 Root Files ────────────────────────────────────────┐
│   ├── README.md          Main documentation (RU)        │
│   ├── README_en.md       English version                │
│   ├── INDEX.md           Navigation index               │
│   ├── RULES.md           Data formatting rules          │
│   ├── SOURCES.md         Sources catalog                │
│   ├── CONTRIBUTING.md    Contribution guide             │
│   ├── CHANGELOG.md       Version history                │
│   ├── AGENT.md           GitHub agent specs             │
│   └── manage.py          Unified CLI interface          │
│                                                          │
├── 💾 data/ ─────────────────────────────────────────────┤
│   │   Structured CSV data files                         │
│   ├── gost/          GOST standard bearings             │
│   ├── iso/           ISO standard bearings              │
│   ├── analogs/       GOST ↔ ISO equivalents            │
│   ├── brands/        Manufacturer information           │
│   └── reports/       Auto-generated update reports      │
│                                                          │
├── 📚 docs/ ─────────────────────────────────────────────┤
│   │   Documentation and articles                        │
│   ├── bearings/      Main bearing documentation         │
│   ├── articles/      Article database (122 articles)    │
│   ├── images/        Diagrams and illustrations         │
│   ├── en/            English translations               │
│   └── *.md           Various guides and indexes         │
│                                                          │
├── 📋 schemas/ ──────────────────────────────────────────┤
│   │   Data validation schemas (YAML/JSON)               │
│   ├── gost.yaml      GOST data schemas                  │
│   ├── iso.yaml       ISO data schemas                   │
│   ├── brands.yaml    Brand data schemas                 │
│   └── *.yaml         Other schema definitions           │
│                                                          │
├── 🔧 sources/ ──────────────────────────────────────────┤
│   │   Original source materials                         │
│   ├── gost/          GOST standards (PDF)               │
│   ├── iso/           ISO standards (PDF)                │
│   ├── brands/        Manufacturer catalogs              │
│   ├── skf/           SKF-specific materials             │
│   └── */meta.yaml    Metadata for each category         │
│                                                          │
├── 🛠️ tools/scripts/ ──────────────────────────────────┤
│   │   Processing and automation scripts                 │
│   ├── extract/       Data extraction scripts            │
│   ├── validate/      Data validation tools              │
│   ├── normalize/     Data normalization                 │
│   └── *.py           Various utility scripts            │
│                                                          │
└── ✅ tests/ ────────────────────────────────────────────┘
    │   Test suites
    └── test_*.py      Unit and integration tests
```

## Data Flow Diagram

```
┌─────────────┐
│   SOURCES   │  Original PDFs, DOCX, catalogs
│ (PDF/DOCX)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  EXTRACT    │  tools/scripts/extract/raw_datasets.py
│  (Python)   │  sources/pdf_text_extractor.py
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  RAW DATA   │  Temporary extracted data
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ NORMALIZE   │  tools/scripts/update_repo.py
│  (Python)   │  • Sort data
└──────┬──────┘  • Remove duplicates
       │         • Format CSV
       ▼
┌─────────────┐
│  VALIDATE   │  tools/scripts/validate/run_validations.py
│  (Python)   │  • Check schemas
└──────┬──────┘  • Verify types
       │         • Test uniqueness
       ▼
┌─────────────┐
│    DATA     │  Final CSV files
│   (CSV)     │  data/gost/, data/iso/, etc.
└──────┬──────┘
       │
       ├────────────────────────────┐
       │                            │
       ▼                            ▼
┌─────────────┐            ┌─────────────┐
│ DOCUMENTATION│            │   REPORTS   │
│    (MD)     │            │   (JSON)    │
└─────────────┘            └─────────────┘
```

## Workflow Diagram

### Adding New Data

```
1. Add Source
   └─> Place PDF in sources/<category>/
   └─> Update sources/<category>/meta.yaml

2. Extract (optional)
   └─> python tools/scripts/extract/raw_datasets.py
   └─> or manual CSV creation

3. Normalize
   └─> python manage.py normalize
   └─> Sorts and formats CSV

4. Validate
   └─> python manage.py validate
   └─> Checks against schemas

5. Test
   └─> python manage.py test
   └─> Runs test suite

6. Report
   └─> python manage.py report
   └─> Generates JSON report

7. Commit
   └─> git add .
   └─> git commit -m "Add data from SOURCE"
   └─> git push
```

### Contributing Documentation

```
1. Choose Article
   └─> docs/articles/<category>/<article>.md

2. Write Content
   └─> Follow template structure
   └─> Add examples
   └─> Link to CSV data

3. Add Images (optional)
   └─> Place in docs/images/<subcategory>/
   └─> Reference in article

4. Validate Structure
   └─> python tools/scripts/validate_articles_structure.py

5. Test Links
   └─> Check relative paths
   └─> Verify data references

6. Commit
   └─> git add docs/
   └─> git commit -m "Add article: TITLE"
   └─> git push
```

## Component Interactions

```
┌──────────────────────────────────────────────────────────┐
│                    User Interaction                       │
└───────────────────┬──────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   ┌────────┐  ┌────────┐  ┌────────┐
   │ README │  │  CLI   │  │  Docs  │
   │        │  │manage.py  │        │
   └────┬───┘  └───┬────┘  └───┬────┘
        │          │           │
        └──────────┼───────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
   ┌────────┐ ┌────────┐ ┌────────┐
   │ Scripts│ │ Schemas│ │  Data  │
   └────┬───┘ └───┬────┘ └───┬────┘
        │         │          │
        └─────────┼──────────┘
                  │
                  ▼
           ┌────────────┐
           │   Tests    │
           └────────────┘
```

## CI/CD Pipeline

```
┌─────────────┐
│  Git Push   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ GitHub Actions  │
└──────┬──────────┘
       │
       ├─────────────┐
       │             │
       ▼             ▼
┌──────────┐   ┌──────────┐
│ Validate │   │  Tests   │
│  Python  │   │ (pytest) │
└────┬─────┘   └────┬─────┘
     │              │
     ├──────────────┘
     │
     ▼
┌──────────┐
│ Validate │
│   CSV    │
└────┬─────┘
     │
     ▼
┌──────────┐
│  Build   │
│  Report  │
└────┬─────┘
     │
     ├───────────────┐
     │               │
     ▼               ▼
┌─────────┐    ┌─────────┐
│  Pass   │    │  Fail   │
│ Merge OK│    │  Block  │
└─────────┘    └─────────┘
```

## Schema-Data Relationship

```
schemas/gost.yaml ───────────┐
                             │
                             ├──> Validates
                             │
data/gost/bearings.csv ──────┘
data/gost/dimensions.csv ────┐
data/gost/series.csv ────────┤
data/gost/tolerances.csv ────┤
                             │
                             ├──> Referenced by
                             │
docs/articles/*.md ──────────┘
```

## Quick Reference: Key Files

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `README.md` | Main documentation | On major changes |
| `INDEX.md` | Navigation hub | Monthly |
| `SOURCES.md` | Source catalog | When adding sources |
| `manage.py` | CLI interface | Rarely |
| `schemas/*.yaml` | Data validation | When data structure changes |
| `data/**/*.csv` | Actual data | Frequently |
| `docs/articles/**/*.md` | Content articles | Frequently |
| `tests/test_*.py` | Test suites | When adding features |

## Support Resources

- **Main README**: [README.md](../README.md)
- **Navigation**: [INDEX.md](../INDEX.md)
- **Contributing**: [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Scripts Guide**: [tools/scripts/README.md](../tools/scripts/README.md)
- **CLI Help**: `python manage.py help`

---

**Last Updated**: December 31, 2025  
**Version**: 1.0.1
