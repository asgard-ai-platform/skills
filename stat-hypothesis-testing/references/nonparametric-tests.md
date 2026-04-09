# Nonparametric Tests

Nonparametric tests make no assumption about the population distribution. Use them when parametric assumptions (normality, equal variance) are violated — especially with small samples, ordinal data, or heavy skew.

## When to Switch from Parametric

| Condition | Action |
|-----------|--------|
| n < 30 AND distribution unknown/non-normal | Use nonparametric |
| Ordinal data (Likert, rankings) | Always nonparametric |
| Outliers that cannot be removed | Use nonparametric |
| n ≥ 30, mild skew | t-test/ANOVA still robust (CLT) |
| Confirmed normal by Shapiro-Wilk (p > 0.05) | Parametric preferred |

**Shapiro-Wilk** is the standard normality check for n < 50. For n ≥ 50, use Q-Q plot + skewness/kurtosis inspection — Shapiro-Wilk becomes oversensitive.

## Parametric → Nonparametric Equivalents

| Parametric Test | Nonparametric Equivalent | Replaces |
|-----------------|--------------------------|---------|
| Independent t-test | Mann-Whitney U | 2 independent groups |
| Paired t-test | Wilcoxon Signed-Rank | 2 paired/before-after groups |
| One-way ANOVA | Kruskal-Wallis H | 3+ independent groups |
| Repeated-measures ANOVA | Friedman test | 3+ related groups |
| Pearson correlation | Spearman ρ | Relationship between 2 variables |

## Mann-Whitney U Test

**Use**: Two independent groups, continuous or ordinal outcome, non-normal.

### Procedure

1. Pool all observations, rank from lowest (1) to highest
2. Assign ranks back to original groups (ties get average rank)
3. Sum the ranks for each group: R₁, R₂

```
U₁ = n₁·n₂ + n₁(n₁+1)/2 − R₁
U₂ = n₁·n₂ + n₂(n₂+1)/2 − R₂
U = min(U₁, U₂)
```

4. For small samples (n < 20): compare U to critical value table
5. For large samples (n ≥ 20): use normal approximation

```
z = (U − n₁n₂/2) / sqrt(n₁·n₂·(n₁+n₂+1)/12)
```

### Worked Example

Group A recovery days: 3, 5, 7, 8, 12  
Group B recovery days: 6, 9, 11, 14, 18

**Step 1 — Pool and rank:**

| Value | Group | Rank |
|-------|-------|------|
| 3 | A | 1 |
| 5 | A | 2 |
| 6 | B | 3 |
| 7 | A | 4 |
| 8 | A | 5 |
| 9 | B | 6 |
| 11 | B | 7 |
| 12 | A | 8 |
| 14 | B | 9 |
| 18 | B | 10 |

**Step 2 — Sum ranks:**  
R₁ (Group A) = 1+2+4+5+8 = 20  
R₂ (Group B) = 3+6+7+9+10 = 35

**Step 3 — Calculate U:**  
U₁ = 5·5 + 5·6/2 − 20 = 25 + 15 − 20 = 20  
U₂ = 5·5 + 5·6/2 − 35 = 25 + 15 − 35 = 5  
U = min(20, 5) = **5**

For n₁=n₂=5, critical value at α=0.05 (two-tailed) = 2.  
U = 5 > 2 → **Fail to reject H₀**. No significant difference.

### Effect Size (r)

```
r = z / sqrt(N)    where N = total observations
```

Interpretation: |r| < 0.3 small, 0.3–0.5 medium, > 0.5 large.

### Python

```python
from scipy.stats import mannwhitneyu

group_a = [3, 5, 7, 8, 12]
group_b = [6, 9, 11, 14, 18]

stat, p = mannwhitneyu(group_a, group_b, alternative='two-sided')
print(f"U={stat}, p={p:.4f}")

# Effect size
import numpy as np
n = len(group_a) + len(group_b)
z = (stat - len(group_a)*len(group_b)/2) / np.sqrt(len(group_a)*len(group_b)*(n+1)/12)
r = abs(z) / np.sqrt(n)
print(f"r={r:.3f}")
```

## Wilcoxon Signed-Rank Test

**Use**: Two paired/related measurements on the same subjects (before-after, matched pairs), non-normal differences.

### Procedure

1. Compute differences: dᵢ = x₂ᵢ − x₁ᵢ
2. Drop pairs where dᵢ = 0
3. Rank |dᵢ| from smallest (1) to largest; ties get average rank
4. Assign the sign of dᵢ to each rank
5. W⁺ = sum of positive ranks; W⁻ = sum of negative ranks
6. W = min(W⁺, W⁻)
7. Compare to critical value (small n) or use z approximation (n > 25)

```
z = (W − n(n+1)/4) / sqrt(n(n+1)(2n+1)/24)
```

### Worked Example

Pain scores before/after treatment (lower = better):

| Patient | Before | After | d | \|d\| | Rank | Signed Rank |
|---------|--------|-------|---|-------|------|-------------|
| 1 | 7 | 4 | −3 | 3 | 4.5 | −4.5 |
| 2 | 5 | 3 | −2 | 2 | 2.5 | −2.5 |
| 3 | 8 | 5 | −3 | 3 | 4.5 | −4.5 |
| 4 | 6 | 7 | +1 | 1 | 1 | +1 |
| 5 | 9 | 7 | −2 | 2 | 2.5 | −2.5 |
| 6 | 4 | 8 | +4 | 4 | 6 | +6 |

