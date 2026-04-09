# S / O / D Scoring Rubrics for FMEA

These tables and calibration notes support consistent scoring across team members. Use them during FMEA workshops to align before scoring begins, not after disputes arise.

---

## Severity (S) — Effect on the Customer

Severity is immutable: it reflects what happens to the **customer** if the failure mode reaches them, independent of likelihood or detection capability. Do not lower S because the failure is rare or easily caught.

| S | Effect Description | Automotive Example | Medical Device Example |
|---|---|---|---|
| 10 | Hazard without warning. May injure end user or violate regulation. | Brake failure at highway speed | Insulin pump over-doses without alarm |
| 9 | Hazard with warning. User is warned before harm occurs. | Steering loss with dashboard alert | Infusion pump under-doses, alarm sounds |
| 8 | Loss of primary function. Product is inoperable. | Vehicle won't start | Device powers off mid-therapy |
| 7 | Degraded primary function. Product operable but impaired. | Engine runs rough, reduced power | Flow rate 20% below setpoint |
| 6 | Loss of secondary function. Comfort/convenience lost. | A/C fails in summer | Device logging fails |
| 5 | Degraded secondary function. | Seat adjustment sluggish | Touch screen slow to respond |
| 4 | Cosmetic/fit-finish defect noticed by most users. | Paint blemish visible at arm's length | Housing scratch on visible panel |
| 3 | Cosmetic defect noticed by discerning users. | Minor surface texture variation | Slight color mismatch on label |
| 2 | Barely perceptible effect. | Faint trim rattle at high speed | Mild vibration during operation |
| 1 | No discernible effect. | — | — |

**Calibration anchor:** If a failure mode can result in regulatory non-compliance (FDA, IATF, ISO 13485 field safety), the minimum S is 9. If it involves potential injury, S = 10.

### Common Severity Mis-scorings

| Mistake | Correct logic |
|---|---|
| "We added a warning label, so S drops to 8" | Labels are detection/prevention controls, not severity reducers |
| "The failure is transient so S=5" | Severity = worst credible effect, not average effect |
| "Customer can work around it, so S=4" | Workaround = degraded primary function → S=7 |
| Scoring S based on internal cost, not customer impact | S must reflect the end user or next-process customer |

---

## Occurrence (O) — Frequency of the Root Cause

Occurrence scores the **likelihood that the root cause results in the failure mode**, given current prevention controls. This is the score you can reduce through design changes, process improvements, or supplier controls.

| O | Probability of Occurrence | Cpk Equivalent | Process PPM |
|---|---|---|---|
| 10 | ≥ 1 in 2 | Cpk < 0.33 | ≥ 500,000 |
| 9 | 1 in 8 | Cpk ≈ 0.33–0.51 | ~125,000 |
| 8 | 1 in 20 | Cpk ≈ 0.51–0.67 | ~50,000 |
| 7 | 1 in 80 | Cpk ≈ 0.67–0.83 | ~12,500 |
| 6 | 1 in 400 | Cpk ≈ 0.83–1.00 | ~2,500 |
| 5 | 1 in 2,000 | Cpk ≈ 1.00–1.17 | ~500 |
| 4 | 1 in 15,000 | Cpk ≈ 1.17–1.33 | ~67 |
| 3 | 1 in 150,000 | Cpk ≈ 1.33–1.50 | ~6.7 |
| 2 | 1 in 1,500,000 | Cpk ≈ 1.50–1.67 | ~0.7 |
| 1 | < 1 in 1,500,000 | Cpk > 1.67 | < 0.7 |

**No historical data?** Use engineering judgment with explicit documentation: "Estimated O=6 based on similar material in prior program; update when production data is available." Document the rationale — an undocumented guess is a liability.

### Occurrence Scoring Decision Tree

```
Is there field/warranty data from similar parts/processes?
├─ YES → Calculate actual PPM or Cpk → look up table above
└─ NO
    ├─ Similar part/process exists in engineering history?
    │   ├─ YES → Use analogous PPM, note it's analogous
    │   └─ NO → Is there a prevention control (poka-yoke, SPC)?
    │       ├─ YES → Start at O=5, adjust for control robustness
    │       └─ NO → Start at O=7 (unknown, uncontrolled)
    └─ Is the cause well-understood physics/chemistry?
        ├─ YES (mature failure mechanism) → O=3–4
        └─ NO (novel material, untested condition) → O=6–8
```

### Common Occurrence Mis-scorings

| Mistake | Correct logic |
|---|---|
| "We've never seen this fail" → O=1 | Never seeing it may mean no data, not zero probability |
| Including detection controls when scoring O | O reflects prevention only; detection ≠ prevention |
| Using field returns without adjusting for sample size | 0 returns on 100 units ≠ 0 returns on 1,000,000 units |
| Anchoring on best-case process capability | Use actual Cpk from production, not SPC target |

---

## Detection (D) — Ability to Find the Failure Before It Reaches the Customer

Detection scores the **effectiveness of current detection controls** at catching the failure mode (or its cause) before it reaches the end customer. Lower D = better detection. D=10 means no detection at all.

