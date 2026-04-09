# Sensor Selection Guide for Predictive Maintenance

This guide expands the sensor table in `SKILL.md` into a decision framework with specific thresholds, installation rules, and worked examples. The goal: given an equipment type and failure mode, identify the right sensor and placement.

---

## Sensor-to-Failure Mode Mapping

| Failure Mode | Primary Sensor | Secondary Sensor | Why |
|---|---|---|---|
| Bearing wear (rolling element) | Vibration (high-freq) | Temperature | Bearing defect frequencies appear in vibration spectrum before heat rises |
| Bearing wear (sleeve/journal) | Oil debris | Vibration (low-freq) | Metal particles shed early; vibration is a late indicator for sleeve bearings |
| Shaft imbalance | Vibration (1× RPM) | None | Pure imbalance = single frequency spike at 1× running speed |
| Misalignment | Vibration (2× RPM) | Temperature (coupling) | 2× harmonic is the diagnostic signature; misalignment heats coupling |
| Cavitation (pump) | Acoustic / Ultrasound | Vibration (broadband) | Cavitation generates broadband noise 20–100 kHz; vibration shows it but noisier |
| Electrical winding fault | Current (Motor Current Sig. Analysis) | Temperature (winding) | MCSA detects rotor bar cracks, stator faults from current spectrum |
| Gear tooth wear | Vibration (gear mesh freq.) | Oil debris | Gear mesh frequency (GMF) = RPM × tooth count; wear shifts sidebands |
| Hydraulic seal leak | Acoustic / Ultrasound | Pressure differential | Turbulent flow through leak creates ultrasonic signature |
| Overload / thermal runaway | Temperature + Current | Vibration | Load > rating heats winding/insulation; current rises proportionally |
| Contaminated oil / gearbox | Oil analysis (particle count) | Vibration | Chemical degradation precedes mechanical damage by weeks |

---

## Vibration Sensors — Detailed Selection

### Sensor Type Decision

```
Is running speed known and stable?
├── Yes → Use accelerometer (MEMS or piezo ICP)
│         └── Is frequency of interest > 10 kHz?
│             ├── Yes → High-frequency piezo (resonant freq > 30 kHz)
│             └── No  → General-purpose ICP accelerometer (100 Hz–10 kHz flat)
└── No  → Use velocity sensor or non-contact proximity probe
          └── Is shaft displacement important (large journal bearings)?
              ├── Yes → Eddy current proximity probe (0–1 kHz, DC-coupled)
              └── No  → Velocity sensor (geophone, 10 Hz–2 kHz)
```

### Frequency Ranges for Common Faults

| Fault | Diagnostic Frequency | Example at 1,500 RPM (25 Hz) |
|---|---|---|
| Imbalance | 1× RPM | 25 Hz |
| Misalignment | 2× RPM (and 1×) | 50 Hz |
| Looseness | 0.5×, 1×, 2×, 3× RPM (sub/super harmonics) | 12.5, 25, 50, 75 Hz |
| Bearing BPFO (outer race) | BPFO formula (see below) | typically 3–8× RPM |
| Bearing BPFI (inner race) | BPFI formula | typically 5–10× RPM |
| Gear mesh | RPM × number of teeth | 1,500 RPM × 24 teeth = 600 Hz |

**Bearing Defect Frequencies (calculated, not measured):**

```
BPFO = (N/2) × RPM × (1 − (d/D)cosα)
BPFI = (N/2) × RPM × (1 + (d/D)cosα)
BSF  = (D/2d) × RPM × (1 − (d/D)²cos²α)
FTF  = (RPM/2) × (1 − (d/D)cosα)
```

Where:
- `N` = number of rolling elements
- `d` = rolling element diameter
- `D` = pitch circle diameter
- `α` = contact angle (typically 0° for radial bearings → cosα = 1)
- RPM in revolutions per second (Hz) for result in Hz

**Worked Example — SKF 6205 bearing at 1,500 RPM:**