W⁺ = 1 + 6 = 7  
W⁻ = 4.5 + 2.5 + 4.5 + 2.5 = 14  
W = min(7, 14) = **7**

For n=6, critical value at α=0.05 (two-tailed) = 0.  
W = 7 > 0 → **Fail to reject H₀**.

### Python

```python
from scipy.stats import wilcoxon

before = [7, 5, 8, 6, 9, 4]
after  = [4, 3, 5, 7, 7, 8]

stat, p = wilcoxon(before, after, alternative='two-sided')
print(f"W={stat}, p={p:.4f}")
```

## Kruskal-Wallis H Test

**Use**: Three or more independent groups, continuous or ordinal outcome, non-normal. Nonparametric replacement for one-way ANOVA.

**IRON LAW reinforcement**: Kruskal-Wallis tests whether AT LEAST ONE group differs. A significant result does not tell you WHICH groups differ — you need post-hoc tests (Dunn's test with Bonferroni correction).

### Formula

```
H = [12 / N(N+1)] · Σ(Rⱼ² / nⱼ) − 3(N+1)
```

Where:
- N = total observations
- nⱼ = observations in group j
- Rⱼ = sum of ranks in group j

H follows chi-square distribution with df = k−1 (k = number of groups).

### Python

```python
from scipy.stats import kruskal
import scikit_posthocs as sp  # for Dunn's post-hoc

group1 = [2, 4, 6, 8]
group2 = [3, 5, 9, 12]
group3 = [1, 7, 11, 15]

stat, p = kruskal(group1, group2, group3)
print(f"H={stat:.3f}, p={p:.4f}")

if p < 0.05:
    # Post-hoc: Dunn's test with Bonferroni correction
    import pandas as pd
    data = pd.DataFrame({
        'value': group1 + group2 + group3,
        'group': ['A']*4 + ['B']*4 + ['C']*4
    })
    posthoc = sp.posthoc_dunn(data, val_col='value', group_col='group', p_adjust='bonferroni')
    print(posthoc)
```

## Spearman Rank Correlation

**Use**: Relationship between two variables when either is ordinal, non-normal, or the relationship is monotonic but not linear.

### Formula

```
ρ = 1 − 6·Σdᵢ² / (n(n²−1))
```

Where dᵢ = difference in ranks for observation i.

This formula assumes no ties. With ties, use Pearson's formula on the ranked data.

### Worked Example

Study hours vs. exam score (5 students):

| Student | Hours | Score | Rank Hours | Rank Score | d | d² |
|---------|-------|-------|------------|------------|---|----|
| A | 2 | 55 | 1 | 1 | 0 | 0 |
| B | 4 | 70 | 2 | 3 | −1 | 1 |
| C | 6 | 65 | 3 | 2 | 1 | 1 |
| D | 8 | 85 | 4 | 4 | 0 | 0 |
| E | 10 | 90 | 5 | 5 | 0 | 0 |

ρ = 1 − 6·(0+1+1+0+0) / (5·(25−1))  
ρ = 1 − 12/120 = 1 − 0.1 = **0.9**

Strong positive monotonic relationship.

### Python

```python
from scipy.stats import spearmanr

hours = [2, 4, 6, 8, 10]
score = [55, 70, 65, 85, 90]

rho, p = spearmanr(hours, score)
print(f"ρ={rho:.3f}, p={p:.4f}")
```

### Pearson vs. Spearman

| Condition | Use |
|-----------|-----|
| Both variables normal + linear relationship | Pearson |
| Either variable ordinal | Spearman |
| Outliers present | Spearman |
| Non-linear but monotonic relationship | Spearman |
| Both variables normal, outlier-free | Pearson (more powerful) |

## Effect Sizes for Nonparametric Tests

Nonparametric tests are not exempt from the IRON LAW: always report effect size.

| Test | Effect Size | Formula | Thresholds (Cohen) |
|------|-------------|---------|-------------------|
| Mann-Whitney U | r | z / √N | 0.1 small, 0.3 medium, 0.5 large |
| Wilcoxon | r | z / √N | same |
| Kruskal-Wallis | η² | (H − k + 1) / (N − k) | 0.01 small, 0.06 medium, 0.14 large |
| Spearman | ρ² | square of ρ | treat like r² |

## Common Mistakes

**Using nonparametric when not needed.** If n ≥ 30 and skew is mild, t-test/ANOVA are robust. Switching to nonparametric unnecessarily reduces power.

**Forgetting post-hoc tests after Kruskal-Wallis.** A significant H statistic only means "at least one group differs." Always follow up with Dunn's test and apply Bonferroni correction (see Gotchas in parent skill on multiple comparisons).

**Treating nonparametric as assumption-free.** Mann-Whitney still assumes independence of observations. Wilcoxon requires symmetry of differences if you want to interpret it as a location test. Kruskal-Wallis assumes groups have similar distribution shapes (if only testing medians).

**Misinterpreting what nonparametric tests compare.** Mann-Whitney U is often described as comparing medians, but it actually tests whether one distribution is stochastically greater. If distributions have different shapes, a significant result means more than "median A > median B."

**Applying Wilcoxon to independent samples.** Wilcoxon Signed-Rank requires paired data. For independent groups, use Mann-Whitney U.
