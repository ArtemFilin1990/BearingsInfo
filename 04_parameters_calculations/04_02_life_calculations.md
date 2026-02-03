# Bearing Life Calculations

## Purpose

This document provides comprehensive methodology for calculating bearing rating life, including basic L₁₀ life, modified life calculations per ISO 281, life adjustment factors, and service life requirements for various applications. Understanding bearing life is essential for reliable machinery design and maintenance planning.

---

## 1. Basic Concepts

### 1.1 Bearing Life Definition

**Bearing Life (Долговечность подшипника):**

The number of revolutions (or operating hours) that a bearing can complete before the first evidence of material fatigue appears on the rolling elements or raceways.

**Key characteristics:**
- Statistical phenomenon (not deterministic)
- Based on subsurface fatigue failure
- Excludes failures from: wear, corrosion, electrical damage, improper mounting
- Assumes: adequate lubrication, proper installation, clean environment

### 1.2 Fatigue Failure Mechanism

**Rolling contact fatigue:**

1. **Hertzian contact stress** → subsurface shear stress
2. **Cyclic loading** → micro-crack initiation (10-50 μm below surface)
3. **Crack propagation** → spalling (flaking of material)
4. **Progressive damage** → vibration, noise, failure

**Weibull distribution:**

Bearing life follows Weibull probability distribution with shape parameter β ≈ 1.5 (for ball bearings) or β ≈ 1.1-1.3 (for roller bearings).

### 1.3 Rating Life Concept

**Basic Rating Life L₁₀:**

The life that **90% of a group of apparently identical bearings** will complete or exceed before the first evidence of fatigue develops.

**Interpretation:**
- L₁₀ = 90% survival probability
- 10% probability of failure
- Also called: **B₁₀ life** (B = bearing, 10% failure rate)

**Standard conditions:**
- Material: through-hardened bearing steel (≥ 58 HRC)
- Lubrication: adequate, clean
- Temperature: ≤ 120°C
- Proper mounting and alignment
- No contamination

---

## 2. Basic Life Calculation (L₁₀)

### 2.1 Formula for Ball Bearings

**Basic rating life (revolutions):**

```
L₁₀ = (C / P)³  [million revolutions]
```

Where:
- **L₁₀** = basic rating life [10⁶ revolutions]
- **C** = basic dynamic load rating [kN]
- **P** = equivalent dynamic load [kN]
- **Exponent = 3** (for ball bearings)

**Basic rating life (hours):**

```
L₁₀h = (10⁶ / (60 · n)) · L₁₀
```

Where:
- **L₁₀h** = basic rating life [operating hours]
- **n** = rotational speed [rpm]
- **60** = conversion minutes to hours

**Simplified formula:**

```
L₁₀h = (10⁶ / (60 · n)) · (C / P)³

L₁₀h = 16667 / n · (C / P)³   [hours]
```

### 2.2 Formula for Roller Bearings

**Basic rating life (revolutions):**

```
L₁₀ = (C / P)^(10/3)  [million revolutions]
```

**Exponent = 10/3 ≈ 3.33** (for roller bearings)

**Basic rating life (hours):**

```
L₁₀h = (10⁶ / (60 · n)) · (C / P)^(10/3)

L₁₀h = 16667 / n · (C / P)^3.33   [hours]
```

**Reason for different exponent:**

Line contact (rollers) vs. point contact (balls) produces different stress distribution and fatigue behavior.

### 2.3 Quick Reference Table

| Bearing Type | Life Exponent p |
|--------------|----------------|
| **Ball bearings** (all types) | 3 |
| **Roller bearings** (cylindrical, tapered, spherical) | 10/3 ≈ 3.33 |
| **Needle roller bearings** | 10/3 ≈ 3.33 |

---

## 3. Modified Rating Life (ISO 281:2007)

### 3.1 General Formula

**ISO 281:2007** introduced life modification factors to account for real operating conditions:

```
L₁₀m = a₁ · aISO · L₁₀
```

