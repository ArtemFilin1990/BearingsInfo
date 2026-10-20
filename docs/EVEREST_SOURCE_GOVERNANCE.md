# EVEREST — external source governance (21 October 2026)

1. Primary manufacturer catalogues: SKF Product Select, NTN Bearing Finder, NSK online catalogue, Timken Engineering. Verify *exact* OEM SKU, publication edition and product feature before granting attribute provenance `CATALOG_VERIFIED`.
2. Secondary cross-references: IRBIS, Podshipnik.info, 2rs.com.ua, Podshipnikon.ru, Planeta Podshipnik, BearingWorks. Search candidates only. A listing of GOST=ISO is NOT an approved analogue.
3. Further candidates for source review: KOYO/JTEKT, AST, RBC, Kugellager Express, Sacom.lt, GlobalSpec, Size.name, Technodrive.pro, Universal Bearings. Recheck official domain, product coverage, copyright, terms and robots rules before any automated import.
4. Reject numeric zero dimensions, ambiguous width concept B/T/C/H, inferred tolerance equivalence and unsupported manufacturer suffixes. Keep the original supplier designation and source.
5. Every accepted attribute requires a source ID, document version, date, SKU and source location. Unknown or conflicting attributes block auto-replacement.
6. `IDT/MOD/NEQ` is a relationship of standard *editions*, not products.
7. Only a reviewed `analogue_decision` with immutable passport evidence and valid application scope can authorize a substitute.

Verified public landing pages:
- https://productselect.skf.com/
- https://bearingfinder.ntnamericas.com/
- https://www.nsk.com/catalogs-and-cad/
- https://engineering.timken.com/engineering-tool/bearing-search/
- https://www.rbcbearings.com/Catalogs-Industrial
- https://www.irbis.ua/ru/production/podshipniki-optom/razmery-podshipnikov
- https://podshipnik.info/catalog
- https://2rs.com.ua/ru/select-bearings/
- https://podshipnikon.ru/razmeri-podshipnikov
- https://planetapodshipnik.ru/news/post/tablica-markirovki-podshipnikov-iso-i-gost
- https://www.bearingworks.com/bearing-sizes/

Batch proof: 4,583 source rows; 874 matching dictionary brand tokens; 141 fully recognized suffix sequences; 4,583 auto-replacements denied because documented scoped approvals were absent. Locally validated with 42 pytest tests; no approval of product pairs.
