"""Regression coverage for manufacturer-verified suffix and prefix decoding."""
import pytest

from src.verified_designation_dictionary import VerifiedCodebook, assess_code_level_compatibility


def book():
    return VerifiedCodebook()


def test_registry_keeps_ina_distinct_from_fag():
    b = book()
    assert {"SKF", "NSK", "NTN", "FAG", "INA"} <= b.brands
    assert b.lookup("INA", "2RSR") is None


@pytest.mark.parametrize(
    "brand,contact,noncontact",
    [("NSK", "DDU", "VV"), ("NTN", "LLU", "LLB"), ("SKF", "2RSH", "2RZ")],
)
def test_contact_vs_noncontact(brand, contact, noncontact):
    b = book()
    left = b.lookup(brand, contact)
    right = b.lookup(brand, noncontact)
    assert left.contact_type == "contact"
    assert right.contact_type == "noncontact"
    assert assess_code_level_compatibility(left, right) == "DIFFERENT_TECHNICAL_FEATURE"


def test_nsk_light_contact_is_distinct():
    b = book()
    assert b.lookup("NSK", "DDW").contact_type == "light_contact"


def test_fag_historical_scope_explicit():
    c = book().lookup("FAG", "W203B")
    assert "архивная" in c.bearing_scope
    assert "1997" in c.source_locator


def test_longest_token_suffix_with_slash():
    result = book().decode_suffix("SKF", "-2RSH/C3")
    assert [x.code for x in result.codes] == ["2RSH", "C3"]
    assert result.status == "VERIFIED_CODE_SCOPE_REVIEW"


def test_concatenated_nsk_codes():
    result = book().decode_suffix("NSK", "DDUCM")
    assert [x.code for x in result.codes] == ["DDU", "CM"]
    assert result.status == "VERIFIED_CODE_SCOPE_REVIEW"


def test_unknown_segment_not_split_into_fake_valid_code():
    result = book().decode_suffix("NSK", "DDUXYZCM")
    assert result.status == "REVIEW_UNKNOWN_CODE"
    assert result.unknown_parts == ("XYZCM",)


def test_no_cross_brand_inference():
    assert book().decode_suffix(None, "DDU").status == "UNKNOWN_BRAND"
    assert book().decode_suffix("SKF", "DDU").status == "REVIEW_UNKNOWN_CODE"


def test_verified_oem_prefix_only():
    b = book()
    found, rest = b.match_prefix("NTN", "4T-30205")
    assert found.code == "4T-" and rest == "30205"
    found, rest = b.match_prefix("SKF", "4T-30205")
    assert found is None and rest == "4T-30205"


def test_structural_series_not_detachable_oem_prefix():
    b = book()
    assert b.lookup("SKF", "NU", "basic_family") is not None
    assert b.match_prefix("SKF", "NU205")[0] is None


def test_same_seal_category_never_confirms_analogue():
    b = book()
    result = assess_code_level_compatibility(b.lookup("NSK", "DDU"), b.lookup("NTN", "LLU"))
    assert result == "SAME_FEATURE_NOT_PROVEN_INTERCHANGEABLE"


def test_exactly_55_official_source_rows():
    b = book()
    assert len(b.codes) == 55
    assert all(c.source_url.startswith("https://") and c.bearing_scope for c in b.codes.values())
