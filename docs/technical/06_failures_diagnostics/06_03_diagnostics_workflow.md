# Bearing Diagnostics Workflow

## Purpose
This document provides comprehensive diagnostic procedures, condition monitoring techniques, and decision-making frameworks for bearing health assessment. Covers vibration analysis, oil analysis, thermography, and integrated predictive maintenance strategies.

## Overview of Bearing Diagnostics

### Diagnostic Pyramid

**Level 1: Operational Monitoring**
- Temperature indicators
- Noise/vibration (subjective)
- Visual inspection during rounds
- Basic performance monitoring

**Level 2: Periodic Condition Monitoring**
- Scheduled vibration measurements
- Periodic oil sampling
- Thermographic inspection
- Ultrasonic listening

**Level 3: Continuous Monitoring**
- Online vibration sensors
- Continuous temperature monitoring
- Automatic trending and alarming
- Integration with control systems

**Level 4: Advanced Diagnostics**
- Detailed vibration analysis (FFT, envelope)
- Comprehensive oil analysis
- Acoustic emission
- Root cause failure analysis

### Diagnostic Strategy Selection

**Critical Equipment:**
- Continuous monitoring (Level 3)
- Advanced diagnostics when indicated (Level 4)
- Low threshold for intervention
- Examples: Main process equipment, safety systems

**Important Equipment:**
- Periodic monitoring (Level 2)
- Monthly or quarterly measurements
- Trend analysis
- Examples: Production equipment, essential services

**General Equipment:**
- Operational monitoring (Level 1)
- Visual inspection during rounds
- Run-to-failure may be acceptable
- Examples: Non-critical pumps, fans

## 1. Vibration Analysis

### 1.1 Vibration Fundamentals

**Why Vibration Analysis Works:**
- Bearing defects create periodic impacts
- Impacts generate vibration at characteristic frequencies
- Amplitude increases as damage progresses
- Pattern changes indicate defect type and location

**Vibration Parameters:**
- **Displacement (μm, mils):** Low frequencies, alignment issues
- **Velocity (mm/s, in/s):** General machinery condition (most common)
- **Acceleration (g, m/s²):** High frequencies, bearing defects

**Frequency Ranges:**
- **Low frequency (< 100 Hz):** Unbalance, misalignment, looseness
- **Medium frequency (100-1000 Hz):** Gear mesh, vane pass, aerodynamic
- **High frequency (1000-20,000 Hz):** Bearing defects, cavitation
- **Very high frequency (20-40+ kHz):** Ultrasonic, early bearing damage

### 1.2 Bearing Defect Frequencies

**Fundamental Frequencies:**

Rolling bearings generate vibration at specific frequencies based on geometry and speed:

**1. BPFO - Ball Pass Frequency Outer Race (Частота прохождения тел качения по наружному кольцу)**

Formula: BPFO = (n × Z / 2) × (1 - (d/D) × cos α)

Where:
- n = shaft speed (Hz or RPM/60)
- Z = number of rolling elements
- d = rolling element diameter
- D = pitch diameter
- α = contact angle

**Physical meaning:** Frequency at which rolling elements pass a point on the stationary outer ring.

**Typical characteristics:**
- Non-synchronous with shaft speed
- Usually most prominent for outer ring defects
- Harmonics indicate defect progression

**2. BPFI - Ball Pass Frequency Inner Race (Частота прохождения тел качения по внутреннему кольцу)**

Formula: BPFI = (n × Z / 2) × (1 + (d/D) × cos α)

**Physical meaning:** Frequency at which rolling elements pass a point on the rotating inner ring.

**Typical characteristics:**
- Higher than BPFO (inner ring rotates)
- Modulated by shaft speed (sidebands)
- Inner ring defects common due to higher stress

**3. BSF - Ball Spin Frequency (Частота вращения тела качения)**

Formula: BSF = (n × D / 2d) × (1 - (d/D)² × cos² α)

**Physical meaning:** Frequency at which a rolling element rotates about its own axis.

**Typical characteristics:**
- Lowest amplitude typically
- Rolling element defects generate 2× BSF (defect hits both rings per revolution)
- Often difficult to detect until advanced

**4. FTF - Fundamental Train Frequency (Частота вращения сепаратора)**

Formula: FTF = (n / 2) × (1 - (d/D) × cos α)

**Physical meaning:** Frequency at which the cage (and rolling element set) rotates.

**Typical characteristics:**
- Very low frequency (0.3-0.4× shaft speed typically)
- Cage defects generate multiples of FTF
- Can indicate uneven element spacing

**Simplified Quick Reference (α ≈ 0° for radial bearings):**
- BPFO ≈ 0.4 × n × Z
- BPFI ≈ 0.6 × n × Z
- BSF ≈ 0.2 × n × (D/d)
- FTF ≈ 0.4 × n

**Example Calculation:**
Bearing 6205 operating at 1800 RPM
- Z = 9 balls
- d ≈ 7.94mm
- D ≈ 39mm
- α ≈ 0°
- n = 1800/60 = 30 Hz

Results:
- BPFO = 30 × 9 × 0.4 = 108 Hz
- BPFI = 30 × 9 × 0.6 = 162 Hz
- BSF = 30 × 0.2 × (39/7.94) ≈ 29.4 Hz
- FTF = 30 × 0.4 = 12 Hz

### 1.3 Vibration Measurement Techniques

**Sensor Placement:**
- **Preferred:** Bearing housing, close to bearing
- **Orientation:** Radial (horizontal and vertical), axial
- **Mounting:** Stud-mounted (best), magnetic (good), hand-held (screening only)
- **Avoid:** Flexible structures, painted surfaces, near discontinuities

**Measurement Points:**
- Consistent locations for trending
- All three axes (horizontal, vertical, axial)
- Both bearing positions (drive end, non-drive end)
- Mark and document measurement locations

