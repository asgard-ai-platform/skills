# Bayesian A/B Testing

Bayesian A/B testing replaces the binary reject/fail-to-reject decision with a probability statement: "there is an X% chance that treatment is better than control." This is often what decision-makers actually want, but it requires explicit prior beliefs and a different stopping framework.

## The Beta-Binomial Model (Conversion Rates)

For binary outcomes (converted / not converted), the conjugate prior is the **Beta distribution**.

### Setup

```
Prior:        θ_A ~ Beta(α₀, β₀)    # beliefs before data
              θ_B ~ Beta(α₀, β₀)

After seeing data:
  Control:    n_A visitors, k_A conversions
  Treatment:  n_B visitors, k_B conversions

Posterior:    θ_A | data ~ Beta(α₀ + k_A,  β₀ + (n_A - k_A))
              θ_B | data ~ Beta(α₀ + k_B,  β₀ + (n_B - k_B))
```

The posterior parameters are just the prior counts plus the observed counts — no integration needed.

### Prior Choice

| Prior | α₀ | β₀ | Meaning | When to use |
|-------|-----|-----|---------|-------------|
| Uniform (flat) | 1 | 1 | Complete ignorance | Discouraged — see note below |
| Weakly informative | 1 | 19 | Centers at 5% conversion | Baseline ~5%, low confidence |
| Historical | α* | β* | Matched to historical rate | You have 3+ months of data |

**How to set a historical prior**: if your historical conversion rate is `p` and you want to encode `N_prior` effective observations:
```
α₀ = p × N_prior
β₀ = (1 - p) × N_prior
```

Example: 8% conversion, encode 100 prior observations → `Beta(8, 92)`.

**Why avoid Uniform(1,1)**: It assigns equal probability to a 99% conversion rate and a 1% one. Use at minimum `Beta(1, 9)` for realistic e-commerce contexts.

---

## Worked Example

**Setup:**
- Baseline conversion rate: 5%
- Prior: `Beta(5, 95)` (100 effective prior obs, centered at 5%)
- Control sees 2,000 visitors, 104 conversions
- Treatment sees 2,000 visitors, 130 conversions

**Posteriors:**
```
θ_A | data ~ Beta(5 + 104,  95 + 1896) = Beta(109, 1991)
θ_B | data ~ Beta(5 + 130,  95 + 1870) = Beta(135, 1965)

Posterior means:
  Control:   109 / (109 + 1991) = 5.19%
  Treatment: 135 / (135 + 1965) = 6.43%
```

**Key quantities:**
```python
import numpy as np
from scipy import stats

alpha_A, beta_A = 109, 1991
alpha_B, beta_B = 135, 1965

N_samples = 200_000
samples_A = np.random.beta(alpha_A, beta_A, N_samples)
samples_B = np.random.beta(alpha_B, beta_B, N_samples)

# P(B > A)
prob_B_better = (samples_B > samples_A).mean()
print(f"P(B > A) = {prob_B_better:.3f}")  # ~0.963

# Expected relative lift
relative_lift = ((samples_B - samples_A) / samples_A).mean()
print(f"Expected relative lift = {relative_lift:.1%}")  # ~24%

# Expected Loss if we choose A (i.e., miss out on B's gain)
loss_choosing_A = np.maximum(samples_B - samples_A, 0).mean()
print(f"Expected loss (choose A) = {loss_choosing_A:.4f}")  # ~0.0124

# Expected Loss if we choose B
loss_choosing_B = np.maximum(samples_A - samples_B, 0).mean()
print(f"Expected loss (choose B) = {loss_choosing_B:.6f}")  # ~0.000047
```

---

## Decision Framework: Expected Loss

**P(B > A) alone is insufficient for stopping.** At 50.1% it's technically "more likely B is better" but you should not ship. The right stopping criterion is **Expected Loss (EL)**.

```
EL(choose A) = E[max(θ_B - θ_A, 0)]   # expected gain foregone by picking A
EL(choose B) = E[max(θ_A - θ_B, 0)]   # expected gain foregone by picking B
```

### Stopping Rule

Define a **loss threshold ε** in absolute percentage points:

| Decision context | ε |
|-----------------|---|
| Low-stakes UI tweak | 0.001 (0.1 pp) |
| Revenue-impacting feature | 0.0002 (0.02 pp) |
| Pricing / major UX change | 0.00005 (0.005 pp) |

**Stop and choose B when**: `EL(choose B) < ε`

**Stop and keep A when**: `EL(choose A) < ε`

**Continue collecting data** otherwise.

For the worked example above:
- `EL(choose B) = 0.000047` → if ε = 0.0002, this crosses the threshold → **ship B**
- `EL(choose A) = 0.0124` → would need to run much longer before keeping A

This is why Expected Loss is superior to P(B > A): it weighs the *magnitude* of what you'd miss, not just the direction.

---

## Closed-Form P(B > A) for Beta Distributions

Monte Carlo works, but for production systems or dashboards, use the closed-form formula:

