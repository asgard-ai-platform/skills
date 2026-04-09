# Response Curves for Ad Budget Allocation

A response curve maps spend → conversions (or revenue) for a single campaign. The shape of this curve determines where marginal returns are high or low, which drives the allocation decision.

---

## The Three Models

### 1. Log Curve

```
conversions(x) = a * ln(x) + b
```

- `a` controls steepness; larger `a` = faster early gains, faster saturation
- `b` shifts the curve vertically (baseline at low spend)
- Marginal return: `a / x`

**When it fits:** Mature campaigns with stable audiences. Reaches about 63% of theoretical max by the time spend equals `e * x_min`. Fastest to fit — only 2 parameters.

### 2. Power Curve

```
conversions(x) = a * x^β
```

- `β < 1` produces diminishing returns (typical range 0.4–0.8)
- `β = 1` is linear (no diminishing returns — should not happen in practice)
- Marginal return: `a * β * x^(β-1)`

**When it fits:** Campaigns where spend scales with impression volume (programmatic, YouTube). Linearizes under log-log transformation, so fitting via OLS is straightforward.

### 3. S-Curve (Logistic)

```
conversions(x) = L / (1 + exp(-k * (x - x0)))
```

- `L` = saturation ceiling (max conversions achievable)
- `k` = steepness of the inflection point
- `x0` = spend at inflection (where marginal returns peak)
- Marginal return: `L * k * exp(-k*(x-x0)) / (1 + exp(-k*(x-x0)))^2`

**When it fits:** Campaigns that need minimum spend to "turn on" — branded search before hitting brand awareness threshold, influencer campaigns that need reach before conversion rates improve. Requires at least 5–6 data points to fit reliably; 3 parameters.

---

## Fitting Procedure

### Data Requirements

You need at least 3 (spend, conversions) observations per campaign, ideally at different spend levels. The observations can come from:

- Week-over-week spend variation (most common)
- A/B budget tests (highest quality)
- Geo holdout experiments

Do not use data points where spend or conversions are zero — log models break and power models produce undefined marginals.

### Step 1: Check For Diminishing Returns

Plot conversions vs. spend. Compute the simple ratio `conversions / spend` at each observed level. If this ratio decreases as spend increases, diminishing returns are present and the model applies.

| Pattern | Likely model |
|---------|-------------|
| Ratio decreases smoothly from the start | Log or power |
| Ratio stays flat then drops sharply | S-curve |
| Ratio is flat throughout | Linear — check if audience is undersaturated or tracking is broken |
| Ratio increases (scale effects) | Do not use diminishing-returns framework; flag for review |

### Step 2: Fit the Candidate Model

**Log curve — OLS after log transform:**

```python
import math

# data: list of (spend, conversions)
def fit_log(data):
    n = len(data)
    log_x = [math.log(x) for x, _ in data]
    y = [conv for _, conv in data]
    
    mean_lx = sum(log_x) / n
    mean_y  = sum(y) / n
    
    a = sum((lx - mean_lx) * (yi - mean_y) for lx, yi in zip(log_x, y)) \
      / sum((lx - mean_lx)**2 for lx in log_x)
    b = mean_y - a * mean_lx
    return a, b

def log_curve(x, a, b):
    return a * math.log(x) + b

def log_marginal(x, a):
    return a / x
```

**Power curve — OLS after log-log transform:**

```python
def fit_power(data):
    n = len(data)
    log_x = [math.log(x) for x, _ in data]
    log_y = [math.log(conv) for _, conv in data]
    
    mean_lx = sum(log_x) / n
    mean_ly = sum(log_y) / n
    
    beta = sum((lx - mean_lx) * (ly - mean_ly) for lx, ly in zip(log_x, log_y)) \
         / sum((lx - mean_lx)**2 for lx in log_x)
    log_a = mean_ly - beta * mean_lx
    a = math.exp(log_a)
    return a, beta

def power_curve(x, a, beta):
    return a * (x ** beta)

def power_marginal(x, a, beta):
    return a * beta * (x ** (beta - 1))
```