Where:
- **L₁₀m** = modified rating life [10⁶ revolutions or hours]
- **a₁** = reliability adjustment factor
- **aISO** = life modification factor (lubrication, contamination, fatigue limit)
- **L₁₀** = basic rating life

### 3.2 Reliability Adjustment Factor (a₁)

**Purpose:** Adjust life for different reliability levels (survival probabilities).

**Formula:**

```
a₁ = (Lp / L₁₀)^(1/β)
```

For typical bearing steel: β ≈ 1.5

**Standard values (ISO 281, ГОСТ 18855):**

| Reliability | Symbol | a₁ | Interpretation |
|-------------|--------|-----|----------------|
| **90%** | L₁₀, B₁₀ | 1.00 | Standard (10% failure) |
| **95%** | L₅, B₅ | 0.64 | High reliability (5% failure) |
| **96%** | L₄, B₄ | 0.55 | — |
| **97%** | L₃, B₃ | 0.47 | — |
| **98%** | L₂, B₂ | 0.37 | — |
| **99%** | L₁, B₁ | 0.25 | Very high reliability (1% failure) |

**Example:**

For 95% reliability (L₅):
```
L₅ = 0.64 · L₁₀
```

For 99% reliability (L₁):
```
L₁ = 0.25 · L₁₀
```

**Usage:**

- Critical applications → use L₅ or L₁
- Standard machinery → use L₁₀
- Non-critical, replaceable → L₁₀ acceptable

### 3.3 ISO Life Modification Factor (aISO)

**Purpose:** Account for lubrication quality, contamination, and material fatigue limit.

**Formula (ISO 281:2007):**

```
aISO = f(κ, Pu/P, contamination)
```

Where:
- **κ** (kappa) = lubrication condition parameter (viscosity ratio)
- **Pu/P** = fatigue load limit ratio
- **contamination** = cleanliness factor

**Simplified approach:**

```
aISO ≈ 1.0 to 50+ depending on conditions
```

- **Poor conditions:** aISO ≈ 0.1 - 0.3 (inadequate lubrication, contamination)
- **Normal conditions:** aISO ≈ 1.0 (adequate lubrication)
- **Good conditions:** aISO ≈ 3 - 10 (excellent lubrication, clean, light load)
- **Excellent conditions:** aISO ≈ 10 - 50+ (very light load, optimal lubrication)

### 3.4 Lubrication Condition Parameter (κ)

**Definition:**

```
κ = ν / ν₁
```

Where:
- **ν** = actual kinematic viscosity at operating temperature [mm²/s]
- **ν₁** = reference kinematic viscosity (minimum required) [mm²/s]

**Reference viscosity ν₁:**

Depends on speed and bearing mean diameter:

```
dm = (d + D) / 2   [mm]
n·dm = speed parameter [mm·rpm]
```

**Table: Reference viscosity ν₁ (ISO 281, SKF):**

| n·dm | ν₁ [mm²/s] |
|------|-----------|
| 1,000 | 140 |
| 2,000 | 100 |
| 5,000 | 50 |
| 10,000 | 25 |
| 20,000 | 13 |
| 50,000 | 7 |
| 100,000 | 4 |
| 200,000 | 3 |

*Interpolate for intermediate values*

**Lubrication quality interpretation:**

| κ | Lubrication Quality | aISO Effect |
|---|---------------------|-------------|
| **< 0.4** | Inadequate | aISO < 0.1 (very short life) |
| **0.4 - 1** | Marginal | aISO ≈ 0.1 - 1 |
| **1 - 4** | Adequate to good | aISO ≈ 1 - 10 |
| **> 4** | Excellent | aISO ≈ 10 - 50+ |

### 3.5 Fatigue Load Limit (Pu)

**Definition:**

The load below which fatigue life approaches infinity (no fatigue failure expected).

**Approximate values:**

```
Pu ≈ 0.01 · C₀   (for ball bearings)
Pu ≈ 0.02 · C₀   (for roller bearings)
```

**Effect on aISO:**

