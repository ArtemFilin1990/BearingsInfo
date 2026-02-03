# Internal Clearance and Preload

## Purpose

This document provides comprehensive information on bearing internal clearance, clearance groups, preload concepts, calculation of operating clearance, and proper selection of clearance or preload for various applications. Understanding clearance and preload is essential for optimal bearing performance, life, and precision.

---

## 1. Internal Clearance Fundamentals

### 1.1 Definition

**Internal Clearance (Внутренний зазор):**

The total distance through which one bearing ring can be moved relative to the other ring in the radial or axial direction when the bearing is unmounted and no external load is applied.

**Key characteristics:**
- Measured before installation (free state)
- Changes during mounting (fits create interference)
- Changes during operation (thermal expansion)
- Critical parameter affecting: load distribution, friction, life, noise

### 1.2 Types of Clearance

**1. Radial Internal Clearance:**

The maximum distance one ring can be displaced radially relative to the other.

**Measurement method:**
- Fix one ring
- Displace the other ring from one extreme radial position to the opposite
- Measure total displacement

**Applies to:**
- Radial bearings (deep groove, cylindrical roller, spherical roller)
- Radial-angular contact bearings

**2. Axial Internal Clearance:**

The maximum distance one ring can be displaced axially relative to the other.

**Applies to:**
- Angular contact ball bearings
- Tapered roller bearings (non-separable assemblies)
- Thrust bearings

**Relationship to radial clearance (angular contact bearings):**

```
Axial clearance = Radial clearance / sin α
```

Where α = contact angle

### 1.3 Clearance Evolution

**Three stages of clearance:**

**1. Initial Clearance (Начальный зазор):**
- As manufactured, before mounting
- Stamped on bearing (clearance group marking)
- Reference condition for specifications

**2. Mounted Clearance (Посадочный зазор):**
- After mounting on shaft and in housing
- Affected by interference fits
- Typically reduced from initial clearance

**3. Operating Clearance (Рабочий зазор):**
- During operation at steady-state temperature
- Affected by differential thermal expansion
- Final clearance that determines bearing behavior

**Critical relationship:**

```
Initial Clearance > Mounted Clearance ≥ Operating Clearance
```

**Objective:**

Select initial clearance so that operating clearance is optimal (slightly positive for most applications).

---

## 2. Clearance Groups and Standards

### 2.1 ГОСТ Clearance Groups

**ГОСТ 24810-2013** — Подшипники качения. Внутренние зазоры

Different bearing types have different clearance group designations.

### 2.2 Clearance Groups for Radial Ball Bearings

**Cylindrical bore (single row deep groove):**

| ГОСТ Group | ISO Equivalent | Designation |
|-----------|----------------|-------------|
| 6 | C2 | Reduced |
| **Нормальная** | **CN** | **Normal** (not marked) |
| 7 | C3 | Increased |
| 8 | C4 | Large |
| 9 | C5 | Very large |

**Conical bore (deep groove with tapered bore):**

| ГОСТ Group | Designation |
|-----------|-------------|
| 2 | Reduced |
| **Нормальная** | **Normal** |
| 3 | Increased |
| 4 | Large |

### 2.3 Clearance Groups for Roller Bearings

**Cylindrical roller bearings (interchangeable NJ, NU):**

| ГОСТ Group | ISO Equivalent |
|-----------|----------------|
| 1 | C1 |
| 6 | C2 |
| 2 | CN |
| 3 | C3 |
| 4 | C4 |

**Cylindrical roller bearings (non-interchangeable):**

| ГОСТ Group | ISO Equivalent |
|-----------|----------------|
| 0 | — |
| 5 | C2 |
| **Нормальная** | **CN** |
| 7 | C3 |
| 8 | C4 |
| 9 | C5 |

**Spherical roller bearings (cylindrical bore):**

| ГОСТ Group | ISO Equivalent |
|-----------|----------------|
| 1 | C1 |
| 2 | C2 |
| **Нормальная** | **CN** |
| 3 | C3 |
| 4 | C4 |
| 5 | C5 |

**Tapered roller bearings:**

Groups depend on series and design. Typically: 2, 1, 3, 4 or similar.

### 2.4 Radial Clearance Values - Deep Groove Ball Bearings

**Example: Bearing series 62, 63 (ISO CN group):**