**S-curve — scipy-free iterative fit (Newton's method on MSE gradient):**

Fitting an S-curve without scipy requires non-linear least squares. If you're in a pure-stdlib environment, use the following grid search over `k` and `x0` with `L` fixed at the observed max:

```python
def fit_scurve(data, L=None):
    if L is None:
        L = max(conv for _, conv in data) * 1.2  # allow 20% headroom
    
    best = (float('inf'), 1e-5, 0)
    # coarse grid; refine if needed
    x_vals = [x for x, _ in data]
    x0_candidates = [sum(x_vals)/len(x_vals) * f for f in [0.5, 0.75, 1.0, 1.25, 1.5]]
    k_candidates = [1e-4, 5e-4, 1e-3, 5e-3, 1e-2]
    
    for k in k_candidates:
        for x0 in x0_candidates:
            mse = sum(
                (L / (1 + math.exp(-k * (x - x0))) - conv)**2
                for x, conv in data
            ) / len(data)
            if mse < best[0]:
                best = (mse, k, x0)
    
    _, k, x0 = best
    return L, k, x0

def scurve(x, L, k, x0):
    return L / (1 + math.exp(-k * (x - x0)))

def scurve_marginal(x, L, k, x0):
    e = math.exp(-k * (x - x0))
    return L * k * e / (1 + e)**2
```

### Step 3: Select Model by R²

```python
def r_squared(data, curve_fn):
    y = [conv for _, conv in data]
    y_hat = [curve_fn(x) for x, _ in data]
    mean_y = sum(y) / len(y)
    ss_res = sum((yi - yhi)**2 for yi, yhi in zip(y, y_hat))
    ss_tot = sum((yi - mean_y)**2 for yi in y)
    return 1 - ss_res / ss_tot if ss_tot > 0 else 0
```

Choose the model with highest R². If R² < 0.80 for all candidates, flag the campaign for manual review — the data may be insufficient or the campaign has a non-smooth response (step function, see Gotchas in SKILL.md).

---

## Worked Example

**Campaign: Search-Brand**

Observed data:

| Week | Spend ($) | Conversions |
|------|-----------|-------------|
| 1    | 20,000    | 68          |
| 2    | 35,000    | 97          |
| 3    | 50,000    | 118         |
| 4    | 65,000    | 131         |
| 5    | 80,000    | 141         |

**Fit log curve:**

ln(20000)=9.903, ln(35000)=10.463, ln(50000)=10.820, ln(65000)=11.082, ln(80000)=11.290

mean_ln_x = 10.712, mean_y = 111.0

Numerator: Σ(ln_x - mean)(y - mean)
= (9.903-10.712)(68-111) + (10.463-10.712)(97-111) + (10.820-10.712)(118-111) + (11.082-10.712)(131-111) + (11.290-10.712)(141-111)
= (-0.809)(-43) + (-0.249)(-14) + (0.108)(7) + (0.370)(20) + (0.578)(30)
= 34.79 + 3.49 + 0.76 + 7.40 + 17.34 = 63.78

Denominator: Σ(ln_x - mean)²
= 0.654 + 0.062 + 0.012 + 0.137 + 0.334 = 1.199

**a = 63.78 / 1.199 = 53.2**
**b = 111.0 - 53.2 * 10.712 = 111.0 - 569.9 = -458.9**

Fitted curve: `conversions = 53.2 * ln(spend) - 458.9`

**Marginal return at $50,000:** `53.2 / 50,000 = 0.00106 conversions per dollar`
**Marginal return at $80,000:** `53.2 / 80,000 = 0.000665 conversions per dollar`

This means the 80,001st dollar buys 0.000665 conversions (≈ $1,504 marginal CPA at $80K spend vs. $943 at $50K spend). If another campaign has a marginal CPA lower than $1,504 at its current budget, shift dollars there.

---

## Extrapolation Bounds

Never evaluate the marginal return at spend levels more than **20% beyond the highest observed spend** in the training data. The log curve predicts infinite conversions as spend → ∞, which is physically impossible. The power curve has the same problem. The S-curve self-corrects (it has a ceiling) but you still need data near the inflection point to trust the fit.

Practical rule: tag each campaign with `max_trusted_spend = max_observed_spend * 1.20`. The allocator must not assign more than this amount to the campaign. Anything above the cap gets redistributed to campaigns with available headroom.

```python
def allocation_cap(data, margin=1.20):
    return max(x for x, _ in data) * margin
```

---

## Model Comparison Table

| Model | Parameters | Fitting method | Min data points | Suitable spend range | Marginal formula |
|-------|-----------|---------------|-----------------|---------------------|-----------------|
| Log | 2 (a, b) | OLS on ln(x) | 3 | Low to medium | a / x |
| Power | 2 (a, β) | OLS on ln-ln | 3 | Low to medium | a·β·x^(β-1) |
| S-curve | 3 (L, k, x0) | Grid or NLS | 5–6 | Full range including saturation | L·k·e^(-k(x-x0)) / (1+e^(-k(x-x0)))^2 |

---

## Common Failure Modes

**Negative `a` in log fit:** Your conversions decreased as spend increased in the data. This can happen if you're comparing different time periods with different market conditions. Do not use the model; collect cleaner data or use time-indexed controls.

**β > 1 in power fit:** Implies increasing returns to scale. Either the campaign is genuinely early-stage (not yet in your targeting ICP) or the data period includes a major creative refresh. Treat as a special case, cap spend at the highest observed level, and re-evaluate next cycle.

**S-curve L too low:** If `L` is set equal to the observed max (no headroom), the fitted curve flatlines prematurely and marginal returns drop to near-zero before the actual saturation point. Always allow at least 20% headroom when setting `L`.

**Single-period data:** If all observations come from a single 7-day window (e.g., budget was varied within one week), the response curve conflates day-of-week effects with spend effects. Require at least 3 distinct weeks of data before fitting.
