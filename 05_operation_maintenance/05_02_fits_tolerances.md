# Bearing Fits and Tolerances

## Purpose
This document provides comprehensive guidance on fits and tolerances for bearing mounting, including ISO tolerance systems, fit selection criteria, calculations, and practical guidelines for different operating conditions.

## ISO Tolerance System Overview

### Basic Principles

**ISO 286-1 and ISO 286-2:**
- International standard for limits and fits
- Applies to both shafts and holes
- ГОСТ 25347-82 is the Russian equivalent

**Fundamental Deviation:**
- Designated by letter (uppercase for holes, lowercase for shafts)
- Determines position of tolerance zone relative to zero line

**IT Grade (International Tolerance Grade):**
- Designated by number (IT01 to IT18)
- Determines size of tolerance zone
- Lower number = tighter tolerance

### Tolerance Zones for Shafts

**Common shaft tolerance classes for bearings:**

| Tolerance | Character | Fit Type | Application |
|-----------|-----------|----------|-------------|
| h5, h6 | Loose | Clearance | Stationary load, easy mounting |
| j5, j6 | Snug | Transition | Light loads, easy assembly |
| k5, k6 | Tight | Transition/Interference | Moderate loads, normal conditions |
| m5, m6 | Firm | Interference | Normal to heavy loads |
| n6 | Strong | Interference | Heavy loads, shock/vibration |
| p6 | Very tight | Interference | Very heavy loads, high precision |
| r6, r7 | Extra tight | Interference | Extreme loads (rarely used) |

**h6 - Most Common for Clearance Fits:**
- Zero fundamental deviation
- Tolerance zone entirely below zero line
- Easy assembly/disassembly

**k6 - Most Common for Interference Fits (Normal Loads):**
- Slight interference
- Suitable for most rotating load applications
- Good compromise between hold and mounting ease

**m6 - Heavy Loads:**
- Medium interference
- For heavy rotating loads
- Requires press or thermal mounting

### Tolerance Zones for Housings

**Common housing tolerance classes for bearings:**

| Tolerance | Character | Fit Type | Application |
|-----------|-----------|----------|-------------|
| G7 | Loose | Clearance | Displacement required, thermal expansion |
| H6, H7 | Normal | Clearance | Stationary load, standard housing |
| J7, J6 | Snug | Transition | Light loads with locating |
| K7, K6 | Tight | Transition/Interference | Moderate loads, thin-wall housings |
| M7, M6 | Firm | Interference | Heavy loads, solid housings |
| N7, N6 | Strong | Interference | Very heavy loads, shock loads |
| P7 | Very tight | Interference | Extreme loads (rarely used) |

**H7 - Most Common for Housings:**
- Zero fundamental deviation
- Tolerance zone entirely above zero line
- Standard for most applications

**M7 - For Heavy Loads:**
- Light interference
- Prevents outer ring creep
- Solid housing required

### IT Grades Commonly Used

**For Bearing Seats:**

| Grade | Tolerance Level | Application |
|-------|----------------|-------------|
| IT5 | Very precise | Precision bearings, tight fits |
| IT6 | Precise | Standard bearing seats |
| IT7 | Normal | General purpose housings |
| IT8 | Coarse | Non-critical applications |

**Typical Combinations:**
- Shaft: h6, j6, k6, m6, n6 (IT6)
- Shaft (precision): h5, j5, k5, m5 (IT5)
- Housing: H7, J7, K7, M7, N7 (IT7)
- Housing (precision): H6, J6, K6, M6 (IT6)

## Fit Selection Based on Load Conditions

### Load Direction

**Rotating Load (Circumferential):**
- Load rotates relative to ring
- Ring must have interference fit
- Prevents ring creep on seat

**Stationary Load (Point Load):**
- Load stationary relative to ring
- Ring can have clearance fit
- Easier assembly/disassembly

**Indeterminate Load:**
- Direction varies or unknown
- Treat as rotating load (safer)

### Shaft Fits - Selection Guide

#### For Inner Ring (Typical Scenarios)

**Clearance Fit (h5, h6):**

**When to Use:**
- Outer ring rotates, inner ring stationary
- Axial displacement needed (free bearing arrangement)
- Temperature differences (thermal expansion)
- Easy dismounting required
- Very light loads