| Bore d [mm] | Radial Clearance CN [μm] |
|------------|-------------------------|
| | Min | Max |
| 2.5 - 10 | 0 | 13 |
| 10 - 18 | 0 | 13 |
| 18 - 24 | 0 | 15 |
| 24 - 30 | 1 | 18 |
| 30 - 40 | 1 | 20 |
| 40 - 50 | 1 | 23 |
| 50 - 65 | 1 | 28 |
| 65 - 80 | 1 | 30 |
| 80 - 100 | 1 | 35 |
| 100 - 120 | 2 | 40 |

**Clearance increase for C3, C4, C5 groups:**

Approximately:
- C3 ≈ CN + 8-15 μm
- C4 ≈ CN + 15-25 μm
- C5 ≈ CN + 25-40 μm

(Exact values from ГОСТ 24810 or manufacturer catalog)

### 2.5 Radial Clearance Values - Cylindrical Roller Bearings

**Typical values (CN group, non-interchangeable):**

| Bore d [mm] | Radial Clearance CN [μm] |
|------------|-------------------------|
| | Min | Max |
| 18 - 24 | 20 | 45 |
| 24 - 30 | 20 | 50 |
| 30 - 40 | 25 | 55 |
| 40 - 50 | 30 | 60 |
| 50 - 65 | 30 | 65 |
| 65 - 80 | 40 | 75 |
| 80 - 100 | 40 | 80 |
| 100 - 120 | 45 | 90 |

**Note:** Roller bearings have larger clearances than ball bearings.

### 2.6 Clearance Marking on Bearing

**Position in designation:**

Clearance group is indicated **before** tolerance class in bearing designation.

**Examples:**

- **75-313** → Group 7, Class 5, Bearing 313
- **8-180213** → Group 8, Bearing 180213
- **0-32210** → Group 0, Bearing 32210
- **313** → Normal clearance (not marked), Bearing 313

**Special designations:**

- **Н** (H) → Non-standardized (special clearance)
- **М** (M) → Normal clearance with torque requirements
- **НТ** → Tight selection (narrow clearance tolerance)

---

## 3. Effects of Mounting on Clearance

### 3.1 Interference Fit Effects

**Tight fit (interference) causes:**

1. **Inner ring:** Expands radially outward
2. **Outer ring:** Contracts radially inward
3. **Net effect:** Reduction of internal clearance

**Clearance reduction formula:**

**Inner ring interference (shaft fit):**

```
Δs_inner ≈ d · Δd / dm
```

Where:
- d = bore diameter [mm]
- Δd = effective interference [μm]
- dm = bearing mean diameter = (d + D) / 2

**Outer ring interference (housing fit):**

```
Δs_outer ≈ D · ΔD / dm
```

Where:
- D = outer diameter [mm]
- ΔD = effective interference [μm]

**Total clearance reduction:**

```
ΔCr = Δs_inner + Δs_outer
```

**Mounted clearance:**

```
Cr_mounted = Cr_initial - ΔCr
```

### 3.2 Practical Clearance Reduction Values

**Typical values for steel rings, solid steel shaft, split housing:**

**Inner ring interference (common fits):**

| Fit (ISO) | Interference [μm] | Clearance reduction [μm] |
|-----------|------------------|-------------------------|
| **g6** | Slight clearance | 0 (or small increase) |
| **h5, h6** | Transition | 0 - 5 |
| **j5, j6** | Transition | 2 - 8 |
| **k5, k6** | Light interference | 5 - 15 |
| **m5, m6** | Interference | 10 - 25 |
| **n6** | Tight interference | 20 - 40 |
| **p6** | Very tight | 30 - 60 |

**Outer ring fit (housing):**

Typically **H7, H8** (clearance fit) → minimal effect on clearance (0-5 μm reduction)

If tight fit in housing (rare):
- **M7, N7** → 10-30 μm reduction

### 3.3 Example Calculation - Mounting Effect

**Given:**
- Bearing: 6308 (d = 40 mm, D = 90 mm, B = 23 mm)
- Initial clearance: Cr = 18 μm (CN group, mid-range)
- Shaft fit: k6 (interference ≈ 10 μm effective)
- Housing fit: H7 (minimal effect, assume 2 μm)

**Solution:**

```
dm = (40 + 90) / 2 = 65 mm

Δs_inner = 40 · 10 / 65 ≈ 6 μm
Δs_outer ≈ 2 μm

ΔCr = 6 + 2 = 8 μm

Cr_mounted = 18 - 8 = 10 μm
```

