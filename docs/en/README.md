# Bearing Database: GOST and ISO Standards

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/en/bearings/selection_guide.md)
![Status](https://img.shields.io/badge/status-production-success.svg)

> Comprehensive reference system for rolling bearings according to GOST and ISO standards

[🇷🇺 Русская версия](../../README.md) | [📖 Selection Guide](bearings/selection_guide.md) | [📋 Equivalents Table](bearings/analogues/complete_analogues_table.md)

---

## Project Description

A reference database for rolling bearings that comply with GOST and ISO standards. The project includes technical documentation, specifications, classification, designation systems, equivalents, selection recommendations, and training materials.

## Purpose and Status

- **Purpose**: Unified production knowledge base for GOST/ISO bearings for training, selection, sales, and automation
- **Application areas**: Engineering calculation and selection, commercial proposal preparation, training of managers and engineers, Bitrix24 integration and automatic marking decoders
- **Update rules**: Data is taken only from offline-extracted materials; numerical values are transferred without rounding; each update records changes in GOST, ISO, Equivalents, Brands, and Tables sections
- **Sources**: DOCX files (see details in extracted knowledge index)
- **Database status**: Production — structure and data are aligned with extracted sources, ISO/GOST/Equivalents/Brands/Tables sections are ready for use

## ✨ Key Features

- 🔍 **Equivalents Search** - Quick lookup of GOST ↔ ISO correspondences
- 📊 **Technical Specifications** - Complete bearing specifications
- 🏭 **Manufacturer Database** - Information about brands and suppliers
- 📖 **Training Materials** - Guides for specialists
- 🔧 **Selection References** - Step-by-step selection instructions

## 📑 Table of Contents

### 🚀 Quick Start

- [📖 Bearing Selection Guide](bearings/selection_guide.md) - **Main document for selection**
- [📋 Step-by-Step Instructions](bearings/guides/README.md) - **Practical guides**
- [👨‍💼 Manager's Guide](bearings/training/managers_guide.md) - **Training material**
- [📚 Glossary of Terms](bearings/glossary.md) - **Terminology standardization**

### 📖 Main Documentation

#### Designation Systems
- [GOST Designations](bearings/designations/gost.md)
- [ISO Designations](bearings/designations/iso.md)
- [ISO Suffixes](bearings/designations/iso_suffixes.md)
- [Manufacturer Suffix Cross-Reference](bearings/designations/manufacturer_suffixes_cross_reference.md) - **Complete suffix correspondence table**

#### Bearing Equivalents
- [GOST ↔ ISO Equivalents Tables](bearings/analogues/README.md) - **Complete correspondence tables**
- [Complete Equivalents Table](bearings/analogues/complete_analogues_table.md) - **2000+ correspondence entries**
- [GOST/ISO Correspondence Table](bearings/analogues/gost_iso_table.md)
- [Equivalent Selection Examples](bearings/analogues/analog_examples.md)

#### Manufacturers and Brands
- [International Brands](bearings/brands/international_brands.md) - **Classification by quality and price**
- [Brand and Supplier Catalog](bearings/brands/supplier_directory.md) - **Alphabetical list of brands**
- [SKF Brand Overview](bearings/brands/skf_overview.md)
- [SKF Designation System](bearings/brands/skf_designation_system.md) - **Complete SKF designation guide**

#### Standards and Classification
- [GOST Standards](bearings/standards/gost_standards.md)
- [GOST Rolling Bearings - Complete Guide](bearings/gost_comprehensive_guide.md) - **Comprehensive GOST guide**
- [Bearing Classification](bearings/classification/README.md)

## Available Languages

- 🇷🇺 **Russian** (Main) - Complete documentation
- 🇬🇧 **English** (In Progress) - Key sections translated
  - [Selection Guide](bearings/selection_guide.md)
  - [Equivalents Table](bearings/analogues/complete_analogues_table.md)
  - [GOST Designations](bearings/designations/gost.md)
  - [ISO Designations](bearings/designations/iso.md)

## Structure

```
docs/en/                          # English documentation
├── README.md                     # This file
└── bearings/
    ├── selection_guide.md        # Bearing selection guide
    ├── analogues/                # Bearing equivalents
    │   ├── README.md
    │   └── complete_analogues_table.md
    ├── brands/                   # Manufacturers and brands
    │   └── international_brands.md
    ├── designations/             # Designation systems
    │   ├── gost.md
    │   └── iso.md
    └── standards/                # Standards
        └── gost_standards.md
```

## How to Use This Database

### For Engineers
1. **Find bearing equivalent**: Use [Equivalents Table](bearings/analogues/complete_analogues_table.md)
2. **Select bearing for equipment**: Follow [Selection Guide](bearings/selection_guide.md)
3. **Decode marking**: Check [GOST Designations](bearings/designations/gost.md) or [ISO Designations](bearings/designations/iso.md)

### For Procurement Managers
1. **Find alternative suppliers**: Use [Equivalents Table](bearings/analogues/complete_analogues_table.md)
2. **Understand manufacturer designations**: See [Manufacturer Suffix Cross-Reference](bearings/designations/manufacturer_suffixes_cross_reference.md)
3. **Choose manufacturer by budget**: Review [International Brands](bearings/brands/international_brands.md)

### For Students
1. **Learn basics**: Start with [GOST Complete Guide](bearings/gost_comprehensive_guide.md)
2. **Understand classification**: Study [Bearing Classification](bearings/classification/README.md)
3. **Practice with examples**: Use practical case studies

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](../../CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## Contact

For questions and suggestions, please open an issue in this repository.

---

**Note**: This is the English version of the documentation. For the most complete and up-to-date information, please refer to the [Russian version](../../README.md).

---

**Created**: 2025-12-29  
**Language**: English  
**Translation Status**: In Progress (Core sections completed)
