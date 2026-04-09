# Position Debiasing in E-Commerce Ranking Training Data

## The Problem: What Position Bias Is

When you train a ranking model on click logs, you observe:

```
query: "wireless earbuds"
position 1 → clicked  (rank 1 product)
position 2 → skipped
position 3 → clicked  (rank 3 product)
```

Naively, this looks like "users preferred products at positions 1 and 3." But the product at position 1 was examined by nearly every user; the product at position 5 was examined by far fewer. A click on position 5 is stronger evidence of preference than a click on position 1 — but raw click counts don't reflect this.

**The core equation:**

```
P(click | item, position) = P(examined | position) × P(relevant | item)
```

If you ignore `P(examined | position)` and train on raw clicks, your model learns a mixture of relevance signal and position artifact. Items that rank high in your current system get more clicks, get higher training signal, and will rank higher in your next model — a feedback loop that entrenches incumbent rankings.

---

## Method 1: Inverse Propensity Scoring (IPS)

### Concept

Assign each click a weight that is the inverse of the probability it was examined:

```
w(q, d, k) = 1 / P(examined | position=k)
```

Where:
- `q` = query
- `d` = document/product
- `k` = position at which `d` was shown for query `q`

A click at position 10 (low examination probability) gets a high weight. A click at position 1 (high examination probability) gets a weight close to 1. This corrects for the examination bias.

### Propensity Estimation: Two Options

**Option A — Position-Only Propensity (simplest)**

Assume examination probability depends only on rank position, not on the query or item:

```
P(examined | k) = θ_k
```

Estimate `θ_k` via a **randomization experiment**: for a random 1–5% of queries, shuffle results randomly. In the shuffled results, clicks are position-artifact-free, so the click rate at each position directly estimates `θ_k`.

Worked estimation:
```
position 1: shown 10,000 times (random), clicked 2,100 → θ₁ = 0.21  → weight = 4.76
position 2: shown 10,000 times (random), clicked 1,850 → θ₂ = 0.185 → weight = 5.41
position 3: shown 10,000 times (random), clicked 1,560 → θ₃ = 0.156 → weight = 6.41
position 5: shown 10,000 times (random), clicked 900  → θ₅ = 0.09  → weight = 11.11
position 10: shown 10,000 times (random), clicked 340 → θ₁₀ = 0.034 → weight = 29.41
```

**Option B — Result Interleaving / Swap Experiments**

Without running random shuffles, you can use interleaving experiments (typically used for A/B testing two rankers) to infer relative examination probabilities. This is more complex and usually not needed unless running a randomization experiment is infeasible.

---

## Method 1 Step-by-Step Procedure

### Step 1: Run a Randomization Experiment

For a small traffic slice (start with 1%):

```python
def should_randomize(request_id: str, rate: float = 0.01) -> bool:
    # Deterministic: same request always gets same treatment
    return (hash(request_id) % 10000) < int(rate * 10000)

def rank_products(query, products, request_id):
    if should_randomize(request_id):
        random.shuffle(products)   # log impression_type="random"
        return products
    else:
        return your_current_ranker(query, products)  # log impression_type="production"
```

Key logging requirements:
- `impression_type`: `"random"` or `"production"`
- `position`: 1-indexed position shown
- `product_id`
- `clicked`: boolean
- `query_id`

Run for **minimum 30 days** to smooth over day-of-week effects. At 1% traffic, you need ~100k random impressions per position to get reliable propensity estimates.

### Step 2: Compute Propensity Scores

```python
import pandas as pd

random_logs = clicks_df[clicks_df['impression_type'] == 'random']

propensity = (
    random_logs
    .groupby('position')
    .agg(impressions=('clicked', 'count'), clicks=('clicked', 'sum'))
    .assign(theta=lambda df: df['clicks'] / df['impressions'])
)

# Smooth with isotonic regression (examination prob must be monotone decreasing)
from sklearn.isotonic import IsotonicRegression
ir = IsotonicRegression(increasing=False)
propensity['theta_smooth'] = ir.fit_transform(
    propensity.index.values,
    propensity['theta'].values
)
```

The isotonic constraint enforces the physical reality that deeper positions are examined less often.

### Step 3: Build Weighted Training Data

```python
production_logs = clicks_df[clicks_df['impression_type'] == 'production'].copy()

# Merge propensity
production_logs = production_logs.merge(
    propensity[['theta_smooth']],
    left_on='position',
    right_index=True,
    how='left'
)

# IPS weight — only for clicked items (unclicked items get weight 0 under point-click assumption)
production_logs['ips_weight'] = production_logs.apply(
    lambda r: 1.0 / r['theta_smooth'] if r['clicked'] else 0.0,
    axis=1
)

# Cap weights to limit variance (common: cap at 10× median weight)
median_w = production_logs[production_logs['ips_weight'] > 0]['ips_weight'].median()
production_logs['ips_weight_capped'] = production_logs['ips_weight'].clip(upper=10 * median_w)
```

### Step 4: Feed Weights into LambdaMART