**Result:** Mounted clearance ≈ 10 μm (still positive).

---

## 4. Effects of Temperature on Clearance

### 4.1 Thermal Expansion Basics

**Different thermal expansion:**

During operation:
- **Inner ring:** Heated by shaft (higher temperature)
- **Outer ring:** Cooled by housing (lower temperature)
- **Temperature difference:** ΔT = T_inner - T_outer

**Typical temperature difference:**

- Normal operation: ΔT = 5 - 10°C
- High-speed operation: ΔT = 10 - 20°C
- Poor heat dissipation: ΔT = 15 - 30°C

### 4.2 Thermal Clearance Change

**Inner ring expands more → Clearance decreases**

**Formula:**

```
ΔCr_thermal = α · dm · ΔT
```

Where:
- α = thermal expansion coefficient [1/K]
  - Steel: α ≈ 11.5 × 10⁻⁶ /K
  - Aluminum housing: α ≈ 23 × 10⁻⁶ /K
- dm = mean diameter [mm]
- ΔT = inner ring temp - outer ring temp [K or °C]

**Note:** If housing is aluminum, outer ring expands more → partially compensates.

### 4.3 Example - Thermal Effect

**Given:**
- Bearing 6308: dm = 65 mm
- Mounted clearance: Cr_mounted = 10 μm
- Operating temperature difference: ΔT = 15°C
- Steel shaft and steel housing

**Solution:**

```
ΔCr_thermal = 11.5 × 10⁻⁶ × 65 × 15
ΔCr_thermal = 11.2 μm

Cr_operating = Cr_mounted - ΔCr_thermal
Cr_operating = 10 - 11.2 = -1.2 μm
```

**Result:** Operating clearance is **slightly negative** (light preload).

**Interpretation:** 
- For precision applications: May be acceptable or even desirable
- For high-speed: Risk of overheating → use larger initial clearance (C3)

---

## 5. Operating Clearance Calculation

### 5.1 Complete Calculation Procedure

**Step 1: Determine initial clearance** (from catalog or ГОСТ 24810)

**Step 2: Calculate clearance reduction due to fits**

```
ΔCr_fit = Δs_inner + Δs_outer
```

**Step 3: Calculate mounted clearance**

```
Cr_mounted = Cr_initial - ΔCr_fit
```

**Step 4: Calculate thermal clearance change**

```
ΔCr_thermal = α · dm · ΔT
```

**Step 5: Calculate operating clearance**

```
Cr_operating = Cr_mounted - ΔCr_thermal
```

### 5.2 Desired Operating Clearance

**Optimal operating clearance depends on application:**

| Application Type | Recommended Cr_operating |
|-----------------|------------------------|
| **General machinery, normal precision** | +5 to +15 μm (slight positive) |
| **High precision, minimal runout** | 0 to +5 μm (very small or zero) |
| **High speed, light load** | +10 to +25 μm (positive) |
| **Heavy load, shock** | +15 to +30 μm (larger positive) |
| **Precision spindles, preloaded** | -5 to -20 μm (negative = preload) |

**Guideline:**

- **Positive clearance:** Normal for most applications
- **Zero clearance:** High precision, careful thermal management
- **Negative clearance (preload):** Precision, rigidity, eliminates play

### 5.3 Selection Strategy

**If operating clearance calculation shows:**

**Cr_operating too small (< 5 μm) or negative:**
- Select larger initial clearance (C3, C4)
- Reduce interference fits
- Improve cooling (reduce ΔT)

**Cr_operating too large (> 30 μm for precision):**
- Select smaller initial clearance (C2)
- Increase interference fits (carefully)
- Accept for non-precision applications

### 5.4 Comprehensive Example

**Application:** Electric motor bearing

**Specifications:**
- Bearing: 6210 (d = 50 mm, D = 90 mm)
- Speed: 3000 rpm
- Load: Moderate
- Shaft fit: k6
- Housing fit: H7
- Expected temperature difference: ΔT = 12°C

**Step 1: Initial clearance**

From catalog, bearing 6210, normal clearance (CN):
- Cr_initial = 12 μm (mid-range for d = 50 mm)

**Step 2: Fit effects**

Shaft fit k6 for d = 50 mm:
- Effective interference ≈ 12 μm

```
dm = (50 + 90) / 2 = 70 mm

Δs_inner = 50 · 12 / 70 ≈ 8.6 μm
Δs_outer ≈ 2 μm (H7, minimal)

ΔCr_fit = 8.6 + 2 = 10.6 μm
```

