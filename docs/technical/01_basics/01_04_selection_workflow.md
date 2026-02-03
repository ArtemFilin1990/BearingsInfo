# Bearing Selection Workflow

## Purpose
This document provides a systematic approach to selecting the appropriate bearing for a specific application.

## Step-by-Step Selection Process

### Step 1: Define Application Requirements

#### Load Analysis
**Questions to answer:**
- What is the radial load magnitude? (N or kN)
- What is the axial load magnitude? (N or kN)
- Is the load constant or variable?
- What is the load direction (radial, axial, or combined)?
- Are there shock loads or vibrations?

**Calculation:**
```
Equivalent load P = X·Fr + Y·Fa
Where:
  Fr = radial load
  Fa = axial load
  X, Y = load factors (from bearing catalogs)
```

#### Speed Requirements
**Questions to answer:**
- What is the operating speed? (rpm)
- Is the inner ring or outer ring rotating?
- What is the required speed range?

**Calculate:**
```
Mean diameter dm = (d + D) / 2
Speed parameter n·dm (rpm·mm)
```

#### Space Constraints
**Measurements needed:**
- Available shaft diameter (d)
- Available housing bore diameter (D)
- Available axial space (B)
- Any envelope limitations?

#### Operating Conditions
**Environmental factors:**
- Operating temperature range (°C)
- Presence of contaminants (dust, water, chemicals)
- Lubrication possibilities (grease or oil)
- Maintenance accessibility
- Expected service life

### Step 2: Select Bearing Type

#### Primary Selection Based on Load Direction

**Pure Radial Load:**
- Light to moderate load → Deep groove ball bearing
- Heavy load → Cylindrical roller bearing
- Very limited space → Needle roller bearing
- Misalignment expected → Self-aligning ball bearing

**Pure Axial Load:**
- Light to moderate load, high speed → Thrust ball bearing
- Heavy load → Cylindrical roller thrust bearing
- Misalignment expected → Spherical roller thrust bearing

**Combined Radial and Axial Load:**
- Fa/Fr < 0.5, high speed → Deep groove ball bearing
- Fa/Fr > 0.5, precision required → Angular contact ball bearing
- Heavy loads → Tapered roller bearing
- Very heavy loads, misalignment → Spherical roller bearing

#### Secondary Considerations

**If misalignment is present:**
- Angular misalignment 1.5° - 3° → Self-aligning ball bearing
- Angular misalignment 1° - 2.5° → Spherical roller bearing

**If space is limited:**
- Radial space limited → Needle roller bearing
- Axial space limited → Thin section bearing

**If speed is critical:**
- Very high speed (n·dm > 500,000) → Deep groove ball bearing, Angular contact ball bearing
- High speed (n·dm > 300,000) → Cylindrical roller bearing
- Moderate speed (n·dm < 300,000) → Tapered roller bearing, Spherical roller bearing

### Step 3: Determine Bearing Size

#### Required Load Rating Calculation

**Formula:**
```
C = P · (L₁₀h · n · 60 / 10⁶)^(1/p)

Where:
  C = required dynamic load rating (N)
  P = equivalent dynamic load (N)
  L₁₀h = required service life (hours)
  n = rotational speed (rpm)
  p = 3 for ball bearings, 10/3 for roller bearings
```

**Example:**
- Required life: 20,000 hours
- Speed: 1,500 rpm
- Equivalent load: 5,000 N
- Bearing type: Deep groove ball (p = 3)

```
L₁₀ = 20,000 × 1,500 × 60 / 10⁶ = 1,800 million revolutions
C = 5,000 × (1,800)^(1/3) = 5,000 × 12.16 = 60,800 N ≈ 61 kN
```

**Select bearing from catalog with C ≥ 61 kN**

#### Size Selection Process

1. **Start with shaft diameter** - Use standard shaft diameters when possible
2. **Check catalog** - Find bearings with bore diameter d matching shaft
3. **Compare load ratings** - Select bearing with C ≥ required C
4. **Verify dimensions** - Ensure bearing fits in available space
5. **Check speed limit** - Ensure bearing can operate at required speed