When P < Pu:
- Fatigue failure unlikely
- aISO increases significantly
- Other failure modes dominate (wear, corrosion)

### 3.6 Contamination Factor

**Standard cleanliness categories (ISO 281 Technical Report):**

| Category | Description | eC Factor |
|----------|-------------|-----------|
| **High cleanliness** | Particle filtration β > 200, sealed bearings | 1.0 |
| **Normal cleanliness** | Typical industrial conditions, basic sealing | 0.8 - 0.9 |
| **Slight contamination** | Some particle ingress | 0.5 - 0.7 |
| **Typical contamination** | Normal industrial environment | 0.3 - 0.5 |
| **Severe contamination** | Harsh environment, abrasive particles | 0.1 - 0.3 |
| **Very severe** | Heavy contamination | < 0.1 |

**Contamination affects aISO through reduction of effective lubrication.**

---

## 4. Practical Life Calculation Examples

### 4.1 Example 1: Basic L₁₀ Calculation (Ball Bearing)

**Given:**
- Bearing: 6308 (deep groove ball bearing)
- C = 55.3 kN
- P = 6.4 kN (from load calculation)
- n = 1500 rpm

**Solution:**

**L₁₀ (revolutions):**
```
L₁₀ = (C / P)³
L₁₀ = (55.3 / 6.4)³ = (8.64)³ = 645 million revolutions
```

**L₁₀h (hours):**
```
L₁₀h = 16667 / n · (C / P)³
L₁₀h = 16667 / 1500 · 645
L₁₀h = 11.11 · 645 = 7167 hours
```

**Interpretation:**
90% of these bearings will survive at least 7167 operating hours.

### 4.2 Example 2: Roller Bearing Life

**Given:**
- Bearing: 22215 (spherical roller bearing)
- C = 240 kN
- P = 37.4 kN
- n = 600 rpm

**Solution:**

**L₁₀ (revolutions):**
```
L₁₀ = (C / P)^(10/3)
L₁₀ = (240 / 37.4)^3.33 = (6.42)^3.33 = 381 million revolutions
```

**L₁₀h (hours):**
```
L₁₀h = 16667 / 600 · 381
L₁₀h = 27.78 · 381 = 10,584 hours
```

### 4.3 Example 3: Modified Life with Reliability Factor

**Given:**
- Same bearing as Example 1: L₁₀h = 7167 hours
- Requirement: 95% reliability (L₅)

**Solution:**

```
a₁ = 0.64  (for 95% reliability)

L₅h = a₁ · L₁₀h
L₅h = 0.64 · 7167 = 4587 hours
```

**Interpretation:**
95% of bearings will survive at least 4587 hours (vs 7167 hours for 90% reliability).

### 4.4 Example 4: Modified Life with aISO (Lubrication Factor)

**Given:**
- Basic life: L₁₀h = 7167 hours
- Operating temperature: 70°C
- Oil viscosity at 70°C: ν = 32 mm²/s
- Speed: n = 1500 rpm
- Bearing: 6308 (d = 40, D = 90 mm)

**Solution:**

**Step 1: Calculate dm**
```
dm = (d + D) / 2 = (40 + 90) / 2 = 65 mm
```

**Step 2: Calculate n·dm**
```
n·dm = 1500 · 65 = 97,500 mm·rpm
```

**Step 3: Find reference viscosity ν₁**

From table (interpolate between 50,000 and 100,000):
```
ν₁ ≈ 4.5 mm²/s
```

**Step 4: Calculate κ**
```
κ = ν / ν₁ = 32 / 4.5 = 7.1
```

**Step 5: Estimate aISO**

With κ = 7.1 (excellent lubrication), clean conditions, moderate load:
```
aISO ≈ 8 - 12  (conservative estimate: 10)
```

**Step 6: Modified life**
```
L₁₀m = aISO · L₁₀h
L₁₀m = 10 · 7167 = 71,670 hours
```

**Interpretation:**
With excellent lubrication, bearing life increases by factor of 10.