**Step 3: Mounted clearance**

```
Cr_mounted = 12 - 10.6 = 1.4 μm
```

**Step 4: Thermal effect**

```
ΔCr_thermal = 11.5 × 10⁻⁶ × 70 × 12
ΔCr_thermal ≈ 9.7 μm
```

**Step 5: Operating clearance**

```
Cr_operating = 1.4 - 9.7 = -8.3 μm
```

**Analysis:**

Operating clearance is **negative** (preload ≈ 8 μm).

**Consequences:**
- Increased friction
- Higher operating temperature
- Possible overheating at 3000 rpm

**Solution:**

Use **Group 7 (C3)** clearance:
- Cr_initial ≈ 20 μm (C3 group, mid-range)

**Recalculation:**

```
Cr_mounted = 20 - 10.6 = 9.4 μm
Cr_operating = 9.4 - 9.7 = -0.3 μm
```

Still slightly negative, but acceptable for normal electric motor.

**Alternative:**

Use **Group 8 (C4)** for higher speed or temperature:
- Cr_initial ≈ 30 μm

```
Cr_mounted = 30 - 10.6 = 19.4 μm
Cr_operating = 19.4 - 9.7 = 9.7 μm
```

Positive clearance → suitable for higher speed.

---

## 6. Preload Fundamentals

### 6.1 Preload Definition

**Preload (Предварительный натяг):**

An intentionally applied load that eliminates internal clearance, creating an interference condition where rolling elements are always under load.

**Achieved by:**
- Axial force on bearing rings
- Thermal expansion (controlled fit)
- Spring pressure
- Dimensional mismatch (paired bearings)

**Effect:**
- Internal clearance → **Zero or negative** (interference)
- All rolling elements carry load simultaneously
- No free play in bearing

### 6.2 Purpose of Preload

**Benefits:**

1. **Increased stiffness:** Eliminates clearance → rigid system
2. **Improved accuracy:** No play → better precision
3. **Reduced vibration:** All rolling elements engaged → smoother
4. **Controlled load distribution:** Optimized contact conditions
5. **Prevention of skidding:** Ensures proper rolling at high speed

**Applications requiring preload:**

- Machine tool spindles (precision, rigidity)
- High-precision instruments
- High-speed applications (prevents skidding)
- Angular contact bearing arrangements
- Tapered roller bearing sets
- Applications with moment loads

### 6.3 Disadvantages of Preload

**Drawbacks:**

1. **Increased friction:** More heat generation
2. **Reduced life:** Higher contact stress
3. **Thermal sensitivity:** Must manage temperature rise
4. **More complex mounting:** Requires precision
5. **Higher cost:** Special bearings, precision assembly

**When NOT to use preload:**

- Heavy radial loads (normal clearance better)
- High-temperature applications (thermal expansion issues)
- Low-precision machinery
- Cost-sensitive applications

---

## 7. Preload Methods

### 7.1 Position Preload (Rigid Preload)

**Principle:**

Axial position of bearing rings is fixed. Preload is determined by dimensional interference or spacer length.

**Implementation:**

1. **Grinding of spacers:** Inner or outer ring spacers ground to precise length
2. **Shim adjustment:** Add/remove shims to set preload
3. **Locknut adjustment:** Tighten to specific torque or axial displacement

**Characteristics:**

- Preload is **constant** at assembly
- Changes with temperature (thermal expansion)
- Can increase significantly if temperature rises
- Suitable for stable thermal conditions

**Advantages:**
- High stiffness
- Precise control (if done correctly)

**Disadvantages:**
- Sensitive to temperature variation
- Risk of overload if thermal expansion not considered
- Requires precision assembly

### 7.2 Spring Preload (Elastic Preload)

**Principle:**

Preload applied by spring (disc springs, coil springs, wave washers).

**Characteristics:**

- Preload is **approximately constant** regardless of thermal expansion
- Spring deflects to accommodate length changes
- Lower stiffness than position preload

**Advantages:**
- Tolerant to temperature variation
- Simpler assembly (less critical dimensions)
- Protects against overload

**Disadvantages:**
- Lower stiffness (spring compliance)
- More complex design (spring, retainer needed)
- Potential for spring fatigue

**Applications:**
- Variable temperature environments
- Less critical precision (vs. position preload)
- Automotive, appliances

### 7.3 Preload Magnitude

