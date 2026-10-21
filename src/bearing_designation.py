"""Conservative bearing-designation parsing and interchangeability checks.

This module is intentionally independent of the production catalog importer.
It returns review statuses rather than inventing analogues or dropping suffixes.

Designation-system background:
- SKF basic bearing designation, see docs/everest_designation_pilot.md
- NTN seal nomenclature: https://ntnamericas.com/technical-resources/faqs/
- NSK DDU/VV nomenclature: https://www.nsk.com/engineering/6022ddu-dgbb-sr.html
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

ParseStatus = Literal["PARSED", "REVIEW", "INVALID"]
AnalogueStatus = Literal[
    "REJECTED", "DIMENSIONAL_CANDIDATE", "BASIC_MATCH", "CONFIRMED", "INSUFFICIENT_DATA"
]

# Brands must be standalone tokens at one end of the supplier's designation.
_BRANDS = {
    "SKF",
    "FAG",
    "NSK",
    "NTN",
    "KOYO",
    "TIMKEN",
    "INA",
    "IKO",
    "SNR",
    "ZKL",
    "KINEX",
    "ВПП",
    "ВПЗ",
    "СПЗ",
    "ГПЗ",
    "МПЗ",
}
# These are part of the basic ISO designation, not detachable manufacturer prefixes.
_SERIES = (
    "NUP", "UCFL", "UCFC", "UCP", "RNA", "NJL", "NU", "NJ",
    "NF", "NA", "HK", "BK", "QJ", "UC", "UK", "N",
)
# Manufacturer-dependent suffixes: decoding these for other brands is NOT supported.
_SUFFIX_MEANINGS: dict[str, dict[str, str]] = {
    "NSK": {
        "DDU": "contact_seal_2", "VV": "noncontact_seal_2",
        "ZZ": "shield_2", "CM": "electric_motor_clearance",
    },
    "NTN": {"LLU": "contact_seal_2", "LLB": "noncontact_seal_2", "ZZ": "shield_2"},
    "SKF": {"2RS1": "contact_seal_2", "2Z": "shield_2", "ECP": "internal_design"},
    "FAG": {"2RSR": "contact_seal_2"},
}
_GENERIC_SUFFIXES = {
    "C1": "clearance", "C2": "clearance", "C3": "clearance",
    "C4": "clearance", "C5": "clearance",
    "P2": "precision", "P4": "precision", "P5": "precision", "P6": "precision",
}
_ALL_SUFFIX_CODES = sorted(
    set(_GENERIC_SUFFIXES)
    | {code for codes in _SUFFIX_MEANINGS.values() for code in codes}
    | {"2RS", "2Z", "ZZ", "W33", "ECP"},
    key=len, reverse=True,
)
_NUMERIC_BASE = re.compile(r"^(?P<base>\d{3,7})(?P<tail>.*)$")
_PREFIX = re.compile(r"^(?P<prefix>\d{1,2}-)(?P<rest>\d{3,7}(?:\b|[- /]|$).*)$")
_VALID_CHARS = re.compile(r"^[\w\s./+\-]+$", re.UNICODE)


@dataclass(frozen=True)
class ParsedDesignation:
    raw: str
    normalized_input: str
    brand: str | None
    standard_hint: str
    prefix: str
    body: str
    suffix: str
    suffix_codes: tuple[str, ...]
    suffix_meanings: tuple[str, ...]
    status: ParseStatus
    issues: tuple[str, ...]

    @property
    def full_code(self) -> str:
        return f"{self.prefix}{self.body}{self.suffix}"


def _suffix_tokens(suffix: str) -> tuple[str, ...]:
    """Tokenize known suffixes greedily, retaining unknown fragments for review."""
    pending = re.sub(r"^[\s./-]+", "", suffix)
    tokens: list[str] = []
    while pending:
        if pending[0] in " /.-":
            pending = pending[1:]
            continue
        matched = next((code for code in _ALL_SUFFIX_CODES if pending.startswith(code)), None)
        if matched:
            tokens.append(matched)
            pending = pending[len(matched) :]
            continue
        fragment = re.match(r"^[^ /.-]+", pending)
        if fragment:
            tokens.append(fragment.group())
            pending = pending[len(fragment.group()) :]
        else:
            tokens.append(pending[0])
            pending = pending[1:]
    return tuple(tokens)


def parse_designation(text: str, brand: str | None = None) -> ParsedDesignation:
    """Parse a supplier code without guessing ГОСТ/ISO conversion or interchangeability.

    A typed brand argument overrides the absence of a brand in supplier text; conflicting
    brands explicitly require review. Do not use the standard_hint as a confirmed standard.
    """
    raw = text or ""
    value = re.sub(r"\s+", " ", raw.strip().upper())
    explicit_brand = brand.upper().strip() if brand else None
    problems: list[str] = []
    if not value or not _VALID_CHARS.fullmatch(value):
        return ParsedDesignation(
            raw, value, explicit_brand, "UNKNOWN", "", "", "", (), (),
            "INVALID", ("empty_or_invalid_chars",),
        )

    if value.startswith("ПОДШИПНИК "):
        value = value[len("ПОДШИПНИК ") :]
    if value.startswith("BEARING "):
        value = value[len("BEARING ") :]
    words = value.split(" ")
    found: list[str] = []
    while words and words[0] in _BRANDS:
        found.append(words.pop(0))
    while words and words[-1] in _BRANDS:
        found.append(words.pop())
    value = " ".join(words)
    if len(set(found + ([explicit_brand] if explicit_brand else []))) > 1:
        problems.append("conflicting_brands")
    manufacturer = explicit_brand or (found[0] if found else None)
    if manufacturer and manufacturer not in _BRANDS:
        problems.append("unrecognized_brand")

    if re.search(r"[A-Z]", value) and re.search(r"[А-ЯЁ]", value):
        problems.append("mixed_latin_cyrillic")
    if "+" in value or "(" in value or ")" in value:
        problems.append("multiple_parts_or_description")

    prefix = ""
    match_prefix = _PREFIX.match(value)
    if match_prefix:
        prefix = match_prefix.group("prefix")
        value = match_prefix.group("rest")

    value = re.sub(r"\s+", " ", value).strip()
    series = next((series for series in _SERIES if re.match(rf"^{series}\s*\d", value)), None)
    if series:
        m = re.match(rf"^{series}\s*(\d{{2,6}})(.*)$", value)
        assert m is not None
        body = f"{series}{m.group(1)}"
        suffix = m.group(2)
        standard = "ISO_CANDIDATE"
    else:
        m = _NUMERIC_BASE.match(value)
        if not m:
            return ParsedDesignation(
                raw, value, manufacturer, "UNKNOWN", prefix, "", value, (), (),
                "INVALID", ("missing_basic_code",),
            )
        body = m.group("base")
        suffix = m.group("tail")
        standard = "ISO_CANDIDATE" if len(body) in (4, 5) and body.startswith(("6", "7")) else "GOST_CANDIDATE"

    suffix = suffix.upper()
    codes = _suffix_tokens(suffix)
    meanings: list[str] = []
    for code in codes:
        meaning = _GENERIC_SUFFIXES.get(code) or _SUFFIX_MEANINGS.get(manufacturer or "", {}).get(code)
        meanings.append(meaning or "unresolved")
        if meaning is None:
            problems.append(f"unresolved_suffix:{code}")
    if prefix and prefix[:-1] not in {"0", "2", "4", "5", "6", "7"}:
        problems.append("unverified_gost_prefix")
    if not body:
        problems.append("missing_basic_code")
    status: ParseStatus = "REVIEW" if problems else "PARSED"
    return ParsedDesignation(
        raw, value, manufacturer, standard, prefix, body, suffix, codes,
        tuple(meanings), status, tuple(dict.fromkeys(problems)),
    )


@dataclass(frozen=True)
class BearingSpecification:
    designation: str
    bearing_type: str | None = None
    d: float | None = None
    D: float | None = None
    width: float | None = None  # Must refer to the same dimensional concept (B/T/C).
    width_kind: str | None = None
    sealing: str | None = None
    clearance: str | None = None
    precision: str | None = None
    cage: str | None = None
    bore_type: str | None = None


@dataclass(frozen=True)
class AnalogueAssessment:
    status: AnalogueStatus
    reasons: tuple[str, ...]


def assess_analogue(
    left: BearingSpecification,
    right: BearingSpecification,
    *,
    documented_crossref: bool = False,
    verified_source: bool = False,
    negative_note: bool = False,
) -> AnalogueAssessment:
    """Fail closed: an apparent ISO match is never equivalent to a proven replacement.

    A verified cross-reference must come from independent reviewed evidence. Raw rows
    in data/analogs/*.csv alone should pass verified_source=False.
    """
    if negative_note:
        return AnalogueAssessment("REJECTED", ("source_explicitly_rejects_replacement",))

    critical = (
        "bearing_type", "d", "D", "width", "width_kind", "sealing",
        "clearance", "precision", "cage", "bore_type",
    )
    conflicts = [
        field for field in critical
        if getattr(left, field) is not None
        and getattr(right, field) is not None
        and getattr(left, field) != getattr(right, field)
    ]
    if conflicts:
        return AnalogueAssessment("REJECTED", tuple(f"mismatch:{field}" for field in conflicts))

    sizes = ("d", "D", "width", "width_kind", "bearing_type")
    if any(getattr(left, f) is None or getattr(right, f) is None for f in sizes):
        return AnalogueAssessment("INSUFFICIENT_DATA", ("type_or_dimensions_missing",))

    if not documented_crossref:
        return AnalogueAssessment("DIMENSIONAL_CANDIDATE", ("no_direct_cross_reference",))
    if not verified_source:
        return AnalogueAssessment("DIMENSIONAL_CANDIDATE", ("cross_reference_not_independently_verified",))

    unknown = [f for f in critical if getattr(left, f) is None or getattr(right, f) is None]
    if unknown:
        return AnalogueAssessment("BASIC_MATCH", tuple(f"unverified:{f}" for f in unknown))
    return AnalogueAssessment("CONFIRMED", ("catalogue_attributes_match",))


@dataclass(frozen=True)
class ConversionCandidate:
    gost: str
    iso: str
    scope: str
    decision: str
    source: str
    notes: str


def lookup_gost_iso(gost_designation: str, csv_path: str | None = None) -> tuple[ConversionCandidate, ...]:
    """Look up explicit curated correspondences; NEVER compute ISO from the digits.

    Curated rows are still only candidates; a separate assess_analogue call is
    required to confirm a physical substitute. No fuzzy, prefix-stripped or
    suffix-stripped matching is permitted.
    """
    path = (
        Path(csv_path) if csv_path
        else Path(__file__).resolve().parents[1] / "data/reference/everest_gost_iso_candidates.csv"
    )
    query = gost_designation.strip().upper()
    matches = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["gost"].strip().upper() == query:
                matches.append(
                    ConversionCandidate(
                        gost=row["gost"],
                        iso=row["iso"],
                        scope=row["scope"],
                        decision=row["decision"],
                        source=row["source"],
                        notes=row["notes"],
                    )
                )
    return tuple(matches)