**Data Collection Settings:**
- **Fmax (maximum frequency):** 
  - General: 1000-2000 Hz
  - Bearing focus: 5000-10,000 Hz
  - Envelope analysis: 20,000-40,000 Hz
- **Lines of resolution:** Minimum 800, prefer 1600-3200
- **Averages:** 4-8 for stable signals
- **Window:** Hanning (typical), uniform (transient)

**Measurement Intervals:**
- **Critical equipment:** Weekly or continuous
- **Important equipment:** Monthly
- **General equipment:** Quarterly or semi-annually
- **New/repaired equipment:** Initial, 1 week, 1 month, then normal schedule

### 1.4 Vibration Analysis Methods

#### Overall Vibration Level

**Velocity RMS (ISO 10816):**
- Single-value indicator of machine condition
- Easy to trend over time
- Insufficient for diagnosis alone

**ISO 10816 Severity Zones:**

| Class | Description | Zone A | Zone B | Zone C | Zone D |
|-------|-------------|--------|--------|--------|--------|
| I | Small machines (< 15 kW) | < 0.71 | 0.71-1.8 | 1.8-4.5 | > 4.5 |
| II | Medium machines (15-75 kW) | < 1.12 | 1.12-2.8 | 2.8-7.1 | > 7.1 |
| III | Large machines (> 75 kW), rigid | < 1.8 | 1.8-4.5 | 4.5-11.2 | > 11.2 |
| IV | Large machines, flexible | < 2.8 | 2.8-7.1 | 7.1-18 | > 18 |

Values in mm/s RMS (10-1000 Hz)

**Zone Interpretation:**
- **Zone A:** Good - Newly commissioned machines
- **Zone B:** Acceptable - Unrestricted long-term operation
- **Zone C:** Unsatisfactory - Limited operation, plan corrective action
- **Zone D:** Unacceptable - Damage risk, immediate action required

**Trending:**
- Baseline at commissioning
- 25% increase: Monitor closely
- 50% increase: Investigate
- 100% increase (2× baseline): Action required

#### Frequency Analysis (FFT)

**Fast Fourier Transform (FFT):**
- Converts time waveform to frequency spectrum
- Identifies specific defect frequencies
- Essential for bearing diagnostics

**Spectrum Interpretation:**

**Bearing Defect Indicators:**
1. **Peaks at BPFO, BPFI, BSF, or FTF**
   - Indicates corresponding defect
   - Check harmonics (2×, 3×, 4× frequency)
   - More harmonics = more severe defect

2. **Sidebands around bearing frequencies**
   - Spacing = shaft speed (1× RPM)
   - Indicates modulation (inner ring defect, load variation)
   - Asymmetric sidebands suggest advanced damage

3. **Raised noise floor at high frequencies**
   - Early bearing damage
   - Broadband high-frequency energy
   - Precursor to discrete peaks

4. **Sub-harmonic peaks**
   - Below 1× RPM
   - Can indicate cage issues or looseness
   - FTF and harmonics

**Other Common Frequencies:**
- **1× RPM:** Unbalance, misalignment
- **2× RPM:** Misalignment, bent shaft
- **3× RPM:** Misalignment
- **Harmonics of line frequency (50/60 Hz):** Electrical issues

**ГОСТ Vibration Standards:**
- ГОСТ ISO 10816-1-97 - Общие требования (General requirements)
- ГОСТ ISO 10816-3-2002 - Промышленные машины (Industrial machines)

#### Envelope Analysis (Acceleration Enveloping)

**Principle:**
- High-pass filter to isolate bearing frequencies (typically > 5 kHz)
- Demodulate (envelope) the signal
- FFT of envelope reveals bearing defect frequencies
- Much more sensitive to early defects than velocity analysis

**Why It Works:**
- Bearing defects create impulses (impacts)
- Impulses excite structural resonances
- Envelope detects amplitude modulation of resonances
- Amplifies weak signals from early defects

**Procedure:**
1. Acquire acceleration time waveform
2. High-pass filter (5-20 kHz typical, or around structural resonance)
3. Envelope/demodulate signal
4. FFT of enveloped signal
5. Identify bearing defect frequencies

**Interpretation:**
- **No bearing frequencies:** Bearing OK
- **BPFO or BPFI present:** Outer or inner ring defect developing
- **Multiple harmonics:** Defect progressing
- **Sidebands:** Advanced defect, modulation
- **Broadband noise increase:** Very early defect stage

**Advantages:**
- Detects defects earlier than velocity analysis
- Better signal-to-noise ratio for bearings
- Less affected by low-frequency vibration

**Envelope Alarm Levels (Example):**
- **Alert:** Bearing frequency peak > 0.5 g
- **Alarm:** Bearing frequency peak > 1.0 g
- **Danger:** Bearing frequency peak > 2.0 g or multiple harmonics

#### Time Waveform Analysis

**Purpose:**
- Visualize impacts from defects
- Assess impulsiveness and periodicity
- Confirm frequency analysis findings

**Indicators:**
- **Regular impulses:** Defect on raceway (period = 1/BPFO or 1/BPFI)
- **Irregular impulses:** Distributed damage or cage issues
- **High amplitude spikes:** Advanced damage
- **Waveform shape:** Indicates impact severity

**Kurtosis (Peaked-ness):**
- Measure of impulsiveness
- Normal: Kurtosis ≈ 3
- Early bearing defect: Kurtosis > 4-6
- Advanced defect: May decrease as damage spreads

#### Trend Analysis

**Trending Parameters:**
- Overall vibration level (velocity RMS)
- Peak levels at specific frequencies
- Envelope acceleration
- Kurtosis
- Crest factor

