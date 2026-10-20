"""Regression cases from EVEREST supplier nomenclature and manufacturer conventions."""

from src.bearing_designation import BearingSpecification, assess_analogue, parse_designation


def test_iso_brand_seal_and_clearance() -> None:
    value = parse_designation("SKF 6205-2RS1/C3")
    assert (value.brand, value.prefix, value.body, value.suffix) == ("SKF", "", "6205", "-2RS1/C3")
    assert value.suffix_codes == ("2RS1", "C3")
    assert value.suffix_meanings == ("contact_seal_2", "clearance")
    assert value.status == "PARSED"


def test_gost_precision_prefix_not_discarded() -> None:
    value = parse_designation("6-180205")
    assert (value.prefix, value.body, value.suffix, value.full_code) == ("6-", "180205", "", "6-180205")


def test_nu_is_part_of_basic_designation() -> None:
    value = parse_designation("SKF NU 205 ECP/C3")
    assert (value.prefix, value.body, value.suffix) == ("", "NU205", " ECP/C3")
    assert value.suffix_codes == ("ECP", "C3")
    assert value.status == "PARSED"


def test_nsk_contact_and_noncontact_are_distinct() -> None:
    contact = parse_designation("6205DDU NSK")
    noncontact = parse_designation("NSK 6205VV")
    assert contact.suffix_meanings == ("contact_seal_2",)
    assert noncontact.suffix_meanings == ("noncontact_seal_2",)


def test_ntn_contact_and_noncontact_are_distinct() -> None:
    assert parse_designation("NTN 6205LLU").suffix_meanings == ("contact_seal_2",)
    assert parse_designation("NTN 6205LLB").suffix_meanings == ("noncontact_seal_2",)


def test_foreign_script_mixed_requires_review() -> None:
    value = parse_designation("22228 ССK/C3W33 SKF")
    assert value.status == "REVIEW"
    assert "mixed_latin_cyrillic" in value.issues


def test_unverified_gost_prefix_not_reinterpreted() -> None:
    value = parse_designation("70-180205")
    assert (value.prefix, value.body, value.status) == ("70-", "180205", "REVIEW")


def test_numerical_series_does_not_imply_prefix() -> None:
    value = parse_designation("180205")
    assert (value.prefix, value.body, value.suffix) == ("", "180205", "")


def test_unsupported_suffix_is_preserved_and_flagged() -> None:
    value = parse_designation("HK1312-B")
    assert (value.body, value.suffix, value.status) == ("HK1312", "-B", "REVIEW")


def _spec(code: str, *, seal: str | None = None, clearance: str | None = None) -> BearingSpecification:
    return BearingSpecification(code, "deep_groove_ball", 25, 52, 15, "B", seal, clearance, "P0", "steel", "cylindrical")


def test_different_seals_are_not_analogues() -> None:
    actual = assess_analogue(
        _spec("6205-2Z", seal="shield_2"), _spec("6205-2RS", seal="contact_seal_2"),
        documented_crossref=True, verified_source=True,
    )
    assert actual.status == "REJECTED"
    assert "mismatch:sealing" in actual.reasons


def test_rejected_example_cannot_be_promoted_by_dimensions() -> None:
    result = assess_analogue(
        _spec("6205"), _spec("6305"), negative_note=True,
    )
    assert result.status == "REJECTED"


def test_raw_cross_reference_is_only_candidate() -> None:
    result = assess_analogue(
        _spec("180205", seal="contact_seal_2"),
        _spec("6205-2RS", seal="contact_seal_2"),
        documented_crossref=True,
    )
    assert result.status == "DIMENSIONAL_CANDIDATE"


def test_verified_basic_pair_does_not_fill_unknown_suffixes() -> None:
    result = assess_analogue(
        _spec("180205", seal="contact_seal_2"), _spec("6205", seal=None),
        documented_crossref=True, verified_source=True,
    )
    assert result.status == "BASIC_MATCH"
    assert "unverified:sealing" in result.reasons


def test_complete_verified_specification_is_confirmed() -> None:
    result = assess_analogue(
        _spec("X", seal="contact_seal_2", clearance="C3"),
        _spec("Y", seal="contact_seal_2", clearance="C3"),
        documented_crossref=True, verified_source=True,
    )
    assert result.status == "CONFIRMED"


def test_conflicting_brand_is_reviewed() -> None:
    result = parse_designation("SKF 6205-2Z NSK")
    assert result.status == "REVIEW"
    assert "conflicting_brands" in result.issues


def test_lookup_gost_iso_uses_explicit_rows_only() -> None:
    from src.bearing_designation import lookup_gost_iso

    matches = lookup_gost_iso("180205")
    assert len(matches) == 1
    assert (matches[0].iso, matches[0].decision) == ("6205-2RS", "CANDIDATE")
    assert lookup_gost_iso("6-180205") == ()  # Accuracy prefix must not be dropped.
    assert lookup_gost_iso("99999999") == ()


def test_conflicting_11215_cannot_be_autoreplaced() -> None:
    from src.bearing_designation import lookup_gost_iso

    candidates = lookup_gost_iso("11215")
    assert {x.iso for x in candidates if x.decision == "CANDIDATE"} == {"1217K+H217"}
    assert {x.iso for x in candidates if x.decision == "REJECTED"} == {"1215K+H215"}


def test_product_label_is_separate_from_marking() -> None:
    code = parse_designation("Подшипник SKF 6205-2RS1/C3")
    assert (code.brand, code.body, code.suffix) == ("SKF", "6205", "-2RS1/C3")
    assert code.raw == "Подшипник SKF 6205-2RS1/C3"


def test_source_suffix_dictionary_does_not_invert_seal_contact() -> None:
    import csv
    from pathlib import Path

    path = Path("data/iso/suffixes.csv")
    with path.open(encoding="utf-8", newline="") as handle:
        rows = {(row["manufacturer"], row["code"]): row for row in csv.DictReader(handle)}
    assert "контактн" in rows[("NSK", "DDU")]["description"].lower()
    assert "бесконтактн" in rows[("NSK", "VV")]["description"].lower()
    assert "контактн" in rows[("NTN", "LLU")]["description"].lower()
    assert "бесконтактн" in rows[("NTN", "LLB")]["description"].lower()
    assert not rows[("NTN", "LLU")]["snr_equivalent"]