**Examples:**
- Idler pulleys (outer ring rotating)
- Tapered roller bearings (adjusted arrangement)
- High-temperature applications with thermal expansion

**Disadvantages:**
- Ring may creep under heavy load
- Not suitable for shock/vibration

---

**Transition Fit (j5, j6, k5, k6):**

**When to Use:**
- Light to moderate loads
- Direction load or light rotating load
- Normal operating conditions
- Thin-walled shafts
- Easy assembly still needed

**k5, k6 Most Common:**
- **Small bearings (d < 40 mm):** k5
- **Medium/large bearings (d ≥ 40 mm):** k6
- General-purpose rotating load
- Electric motors, pumps, fans

**Examples:**
- Electric motor shafts
- Standard industrial applications
- Fan bearings

---

**Interference Fit (m5, m6, n6, p6):**

**m5, m6 - Normal to Heavy Loads:**

**When to Use:**
- Rotating loads (normal)
- Solid steel shafts
- Heavy loads without shock
- Standard industrial machinery

**Examples:**
- Gearbox shafts
- Pump shafts (heavy duty)
- Machine tool spindles

**n6 - Heavy Loads, Shock, Vibration:**

**When to Use:**
- Heavy rotating loads
- Shock loads
- Vibration
- Hollow shafts
- High precision required

**Examples:**
- Railway axleboxes
- Heavy machinery
- Construction equipment
- Vibrating screens

**p6 - Very Heavy Loads:**

**When to Use:**
- Extreme loads
- Very heavy shock
- Large bearings on solid shafts
- High precision applications

**Examples:**
- Rolling mill bearings
- Large crusher bearings
- Heavy-duty industrial equipment

**Warning:** Very tight - requires heating or heavy press

### Housing Fits - Selection Guide

#### For Outer Ring (Typical Scenarios)

**Clearance Fit (G7, H7):**

**H7 - Standard Housing Fit:**

**When to Use:**
- Inner ring rotates, outer ring stationary
- Normal point load conditions
- Temperature differences
- Axial displacement needed
- Easy assembly/disassembly

**Examples:**
- Most industrial bearings
- Electric motors (standard)
- Pumps with stationary outer ring
- Standard machine applications

**This is the most common housing fit (>80% of applications)**

**G7 - Loose Fit:**

**When to Use:**
- Axial displacement required
- High temperature differences
- Adjustable bearing arrangements
- Thin-wall housings (sheet metal)

**Examples:**
- Floating bearing arrangements
- High-temperature applications
- Lightweight housings

---

**Transition Fit (J7, K7):**

**When to Use:**
- Light loads with direction changing
- Thin-wall housings with some load
- Split housings

**Less common for outer rings**

---

**Interference Fit (M7, N7, P7):**

**M7 - Light Interference:**

**When to Use:**
- Outer ring rotating
- Heavy point loads with shock
- Thin-wall housings (aluminum, cast iron)
- Preventing outer ring creep

**Examples:**
- Wheel hubs (outer ring rotating)
- Heavy vibration applications
- Thin-wall cast housings under load

**N7 - Medium Interference:**

**When to Use:**
- Heavy rotating outer ring
- Very heavy point loads
- Solid housings (steel, heavy cast iron)
- High shock loads on stationary ring

**Examples:**
- Heavy-duty wheel hubs
- Railway applications
- Large vibrating machinery

**P7 - Strong Interference:**

**Rarely used - extreme applications only**

### Fit Selection Tables

#### Shaft Fits by Load and Bearing Size

**Ball Bearings and Cylindrical Roller Bearings:**

| Load Type | d ≤ 40 mm | 40 < d ≤ 100 mm | 100 < d ≤ 200 mm | d > 200 mm |
|-----------|-----------|----------------|-----------------|------------|
| **Point load** | h5 | h6 | h6 | h6 |
| **Light rotating** | j5 | j6 | j6 | j6 |
| **Normal rotating** | k5 | k6 | k6 | k6 |
| **Heavy rotating** | m5 | m6 | m6 | m6 |
| **Very heavy + shock** | n6 | n6 | n6 | n6 |
| **Extreme load** | p6 | p6 | p6 | p6 |