**Trend Interpretation:**
- **Stable:** Normal operation
- **Gradual increase:** Normal aging, monitor
- **Sudden increase:** Event occurred (e.g., overload, contamination)
- **Exponential increase:** Failure approaching, plan replacement
- **Erratic:** Operational changes, inconsistent measurement

**Alarm Setting:**
- **Baseline + statistical variation:** For stable operation
- **Percentage increase:** e.g., Alert at +50%, Alarm at +100%
- **Absolute levels:** Per ISO 10816 or manufacturer recommendation
- **Rate of change:** Rapid increase indicates accelerated degradation

### 1.5 Bearing Condition Assessment by Vibration

**Stage 1: Normal/Good**
- Overall vibration in ISO Zone A or B
- No bearing defect frequencies visible
- Low background noise
- **Action:** Continue normal monitoring

**Stage 2: Early Defect**
- Slight increase in overall vibration
- Raised high-frequency noise floor
- Envelope shows initial bearing frequencies
- **Action:** Increase monitoring frequency, investigate cause

**Stage 3: Moderate Defect**
- Noticeable increase in overall vibration (Zone C)
- Clear bearing defect frequencies in spectrum
- Multiple harmonics appearing
- Envelope shows strong peaks
- **Action:** Plan replacement during next maintenance window

**Stage 4: Advanced Defect**
- High overall vibration (approaching or in Zone D)
- Multiple harmonics and sidebands
- Broadband noise increase
- Audible noise
- **Action:** Replace at earliest opportunity, avoid full-load operation

**Stage 5: Severe/Imminent Failure**
- Very high overall vibration (Zone D)
- Complex spectrum with many frequencies
- Temperature increase
- Clearly audible and rough rotation
- **Action:** Immediate shutdown and replacement

## 2. Temperature Monitoring

### 2.1 Temperature Measurement

**Measurement Methods:**
- **Contact thermometers:** Direct measurement, accurate
- **Infrared (IR) thermography:** Non-contact, imaging, trends
- **Embedded sensors (RTD, thermocouple):** Continuous monitoring
- **Temperature sticks/crayons:** Indication of maximum temperature reached

**Measurement Locations:**
- Bearing outer ring (housing)
- Oil drain temperature (for oil-lubricated bearings)
- Ambient temperature (for comparison)

**Typical Operating Temperatures:**
- **Normal:** 30-50°C above ambient
- **Acceptable:** Up to 70°C above ambient (depends on application)
- **High:** 70-90°C above ambient - investigate
- **Excessive:** > 90°C above ambient - action required

**Maximum Temperatures:**
- **Standard grease:** Typically 90-110°C continuous
- **High-temp grease:** Up to 150°C continuous
- **Oil lubrication:** Up to 120°C (depends on oil)
- **Seals:** Limit based on seal material (typically 100-120°C for standard)

### 2.2 Temperature Analysis

**Temperature Rise Causes:**

**Excessive Friction:**
- Inadequate lubrication
- Wrong lubricant viscosity
- Over-greasing (grease-packed)
- Excessive preload
- Bearing damage

**External Heat:**
- Adjacent hot processes
- Poor heat dissipation
- High ambient temperature

**High Load:**
- Overload
- Misalignment

**Temperature Trending:**
- **Stable:** Normal operation
- **Gradual increase over months:** Normal aging, possible lubrication degradation
- **Sudden increase:** Event (lubrication failure, damage, overload)
- **Cyclic variation:** Normal with load/speed changes
- **Rapid increase:** Imminent failure, often accompanies advanced bearing damage

**Thermographic Patterns:**
- **Uniform hot spot at bearing:** Normal under load
- **Very hot localized area:** Defect location
- **Entire housing hot:** Excessive friction or external heat
- **Temperature difference between bearings:** Uneven load, one bearing damaged

### 2.3 Temperature Alarm Levels (Example)

| Level | Temperature | Action |
|-------|-------------|--------|
| Normal | < 70°C | Continue operation |
| Alert | 70-80°C | Investigate, increase monitoring |
| Alarm | 80-90°C | Plan corrective action |
| Danger | > 90°C | Immediate action, consider shutdown |

**Note:** Actual limits depend on bearing type, lubrication, application. Consult manufacturer.

## 3. Acoustic Emission (AE) Monitoring

### 3.1 AE Principles

**What is Acoustic Emission:**
- High-frequency elastic waves (100 kHz - 1 MHz)
- Generated by rapid energy release (crack growth, impacts, friction)
- Propagates through material
- Detected by piezoelectric sensors

**Why It Works for Bearings:**
- Defects create micro-impacts and friction
- AE sensitive to early-stage damage
- Detects events not visible in vibration
- Less affected by background noise

### 3.2 AE Measurement

**Sensors:**
- Piezoelectric AE sensors
- Mounted on bearing housing
- Frequency range: typically 100-300 kHz

**Parameters:**
- **AE RMS:** Overall level
- **AE counts:** Number of events exceeding threshold
- **Energy:** Integrated signal energy
- **Peak amplitude:** Maximum events

**Advantages:**
- Very early defect detection
- Sensitive to lubrication condition
- Good for slow-speed bearings (where vibration is weak)

**Limitations:**
- Affected by sensor coupling
- Attenuation over distance
- Requires experience for interpretation
- More expensive than vibration

### 3.3 AE Interpretation

**Normal Bearing:**
- Low AE RMS and counts
- Stable readings

**Insufficient Lubrication:**
- Increased AE RMS
- Increased counts
- May precede vibration increase

**Early Defect:**
- Increase in AE energy
- Intermittent high-amplitude events

**Advanced Defect:**
- High AE levels
- Continuous high activity
- Vibration also elevated

## 4. Oil Analysis

### 4.1 Oil Sampling

**Sampling Procedure:**
- Sample from active circulation zone
- Consistent sampling point
- Avoid contamination during sampling
- Use clean bottles
- Label with equipment ID, date, oil type