**Note:** Manufacturer catalogs or software provide more accurate aISO calculations.

### 4.5 Example 5: Combined Reliability and ISO Factors

**Given:**
- Basic life: L₁₀h = 10,000 hours
- Requirement: 99% reliability (L₁)
- Operating conditions: aISO = 5 (good lubrication, clean)

**Solution:**

```
a₁ = 0.25  (for L₁, 99% reliability)

L₁m = a₁ · aISO · L₁₀h
L₁m = 0.25 · 5 · 10,000
L₁m = 12,500 hours
```

**Interpretation:**
- Basic 90% life: 10,000 hours
- With aISO only (90% reliability): 50,000 hours
- With 99% reliability, good conditions: 12,500 hours

**Note:** Higher reliability requirement reduces life, but good conditions compensate.

### 4.6 Example 6: Variable Load and Speed

**Given:**
- Bearing operates in 3 conditions:
  - Condition A: PA = 5 kN, nA = 1200 rpm, 40% of time
  - Condition B: PB = 8 kN, nB = 1800 rpm, 50% of time
  - Condition C: PC = 12 kN, nC = 2400 rpm, 10% of time
- Bearing: C = 48 kN (ball bearing)

**Solution:**

**Method: Equivalent load and speed**

**Step 1: Calculate equivalent load**

```
Peq³ = (qA · PA³ + qB · PB³ + qC · PC³)

Where q = time fraction

Peq³ = 0.40 · 5³ + 0.50 · 8³ + 0.10 · 12³
Peq³ = 0.40 · 125 + 0.50 · 512 + 0.10 · 1728
Peq³ = 50 + 256 + 172.8 = 478.8

Peq = (478.8)^(1/3) = 7.83 kN
```

**Step 2: Calculate average speed**

```
navg = qA · nA + qB · nB + qC · nC
navg = 0.40 · 1200 + 0.50 · 1800 + 0.10 · 2400
navg = 480 + 900 + 240 = 1620 rpm
```

**Step 3: Calculate life**

```
L₁₀h = 16667 / 1620 · (48 / 7.83)³
L₁₀h = 10.29 · (6.13)³
L₁₀h = 10.29 · 230.3 = 2370 hours
```

---

## 5. Service Life Requirements by Application

### 5.1 General Industrial Applications

| Application | Recommended L₁₀h | Reliability Level |
|-------------|------------------|-------------------|
| **Household appliances** | 1,000 - 2,000 h | L₁₀ (90%) |
| **Agricultural machinery** | 2,000 - 4,000 h | L₁₀ (90%) |
| **Construction equipment** | 3,000 - 8,000 h | L₁₀ (90%) |
| **General industrial machinery** | 8,000 - 20,000 h | L₁₀ (90%) |
| **Electric motors (continuous)** | 20,000 - 40,000 h | L₁₀ (90%) |
| **Machine tools** | 20,000 - 50,000 h | L₅ or L₁₀ |
| **Pumps, fans (continuous)** | 40,000 - 100,000 h | L₁₀ to L₅ |

### 5.2 Critical and High-Reliability Applications

| Application | Recommended L₁₀h | Reliability Level |
|-------------|------------------|-------------------|
| **Aerospace** | 10,000 - 50,000 h | **L₁ (99%)** |
| **Rail traction** | 500,000 - 1,000,000 km | L₁₀ to L₅ |
| **Wind turbines** | 130,000 - 175,000 h (20 years) | L₁ to L₅ |
| **Medical equipment** | 10,000 - 20,000 h | **L₁ (99%)** |
| **Nuclear power** | 100,000+ h | **L₁ (99%)** |

### 5.3 Automotive Applications

| Component | Service Life | Reliability |
|-----------|--------------|-------------|
| **Engine accessories** | 3,000 - 5,000 h | L₁₀ |
| **Transmission** | 200,000 - 300,000 km | L₅ - L₁ |
| **Wheel bearings** | 150,000 - 300,000 km | **L₁ (99%)** |
| **Electric vehicle drives** | 200,000+ km | L₁ - L₀.₁ |

