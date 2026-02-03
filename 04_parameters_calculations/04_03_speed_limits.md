# Speed Limits and Thermal Considerations

## Purpose

This document provides comprehensive information on bearing speed limits, thermal speed rating, speed-related parameters, factors affecting maximum operating speed, and solutions for high-speed applications. Understanding speed limitations is critical for preventing thermal damage and ensuring bearing reliability.

---

## 1. Basic Speed Concepts

### 1.1 Speed Terminology

**Rotational Speed (n):**

The number of revolutions per minute of the rotating ring (typically inner ring).

**Units:**
- **rpm** (revolutions per minute) — most common
- **rad/s** (radians per second) — SI unit
- Conversion: ω [rad/s] = 2π · n [rpm] / 60

**Mean Diameter (dm):**

```
dm = (d + D) / 2   [mm]
```

Where:
- d = bearing bore diameter [mm]
- D = bearing outer diameter [mm]

**Speed Parameter (n·dm):**

```
n·dm = rotational speed × mean diameter   [mm·rpm]
```

Critical parameter for:
- Lubrication selection (reference viscosity)
- Speed limit determination
- Centrifugal force effects
- Thermal behavior

### 1.2 Types of Speed Limits

**1. Reference Speed (nref):**
- Thermal equilibrium speed with grease lubrication
- Continuous operation possible
- Standard bearing design, typical mounting

**2. Thermal Speed Rating (nth):**
- Maximum continuous speed with oil lubrication
- Optimized lubrication and cooling
- May require special features

**3. Limiting Speed (nlim):**
- Absolute mechanical limit
- Cage strength and centrifugal forces
- Short-term operation only
- Usually not published (far beyond thermal limits)

**Typical relationship:**

```
nref < nth < nlim

nref ≈ 0.4 - 0.6 · nth (for grease)
nlim ≈ 2 - 3 · nth (approximately)
```

---

## 2. Reference Speed (nref)

### 2.1 Definition

**Reference speed** is the speed at which the bearing operates with a steady-state temperature rise of approximately **50°C above ambient** under the following conditions:

**Standard conditions:**
- Grease lubrication (consistency NLGI 2-3)
- Normal bearing design (not special high-speed version)
- Radial load: P ≈ 0.05 · C (light load)
- Axial load: minimal or none
- Ambient temperature: 20°C
- Typical mounting and housing design
- Natural convection cooling (no forced cooling)

### 2.2 Catalog Values

**ГОСТ and manufacturer catalogs provide nref values for each bearing:**

| Bearing Type | Typical nref Range |
|--------------|-------------------|
| **Deep groove ball** (small) | 15,000 - 30,000 rpm |
| **Deep groove ball** (medium) | 8,000 - 15,000 rpm |
| **Deep groove ball** (large) | 3,000 - 8,000 rpm |
| **Angular contact ball** | 10,000 - 25,000 rpm |
| **Cylindrical roller** | 5,000 - 12,000 rpm |
| **Tapered roller** | 2,500 - 6,000 rpm |
| **Spherical roller** | 2,000 - 5,000 rpm |
| **Thrust ball** | 3,000 - 8,000 rpm |
| **Needle roller** | 8,000 - 15,000 rpm |

**General trend:**
- Smaller bearings → higher nref
- Ball bearings → higher than roller bearings
- Low friction designs → higher nref

### 2.3 Correction Factors for nref

**Actual permissible speed:**

```
nperm = nref · f1 · f2 · f3 · f4
```

Where:
- **f1** = load factor
- **f2** = lubrication factor
- **f3** = cooling factor
- **f4** = bearing design factor

#### Load Factor (f1)

Higher loads → more friction → more heat → lower speed

**Table: Load factor f1**

| P/C | f1 |
|-----|-----|
| 0.01 | 1.3 |
| 0.05 | 1.0 (reference) |
| 0.10 | 0.75 |
| 0.15 | 0.60 |
| 0.20 | 0.50 |
| 0.30 | 0.35 |

**Formula (approximate):**

```
f1 ≈ (0.05 / (P/C))^0.3
```

