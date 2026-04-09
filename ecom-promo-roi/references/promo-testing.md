# Promo A/B Testing

A/B testing is the most reliable way to measure true incremental lift — it eliminates the baseline estimation problem by creating a real control group instead of estimating what "would have happened."

## When to Use A/B Testing vs. Before/After Analysis

| Situation | Method | Reason |
|-----------|--------|--------|
| Enough traffic volume (>2,000 orders/week) | A/B test | Control group eliminates baseline guesswork |
| Low volume or single SKU | Before/After with prior year | A/B needs statistical power |
| Testing promo type (% off vs. $ off) | A/B test | Direct comparison, same time period |
| Testing discount depth (10% vs. 20%) | A/B test | Controls for timing effects |
| One-time clearance event | Before/After | Can't exclude half your customers |
| New market / no history | A/B test | No baseline to reference |

## Experiment Design

### Step 1: Define the Hypothesis

```
H0 (Null): The promotion has no effect on incremental revenue
H1 (Alt):  The promotion increases incremental revenue by at least X%
```

"At least X%" should be your **minimum detectable effect (MDE)** — the smallest lift worth caring about commercially. Example: if a 5% incremental lift would cover the promo cost, set MDE = 5%.

### Step 2: Calculate Required Sample Size

For a two-proportion test comparing conversion rates:

```
n = 2 × (Z_α/2 + Z_β)² × p̄(1 - p̄) / δ²
```

Where:
- `Z_α/2` = 1.96 for α = 0.05 (95% confidence)
- `Z_β` = 0.84 for β = 0.20 (80% power)
- `p̄` = average conversion rate baseline
- `δ` = minimum detectable effect (absolute, e.g., 0.02 for 2pp lift)

**Worked example:**
- Baseline conversion rate: 3.5% (p̄ = 0.035)
- MDE: 1pp lift (δ = 0.01), i.e., you want to detect 3.5% → 4.5%
- α = 0.05, power = 80%

```
p̄(1 - p̄) = 0.035 × 0.965 = 0.03378
(1.96 + 0.84)² = 7.84
n = 2 × 7.84 × 0.03378 / 0.0001 = 5,298 per group
```

You need ~5,300 visitors per group, or ~10,600 total, before reading results.

**Quick lookup table** (α=0.05, power=80%, baseline conversion 3.5%):

| MDE | Sample per group | ~Days at 500 visitors/day |
|-----|-----------------|--------------------------|
| 0.5pp | 21,000 | 84 days |
| 1.0pp | 5,300 | 22 days |
| 1.5pp | 2,400 | 10 days |
| 2.0pp | 1,350 | 6 days |

If the required runtime exceeds your promo window, the A/B test isn't feasible. Fall back to before/after analysis.

### Step 3: Randomization Unit

Choose the right unit before the experiment starts. Changing it mid-test invalidates results.

| Unit | When to use | Watch out for |
|------|-------------|---------------|
| **User/customer ID** | Repeat-purchase categories (fashion, grocery) | New users without ID get random assignment — track them by cookie until login |
| **Session** | Low repeat-purchase, high anonymous traffic | Same user can see both treatments if they clear cookies |
| **Household / device** | When family members share an account | Hard to implement, rarely worth it |
| **Geographic region** | Promo can't be shown to half the visitors on the same page | Region-level noise can confound; needs larger geography |

For most e-commerce promos: **user ID** if you can, **session** if you have mostly anonymous traffic.

### Step 4: Assignment and Isolation

```python
import hashlib

def assign_variant(user_id: str, experiment_id: str, traffic_pct: float = 1.0) -> str:
    """
    Deterministic assignment: same user always gets same variant.
    traffic_pct: fraction of users included in experiment (0.0–1.0)
    Returns: 'control', 'treatment', or 'excluded'
    """
    hash_input = f"{experiment_id}:{user_id}"
    hash_val = int(hashlib.md5(hash_input.encode()).hexdigest(), 16) % 10000
    
    included_threshold = int(traffic_pct * 10000)
    if hash_val >= included_threshold:
        return "excluded"
    
    return "treatment" if hash_val % 2 == 0 else "control"
```

Key isolation rules:
- **No peeking**: Do not check results until the predetermined sample size is reached
- **No stopping early**: Even if treatment looks great on day 3, wait for full sample
- **Log assignment at first exposure**, not at purchase — this is the denominator

## Metrics to Measure

Primary metric (pick one):
- **Conversion rate** (orders / unique visitors) — most common
- **Revenue per visitor** — better when you care about AOV, not just conversion

Secondary metrics (do not make decisions on these, but track for learning):
- Average order value
- Items per order
- Return rate (30 days post-promo)
- New vs. returning customer mix

**Guard rail metrics** (experiment fails if these are violated):
- Page load time (promo banners can slow pages)
- Customer service contact rate (promo confusion causes tickets)

## Statistical Analysis

### Two-Proportion Z-Test (Conversion Rate)

