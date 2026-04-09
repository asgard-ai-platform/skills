# Higher-Digit Tests in Benford's Law Analysis

Second and third digit tests extend Benford's Law beyond the first digit to detect subtler manipulation patterns that first-digit analysis cannot catch.

---

## Why First-Digit Analysis Is Not Enough

A fraudster who knows Benford's Law can construct fake numbers whose first digits conform — simply by randomly generating amounts where ~30% start with 1, ~18% start with 2, etc. The first-digit test will pass.

What such a fraudster cannot easily control: the joint distribution of the first two or three digits. Higher-digit tests close this gap.

---

## Expected Distributions

### Second Digit

The expected probability for digit d (0–9) in the **second** position:

```
P₂(d) = Σ_{k=1}^{9} log₁₀(1 + 1/(10k + d))
```

| Digit | Expected % |
|-------|-----------|
| 0     | 11.97     |
| 1     | 11.39     |
| 2     | 10.88     |
| 3     | 10.43     |
| 4     | 10.03     |
| 5     | 9.67      |
| 6     | 9.34      |
| 7     | 9.04      |
| 8     | 8.76      |
| 9     | 8.50      |

Unlike the first digit (where 0 is excluded), the second digit includes 0, and the distribution is much flatter — roughly 8.5–12% per digit vs. 4.6–30.1%.

### First-Two-Digits (Combined)

For the first two digits viewed jointly (leading pair 10–99), the expected probability is simply:

```
P₁₂(n) = log₁₀(1 + 1/n)    for n ∈ {10, 11, 12, ..., 99}
```

This gives 90 distinct expected frequencies, each around 0.4–4.1%.

| Leading pair | Expected % |
|-------------|-----------|
| 10          | 4.14      |
| 11          | 3.78      |
| 19          | 2.26      |
| 50          | 0.86      |
| 99          | 0.44      |

This is the **most sensitive test** for fabrication because there are 90 bins to match rather than 9.

### Third Digit

The third-digit distribution is nearly uniform: each digit 0–9 should appear approximately 10% of the time, with slight decreases from 0 to 9. In practice, deviations from uniformity in the third digit indicate extreme clustering or rounding behavior.

---

## Fraud Patterns Each Test Catches

| Test | Fabrication Pattern Detected |
|------|------------------------------|
| First digit | Gross deviation (naïve number invention) |
| Second digit | Subtle rounding, threshold avoidance |
| First-two-digits | Clustering around specific amounts (e.g., $49xx, $99xx) |
| Third digit | Rounding to nearest 10 or 100 |

### Threshold Avoidance — The Classic Second-Digit Indicator

If a company requires manager approval for purchases over $5,000, a fraudster submits claims for $4,900, $4,850, $4,920. The first digit is 4 in all cases — fine. But the second digit clusters heavily on 8 and 9. This is invisible to a first-digit test.

The second-digit test will flag an unusually high frequency of digit 9 (or 8) in the second position when the dataset contains threshold-avoidance behavior.

---

## Step-by-Step: Second-Digit Test

### Step 1 — Extract second digits

For each number in the dataset, normalize to remove the leading digit:

```python
def extract_second_digit(n: float) -> int | None:
    """Return second significant digit, or None if number has only one digit."""
    import math
    if n <= 0:
        n = abs(n)
    if n == 0:
        return None
    # Shift to range [10, 100)
    magnitude = math.floor(math.log10(n))
    shifted = n / (10 ** (magnitude - 1))  # now in [10, 100)
    return int(shifted) % 10
```

### Step 2 — Compute expected frequencies

```python
import math

def second_digit_expected() -> dict[int, float]:
    probs = {}
    for d in range(10):
        p = sum(math.log10(1 + 1/(10*k + d)) for k in range(1, 10))
        probs[d] = p
    return probs

# Expected values (verified):
# {0: 0.1197, 1: 0.1139, 2: 0.1088, 3: 0.1043, 4: 0.1003,
#  5: 0.0967, 6: 0.0934, 7: 0.0904, 8: 0.0876, 9: 0.0850}
```

### Step 3 — Compute MAD for second-digit test

Use the same MAD formula as in the first-digit test:

```
MAD₂ = (1/10) × Σ_{d=0}^{9} |observed_pct(d) − expected_pct(d)|
```

MAD thresholds for the **second-digit test** are identical to first-digit MAD thresholds:

| MAD        | Conformity        |
|------------|-------------------|
| < 0.008    | Close             |
| 0.008–0.012| Acceptable        |
| 0.012–0.016| Marginal          |
| > 0.016    | Non-conforming    |

*(Thresholds vary slightly by author; some practitioners use the same 0.006/0.012/0.015 cutoffs as for first digits. Use consistently within a single engagement.)*

### Step 4 — Chi-squared for second digits

```
χ² = Σ_{d=0}^{9} (O_d − E_d)² / E_d     df = 9
```

Critical value at α=0.05 with df=9 is **16.92**. Flag if χ² > 16.92.

---

## Step-by-Step: First-Two-Digits Test

### Step 1 — Extract leading pairs

