# Statistical Process Control (SPC) Basics

SPC uses statistical methods to monitor a process over time and distinguish between two types of variation:

- **Common cause variation** — inherent randomness in a stable process (normal noise)
- **Special cause variation** — something abnormal happened; the process changed

The DMAIC Control phase deploys SPC to detect special causes early, before they produce defects. Without SPC, teams react to noise (over-adjustment) or miss real signals (under-reaction) — both make things worse.

---

## Control Charts: Core Concept

A control chart plots a process metric over time with three reference lines:

```
UCL ─────────────────────────────────  Upper Control Limit
CL  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  Center Line (process mean)
LCL ─────────────────────────────────  Lower Control Limit
```

Control limits are **not** specification limits. They are calculated from the process's own historical variation (±3σ). They answer: "what does this process naturally produce?" Specification limits answer: "what does the customer need?"

**Critical distinction**: if a point falls outside the spec limit but inside the control limit, the process is stable but incapable. If a point falls outside the control limit but inside the spec limit, a special cause occurred even though the output looks acceptable.

---

## Choosing the Right Chart

| Data type | Subgroup size | Chart |
|-----------|--------------|-------|
| Continuous (length, weight, time) | n = 2–10 | X̄–R chart |
| Continuous | n > 10 | X̄–S chart |
| Continuous, individual readings | n = 1 | I–MR chart (Individuals + Moving Range) |
| Defective units (pass/fail) | variable n | p-chart |
| Defective units | constant n | np-chart |
| Count of defects per unit | variable area | u-chart |
| Count of defects per unit | constant area | c-chart |

For most manufacturing and service process improvement projects, start with **X̄–R** (subgroup data) or **I–MR** (single readings).

---

## X̄–R Chart: Step-by-Step

### Step 1 — Collect baseline data

Collect k subgroups of size n. Recommended: k ≥ 20 subgroups, n = 4 or 5 per subgroup.

Example: order fulfillment cycle time (hours), 5 orders measured each day for 20 days.

| Day | x₁ | x₂ | x₃ | x₄ | x₅ | X̄ | R |
|-----|----|----|----|----|----|----|---|
| 1 | 4.2 | 3.8 | 4.5 | 4.1 | 3.9 | 4.10 | 0.7 |
| 2 | 5.1 | 4.6 | 4.8 | 5.2 | 4.9 | 4.92 | 0.6 |
| … | … | … | … | … | … | … | … |
| 20 | 4.3 | 4.1 | 4.4 | 4.0 | 4.2 | 4.20 | 0.4 |

Calculate for each subgroup:
- **X̄ᵢ** = (x₁ + x₂ + … + xₙ) / n
- **Rᵢ** = max(xᵢ) − min(xᵢ)

### Step 2 — Calculate grand averages

```
X̄̄  = (X̄₁ + X̄₂ + … + X̄ₖ) / k      ← grand mean (center line of X̄ chart)
R̄   = (R₁ + R₂ + … + Rₖ) / k      ← average range (center line of R chart)
```

Suppose from 20 days: **X̄̄ = 4.45 hr**, **R̄ = 0.58 hr**

### Step 3 — Calculate control limits

Use the standard control chart constants (tabulated by subgroup size n):

| n | A₂ | D₃ | D₄ |
|---|----|----|-----|
| 2 | 1.880 | 0 | 3.267 |
| 3 | 1.023 | 0 | 2.574 |
| 4 | 0.729 | 0 | 2.282 |
| **5** | **0.577** | **0** | **2.114** |
| 6 | 0.483 | 0 | 2.004 |
| 7 | 0.419 | 0.076 | 1.924 |
| 8 | 0.373 | 0.136 | 1.864 |
| 10 | 0.308 | 0.223 | 1.777 |

**X̄ chart limits** (n = 5, A₂ = 0.577):
```
UCL_X̄ = X̄̄ + A₂ × R̄  = 4.45 + 0.577 × 0.58 = 4.45 + 0.335 = 4.785 hr
LCL_X̄ = X̄̄ − A₂ × R̄  = 4.45 − 0.335 = 4.115 hr
```

