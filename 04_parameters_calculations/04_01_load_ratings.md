# Load Ratings and Load Calculations

## Purpose

This document provides comprehensive information on bearing load ratings, equivalent load calculations, and the application of load factors for proper bearing selection and verification. Understanding load ratings is fundamental to bearing engineering and ensures safe, reliable operation.

---

## 1. Basic Definitions

### 1.1 Static Load Rating (C₀)

**Definition (ГОСТ 18854, ISO 76):**

The **Basic Static Load Rating** (C₀) is the static load that produces a total permanent deformation of rolling elements and raceways equal to **0.0001** (0.01%) of the rolling element diameter at the most heavily loaded contact.

**Key characteristics:**
- Applied when bearing is stationary or rotating very slowly (n < 10 rpm)
- Represents load capacity without rotation
- Permanent deformation criteria: 0.0001 × Dw (Dw = ball/roller diameter)
- Used to calculate static safety factor
- Always lower than dynamic rating for same bearing

**Units:**
- ГОСТ: kilonewtons (kN)
- ISO: newtons (N) or kilonewtons (kN)
- Catalogs often show: kN

**Physical meaning:**

At load C₀, the contact stress reaches approximately:
- **Ball bearings:** 4,600 MPa (Hertzian stress)
- **Roller bearings:** 4,000 MPa (line contact stress)

These stress levels produce acceptable permanent deformation for intermittent operation.

### 1.2 Dynamic Load Rating (C)

**Definition (ГОСТ 18855, ISO 281):**

The **Basic Dynamic Load Rating** (C) is the constant radial load (for radial bearings) or constant axial load (for thrust bearings) that a bearing can theoretically endure for a rating life of **1 million revolutions** (L₁₀ = 10⁶) with **90% reliability**.

**Key characteristics:**
- Applies to rotating bearings under load
- Based on fatigue life theory
- 90% survival probability (10% probability of failure)
- Standardized to 1 million revolutions
- Forms the basis for life calculations

**Rating life concept:**
- **L₁₀ = 1,000,000 revolutions** when load P = C
- L₁₀ = basic rating life (90% reliability)
- Material: through-hardened bearing steel (≥ 58 HRC)
- Lubrication: adequate, clean
- Temperature: ≤ 120°C

**Physical meaning:**

Dynamic rating represents fatigue resistance. The bearing material (typically 100Cr6 / ШХ15) under cyclic Hertzian contact stress will develop subsurface fatigue cracks after repeated loading cycles.

---

## 2. Static Load Rating Calculations

### 2.1 Radial Ball Bearings

**Formula (ГОСТ 18854-94, ISO 76:2006):**

```
C₀ = f₀ · i · Z · Dw² · cos α
```

Where:
- **f₀** = calculation factor (depends on bearing geometry)
- **i** = number of rows of rolling elements
- **Z** = number of balls per row
- **Dw** = ball diameter [mm]
- **α** = nominal contact angle [degrees]
- **C₀** = basic static load rating [N]

**Calculation factors f₀ for radial ball bearings:**

| Bearing Type | Dw · cos α / Dpw | f₀ |
|--------------|------------------|-----|
| **Single row radial groove** | — | 12.3 |
| **Radial contact groove ball (α ≈ 0°)** | All values | 12.3 |
| **Angular contact** | ≥ 0.025 | 13.0 |
| **Angular contact** | 0.020 - 0.025 | 12.0 - 13.0 (interpolate) |
| **Self-aligning ball** | All values | 7.0 |

**Dpw** = pitch diameter of ball set = (d + D) / 2

### 2.2 Radial Roller Bearings

**Formula for cylindrical and needle roller bearings:**

```
C₀ = 44 · i · Z · lwe · Dw · cos α  [for lwe ≤ Dw]
C₀ = 220 · i · Z · Dw² · cos α      [for lwe > Dw]
```

**Formula for tapered roller bearings:**