**Tapered and Spherical Roller Bearings:**

| Load Type | d ≤ 100 mm | 100 < d ≤ 200 mm | d > 200 mm |
|-----------|-----------|-----------------|------------|
| **Point load** | h6 | h6 | h6 |
| **Light rotating** | j6 | j6 | j6 |
| **Normal rotating** | k6 | m6 | m6 |
| **Heavy rotating** | m6 | n6 | n6 |
| **Very heavy + shock** | n6 | p6 | p6 |

**Note:** Roller bearings generate higher loads on seats due to line contact

#### Housing Fits by Load and Bearing Type

**Ball Bearings:**

| Load Type | Solid Housing | Thin-Wall Housing | Light Alloy Housing |
|-----------|--------------|-------------------|-------------------|
| **Point load** | H7 | H7 | H7 |
| **Light load direction** | H7 | J7 | J7 |
| **Rotating outer ring** | K7 | M7 | M7 |
| **Heavy point load + shock** | K7 | M7 | M7 |
| **Heavy rotating** | M7 | N7 | N7 |

**Roller Bearings:**

| Load Type | Solid Housing | Thin-Wall Housing | Light Alloy Housing |
|-----------|--------------|-------------------|-------------------|
| **Point load** | H7 | J7 | K7 |
| **Light load direction** | J7 | K7 | K7 |
| **Rotating outer ring** | M7 | N7 | N7 |
| **Heavy point load + shock** | M7 | N7 | P7 |
| **Heavy rotating** | N7 | P7 | P7 |

**Note:** Roller bearings require tighter housing fits than ball bearings

### Special Considerations

**Thin-Wall Housings:**
- Cast iron, aluminum, plastic
- Wall thickness < 0.1 × D (outer diameter)
- Require tighter fit (one grade tighter)
- M7 instead of K7, N7 instead of M7

**Hollow Shafts:**
- Require tighter fit (one grade tighter)
- m6 instead of k6, n6 instead of m6
- Shaft expands under interference

**High Temperature (>100°C):**
- Shaft expands more than housing
- Reduce interference or use clearance
- Consider thermal expansion coefficient

**Split Housings:**
- Tighter fit recommended
- K7 or M7 instead of H7
- Prevents movement at split line

## Interference and Clearance Calculations

### Effective Interference

**Definition:**
The actual interference between bearing ring bore and shaft (or OD and housing) considering:
- Nominal fit interference
- Surface roughness
- Elastic deformation

**Formula:**
```
δeff = δnom - (Rzi + Rza)
```

Where:
- δeff = effective interference (μm)
- δnom = nominal interference from ISO tables (μm)
- Rzi = roughness height of bore/shaft (μm) ≈ 2-4 μm
- Rza = roughness height of mating surface (μm) ≈ 2-4 μm

**Typical Surface Roughness:**
- Bearing bore: Ra 0.4 μm (Rz ≈ 2.5 μm)
- Shaft: Ra 0.8-1.6 μm (Rz ≈ 4-8 μm)

**Effective interference is reduced by ~4-8 μm from nominal**

### Radial Interference Expansion

When bearing is mounted with interference, the bore expands:

**Inner Ring Bore Expansion:**
```
Δd = δeff × (d/s) × [(D² + d²)/(D² - d²)]
```

Where:
- Δd = diametral bore expansion (μm)
- δeff = effective interference (μm)
- d = bearing bore diameter (mm)
- D = bearing outer diameter (mm)
- s = ring thickness = (D - d) / 2

**Simplified for Typical Bearings:**
```
Δd ≈ (1.5 to 2.5) × δeff
```

**Effect on Internal Clearance:**
- Radial internal clearance reduced by ≈ 0.8 × Δd
- Must select bearing with adequate initial clearance

### Fit Tolerance Examples

**Example: 6308 Bearing on k6 Shaft**

**Bearing:** 6308
- Bore (d) = 40 mm
- OD (D) = 90 mm

**Shaft: 40 k6**
- Upper limit: 40.000 + 0.018 = 40.018 mm
- Lower limit: 40.000 + 0.002 = 40.002 mm

