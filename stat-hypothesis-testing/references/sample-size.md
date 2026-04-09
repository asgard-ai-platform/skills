# Sample Size Calculation

Sample size must be determined **before data collection**. Calculating it after data collection to justify results is p-hacking.

---

## Why Sample Size Matters

| Problem | Consequence |
|---------|-------------|
| Too small | Low power (β↑) — real effects go undetected (Type II error) |
| Too large | Wastes resources; trivially small effects become "significant" |
| Calculated post-hoc | Invalid — circular reasoning, biases toward observed effect |

---

## The Four Parameters

Every sample size calculation requires exactly four inputs. If you don't know one, you must estimate or justify it.

| Parameter | Symbol | Role | Typical value |
|-----------|--------|------|---------------|
| Significance level | α | Max acceptable Type I error rate | 0.05 |
| Power | 1 − β | Probability of detecting a real effect | 0.80 (sometimes 0.90) |
| Effect size | δ, d, f, w | Magnitude of the difference you care about | domain-specific |
| Sample size | n | What you're solving for | — |

The relationship is a constraint: fix any three, the fourth is determined.

---

## Effect Size: The Number Everyone Guesses Wrong

Effect size is the most important and most mishandled input. Do not use "I want to detect any effect" — this implies n → ∞.

### How to specify effect size

**Option A — Domain threshold (preferred)**  
Define the smallest effect that would change a decision.  
Example: "A conversion rate lift below 0.5 percentage points isn't worth the engineering cost."

**Option B — Prior literature**  
Use effect sizes reported in similar studies. Be conservative (published studies overestimate effects due to publication bias).

**Option C — Cohen's conventional benchmarks (last resort)**  
Only use when you have no domain knowledge or prior data.