```python
def extract_leading_pair(n: float) -> int | None:
    """Return leading two-digit integer (10–99)."""
    import math
    if n <= 0:
        n = abs(n)
    if n == 0:
        return None
    magnitude = math.floor(math.log10(n))
    shifted = n / (10 ** (magnitude - 1))  # in [10, 100)
    return int(shifted)  # truncate to integer in {10,...,99}
```

### Step 2 — Expected probabilities

```python
def first_two_expected() -> dict[int, float]:
    return {n: math.log10(1 + 1/n) for n in range(10, 100)}
```

### Step 3 — Z-score per bin

With 90 bins, chi-squared has df = 89 (critical value ≈ 113 at α=0.05). For focused investigation, compute Z-scores per bin:

```
Z(n) = (O_n − E_n) / sqrt(E_n × (1 − E_n) / N)
```

where N is total record count, O_n is observed proportion, E_n is expected proportion.

Flag any leading pair with |Z| > 1.96 (α=0.05, two-tailed). Adjust with Bonferroni correction for 90 simultaneous tests: use |Z| > 3.29 to hold family-wise error rate at 5%.

### Worked Example: Expense Report Cluster

Dataset: 3,000 expense claims. Expected count for leading pair "49" (amounts $4,900–$4,999):

```
E("49") = log₁₀(1 + 1/49) × 3000
        = log₁₀(1.0204...) × 3000
        = 0.00877 × 3000
        = 26.3 claims
```

Observed: 94 claims.

```
Z("49") = (94/3000 − 0.00877) / sqrt(0.00877 × 0.99123 / 3000)
        = (0.03133 − 0.00877) / sqrt(0.0000029)
        = 0.02256 / 0.001703
        = 13.25
```

Z = 13.25 far exceeds any threshold. This pair warrants immediate investigation for approval threshold avoidance at $5,000.

---

## Decision Framework: Which Test to Run

```
Start
│
├─ First-digit MAD > 0.012?
│   ├─ YES → Gross anomaly present. Report first-digit findings.
│   │         Also run second-digit and first-two-digit tests.
│   └─ NO  → First digit conforms. Proceed to second-digit test.
│
├─ Second-digit MAD > 0.012?
│   ├─ YES → Subtle fabrication or threshold avoidance likely.
│   │         Run first-two-digit test to identify specific clusters.
│   └─ NO  → Second digit conforms. Proceed only if context warrants.
│
└─ First-two-digit Z-scores (Bonferroni-corrected)?
    ├─ Any |Z| > 3.29 → Pinpoint cluster. Document specific amounts.
    └─ None → Dataset conforms at two-digit level.
```

Do not run all three tests on every dataset by default. First-two-digit tests on small datasets (< 1,000 records) will generate spurious flags due to low expected counts per bin (many bins have E < 5, violating chi-squared assumptions).

**Minimum sample sizes by test:**

| Test             | Minimum N |
|------------------|-----------|
| First digit      | 500       |
| Second digit     | 500       |
| First-two-digits | 1,000     |
| Third digit      | 2,000     |

---

## Third-Digit Test: When and How

The third-digit test is appropriate when you suspect **rounding to the nearest 10 or 100** — a common pattern when employees estimate amounts rather than using actual receipts.

Expected distribution: nearly uniform at ~10% per digit (0–9), with a slight skew:

```python
def third_digit_expected() -> dict[int, float]:
    import math
    probs = {}
    for d in range(10):
        p = sum(
            math.log10(1 + 1/(100*k + 10*j + d))
            for k in range(1, 10)
            for j in range(10)
        )
        probs[d] = p
    return probs
# Approximate: all near 0.10, digit 0 ≈ 0.1018, digit 9 ≈ 0.0983
```

**Rounding signature**: if employees round amounts to the nearest $10, the third digit should be 0 far more often than 10%. Observed frequency of 0 in the 25–30% range is a strong rounding indicator.

**Uniform digit test** (simplified for third digit):

```
χ² = Σ_{d=0}^{9} (O_d − N/10)² / (N/10)     df = 9
```

This approximation is valid because the third-digit expected distribution is nearly flat.

---

## Combining Test Results

No single test is definitive. Use a weight-of-evidence approach:

| Findings | Assessment |
|----------|-----------|
| First digit conforms, second digit conforms | Strong conformity |
| First digit conforms, second digit flags | Threshold manipulation likely; low-risk gross fabrication |
| First digit flags, second conforms | Possible dataset mixing or structural constraint; recheck Iron Law conditions |
| Both flag, specific first-two-digit clusters found | High-risk; pinpoint amounts for review |
| Third digit spikes at 0 | Rounding behavior; may be benign estimation |
| Third digit spikes at 5 | Rounding to nearest 50 or 500; investigate further |

---

## Common Misuse

**Running second-digit tests on constrained-range data.** If amounts are all between $100–$199 (e.g., a fixed-fee category), the second digit distribution is structurally determined by the data range, not by Benford's Law. The test will always fail — this is expected, not suspicious. The Iron Law from the parent skill applies equally to higher-digit tests: verify that the underlying data type is appropriate before drawing conclusions.

**Treating each test as independent evidence.** Second-digit deviations in the same digit cluster as first-digit deviations are not additive evidence — they may reflect the same underlying pattern measured twice. Identify the root cause (specific amount cluster, approval threshold) before quantifying the anomaly's severity.
