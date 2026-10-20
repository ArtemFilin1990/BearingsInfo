"""Safety invariants for EVEREST инженерное ядро.

This is intentionally small and dependency-free (pytest only).
"""
from dataclasses import replace
from datetime import date, timedelta
from decimal import Decimal

import pytest

from src.engineering_core import (
    RADIAL_BALL_CRITICAL, AnalogueDecision, ApplicationContext,
    AttributeFact, BearingPassport, evaluate_autoreplace,
)

TODAY = date(2026, 10, 21)


def facts(*, clearance='CN', precision='TOL_PROFILE_001', standard_system='ISO', basis=None):
    vals = {
        'bearing_type':'DEEP_GROOVE_BALL', 'd_mm':Decimal('25'), 'D_mm':Decimal('52'),
        'width_mm':Decimal('15'), 'width_kind':'B', 'sealing':'CONTACT_BOTH_SIDES',
        'clearance':clearance, 'precision':precision, 'cage':'STEEL',
        'bore_type':'CYLINDRICAL', 'lubrication':'GREASE_STD', 'internal_design':'6000_SERIES',
    }
    return {
        k: AttributeFact(v, 'CATALOG_VERIFIED', 'SKF_CATALOG_2025', '2025',
                         comparison_basis_id=basis if k == 'precision' else None)
        for k, v in vals.items()
    }


def make(source='a', other='ISO', attr=None):
    return BearingPassport(source, f'RAW-{source}', 'SKF', other, '', '6205', '2RS', attr or facts())


def approval(a, b, status='CONFIRMED', **kwargs):
    return AnalogueDecision(
        decision_id='DEC-1', source_bearing_id=a.bearing_id, candidate_bearing_id=b.bearing_id,
        status=status, approved_by='engineer-18', approval_date=TODAY - timedelta(days=1),
        valid_until=TODAY + timedelta(days=30), source_document_id='ENG-REPORT-1',
        audit_event_id='AUDIT-1', justification='Reviewed catalogue drawings and all attributes',
        source_snapshot_digest=a.snapshot_digest(), candidate_snapshot_digest=b.snapshot_digest(),
        **kwargs,
    )


def evalpair(a, b, decision=None, *, scope=None, restrictions=frozenset(), today=TODAY):
    return evaluate_autoreplace(a, b, decision, ApplicationContext(today, scope, restrictions))


def test_required_critical_profile_has_12_attributes():
    assert len(RADIAL_BALL_CRITICAL) == 12


def test_no_decision_denied():
    a, b = make('a'), make('b')
    assert evalpair(a, b).reasons == ('NO_APPROVED_DECISION',)


def test_confirmed_complete_same_system_allowed():
    a, b = make('a'), make('b')
    decision = approval(a, b)
    assert evalpair(a, b, decision).allow_autoreplace


@pytest.mark.parametrize('status', ['BASIC', 'DIMENSIONAL', 'REJECTED'])
def test_candidate_statuses_not_approvals(status):
    a, b = make('a'), make('b')
    result = evalpair(a, b, approval(a, b, status))
    assert not result.allow_autoreplace
    assert 'DECISION_NOT_AUTHORIZED_FOR_AUTOREPLACE' in result.reasons


@pytest.mark.parametrize('origin', ['UNKNOWN', 'CONFLICT'])
def test_unknown_conflict_blocks_even_confirmed(origin):
    a, b = make('a'), make('b')
    b = replace(b, attributes={**b.attributes, 'clearance': AttributeFact(None, origin)})
    outcome = evalpair(a, b, approval(a, b))
    assert not outcome.allow_autoreplace
    assert any(origin in r for r in outcome.reasons)


def test_missing_critical_attribute_blocks():
    a = make('a')
    b = make('b', attr={k: v for k, v in facts().items() if k != 'cage'})
    assert 'cage:ATTRIBUTE_MISSING' in evalpair(a, b, approval(a, b)).reasons


def test_inferred_without_edition_and_confidence_blocks():
    a = make('a')
    b = make('b', attr={**facts(), 'clearance': AttributeFact('CN', 'STANDARD_DEFAULT', 'GOST3189', '2024')})
    result = evalpair(a, b, approval(a, b))
    assert not result.allow_autoreplace
    assert any('STANDARD_EDITION_MISSING' in x for x in result.reasons)
    assert any('INFERENCE_CONFIDENCE_MISSING' in x for x in result.reasons)


