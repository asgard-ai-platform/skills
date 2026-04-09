# Capability Indices: Cp, Cpk, Pp, Ppk, Cpm

## The Four-Index Family

| Index | Variation Source | Centering | Question Answered |
|-------|-----------------|-----------|-------------------|
| Cp | Within-subgroup σ | Ignored | What could this process achieve if perfectly centered? |
| Cpk | Within-subgroup σ | Included | What is this process actually achieving (short-term)? |
| Pp | Overall σ | Ignored | What is the spread of all data relative to spec? |
| Ppk | Overall σ | Included | What is the long-term actual performance? |

**Rule of thumb:** C-indices (Cp, Cpk) use σ estimated from subgroup variation. P-indices (Pp, Ppk) use the sample standard deviation of all data.

---

## Formulas

Let:
- n = total number of measurements
- μ = process mean (x̄)
- USL, LSL = upper and lower specification limits
- σ̂_within = within-subgroup standard deviation (from R̄/d₂ or S̄/c₄)
- s = overall sample standard deviation = √[ Σ(xᵢ − x̄)² / (n−1) ]

```
Cp  = (USL − LSL) / (6 × σ̂_within)
Cpk = min( (USL − μ) / (3 × σ̂_within),  (μ − LSL) / (3 × σ̂_within) )

Pp  = (USL − LSL) / (6 × s)
Ppk = min( (USL − μ) / (3 × s),  (μ − LSL) / (3 × s) )
```

### Cpm (Taguchi Index)

Cpm penalizes deviation from the nominal target T, not just from the mean:

```
σ_T = √[ Σ(xᵢ − T)² / n ]
Cpm = (USL − LSL) / (6 × σ_T)
```

When T = μ, Cpm = Cp. When the process is off-target, Cpm < Cp. Cpm is appropriate when the cost of deviation from T is asymmetric (e.g., a safety-critical dimension).

---

## σ Estimation: Within-Subgroup vs Overall

This is the most commonly confused aspect of capability analysis.

### Within-subgroup σ (used for Cp, Cpk)

Captures **short-term, common-cause variation only**. Estimated from ranges or standard deviations within rational subgroups (e.g., 5 consecutive parts per hour).

**Method 1 — R̄/d₂ (range method):**
```
σ̂_within = R̄ / d₂
```
Where R̄ = average subgroup range, d₂ = control-chart constant for subgroup size k.

| Subgroup size k | d₂ |
|----------------|----|
| 2 | 1.128 |
| 3 | 1.693 |
| 4 | 2.059 |
| 5 | 2.326 |
| 10 | 3.078 |

**Method 2 — S̄/c₄ (standard deviation method, preferred for k ≥ 10):**
```
σ̂_within = S̄ / c₄
```
Where S̄ = average subgroup standard deviation, c₄ = unbiasing constant.

### Overall σ (used for Pp, Ppk)

```
s = √[ Σ(xᵢ − x̄)² / (n−1) ]
```

Includes **both** within-subgroup variation and between-subgroup shifts (operator changes, lot-to-lot drift, time effects). This is the standard pandas/numpy `std()` with `ddof=1`.

### The σ Ratio as a Diagnostic

```
σ_overall / σ_within ≥ 1.0  (always)
```

- Ratio ≈ 1.0 → process is stable; no meaningful between-subgroup shifts
- Ratio > 1.3 → significant instability; investigate before reporting Cpk
- Ratio > 1.5 → SPC charts will show out-of-control signals; Cpk is misleading

If σ_overall / σ_within >> 1, the process is NOT in statistical control and Cpk should not be reported to customers.

---

## Worked Example

**Scenario:** Shaft diameter. USL = 25.05 mm, LSL = 24.95 mm, T = 25.00 mm.  
20 subgroups of 5 measurements each (100 total).

**Collected statistics:**
- x̄ = 25.01 mm
- R̄ = 0.030 mm → σ̂_within = 0.030 / 2.326 = 0.01290 mm
- s (overall) = 0.01550 mm

**Step 1: Compute C-indices**
```
Cp  = (25.05 − 24.95) / (6 × 0.01290) = 0.10 / 0.07740 = 1.29
Cpk = min( (25.05 − 25.01) / (3 × 0.01290),  (25.01 − 24.95) / (3 × 0.01290) )
    = min( 0.04 / 0.03870,  0.06 / 0.03870 )
    = min( 1.03,  1.55 )
    = 1.03
```

**Step 2: Compute P-indices**
```
Pp  = (25.05 − 24.95) / (6 × 0.01550) = 0.10 / 0.09300 = 1.08
Ppk = min( (25.05 − 25.01) / (3 × 0.01550),  (25.01 − 24.95) / (3 × 0.01550) )
    = min( 0.04 / 0.04650,  0.06 / 0.04650 )
    = min( 0.86,  1.29 )
    = 0.86
```

**Step 3: Compute Cpm**
```
σ_T = √[ Σ(xᵢ − 25.00)² / 100 ]
    ≈ √( s² + (x̄ − T)² )  [shortcut]
    = √( 0.01550² + 0.01² )
    = √( 0.000240 + 0.000100 )
    = √0.000340 = 0.01844 mm

Cpm = 0.10 / (6 × 0.01844) = 0.10 / 0.11066 = 0.90
```

**Interpretation:**
| Index | Value | Assessment |
|-------|-------|-----------|
| Cp | 1.29 | Below 1.33 — spread too wide for specs |
| Cpk | 1.03 | Mean shifted toward USL; worse than Cp |
| Pp | 1.08 | Long-term spread even wider |
| Ppk | 0.86 | Not capable long-term — FAIL |
| Cpm | 0.90 | Off-nominal penalized; confirms real issue |