#### Lubrication Factor (f2)

**Grease:**
- Standard grease (NLGI 2): f2 = 1.0 (reference)
- High-speed grease: f2 = 1.2 - 1.5
- Heavy grease (NLGI 4): f2 = 0.7 - 0.8

**Oil:**
- Oil bath (correct level): f2 = 1.5 - 2.0
- Oil mist: f2 = 2.0 - 3.0
- Oil-air lubrication: f2 = 3.0 - 5.0
- Jet lubrication (cooling): f2 = 4.0 - 8.0

#### Cooling Factor (f3)

**Natural convection:** f3 = 1.0 (reference)

**Improved cooling:**
- Forced air cooling: f3 = 1.2 - 1.5
- Water-cooled housing: f3 = 1.5 - 2.5
- Oil cooling circulation: f3 = 2.0 - 4.0

#### Bearing Design Factor (f4)

**Standard bearing:** f4 = 1.0

**Special designs:**
- Low friction seals (Z type): f4 = 1.1 - 1.2
- Non-contact seals: f4 = 1.3 - 1.5
- Open bearings (no seals): f4 = 1.5 - 2.0
- High-speed design (optimized): f4 = 1.5 - 3.0
- Ceramic hybrid bearings: f4 = 2.0 - 5.0

---

## 3. Thermal Speed Rating (nth)

### 3.1 Definition

**Thermal speed rating** represents the maximum speed at which the bearing can operate continuously with adequate oil lubrication and heat dissipation, maintaining acceptable operating temperature (typically < 90-100°C).

**Assumptions:**
- Optimized oil lubrication (oil-air, jet, or circulating)
- Effective cooling system
- Open bearing or non-contact seals
- Light to moderate load
- Proper mounting and alignment

**Typical values (SKF convention):**

```
nth ≈ 1.5 - 2.5 · nref   (for oil vs grease)
```

### 3.2 Factors Affecting Thermal Speed

**Heat generation sources:**

1. **Rolling friction:** Hysteresis losses in rolling contact
2. **Sliding friction:** Cage/race contact, ball/cage contact
3. **Lubricant churning:** Viscous drag
4. **Seal friction:** Contact seals generate significant heat

**Heat dissipation paths:**

1. **Conduction:** Through shaft and housing
2. **Convection:** Air or oil flow
3. **Radiation:** Minor at bearing temperatures

**Thermal equilibrium:**

```
Heat generated = Heat dissipated
```

When generated heat exceeds dissipation capacity:
- Temperature rises
- Lubricant viscosity decreases
- Increased wear, oxidation
- Potential thermal runaway → seizure

---

## 4. Speed Parameter (n·dm)

### 4.1 Definition and Importance

**Speed parameter:**

```
n·dm = n [rpm] · dm [mm]
```

Where:
```
dm = (d + D) / 2
```

**Physical meaning:**

Represents circumferential velocity at pitch diameter:

```
v = π · dm · n / 60000   [m/s]
```

**Critical applications:**

1. **Lubrication selection:** Reference viscosity ν₁ depends on n·dm
2. **Centrifugal effects:** Cage stress, ball loading
3. **Thermal behavior:** Heat generation rate
4. **Design limits:** Mechanical constraints

### 4.2 Speed Parameter Ranges

**Typical ranges for different bearing types:**

| Bearing Type | Typical n·dm max [mm·rpm] |
|--------------|---------------------------|
| **Deep groove ball (standard)** | 300,000 - 500,000 |
| **Deep groove ball (high-speed)** | 1,000,000 - 2,000,000 |
| **Angular contact ball (single)** | 500,000 - 1,000,000 |
| **Angular contact ball (paired)** | 400,000 - 800,000 |
| **Cylindrical roller** | 300,000 - 600,000 |
| **Tapered roller** | 150,000 - 350,000 |
| **Spherical roller** | 150,000 - 300,000 |
| **Thrust ball** | 150,000 - 300,000 |
| **Ceramic hybrid ball** | 2,000,000 - 3,000,000+ |

**Example:**