**Light preload:**
- Axial load: 0.5 - 2% of C₀
- Applications: General machinery, moderate precision
- Friction increase: Minimal

**Medium preload:**
- Axial load: 2 - 5% of C₀
- Applications: Machine tools, precision equipment
- Friction increase: Moderate

**Heavy preload:**
- Axial load: 5 - 10% of C₀
- Applications: High rigidity spindles, aerospace
- Friction increase: Significant

**Manufacturer specifications:**

Bearing catalogs often specify preload in classes:
- **Light (L):** Low preload
- **Medium (M):** Standard preload
- **Heavy (H):** High preload

---

## 8. Preload for Angular Contact Bearings

### 8.1 Bearing Arrangements

**Duplex bearing sets:**

Pre-matched pairs or triplets, ground for specific preload.

**Back-to-back (DB, O-arrangement):**

```
O ← →
```

- High moment rigidity
- Pressure centers widely spaced
- Most common for high precision

**Face-to-face (DF, X-arrangement):**

```
X → ←
```

- Lower moment rigidity than DB
- Pressure centers close together
- Less common

**Tandem (DT, II-arrangement):**

```
II ↑ ↑
```

- Load capacity doubled (same direction)
- No moment rigidity improvement
- Used for high axial loads

### 8.2 Preload Specification for Angular Contact Bearings

**Universal matched bearing sets (suffix):**

- **DB:** Back-to-back, universal
- **DF:** Face-to-face, universal
- **DT:** Tandem, universal

**Preload classes (SKF system, example):**

- **Suffix A:** Light preload
- **Suffix B:** Medium preload
- **Suffix C:** Heavy preload

**Example designation:**

- **7208 BECBP:** Angular contact, back-to-back (B), medium preload (C)

### 8.3 Preload Adjustment by Spacer Grinding

**Procedure:**

1. Mount bearings back-to-back with initial spacers
2. Measure axial clearance or play
3. Calculate required spacer reduction
4. Grind spacers to precise length
5. Reassemble with target preload

**Formula:**

```
Δs = (Clearance + Desired_preload) / 2
```

Where Δs = amount to remove from spacers (each side)

**Example:**

- Initial axial clearance: 20 μm
- Desired preload (equivalent axial displacement): 10 μm

```
Δs = (20 + 10) / 2 = 15 μm per spacer
```

Remove 15 μm from each spacer (inner or outer ring spacer).

---

## 9. Preload for Tapered Roller Bearings

### 9.1 Arrangement and Adjustment

**Tapered roller bearings always used in pairs:**

- **Direct mounting (face-to-face):** Common
- **Indirect mounting (back-to-back):** Less common

**Adjustment methods:**

1. **Locknut and washer:** Tighten to specific torque or end play
2. **Shim adjustment:** Add/remove shims
3. **Threaded adjustment:** Precision thread and locknut

### 9.2 End Play vs Preload

**End play:** Small positive axial clearance (older practice)

**Modern practice:** Light preload preferred

**Setting:**

1. Tighten locknut until zero end play (turn bearing by hand, no play)
2. Back off slightly for end play, OR
3. Tighten further for preload (specific torque or angle)

**Typical automotive wheel bearing:**

- Tighten to 50 Nm while rotating
- Back off 1/4 turn
- Retighten to 5-10 Nm
- Install lock (cotter pin, lock washer)

**Precision applications:**

- Measure end play with dial indicator
- Adjust to 5-10 μm end play, or
- Set preload equivalent to 1-2% C₀

### 9.3 Preload Verification

**Measure torque:**

Bearing turning torque increases with preload.

**Dial indicator:**

Axial displacement measurement:
- Positive displacement = end play
- No displacement = zero clearance
- Resistance to displacement = preload

**Temperature monitoring:**

After operation:
- Normal temperature → correct preload
- Overheating → excessive preload

---

## 10. When to Use Clearance vs Preload

### 10.1 Clearance Applications

**Use increased clearance (C3, C4, C5) when:**

1. **Heavy loads** requiring tight shaft fit
2. **High temperature** operation (> 100°C)
3. **Inner ring hotter** than outer ring (typical)
4. **Loose housing fit** (outer ring not constrained)
5. **Thermal expansion** from shaft heat
6. **Misalignment** expected (spherical bearings)
7. **Vibration and shock** loads

**Examples:**
- Electric motors (continuous, ΔT ≈ 10-15°C)
- Pumps (high temperature fluids)
- Gearboxes (heavy load, tight fits)
- Conveyors (robust, not precision)

