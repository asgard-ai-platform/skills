# AIAG-VDA Action Priority (AP) Matrix

## Why RPN Was Replaced

Classic RPN = S × O × D has a structural flaw: multiplication treats all three dimensions as equivalent, producing identical scores for radically different risk profiles.

| Scenario | S | O | D | RPN | Actual Risk |
|----------|---|---|---|-----|-------------|
| Catastrophic, rare, undetectable | 10 | 1 | 10 | 100 | Potentially catastrophic |
| Trivial, frequent, undetectable | 1 | 10 | 10 | 100 | Minor nuisance |
| Safety critical, occasional, detected | 10 | 5 | 2 | 100 | High risk |

Three failure modes with identical RPN=100 demand completely different responses. RPN also has the threshold problem: teams set arbitrary cutoffs (e.g., "act on RPN > 100") that carry no statistical or engineering basis.

**AIAG-VDA 2019 solution:** Replace the formula with a lookup table that reflects how humans actually reason about risk — Severity dominates, then Occurrence, then Detection.

---

## How the AP Lookup Works

AP is **not a formula**. It is a three-dimensional lookup:

```
AP = Lookup(S, O, D)
AP ∈ {High, Medium, Low}
```

The lookup encodes an expert decision model:
- **Severity 9–10:** Almost always High, regardless of O and D. The customer effect is too severe to accept any risk.
- **Severity 7–8:** Depends on O. High D (poor detection) can push Medium → High.
- **Severity 5–6:** Depends on both O and D; most combinations are Medium or Low.
- **Severity 1–4:** Rarely exceeds Low unless O is extreme.

### Representative AP Table

> **Note:** The exact AIAG-VDA 2019 AP table is published in the proprietary *FMEA Handbook* (available from AIAG/VDA). The table below reflects publicly documented principles and is suitable for training and audit preparation. Refer to the official handbook for production use.

**S = 9–10**

| Occurrence (O) | Detection (D) | AP |
|----------------|---------------|-----|
| 6–10 | any | **H** |
| 4–5 | 5–10 | **H** |
| 4–5 | 1–4 | **H** |
| 2–3 | 7–10 | **H** |
| 2–3 | 4–6 | **M** |
| 2–3 | 1–3 | **M** |
| 1 | 7–10 | **H** |
| 1 | 4–6 | **M** |
| 1 | 1–3 | **L** |

**S = 7–8**

| Occurrence (O) | Detection (D) | AP |
|----------------|---------------|-----|
| 8–10 | any | **H** |
| 6–7 | 8–10 | **H** |
| 6–7 | 1–7 | **M** |
| 4–5 | 8–10 | **H** |
| 4–5 | 5–7 | **M** |
| 4–5 | 1–4 | **M** |
| 2–3 | 8–10 | **M** |
| 2–3 | 1–7 | **L** |
| 1 | any | **L** |

**S = 5–6**

| Occurrence (O) | Detection (D) | AP |
|----------------|---------------|-----|
| 8–10 | 8–10 | **H** |
| 8–10 | 5–7 | **M** |
| 8–10 | 1–4 | **M** |
| 5–7 | 8–10 | **M** |
| 5–7 | 1–7 | **M** |
| 3–4 | 8–10 | **M** |
| 3–4 | 1–7 | **L** |
| 1–2 | any | **L** |

**S = 1–4**

| Occurrence (O) | Detection (D) | AP |
|----------------|---------------|-----|
| 8–10 | 8–10 | **M** |
| 8–10 | 1–7 | **L** |
| 1–7 | any | **L** |

---

## What AP Means: Required Actions

| AP | Required Response |
|----|-------------------|
| **High** | Team **must** take action. Identify and implement improvements to lower S, O, or D. Management review required. Document justification if no action is taken (rare; requires VP-level sign-off in IATF 16949 contexts). |
| **Medium** | Team **should** take action. Evaluate whether improvement is feasible and cost-effective. Inaction is permissible if documented rationale is provided. |
| **Low** | Action at team's discretion. Acceptable to leave unchanged; note in FMEA for future review cycles. |

**Critical rule (reinforcing SKILL.md Iron Law):** AP=High cannot be downgraded by improving Detection alone when S=9–10. Severity is fixed by customer effect. Only design changes that reduce the probability of the failure (lower O) or design changes that eliminate the failure mode entirely (lower S by eliminating the effect) are valid paths to reducing AP for high-severity items.

---

## Worked Example: Brake Caliper Assembly (PFMEA)

**Process step:** Torque brake caliper bolts to 120 N·m

### Failure Mode 1: Under-torque (bolt loose)