```
C₀ = (f₀ · i · lwe · Dw · cos α) / (1 - 1.5 · tan α)
```

Where:
- **lwe** = effective contact length of roller [mm]
- **f₀** = 220 for tapered rollers
- **α** = contact angle

**Formula for spherical roller bearings:**

```
C₀ = 220 · i · Z · Dw² · cos α
```

For double-row spherical: i = 2 (two rows)

### 2.3 Thrust Ball Bearings

**Formula:**

```
C₀a = f₀ · Z · Dw² · sin α
```

Where:
- **C₀a** = basic static axial load rating [N]
- **f₀** = 26.6 (for thrust ball bearings)
- **sin α** = axial load component factor

### 2.4 Thrust Roller Bearings

**Formula (cylindrical thrust rollers):**

```
C₀a = 220 · Z · lwe · Dw · sin α
```

**Formula (tapered thrust rollers):**

```
C₀a = 220 · Z · lwe · Dw · sin α / (1 - 1.5 · tan α)
```

---

## 3. Dynamic Load Rating Calculations

### 3.1 Radial Ball Bearings

**Formula (ISO 281:2007):**

```
C = fc · (i · Z)^(0.7) · Dw^1.8 · (cos α)^0.3
```

Where:
- **fc** = calculation factor (function of geometry)
- **i** = number of rows
- **Z** = balls per row
- **Dw** = ball diameter [mm]
- **α** = contact angle

**Typical fc values:**
- Single row deep groove: fc ≈ 98 - 106 (depends on Dw/Dpw ratio)
- Angular contact: fc ≈ 60 - 100
- Self-aligning: fc ≈ 50 - 70

*Note: Exact fc values from manufacturer data or ISO 281 detailed tables*

### 3.2 Radial Roller Bearings

**Formula (cylindrical rollers):**

```
C = fc · (lwe · i · Z)^(7/9) · Dw^(29/27)
```

**Formula (tapered rollers):**

```
C = (2/3)^(e) · fc · (lwe · i · Z)^(7/9) · Dw^(29/27) · (cos α)^n
```

Where:
- **e** = load distribution exponent
- **n** = exponent for contact angle effect

### 3.3 Thrust Bearings

**Ball thrust bearings:**

```
Ca = fc · Z^(2/3) · Dw^1.8 · (tan α)^0.3
```

**Roller thrust bearings:**

```
Ca = fc · (lwe · Z)^(7/9) · Dw^(29/27) · (tan α)^n
```

---

## 4. Equivalent Static Load (P₀)

### 4.1 Definition

The **equivalent static load** P₀ is a calculated constant radial load (or axial load for thrust bearings) that would produce the same maximum contact stress as the actual load combination.

**Purpose:**
- Evaluate bearing safety under static or very slow rotation
- Calculate static safety factor: s₀ = C₀ / P₀
- Check peak loads, shock loads, starting conditions

### 4.2 Radial Bearings - General Formula

```
P₀ = X₀ · Fr + Y₀ · Fa
```

Where:
- **P₀** = equivalent static radial load [N]
- **Fr** = actual radial load [N]
- **Fa** = actual axial load [N]
- **X₀** = radial load factor
- **Y₀** = axial load factor

### 4.3 Load Factors for Static Load

**Single row deep groove ball bearings (α = 0°):**

| Condition | X₀ | Y₀ |
|-----------|----|----|
| Fa / Fr ≤ 0.8 | 0.6 | 0.5 |
| Fa / Fr > 0.8 | 0.5 | 0.47 |

**Single row angular contact ball bearings:**

Function of Fa/(Fr · tan α):

| Fa/(Fr·tan α) | X₀ | Y₀ |
|---------------|----|----|
| 0 - 0.55 | 1 | 0 |
| 0.55 - 1.0 | 0.6 | 0.5 |
| > 1.0 | 0.5 | 0.26·cot α |

**Cylindrical roller bearings (radial only):**

```
P₀ = Fr     (X₀ = 1, Y₀ = 0)
```