---

## 6. Probability of Survival

### 6.1 Weibull Distribution

**Survival probability function:**

```
S(L) = exp[-(L / L₁₀)^(1/e)]
```

Where:
- **S(L)** = probability of survival to life L
- **e** = Weibull slope exponent
- **L₁₀** = characteristic life

For bearing steel: e ≈ 1.5

### 6.2 Reliability Table

**Probability that bearing survives to different lives:**

| Life | Reliability (%) | Symbol |
|------|----------------|--------|
| **0.05 · L₁₀** | 99.9% | — |
| **0.1 · L₁₀** | 99.5% | — |
| **0.25 · L₁₀** | 99% | L₁ |
| **0.64 · L₁₀** | 95% | L₅ |
| **1.0 · L₁₀** | **90%** | **L₁₀** |
| **3.0 · L₁₀** | 60% | — |
| **5.0 · L₁₀** | 50% | L₅₀ (median life) |
| **10 · L₁₀** | 35% | — |
| **20 · L₁₀** | 20% | — |

**Key insight:**

Median life (L₅₀) ≈ **5 times L₁₀ life**

Meaning: Half the bearings will survive 5× longer than the L₁₀ rating.

---

## 7. Factors Affecting Actual Life

### 7.1 Positive Factors (Increase Life)

**Lubrication:**
- High viscosity oil (κ > 4): +500% to +2000%
- Synthetic oils: +20% to +50%
- Proper filtration (β > 200): +100% to +300%

**Operating conditions:**
- Light loads (P < 0.1·C): +1000% to unlimited
- Lower speed: improves lubrication film
- Stable temperature: prevents lubricant degradation
- Clean environment: prevents abrasion

**Design factors:**
- High-quality steel (vacuum degassed): +20% to +50%
- Ceramic rolling elements: +300% to +1000%
- Improved surface finish: +20% to +100%

### 7.2 Negative Factors (Decrease Life)

**Lubrication issues:**
- Inadequate lubrication (κ < 0.4): -90% or more
- Contamination: -50% to -90%
- Water contamination: -80% to -95%
- Wrong viscosity: -50% to -80%

**Operating conditions:**
- High temperature (>120°C): see reduction factors
- Vibration and shocks: -20% to -60%
- Misalignment: -30% to -70%
- Incorrect mounting: -50% to -90%

**Environmental:**
- Corrosive atmosphere: -50% to -90%
- Electrical current passage: -80% to -95%
- Moisture: -30% to -70%

---

## 8. Life Calculation Strategy

### 8.1 Design Stage

**Step 1: Determine required service life**
- Application type → Table 5.1 or 5.2
- Operating hours per year
- Desired replacement interval

**Step 2: Select reliability level**
- Standard machinery → L₁₀
- Important components → L₅
- Critical safety → L₁

**Step 3: Calculate required C**

```
C_required = P · (L_required / L₁₀_target)^(1/p)
```

Where p = 3 (balls) or 10/3 (rollers)

**Step 4: Select bearing**
- Choose bearing with C ≥ C_required
- Verify size, speed, temperature limits
- Check static safety s₀

### 8.2 Verification Stage

**Calculate actual life:**

```
L₁₀m = a₁ · aISO · (C / P)^p · (10⁶ / (60·n))
```

**Compare with requirement:**
- L₁₀m ≥ L_required → OK
- L₁₀m < L_required → Select larger bearing or improve conditions

### 8.3 Maintenance Planning

**Use calculated life for:**
- Predictive maintenance schedules
- Spare parts inventory
- Expected replacement intervals
- MTBF (Mean Time Between Failures) estimates

**MTBF relationship:**

```
MTBF ≈ 5 × L₁₀h  (median life for e ≈ 1.5)
```

---

## 9. Advanced Topics

### 9.1 Bearing Combinations

**Tandem arrangement:**
```
L₁₀_total = L₁₀_single / 2^(1/p)
```