Bearing 6208:
- d = 40 mm, D = 80 mm
- dm = 60 mm
- nref = 10,000 rpm

```
n·dm = 10,000 · 60 = 600,000 mm·rpm
```

At reference speed, this is near upper limit for standard deep groove ball bearing.

---

## 5. Factors Affecting Speed Limits

### 5.1 Bearing Type and Design

**Ball vs Roller:**

Ball bearings generally faster because:
- Lower sliding friction
- Lower mass → less centrifugal force
- Point contact → lower friction torque

**Contact angle:**

Higher contact angle (angular contact bearings):
- Higher gyroscopic moments on balls
- More sliding at ball/race contact
- Generally lower speed than radial contact

**Cage design:**

Critical for high speed:
- **Machined brass/bronze cage:** good to moderate speed
- **Pressed steel cage:** standard speeds
- **Phenolic/polyamide cage:** high speed, low mass
- **Machined light alloy cage:** very high speed
- **Ceramic cage:** extreme speed

### 5.2 Lubrication Method

**Speed capability by lubrication type:**

| Lubrication Type | Relative Speed Factor | Typical nmax/nref |
|------------------|----------------------|------------------|
| **Grease (standard)** | 1.0 | 1.0 |
| **Grease (high-speed)** | 1.3 | 1.3 |
| **Oil bath** | 1.5 - 2.0 | 1.5 - 2.0 |
| **Oil jet (cooling)** | 2.5 - 4.0 | 2.5 - 4.0 |
| **Oil mist** | 2.5 - 3.5 | 2.5 - 3.5 |
| **Oil-air** | 3.0 - 5.0 | 3.0 - 5.0 |
| **Under-race lubrication** | 5.0 - 8.0 | 5.0 - 8.0 |

**Lubrication viscosity:**

Lower viscosity at high speed:
- Reduces churning losses
- Maintains adequate film thickness
- Prevents excessive temperature rise

**Rule of thumb:**

```
Use ν₁ (reference viscosity) or slightly higher
Avoid excessive viscosity → heat generation
```

### 5.3 Seals and Shields

**Effect on speed:**

| Configuration | Speed Impact |
|--------------|--------------|
| **Open bearing** | 100% (reference) |
| **Metal shields (Z, ZZ)** | 90 - 95% |
| **Non-contact seals (RZ)** | 80 - 90% |
| **Contact seals (RS)** | 50 - 70% |
| **High-contact seals (2RS)** | 40 - 60% |

**Seal friction generates significant heat at high speed.**

**High-speed applications:** Use open bearings or non-contact seals.

### 5.4 Load

**Radial and axial loads increase friction and heat:**

- Light load (P < 0.05·C): Near full speed capability
- Moderate load (P ≈ 0.1·C): Reduce speed to 70-80% of nref
- Heavy load (P > 0.2·C): Reduce speed to 40-50% of nref

**Load distribution:**

Uniform load distribution → lower friction
High peak loads → localized heating → speed reduction required

### 5.5 Bearing Size

**Centrifugal forces:**

```
Fc = m · ω² · r
```

Where:
- m = ball/roller mass
- ω = angular velocity
- r = pitch radius

Larger bearings:
- Higher mass
- Higher centrifugal forces
- Lower maximum speed

**Typical nref vs bore diameter (deep groove ball):**

| Bore Diameter d [mm] | Typical nref [rpm] |
|---------------------|-------------------|
| 10 | 28,000 |
| 20 | 19,000 |
| 30 | 14,000 |
| 50 | 10,000 |
| 80 | 7,000 |
| 100 | 5,600 |
| 150 | 4,000 |
| 200 | 3,200 |

**Approximate relationship:**

```
nref ∝ d^(-0.5 to -0.7)
```

### 5.6 Temperature

**Operating temperature affects:**

1. **Lubricant viscosity:** Decreases with temperature
2. **Clearance:** Increases with temperature (differential expansion)
3. **Material properties:** Hardness, fatigue resistance
4. **Dimensional stability:** Thermal growth

**High temperature effects:**