σ ratio = 0.01550 / 0.01290 = 1.20 → moderate instability present.

**Diagnosis:** The process has two problems: (1) spread is too wide (Cp < 1.33), and (2) the mean is shifted 0.01 mm above target. Fix centering first (cheaper), then reduce variation.

---

## Index Selection Decision Table

```
Is the process in statistical control?
├── NO → Fix process first. Do NOT report Cpk.
└── YES
    ├── What time horizon does the customer want?
    │   ├── Short-term / process qualification → Use Cp, Cpk
    │   └── Long-term / ongoing performance → Use Pp, Ppk
    │
    ├── Does centering matter?
    │   ├── YES (bilateral spec, customer cares about offset) → Use Cpk / Ppk
    │   └── NO (report theoretical maximum) → Use Cp / Pp
    │
    └── Is deviation from nominal T costly even within spec?
        ├── YES (asymmetric loss function) → Also compute Cpm
        └── NO → Cpk / Ppk sufficient
```

---

## Common Customer Requirements by Industry

| Industry | Typical Minimum | Index Required | Notes |
|----------|----------------|---------------|-------|
| Automotive (IATF 16949) | Cpk ≥ 1.67 for new tooling, ≥ 1.33 ongoing | Cpk | PPAP requires initial capability study |
| Semiconductor | Cpk ≥ 1.67 standard, ≥ 2.0 for critical | Cpk | |
| Aerospace | Cpk ≥ 1.33, sometimes Ppk ≥ 1.67 | Both | Long-term performance scrutinized |
| Medical devices | Ppk ≥ 1.33 typical | Ppk | FDA process validation expects long-term |
| General manufacturing | Cpk ≥ 1.33 | Cpk | Baseline expectation |

If a customer contract specifies only "Cpk," clarify whether they mean the C-index (within-subgroup σ) or are using "Cpk" as shorthand for Ppk. This distinction is frequently a source of disputes during supplier qualification.

---

## Centering Ratio: Quantifying How Off-Center a Process Is

```
K = (μ − M) / ( (USL − LSL) / 2 )
```

Where M = (USL + LSL) / 2 = spec midpoint.

- K = 0 → perfectly centered
- |K| = 1 → mean at a specification limit (Cpk = 0)
- K > 0 → shifted toward USL; K < 0 → shifted toward LSL

**Relationship to Cp and Cpk:**
```
Cpk = Cp × (1 − |K|)
```

This means if Cp = 1.60 and you observe Cpk = 1.28:
```
|K| = 1 − (Cpk / Cp) = 1 − (1.28 / 1.60) = 0.20
```
The process mean is 20% of the half-tolerance away from center. Corrective action: adjust the process mean (centering fix), not spread reduction.

---

## Confidence Intervals for Cpk

A point estimate of Cpk from a small sample is unreliable. Report the lower confidence bound.

**Approximate 95% lower confidence bound (χ² method):**
```
Cpk_lower = Cpk × √( χ²_(α, ν) / ν )
```
Where ν ≈ n − 1 and χ²_(0.05, ν) is the 5th percentile of chi-squared.

**Practical table — lower 95% bound on Cpk:**

| n | Observed Cpk = 1.33 | Observed Cpk = 1.67 |
|---|---------------------|---------------------|
| 30 | 1.01 | 1.27 |
| 50 | 1.07 | 1.35 |
| 100 | 1.13 | 1.43 |
| 200 | 1.19 | 1.50 |
| 300 | 1.22 | 1.53 |

**Implication:** A sample of 30 units showing Cpk = 1.33 has a 95% lower bound of only 1.01 — far below the requirement. Automotive PPAP typically requires n ≥ 100 for initial capability studies. Never present Cpk without noting sample size.

---

## Pp/Ppk vs Cp/Cpk: Expected Gap

In a stable, well-controlled process, Pp ≈ Cp and Ppk ≈ Cpk.

In practice, due to long-term drift and shift, the empirical relationship used in Six Sigma is:

```
Pp ≈ Cp − 0.5 sigma shift adjustment (rule of thumb only)
```

Motorola's original Six Sigma model assumed a 1.5σ long-term shift, giving:
```
Long-term Cpk ≈ Short-term Cpk − 0.5
```

This 1.5σ shift is **controversial** — it was empirically observed in Motorola's processes and is not a physical law. Use actual Ppk measurement instead of adjusting Cpk by 0.5.

---

## When Cpk < 0

Cpk is negative when the process mean lies outside one of the specification limits.

```
Example: USL = 10, LSL = 5, μ = 11, σ = 0.5

Cpk = min( (10 − 11) / 1.5,  (11 − 5) / 1.5 )
    = min( −0.67,  4.0 )
    = −0.67
```

Negative Cpk means the majority of production is out of spec. The magnitude gives a sense of how far out: Cpk = −0.67 corresponds to the mean being 2σ beyond the specification limit.

---

## One-Sided Specifications

When only USL exists (e.g., surface roughness, contamination level):

```
Cpk = (USL − μ) / (3σ)   [upper-sided only]
```

When only LSL exists (e.g., minimum tensile strength):

```
Cpk = (μ − LSL) / (3σ)   [lower-sided only]
```

Cp is undefined for one-sided specifications — there is no tolerance band to center within. Report only Cpk (or Ppk).