**Sampling Frequency:**
- **Critical equipment:** Monthly
- **Important equipment:** Quarterly
- **General equipment:** Annually
- **New oil:** Baseline before use
- **After events:** Contamination, water ingress, overheating

**Sample Size:**
- Typically 100-250 mL
- Follow lab requirements

### 4.2 Oil Analysis Tests

#### Particle Counting (ISO 4406)

**Purpose:**
- Quantify solid contamination in oil
- Track cleanliness over time

**Method:**
- Optical particle counter
- Counts particles in size ranges: > 4μm, > 6μm, > 14μm

**ISO 4406 Cleanliness Code:**
Format: XX/YY/ZZ
- XX = particles > 4μm per mL
- YY = particles > 6μm per mL  
- ZZ = particles > 14μm per mL

Each number represents a range (logarithmic scale)

**Example:** 18/16/13
- 18: 1300-2500 particles > 4μm/mL
- 16: 320-640 particles > 6μm/mL
- 13: 40-80 particles > 14μm/mL

**Target Cleanliness:**
- **High-speed bearings:** 15/13/10 or better
- **General bearings:** 18/16/13
- **Acceptable maximum:** 20/18/15
- **Action required:** > 21/19/16

#### Ferrography

**Purpose:**
- Analyze wear particles (composition, size, morphology)
- Determine wear mode and source

**Types:**

**Analytical Ferrography:**
- Magnetic separation of particles onto glass slide
- Microscopic examination
- Classify particles by type:
  - Cutting wear (machining-type particles)
  - Rubbing wear (small platelets)
  - Severe sliding (large platelets)
  - Rolling fatigue (chunky, spherical)
  - Laminar particles (delamination)
  - Non-ferrous (brass from cages)

**Direct-Reading Ferrography:**
- Quantifies large and small ferrous particles
- Trending parameter
- Large particle index increasing indicates wear acceleration

**Interpretation:**
- Normal wear: Small particles, low concentration
- Abnormal wear: Large particles, high concentration
- Cutting wear: New damage or break-in
- Fatigue particles: Bearing spalling
- Non-ferrous increase: Cage wear

#### Spectrometric Analysis (ICP)

**Purpose:**
- Measure dissolved metals in oil (ppm - parts per million)
- Identify wear sources

**Common Elements:**
- **Iron (Fe):** Steel components (rings, rollers, shafts)
- **Chromium (Cr):** Bearing steel (ШХ15 contains ~1.5% Cr)
- **Copper (Cu):** Brass cages, bronze components
- **Zinc (Zn):** Brass, some additives
- **Aluminum (Al):** Housings, some cages
- **Tin (Sn):** Babbitt bearings, some lubricant additives
- **Lead (Pb):** Babbitt, some additives
- **Silicon (Si):** Dirt contamination, some additives

**Trending:**
- Establish baseline for new oil and equipment
- Monitor trends rather than absolute values
- Sudden increase indicates accelerated wear or contamination

**Alarm Levels (Example - bearing steel components):**
- **Normal:** Fe < 50 ppm, Cr < 5 ppm
- **Alert:** Fe 50-100 ppm, Cr 5-10 ppm
- **Alarm:** Fe > 100 ppm, Cr > 10 ppm

**Note:** Values are application-specific; large gearboxes normally have higher levels.

#### Water Content

**Methods:**
- Karl Fischer titration (most accurate)
- Crackle test (field method)
- Visual inspection (severe contamination)

**Limits:**
- **Target:** < 100 ppm (< 0.01%)
- **Acceptable:** 100-500 ppm
- **Action required:** > 500 ppm
- **Severe:** > 1000 ppm (0.1%) - bearing damage likely

**Effects:**
- Reduces lubricant film strength
- Promotes corrosion
- Additive depletion
- Oxidation acceleration

#### Viscosity

**Purpose:**
- Verify oil grade
- Detect contamination or degradation

**Measurement:**
- Kinematic viscosity at 40°C and 100°C
- ASTM D445 method

**Interpretation:**
- **Increase > 10%:** Oxidation, contamination (soot, glycol)
- **Decrease > 10%:** Fuel dilution, wrong oil, shear degradation

#### Acid Number (TAN - Total Acid Number)

**Purpose:**
- Measure acidic compounds in oil
- Indicator of oxidation

**Limits:**
- **New oil:** Typically 0.5-2.0 mg KOH/g
- **Action required:** Increase of 0.5-1.0 from baseline, or absolute > 2.0-4.0

**Action:**
- Increase indicates oil degradation
- Change oil when limit reached

### 4.3 Oil Analysis Decision Matrix

| Test Result | Indication | Action |
|-------------|------------|--------|
| ISO code degraded 2+ levels | Increasing contamination | Improve filtration, find source |
| Large particles increasing | Active wear | Increase sampling, investigate |
| Fe > 100 ppm or rapidly increasing | Bearing or steel component wear | Vibration analysis, plan inspection |
| Cu > 50 ppm increasing | Cage wear | Monitor, plan bearing replacement |
| Water > 500 ppm | Water ingress | Find and fix source, change oil |
| Viscosity change > 10% | Wrong oil or degradation | Verify oil grade, change if degraded |
| TAN increase > 1.0 from baseline | Oil oxidation | Change oil |
| Fatigue particles in ferrography | Bearing spalling | Plan bearing replacement |

## 5. Visual Inspection Procedures

### 5.1 In-Service Visual Inspection

**Operator Daily/Shift Checks:**
- Visual check for leaks
- Listen for unusual noise
- Feel for excessive vibration (hand on housing)
- Check temperature (hand-touch or IR gun)
- Look for discoloration or smoking

**Maintenance Technician Inspection:**
- More detailed visual inspection
- Check seal condition
- Look for lubricant leakage or contamination
- Inspect for cracks, corrosion
- Verify proper lubricant level (if visible)
- Check mounting bolts/fasteners