def test_source_version_is_required():
    a=make('a')
    b=make('b', attr={**facts(), 'sealing': AttributeFact('CONTACT_BOTH_SIDES', 'EXPLICIT', 'source', None)})
    assert any('SOURCE_VERSION_MISSING' in x for x in evalpair(a,b,approval(a,b)).reasons)


def test_two_discrepancies_from_gost_example_block():
    a = make('gost', 'GOST', attr=facts(clearance='CN', precision='GOST_CLASS_6'))
    b = make('skf', 'ISO', attr=facts(clearance='C3', precision='SKF_NORMAL'))
    d = approval(a, b, 'CONFIRMED')
    result = evalpair(a,b,d)
    assert not result.allow_autoreplace
    assert {'clearance','precision'} <= set(result.differences)
    assert 'CROSS_STANDARD_PRECISION_EQUIVALENCE_UNVERIFIED' in result.reasons


def test_cross_standard_equal_text_precision_still_requires_proof():
    a = make('gost','GOST')
    b = make('iso','ISO')
    result = evalpair(a,b,approval(a,b))
    assert not result.allow_autoreplace
    assert 'CROSS_STANDARD_PRECISION_EQUIVALENCE_UNVERIFIED' in result.reasons


def test_cross_standard_certified_common_tolerance_profile():
    a = make('gost', 'GOST', attr=facts(basis='TOL-COMP-98'))
    b = make('iso', 'ISO', attr=facts(basis='TOL-COMP-98'))
    assert evalpair(a,b,approval(a,b)).allow_autoreplace


def test_conditional_requires_scope_restrictions_and_approved_differences():
    a, b = make('a'), make('b', attr=facts(clearance='C3'))
    d = approval(a,b,'CONDITIONAL', approved_differences=frozenset({'clearance'}),
                 restrictions=frozenset({'MAX_TEMP_80C'}),scope_id='PUMP-7-2026')
    assert evalpair(a,b,d,scope='PUMP-7-2026',restrictions=frozenset({'MAX_TEMP_80C'})).allow_autoreplace
    assert not evalpair(a,b,d,scope='PUMP-8-2026',restrictions=frozenset({'MAX_TEMP_80C'})).allow_autoreplace
    assert not evalpair(a,b,d,scope='PUMP-7-2026').allow_autoreplace
    assert not evalpair(a,b,replace(d,scope_id=None),scope='PUMP-7-2026',restrictions=frozenset({'MAX_TEMP_80C'})).allow_autoreplace
    assert not evalpair(a,b,replace(d,approved_differences=frozenset()),scope='PUMP-7-2026',restrictions=frozenset({'MAX_TEMP_80C'})).allow_autoreplace


def test_conditional_without_restrictions_blocked():
    a,b=make('a'),make('b')
    d=approval(a,b,'CONDITIONAL',scope_id='SITE-1')
    assert 'CONDITIONAL_RESTRICTIONS_REQUIRED' in evalpair(a,b,d,scope='SITE-1').reasons


def test_expired_or_missing_audit_block():
    a,b=make('a'),make('b')
    d=approval(a,b)
    assert not evalpair(a,b,replace(d,valid_until=TODAY-timedelta(days=1))).allow_autoreplace
    assert not evalpair(a,b,replace(d,audit_event_id=None)).allow_autoreplace


def test_passport_change_invalidates_approval():
    a,b=make('a'),make('b')
    d=approval(a,b)
    modified = replace(a, attributes={**a.attributes, 'clearance': AttributeFact('C3','EXPLICIT','supplier','v2')})
    assert 'SOURCE_PASSPORT_SNAPSHOT_STALE' in evalpair(modified,b,d).reasons


def test_direction_not_symmetric():
    a,b=make('a'),make('b')
    d=approval(a,b)
    assert 'WRONG_DIRECTION_OR_BEARING_ID' in evalpair(b,a,d).reasons


def test_no_auto_if_lacking_authoritative_source_or_signature():
    a,b=make('a'),make('b')
    d=approval(a,b)
    assert not evalpair(a,b,replace(d,source_document_id=None)).allow_autoreplace
    assert not evalpair(a,b,replace(d,approved_by=None)).allow_autoreplace


def test_same_numeric_dimension_float_rejected():
    with pytest.raises(TypeError):
        make('a',attr={**facts(), 'd_mm':AttributeFact(25.0,'EXPLICIT','s','v1')}).snapshot_digest()
