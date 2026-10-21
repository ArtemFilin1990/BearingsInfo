# EVEREST — проверенный словарь кодов производителей (этап 2)

Назначение: документировать **значения кодов обозначения подшипников** с первичным источником, производителем и областью применения. Совпадение обозначений, размеров или свойств НЕ подтверждает аналог ГОСТ/ISO и НЕ разрешает замену.

## Данные

- `data/reference/verified_manufacturer_codes.csv`: 55 записей, ключ `(manufacturer, component, code)`; сохранены значение, тип контакта, количество сторон, применимость, URL источника, место в документе, дата проверки. Статус `OFFICIAL_CODE_ONLY` — доказано только значение кода, не полная взаимозаменяемость.
- `data/reference/verified_manufacturers.csv`: пять отдельно распознаваемых брендов: SKF, NSK, NTN, FAG, INA. Для INA кодов пока нет. Принадлежность FAG и INA к группе Schaeffler НЕ делает суффиксы одинаковыми.
- `src/verified_designation_dictionary.py`: точный поиск производителя, разбор составных суффиксов и проверка источников. Не вызывает продуктивный импорт.
- `tests/test_verified_dictionary.py`: тесты контактности, уникальности, префиксов и отказов при неизвестных кодах.

## Алгоритм применения к нормализованному прайсу

1. Сохранить маркировку с первичного документа в отдельном поле без правок.
2. Подтвердить бренд. Если бренд неизвестен — `UNKNOWN_BRAND`, не подставлять производителя на основании суффикса.
3. Сохранить конструктивные базовые группы (например `NU`, `NJ`, `NUP`) вместе с телом; это не отдельные необязательные приставки.
4. Отделять только подтверждённый брендовый префикс: NTN `4T-` и `TS2` — контекстно зависимые коды, не применяются к SKF.
5. Суффикс `SKF 2RSH/C3` разбирается как `2RSH` + `C3`. `NSK DDUCM` — `DDU` + `CM`. Незнакомые части сохраняются и переводят запись в `REVIEW_UNKNOWN_CODE`.
6. `VERIFIED_CODE_SCOPE_REVIEW` означает, что смысл кодов найден по документации. Для карточки конкретного товара ещё требуется сверить применимость к типу, конструкцию, ревизию и данные производителя.
7. Аналог ГОСТ↔ISO утверждается отдельно после проверки прямого соответствия в каталоге, `d/D/B/T`, типа, контактности, зазора, точности, сепаратора, конусности, смазки и монтажных ограничений.

## Ограничения

- Контактное уплотнение `DDU` NSK и `LLU` NTN имеет схожую функцию, но **не даёт** оснований считать подшипники взаимозаменяемыми.
- В публикации FAG WL 43 163 обозначения подтверждены для указанного исторического семейства. При применении к новой продукции требуется актуальный каталог Schaeffler.
- Код `TS2` NTN означает термостабилизацию колец, а не автоматическую работоспособность подшипника в сборе при той же температуре.
- Код `W33` SKF относится к соответствующим конструкциям сферических роликовых подшипников; не применять к произвольным сериям.

## Первоисточники

- SKF — https://evolution.skf.com/en/added-versatility-as-use-of-rsh-heavy-duty-seals-is-extended/
- SKF Bearing Designations (2020) — https://benelux.promo.skf.com/acton/attachment/21304/f-55e38212-9419-4532-a361-8c1a9aab6720/0/-/-/-/file.pdf?sid=TV2%3AFx2eJqRHy
- NSK Deep Groove Ball Bearings, pp. 7, 9 — https://www.nsk.com/content/dam/nsk-marketing/projects-completed/literature/product-brochures/deep-grooves-bbs_product-brochure/en_deep-grooves-bbs_product-brochure/preview-pdf_deep-grooves-bbs_product-brochure_en/EN_Deep%20Grooves%20BBs_Product_Brochure_low-res.pdf
- NTN Numbering System Quick Reference, p. 5 — https://ntnamericas.com/wp-content/uploads/2025/12/UPDATED-NTN-Catalog-Gen-NomenclatureQRG-A-22NTNQREF.pdf
- NTN FAQ, 4T- — https://ntnamericas.com/technical-resources/faqs/
- FAG Deep Groove Ball Bearings WL 43 163 (1997) — https://www.schaeffler.com/remotemedien/media/_shared_media/08_media_library/01_publications/schaeffler_2/publication/downloads_18/wl_43163_de_en.pdf

## Контроль

```bash
python -m pytest tests/test_verified_dictionary.py -q
```

Словарь создаётся как самостоятельный проверяемый слой. Его подключение к `src/bearing_designation.py` и обновление реального прайса выполняются отдельным этапом после тестирования на фактических строках и проверки CI.