**Documentation:**
- Note any abnormalities
- Record temperature if measured
- Tag equipment if issues found
- Update CMMS (Computerized Maintenance Management System)

### 5.2 Removed Bearing Inspection

**Preparation:**
- Clean workspace
- Proper lighting (1000+ lux)
- Cleaning solvent
- Magnification (loupe, microscope)
- Camera for documentation
- Inspection forms

**Procedure:**
1. **Preliminary inspection before cleaning:**
   - Check lubricant condition (color, consistency, smell)
   - Look for contamination
   - Check for obvious damage

2. **Cleaning:**
   - Solvent wash (kerosene, mineral spirits)
   - Remove all lubricant and contamination
   - Air dry or clean cloth
   - Do not spin bearing with compressed air (damage risk)

3. **Detailed inspection:**
   - Check each raceway (rotate for full view)
   - Inspect all rolling elements individually
   - Examine cage for damage
   - Check seals/shields
   - Inspect mounting surfaces and faces

4. **Functional check:**
   - Rotate slowly by hand
   - Feel for roughness, resistance
   - Listen for noise
   - Check clearance (compare to spec)

5. **Measurements:**
   - Clearance (radial, axial)
   - Bore and OD (if suspected issues)
   - Defect dimensions

6. **Documentation:**
   - Complete inspection form
   - Photograph defects
   - Classify defects per terminology
   - Record recommendation

**Disposition:**
- **Acceptable for continued use:** Clean, lubricate, reinstall
- **Monitor:** Minor wear, schedule replacement
- **Reject:** Defects exceeding criteria, dispose
- **Failure analysis:** Send to lab for detailed analysis

## 6. Symptom-to-Failure Mapping

### 6.1 Diagnostic Decision Trees

#### Tree 1: High Vibration

**High overall vibration detected**

→ **Is it increasing over time?**
   - Yes → Continue
   - No (stable) → Check for installation issues, resonance

→ **Check frequency spectrum**

   **Peaks at 1×, 2× RPM:**
   - Likely: Unbalance, misalignment
   - Action: Balance, align shaft
   
   **Peaks at bearing frequencies (BPFO, BPFI):**
   - Likely: Bearing defect
   - Action: Envelope analysis, plan replacement
   
   **Broadband noise, high frequency:**
   - Likely: Early bearing damage, lubrication issue
   - Action: Check lubrication, increase monitoring
   
   **Peaks at multiples of line frequency (50/60 Hz):**
   - Likely: Electrical issues (motor)
   - Action: Check motor, electrical system

#### Tree 2: High Temperature

**High bearing temperature detected**

→ **Is vibration also high?**
   - Yes → Likely bearing damage - immediate action
   - No → Continue

→ **Check lubrication**
   - Insufficient? → Add lubricant
   - Excessive (grease)? → Purge excess
   - Wrong viscosity? → Change lubricant
   - Degraded? → Change lubricant

→ **Check load and alignment**
   - Misalignment → Align
   - Overload → Verify application, check for process changes
   - Excessive preload → Adjust

→ **Still high?**
   - Possible internal damage → Plan inspection/replacement

#### Tree 3: Noise

**Unusual noise from bearing**

→ **Type of noise?**

   **Grinding, rumbling:**
   - Check: Vibration analysis
   - Likely: Bearing damage
   - Action: Replace bearing
   
   **Clicking, popping (intermittent):**
   - Likely: Indentation (brinelling), debris
   - Check: Vibration, inspect when possible
   
   **Squealing, squeaking:**
   - Likely: Inadequate lubrication, cage slip
   - Check: Lubrication, speed
   - Action: Improve lubrication
   
   **Humming (electric motor):**
   - May be: Electrical issues, not bearing
   - Check: Motor electrically

### 6.2 Symptom-Cause-Action Table

| Symptom | Likely Causes | Diagnostic Steps | Action |
|---------|---------------|------------------|--------|
| High vibration, bearing frequencies | Bearing defect (spalling, pitting) | FFT, envelope analysis, check harmonics | Replace bearing |
| High vibration, 1× RPM | Unbalance | Verify 1× peak, check phase | Balance rotor |
| High vibration, 2× RPM | Misalignment, bent shaft | Check alignment, inspect shaft | Align or replace shaft |
| High temperature, normal vibration | Lubrication issue | Check lubricant quantity, type, condition | Correct lubrication |
| High temperature + vibration | Bearing damage | Vibration analysis, visual inspection | Replace bearing |
| Temperature increase sudden | Lubrication loss, contamination | Inspect seals, check lubricant | Fix seals, change lubricant |
| Noise, grinding | Advanced bearing damage | Vibration, visual | Replace immediately |
| Noise, squeaking | Inadequate lubrication | Check lubricant | Lubricate properly |
| Intermittent noise/vibration | Brinelling, debris | Inspect bearing | Remove debris or replace |
| Oil contamination, particles | Bearing wear, external ingress | Oil analysis, vibration | Improve sealing, replace bearing if needed |
| Oil contamination, water | Seal failure, condensation | Find source | Fix seals, change oil |
| Lubricant leakage | Seal wear, excessive pressure | Inspect seals, check vents | Replace seals, verify breather |
| Bearing locked/seized | Severe overheating, damage | Inspect bearing, check cause | Replace bearing, fix root cause |

## 7. Condition Monitoring Systems

### 7.1 Online Monitoring Systems

**Components:**
- **Sensors:** Accelerometers, temperature (RTD, thermocouple), proximity probes
- **Signal conditioning:** Amplifiers, filters
- **Data acquisition:** ADC, processors
- **Communication:** Ethernet, wireless, 4-20mA
- **Software:** Trending, alarming, diagnostics