LambdaMART (XGBoost or LightGBM implementation) accepts per-sample weights via `sample_weight`:

```python
import lightgbm as lgb

train_data = lgb.Dataset(
    X_train,
    label=y_train,          # relevance grade (e.g., 2=bought, 1=clicked, 0=skipped)
    group=query_groups,     # number of items per query
    weight=ips_weights_capped
)

params = {
    'objective': 'lambdarank',
    'metric': 'ndcg',
    'ndcg_eval_at': [5, 10],
    'learning_rate': 0.05,
    'num_leaves': 63,
}

model = lgb.train(params, train_data, num_boost_round=500)
```

---

## Method 2: Intervention Harvesting (No Randomization)

If you cannot run a randomization experiment (policy constraints, low traffic), you can exploit **natural variation** in your existing ranker.

Your ranker doesn't always place the same product at the same position for the same query — slight variations occur due to:
- Inventory changes
- Feature value updates (price changes, new reviews)
- A/B tests running in production

Find pairs where the **same product appeared at two different positions** for the **same or very similar query**:

```python
# Find product × query pairs that appeared at multiple positions
position_pairs = (
    clicks_df
    .groupby(['query_normalized', 'product_id'])
    .agg(positions=('position', list), clicks=('clicked', list))
    .query('positions.apply(len) >= 2')  # appeared at 2+ positions
)
```

For each such pair, the click rate ratio estimates relative propensity:

```
θ_k1 / θ_k2 ≈ click_rate(position=k1) / click_rate(position=k2)
```

Normalize so `θ₁ = 1.0` (position 1 is your reference). This gives relative propensities that can be used as IPS weights.

**Limitation:** Intervention harvesting is noisier than controlled randomization. The product-query pairs that appear at multiple positions are a biased sample (they tend to be marginal items). Use this only as a fallback.

---

## Method 3: Dual Learning (No Weight, No Propensity Model)

Rather than reweighting clicks, you can model position bias explicitly as a latent variable. The **Dual Learning Algorithm (DLA)** alternates between:

1. Estimating examination propensity given current relevance model
2. Updating relevance model given current propensity estimates

This is implemented in the [TF-Ranking](https://github.com/tensorflow/ranking) library as `DualLearningAlgorithm`. It requires no randomization experiment, but converges slower and is harder to debug than IPS.

**When to use DLA vs IPS:**

| Condition | Prefer |
|-----------|--------|
| Can run randomization experiment | IPS |
| Cannot randomize traffic | DLA or Intervention Harvesting |
| High traffic (>1M queries/day) | Either works |
| Low traffic (<100k queries/day) | IPS with very long experiment (60–90 days) |
| Fast iteration cycle needed | IPS (simpler to debug) |
| Complex multi-position display (carousels, grids) | DLA (position model is more flexible) |

---

## Worked Numerical Example

Scenario: You have two products for query "headphones":

- Product A: shown at position 1, clicked 800/1000 times
- Product B: shown at position 5, clicked 200/1000 times

**Without debiasing:**
- Raw CTR_A = 0.80
- Raw CTR_B = 0.20
- Model learns: A is 4× more relevant than B

**With IPS (using propensities from the table above):**
- Debiased CTR_A = 0.80 / 0.21 = 3.81
- Debiased CTR_B = 0.20 / 0.09 = 2.22
- Ratio = 3.81 / 2.22 = 1.72

After debiasing, A is only 1.72× more relevant than B — a much smaller gap. The model will be less aggressive about permanently burying B just because it was historically shown in an unfavorable position.

---

## Practical Caveats

**Weight variance explosion**: IPS weights at deep positions can be 30–50×. Uncapped, these produce a highly variable loss that destabilizes training. Always cap at 5–20× the median weight. The optimal cap is a hyperparameter to tune offline by measuring NDCG on a held-out set under different caps.

**Position vs. examination**: This reference assumes the "position-based model" (PBM): whether a user examines an item depends only on its position. In reality, examination also depends on:
- The attractiveness of surrounding items (cascade model)
- Whether the user found a satisfying result earlier (dynamic stopping)

The PBM is a simplification that works well in practice for standard list displays. For carousel, grid, or mixed-media layouts, you need a more complex examination model.

**Cold start for new positions**: If your UI adds a new position (e.g., a 6th visible slot becomes a 7th), you have no propensity estimate for position 7. Extrapolate using a power-law fit:

```python
import numpy as np
from scipy.optimize import curve_fit

def power_law(k, a, b):
    return a * np.power(k, -b)

popt, _ = curve_fit(power_law, propensity.index.values, propensity['theta_smooth'].values)
theta_new_position = power_law(7, *popt)
```

**Stale propensities**: Propensity scores should be recomputed every 30–90 days. UI changes (adding images, changing font size, introducing badges) alter how users scan results, shifting examination probabilities. Treat propensity estimation as a recurring pipeline step, not a one-time calibration.

**Do not debias sponsored slots**: Paid placement operates under a different examination model (users have different intent when looking at ads). Keep organic and sponsored training data separate; do not apply organic propensity weights to sponsored click logs.