**Bearing bore tolerance (normal class):**
- Upper limit: 40.000 mm
- Lower limit: 40.000 - 0.012 = 39.988 mm

**Interference range:**
- Maximum: 40.018 - 39.988 = **0.030 mm = 30 μm**
- Minimum: 40.002 - 40.000 = **0.002 mm = 2 μm**

**Effective interference (accounting for roughness ~6 μm):**
- Maximum effective: 30 - 6 = **24 μm**
- Minimum effective: 2 - 6 = **-4 μm** (possible clearance)

**Conclusion:** Provides light interference, suitable for normal loads

---

**Example: 6308 Bearing in H7 Housing**

**Housing: 90 H7**
- Upper limit: 90.000 + 0.035 = 90.035 mm
- Lower limit: 90.000 mm

**Bearing OD tolerance (normal class):**
- Upper limit: 90.000 mm
- Lower limit: 90.000 - 0.015 = 89.985 mm

**Clearance range:**
- Maximum: 90.035 - 89.985 = **0.050 mm = 50 μm**
- Minimum: 90.000 - 90.000 = **0 mm**

**Result:** Clearance fit, suitable for stationary outer ring

## Thermal Effects on Fits

### Thermal Expansion

**Linear Thermal Expansion:**
```
ΔL = α × L × ΔT
```

Where:
- α = coefficient of thermal expansion (1/°C)
- L = original length (mm)
- ΔT = temperature change (°C)

**Typical α values:**
- Steel: 11-12 × 10⁻⁶ /°C
- Aluminum: 23 × 10⁻⁶ /°C
- Cast iron: 10-11 × 10⁻⁶ /°C

### Temperature Effects on Fits

**Scenario 1: Steel Shaft in Steel Housing**

Both expand equally → fit maintained (slight reduction in interference)

**Scenario 2: Steel Shaft in Aluminum Housing**

Aluminum expands ~2× steel:
- Shaft interference effectively increases
- Outer ring clearance increases
- May require adjustment of fits

**Scenario 3: High Operating Temperature**

**Example:**
- Ambient temperature: 20°C
- Operating temperature: 100°C
- ΔT = 80°C
- Shaft diameter: 100 mm

**Shaft expansion:**
```
Δd = 12 × 10⁻⁶ × 100 × 80 = 0.096 mm = 96 μm
```

**Effect:**
- Interference increased by ~96 μm
- May become too tight
- Excessive stress on bearing

**Solution:**
- Use one grade looser fit (k6 → j6)
- Consider thermal expansion in fit selection

### Thermal Mounting Temperature

**Required heating temperature for thermal mounting:**

```
ΔT = (δ + f) / (α × d)
```

Where:
- δ = interference (mm)
- f = clearance for mounting (typically 0.001-0.002 × d)
- α = thermal expansion coefficient
- d = bore diameter (mm)

**Example:**
- Bearing bore: 100 mm
- Interference: 0.050 mm
- Required clearance: 0.1 mm (for easy mounting)
- Total expansion needed: 0.150 mm

```
ΔT = 0.150 / (12 × 10⁻⁶ × 100) = 125°C
```

**Heating temperature: 20°C + 125°C = 145°C**

**Practical limit:** 
- Maximum 120-130°C for standard bearings
- Avoid overheating (>150°C can affect heat treatment)

## Creep and Fretting

### Ring Creep

**Definition:**
Gradual rotation of bearing ring on its seat due to insufficient interference

**Causes:**
- Insufficient interference fit
- Rotating load with clearance fit
- Shock and vibration
- High loads

**Consequences:**
- Wear of shaft/housing surface
- Overheating
- Accelerated bearing failure
- Loss of accuracy

**Prevention:**
1. Proper fit selection (adequate interference)
2. Positive axial location (shoulders, lock nuts)
3. Adhesive bonding (special applications)
4. Knurled shafts (small bearings, light loads)

**Detection:**
- Black oxide dust (fretting debris)
- Shiny wear tracks on shaft
- Noise and vibration
- Overheating

### Fretting Corrosion

**Definition:**
Surface damage at contact interfaces due to micro-motion