**Capabilities:**
- Continuous monitoring
- Automatic alarming
- Trend data storage
- Remote access
- Integration with plant DCS/SCADA

**Applications:**
- Critical equipment (main compressors, turbines, large motors)
- Difficult to access equipment
- High failure consequence
- Regulatory requirements

**Advantages:**
- Real-time awareness
- Immediate alarm notification
- Capture transient events
- Long-term trending

**Disadvantages:**
- Higher cost
- Installation complexity
- Maintenance of monitoring system
- Data management

### 7.2 Portable Monitoring (Route-Based)

**Equipment:**
- Portable vibration analyzer
- Infrared thermometer or camera
- Ultrasonic detector
- Data collector

**Process:**
1. Define routes (equipment to monitor)
2. Establish measurement points
3. Schedule periodic collection (monthly, quarterly)
4. Technician walks route, collects data at each point
5. Data uploaded to software
6. Automatic trending and alarm checking
7. Generate reports and work orders

**Advantages:**
- Lower cost than online
- Covers many machines
- Flexible (can add detail measurements as needed)

**Disadvantages:**
- Periodic snapshots, not continuous
- Requires technician time
- Can miss rapidly developing faults

### 7.3 Condition-Based Maintenance (CBM)

**Concept:**
- Maintenance based on actual equipment condition
- Replace/repair only when needed
- Avoid premature replacement
- Prevent failures

**Implementation:**
1. **Identify critical equipment** - Apply CBM where benefit justifies cost
2. **Select monitoring parameters** - Vibration, temperature, oil analysis, etc.
3. **Establish baselines** - Measure when equipment is known-good
4. **Set alarm levels** - Alert, alarm, danger based on criticality
5. **Monitor regularly** - Online or route-based
6. **Analyze trends** - Identify degradation
7. **Plan maintenance** - Schedule work when needed, before failure
8. **Execute work** - Replace/repair identified issues
9. **Verify** - Confirm improvement after maintenance
10. **Refine** - Adjust strategy based on results

**Benefits:**
- Reduced downtime (planned vs. unplanned)
- Extended component life (replace when needed, not prematurely)
- Improved reliability
- Lower maintenance costs (when properly implemented)

**Challenges:**
- Initial investment (equipment, training)
- Requires skilled personnel
- Data management
- Organizational change

## 8. Predictive Maintenance

### 8.1 P-F Curve (Potential Failure to Functional Failure)

**Concept:**
- All failures have a progression
- **P (Potential Failure):** Condition deterioration detectable
- **F (Functional Failure):** Equipment unable to perform function
- **P-F Interval:** Time available for planned intervention

**For Bearings:**
- **P:** Early defect detectable by envelope analysis, AE, oil analysis
- **F:** Bearing seized, fractured, or causing secondary damage

**Goal:**
- Detect at P (or earlier)
- Act during P-F interval
- Avoid reaching F

**Detection Methods and P-F Interval:**
- **Acoustic Emission:** Earliest detection, longest P-F interval
- **Envelope analysis:** Early detection, long P-F interval
- **Vibration (velocity):** Moderate detection, medium P-F interval
- **Temperature:** Later detection, shorter P-F interval
- **Noise (audible):** Late detection, short P-F interval

**Monitoring Frequency:**
- Must be shorter than P-F interval
- Critical equipment: Weekly or continuous monitoring
- Non-critical: Monthly or quarterly

### 8.2 Remaining Useful Life (RUL) Estimation

**Methods:**

**Trend Extrapolation:**
- Plot vibration or other parameter over time
- Fit trend line
- Extrapolate to failure threshold
- Provides estimated time to failure

**Limitations:**
- Assumes consistent degradation rate
- Failures often accelerate
- Use conservative estimates

**Advanced Methods:**
- **Physics-based models:** Use load, speed, lubricant to model damage accumulation
- **Data-driven models:** Machine learning on historical data
- **Hybrid models:** Combine physics and data

**Practical Approach:**
- **Stage 1-2 (early defect):** Months of remaining life likely
- **Stage 3 (moderate defect):** Weeks to months
- **Stage 4 (advanced defect):** Days to weeks
- **Stage 5 (severe):** Hours to days

**Factors Affecting RUL:**
- Load (higher load accelerates)
- Speed (higher speed accelerates)
- Temperature (elevated temperature accelerates)
- Lubrication (inadequate shortens life)
- Operating mode (continuous vs. start-stop)

### 8.3 Predictive Maintenance Workflow

**1. Baseline Establishment**
- Measure when equipment new or after overhaul
- Establish "good" signature
- Record operating conditions

**2. Routine Monitoring**
- Periodic measurements per schedule
- Automatic trending
- Compare to baseline and limits

**3. Alert Triggered**
- Parameter exceeds alert level
- Automatic notification
- Increase monitoring frequency

**4. Detailed Diagnostics**
- Perform advanced analysis (envelope, time waveform)
- Confirm defect type and severity
- Estimate remaining life

**5. Work Planning**
- Determine scope (bearing replacement, alignment, etc.)
- Procure parts
- Schedule during next available window
- Prepare procedures

**6. Execute Maintenance**
- Perform work as planned
- Document findings during teardown
- Verify root cause assumptions

**7. Post-Maintenance Verification**
- Measure vibration, temperature after startup
- Confirm improvement
- Update baseline if major work done

**8. Root Cause Analysis**
- Determine why failure occurred
- Implement corrective actions (improve sealing, lubrication, etc.)
- Update PdM strategy if needed

## 9. Inspection Intervals

### 9.1 Interval Determination Factors

**Equipment Criticality:**
- **Critical:** Safety, environment, or major production impact - More frequent
- **Important:** Significant production or cost impact - Moderate frequency
- **Non-critical:** Minor impact - Less frequent or run-to-failure