```
P(θ_B > θ_A) = Σ_{i=0}^{α_B - 1}  B(α_A + i, β_A + β_B) / [(β_B + i) × B(1 + i, β_B) × B(α_A, β_A)]
```

Where `B(·,·)` is the Beta function. This sum has `α_B` terms; for large α, Monte Carlo is faster.

**Simpler approximation** (works well when both posteriors are reasonably peaked):

```python
from scipy.stats import norm

# Approximate using normal approximation of Beta posteriors
mean_A = alpha_A / (alpha_A + beta_A)
mean_B = alpha_B / (alpha_B + beta_B)
var_A  = (alpha_A * beta_A) / ((alpha_A + beta_A)**2 * (alpha_A + beta_A + 1))
var_B  = (alpha_B * beta_B) / ((alpha_B + beta_B)**2 * (alpha_B + beta_B + 1))

z = (mean_B - mean_A) / np.sqrt(var_A + var_B)
prob_B_better_approx = norm.cdf(z)
```

This approximation is accurate when `α, β > 30`. Below that, use sampling.

---

## Credible Intervals vs. Confidence Intervals

A **95% Bayesian credible interval** means: *given the data and prior, there is a 95% probability that θ lies within this interval.*

A frequentist 95% CI does NOT mean this — it means: *in repeated experiments, 95% of such intervals would contain the true θ.*

**How to compute:**
```python
# 95% highest-density interval (HDI) for treatment rate
lower = stats.beta.ppf(0.025, alpha_B, beta_B)
upper = stats.beta.ppf(0.975, alpha_B, beta_B)
print(f"95% credible interval for θ_B: [{lower:.4f}, {upper:.4f}]")
# e.g., [0.0540, 0.0753]
```

**Credible interval for the lift:**
```python
lift_samples = (samples_B - samples_A) / samples_A
ci_lower, ci_upper = np.percentile(lift_samples, [2.5, 97.5])
print(f"95% CI for relative lift: [{ci_lower:.1%}, {ci_upper:.1%}]")
```

---

## When to Use Bayesian vs. Frequentist

| Situation | Prefer |
|-----------|--------|
| Regulatory/compliance reporting required | Frequentist (fixed-horizon) |
| Want to stop early when result is clear | Bayesian (Expected Loss) or Sequential frequentist |
| Need probability statements for stakeholders | Bayesian |
| No reliable prior available | Frequentist (avoids prior sensitivity debate) |
| Multi-armed bandits / continuous deployment | Bayesian (natural extension) |
| Small sample sizes (<500 per group) | Bayesian with informative prior |

**The IRON LAW still applies**: even with Bayesian methods, calculate a minimum viable sample size before starting. Use it as a floor, not a ceiling. Bayesian testing does not eliminate the need for planning — it just gives you a principled early-stopping mechanism.

---

## Common Bayesian Anti-Patterns

**1. Stopping at P(B > A) = 95% without checking Expected Loss**

A test can reach 95% confidence with tiny absolute differences (e.g., 5.001% vs 5.000%). Expected Loss quantifies whether the decision actually matters.

**2. Using a flat prior to seem "objective"**

The Uniform(1,1) prior is not neutral — it says 50% conversion is as plausible as 5%. Use a weakly informative prior anchored to your actual baseline.

**3. Ignoring prior sensitivity**

Report results under two priors: your chosen prior AND a flatter one. If the decision flips, you need more data. If it doesn't, prior choice doesn't matter much.

**4. Treating P(B > A) as fixed-horizon p-value**

Unlike p-values, P(B > A) does not have a fixed false-positive rate at any threshold. You cannot compare "Bayesian p=0.05" to "frequentist p=0.05."

**5. Forgetting to check guardrail metrics**

Bayesian analysis gives you P(θ_B > θ_A) for the primary metric. Run the same analysis on guardrail metrics. Ship only if primary metric wins AND guardrail metrics show `P(guardrail_B < guardrail_A) < 5%`.

---

## Posterior Distribution Summary Template

```markdown
## Bayesian Analysis

**Model**: Beta-Binomial with prior Beta({α₀}, {β₀})

| Variant | Visitors | Conversions | Posterior Mean | 95% CI |
|---------|----------|-------------|----------------|--------|
| Control (A) | {n_A} | {k_A} | {mean_A:.2%} | [{lower_A:.2%}, {upper_A:.2%}] |
| Treatment (B) | {n_B} | {k_B} | {mean_B:.2%} | [{lower_B:.2%}, {upper_B:.2%}] |

**P(B > A)**: {prob_B_better:.1%}

**Expected relative lift**: {rel_lift:.1%} (95% CI: [{lift_lower:.1%}, {lift_upper:.1%}])

**Expected Loss**:
- If we ship B: {el_B:.5f}
- If we keep A: {el_A:.5f}
- Loss threshold (ε): {epsilon}

**Decision**: {Ship B / Keep A / Collect more data}
```
