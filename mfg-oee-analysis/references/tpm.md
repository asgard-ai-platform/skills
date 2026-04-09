# TPM — Total Productive Maintenance

TPM is the organizational system that sustains OEE improvements. Without TPM, OEE gains from one-off projects decay within months as equipment degrades and losses creep back. With TPM, OEE improvement becomes a repeatable, operator-owned process.

## TPM and OEE: The Relationship

OEE measures the **result**. TPM is the **system** that produces it.

```
OEE diagnosis → identifies which of the Six Big Losses dominates
TPM pillar    → provides the structured intervention for that loss type
```

| Dominant OEE Loss | Corresponding TPM Pillar |
|-------------------|------------------------|
| Availability ↓ (breakdowns) | Planned Maintenance (PM) + Early Equipment Management |
| Availability ↓ (changeover) | Focused Improvement (Kobetsu-Kaizen) |
| Performance ↓ (minor stops, slow running) | Autonomous Maintenance (AM) |
| Quality ↓ (defects, startup rejects) | Quality Maintenance (Hinshitsu-Hozen) |

## The Eight TPM Pillars

Original Nakajima TPM model (JIPM, 1988). Most plants implement pillars 1-4 first.

| # | Pillar | Japanese Name | Core Purpose |
|---|--------|--------------|-------------|
| 1 | Autonomous Maintenance | Jishu-Hozen | Operators perform basic equipment care |
| 2 | Planned Maintenance | Keikaku-Hozen | Maintenance team prevents failures |
| 3 | Focused Improvement | Kobetsu-Kaizen | Cross-functional teams eliminate specific losses |
| 4 | Quality Maintenance | Hinshitsu-Hozen | Zero defects through equipment condition control |
| 5 | Early Equipment Management | — | Design maintainability into new equipment |
| 6 | Training & Education | — | Build skills for pillars 1-4 |
| 7 | Safety, Health & Environment | — | Zero accidents |
| 8 | TPM in Administration | Jimusho TPM | Apply TPM thinking to office processes |

---

## Pillar 1 — Autonomous Maintenance (AM)

**Core idea**: Transfer basic maintenance tasks (cleaning, inspection, lubrication, minor adjustments) from the maintenance department to operators. Operators know their machines; they detect anomalies earliest.

### The 7-Step AM Progression

Each step must be audited before proceeding to the next. Typical timeline: 18-36 months to reach Step 7.

| Step | Name | What Operators Do | OEE Impact |
|------|------|-------------------|-----------|
| 1 | Initial cleaning | Clean machine thoroughly; tag every defect found (fuguai) | Baseline — exposes hidden problems |
| 2 | Eliminate contamination sources | Fix leaks, reduce spatter, shorten cleaning time | Performance ↑ (fewer minor stops) |
| 3 | Cleaning & lubrication standards | Write Operator Standards Sheets (OSSs); specify time, method, tools | Availability ↑ (prevents lubrication-related failures) |
| 4 | General inspection | Train operators on machine mechanisms; inspect per checklist | Availability ↑ (detects deterioration early) |
| 5 | Autonomous inspection | Operators self-manage inspection; maintenance reviews | All three factors stabilize |
| 6 | Standardization | Visual management; organized workplace (5S integrated) | Performance ↑ (faster minor stop recovery) |
| 7 | Autonomous management | Operators set targets, analyze data, drive improvement | OEE ownership shifts to floor |

### Fuguai Tagging

A "fuguai" (不具合 — abnormality) tag is the core AM tool.

```
Tag fields:
  Machine ID:     ___________
  Date found:     ___________
  Operator ID:    ___________
  Location:       ___________
  Abnormality:    ___________   (describe what you see/hear/smell)
  Severity:       Safety / Critical / Minor
  Action needed:  Operator can fix / Needs maintenance / Needs engineering
  Status:         Open / In-progress / Closed
```

**Red tags** = operator cannot fix, escalate to maintenance.
**Blue tags** = operator can fix with training or simple tools.

Track open tag count weekly. A backlog of red tags > 10% of machines is a maintenance capacity problem, not an AM problem.

---

## Pillar 2 — Planned Maintenance (PM)

**Core idea**: Shift maintenance from reactive (fix after failure) to proactive (prevent failures before they cause downtime).

### Maintenance Strategy Matrix

Not all equipment needs the same strategy. Select by failure consequence and failure predictability:

```
                High Consequence
                (Safety / Line-stop)
                        │
         ───────────────┼───────────────
         Predictable    │  Unpredictable
         failure mode   │  failure mode
                        │
   TBM (Time-Based) ───►│◄─── CBM (Condition-Based)
   Replace on schedule  │    Monitor; act on signal
                        │
         ───────────────┼───────────────
                        │
                Low Consequence
                (Run-to-failure OK)
```

| Strategy | When to Use | Typical Cost vs Reactive |
|----------|-------------|--------------------------|
| Run-to-Failure (RTF) | Low consequence, no pattern | Lowest — but unpredictable |
| Time-Based Maintenance (TBM) | Known wear rate, safety-critical | 2-3× higher than RTF |
| Condition-Based Maintenance (CBM) | High consequence, detectable signal | 3-5× setup cost, lower long-run |
| Predictive Maintenance (PdM) | High consequence, sensor feasible | Highest setup, lowest failure rate |

### Maintenance Cost Calculation

IRON LAW from SKILL.md applies: failures compound. A single unplanned breakdown at 60 min downtime costs:

```
Availability loss = 60 / 480 = 12.5%
OEE impact = 12.5% × Performance × Quality

Example: 87.5% → 75.0% Availability
OEE drop: (87.5% × 90.5% × 94.7%) = 75.0%
         → (75.0% × 90.5% × 94.7%) = 64.3%

Lost OEE: 10.7 percentage points from one 60-min breakdown
```

If the machine runs 20 shifts/month and each breakdown costs 60 min, annualized OEE cost often exceeds the cost of a CBM sensor installation in 6-12 months.

### PM Interval Setting

For TBM, set intervals using Weibull analysis on historical failure data:

```
Weibull parameters from MTBF data:
  β (shape) > 1  → wear-out failure; TBM interval = 0.7 × MTBF
  β = 1          → random failure; TBM doesn't help — use RTF or CBM
  β < 1          → infant mortality; improve installation/commissioning

Conservative rule without Weibull data:
  PM interval = 0.6 × (average time between failures)
```

---

## Pillar 3 — Focused Improvement (Kobetsu-Kaizen)

**Core idea**: Assign cross-functional teams to eliminate specific, measured losses. Each project targets one loss from the Six Big Losses with a defined OEE improvement goal.

### Project Selection: Loss Pareto

Before assigning teams, run a loss Pareto across all machines for 4 weeks of data:

```
Rank losses by minutes lost (not by frequency):

Loss Type          | Total Min Lost | % of All Lost Time
-------------------|---------------|-------------------
Equipment Failure  | 1,440         | 38%   ← Attack this first
Setup/Changeover   | 960           | 25%
Reduced Speed      | 720           | 19%
Minor Stops        | 480           | 13%
Process Defects    | 120           | 3%
Startup Rejects    | 60            | 2%
```

Focus the first team on Equipment Failure (38%). A 50% reduction in Equipment Failure recovers 720 min/month — more impact than eliminating all defects.

### SMED for Changeover (Availability Loss #2)

Single-Minute Exchange of Die (SMED) is the standard Focused Improvement technique for setup time.

**4-Step SMED Procedure:**

**Step 1 — Observe and record**
Videotape the entire changeover. Record every action, its start time, and duration.

**Step 2 — Classify: Internal vs External**
- **Internal**: Can only be done while machine is stopped (die change, alignment)
- **External**: Can be done while machine is running (staging materials, pre-heating dies)

```
Typical Before SMED:
  Total changeover: 90 min
  Internal: 90 min (everything done after machine stops)

After Step 2 — Convert Externals:
  Internal: 55 min  ← machine stopped
  External: 35 min  ← done before/after machine stop
```

**Step 3 — Streamline internal activities**
- Standardize bolt sizes (one tool for all fasteners)
- Add locating pins to eliminate alignment steps
- Use quick-release clamps instead of bolts
- Parallel task assignments (two operators doing different internal tasks simultaneously)

**Step 4 — Streamline external activities**
- Pre-stage all materials on a changeover cart
- Pre-heat dies in a warming oven
- Pre-set parameters on a secondary control panel

```
Typical After SMED:
  Internal: 22 min  (down from 55 — parallel work, quick clamps)
  External: 35 min  (unchanged)
  Net machine-stopped time: 22 min (down from 90 min)
  
  Changeover Availability gain per shift with 2 changeovers:
  Before: (480 - 180) / 480 = 62.5%
  After:  (480 - 44) / 480  = 90.8%
  OEE Availability gain: +28.3 percentage points
```

