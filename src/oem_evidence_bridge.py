"""Manufacturer code meaning is not per-SKU evidence or an analogue approval."""
from __future__ import annotations

from dataclasses import dataclass

from src.engineering_core import (
    ApplicationContext,
    AnalogueDecision,
    BearingPassport,
    GateResult,
    evaluate_autoreplace,
)
from src.verified_designation_dictionary import VerifiedCodebook


@dataclass(frozen=True)
class CodeObservation:
    code: str
    brand: str
    feature: str
    contact_type: str
    source_url: str
    status: str = "OFFICIAL_CODE_ONLY"


@dataclass(frozen=True)
class InspectionResult:
    observations: tuple[CodeObservation, ...]
    unknown_suffix_parts: tuple[str, ...]
    code_parse_status: str
    gate: GateResult


def inspect_candidate(
    source: BearingPassport,
    candidate: BearingPassport,
    decision: AnalogueDecision | None,
    context: ApplicationContext,
    codebook: VerifiedCodebook | None = None,
) -> InspectionResult:
    """No mutation of source attributes, provenance or engineering approval."""
    book = codebook or VerifiedCodebook()
    decoded = book.decode_suffix(candidate.brand, candidate.suffix)
    observations = tuple(
        CodeObservation(c.code, c.manufacturer, c.feature, c.contact_type, c.source_url)
        for c in decoded.codes
    )
    gate = evaluate_autoreplace(source, candidate, decision, context)
    return InspectionResult(observations, decoded.unknown_parts, decoded.status, gate)