```
N = 9 balls, d = 7.94 mm, D = 38.5 mm, α = 0°

Shaft frequency = 1500/60 = 25 Hz

BPFO = (9/2) × 25 × (1 − 7.94/38.5) = 4.5 × 25 × 0.794 = 89.3 Hz
BPFI = (9/2) × 25 × (1 + 7.94/38.5) = 4.5 × 25 × 1.206 = 135.7 Hz
BSF  = (38.5/(2×7.94)) × 25 × (1 − (7.94/38.5)²) = 2.424 × 25 × 0.957 = 57.9 Hz
```

Install the accelerometer at the bearing housing, radial direction. Look for energy at 89.3 Hz and harmonics (178.6, 267.9 Hz) for outer race defects.

### Accelerometer Placement Rules

```
1. Mount on load path, not on sheet metal covers
   ✓ On bearing housing, main frame casting
   ✗ On access panel, thin brackets

2. Radial direction for radial loads (most bearings)
   Axial direction for thrust bearing assessment

3. Mount method affects usable frequency range:
   ┌─────────────────┬──────────────────┬──────────────────┐
   │ Mount Method    │ Usable Freq (kHz)│ Typical Use      │
   ├─────────────────┼──────────────────┼──────────────────┤
   │ Stud (tapped)   │ Up to 20–30 kHz  │ Permanent, best  │
   │ Adhesive pad    │ Up to 10–15 kHz  │ Permanent, good  │
   │ Magnetic base   │ Up to 5–7 kHz    │ Temporary/survey │
   │ Hand-held probe │ Up to 1–2 kHz    │ Walk-around only │
   └─────────────────┴──────────────────┴──────────────────┘

4. Minimum distance from sensor to fault: none — closer = better SNR
   Avoid mounting across a joint or weld if possible
```

---

## Temperature Sensors — Detailed Selection

Temperature is a **lagging indicator** for most mechanical faults (vibration precedes by hours to weeks). Use temperature as a confirmation channel, not the primary alert.

### Sensor Type Selection

| Sensor | Range | Accuracy | Use Case |
|---|---|---|---|
| PT100 RTD | −50 to +400°C | ±0.3°C | Motor winding, bearing housing (contact, wired) |
| Type K Thermocouple | −200 to +1260°C | ±1–2°C | High-temperature environments, exhaust, kilns |
| NTC Thermistor | −55 to +150°C | ±0.1°C (narrow range) | Motor winding embedded measurement |
| IR Pyrometer (non-contact) | 0 to +1000°C | ±1–2% | Moving parts, electrical panels (cannot touch) |
| Thermal camera | −20 to +650°C | ±2°C | Walk-around survey, electrical switchgear, large areas |

### Temperature Thresholds for Common Equipment

These are starting-point alarm levels; adjust for your specific equipment rating and ambient conditions:

```
Electric Motor (TEFC, Class F insulation, rated 105°C rise):
  Winding temperature: 
    Warning: >115°C
    Trip:    >130°C (or 155°C absolute for Class F)
  Bearing temperature:
    Warning: ambient + 40°C
    Trip:    ambient + 60°C  (or >95°C absolute)

Gearbox oil temperature:
    Warning: >80°C
    Trip:    >95°C

Hydraulic oil temperature:
    Warning: >65°C
    Trip:    >75°C

Transformer (oil-cooled):
    Top oil temperature:
    Warning: >85°C
    Trip:    >95°C
```

**Delta-T rule**: More reliable than absolute thresholds. Alert when temperature rises faster than `X °C/hour` where `X` is determined from baseline:

```
Baseline delta-T (normal load): collected over 30-day baseline period
Alert threshold = mean_deltaT + 3 × std_deltaT
```

---

## Current / MCSA Sensors — Detailed Selection

Motor Current Signature Analysis (MCSA) detects electrical and mechanical faults from the AC supply current waveform. No physical access to rotating parts needed — clip the CT onto the supply cable.

### What MCSA Detects