Cannot support axial load with standard design.

**Tapered roller bearings:**

| Fa/Fr | X₀ | Y₀ |
|-------|----|----|
| ≤ e | 1 | 0 |
| > e | 0.5 | 0.22 · cot α |

Where **e** = boundary factor (typically 0.3 - 0.4, from catalog)

**Spherical roller bearings:**

| Fa/Fr | X₀ | Y₀ |
|-------|----|----|
| ≤ e | 1 | 0 |
| > e | 0.67 | 0.67 · Y (from catalog) |

### 4.4 Minimum Equivalent Static Load

**Important rule:**

```
P₀ ≥ Fr  (radial bearings)
P₀ ≥ Fa  (thrust bearings)
```

Even if calculated P₀ is lower, use the actual radial (or axial) load as minimum.

### 4.5 Static Safety Factor

**Definition:**

```
s₀ = C₀ / P₀
```

**Recommended minimum values:**

| Application | s₀ min |
|-------------|--------|
| **Smooth operation, low requirements** | 0.5 - 1.0 |
| **Normal conditions, general machinery** | 1.0 - 1.5 |
| **High reliability, smooth running required** | 1.5 - 2.5 |
| **Precision applications, minimal vibration** | 2.5 - 4.0 |
| **Heavy shock loads** | 3.0 - 5.0 |

**Note:** s₀ < 1 is acceptable for light loads without shocks if smooth running is not critical.

---

## 5. Equivalent Dynamic Load (P)

### 5.1 Definition

The **equivalent dynamic load** P is a calculated constant radial load (or axial load) that would give the same bearing life as the actual load combination under actual operating conditions.

**Purpose:**
- Calculate bearing rating life L₁₀
- Compare different bearings
- Verify load capacity

### 5.2 Radial Bearings - General Formula

```
P = X · Fr + Y · Fa
```

Where:
- **P** = equivalent dynamic radial load [N]
- **Fr** = actual radial load [N]
- **Fa** = actual axial load [N]
- **X** = radial load factor (dynamic)
- **Y** = axial load factor (dynamic)

**Minimum value:**

```
P ≥ Fr (for radial bearings)
```

### 5.3 Load Factors for Dynamic Load

#### Single Row Deep Groove Ball Bearings

**Calculation parameter:**

```
fa = Fa / C₀
e = f(fa)  [from tables]
```

**Load factors:**

| Condition | X | Y |
|-----------|---|---|
| Fa / Fr ≤ e | 1 | 0 |
| Fa / Fr > e | 0.56 | Y (from table) |

**Table: e and Y values for deep groove ball bearings:**

| fa | e | Y (Fa/Fr > e) |
|----|---|---------------|
| 0.025 | 0.22 | 2.30 |
| 0.04 | 0.24 | 1.99 |
| 0.07 | 0.27 | 1.71 |
| 0.13 | 0.31 | 1.45 |
| 0.25 | 0.37 | 1.23 |
| 0.50 | 0.44 | 1.05 |

*Interpolate for intermediate values*

#### Single Row Angular Contact Ball Bearings

**For contact angle α = 15°:**

| Fa/(Fr·tan α) | X | Y |
|---------------|---|---|
| ≤ 1.14 | 1 | 0 |
| > 1.14 | 0.56 | 1.68 |

**For contact angle α = 25°:**

| Fa/(Fr·tan α) | X | Y |
|---------------|---|---|
| ≤ 0.95 | 1 | 0 |
| > 0.95 | 0.56 | 1.42 |

**For contact angle α = 40°:**

| Fa/(Fr·tan α) | X | Y |
|---------------|---|---|
| ≤ 0.76 | 1 | 0 |
| > 0.76 | 0.56 | 1.07 |

#### Cylindrical Roller Bearings (Standard)

```
P = Fr     (X = 1, Y = 0)
```

*No axial load capacity in standard design*

#### Tapered Roller Bearings

**Single bearing:**