**Mechanism:**
- Small amplitude oscillatory motion
- Protective oxide layer breaks
- Fresh metal oxidizes (iron oxide - red/brown)
- Repeated process creates pitting

**Appearance:**
- Red/brown corrosion product (for steel)
- Surface pitting and roughness
- Progressive damage

**Prevention:**
1. Adequate interference fit
2. Surface treatments (phosphating, coating)
3. Improved surface finish
4. Lubricants with EP additives
5. Eliminate vibration source

## Fit Tables for Common Bearing Sizes

### Shaft Tolerance Deviations (IT6)

**Commonly Used Shaft Fits:**

| Nominal Diameter | h6 (μm) | j6 (μm) | k6 (μm) | m6 (μm) | n6 (μm) | p6 (μm) |
|------------------|---------|---------|---------|---------|---------|---------|
| **Over-To (mm)** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** |
| 18-30 | 0/-13 | +8/-5 | +15/+2 | +20/+7 | +28/+15 | +32/+19 |
| 30-50 | 0/-16 | +10/-6 | +18/+2 | +24/+8 | +33/+17 | +39/+23 |
| 50-80 | 0/-19 | +12/-7 | +21/+2 | +28/+9 | +39/+20 | +45/+26 |
| 80-120 | 0/-22 | +15/-7 | +25/+3 | +33/+11 | +45/+23 | +53/+31 |
| 120-180 | 0/-25 | +18/-7 | +28/+3 | +37/+12 | +52/+27 | +59/+34 |
| 180-250 | 0/-29 | +20/-9 | +33/+4 | +43/+14 | +60/+31 | +68/+39 |
| 250-315 | 0/-32 | +23/-9 | +36/+4 | +47/+15 | +66/+34 | +77/+45 |

**Note:** All values in micrometers (μm)

### Housing Tolerance Deviations (IT7)

**Commonly Used Housing Fits:**

| Nominal Diameter | H7 (μm) | J7 (μm) | K7 (μm) | M7 (μm) | N7 (μm) | P7 (μm) |
|------------------|---------|---------|---------|---------|---------|---------|
| **Over-To (mm)** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** | **Upper/Lower** |
| 18-30 | +21/0 | +12/-9 | +6/-15 | +2/-19 | -7/-28 | -13/-34 |
| 30-50 | +25/0 | +15/-10 | +9/-16 | +2/-23 | -9/-34 | -15/-40 |
| 50-80 | +30/0 | +18/-12 | +10/-20 | +2/-28 | -10/-40 | -17/-47 |
| 80-120 | +35/0 | +22/-13 | +13/-22 | +2/-33 | -12/-47 | -20/-55 |
| 120-180 | +40/0 | +25/-15 | +15/-25 | +2/-38 | -14/-54 | -23/-63 |
| 180-250 | +46/0 | +29/-17 | +17/-29 | +2/-44 | -15/-61 | -26/-72 |
| 250-315 | +52/0 | +32/-20 | +20/-32 | +2/-50 | -17/-69 | -29/-81 |

**Note:** All values in micrometers (μm)

### Practical Fit Selection Summary

**Quick Reference:**

| Application | Shaft Fit | Housing Fit |
|-------------|-----------|-------------|
| **Standard electric motor** | k6 | H7 |
| **Pump (rotating shaft)** | k6 or m6 | H7 |
| **Wheel hub (rotating outer)** | h6 | M7 or N7 |
| **Fan (light load)** | j6 | H7 |
| **Gearbox (heavy load)** | m6 or n6 | H7 |
| **Machine tool spindle** | k5 or m5 | H6 or J6 |
| **Conveyor roller** | h6 | H7 |
| **Vibrating screen** | n6 | M7 or N7 |
| **Railway axlebox** | n6 or p6 | N7 or P7 |
| **Precision instrument** | k5 | H6 or J6 |

## ГОСТ Standards and Equivalents

### ГОСТ 25347-82

**Russian standard equivalent to ISO 286:**
- Defines tolerance zones for shafts and holes
- Uses same letter-number designation
- Directly compatible with ISO system

**Tolerance Fields:**
- Shafts: h, j, k, m, n, p (same as ISO)
- Holes: H, J, K, M, N, P (same as ISO)

### ГОСТ 520-2002