| Fault | Frequency Signature |
|---|---|
| Rotor bar crack | Sidebands at `f_s ± 2s·f_s` where `s` = slip, `f_s` = supply freq |
| Stator eccentricity | Sidebands at `f_s ± k·f_r` where `f_r` = rotor frequency |
| Bearing fault (via load fluctuation) | Sidebands at `f_s ± f_bearing_defect` |
| Mechanical imbalance | Sideband at `f_s ± f_rotation` |

**Rotor Bar Fault Example:**
```
Supply frequency: 50 Hz
Motor: 4-pole, running at 1485 RPM → slip s = (1500−1485)/1500 = 0.01

Rotor bar fault sidebands = 50 ± 2×0.01×50 = 50 ± 1 Hz = 49 Hz and 51 Hz

Alert when amplitude at 49 or 51 Hz rises above −50 dB relative to 50 Hz fundamental
(healthy motor typically shows these sidebands below −60 dB)
```

### CT Selection

- **Accuracy class**: Class 0.5 or better for MCSA (Class 1 is insufficient for sideband detection)
- **Ratio**: Select so motor full-load current falls in 60–80% of CT primary rating
- **Bandwidth**: CT must be flat to at least 2 kHz for higher-order harmonics

---

## Acoustic / Ultrasound Sensors

Useful range: 20 kHz–100 kHz (ultrasonic). Human ear tops out at ~20 kHz, so this range is free from ambient noise.

### Applications

| Application | Frequency Band | Detection Threshold |
|---|---|---|
| Air/gas leak detection | 35–45 kHz | Leaks ≥ 1 mm orifice at 3 bar |
| Steam trap failure | 38–42 kHz | Distinguishes live steam bypass from healthy trap |
| Bearing lubrication need | 25–40 kHz | dB rise > 8 dB above baseline = lubrication needed |
| Electrical arcing / corona | 35–50 kHz | Any dB signal in quiescent electrical cabinet |
| Cavitation in pump | 20–40 kHz | Broadband noise floor rise of > 10 dB |

### Portable vs. Permanent

```
Portable (handheld wand):
  ✓ Low cost, survey-based
  ✓ Good for leak detection routes
  ✗ Operator-dependent
  ✗ Cannot trend over time automatically

Permanent (flush-mounted or waveguide):
  ✓ Continuous trending, automated alerts
  ✓ Detects intermittent faults
  ✗ Higher cost per point
  ✗ Requires cable routing to data acquisition
```

For predictive maintenance (continuous trending), permanent sensors are required. Portable is adequate for lubrication management routes.

---

## Oil Analysis — When to Use and What to Measure

Oil analysis is the correct first sensor for:
- Gearboxes (enclosed oil bath)
- Hydraulic systems
- Large diesel engines
- Any equipment where lubrication condition drives failure

### Parameters and What They Mean

| Parameter | Test Method | Indicates |
|---|---|---|
| Particle count (ISO 4406) | Laser particle counter | Overall contamination level; trending up = wear or ingress |
| Wear metals (Fe, Cu, Cr, Al) | ICP spectroscopy | Source of wear: Fe = steel/cast iron, Cu = bronze/brass bearings |
| Viscosity (cSt @ 40°C, 100°C) | ASTM D445 | Oil degradation, wrong oil, dilution |
| Acid Number (AN) | ASTM D664 | Oxidation / oil life remaining |
| Water content (ppm) | Karl Fischer titration | Seal failure, condensation |
| Particle morphology | Ferrography | Shape of wear particles reveals mechanism (fatigue = spherical, adhesive = platelets) |

### ISO 4406 Cleanliness Code (Quick Reference)

```
Code format: X/Y/Z
  X = particles ≥ 4 µm per 100 mL (range code)
  Y = particles ≥ 6 µm per 100 mL
  Z = particles ≥ 14 µm per 100 mL

Range codes:
  Code 14 = 80–160 particles     (very clean)
  Code 16 = 320–640 particles    (clean)
  Code 18 = 1300–2500 particles  (typical in-service)
  Code 20 = 5000–10000 particles (contaminated — action required)
  Code 22 = 20000–40000 particles (severely contaminated)

Typical target cleanliness for:
  Hydraulic servo systems: 15/13/10
  Gearboxes (precision):   17/15/13
  Gearboxes (industrial):  18/16/13
```