- T < 120°C: Normal operation
- T = 120-150°C: Reduced life, special lubricant required
- T = 150-200°C: Significant life reduction, high-temp bearings needed
- T > 200°C: Special materials (ceramics, high-temp steel)

**Speed must be reduced if temperature exceeds limits.**

---

## 6. Temperature Rise Considerations

### 6.1 Heat Balance Equation

**Steady-state heat balance:**

```
Q_generated = Q_dissipated
```

**Heat generated:**

```
Q = M · n / 9550   [W]
```

Where:
- M = friction torque [Nmm]
- n = speed [rpm]

**Heat dissipated:**

```
Q = k · A · ΔT   [W]
```

Where:
- k = overall heat transfer coefficient [W/m²K]
- A = heat transfer area [m²]
- ΔT = temperature rise [K]

### 6.2 Friction Torque Components

**Total friction torque:**

```
M = M₀ + M₁
```

**M₀** = load-independent torque (lubricant viscosity, seals):

```
M₀ = 10^(-7) · f₀ · (ν · n)^(2/3) · dm³   [Nmm]
```

Where:
- f₀ = bearing type factor
- ν = kinematic viscosity [mm²/s]
- n = speed [rpm]
- dm = mean diameter [mm]

**M₁** = load-dependent torque:

```
M₁ = f₁ · P · dm   [Nmm]
```

Where:
- f₁ = load factor (depends on bearing type, load)
- P = equivalent load [N]
- dm = mean diameter [mm]

**Seal friction (if present):**

```
Ms = seal friction moment [Nmm]
```

Can be significant, especially at high speed.

### 6.3 Temperature Rise Calculation

**Simplified approach:**

```
ΔT = Q / (k · A)
```

**Typical k values:**
- Natural convection, air: 10 - 20 W/m²K
- Forced air cooling: 30 - 60 W/m²K
- Oil cooling: 100 - 300 W/m²K
- Water cooling: 500 - 2000 W/m²K

**Acceptable temperature rise:**

| Application | Max ΔT | Max T_bearing |
|-------------|--------|--------------|
| **Standard machinery** | 40 - 50°C | 70 - 80°C |
| **Continuous operation** | 50 - 60°C | 80 - 90°C |
| **Short-term** | 60 - 80°C | 90 - 110°C |
| **High-temp design** | 80 - 100°C | 110 - 150°C |

**If calculated ΔT exceeds limit → reduce speed or improve cooling.**

---

## 7. Speed Limits by Bearing Type

### 7.1 Deep Groove Ball Bearings

**Characteristics:**
- Highest speed capability among standard bearings
- Low friction
- Suitable for grease or oil lubrication

**Typical nref (grease):**

| Series | Size d [mm] | Typical nref [rpm] |
|--------|-------------|-------------------|
| 60 | 10 - 30 | 18,000 - 28,000 |
| 62 | 15 - 50 | 12,000 - 18,000 |
| 63 | 17 - 60 | 10,000 - 15,000 |
| 64 | 20 - 80 | 7,000 - 11,000 |

**High-speed versions (suffix):**
- Suffix HT: Higher temperature, better balance
- Suffix VH: Very high speed (nth up to 2× standard)

### 7.2 Angular Contact Ball Bearings

**Single row:**
- Good high-speed capability
- Contact angle α = 15° - 40°
- Lower α → higher speed capability

**Paired arrangements:**
- Back-to-back (DB, O): Moderate speed
- Face-to-face (DF, X): Similar to DB
- Tandem (DT, II): Slightly lower due to friction

**Typical nref (single, α = 15°):**

| Size d [mm] | nref [rpm] |
|-------------|-----------|
| 20 - 30 | 14,000 - 18,000 |
| 40 - 60 | 9,000 - 12,000 |
| 80 - 100 | 5,500 - 7,000 |

**Precision classes (P5, P4):**
- Better balance
- nref up to 1.5× standard

### 7.3 Cylindrical Roller Bearings

**Lower speed than ball bearings:**
- Higher sliding friction
- Higher mass (rollers heavier than balls)
- Cage design critical

**Typical nref:**