**Rolling bearings - General technical requirements**
- Specifies bearing tolerances
- Defines accuracy classes
- Compatible with ISO 492

**Accuracy Classes:**
- Class 0 (Normal) - ISO P0
- Class 6 - ISO P6
- Class 5 - ISO P5
- Class 4 - ISO P4

## Worked Examples

### Example 1: Fit Selection for Electric Motor

**Application:**
- 3-phase electric motor, 15 kW, 1500 rpm
- Bearing: 6310 (d=50 mm, D=110 mm, B=27 mm)
- Load: rotating inner ring, stationary outer ring
- Normal load, no shock

**Solution:**

**Shaft fit:**
- Rotating load on inner ring → interference fit
- Bearing size: d=50 mm (medium)
- Normal load → **k6** (standard)

**Housing fit:**
- Stationary load on outer ring → clearance fit
- Standard application → **H7**

**Final selection: Shaft 50 k6, Housing 110 H7**

---

### Example 2: Wheel Hub Bearing

**Application:**
- Automotive wheel hub
- Bearing: Double row angular contact ball bearing
- Load: stationary inner ring, rotating outer ring
- Medium loads, some shock

**Solution:**

**Shaft fit (inner ring stationary):**
- Stationary load → clearance fit
- Some shock, precise location → **j6**

**Housing fit (outer ring rotating):**
- Rotating load → interference fit
- Aluminum alloy housing (thin-wall) → **M7 or N7**
- Select **M7** for normal service

**Final selection: Shaft j6, Housing M7**

---

### Example 3: High-Temperature Application

**Application:**
- Bearing near furnace
- Operating temperature: 120°C
- Ambient: 20°C
- Bearing: 6212 on steel shaft in cast iron housing

**Analysis:**

**Temperature rise:** ΔT = 100°C

**Shaft expansion (d=60 mm):**
```
Δd = 12 × 10⁻⁶ × 60 × 100 = 0.072 mm = 72 μm
```

**Standard k6 interference:** ~15-30 μm
**At operating temp:** 15+72 = 87 μm (too tight!)

**Solution:**
- Use **j6** instead of k6 (looser fit)
- Or use **h6** with mechanical locking
- Monitor bearing clearance

---

### Example 4: Interference Calculation

**Given:**
- Bearing: 6309 (d=45 mm, D=100 mm)
- Shaft: 45 m6
- Calculate effective interference

**From table (30-50 mm range):**
- m6: Upper +24 μm, Lower +8 μm

**Bearing bore tolerance (Normal class, ISO 492):**
- Upper: 0 μm
- Lower: -12 μm (typical)

**Nominal interference:**
- Max: 24 - (-12) = 36 μm
- Min: 8 - 0 = 8 μm

**Effective interference (roughness ~6 μm):**
- Max effective: 36 - 6 = **30 μm**
- Min effective: 8 - 6 = **2 μm**

**Assessment:** Adequate for normal rotating loads

## Best Practices

### Design Recommendations

1. **Use standard fits when possible:**
   - Shaft: k6 for normal loads, m6 for heavy
   - Housing: H7 for stationary outer ring

2. **Consider operating conditions:**
   - Temperature, speed, load, vibration
   - Material of shaft and housing

3. **Provide adequate clearance:**
   - Account for thermal expansion
   - Consider internal bearing clearance reduction

4. **Design for assembly/disassembly:**
   - Tighter fits require thermal or press mounting
   - Consider maintenance requirements

5. **Use shoulders and retaining features:**
   - Prevent axial movement
   - Support against creep

### Measurement and Verification

**Shaft and housing measurement:**
- Use calibrated micrometers
- Measure at multiple points
- Check roundness and cylindricity
- Document actual dimensions

**Surface finish:**
- Verify Ra ≤ 1.6 μm for shafts
- Verify Ra ≤ 3.2 μm for housings
- Smooth, defect-free surfaces

**Tolerance verification:**
- Confirm dimensions within tolerance zone
- Check both shaft and housing
- Verify before bearing mounting

---

**Document Version:** 1.0  
**Last Updated:** 2024  
**Related Documents:** 05_01_lubrication.md, 05_03_mounting.md, 04_parameters_calculations