**Alarm Logic**: Alert when particle count class increases by ≥ 2 codes in a single sampling interval, regardless of absolute level. Rate-of-change matters more than absolute level.

### Sampling Frequency

```
Equipment Type          | New/Unknown | Established | Critical
─────────────────────────────────────────────────────────────
High-speed gearbox      | Monthly     | Quarterly   | Monthly
Hydraulic system        | Monthly     | Quarterly   | Monthly
Industrial gearbox      | Quarterly   | Semi-annual | Quarterly
Diesel engine (large)   | Per 250 hr  | Per 500 hr  | Per 250 hr
```

---

## Sensor Placement Decision Worksheet

For each piece of equipment to instrument, work through these four steps:

**Step 1: Identify the credible failure modes**

Use the failure history, FMEA, or manufacturer documentation. List the top 3 failure modes by cost × frequency.

**Step 2: Match failure mode to sensor type**

Use the Sensor-to-Failure Mode table at the top of this document.

**Step 3: Determine P-F interval**

```
Failure Mode              | Typical P-F Interval
──────────────────────────────────────────────────
Bearing wear (vibration)  | 1–6 weeks
Electrical winding fault  | 1–4 weeks
Gearbox oil degradation   | 4–12 weeks
Seal leak (acoustic)      | Days to weeks
Cavitation damage         | Hours to days (fast!)
Shaft imbalance buildup   | Weeks to months
```

If P-F interval < 1 week, you need continuous monitoring, not periodic routes.

**Step 4: Choose monitoring approach**

```
P-F Interval ≥ 4 weeks  → Periodic route (technician, portable equipment) viable
P-F Interval 1–4 weeks  → Permanent sensor with weekly automated report
P-F Interval < 1 week   → Permanent sensor with real-time alert (< 1 hr latency)
```

---

## Sensor Count Estimation for Budget Planning

Rule of thumb for a rotating equipment train (motor + gearbox + driven load):

```
Minimum instrumentation (detect major faults only):
  2 vibration sensors (motor DE bearing, gearbox output bearing)
  1 temperature sensor (motor winding)
  1 current transformer (motor supply)
  ─────────────────────────────────────────────────────
  Total: 4 sensors per train

Full instrumentation (detect 90%+ of credible faults):
  4–6 vibration sensors (all bearing housings, radial + axial)
  3–4 temperature sensors (motor winding, motor NDE bearing, gearbox oil)
  1 current transformer
  1 oil debris sensor (if gearbox is enclosed)
  ─────────────────────────────────────────────────────
  Total: 9–12 sensors per train
```

Start with minimum instrumentation. Add channels after baseline data confirms which additional failure modes are present.

---

## Common Mistakes

**Wrong sensor for the failure mode**: Installing temperature sensors to detect bearing wear. Temperature rises only in the final stage of bearing failure — well after vibration has already shown the problem for days or weeks.

**Under-sampling rate**: Nyquist theorem requires sample rate ≥ 2× maximum frequency of interest. For gear mesh at 2 kHz, you need ≥ 4 kHz sample rate. Many cheap IoT sensors sample at 200 Hz — useless for bearing and gear diagnostics.

**Cable routing through interference sources**: Running sensor cables parallel to motor power cables induces noise that masks fault signatures. Cross power cables at 90°; use shielded cable; ground shield at one end only.

**Baseline collected during abnormal conditions**: If you collect your "healthy" baseline during a run-in period, after maintenance, or at partial load, the baseline is wrong. Collect baseline at steady-state normal operating load for ≥ 30 days.

**Single threshold for variable load**: Vibration and temperature scale with load. A threshold calibrated at 100% load will produce false alarms at 50% load and miss faults at 150% load. Use load-normalized thresholds or segment data by operating condition.

**Over-relying on periodic oil sampling for fast-degrading systems**: If a hydraulic servo system can go from clean to damaged in 72 hours (due to seal ingress), monthly sampling will always be too late. Match sampling frequency to the failure speed.