```python
from math import sqrt

def two_prop_z_test(conv_treatment, n_treatment, conv_control, n_control):
    """
    Returns z-score and p-value (two-tailed).
    conv_*: number of conversions
    n_*: number of visitors
    """
    p1 = conv_treatment / n_treatment
    p2 = conv_control / n_control
    p_pool = (conv_treatment + conv_control) / (n_treatment + n_control)
    
    se = sqrt(p_pool * (1 - p_pool) * (1/n_treatment + 1/n_control))
    z = (p1 - p2) / se
    
    # Two-tailed p-value approximation
    # Use scipy.stats.norm.sf(abs(z)) * 2 in production
    return z, p1, p2

# Example
z, p_treat, p_ctrl = two_prop_z_test(
    conv_treatment=312, n_treatment=7000,
    conv_control=245, n_control=7000
)
# p_treat = 4.46%, p_ctrl = 3.50%
# Lift = +0.96pp absolute, +27% relative
# z ≈ 3.1 → p < 0.002 → statistically significant
```

### Revenue Per Visitor (T-Test or Mann-Whitney)

When revenue is the primary metric (highly skewed due to outlier orders), use:
- **Mann-Whitney U test** — robust to outliers, non-parametric
- Or **bootstrap confidence intervals** — resample 10,000 times, compute mean difference each time

```python
import random

def bootstrap_mean_diff(treatment_revenues, control_revenues, n_iterations=10000):
    """
    Returns 95% CI for (mean_treatment - mean_control).
    """
    diffs = []
    for _ in range(n_iterations):
        t_sample = random.choices(treatment_revenues, k=len(treatment_revenues))
        c_sample = random.choices(control_revenues, k=len(control_revenues))
        diffs.append(sum(t_sample)/len(t_sample) - sum(c_sample)/len(c_sample))
    
    diffs.sort()
    lo = diffs[int(0.025 * n_iterations)]
    hi = diffs[int(0.975 * n_iterations)]
    return lo, hi

# If CI does not include 0: statistically significant at 95%
```

## Reading the Results

### Decision Matrix

| Statistical significance | Practical significance (lift > MDE) | Decision |
|-------------------------|-------------------------------------|----------|
| Yes | Yes | Ship the promo |
| Yes | No | Promo works but isn't worth the cost — don't scale |
| No | Yes | Need more data — extend experiment or accept uncertainty |
| No | No | No evidence this promo works — don't ship |

**Practical significance** = the observed lift is large enough to cover promo cost at scale. Always verify:

```
Promo ROI check:
  Incremental Revenue = Lift (%) × Baseline Revenue
  Incremental Gross Profit = Incremental Revenue × Gross Margin
  Promo Cost = Discount given + Marketing spend + Ops cost
  ROI = (Incremental Gross Profit - Promo Cost) / Promo Cost
```

A promo can be statistically significant (we're confident it lifts sales) but still unprofitable if the lift is too small to cover the discount cost.

### Segmentation: Do Not Run Before Significance

Wait until the overall experiment reaches significance, then segment to understand *who* responded. Common cuts:

- New vs. returning customers
- Mobile vs. desktop
- Acquisition channel (paid vs. organic)
- Product category

Treat segments as learning, not as decision criteria. Multiple comparisons inflate false positive rate — apply Bonferroni correction or treat segment findings as hypotheses for the next test.

## Common Mistakes

**Starting the experiment after the promo was announced**
Users who saw the announcement (email blast, social post) self-select into high-intent behavior before being assigned to a variant. Assignment must happen at or before first exposure to any promo signal.

**Using the same experiment ID across multiple promos**
Hash-based assignment is deterministic. Reusing an experiment ID means the same users always get treatment or control, which can create correlation artifacts across promos. Rotate experiment IDs.

**Measuring only during the promo window**
Pull-forward and post-promo dips matter. Measure revenue for at least 2 weeks post-promo end for both groups. Many promos that look profitable during the event lose money when the dip is included.

**Excluding coupon codes from control group analysis**
If treatment gets a promo banner and control gets nothing, but both groups can redeem a public coupon code, control group redemptions will contaminate your measurement. Track coupon code usage by variant.

**Underpowering on a short flash sale**
A 24-hour flash sale rarely gets enough traffic for statistical significance. Use it to measure engagement metrics (click-through, add-to-cart) rather than conversion or revenue. Don't make ROI decisions from underpowered flash sale data — use historical before/after instead.

## Promo Type A/B Test Template

When comparing two promo types (e.g., 20% off vs. NT$200 off orders >NT$1,000):

```
Experiment: [Promo Name] Type Comparison
Start date: YYYY-MM-DD
Target end date: YYYY-MM-DD (after n_required reached)

Groups:
  - Control:   No promo (or current default)
  - Treatment A: 20% off
  - Treatment B: NT$200 off >NT$1,000

Primary metric: Revenue per visitor
MDE: NT$15/visitor incremental (covers discount cost)
Required n per group: [calculate]
Traffic split: 33% / 33% / 33%

Guard rails:
  - Page error rate < 0.5%
  - CS contact rate increase < 20%

Analysis date: [do not analyze before this date]
Decision owner: [name]
```

Multi-variant tests (more than 2 groups) require adjusting significance threshold: use α/k where k = number of pairwise comparisons, or use a FWER-controlled method like Holm-Bonferroni.