| Test | Small | Medium | Large |
|------|-------|--------|-------|
| t-test (Cohen's d) | 0.2 | 0.5 | 0.8 |
| ANOVA (Cohen's f) | 0.10 | 0.25 | 0.40 |
| Chi-square (Cohen's w) | 0.1 | 0.3 | 0.5 |
| Correlation (r) | 0.1 | 0.3 | 0.5 |

Cohen himself cautioned that these benchmarks are arbitrary and context-free.

---

## Formulas by Test Type

### Two-sample independent t-test

**Scenario**: Compare means of two independent groups (equal n per group).

$$n = \frac{2(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

Where:
- $z_{\alpha/2}$ = critical z for significance level (1.96 for α=0.05, two-tailed)
- $z_\beta$ = critical z for power (0.842 for 80% power, 1.282 for 90%)
- $\sigma$ = standard deviation (assumed equal in both groups)
- $\delta$ = minimum detectable difference ($\mu_1 - \mu_2$)

**Equivalent using Cohen's d** ($d = \delta / \sigma$):

$$n = \frac{2(z_{\alpha/2} + z_\beta)^2}{d^2}$$

#### Worked example

A product team wants to detect a 5-point increase in NPS (scale 0–100).  
Historical NPS SD: σ = 20. They want α = 0.05, power = 0.80.

$$d = \frac{5}{20} = 0.25$$

$$n = \frac{2(1.96 + 0.842)^2}{0.25^2} = \frac{2 \times 7.85}{0.0625} = \frac{15.70}{0.0625} \approx 251 \text{ per group}$$

**Total required: 502 participants.**

---

### One-sample t-test

**Scenario**: Compare a sample mean to a known constant.

$$n = \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

Half the sample size of the two-sample case because there's no second group to measure.

---

### Paired t-test (before/after, matched pairs)

Same formula as one-sample t-test, but σ is the **standard deviation of the paired differences**, not the raw variable. If pre-post measurements are correlated at ρ:

$$\sigma_{diff} = \sigma\sqrt{2(1-\rho)}$$

Higher correlation → smaller σ_diff → smaller n needed. This is why within-subject designs are more efficient than between-subject designs.

---

### Chi-square test of independence

**Scenario**: Categorical outcome, comparing proportions between groups.

For comparing two proportions $p_1$ and $p_2$:

$$n = \frac{(z_{\alpha/2} + z_\beta)^2 [p_1(1-p_1) + p_2(1-p_2)]}{(p_1 - p_2)^2}$$

#### Worked example

Baseline conversion rate: 3%. Goal: detect a lift to 4.5% (absolute +1.5 pp).  
α = 0.05 (two-tailed), power = 0.80.

$$n = \frac{(1.96 + 0.842)^2 [0.03 \times 0.97 + 0.045 \times 0.955]}{(0.03 - 0.045)^2}$$

$$= \frac{7.85 \times [0.0291 + 0.042975]}{0.000225}$$

$$= \frac{7.85 \times 0.072075}{0.000225} \approx \frac{0.5658}{0.000225} \approx 2514 \text{ per group}$$

**Total: ~5,028 conversions needed.** At 3% baseline, you need ~83,800 visitors per group if measuring on visitors.

This illustrates why detecting small absolute lifts at low base rates is expensive.

---

### One-way ANOVA (k groups)

Using Cohen's f:

$$n_{per group} = \frac{(z_{\alpha/2} + z_\beta)^2}{f^2} \cdot \frac{k+1}{k}$$

Or more precisely, use the non-central F distribution (requires software — see Python snippet below).

---

## z-values Quick Reference

| α (two-tailed) | $z_{\alpha/2}$ | Power (1−β) | $z_\beta$ |
|----------------|---------------|-------------|-----------|
| 0.10 | 1.645 | 0.70 | 0.524 |
| 0.05 | 1.960 | 0.80 | 0.842 |
| 0.01 | 2.576 | 0.90 | 1.282 |
| 0.001 | 3.291 | 0.95 | 1.645 |

One-tailed test: use $z_\alpha$ instead of $z_{\alpha/2}$ (e.g., 1.645 for α=0.05 one-tailed).

---

## Python: Computing Sample Size

```python
from scipy.stats import norm
import math

def sample_size_two_sample_ttest(
    effect_size_d: float,  # Cohen's d = delta / sigma
    alpha: float = 0.05,
    power: float = 0.80,
    two_tailed: bool = True
) -> int:
    """
    Returns required n PER GROUP for a two-sample independent t-test.
    """
    if two_tailed:
        z_alpha = norm.ppf(1 - alpha / 2)
    else:
        z_alpha = norm.ppf(1 - alpha)
    z_beta = norm.ppf(power)
    n = 2 * (z_alpha + z_beta) ** 2 / effect_size_d ** 2
    return math.ceil(n)


def sample_size_two_proportions(
    p1: float,
    p2: float,
    alpha: float = 0.05,
    power: float = 0.80,
    two_tailed: bool = True
) -> int:
    """
    Returns required n PER GROUP for a two-proportion z-test (chi-square equivalent).
    """
    if two_tailed:
        z_alpha = norm.ppf(1 - alpha / 2)
    else:
        z_alpha = norm.ppf(1 - alpha)
    z_beta = norm.ppf(power)
    pooled_var = p1 * (1 - p1) + p2 * (1 - p2)
    n = (z_alpha + z_beta) ** 2 * pooled_var / (p1 - p2) ** 2
    return math.ceil(n)


# Example usage
n = sample_size_two_sample_ttest(effect_size_d=0.25)
print(f"n per group: {n}")   # → 252

n = sample_size_two_proportions(p1=0.03, p2=0.045)
print(f"n per group: {n}")   # → 2514
```

For ANOVA, logistic regression, and survival analysis, use `statsmodels.stats.power`:

```python
from statsmodels.stats.power import (
    TTestIndPower,
    TTestPower,
    FTestAnovaPower,
    GofChisquarePower,
    NormalIndPower,
)

# Two-sample t-test
analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.25, alpha=0.05, power=0.80, ratio=1.0)
print(math.ceil(n))  # per group

# One-way ANOVA (Cohen's f)
analysis = FTestAnovaPower()
n = analysis.solve_power(effect_size=0.25, alpha=0.05, power=0.80, k_groups=3)
print(math.ceil(n))  # per group
```

---

## Sensitivity Analysis: Power Curves

Don't report a single n. Show how n varies with effect size — this communicates the tradeoff honestly.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()
effect_sizes = np.arange(0.1, 1.0, 0.05)

for power_target in [0.70, 0.80, 0.90]:
    ns = [math.ceil(analysis.solve_power(d, alpha=0.05, power=power_target))
          for d in effect_sizes]
    plt.plot(effect_sizes, ns, label=f"Power={power_target}")

plt.xlabel("Cohen's d (effect size)")
plt.ylabel("n per group")
plt.yscale("log")
plt.legend()
plt.title("Required Sample Size vs. Effect Size")
plt.grid(True)
plt.show()
```

The log-scale y-axis reveals that detecting small effects (d < 0.2) requires dramatically larger samples than medium effects (d = 0.5).

---

## Unequal Group Sizes

When the control group is larger than the treatment group (common in observational studies or when one condition is costly), use the harmonic mean:

$$n_{harmonic} = \frac{2 n_1 n_2}{n_1 + n_2}$$

For a fixed total N, equal groups maximize power. If groups are unequal with ratio $k = n_2 / n_1$:

$$n_1 = \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2 (1 + 1/k)}{\delta^2}$$

**Rule of thumb**: group size ratio beyond 3:1 substantially degrades power. Beyond 4:1, consider whether the design is worth the cost.

---

## Multiple Comparisons Adjustment

If you plan to test $m$ hypotheses on the same dataset, adjust α before computing sample sizes — not after.

| Method | Adjusted α | When to use |
|--------|-----------|-------------|
| Bonferroni | α / m | Conservative; m is small; tests are independent |
| Šidák | 1 − (1−α)^(1/m) | Slightly less conservative than Bonferroni |
| FDR (Benjamini-Hochberg) | Controlled at q | Many comparisons; some false positives acceptable |

Example: 5 planned comparisons at α = 0.05.  
Bonferroni corrected: α_adj = 0.05 / 5 = 0.01 → use $z_{\alpha/2}$ = 2.576.  
This increases required n by roughly 50% versus α = 0.05.

**Compute n using the adjusted α**, not 0.05.

---

## Common Mistakes

**Mistake 1: Using the observed effect size from a pilot study directly**  
Pilot studies overestimate effects due to random fluctuation. Discount the observed effect by 25–50%, or use the lower bound of the pilot's confidence interval.

**Mistake 2: Forgetting attrition and exclusions**  
If you expect 20% dropout or exclusion, inflate n:

$$n_{enrolled} = \frac{n_{required}}{1 - \text{attrition rate}} = \frac{252}{0.80} = 315 \text{ per group}$$

**Mistake 3: Assuming equal variance without checking**  
If group variances differ substantially, use the unequal-variance form. If σ₂ = 2σ₁, equal-n design is no longer optimal.

**Mistake 4: Conflating one-tailed and two-tailed**  
One-tailed tests require ~20% fewer participants. Only use one-tailed when you can definitively rule out effects in the other direction before data collection — not because it's convenient.

**Mistake 5: Not accounting for clustering**  
If units are clustered (e.g., users within stores, patients within hospitals), simple formulas underestimate required n. Multiply by the design effect:

$$DEFF = 1 + (m - 1)\rho$$

where $m$ = cluster size, $\rho$ = intraclass correlation. For ρ = 0.05 and m = 20: DEFF = 1.95 — you need nearly twice as many participants.

---

## Decision Checklist

Before finalizing sample size:

- [ ] Effect size is based on domain threshold or prior literature, not Cohen's benchmarks alone
- [ ] α is set (and adjusted for multiple comparisons if applicable)
- [ ] Power target is justified (0.80 minimum; 0.90 for high-stakes decisions)
- [ ] Attrition and exclusion rate accounted for
- [ ] Clustering accounted for if design is hierarchical
- [ ] Sample size is per group, and total is stated explicitly
- [ ] Sensitivity analysis shows n across a plausible range of effect sizes
- [ ] Calculation is documented and reproducible (code or formula + inputs recorded)