### Step 4: Verify Selection

#### Static Load Check

**When required:**
- Slow rotation or oscillation
- Frequent starts/stops
- Heavy shock loads

**Calculation:**
```
P₀ = X₀·Fr + Y₀·Fa ≤ C₀

Where:
  P₀ = equivalent static load (N)
  C₀ = static load rating (N)
  X₀, Y₀ = static load factors
```

**Safety factor:**
- Smooth operation: S₀ = P₀/C₀ ≤ 0.5
- Normal operation: S₀ = P₀/C₀ ≤ 1.0
- Shock loads: S₀ = P₀/C₀ ≤ 1.5

#### Speed Limit Check

**Reference speed (n_ref):**
- Typical limiting speed for grease lubrication
- Found in bearing catalogs

**Thermal speed (n_th):**
- Speed at which thermal equilibrium is reached
- Depends on lubrication method and cooling

**Verification:**
```
Operating speed ≤ n_ref (for grease lubrication)
Operating speed ≤ n_th (for oil lubrication with cooling)
```

#### Fatigue Life Check

**Minimum acceptable life:**
- Household appliances: 300 - 2,000 hours
- Agricultural machinery: 3,000 - 6,000 hours
- Automotive: 2,000 - 5,000 hours (continuous operation)
- Industrial machinery: 20,000 - 30,000 hours (8h/day operation)
- Machine tools: 20,000 - 40,000 hours
- Continuous operation: 40,000 - 100,000 hours

### Step 5: Select Bearing Variant

#### Internal Clearance

**Options:**
- **C2** - clearance less than Normal
- **Normal (CN)** - standard clearance
- **C3** - clearance greater than Normal
- **C4** - clearance greater than C3
- **C5** - clearance greater than C4

**Selection criteria:**
- Tight fits → C3 or C4 (compensates for clearance reduction)
- High temperature → C3 or C4 (compensates for thermal expansion)
- Preload required → C2 or less
- Normal conditions → Normal (CN)

#### Accuracy Class

**ГОСТ / ISO / ABEC:**
- **Class 0 / P0 / ABEC 1** - General machinery
- **Class 6 / P6 / ABEC 3** - Moderate precision
- **Class 5 / P5 / ABEC 5** - Precision applications
- **Class 4 / P4 / ABEC 7** - High precision (machine tools)
- **Class 2 / P2 / ABEC 9** - Ultra-precision

**Selection criteria:**
- Standard machinery → Class 0
- Electric motors, pumps → Class 6
- Machine tool spindles (low speed) → Class 5
- Machine tool spindles (high speed) → Class 4
- Ultra-precision spindles → Class 2

#### Seals and Shields

**Options:**
- **Open** - no protection, external sealing required
- **Z** - one shield (non-contact)
- **ZZ** - two shields (non-contact)
- **RS** - one seal (contact)
- **2RS** - two seals (contact)

**Selection criteria:**
- Clean environment, high speed → Open or Z/ZZ
- Dusty environment → 2RS
- Water exposure → 2RS
- No maintenance required → 2RS (sealed and greased)
- Regreasable → Open or Z/ZZ

#### Cage Material

**Options:**
- **Steel** - standard, economical
- **Brass** - better heat dissipation
- **Polyamide** - lightweight, low noise
- **Phenolic** - high temperature resistance

**Selection criteria:**
- Standard applications → Steel
- High speed, low weight → Polyamide
- High temperature → Brass or Phenolic
- Quiet operation → Polyamide

### Step 6: Define Lubrication

#### Grease Lubrication

**When to use:**
- Simple sealing requirements
- Long relubrication intervals acceptable
- Moderate speeds (n·dm < 300,000 - 500,000)
- Limited maintenance access

