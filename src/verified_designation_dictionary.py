"""Source-verified manufacturer-specific bearing code dictionary.

A verified suffix meaning is not a confirmed ГOСТ↔ISO analogue.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_CODES = Path(__file__).resolve().parents[1] / "data/reference/verified_manufacturer_codes.csv"
DEFAULT_BRANDS = Path(__file__).resolve().parents[1] / "data/reference/verified_manufacturers.csv"
_OFFICIAL_HOSTS = ("skf.com", "nsk.com", "ntnamericas.com", "ntnglobal.com", "schaeffler.com")
_COMPONENTS = {"suffix", "prefix", "basic_family"}
_CONTACT_TYPES = {"contact", "noncontact", "light_contact", "shield", "unspecified"}


@dataclass(frozen=True)
class VerifiedCode:
    manufacturer: str
    code: str
    component: str
    feature: str
    contact_type: str
    sides: str
    meaning_ru: str
    bearing_scope: str
    source_url: str
    source_locator: str
    verified_on: str
    verification_status: str


@dataclass(frozen=True)
class DecodeResult:
    manufacturer: str | None
    original: str
    codes: tuple[VerifiedCode, ...]
    unknown_parts: tuple[str, ...]
    status: str


def _official(url: str) -> bool:
    p = urlparse(url)
    host = (p.hostname or "").lower()
    return p.scheme == "https" and any(host == h or host.endswith("." + h) for h in _OFFICIAL_HOSTS)


class VerifiedCodebook:
    """Strict brand-scoped lookup; does not infer product compatibility."""

    def __init__(self, codes_path: Path | str = DEFAULT_CODES, brands_path: Path | str = DEFAULT_BRANDS):
        self.codes: dict[tuple[str, str, str], VerifiedCode] = {}
        self.brands: set[str] = set()
        with Path(brands_path).open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                brand = row["brand_token"].strip().upper()
                if not _official(row["official_site"]):
                    raise ValueError("Non-official brand source: " + brand)
                if not brand or brand in self.brands:
                    raise ValueError("Duplicate/blank brand: " + brand)
                if row["canonical_brand"].strip().upper() != brand:
                    raise ValueError("Brand aliases require explicit separate verification")
                self.brands.add(brand)
        with Path(codes_path).open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                c = VerifiedCode(**row)
                key = (c.manufacturer, c.component, c.code)
                if c.manufacturer not in self.brands or c.code != c.code.upper():
                    raise ValueError("Unknown brand or noncanonical code: " + str(key))
                if c.component not in _COMPONENTS or c.contact_type not in _CONTACT_TYPES:
                    raise ValueError("Invalid component/contact category: " + str(key))
                if not _official(c.source_url):
                    raise ValueError("Non-official URL: " + str(key))
                if not c.source_locator or not c.bearing_scope or c.verification_status != "OFFICIAL_CODE_ONLY":
                    raise ValueError("Missing scope/provenance or invalid status: " + str(key))
                if key in self.codes:
                    raise ValueError("Duplicate manufacturer+component+code: " + str(key))
                self.codes[key] = c

    def lookup(self, manufacturer: str, code: str, component: str = "suffix") -> VerifiedCode | None:
        """Never silently inherit codes of another brand or parent group."""
        return self.codes.get((manufacturer.strip().upper(), component, code.strip().upper()))

    def decode_suffix(self, manufacturer: str | None, suffix: str) -> DecodeResult:
        """Longest exact codes only. Never drop unresolved segments."""
        raw = suffix or ""
        brand = manufacturer.strip().upper() if manufacturer else None
        if not brand or brand not in self.brands:
            return DecodeResult(brand, raw, (), (raw,) if raw else (), "UNKNOWN_BRAND")
        s = raw.strip().upper()
        known = sorted(
            (c for (b, component, _), c in self.codes.items() if b == brand and component == "suffix"),
            key=lambda entry: (-len(entry.code), entry.code),
        )
        codes: list[VerifiedCode] = []
        unknown: list[str] = []
        i = 0
        while i < len(s):
            if s[i] in " -/.":
                i += 1
                continue
            hit = next((c for c in known if s.startswith(c.code, i)), None)
            if hit:
                codes.append(hit)
                i += len(hit.code)
            else:
                j = i + 1
                while j < len(s) and s[j] not in " -/.":
                    j += 1
                unknown.append(s[i:j])
                i = j
        status = "VERIFIED_CODE_SCOPE_REVIEW" if codes and not unknown else "REVIEW_UNKNOWN_CODE"
        if not s:
            status = "EMPTY"
        return DecodeResult(brand, raw, tuple(codes), tuple(unknown), status)

    def match_prefix(self, manufacturer: str | None, designation: str) -> tuple[VerifiedCode | None, str]:
        """Only documented OEM prefixes; NU/NJ/NUP remain in the base designation."""
        s = designation.strip().upper()
        brand = manufacturer.strip().upper() if manufacturer else ""
        candidates = sorted(
            (c for (b, typ, _), c in self.codes.items() if b == brand and typ == "prefix"),
            key=lambda c: -len(c.code),
        )
        for c in candidates:
            if s.startswith(c.code):
                return c, s[len(c.code):].lstrip(" -")
        return None, s


def assess_code_level_compatibility(left: VerifiedCode, right: VerifiedCode) -> str:
    """Detect semantic conflict; even matching features cannot prove interchangeability."""
    if left.feature != right.feature or left.contact_type != right.contact_type or left.sides != right.sides:
        return "DIFFERENT_TECHNICAL_FEATURE"
    return "SAME_FEATURE_NOT_PROVEN_INTERCHANGEABLE"
