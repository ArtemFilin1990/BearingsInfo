# 🔧 Database: GOST and ISO Bearings

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/bearings/selection_guide.md)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Last Update](https://img.shields.io/badge/updated-10.01.2026-blue.svg)
![Articles](https://img.shields.io/badge/articles-122-green.svg)
![Catalogs](https://img.shields.io/badge/catalogs-150+-orange.svg)

> 📚 Comprehensive reference system for rolling bearings according to GOST and ISO standards

## 📋 Table of Contents

- [Project Description](#project-description)
- [Repository Structure](#repository-structure)
- [Quick Start](#quick-start)
- [Article Categories](#article-categories)
- [Data and Tools](#data-and-tools)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [Related Resources](#related-resources)
- [License](#license)

## 🎯 Project Description

A reference database for rolling bearings that comply with GOST and ISO standards. The project includes technical documentation, specifications, classification, designations, analogs, and selection recommendations, as well as training materials.

### ✨ Key Features

- 🔍 **Analog Search** - quick selection of GOST ↔ ISO equivalents
- 📊 **Technical Specifications** - complete bearing specifications
- 🏭 **Manufacturer Database** - information about brands and suppliers
- 📖 **Training Materials** - guides for specialists
- 🔧 **Selection Guides** - step-by-step selection instructions
- 💾 **Structured Data** - CSV files with dimensions, tolerances, analogs
- 🛠️ **Processing Tools** - Python scripts for validation and data normalization
- 📚 **122 Articles** - comprehensive knowledge base
- 📂 **150+ Catalogs** - manufacturer catalogs in Markdown format

## 📁 Repository Structure

```
Baza/
├── 📊 data/           # Data in CSV format (GOST, ISO, analogs, brands)
├── 📚 docs/           # Documentation and articles
│   ├── articles/      # Knowledge base (122 articles)
│   ├── bearings/      # Reference guides and manuals
│   ├── gost/          # GOST standards
│   └── iso/           # ISO standards
├── 🖼️  Изображения/    # Images from articles and documentation
├── 📖 Статьи/         # Technical documentation (122 articles)
│   ├── 01_Подбор_и_поиск/              # Selection and search
│   ├── 02_Обозначения_и_маркировка/    # Designations and marking
│   ├── 05_Типы_подшипников/            # Bearing types
│   ├── 07_ГОСТ_и_ISO/                  # GOST and ISO standards
│   ├── 10_Производители/               # Manufacturers
│   └── 14_Справочная_информация/       # Reference information
├── 📂 Каталоги/       # Manufacturer catalogs in Markdown (150+ catalogs)
├── 📋 schemas/        # Data schemas (YAML)
├── 🛠️  tools/scripts/  # Processing and validation scripts
├── 🔧 sources/        # Source materials (PDFs, catalogs, standards)
└── ✅ tests/          # Tests
```

## 🚀 Quick Start

### Main Documents

📖 **[Bearing Selection Guide](docs/bearings/selection_guide.md)** - Main selection document  
👨‍💼 **[Manager's Guide](docs/bearings/training/managers_guide.md)** - Training material  
🗺️ **[Full Navigation](docs/NAVIGATION_GUIDE.md)** - Detailed repository navigation  
📇 **[Data Index](INDEX.md)** - Detailed index of all data

### Manufacturer Catalogs

📂 **[Каталоги/](Каталоги/)** - 150+ manufacturer catalogs in Markdown format

## 📚 Article Categories

| Category | Count | Description |
|----------|-------|-------------|
| 📌 **[Selection & Search](Статьи/01_Подбор_и_поиск/)** | 3 articles | Bearing selection and search methods |
| 🏷️ **[Designations & Marking](Статьи/02_Обозначения_и_маркировка/)** | 3 articles | Designation and marking systems |
| 🎯 **[Precision Classes](Статьи/03_Классы_точности/)** | 1 article | Bearing precision classes |
| 📏 **[Clearances](Статьи/04_Зазоры/)** | 1 article | Radial and axial clearances |
| 🔩 **[Bearing Types](Статьи/05_Типы_подшипников/)** | 9 articles | Classification and types |
| ⚙️ **[Construction](Статьи/06_Конструкция/)** | 6 articles | Design features |
| 📋 **[GOST & ISO](Статьи/07_ГОСТ_и_ISO/)** | 9 articles | Standards and equivalents |
| 📊 **[Technical Specs](Статьи/08_Технические_характеристики/)** | 8 articles | Technical parameters |
| 🔧 **[Operation](Статьи/09_Эксплуатация/)** | 1 article | Maintenance and lubrication |
| 🏭 **[Manufacturers](Статьи/10_Производители/)** | 13 articles | Manufacturer information |
| 🛠️ **[Drives & Components](Статьи/12_Приводы_и_компоненты/)** | 7 articles | Drive technology |
| 📖 **[Literature](Статьи/13_Литература/)** | 1 article | Reference literature |
| 📑 **[Reference Info](Статьи/14_Справочная_информация/)** | 60 articles | Reference materials |

## 💾 Data and Tools

### Structured Data (CSV)

#### GOST
- [`data/gost/bearings.csv`](data/gost/bearings.csv) - GOST bearings
- [`data/gost/dimensions.csv`](data/gost/dimensions.csv) - Dimensions
- [`data/gost/series.csv`](data/gost/series.csv) - Series
- [`data/gost/tolerances.csv`](data/gost/tolerances.csv) - Tolerances

#### ISO
- [`data/iso/bearings.csv`](data/iso/bearings.csv) - ISO bearings
- [`data/iso/dimensions.csv`](data/iso/dimensions.csv) - Dimensions
- [`data/iso/prefixes.csv`](data/iso/prefixes.csv) - Prefixes
- [`data/iso/suffixes.csv`](data/iso/suffixes.csv) - Suffixes

#### Analogs
- [`data/analogs/gost_iso.csv`](data/analogs/gost_iso.csv) - GOST ↔ ISO equivalents
- [`data/analogs/units.csv`](data/analogs/units.csv) - Bearing units
- [`data/analogs/housings.csv`](data/analogs/housings.csv) - Housings

#### Brands
- [`data/brands/brands.csv`](data/brands/brands.csv) - Manufacturer and brand database

## 🔨 Installation and Usage

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArtemFilin1990/Baza.git
   cd Baza
   ```

2. Install dependencies for Python scripts:
   ```bash
   pip install -r requirements.txt
   ```

3. Start with the main guide:
   - [📖 Bearing Selection Guide](docs/bearings/selection_guide.md)
   - [👨‍💼 Manager's Guide](docs/bearings/training/managers_guide.md)

### Working with Data

**Data normalization:**
```bash
python tools/scripts/update_repo.py
```

**Data validation:**
```bash
python tools/scripts/validate/run_validations.py
```

**Running tests:**
```bash
pytest tests/
```

## 🤝 Contributing

We welcome contributions to the project! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### How to Contribute

1. Fork the repository
2. Create a branch for your feature
3. Make changes and validate them
4. Commit and open a Pull Request

### Guidelines

- Use clear commit messages
- Document added code
- Follow existing coding style
- Add tests for new functionality
- Validate CSV data before committing
- Cite sources for all technical data (GOST, ISO, catalogs)

## 📚 Related Resources

- [GOST 520-2002](http://docs.cntd.ru/) - Rolling bearings. General specifications
- [GOST 3478-2012](http://docs.cntd.ru/) - Basic standards of interchangeability
- [GOST 24810-2013](http://docs.cntd.ru/) - Rolling bearings. Internal design

## 📞 Technical Support

For questions about using the database:
- GitHub Issues: [create issue](../../issues)

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Note**: This database is for reference purposes. For critical applications, always verify with current GOST standards and manufacturer technical documentation.

## 📌 Version and Updates

**Current version:** 1.1.0  
**Last update:** January 10, 2026  
**Articles:** 122  
**Catalogs:** 150+  
**Images:** 688

---

© 2025 ArtemFilin1990. All rights reserved.

---

[🇷🇺 Русская версия](README.md) | [📇 Index](INDEX.md) | [📂 Catalogs](Каталоги/README.md) | [📚 Articles](Статьи/README.md)