| Parameter | Score | Rationale |
|-----------|-------|-----------|
| Severity | 10 | Brake failure → accident risk → customer safety |
| Occurrence | 3 | Pneumatic torque wrench calibrated weekly; operator error rate ~1 in 500 |
| Detection | 5 | End-of-line torque audit on 5% sample; not 100% inspection |

**Classic RPN:** 10 × 3 × 5 = **150**

**AIAG-VDA AP lookup:** S=10 → row S=9–10; O=3 → row "2–3"; D=5 → column "4–6" → **AP = Medium**

Action taken: Add 100% automated torque verification station after assembly.

**After action:**
- Occurrence unchanged: 3 (wrench calibration unchanged)
- Detection: 2 (100% automated check, highly reliable)
- New RPN: 10 × 3 × 2 = **60** ← RPN improved significantly
- New AP lookup: S=10, O=3, D=2 → "1–3" column → **AP = Medium**

**AP did not change.** This is correct: the customer effect remains S=10, the failure still occurs at O=3, and we only improved detection. The risk of the brake failing is unchanged; we are now just catching it before it reaches the customer. The team must also address Occurrence (redesign, poka-yoke, mandatory torque wrench with auto-shutoff).

### Failure Mode 2: Over-torque (bolt strips)

| Parameter | Score | Rationale |
|-----------|-------|-----------|
| Severity | 7 | Caliper bracket stress fracture; potential brake drag/failure |
| Occurrence | 2 | Same process; overtorque is rarer than undertorque |
| Detection | 4 | Stripped bolt is visually apparent to operator |

**Classic RPN:** 7 × 2 × 4 = **56**

**AIAG-VDA AP lookup:** S=7–8; O=2–3; D=4 → row "2–3", column "1–7" → **AP = Low**

No immediate action required. Document in FMEA; revisit at next design review.

### Side-by-Side Comparison

| Failure Mode | RPN | RPN Rank | AP | AP Action |
|--------------|-----|----------|----|-----------|
| Under-torque | 150 | 1st | Medium | Action recommended |
| Over-torque | 56 | 2nd | Low | No action required |

Both methods agree on priority order here. The critical difference emerges when comparing under-torque (S=10, O=3, D=5) against a hypothetical cosmetic defect (S=2, O=9, D=9, RPN=162): RPN ranks cosmetic defect as higher risk; AP correctly classifies it as Low while keeping under-torque at Medium.

---

## Migrating an Existing FMEA from RPN to AP

1. **No re-scoring required.** Existing S, O, D scores are reused directly.
2. For each row, look up AP using the S-O-D table.
3. Reclassify action status:
   - Former "RPN > threshold" items that are now AP=Low: document the rationale, close or defer.
   - Former "RPN < threshold" items that are now AP=High: escalate immediately.
4. Sort the FMEA by AP (High → Medium → Low), then by S descending within each tier.
5. Update the FMEA header to note: *"Converted to AIAG-VDA 2019 AP methodology on [date]."*

**Common reclassification surprises:**
- S=10 items with low O (e.g., O=1) that had RPN=10–30 and were previously ignored → now AP=Medium or High
- S=2 items with high O and D that had RPN=160+ and were previously prioritized → now AP=Low

---

## Scoring Calibration for AP

Because AP is dominated by Severity, scoring inconsistency in S has the largest downstream impact. A team that scores S=8 instead of S=9 on a structural failure can shift an item from High to Medium, eliminating the mandatory action requirement.

### Anchoring Protocol

Before scoring, the team should agree on at least one anchor point per Severity tier:

| S Range | Anchor Example | Rationale |
|---------|---------------|-----------|
| 9–10 | Any safety-critical failure (airbag non-deployment, brake loss, fire) | Regulatory/liability |
| 7–8 | Product inoperability without workaround, warranty claim expected | Field failure |
| 5–6 | Degraded performance, customer complaints likely | Quality |
| 3–4 | Minor performance loss, customer may notice | Cosmetic/minor |
| 1–2 | Undetectable or trivially ignorable | No impact |

**Rule:** If two engineers score the same failure mode 2 or more points apart on S, stop and resolve before proceeding. S disagreement of ≥2 points indicates a gap in how the team has defined the customer effect — not a scoring error.

---

## AP vs. RPN: When Each Is Appropriate

| Context | Recommendation |
|---------|---------------|
| Automotive (IATF 16949) | **AP required** — AIAG-VDA 2019 is the current standard; RPN is legacy |
| Medical devices (ISO 13485 / ISO 14971) | Use severity + probability matrix per ISO 14971; AP is compatible in spirit |
| Legacy FMEA database | Migrate to AP (see section above); do not mix methods in the same register |
| Internal non-regulated process | Either is acceptable; AP is preferred for high-severity processes |
| Customer-specified RPN threshold | If customer contract specifies RPN-based acceptance criteria, retain RPN; add AP as supplementary column |