| Size d [mm] | nref [rpm] |
|-------------|-----------|
| 30 - 50 | 8,000 - 12,000 |
| 60 - 100 | 5,000 - 8,000 |
| 120 - 200 | 3,000 - 5,000 |

**Design variations:**
- NU, NJ: Standard speed
- NUP: Slightly lower (integrated rib)
- Precision class P5: +20-30% speed

### 7.4 Tapered Roller Bearings

**Moderate speed capability:**
- Significant sliding friction
- Contact angle creates gyroscopic moments
- Typically grease lubricated

**Typical nref:**

| Bearing Size | nref [rpm] |
|-------------|-----------|
| Small (d < 50 mm) | 4,000 - 7,000 |
| Medium (d = 50-100 mm) | 2,500 - 4,500 |
| Large (d > 100 mm) | 1,500 - 3,000 |

**Automotive wheel bearings:**
- Special high-speed versions
- nref up to 8,000 - 10,000 rpm (small sizes)

### 7.5 Spherical Roller Bearings

**Low to moderate speed:**
- Complex kinematics (roller tilt)
- High sliding friction
- Large mass

**Typical nref:**

| Size d [mm] | nref [rpm] |
|-------------|-----------|
| 40 - 80 | 3,000 - 5,000 |
| 100 - 200 | 1,800 - 3,000 |
| 250 - 400 | 1,000 - 1,800 |

**Self-aligning capability essential, but limits speed.**

### 7.6 Thrust Bearings

**Ball thrust bearings:**
- Moderate speed
- Centrifugal forces on balls

**Typical nref:**

| Type | nref Range [rpm] |
|------|------------------|
| Single direction | 3,000 - 8,000 |
| Double direction | 2,500 - 6,000 |

**Roller thrust bearings:**
- Low speed only
- High sliding friction

**Typical nref:**
- 1,000 - 3,000 rpm (depending on size)

---

## 8. High-Speed Bearing Solutions

### 8.1 High-Speed Bearing Design Features

**Optimized internal geometry:**
- Reduced contact angle (ball bearings)
- Lighter weight balls/rollers
- Optimized raceway curvature
- Minimal sliding

**Advanced cage designs:**
- Phenolic resin (low mass, good strength)
- Machined aluminum/titanium (very low mass)
- Ceramic cages (extreme conditions)
- Optimized pocket design (minimal friction)

**Precision class:**
- P4, P2 (ISO) or Class 2, 0 (ГОСТ)
- Better balance → less vibration
- Tighter tolerances → stable operation

**Special materials:**
- Hybrid bearings (ceramic balls, steel races)
- Full ceramic bearings (extreme speed/temperature)
- Vacuum-degassed steel (cleaner, longer life)

### 8.2 Ceramic Hybrid Bearings

**Construction:**
- Silicon nitride (Si₃N₄) balls
- Steel races (typically 52100/100Cr6)

**Advantages:**
- Lower density: 40% lighter than steel balls
- Higher stiffness: 50% higher modulus
- Lower centrifugal force: enables higher speed
- Better lubrication: smoother surface
- Electrical isolation: prevents bearing currents
- Corrosion resistant

**Speed capability:**
- 2× to 5× higher than standard steel bearings
- n·dm up to 2-3 million mm·rpm

**Applications:**
- Machine tool spindles
- Turbomachinery
- High-speed motors
- Racing and aerospace

**Limitations:**
- Higher cost (3-10× steel bearings)
- Requires precision mounting
- Not suitable for heavy shock loads

### 8.3 Advanced Lubrication Systems

**Oil-air lubrication:**

Principle: Compressed air + metered oil droplets
- Minimal lubricant quantity → low churning losses
- Effective cooling
- Speed factor: 3-5× grease reference speed

**Under-race lubrication:**

Oil supplied directly to raceway through holes in outer race
- Excellent cooling
- Very high speed capability
- Common in turbomachinery

**Oil jet lubrication:**

High-velocity oil jet directed at bearing
- Removes heat effectively
- Speed factor: 4-8× grease reference

**Mist lubrication:**

