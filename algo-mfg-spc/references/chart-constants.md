# Control Chart Constants

Control chart constants are multipliers derived from the sampling distribution of the range (or standard deviation) for subgroups of size *n*. They convert the average range R̄ (or average standard deviation S̄) into control limit offsets — eliminating the need to estimate σ directly from individual measurements.

## Why Constants Exist

The standard deviation of a normally distributed process cannot be estimated directly from subgroup ranges without a bias correction. For a subgroup of size *n*, the expected value of the range R is:

```
E[R] = d₂ × σ
```

So σ̂ = R̄ / d₂. The constants A₂, D₃, D₄ (and their S-chart equivalents A₃, B₃, B₄) are all derived algebraically from d₂ and related factors.

## X-bar/R Chart Constants

### Formulas

```
UCL_X̄ = X̄̄ + A₂ × R̄
LCL_X̄ = X̄̄ − A₂ × R̄

UCL_R  = D₄ × R̄
LCL_R  = D₃ × R̄   (equals 0 when n ≤ 6; D₃ is tabulated as 0)
```

Where:
- **A₂** = 3 / (d₂ × √n)
- **D₄** = 1 + 3 × d₃/d₂
- **D₃** = 1 − 3 × d₃/d₂  (floor at 0; negative values are set to 0)
- **d₂** = expected value of the relative range W = R/σ
- **d₃** = standard deviation of the relative range W

### Standard Table (n = 2 to 10)

| n  | d₂     | d₃     | A₂    | D₃   | D₄    |
|----|--------|--------|-------|------|-------|
| 2  | 1.128  | 0.853  | 1.880 | 0    | 3.267 |
| 3  | 1.693  | 0.888  | 1.023 | 0    | 2.574 |
| 4  | 2.059  | 0.880  | 0.729 | 0    | 2.282 |
| 5  | 2.326  | 0.864  | 0.577 | 0    | 2.114 |
| 6  | 2.534  | 0.848  | 0.483 | 0    | 2.004 |
| 7  | 2.704  | 0.833  | 0.419 | 0.076| 1.924 |
| 8  | 2.847  | 0.820  | 0.373 | 0.136| 1.864 |
| 9  | 2.970  | 0.808  | 0.337 | 0.184| 1.816 |
| 10 | 3.078  | 0.797  | 0.308 | 0.223| 1.777 |