### 10.2 Normal Clearance Applications

**Use standard clearance (CN) when:**

1. **Normal operating conditions**
2. **Moderate speed and load**
3. **Standard fits** (k5, k6 on shaft, H7 in housing)
4. **Temperature difference** 5-10°C
5. **No special precision** requirements

**Examples:**
- General industrial machinery
- Fans and blowers
- Agricultural equipment
- Construction machinery

### 10.3 Preload Applications

**Use preload when:**

1. **High precision** required
2. **High stiffness** needed (machine tools)
3. **Eliminate play** for accuracy
4. **Prevent skidding** at high speed
5. **Moment loads** present
6. **Axial positioning** critical

**Examples:**
- Machine tool spindles
- Precision grinding machines
- Turbomachinery (compressors, turbines)
- Robotics (precision joints)
- Aerospace actuators
- High-speed dental handpieces

---

## 11. Practical Examples

### 11.1 Example 1: Electric Motor

**Application:** Standard 3-phase motor, 1500 rpm

**Analysis:**
- Operating temperature: Inner ring +70°C, Outer ring +60°C
- ΔT = 10°C
- Shaft fit: k6 (standard)
- Expected clearance reduction: 10-15 μm

**Selection:**

Use **C3 clearance** (Group 7):
- Compensates for thermal expansion
- Maintains small positive operating clearance
- Standard practice for electric motors

### 11.2 Example 2: Machine Tool Spindle

**Application:** Milling machine spindle, precision ±5 μm

**Analysis:**
- Requires high rigidity
- Precision positioning
- Angular contact bearings needed

**Selection:**

Use **angular contact bearing set, back-to-back (DB), medium preload**:
- Eliminates play
- High axial and moment stiffness
- Oil-air lubrication for cooling

**Example:** 7210 BECBP (pair, back-to-back, medium preload)

### 11.3 Example 3: Automotive Wheel Bearing

**Application:** Front wheel bearing, passenger car

**Analysis:**
- Moderate speed (up to 120 km/h → ~1000 rpm at wheel)
- Combined radial and axial loads (cornering)
- Some moment load
- Temperature variation

**Selection:**

Use **tapered roller bearing pair, light preload or small end play**:
- Handles combined loads
- Adjusted during assembly (locknut)
- Slight preload improves handling and reduces noise

**Typical:** 30205 + 30205 (paired tapered rollers)

### 11.4 Example 4: High-Speed Grinder

**Application:** Surface grinder spindle, 15,000 rpm

**Analysis:**
- Very high speed
- Light cutting load
- Requires precision

**Selection:**

Use **ceramic hybrid angular contact bearings, light to medium preload**:
- Hybrid bearings for high-speed capability
- Preload prevents skidding
- Oil-air lubrication essential

**Example:** 7208 CDGA/P4A DB (ceramic hybrid, back-to-back, P4 precision)

---

## 12. Clearance and Preload Measurement

### 12.1 Measuring Initial Clearance

**Radial clearance measurement:**

**Method 1: Feeler gauge**
- Insert feeler gauge between ball and race
- Measure at maximum displacement position
- Limited accuracy

**Method 2: Dial indicator**
- Mount bearing on fixture
- Fix outer ring, displace inner ring radially
- Measure total displacement with dial indicator
- Accurate method

**Standard procedure (ГОСТ):**

Apply specific radial load → measure displacement under load.

### 12.2 Measuring Mounted Clearance

**After installation on shaft, in housing:**

**Method: Axial displacement**
- Apply light axial load (few N)
- Measure axial displacement
- Convert to radial clearance (for ball bearings)

**Method: Lift-off measurement**
- Lift inner ring relative to outer
- Measure radial displacement

**Difficult on assembled machine → usually calculated, not measured.**

### 12.3 Verifying Preload

**Torque method:**

Measure bearing turning torque:
- Higher torque = higher preload
- Compare to specification

**Axial displacement:**

Apply known axial load, measure displacement:
- Stiffness indicates preload level

**Temperature monitoring:**

Run bearing, monitor temperature:
- Correct preload → stable, acceptable temperature
- Excessive preload → overheating

---

## 13. Troubleshooting

### 13.1 Excessive Clearance Problems

**Symptoms:**
- High vibration
- Noise (rattling)
- Poor precision
- Accelerated wear