---

## Pillar 4 — Quality Maintenance (Hinshitsu-Hozen)

**Core idea**: Link defect occurrence to specific equipment conditions. If the machine is in a known good state (tolerances within spec, parameters within range), defects cannot occur. Zero defects is achieved through controlling conditions, not through inspection.

### QM Matrix

Map defect types to machine components that can cause them:

```
         │ Spindle  │ Fixture  │ Tool    │ Coolant │ Feed Rate
─────────┼──────────┼──────────┼─────────┼─────────┼──────────
Burring  │    ◎     │          │    ○    │         │    ○
Oversize │    ◎     │    ○     │         │         │    ◎
Scratch  │          │    ◎     │    ○    │    ○    │
Void     │          │          │         │    ◎    │

◎ = Primary cause   ○ = Contributing cause
```

For each ◎ cell, define:
1. The measurable equipment condition (e.g., spindle runout ≤ 0.003 mm)
2. The inspection method (dial indicator at spindle nose)
3. The inspection frequency (daily, before production start)
4. The action if out-of-spec (halt line, notify maintenance)

This converts quality control from post-process inspection to pre-process condition verification.

---

## OEE Improvement Roadmap with TPM

Typical 3-year roadmap. Actual timelines vary significantly by plant size and management commitment.

```
Year 1: Foundation
  ├─ 5S throughout plant (prerequisite for all pillars)
  ├─ AM Steps 1-3 on worst-performing machines
  ├─ PM: Eliminate reactive maintenance on top 3 failure modes
  └─ First Focused Improvement project (top Pareto loss)
  Target OEE lift: +5 to +10 percentage points

Year 2: Capability Building
  ├─ AM Steps 4-5 plant-wide
  ├─ PM: Implement CBM on 2-3 critical machines
  ├─ SMED projects on top 2 changeover losses
  └─ QM Matrix for top 2 defect types
  Target OEE lift: +8 to +12 percentage points additional

Year 3: Sustain & Extend
  ├─ AM Steps 6-7; operators own OEE data for their machines
  ├─ PM: PdM pilot (vibration analysis, oil analysis)
  ├─ Pillar 5: Incorporate maintainability specs in next equipment purchase
  └─ TPM extended to support processes (logistics, toolroom)
  Target OEE lift: +5 to +8 percentage points additional
```

Cumulative: a plant starting at 60% OEE can realistically reach 78-85% over three years with consistent TPM implementation.

---

## Common TPM Failure Modes

These are organizational failures, not technical ones.

| Failure Mode | Symptom | Correction |
|-------------|---------|-----------|
| **AM as janitorial work** | Operators clean but never inspect; tag count stays near zero | Re-train Step 1 with machine mechanisms education; require minimum tag count |
| **Maintenance won't close tags** | Red tag backlog grows; operators stop tagging | Track tag closure rate (target: >80% closed within 2 weeks); escalate in ops review |
| **PM schedules set by guesswork** | PM every 3 months because "it feels right"; failures still occur | Pull 12 months failure logs; set interval at 0.6× actual MTBF |
| **Focused Improvement projects without data** | Team discusses problems, proposes solutions, no baseline OEE measurement | Require 4-week baseline before any project starts; no before/after comparison = project invalid |
| **TPM as a certification exercise** | Documents created for audit; actual practice unchanged | Tie TPM pillar progress to manager KPIs, not to audit scores |
| **Skipping 5S prerequisite** | AM cleaning takes 3× as long; standards can't be written for chaotic workplaces | 5S audit score >3.5/5.0 required before AM Step 1 starts on any machine |

---

## Key Metrics by Pillar

Track these to verify TPM pillars are functioning, not just to report completion.

| Pillar | Leading Metric | Lagging Metric |
|--------|---------------|----------------|
| AM | Open fuguai tag count; OSSs written | Minor stop frequency (Performance factor) |
| PM | % planned vs reactive maintenance hours | MTBF trend; Availability factor |
| Focused Improvement | Projects completed; OEE delta per project | Cumulative OEE gain |
| Quality Maintenance | Equipment condition inspection compliance | First-pass yield; Quality factor |

**Target for mature TPM**: Planned maintenance ≥ 80% of total maintenance hours. Plants below 50% planned are still in reactive mode regardless of what their TPM documents say.