| Fa/Fr | X | Y |
|-------|---|---|
| ≤ e | 1 | 0 |
| > e | 0.4 | Y (from catalog) |

**e** = typically 0.3 - 0.4 (from manufacturer)
**Y** = depends on contact angle (typically 1.5 - 2.5)

**Paired bearings (X or O arrangement):**

Must consider induced axial loads. Calculation more complex, requires iterative solution or manufacturer software.

#### Spherical Roller Bearings

**General formula:**

| Fa/Fr | X | Y |
|-------|---|---|
| ≤ e | 1 | 0 |
| > e | 0.67 | Y (from catalog) |

**Typical Y values:** 2.5 - 4.5 (depends on bearing series)

**e values:** typically 0.22 - 0.30

---

## 6. Practical Calculation Examples

### 6.1 Example 1: Deep Groove Ball Bearing - Simple Radial Load

**Given:**
- Bearing: 6208 (d = 40 mm, D = 80 mm, B = 18 mm)
- Catalog data: C = 32.0 kN, C₀ = 17.0 kN
- Radial load: Fr = 2500 N
- Axial load: Fa = 0 N

**Solution:**

Since Fa = 0:
```
P = Fr = 2500 N = 2.5 kN
```

**Static check:**
```
P₀ = Fr = 2500 N = 2.5 kN
s₀ = C₀ / P₀ = 17.0 / 2.5 = 6.8
```

Excellent static safety (s₀ > 1).

### 6.2 Example 2: Deep Groove Ball Bearing - Combined Load

**Given:**
- Bearing: 6308 (d = 40 mm, D = 90 mm, B = 23 mm)
- Catalog data: C = 55.3 kN, C₀ = 31.0 kN
- Radial load: Fr = 5000 N
- Axial load: Fa = 2000 N
- Speed: n = 1500 rpm

**Solution - Static Load:**

Step 1: Calculate Fa/Fr ratio
```
Fa / Fr = 2000 / 5000 = 0.4
```

Step 2: Compare with 0.8
```
0.4 < 0.8 → Use X₀ = 0.6, Y₀ = 0.5
```

Step 3: Calculate P₀
```
P₀ = X₀ · Fr + Y₀ · Fa
P₀ = 0.6 · 5000 + 0.5 · 2000
P₀ = 3000 + 1000 = 4000 N = 4.0 kN
```

Step 4: Static safety
```
s₀ = C₀ / P₀ = 31.0 / 4.0 = 7.75
```

Excellent static safety.

**Solution - Dynamic Load:**

Step 1: Calculate fa
```
fa = Fa / C₀ = 2000 / 31000 = 0.065
```

Step 2: From table (interpolate between 0.04 and 0.07):
```
e ≈ 0.26
Y ≈ 1.8
```

Step 3: Check Fa/Fr vs e
```
Fa / Fr = 0.4 > e (0.26)
```

Therefore use: X = 0.56, Y = 1.8

Step 4: Calculate P
```
P = X · Fr + Y · Fa
P = 0.56 · 5000 + 1.8 · 2000
P = 2800 + 3600 = 6400 N = 6.4 kN
```

**Rating life:**
```
L₁₀ = (C / P)³ million revolutions
L₁₀ = (55.3 / 6.4)³ = (8.64)³ = 645 million revolutions
```

**Operating hours:**
```
L₁₀h = (10⁶ / (60 · n)) · L₁₀
L₁₀h = (10⁶ / (60 · 1500)) · 645
L₁₀h = (1000000 / 90000) · 645 = 7167 hours
```

### 6.3 Example 3: Angular Contact Ball Bearing (α = 25°)

**Given:**
- Bearing: 7308 BEGAP (single, α = 25°)
- Catalog data: C = 53.0 kN, C₀ = 36.0 kN
- Radial load: Fr = 6000 N
- Axial load: Fa = 4000 N

**Solution - Dynamic Load:**