**Parallel arrangement (load sharing):**

Each bearing carries portion of load → longer total life.

### 9.2 Variable Loads (Duty Cycle)

**General method:**

Calculate equivalent load based on load spectrum:

```
P_eq^p = (1/N_total) · Σ(Ni · Pi^p)
```

Where:
- Ni = revolutions at load Pi
- N_total = total revolutions

### 9.3 Temperature-Adjusted Life

**For T > 120°C:**

```
C_adj = C · f_temp
L₁₀_adj = (C_adj / P)^p
```

Temperature reduction factors from load ratings document.

---

## 10. Software Tools

### 10.1 Manufacturer Calculation Programs

**SKF:** SKF Bearing Select, SKF SimPro Expert
**NSK:** NSK CAD-E-Catalogue
**FAG/INA (Schaeffler):** Bearinx calculation software
**Timken:** SYBER bearing analysis
**NTN:** NTN bearing finder

**Features:**
- Accurate aISO calculation
- Load spectrum analysis
- Thermal analysis
- Detailed geometry database

### 10.2 Spreadsheet Methods

**Basic template:**
```
Input: C, P, n, bearing type
Calculate: L₁₀, L₁₀h
Apply: a₁, aISO (manual input)
Output: L₁₀m, L_reliability
```

---

## 11. Standards References

### 11.1 ГОСТ Standards

**ГОСТ 18855-2013** — Подшипники качения. Динамическая грузоподъёмность и номинальная долговечность
- Basic rating life calculation
- Life exponents for different bearing types
- Equivalent loads

**ГОСТ 16162-93** — Подшипники качения. Расчет ресурса по критерию усталостного выкрашивания
- Service life calculations
- Statistical methods

### 11.2 ISO Standards

**ISO 281:2007** — Rolling bearings — Dynamic load ratings and rating life
- Complete life calculation methodology
- Life modification factors (a₁, aISO)
- Reference viscosity tables
- Fatigue load limit concept

**ISO/TS 16281** — Rolling bearings — Methods for calculating the modified reference rating life for universally loaded bearings
- Advanced calculation methods
- Complex load conditions
- Detailed aISO methodology

---

## 12. Summary

### 12.1 Key Formulas

**Ball bearings:**
```
L₁₀h = 16,667 / n · (C / P)³
```

**Roller bearings:**
```
L₁₀h = 16,667 / n · (C / P)^3.33
```

**Modified life:**
```
L₁₀m = a₁ · aISO · L₁₀h
```

### 12.2 Critical Factors

1. **Load accuracy:** Use correct X, Y factors
2. **Lubrication:** Determines aISO (factor 1 to 50+)
3. **Cleanliness:** Major impact on actual life
4. **Reliability requirement:** L₁₀, L₅, or L₁ based on application criticality
5. **Operating conditions:** Temperature, speed, alignment

### 12.3 Practical Tips

- **Design conservatively:** Use L₅ or L₁ for critical applications
- **Consider aISO carefully:** Good lubrication = 5-10× life improvement
- **Plan maintenance:** L₁₀ is 90% reliability, not 100%
- **Monitor conditions:** Vibration analysis detects early failures
- **Document assumptions:** For future verification and improvement

---

## 13. Conclusion

Bearing life calculation is both a science and an art:
- **Science:** Rigorous formulas from ISO 281 and ГОСТ 18855
- **Art:** Proper estimation of aISO, operating conditions, reliability requirements

Accurate life calculation enables:
- Optimal bearing selection
- Reliable machinery design
- Effective maintenance planning
- Cost-effective operation

**Next Steps:**
- See [04_01_load_ratings.md](04_01_load_ratings.md) for load calculations
- See [04_03_speed_limits.md](04_03_speed_limits.md) for speed verification
- See [04_04_clearance_preload.md](04_04_clearance_preload.md) for clearance/preload

---

**Document Status:** ✔ Complete
**Last Updated:** 2024
**Compliance:** ГОСТ 18855-2013, ISO 281:2007, ISO/TS 16281