| D | Detection Capability | Control Type Examples |
|---|---|---|
| 10 | No current detection control | No inspection, no test |
| 9 | Control unlikely to detect. Indirect or random check. | Visual inspection, random audit <10% |
| 8 | Control may detect. Manual visual inspection, 100%. | 100% operator visual |
| 7 | Control has low chance of detection. Post-process attribute check. | Go/no-go gauge on finished part |
| 6 | Control has moderate chance. Variable measurement post-process. | CMM on finished assembly |
| 5 | Control has moderate-high chance. SPC with reaction plan. | SPC on key process variable |
| 4 | Control has high chance. Error detection and verification downstream. | Automated functional test, 100% |
| 3 | Control has very high chance. Error detection in-station. | Poka-yoke, force/torque monitoring at assembly |
| 2 | Control almost certain. Multiple independent methods. | 100% automated + CMM + functional test |
| 1 | Certain detection. Poka-yoke prevents non-conforming product from advancing. | Physical mistake-proofing prevents the failure |

**Calibration anchor:** D=1 is reserved for physical mistake-proofing (poka-yoke) that makes the failure mechanically impossible to pass. An automated test catching 99.9% of failures is still D=2–3, not D=1.

### Detection Control Effectiveness Matrix

| Control Type | In-Station? | Automated? | Starting D Range |
|---|---|---|---|
| No control | — | — | 10 |
| Periodic random audit | No | No | 8–9 |
| 100% manual visual | No | No | 7–8 |
| 100% manual gauge/measurement | No | No | 6–7 |
| Automated end-of-line test | No | Yes | 4–5 |
| In-process SPC with reaction plan | Yes | Semi | 4–5 |
| In-station automated check | Yes | Yes | 3–4 |
| Multiple independent automated checks | Yes | Yes | 2–3 |
| Physical poka-yoke (prevents advance) | Yes | N/A | 1 |

Adjust within each range based on: known false-negative rate of the test, coverage of the specific failure mode (a leak test doesn't detect cosmetic defects), and gauge R&R results.

### Detection Mis-scorings

| Mistake | Correct logic |
|---|---|
| Scoring low D because "we'd see it at final audit" | Final audit catch rate must be measured, not assumed |
| Assuming automated = D=1 | Automation has false-negative rates; D=1 requires physical impossibility |
| Improving D to lower RPN without addressing S or O | Detection doesn't prevent customer harm; prioritize O reduction |
| Same D score for visual check and poka-yoke | These have fundamentally different effectiveness |

---

## Team Calibration Protocol

Run this 20-minute exercise at the start of any FMEA workshop.

### Step 1 — Anchor on two known items (5 min)

Select one historical failure mode the team knows:
- One that caused a field recall or safety event → confirm everyone scores S ≥ 9
- One cosmetic complaint from a customer survey → confirm everyone scores S ≤ 4

If scores diverge by more than 2 points, discuss before proceeding.

### Step 2 — Score a practice item independently (10 min)

Give every team member this prompt:

> **Process step:** Torque tightening of cylinder head bolts  
> **Failure mode:** Under-torque (bolt not fully seated)  
> **Effect:** Head gasket leak → coolant loss → engine overheat  
> **Cause:** Air tool calibration drift  
> **Prevention control:** Monthly torque wrench calibration  
> **Detection control:** 100% torque audit by quality inspector (visual verification of torque mark)

Each person writes S, O, D independently. Reveal simultaneously.

**Expected consensus range:**
- S: 8–9 (loss of primary function; potential engine damage)
- O: 4–5 (calibration maintained monthly; controlled but not mistake-proofed)
- D: 7–8 (manual visual, 100% coverage but human-dependent)

If any individual score falls outside ±2 of group median, that person explains their reasoning. The team agrees on a final score — not by averaging, but by logic.

### Step 3 — Establish team-specific examples (5 min)

Document one local example for each of: S=10, O=3, D=4. These become your calibration anchors for the session and should be recorded in the FMEA register header.

---

## Worked Example: Injection Molding Gate Vestige

**Process step:** Injection molding, gate trimming  
**Function:** Produce flash-free part surface for assembly mating face  
**Failure mode:** Gate vestige height > 0.3 mm  

**Effect analysis:**
- Customer (next assembly station): prevents sealing surface contact → O-ring leak → water ingress to electronics
- S = 8 (loss of primary function; water damage to product)

**Cause analysis:**
- Root cause: trimming blade wear exceeds replacement interval
- Current prevention: blade replaced every 5,000 shots (based on vendor recommendation, not measured data)
- O = 5 (controlled interval, but interval based on estimate, not measurement)

**Detection analysis:**
- Current detection: 100% visual inspection by operator, go/no-go height gauge sampled 1-in-50
- D = 7 (100% visual is unreliable for 0.3 mm threshold; sampling too sparse to catch early blade wear)

**RPN = 8 × 5 × 7 = 280**  
**AIAG-VDA AP = High** (S=8, O=5 → High regardless of D per AP matrix)

**Recommended action:** Install laser profilometer for 100% automated height measurement → D drops from 7 to 3. Secondary action: replace empirical blade interval with in-process height trend monitoring to reduce O from 5 to 3.

**Post-action RPN = 8 × 3 × 3 = 72; AP = Medium**

Note that S remains 8 throughout. The failure effect on the customer did not change.

---

## Scoring Consistency Rules (Non-negotiable)

1. **Score from the customer's perspective.** S is always the worst credible effect on the end user or next process customer, not the internal cost to rework.

2. **Score with current controls only.** O and D reflect what is in place today. Planned improvements are scored separately as "revised" S/O/D after actions are closed.

3. **One cause per row.** A failure mode with multiple independent causes gets one FMEA row per cause. Combining causes into one row produces inaccurate O scores.

4. **D scores the control, not the intent.** "We plan to add a poka-yoke" is not a current detection control. Score the actual current state.

5. **S=10 items require documented rationale if action is NOT taken.** Management sign-off must be recorded. No FMEA is complete with unaddressed S=10 items and no documented owner.