Step 1: Calculate Fa / (Fr · tan α)
```
tan 25° = 0.466
Fa / (Fr · tan α) = 4000 / (6000 · 0.466) = 4000 / 2796 = 1.43
```

Step 2: Compare with boundary (0.95 for α = 25°)
```
1.43 > 0.95
```

Therefore: X = 0.56, Y = 1.42

Step 3: Calculate P
```
P = X · Fr + Y · Fa
P = 0.56 · 6000 + 1.42 · 4000
P = 3360 + 5680 = 9040 N = 9.04 kN
```

**Note:** High axial load creates significant equivalent load.

### 6.4 Example 4: Tapered Roller Bearing

**Given:**
- Bearing: 32208 (d = 40 mm, D = 80 mm, T = 24.75 mm)
- Catalog data: C = 69.0 kN, C₀ = 64.0 kN
- Contact angle: α ≈ 13.5° (typical for 302 series)
- Radial load: Fr = 8000 N
- Axial load: Fa = 3000 N
- Catalog data: e = 0.35, Y = 1.7

**Solution - Dynamic Load:**

Step 1: Calculate Fa / Fr
```
Fa / Fr = 3000 / 8000 = 0.375
```

Step 2: Compare with e
```
0.375 > 0.35 (e)
```

Therefore: X = 0.4, Y = 1.7

Step 3: Calculate P
```
P = X · Fr + Y · Fa
P = 0.4 · 8000 + 1.7 · 3000
P = 3200 + 5100 = 8300 N = 8.3 kN
```

**Static check:**

For static (Fa/Fr = 0.375 > e):
```
X₀ = 0.5, Y₀ = 0.22 · cot(13.5°)
cot(13.5°) = 1 / tan(13.5°) = 1 / 0.240 = 4.17
Y₀ = 0.22 · 4.17 = 0.92

P₀ = 0.5 · 8000 + 0.92 · 3000
P₀ = 4000 + 2760 = 6760 N = 6.76 kN

s₀ = C₀ / P₀ = 64.0 / 6.76 = 9.5
```

Excellent static safety.

### 6.5 Example 5: Spherical Roller Bearing

**Given:**
- Bearing: 22215 CCK/W33 (d = 75 mm, D = 130 mm, B = 31 mm)
- Catalog data: C = 240 kN, C₀ = 265 kN
- Radial load: Fr = 20000 N
- Axial load: Fa = 8000 N
- Catalog data: e = 0.24, Y = 3.0

**Solution:**

Step 1: Check Fa / Fr
```
Fa / Fr = 8000 / 20000 = 0.4
```

Step 2: Compare with e
```
0.4 > 0.24 (e)
```

Therefore: X = 0.67, Y = 3.0

Step 3: Calculate P
```
P = X · Fr + Y · Fa
P = 0.67 · 20000 + 3.0 · 8000
P = 13400 + 24000 = 37400 N = 37.4 kN
```

**Note:** Spherical roller bearings have high Y factors, making them efficient for combined loads.

---

## 7. Special Considerations

### 7.1 Load Distribution in Multiple Bearing Arrangements

**Tandem arrangement (II, ↑↑):**
- Both bearings carry same direction axial load
- Total capacity = sum of individual capacities
- Equal load distribution if identical bearings

**Back-to-back arrangement (O, ↔):**
- Bearings oppose each other
- Can handle bidirectional axial loads
- Provides moment rigidity
- Load distribution depends on preload

**Face-to-face arrangement (X, →←):**
- Less rigid than back-to-back
- Suitable for widely spaced bearings
- Lower moment capacity

### 7.2 Impact and Shock Loads

**Dynamic load with shock:**

```
P = fs · P_nominal
```

Where fs = shock factor:

| Load Character | fs |
|----------------|-----|
| Smooth operation | 1.0 - 1.2 |
| Normal conditions | 1.2 - 1.5 |
| Light shocks | 1.5 - 2.0 |
| Moderate shocks | 2.0 - 2.5 |
| Heavy shocks | 2.5 - 3.5 |