**Grease selection:**
- **Lithium-based (Li)** - General purpose, -20°C to +120°C
- **Lithium complex (Li-complex)** - Extended temperature, -30°C to +150°C
- **Polyurea** - Long life, high temperature, -30°C to +180°C
- **High-temp grease** - Special applications, up to +230°C

**NLGI grade:**
- NLGI 2 - most common, general purpose
- NLGI 3 - higher temperatures, vertical shafts

#### Oil Lubrication

**When to use:**
- High speeds (n·dm > 500,000)
- High temperatures
- Heat dissipation required
- Continuous operation with long life

**Methods:**
- **Oil bath** - simple, economical, low to moderate speeds
- **Circulating oil** - high speeds, heat removal
- **Oil mist** - high speeds, minimal friction
- **Oil-air** - precision, minimal oil consumption

### Step 7: Specify Mounting Arrangement

#### Shaft Fit

**Rotating inner ring (typical):**
- Light loads → h6, j6
- Normal loads → k5, k6, m5, m6
- Heavy loads, shock → n6, p6

**Stationary inner ring:**
- All loads → g6, h6

#### Housing Fit

**Rotating outer ring:**
- Light loads → k6, m6
- Normal loads → n6, p6

**Stationary outer ring (typical):**
- All loads → H7, J7
- Thermal expansion compensation → G7

#### Axial Location

**Fixed bearing (locates shaft axially):**
- Tapered roller bearing
- Angular contact bearing
- Deep groove ball bearing with shoulder on both sides

**Free bearing (allows axial displacement):**
- Cylindrical roller bearing (NU, N types)
- Deep groove bearing with clearance on one side

### Step 8: Final Verification

#### Checklist:
- [ ] Bearing type appropriate for load direction
- [ ] Dynamic load rating C ≥ required C
- [ ] Static load rating C₀ adequate
- [ ] Speed within limits
- [ ] Bearing fits in available space
- [ ] Internal clearance appropriate for fits and temperature
- [ ] Accuracy class suitable for application
- [ ] Sealing appropriate for environment
- [ ] Lubrication method defined
- [ ] Mounting arrangement specified
- [ ] Service life meets requirements

## Quick Selection Tables

### By Application Type

| Application | Typical Bearing Type | Notes |
|------------|---------------------|-------|
| Electric motors | Deep groove ball | 6000, 6200 series common |
| Gearboxes | Cylindrical roller, Tapered roller | Depends on load |
| Pumps | Deep groove ball, Angular contact | Consider contamination |
| Compressors | Angular contact, Cylindrical roller | High loads |
| Machine tools | Angular contact, Cylindrical roller | High precision |
| Automotive wheels | Tapered roller, Deep groove ball | Adjustable or sealed |
| Conveyors | Self-aligning ball, Spherical roller | Misalignment common |
| Crushers/Mills | Spherical roller | Very heavy loads |

### By Speed Range (n·dm)

| Speed Range | Suitable Bearing Types |
|------------|------------------------|
| < 100,000 | All types |
| 100,000 - 300,000 | All except spherical roller |
| 300,000 - 500,000 | Ball bearings, Cylindrical roller |
| 500,000 - 1,000,000 | Deep groove ball, Angular contact ball |
| > 1,000,000 | Angular contact ball (special designs) |

### By Load Capacity (relative)

| Load Level | Radial Bearings | Thrust Bearings |
|-----------|----------------|-----------------|
| Very High | Spherical roller | Spherical roller thrust |
| High | Tapered roller, Cylindrical roller | Cylindrical roller thrust |
| Moderate | Deep groove ball (large) | - |
| Light | Deep groove ball (small) | Thrust ball |

## References
- ГОСТ 18854-2013: Ball and Roller Bearings - Static Load Ratings
- ISO 281:2007: Rolling Bearings - Dynamic Load Ratings and Rating Life
- ISO 76:2006: Rolling Bearings - Static Load Ratings
- SKF General Catalogue
- FAG Rolling Bearing Catalogue