**Causes:**
- Incorrect clearance group selected
- Loose fits (insufficient interference)
- Wear (end of life)

**Solutions:**
- Select reduced clearance group (C2)
- Increase fit interference (tighter tolerances)
- Replace worn bearing

### 13.2 Insufficient Clearance / Excessive Preload

**Symptoms:**
- Overheating
- High friction
- Premature failure
- Noise (continuous hum)

**Causes:**
- Clearance group too small
- Excessive fit interference
- High thermal expansion (ΔT > expected)
- Over-tightened preload

**Solutions:**
- Select larger clearance group (C3, C4)
- Reduce fit interference (looser tolerances)
- Improve cooling (reduce ΔT)
- Reduce preload (adjust spacers, locknut)

### 13.3 Thermal Runaway

**Mechanism:**

1. Insufficient operating clearance → high friction
2. Heat generation → temperature rise
3. Further clearance reduction (thermal expansion)
4. More friction → more heat
5. **Runaway:** Continuous temperature increase → seizure

**Prevention:**
- Proper clearance selection (C3, C4 for high ΔT)
- Adequate cooling
- Proper lubrication
- Monitoring (temperature sensors)

---

## 14. Standards and References

### 14.1 ГОСТ Standards

**ГОСТ 24810-2013** — Подшипники качения. Внутренние зазоры
- Clearance groups and values for different bearing types
- Radial and axial clearance specifications
- Measurement methods

**ГОСТ 520-2011** — Подшипники качения. Общие технические условия
- General technical requirements including clearance

**ГОСТ 3325-85** — Подшипники качения. Поля допусков и технические требования к посадочным поверхностям валов и корпусов
- Fits and tolerances affecting clearance

### 14.2 ISO Standards

**ISO 5753-1:2009** — Rolling bearings — Internal clearance — Part 1: Radial internal clearance for radial bearings
- Clearance groups (C2, CN, C3, C4, C5)
- Values for various bearing types

**ISO 5753-2** — Part 2: Axial internal clearance for angular contact ball bearings

**ISO 10285** — Cylindrical roller bearings — Boundary dimensions and clearances

### 14.3 Manufacturer Resources

**SKF, NSK, FAG, Timken, NTN:**
- Detailed clearance tables
- Preload specifications
- Clearance calculation tools
- Application guides

---

## 15. Summary

### 15.1 Key Concepts

1. **Initial clearance** → Mounted clearance → **Operating clearance**
2. **Fits reduce clearance** (interference on shaft)
3. **Temperature reduces clearance** (ΔT between rings)
4. **Select initial clearance** to achieve optimal operating clearance
5. **Preload eliminates clearance** for precision and rigidity

### 15.2 Selection Guidelines

**Normal clearance (CN):**
- Standard conditions
- Moderate speed, load, temperature

**Increased clearance (C3, C4):**
- High temperature (ΔT > 10°C)
- Tight shaft fits
- Heavy loads
- Electric motors, pumps

**Reduced clearance (C2):**
- High precision
- Low temperature rise
- Light loads
- Instruments

**Preload:**
- Machine tools
- High-speed precision applications
- Moment loads
- Eliminate play

### 15.3 Critical Formulas

**Mounted clearance:**
```
Cr_mounted = Cr_initial - ΔCr_fit
```

**Operating clearance:**
```
Cr_operating = Cr_mounted - ΔCr_thermal
```

**Thermal effect:**
```
ΔCr_thermal = α · dm · ΔT
```

---

## 16. Conclusion

Proper selection and management of internal clearance and preload are critical for:
- **Bearing life:** Optimal load distribution
- **Performance:** Precision, rigidity, smooth operation
- **Reliability:** Prevent overheating, wear, failure

Understanding:
- Clearance groups (C2, CN, C3, C4, C5)
- Effects of fits and temperature
- Operating clearance calculation
- When to use clearance vs preload
- Preload methods and applications

Enables engineers to select and apply bearings correctly for any application, from robust industrial machinery to ultra-precision spindles.

**Related Documents:**
- See [04_01_load_ratings.md](04_01_load_ratings.md) for load calculations
- See [04_02_life_calculations.md](04_02_life_calculations.md) for bearing life
- See [04_03_speed_limits.md](04_03_speed_limits.md) for speed considerations

---

**Document Status:** ✔ Complete
**Last Updated:** 2024
**Compliance:** ГОСТ 24810-2013, ISO 5753-1:2009, ISO 5753-2