**R chart limits** (D₃ = 0, D₄ = 2.114):
```
UCL_R = D₄ × R̄ = 2.114 × 0.58 = 1.226 hr
LCL_R = D₃ × R̄ = 0 × 0.58 = 0     (no lower limit when n < 7)
```

### Step 4 — Plot and apply detection rules

Plot X̄ and R values for each subgroup. Investigate any subgroup where:

1. One point beyond UCL or LCL
2. 8 consecutive points on the same side of the center line
3. 6 consecutive points steadily increasing or decreasing
4. 2 of 3 consecutive points in the outer ⅓ zone (between 2σ and 3σ)

If a subgroup is flagged, find the special cause, remove that subgroup, and recalculate limits. Repeat until the baseline is clean.

---

## I–MR Chart: When You Have Single Readings

Use when measuring one item per time period (e.g., daily defect rate, monthly cost).

**Moving Range**: MRᵢ = |xᵢ − xᵢ₋₁|  (difference between consecutive readings)

Calculate:
```
X̄   = mean of all individual values
MR̄  = mean of all moving ranges (MR₂ through Mₖ)
```

Control limits using constants for n = 2 (d₂ = 1.128):
```
Individuals chart:
  UCL_I = X̄ + 3 × (MR̄ / d₂) = X̄ + 2.660 × MR̄
  LCL_I = X̄ − 2.660 × MR̄

Moving Range chart:
  UCL_MR = D₄ × MR̄ = 3.267 × MR̄
  LCL_MR = 0
```

**Worked example**: Daily complaint count over 10 days:
```
Day:  1    2    3    4    5    6    7    8    9    10
x:    12   9    11   14   8    10   13   11   9    12

MR:   -    3    2    3    6    2    3    2    2    3
```

```
X̄   = (12+9+11+14+8+10+13+11+9+12) / 10 = 109 / 10 = 10.9
MR̄  = (3+2+3+6+2+3+2+2+3) / 9 = 26 / 9 = 2.89

UCL_I = 10.9 + 2.660 × 2.89 = 10.9 + 7.69 = 18.59
LCL_I = 10.9 − 7.69 = 3.21

UCL_MR = 3.267 × 2.89 = 9.44
```

Day 5 shows MR = 6 (large jump from 14 to 8) — worth investigating. No individual points breach control limits, so the process is stable.

---

## p-Chart: Proportion Defective

Use when each unit is classified as defective or not (pass/fail), and sample size varies.

```
p̄ = total defectives / total inspected = Σdᵢ / Σnᵢ

For each subgroup i:
  UCL_pᵢ = p̄ + 3 × √(p̄(1−p̄) / nᵢ)
  LCL_pᵢ = p̄ − 3 × √(p̄(1−p̄) / nᵢ)   (set to 0 if negative)
```

Note: control limits vary by subgroup because nᵢ varies. This creates a "staircase" UCL/LCL on the chart. If sample sizes vary by less than ±25% from the mean, you can use a fixed average n to simplify.

**Example**: Invoice accuracy check, variable daily sample size:

| Day | Inspected (n) | Defective (d) | p = d/n |
|-----|--------------|--------------|---------|
| 1 | 200 | 8 | 0.040 |
| 2 | 180 | 12 | 0.067 |
| 3 | 220 | 6 | 0.027 |
| 4 | 190 | 9 | 0.047 |
| 5 | 210 | 7 | 0.033 |
| **Total** | **1000** | **42** | |

```
p̄ = 42 / 1000 = 0.042

Day 1 UCL: 0.042 + 3 × √(0.042 × 0.958 / 200) = 0.042 + 3 × 0.01419 = 0.042 + 0.043 = 0.085
Day 2 UCL: 0.042 + 3 × √(0.042 × 0.958 / 180) = 0.042 + 0.045 = 0.087  ← wider (smaller n)
```

Day 2 proportion = 0.067, UCL = 0.087 → within limits. Process is stable.

