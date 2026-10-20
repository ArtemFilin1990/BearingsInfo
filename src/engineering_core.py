"""EVEREST engineering-core v1. Pure deterministic, fail-closed evaluation.

This module does not query a catalogue or grant authorization. Callers must resolve
an APPROVED immutable decision and authenticated engineering application context.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any, Literal, Mapping

Origin = Literal['EXPLICIT', 'STANDARD_DEFAULT', 'CATALOG_VERIFIED', 'UNKNOWN', 'CONFLICT']
DecisionStatus = Literal['CONFIRMED', 'BASIC', 'DIMENSIONAL', 'CONDITIONAL', 'REJECTED']

# For type-specific bearings these must be adapted by a reviewed profile.
# width_mm is B for this profile; tapered/thrust bearings need T/C/H profile fields.
RADIAL_BALL_CRITICAL = frozenset({
    'bearing_type', 'd_mm', 'D_mm', 'width_mm', 'width_kind', 'sealing',
    'clearance', 'precision', 'cage', 'bore_type', 'lubrication',
    'internal_design',
})
ACCEPTABLE_ORIGINS = frozenset({'EXPLICIT', 'STANDARD_DEFAULT', 'CATALOG_VERIFIED'})


def _canonical(v: Any) -> str:
    """Trusted semantic value. Caller must normalize units and code semantics upstream."""
    if isinstance(v, Decimal):
        return format(v.normalize(), 'f')
    if isinstance(v, float):
        raise TypeError('Use Decimal or str; float dimensions risk comparison error')
    if isinstance(v, bool) or v is None:
        return str(v)
    return str(v)


@dataclass(frozen=True)
class AttributeFact:
    value: str | Decimal | None
    origin: Origin
    source_id: str | None = None
    source_version: str | None = None
    standard_edition_id: str | None = None
    confidence: Decimal | None = None
    conflict_details: str | None = None
    comparison_basis_id: str | None = None  # independently reviewed cross-standard property equivalence

    def evidence_problems(self, key: str) -> tuple[str, ...]:
        issues: list[str] = []
        if self.origin not in ACCEPTABLE_ORIGINS:
            issues.append(f'{key}:{self.origin}')
            return tuple(issues)
        if self.value is None or _canonical(self.value).strip() == '':
            issues.append(f'{key}:EMPTY_VALUE')
        if not self.source_id or not self.source_version:
            issues.append(f'{key}:SOURCE_VERSION_MISSING')
        if self.origin == 'STANDARD_DEFAULT' and not self.standard_edition_id:
            issues.append(f'{key}:STANDARD_EDITION_MISSING')
        if self.confidence is not None and not (Decimal('0') <= self.confidence <= Decimal('1')):
            issues.append(f'{key}:INVALID_CONFIDENCE')
        if self.origin == 'STANDARD_DEFAULT' and self.confidence is None:
            issues.append(f'{key}:INFERENCE_CONFIDENCE_MISSING')
        return tuple(issues)


@dataclass(frozen=True)
class BearingPassport:
    bearing_id: str
    raw_designation: str
    brand: str | None
    standard_system: str
    prefix: str
    basic_designation: str
    suffix: str
    attributes: Mapping[str, AttributeFact]
    attribute_profile: str = 'RADIAL_BALL_V1'

    def snapshot_digest(self) -> str:
        """Fingerprint both values and their evidence; evidence changes invalidate approvals."""
        facts = {key: {
            'value': _canonical(v.value), 'origin': v.origin,
            'source_id': v.source_id, 'source_version': v.source_version,
            'edition': v.standard_edition_id,
            'confidence': _canonical(v.confidence),
            'conflict_details': v.conflict_details,
            'comparison_basis_id': v.comparison_basis_id,
        } for key, v in sorted(self.attributes.items())}
        payload = {
            'bearing_id': self.bearing_id, 'raw': self.raw_designation,
            'brand': self.brand, 'system': self.standard_system,
            'prefix': self.prefix, 'basic': self.basic_designation,
            'suffix': self.suffix, 'profile': self.attribute_profile, 'facts': facts,
        }
        return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf-8')).hexdigest()


@dataclass(frozen=True)
class AnalogueDecision:
    decision_id: str
    source_bearing_id: str
    candidate_bearing_id: str
    status: DecisionStatus
    approved_by: str | None
    approval_date: date | None
    valid_until: date | None
    source_document_id: str | None
    audit_event_id: str | None
    justification: str | None
    scope_id: str | None = None
    approved_differences: frozenset[str] = frozenset()
    restrictions: frozenset[str] = frozenset()
    source_snapshot_digest: str | None = None
    candidate_snapshot_digest: str | None = None
    revoked: bool = False


@dataclass(frozen=True)
class ApplicationContext:
    # scope_id / restrictions must be resolved by an authenticated engineering context,
    # not passed untrusted from a public URL or product query.
    as_of: date
    scope_id: str | None
    verified_restrictions: frozenset[str] = frozenset()


@dataclass(frozen=True)
class GateResult:
    allow_autoreplace: bool
    reasons: tuple[str, ...]
    differences: tuple[str, ...]
    decision_id: str | None


def evaluate_autoreplace(
    source: BearingPassport,
    candidate: BearingPassport,
    decision: AnalogueDecision | None,
    application: ApplicationContext,
    required: frozenset[str] = RADIAL_BALL_CRITICAL,
) -> GateResult:
    """Zero positive defaults. Only a current, documented, audited approval can pass.

    Direction matters: source->candidate does not imply candidate->source.
    A conditional exception applies only within the exact approved scope.
    """
    issues: list[str] = []
    differences: list[str] = []
    if not decision:
        return GateResult(False, ('NO_APPROVED_DECISION',), (), None)
    if decision.source_bearing_id != source.bearing_id or decision.candidate_bearing_id != candidate.bearing_id:
        issues.append('WRONG_DIRECTION_OR_BEARING_ID')
    if source.bearing_id == candidate.bearing_id:
        issues.append('SAME_BEARING_NOT_ANALOGUE')
    if source.attribute_profile != candidate.attribute_profile or source.attribute_profile != 'RADIAL_BALL_V1':
        issues.append('UNSUPPORTED_OR_DIFFERENT_ATTRIBUTE_PROFILES')
    if decision.status not in {'CONFIRMED', 'CONDITIONAL'}:
        issues.append('DECISION_NOT_AUTHORIZED_FOR_AUTOREPLACE')
    if decision.revoked:
        issues.append('DECISION_REVOKED')
    if not decision.approved_by or not decision.approval_date:
        issues.append('ENGINEER_APPROVAL_MISSING')
    if not decision.source_document_id or not decision.audit_event_id or not decision.justification:
        issues.append('EVIDENCE_OR_AUDIT_MISSING')
    if decision.valid_until is None or decision.valid_until < application.as_of:
        issues.append('DECISION_EXPIRED_OR_NO_EXPIRY')
    if decision.approval_date is not None and decision.approval_date > application.as_of:
        issues.append('APPROVAL_IN_FUTURE')
    if decision.approval_date and decision.valid_until and decision.valid_until < decision.approval_date:
        issues.append('INVALID_APPROVAL_INTERVAL')
    if decision.scope_id and decision.scope_id != application.scope_id:
        issues.append('SCOPE_MISMATCH')
    if decision.status == 'CONDITIONAL' and not decision.scope_id:
        issues.append('CONDITIONAL_SCOPE_REQUIRED')
    if not decision.source_snapshot_digest or decision.source_snapshot_digest != source.snapshot_digest():
        issues.append('SOURCE_PASSPORT_SNAPSHOT_STALE')
    if not decision.candidate_snapshot_digest or decision.candidate_snapshot_digest != candidate.snapshot_digest():
        issues.append('CANDIDATE_PASSPORT_SNAPSHOT_STALE')
    if not RADIAL_BALL_CRITICAL.issubset(required):
        issues.append('REQUIRED_PROFILE_DOWNGRADED')
    for key in sorted(required):
        left = source.attributes.get(key)
        right = candidate.attributes.get(key)
        if left is None or right is None:
            issues.append(f'{key}:ATTRIBUTE_MISSING')
            continue
        issues.extend('SOURCE_' + p for p in left.evidence_problems(key))
        issues.extend('CANDIDATE_' + p for p in right.evidence_problems(key))
        if left.value is not None and right.value is not None and _canonical(left.value) != _canonical(right.value):
            differences.append(key)
    # Standards-crosswalk IDT/MOD/NEQ does NOT establish product tolerance equality.
    # Equal-looking class codes across standards are blocked without a separately
    # reviewed common tolerance-profile mapping bound to both attribute records.
    if source.standard_system != candidate.standard_system:
        left_precision = source.attributes.get('precision')
        right_precision = candidate.attributes.get('precision')
        if (left_precision is None or right_precision is None or
            not left_precision.comparison_basis_id or
            left_precision.comparison_basis_id != right_precision.comparison_basis_id):
            issues.append('CROSS_STANDARD_PRECISION_EQUIVALENCE_UNVERIFIED')
    if decision.status == 'CONFIRMED' and differences:
        issues.append('CONFIRMED_BUT_CRITICAL_DIFFERENCES')
    if decision.status == 'CONDITIONAL':
        if not decision.restrictions:
            issues.append('CONDITIONAL_RESTRICTIONS_REQUIRED')
        unauthorized = sorted(set(differences) - set(decision.approved_differences))
        if unauthorized:
            issues.extend(f'UNAPPROVED_DIFFERENCE:{key}' for key in unauthorized)
        if not decision.restrictions.issubset(application.verified_restrictions):
            issues.append('RESTRICTIONS_NOT_VERIFIED')
    if not issues:
        return GateResult(True, ('AUTOREPLACE_APPROVED_FOR_CONTEXT',), tuple(differences), decision.decision_id)
    return GateResult(False, tuple(dict.fromkeys(issues)), tuple(differences), decision.decision_id)
