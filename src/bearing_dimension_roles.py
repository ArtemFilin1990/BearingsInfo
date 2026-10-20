"""Explicit dimensional roles for bearings and mounted adapter assemblies.

Does not infer sizes or substitution rights from a designation string.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Literal

AssemblyKind = Literal["SINGLE_BEARING", "BEARING_WITH_ADAPTER"]

@dataclass(frozen=True)
class BearingGeometry:
    designation: str
    assembly_kind: AssemblyKind
    bearing_bore_d_mm: Decimal | None
    outside_d_mm: Decimal | None
    bearing_width_b_mm: Decimal | None
    shaft_seat_d1_mm: Decimal | None
    sleeve_designation: str | None
    bearing_source_url: str | None
    sleeve_source_url: str | None

    def evidence_problems(self) -> tuple[str, ...]:
        issues: list[str] = []
        if any(value is not None and value <= 0 for value in
               (self.bearing_bore_d_mm, self.outside_d_mm, self.bearing_width_b_mm,
                self.shaft_seat_d1_mm)):
            issues.append("NONPOSITIVE_DIMENSIONS")
        if self.bearing_bore_d_mm is not None and self.outside_d_mm is not None and self.bearing_bore_d_mm >= self.outside_d_mm:
            issues.append("INVALID_BEARING_BORE_GEOMETRY")
        if self.assembly_kind == "BEARING_WITH_ADAPTER":
            if not self.sleeve_designation or self.shaft_seat_d1_mm is None:
                issues.append("ADAPTER_OR_SHAFT_SEAT_MISSING")
            if self.bearing_bore_d_mm == self.shaft_seat_d1_mm:
                issues.append("ADAPTER_ROLE_AMBIGUITY")
            if not self.bearing_source_url or not self.sleeve_source_url:
                issues.append("MISSING_COMPONENT_PROVENANCE")
        elif self.sleeve_designation is not None:
            issues.append("SLEEVE_WITHOUT_ASSEMBLY")
        return tuple(issues)

    def ddb_for_single_bearing(self) -> tuple[Decimal, Decimal, Decimal] | None:
        """No unqualified d/D/B entry for an adapter-bearing set."""
        if self.assembly_kind != "SINGLE_BEARING" or self.evidence_problems():
            return None
        if any(x is None for x in (self.bearing_bore_d_mm, self.outside_d_mm, self.bearing_width_b_mm)):
            return None
        return self.bearing_bore_d_mm, self.outside_d_mm, self.bearing_width_b_mm

def compare_geometry(left: BearingGeometry, right: BearingGeometry) -> tuple[str, ...]:
    """Identify dimensional incompatibility, never grant analogue status."""
    issues = list(left.evidence_problems()) + list(right.evidence_problems())
    if left.assembly_kind != right.assembly_kind:
        issues.append("SINGLE_VS_ASSEMBLY")
    for field in ("bearing_bore_d_mm", "outside_d_mm", "bearing_width_b_mm"):
        a, b = getattr(left, field), getattr(right, field)
        if a is None or b is None:
            issues.append(f"UNKNOWN:{field}")
        elif a != b:
            issues.append(f"DIFFERENT:{field}")
    if left.assembly_kind == right.assembly_kind == "BEARING_WITH_ADAPTER":
        if left.shaft_seat_d1_mm is None or right.shaft_seat_d1_mm is None:
            issues.append("UNKNOWN:shaft_seat_d1_mm")
        elif left.shaft_seat_d1_mm != right.shaft_seat_d1_mm:
            issues.append("DIFFERENT:shaft_seat_d1_mm")
        if left.sleeve_designation != right.sleeve_designation:
            issues.append("DIFFERENT:adapter_sleeve")
    return tuple(dict.fromkeys(issues))