Fine oil mist in airstream
- Clean, efficient
- Speed factor: 2.5-3.5× grease reference

### 8.4 Cooling Methods

**Natural convection:**
- Standard housings
- Limited heat dissipation

**Forced air cooling:**
- Fans, blowers
- Moderate improvement

**Oil cooling:**
- Circulating oil through housing
- High heat dissipation

**Water-cooled housings:**
- Water jackets around bearing housing
- Highest heat dissipation
- Used in high-power applications

### 8.5 Special Bearing Arrangements

**Duplex/triplex arrangements:**
- Multiple bearings in series
- Distributes load
- Improves rigidity
- May reduce maximum speed

**Preload:**
- Light preload improves stability at high speed
- Reduces skidding
- But increases friction → careful optimization needed

**Bearing spacing:**
- Wider spacing reduces moment loads
- But increases shaft flexibility

---

## 9. Practical Examples

### 9.1 Example 1: Standard Deep Groove Ball Bearing

**Given:**
- Bearing: 6208
- Catalog: nref = 10,000 rpm (grease)
- Load: P/C = 0.08
- Lubrication: Standard grease NLGI 2
- Cooling: Natural convection

**Question:** Maximum permissible speed?

**Solution:**

```
f1 (load): P/C = 0.08 → f1 ≈ 0.8
f2 (grease): standard → f2 = 1.0
f3 (cooling): natural → f3 = 1.0
f4 (design): standard → f4 = 1.0

nperm = nref · f1 · f2 · f3 · f4
nperm = 10,000 · 0.8 · 1.0 · 1.0 · 1.0
nperm = 8,000 rpm
```

**Recommendation:** Operate at ≤ 8,000 rpm.

### 9.2 Example 2: High-Speed Oil Lubrication

**Given:**
- Same bearing: 6208, nref = 10,000 rpm
- Load: P/C = 0.05 (light)
- Lubrication: Oil jet cooling
- Cooling: Effective oil cooling
- Design: Open bearing (no seals)

**Solution:**

```
f1 (light load): P/C = 0.05 → f1 = 1.0
f2 (oil jet): f2 = 4.0
f3 (oil cooling): f3 = 2.0
f4 (open bearing): f4 = 1.5

nperm = 10,000 · 1.0 · 4.0 · 2.0 · 1.5
nperm = 120,000 rpm (theoretical)
```

**Reality check:**
- dm = 60 mm
- n·dm = 120,000 · 60 = 7,200,000 mm·rpm

This exceeds typical limit for standard bearing. Practical limit ≈ 40,000 - 50,000 rpm with excellent lubrication.

**Recommendation:** Use high-speed design or hybrid bearing for speeds > 40,000 rpm.

### 9.3 Example 3: Tapered Roller Bearing

**Given:**
- Bearing: 32208
- Catalog: nref = 3,800 rpm
- Load: P/C = 0.15
- Lubrication: Grease
- Application: Gearbox

**Solution:**

```
f1 (load): P/C = 0.15 → f1 ≈ 0.6
f2, f3, f4 = 1.0 (standard conditions)

nperm = 3,800 · 0.6 = 2,280 rpm
```

**Recommendation:** Operate at ≤ 2,200 rpm.

### 9.4 Example 4: Machine Tool Spindle

**Given:**
- Required speed: 24,000 rpm
- Bearing size: d = 50 mm, D = 80 mm
- Light load, precision machining

**Design selection:**

Option 1: Standard deep groove ball 6010
- nref ≈ 11,000 rpm
- Insufficient even with oil

Option 2: Angular contact ball 7010 ACDGA/P4A
- High-speed design (suffix A)
- Precision P4
- Ceramic hybrid (suffix CDGA)
- Oil-air lubrication

**Speed check:**

```
dm = (50 + 80) / 2 = 65 mm
n·dm = 24,000 · 65 = 1,560,000 mm·rpm
```

With ceramic hybrid + oil-air: Acceptable for n·dm < 2,000,000.

**Conclusion:** Option 2 suitable with proper lubrication and cooling.

---

## 10. Monitoring and Troubleshooting