---

## Process Capability: Cp and Cpk

Once the control chart shows a stable process (no special causes), calculate capability: can the stable process meet spec limits?

**Definitions**:
- USL = Upper Specification Limit (customer requirement)
- LSL = Lower Specification Limit
- σ̂ = estimated process standard deviation = R̄ / d₂  (use d₂ from the same table as above)

```
Cp  = (USL − LSL) / (6σ̂)          ← potential capability (spread vs. spec width)
Cpk = min[(USL − X̄̄) / (3σ̂),
           (X̄̄ − LSL) / (3σ̂)]     ← actual capability (accounts for off-center mean)
```

| Cpk | Defects (±3σ process) | Interpretation |
|-----|----------------------|----------------|
| < 1.00 | > 2,700 ppm | Incapable — defects certain |
| 1.00 | 2,700 ppm | Marginal — no room for drift |
| 1.33 | 64 ppm | Adequate for most industries |
| 1.67 | 0.6 ppm | Good |
| 2.00 | 0.002 ppm | Six Sigma level |

**Worked example** (continuing the cycle time example):
- USL = 6.0 hr (customer wants orders fulfilled in under 6 hours)
- LSL = 0 hr (no lower bound)
- X̄̄ = 4.45 hr, R̄ = 0.58, d₂ = 2.326 (for n=5)

```
σ̂ = 0.58 / 2.326 = 0.249 hr

Cp  = (6.0 − 0) / (6 × 0.249) = 6.0 / 1.496 = 4.01   ← generous spec width
Cpk = min[(6.0 − 4.45) / (3 × 0.249),
           (4.45 − 0) / (3 × 0.249)]
    = min[1.55 / 0.748, 4.45 / 0.748]
    = min[2.07, 5.95]
    = 2.07   ← process is well-centered and capable
```

This process comfortably meets spec. If Cpk were < 1.33, the Improve phase would need to reduce σ̂ (reduce variation) or shift X̄̄ toward center (correct bias).

---

## Common Mistakes

**Using spec limits as control limits.** Control limits come from the data. Setting UCL = USL confuses "what the process does" with "what the customer wants." These are orthogonal questions.

**Calculating control limits from a contaminated baseline.** If special causes are present in the Phase 1 data, they inflate σ̂, making the control limits too wide. Remove known special causes before calculating limits.

**Reacting to every point that moves.** Common cause variation will produce points near the limits occasionally (false alarm rate ≈ 0.27% per point at ±3σ). Without a detection rule violation, do not adjust the process — adjustment adds variation.

**Confusing Cp with Cpk.** Cp ignores where the mean sits relative to the spec limits. A process can have Cp = 2.0 but Cpk = 0.5 if the mean is shifted far off-center. Always report Cpk.

**Using SPC on an unstable process.** Capability indices (Cp, Cpk) are meaningless if the control chart shows special causes. Stabilize first; measure capability second.

**Short baseline periods.** k < 15 subgroups produces unreliable control limits. The investment in 20–25 subgroups before calculating limits pays off in fewer false alarms.

---

## Quick Reference: Control Chart Constants

| n | d₂ | A₂ | D₃ | D₄ |
|---|----|----|-----|-----|
| 2 | 1.128 | 1.880 | 0 | 3.267 |
| 3 | 1.693 | 1.023 | 0 | 2.574 |
| 4 | 2.059 | 0.729 | 0 | 2.282 |
| 5 | 2.326 | 0.577 | 0 | 2.114 |
| 6 | 2.534 | 0.483 | 0 | 2.004 |
| 7 | 2.704 | 0.419 | 0.076 | 1.924 |
| 8 | 2.847 | 0.373 | 0.136 | 1.864 |
| 9 | 2.970 | 0.337 | 0.184 | 1.816 |
| 10 | 3.078 | 0.308 | 0.223 | 1.777 |

These constants derive from the distribution of the range statistic. `d₂` converts R̄ to σ̂. `A₂ = 3 / (d₂ × √n)`.