### 7.3 Load Direction Uncertainty

If load direction varies:
- Use worst-case combination
- Consider maximum possible load
- Apply additional safety factor (1.2 - 1.5)

### 7.4 Temperature Effects on Load Rating

**High temperature reduction factors:**

| Operating Temperature | Reduction Factor |
|-----------------------|------------------|
| ≤ 120°C | 1.0 |
| 150°C | 0.95 |
| 200°C | 0.85 |
| 250°C | 0.70 |
| 300°C | 0.55 |

**Corrected rating:**
```
C_actual = C_catalog · f_temp
```

---

## 8. Standards References

### 8.1 ГОСТ Standards

**ГОСТ 18854-94** — Подшипники качения. Статическая грузоподъёмность
- Calculation of basic static load rating C₀
- Static equivalent load P₀
- Static safety factor

**ГОСТ 18855-2013** — Подшипники качения. Динамическая грузоподъёмность и номинальная долговечность
- Calculation of basic dynamic load rating C
- Equivalent dynamic load P
- Rating life L₁₀

### 8.2 ISO Standards

**ISO 76:2006** — Rolling bearings — Static load ratings
- Static load rating calculations
- Equivalent static load
- Safety factors

**ISO 281:2007** — Rolling bearings — Dynamic load ratings and rating life
- Dynamic load rating calculations
- Basic rating life
- Modified rating life (includes a₁ and aISO)

### 8.3 Manufacturer Documentation

Major bearing manufacturers (SKF, NSK, FAG, Timken, NTN) provide:
- Detailed load factor tables
- Calculation software
- Application-specific guidelines
- Extended life calculation methods

---

## 9. Summary and Quick Reference

### Quick Selection Guide

**For static loads or slow rotation (n < 10 rpm):**
1. Calculate P₀ using static load factors
2. Check s₀ = C₀ / P₀ ≥ required minimum
3. Verify permanent deformation is acceptable

**For rotating bearings:**
1. Calculate P using dynamic load factors
2. Calculate required C based on desired life
3. Select bearing with C ≥ required C
4. Verify static safety s₀ for starting/shock loads

### Load Factor Summary Table

| Bearing Type | Pure Radial | Combined Load |
|--------------|-------------|---------------|
| **Deep groove ball** | X=1, Y=0 | See tables (X=0.56 or 1) |
| **Angular contact** | X=1, Y=0 | X=0.56, Y=f(α) |
| **Cylindrical roller** | X=1, Y=0 | X=1, Y=0 (no axial) |
| **Tapered roller** | X=1, Y=0 | X=0.4, Y=catalog |
| **Spherical roller** | X=1, Y=0 | X=0.67, Y=catalog |

### Critical Reminders

1. **Always use P ≥ Fr** (minimum rule)
2. **Check both static and dynamic** ratings
3. **Account for shock loads** (multiply by fs)
4. **Verify temperature limits** (reduce C if T > 120°C)
5. **Use catalog data** when available (more accurate than formulas)

---

## 10. Conclusion

Load ratings and equivalent load calculations form the foundation of bearing selection. Proper application of:
- Static load rating (C₀) → prevents permanent deformation
- Dynamic load rating (C) → ensures adequate fatigue life
- Load factors (X, Y) → converts actual loads to equivalent loads
- Safety factors → provides design margin

Understanding and correctly applying these principles ensures reliable, long-lasting bearing performance in all applications.

**Next steps:**
- See [04_02_life_calculations.md](04_02_life_calculations.md) for bearing life calculations
- See [04_03_speed_limits.md](04_03_speed_limits.md) for speed verification
- See [04_04_clearance_preload.md](04_04_clearance_preload.md) for clearance selection

---

**Document Status:** ✔ Complete
**Last Updated:** 2024
**Compliance:** ГОСТ 18854-94, ГОСТ 18855-2013, ISO 76:2006, ISO 281:2007