### 10.1 Temperature Monitoring

**Critical parameters:**
- Bearing outer ring temperature
- Housing temperature
- Lubricant temperature

**Warning signs:**
- Temperature > 90°C: Investigate
- Temperature > 100°C: Reduce speed or improve cooling
- Temperature > 120°C: Stop immediately, risk of failure

**Monitoring methods:**
- Thermocouples embedded in housing
- IR sensors (non-contact)
- Temperature-sensitive paints/labels

### 10.2 Vibration Analysis

**Frequency spectrum:**
- Fundamental bearing frequencies (BPFO, BPFI, BSF, FTF)
- Elevated vibration at high frequency: Poor lubrication, wear

**Trending:**
- Gradual increase: Normal wear
- Sudden increase: Possible damage, check immediately

### 10.3 Common High-Speed Problems

**Overheating:**
- Cause: Excessive speed, inadequate lubrication, high load, seal friction
- Solution: Reduce speed, improve cooling, optimize lubrication

**Skidding:**
- Cause: Insufficient load, high speed, poor lubrication
- Solution: Apply minimum load, ensure adequate lubrication film

**Cage failure:**
- Cause: Excessive centrifugal force, poor lubrication, unbalance
- Solution: Reduce speed, use high-speed cage design

**Lubricant breakdown:**
- Cause: High temperature, oxidation
- Solution: Synthetic lubricant, better cooling, shorten relubrication interval

---

## 11. Standards and References

### 11.1 ГОСТ Standards

**ГОСТ 18854** — Load ratings
- Includes friction torque calculations

**ГОСТ 520** — General technical requirements
- Operating temperature limits
- Speed considerations

### 11.2 ISO Standards

**ISO 15312:2003** — Rolling bearings — Thermal speed rating
- Calculation methods
- Reference conditions

**ISO/TR 14179-1** — Lubrication reference speeds
- Relationship between lubrication and speed

**ISO 281** — Dynamic load ratings and rating life
- Lubrication parameter κ vs speed

### 11.3 Manufacturer Guidelines

**SKF:**
- Speed rating tables
- nref and nth values
- High-speed bearing designs

**NSK, NTN, FAG, Timken:**
- Similar rating systems
- Application-specific recommendations

---

## 12. Summary

### 12.1 Key Concepts

1. **Reference speed (nref):** Grease lubrication, standard conditions, 50°C rise
2. **Thermal speed (nth):** Oil lubrication, optimized cooling
3. **Speed parameter (n·dm):** Critical for lubrication and design limits
4. **Temperature rise:** Must remain within acceptable limits

### 12.2 Correction Factors

```
nperm = nref · f_load · f_lub · f_cool · f_design
```

Each factor can significantly affect maximum speed.

### 12.3 High-Speed Solutions

- **Lubrication:** Oil-air, oil jet, mist
- **Design:** High-speed cages, precision class
- **Materials:** Ceramic hybrids
- **Cooling:** Forced air, oil, water

### 12.4 Practical Guidelines

1. **Always check catalog nref** for specific bearing
2. **Apply correction factors** based on actual conditions
3. **Verify temperature rise** in operation
4. **Use appropriate lubrication** for speed range
5. **Consider high-speed designs** for demanding applications

---

## 13. Conclusion

Speed limits are critical constraints in bearing selection and application. Understanding:
- Reference speed and thermal rating
- Speed parameter (n·dm) and its implications
- Factors affecting speed (load, lubrication, seals, design)
- High-speed solutions (materials, lubrication, cooling)

Enables safe, reliable operation at required speeds while avoiding thermal damage, premature wear, and catastrophic failure.

**Next Steps:**
- See [04_01_load_ratings.md](04_01_load_ratings.md) for load calculations
- See [04_02_life_calculations.md](04_02_life_calculations.md) for bearing life
- See [04_04_clearance_preload.md](04_04_clearance_preload.md) for clearance/preload

---

**Document Status:** ✔ Complete
**Last Updated:** 2024
**Compliance:** ГОСТ 520, ISO 15312:2003, ISO/TR 14179-1