**Operating Conditions:**
- **Severe:** High load, speed, temperature, contamination - More frequent
- **Moderate:** Normal industrial conditions - Standard intervals
- **Light:** Low utilization, clean environment - Less frequent

**Bearing Life:**
- **New equipment:** More frequent initially (infant mortality period)
- **Mid-life:** Standard intervals
- **Approaching design life:** More frequent (wear-out period)

**Failure History:**
- **Reliable equipment:** Standard or reduced frequency
- **Problematic equipment:** Increased frequency, investigate root causes

### 9.2 Recommended Inspection Intervals

**Online Monitoring (Continuous):**
- Data reviewed: Daily (automatic)
- Detailed review: Weekly
- Trend analysis: Monthly
- System maintenance: Quarterly

**Route-Based Vibration Monitoring:**
- **Critical:** Weekly to monthly
- **Important:** Monthly to quarterly
- **General:** Quarterly to semi-annually

**Thermography:**
- **Critical:** Monthly
- **Important:** Quarterly
- **General:** Annually

**Oil Analysis (Circulating Systems):**
- **Critical:** Monthly
- **Important:** Quarterly
- **General:** Semi-annually
- **New oil:** Before use (quality check)
- **After fill:** Initial sample after startup

**Visual Inspection (In-Service):**
- **Operator rounds:** Daily or per shift
- **Technician inspection:** Weekly to monthly
- **Detailed inspection:** Quarterly to annually (during maintenance)

**Bearing Inspection (Removed):**
- **Scheduled overhaul:** Per equipment maintenance plan
- **Condition-based:** When condition indicates
- **After failure:** Always inspect failed bearing

### 9.3 Adjusting Intervals

**Increase Frequency When:**
- Approaching calculated bearing life
- Condition trending unfavorably
- Operating conditions worsen
- After repairs (verification period)
- Reliability concerns

**Decrease Frequency When:**
- Proven reliability over extended period
- Operating conditions improve
- Low criticality equipment
- Resource constraints (use risk-based prioritization)

**Document Rationale:**
- Record why intervals were chosen
- Review periodically (annually)
- Adjust based on results

## 10. Documentation and Reporting

### 10.1 Inspection Reports

**Contents:**
1. **Header Information:**
   - Equipment ID and description
   - Date and time of inspection
   - Inspector name
   - Environmental conditions (ambient temp, etc.)

2. **Measurements:**
   - Vibration levels (overall, spectral peaks)
   - Temperatures
   - Other parameters as applicable
   - Comparison to baseline and limits

3. **Analysis:**
   - Condition assessment
   - Defect identification
   - Severity rating
   - Trending (stable, increasing, etc.)

4. **Recommendations:**
   - Continue normal operation
   - Increase monitoring frequency
   - Plan maintenance (timeline)
   - Immediate action required

5. **Attachments:**
   - Spectra, time waveforms
   - Trend charts
   - Photos
   - Oil analysis reports

**Distribution:**
- Equipment owner/operator
- Maintenance planner
- Reliability engineer
- File/database

### 10.2 Failure Analysis Reports

**Purpose:**
- Document failure details
- Determine root cause
- Recommend corrective actions
- Share lessons learned

**Contents:**

1. **Executive Summary:**
   - Equipment and failure description
   - Root cause (brief)
   - Recommendations (brief)

2. **Equipment Information:**
   - Equipment ID, description, location
   - Bearing designation and manufacturer
   - Installation date
   - Operating hours at failure

3. **Operating History:**
   - Load, speed, temperature
   - Lubrication type and schedule
   - Condition monitoring history
   - Previous failures or issues
   - Recent changes or events

4. **Failure Description:**
   - Failure mode (seized, vibration, noise, etc.)
   - Events leading to failure
   - Consequence (downtime, damage, safety)

5. **Inspection Findings:**
   - Visual inspection results
   - Photos of damage
   - Defect classification (per ISO 15243 or ГОСТ 20407)
   - Measurements (clearance, dimensions)

6. **Analysis:**
   - Failure mechanism
   - Root cause determination
   - Contributing factors
   - Use of P-F curve or timeline

7. **Laboratory Tests (if performed):**
   - Metallurgical examination
   - Hardness testing
   - Chemical analysis
   - Lubricant analysis

8. **Root Cause:**
   - Primary cause
   - Secondary causes
   - Justification

9. **Recommendations:**
   - Immediate corrective actions
   - Long-term improvements
   - Monitoring or inspection changes
   - Design or operational changes

10. **Attachments:**
    - Photos
    - Analysis results
    - References

**Approval and Distribution:**
- Review by reliability engineer
- Approval by maintenance manager
- Distribution to stakeholders
- File in equipment history

### 10.3 Trending Databases

**Purpose:**
- Store historical data
- Enable trend analysis
- Support decision-making
- Demonstrate compliance

**Software:**
- **Vibration:** Emerson AMS, SKF @ptitude, Fluke Accelix, etc.
- **Oil analysis:** Lab-provided portals, CMMS integration
- **CMMS:** SAP PM, Maximo, MP2, etc.
- **Custom databases:** Excel, Access, SQL databases

**Data to Track:**
- Vibration levels over time (overall, specific frequencies)
- Temperatures
- Oil analysis results
- Inspection findings
- Maintenance actions
- Operating parameters (load, speed, hours)

**Analysis:**
- Automated alarming
- Trend plotting
- Statistical analysis (mean, standard deviation, rate of change)
- Correlation (e.g., vibration vs. load)
- Failure prediction

**Best Practices:**
- Consistent data collection
- Quality control (reject bad data)
- Regular review
- Long-term archiving
- Backup and security

## 11. Root Cause Analysis Framework

### 11.1 RCA Process

**When to Perform RCA:**
- Critical equipment failures
- Repeated failures
- Significant consequence (safety, environmental, cost)
- Chronic reliability issues
- Learning opportunities

