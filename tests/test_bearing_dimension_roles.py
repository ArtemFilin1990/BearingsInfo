"""Regression for ГОСТ 11215 / 1217K+H217 and false 75 mm bearing bore."""
from decimal import Decimal as D
from src.bearing_dimension_roles import BearingGeometry, compare_geometry

SKF = "https://skf-us-cad-download.skf.com/item/self-aligning-ball/aligning-ball-bearings-with-tapered-bore-1/1217k"
IRBIS = "https://www.irbis.ua/catalog/product/11215-1217kh217-sh00004877"

def assembly():
    return BearingGeometry("11215 / 1217K+H217", "BEARING_WITH_ADAPTER",
                           D(85), D(150), D(28), D(75), "H217", SKF, IRBIS)

def test_bore_and_shaft_seat_are_not_same_diameter():
    a = assembly()
    assert a.evidence_problems() == ()
    assert (a.bearing_bore_d_mm, a.shaft_seat_d1_mm) == (D(85), D(75))
    assert a.ddb_for_single_bearing() is None

def test_false_75mm_bore_is_detected():
    bad = BearingGeometry("11215","BEARING_WITH_ADAPTER",D(75),D(150),D(28),D(75),"H217",SKF,IRBIS)
    assert "ADAPTER_ROLE_AMBIGUITY" in bad.evidence_problems()

def test_assembly_not_indexed_as_single_bearing():
    standalone = BearingGeometry("1217K","SINGLE_BEARING",D(85),D(150),D(28),None,None,SKF,None)
    assert "SINGLE_VS_ASSEMBLY" in compare_geometry(assembly(),standalone)
    assert standalone.ddb_for_single_bearing() == (D(85),D(150),D(28))

def test_assembly_component_sources_required():
    bad = BearingGeometry("11215","BEARING_WITH_ADAPTER",D(85),D(150),D(28),D(75),"H217",None,IRBIS)
    assert "MISSING_COMPONENT_PROVENANCE" in bad.evidence_problems()

def test_different_shaft_seat_not_equal_assembly():
    other = BearingGeometry("1217K+H???","BEARING_WITH_ADAPTER",D(85),D(150),D(28),D(80),"H217",SKF,IRBIS)
    assert "DIFFERENT:shaft_seat_d1_mm" in compare_geometry(assembly(),other)

def test_bearing_data_missing_blocks_diameter_comparison():
    other = BearingGeometry("unknown","SINGLE_BEARING",None,D(150),D(28),None,None,None,None)
    assert "UNKNOWN:bearing_bore_d_mm" in compare_geometry(assembly(),other)
