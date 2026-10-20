from datetime import date

from src.engineering_core import ApplicationContext, AttributeFact, BearingPassport
from src.oem_evidence_bridge import inspect_candidate


def passport(ident, brand, code):
    return BearingPassport(
        ident, code, brand, "ISO", "", "6205", code.split("6205")[-1],
        {"clearance": AttributeFact(None, "UNKNOWN")},
    )


def test_official_code_does_not_grant_equivalence():
    source = passport("a", "NSK", "6205DDU")
    candidate = passport("b", "SKF", "6205-2RSH/C3")
    result = inspect_candidate(source, candidate, None, ApplicationContext(date(2026, 10, 21), None))
    assert [o.code for o in result.observations] == ["2RSH", "C3"]
    assert not result.gate.allow_autoreplace
    assert result.gate.reasons == ("NO_APPROVED_DECISION",)
    assert all(o.status == "OFFICIAL_CODE_ONLY" for o in result.observations)