**Note:** D₃ = 0 for n ≤ 6 means LCL_R is set to 0 (ranges cannot be negative; the lower tail of the range distribution doesn't reach 3σ below R̄ for small subgroups).

## X-bar/S Chart Constants

Use when subgroup size n ≥ 10, or when you want better σ estimation than R provides at larger n.

### Formulas

```
UCL_X̄ = X̄̄ + A₃ × S̄
LCL_X̄ = X̄̄ − A₃ × S̄

UCL_S  = B₄ × S̄
LCL_S  = B₃ × S̄
```

Where:
- **c₄** = expected value of s/σ = √(2/(n−1)) × Γ(n/2) / Γ((n−1)/2)
- **A₃** = 3 / (c₄ × √n)
- **B₄** = 1 + 3 × √(1 − c₄²) / c₄
- **B₃** = 1 − 3 × √(1 − c₄²) / c₄  (floor at 0)

### Standard Table (n = 2 to 10)

| n  | c₄     | A₃    | B₃   | B₄    |
|----|--------|-------|------|-------|
| 2  | 0.7979 | 2.659 | 0    | 3.267 |
| 3  | 0.8862 | 1.954 | 0    | 2.568 |
| 4  | 0.9213 | 1.628 | 0    | 2.266 |
| 5  | 0.9400 | 1.427 | 0    | 2.089 |
| 6  | 0.9515 | 1.287 | 0.030| 1.970 |
| 7  | 0.9594 | 1.182 | 0.118| 1.882 |
| 8  | 0.9650 | 1.099 | 0.185| 1.815 |
| 9  | 0.9693 | 1.032 | 0.239| 1.761 |
| 10 | 0.9727 | 0.975 | 0.284| 1.716 |

## I-MR Chart Constants (Individual Measurements)

Use when subgroup size = 1 (one measurement per time period).

```
UCL_I  = X̄ + 3 × (MR̄ / d₂)   where d₂ = 1.128 (n=2)
LCL_I  = X̄ − 3 × (MR̄ / d₂)

UCL_MR = D₄ × MR̄               where D₄ = 3.267 (n=2)
LCL_MR = D₃ × MR̄  = 0          where D₃ = 0    (n=2)
```

The moving range is computed between consecutive pairs:

```
MRᵢ = |Xᵢ − Xᵢ₋₁|
MR̄  = mean of all MRᵢ  (drop MR₁; you have n−1 moving ranges for n points)
```

The n=2 constants are always used for I-MR, regardless of how many total observations you have. This is because each moving range uses only 2 consecutive points.

**Simplified formulas (n=2 constants substituted in):**

```
UCL_I  = X̄ + 2.660 × MR̄
LCL_I  = X̄ − 2.660 × MR̄
UCL_MR = 3.267 × MR̄
```

## Worked Example: X-bar/R with n=5

**Data:** 10 subgroups (abbreviated for illustration)

| Subgroup | x₁   | x₂   | x₃   | x₄   | x₅   | X̄    | R    |
|----------|------|------|------|------|------|------|------|
| 1        | 50.1 | 49.8 | 50.3 | 50.0 | 49.9 | 50.02| 0.5  |
| 2        | 50.4 | 50.1 | 49.7 | 50.2 | 50.3 | 50.14| 0.7  |
| 3        | 49.6 | 50.0 | 50.2 | 49.9 | 50.1 | 49.96| 0.6  |
| ...      | ...  | ...  | ...  | ...  | ...  | ...  | ...  |
| Grand    |      |      |      |      |      | X̄̄=50.02 | R̄=0.62 |

**Step 1:** Look up constants for n=5:  A₂ = 0.577, D₄ = 2.114, D₃ = 0

**Step 2:** X-bar chart limits
```
UCL_X̄ = 50.02 + 0.577 × 0.62 = 50.02 + 0.358 = 50.378
LCL_X̄ = 50.02 − 0.577 × 0.62 = 50.02 − 0.358 = 49.662
```

**Step 3:** R chart limits
```
UCL_R = 2.114 × 0.62 = 1.311
LCL_R = 0 × 0.62    = 0
```

**Step 4:** Verify σ̂ implied by these limits
```
σ̂ = R̄ / d₂ = 0.62 / 2.326 = 0.267
```
The ±3σ half-width on X-bar = 3 × σ̂ / √5 = 3 × 0.267 / 2.236 = 0.358 ✓ matches A₂ × R̄ above.

## Chart Type Selection Guide

| Data Type | Subgroup Size | Chart |
|-----------|---------------|-------|
| Continuous measurement | n = 2–9 | X-bar/R |
| Continuous measurement | n ≥ 10 | X-bar/S |
| Continuous measurement | n = 1 | I-MR |
| Proportion defective | variable lot size | p-chart |
| Proportion defective | fixed lot size | np-chart |
| Defect count per unit | variable unit size | u-chart |
| Defect count per unit | fixed unit size | c-chart |

For attribute charts (p, np, c, u), control limits are derived from binomial or Poisson distributions — the constants above do not apply.

## p-chart and c-chart Limits (Attribute Reference)

**p-chart** (proportion nonconforming, variable n):
```
p̄ = total defectives / total inspected

UCL_p = p̄ + 3 × √(p̄(1−p̄)/nᵢ)    ← nᵢ varies per subgroup
LCL_p = p̄ − 3 × √(p̄(1−p̄)/nᵢ)    (floor at 0)
```

**c-chart** (count of defects, fixed area of opportunity):
```
c̄ = mean defect count per unit

UCL_c = c̄ + 3 × √c̄
LCL_c = c̄ − 3 × √c̄    (floor at 0)
```

No lookup table needed; limits come directly from the distribution parameters.

## Constant Verification: Recovering A₂ from d₂

You can verify any tabulated A₂ value with this formula:

```python
import math

d2 = {2: 1.128, 3: 1.693, 4: 2.059, 5: 2.326,
      6: 2.534, 7: 2.704, 8: 2.847, 9: 2.970, 10: 3.078}

for n, d in d2.items():
    A2 = 3 / (d * math.sqrt(n))
    print(f"n={n}: A2={A2:.3f}")
```

Output:
```
n=2: A2=1.880
n=3: A2=1.023
n=4: A2=0.729
n=5: A2=0.577
n=6: A2=0.483
n=7: A2=0.419
n=8: A2=0.373
n=9: A2=0.337
n=10: A2=0.308
```

These match the table exactly, confirming the formula derivation.

## Common Errors When Applying Constants

**Wrong n for I-MR chart.** Always use n=2 constants (d₂=1.128, D₄=3.267) for I-MR, regardless of how many observations you have. The n here refers to the moving range span, not the total sample size.

**Applying X-bar/R constants to individual data.** If you collect one reading per time period and mistakenly treat it as "subgroup of 1" in an X-bar/R framework, you'd need A₂ for n=1 — which is undefined (d₂ is not tabulated for n=1). Use I-MR instead.

**Recalculating R̄ as points are added.** Constants don't change, but R̄ and X̄̄ will shift. Control limits should be frozen once established from a stable baseline (typically 25+ subgroups). Recalculating limits continuously defeats the purpose of detecting a shift — the limits chase the data.

**Ignoring LCL_R = 0 for small n.** Some software prints a negative LCL_R before clamping to 0. Any negative LCL_R should be treated as 0. A range cannot be negative; the lower control limit for the R chart is only meaningful starting at n=7.

**Using specification limits as control limits.** Control limits are computed from A₂, D₃, D₄ applied to actual process data. They are never set from engineering tolerances or customer requirements. See SKILL.md IRON LAW.