**Steps:**

**1. Define the Problem:**
- What failed?
- When did it fail?
- What was the impact?
- Specific, measurable problem statement

**2. Collect Data:**
- Operating history
- Maintenance history
- Condition monitoring data
- Failure inspection findings
- Interview operators and technicians
- Review procedures and documents

**3. Identify Possible Causes:**
- Brainstorm with team
- Use cause categories (equipment, human, system, external)
- Develop comprehensive list

**4. Determine Root Cause(s):**
- Use analysis tools (5-Whys, Fishbone diagram, Fault Tree)
- Verify with evidence
- Distinguish root cause from symptoms and contributing factors

**5. Develop Recommendations:**
- Address root causes
- Prioritize by impact and feasibility
- Include short-term and long-term actions
- Assign responsibility

**6. Implement and Track:**
- Execute recommendations
- Monitor effectiveness
- Document results
- Close out when effective

### 11.2 RCA Tools

**5-Whys:**
- Ask "why" repeatedly to drill down to root cause
- Typically 5 iterations reveals root cause
- Simple and effective for straightforward issues

**Example:**
1. Why did the bearing fail? - Overheating
2. Why did it overheat? - Inadequate lubrication
3. Why was lubrication inadequate? - Wrong grease type used
4. Why was wrong grease used? - Technician selected from shelf
5. Why was wrong grease on shelf? - No labeling system for lubricants

Root cause: Lack of lubricant storage organization and labeling

**Fishbone (Ishikawa) Diagram:**
- Visual tool for categorizing causes
- Categories: Machine, Method, Material, Manpower, Measurement, Environment
- Helps ensure comprehensive analysis

**Fault Tree Analysis:**
- Logic diagram showing failure paths
- Top event: The failure
- Lower levels: Contributing factors
- Boolean logic (AND, OR gates)
- Quantitative or qualitative

**FMEA (Failure Modes and Effects Analysis):**
- Systematic review of potential failure modes
- Assess severity, occurrence, detection
- Prioritize risks (RPN - Risk Priority Number)
- Develop mitigation plans
- Proactive tool (before failures occur)

### 11.3 Common Root Causes for Bearing Failures

**Lubrication-Related (Most Common):**
1. Wrong lubricant type or grade
2. Inadequate quantity
3. Contaminated lubricant
4. Re-lubrication interval too long
5. Grease gun contamination
6. Mixing incompatible greases

**Installation/Mounting:**
1. Improper mounting techniques (hammering)
2. Incorrect fits (too tight or too loose)
3. Misalignment during installation
4. Shaft or housing surface finish inadequate
5. Contamination during installation
6. Incorrect heating (overheating)

**Operational:**
1. Overload (beyond bearing rating)
2. Shock loads
3. Excessive speed
4. Vibration from nearby equipment
5. Misalignment during operation (shaft deflection, thermal growth)

**Maintenance:**
1. Inadequate condition monitoring
2. Delayed response to alarms
3. Poor maintenance procedures
4. Lack of training
5. Spare parts quality issues

**Design/Selection:**
1. Bearing undersized for application
2. Wrong bearing type for loads/speeds
3. Inadequate sealing
4. Poor lubrication system design
5. Shaft/housing design issues (deflection, tolerances)

**System/Organizational:**
1. Inadequate procedures
2. Lack of training
3. Poor communication
4. Budget constraints delaying maintenance
5. No standardization of parts/lubricants

## 12. Advanced Topics

### 12.1 Machine Learning in Bearing Diagnostics

**Applications:**
- Automated fault classification
- Anomaly detection
- Remaining life prediction
- Optimization of alarm thresholds

**Approaches:**
- Supervised learning: Trained on labeled fault data
- Unsupervised learning: Detects anomalies without labels
- Deep learning: Neural networks on raw vibration data

**Benefits:**
- Handle complex patterns
- Improve with more data
- Reduce false alarms

**Challenges:**
- Requires large datasets
- "Black box" - difficult to interpret
- Need for domain expertise in implementation

### 12.2 Wireless Sensors

**Advantages:**
- Easy installation (no wiring)
- Flexible placement
- Cost-effective for distributed monitoring

**Limitations:**
- Battery life (power management)
- Data rate (bandwidth constraints)
- Reliability in harsh environments

**Applications:**
- Difficult-to-wire locations
- Temporary monitoring
- Large numbers of measurement points

### 12.3 Lubrication Condition Monitoring

**In-Line Oil Condition Sensors:**
- Viscosity
- Dielectric constant (water detection)
- Particle counting
- Ferrous density

**Benefits:**
- Real-time oil condition
- Early warning of degradation
- Optimize oil change intervals

**Integration:**
- Tie into plant DCS/SCADA
- Alarming on exceedances
- Trend analysis

## Quick Reference: Diagnostic Method Selection

| Symptom/Situation | Primary Diagnostic Method | Secondary Method |
|-------------------|---------------------------|------------------|
| Routine monitoring | Vibration (route or online) | Thermography |
| Early defect suspected | Envelope analysis | Acoustic emission |
| Lubrication issue | Oil analysis, temperature | Ultrasonic (grease) |
| Slow speed equipment | Acoustic emission, ultrasonic | Vibration (envelope) |
| High-speed equipment | Vibration (velocity, envelope) | Temperature |
| Inaccessible equipment | Online monitoring | Thermography |
| Contamination suspected | Oil analysis (particle count, ferrography) | Visual inspection |
| Overheating | Temperature, thermography | Lubrication analysis |
| Unusual noise | Vibration analysis (FFT) | Visual inspection when possible |
| After maintenance | Vibration baseline | Temperature |

---

**Document Version:** 1.0  
**Last Updated:** 2024  
**Status:** Complete - Comprehensive diagnostics workflow reference
