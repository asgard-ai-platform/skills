# Position Debiasing for CTR Models

Position bias is the single largest confound in click data. Users click top-ranked ads more often because they are top-ranked, not because they are more relevant. A naive CTR model trained on raw clicks learns to predict "this ad was shown in position 1" rather than "this ad is relevant." This document covers how to detect, measure, and remove position bias.

---

## Why Position Bias Breaks CTR Models

Raw click logs conflate **relevance** and **examination probability**:

```
P(click | ad, position) = P(examine | position) × P(click | ad, examined)
                        = θ(position)            × r(ad)
```

Where:
- `θ(position)` — examination probability at position `k`, driven purely by position
- `r(ad)` — true relevance (what we actually want to model)

If you train on `P(click | ad, position)` and then rank ads without controlling for position, you are ranking on `θ × r` instead of `r`. Ads that happened to appear in position 1 in training data will be overestimated; ads always shown at the bottom will be underestimated.

### Empirical scale of the problem

A rough rule of thumb from industry measurements (Yahoo, Baidu, Google papers): position 2 receives roughly 50–70% of the clicks that position 1 receives, even when the underlying ad relevance is identical. By position 5, examination probability has typically dropped below 30% of position 1. These ratios vary by platform and query type, but the magnitude is large enough to dominate model signal.

---

## Method 1: Position as a Feature (Simplest, Most Common)

Include position as an input feature during training, then **drop it at inference time** (or fix it to a neutral value).

### Training

Add a one-hot or embedding for position to your feature vector:

```python
# Feature vector construction
features = {
    "query_ad_match": 0.8,
    "user_is_mobile": 1,
    "ad_category_ctr": 0.04,
    "position": 1,          # ← include during training
}
```

The model learns `θ(position)` implicitly as a coefficient.

### Inference

At serving time, set position to a **fixed neutral value** (commonly 0 or a sentinel representing "no position"):

```python
# At inference — rank by relevance, not position
features["position"] = 0   # or drop the feature entirely
pCTR = model.predict(features)
```

Because the model already learned that position 1 adds `+β_position` to logit, zeroing position removes that boost and returns a position-agnostic relevance score.

### Worked example with logistic regression

Suppose training yields these coefficients:

```
intercept:        -3.0
query_ad_match:    1.5
user_is_mobile:    0.3
position_1:        0.9   ← learned position bias
position_2:        0.5
position_3:        0.2
position_4:        0.0   (baseline)
```

Ad A shown in position 1, query_ad_match=0.9, mobile=1:
```
logit = -3.0 + 1.5(0.9) + 0.3(1) + 0.9(1) = -3.0 + 1.35 + 0.3 + 0.9 = -0.45
pCTR_raw = sigmoid(-0.45) = 0.390
```

At inference (position zeroed out):
```
logit = -3.0 + 1.35 + 0.3 = -1.35
pCTR_relevance = sigmoid(-1.35) = 0.206
```

Ad B shown in position 4, query_ad_match=0.95, mobile=1:
```
logit_raw = -3.0 + 1.425 + 0.3 + 0.0 = -1.275 → pCTR_raw = 0.219
logit_inference = -3.0 + 1.425 + 0.3 = -1.275 → pCTR_relevance = 0.219
```

Ranking by `pCTR_raw`: Ad A (0.390) > Ad B (0.219) → wrong, A is overranked due to position.  
Ranking by `pCTR_relevance`: Ad B (0.219) > Ad A (0.206) → correct, B has higher relevance.

### Limitations

- The model must have seen each position during training. If position 5+ is rare, estimates are noisy.
- Assumes position bias is **separable** from relevance. The true model is multiplicative (`θ × r`), but logistic regression learns an additive approximation in logit space. For most practical purposes this is acceptable.
- If position distribution shifts between train and serve (e.g., you add a 6th slot), the model has no signal for the new position.

---

## Method 2: Inverse Propensity Scoring (IPS)

IPS re-weights each training example to counteract the over-representation of high-position clicks.

### Setup

Estimate the **propensity score** `ê(k)` — the probability that an ad shown at position `k` would have been clicked in a randomized experiment (where position is assigned uniformly). Then weight each click by `1 / ê(k)`.

### IPS Loss

Standard log-loss:
```
L = -[y log(p) + (1-y) log(1-p)]
```

IPS-weighted log-loss:
```
L_IPS = -(y / ê(position)) × log(p)
```

Non-clicks are not re-weighted (the bias only affects positive examples — clicks).

### Estimating propensity scores

**Option A — From a randomization experiment (gold standard):**  
Run a small fraction of traffic (1–5%) with random position assignment. Count clicks per position. The ratio of click rates directly estimates `θ(k) / θ(1)`.

**Option B — EM estimation without randomization:**  
Jointly estimate relevance `r(ad)` and position bias `θ(k)` using the factored model:

```
P(click | ad, k) = θ(k) × r(ad)
```

Algorithm:
1. Initialize `θ(k) = 1` for all positions.
2. E-step: For each impression, estimate `r(ad) = P(click) / θ(k)`.
3. M-step: Update `θ(k) = mean(P(click) / r(ad))` across all impressions at position `k`.
4. Normalize so `θ(1) = 1`. Repeat until convergence.

This is the approach used in the **Unbiased LambdaMart** and **RandProp** lines of work.

**Option C — Heuristic approximation:**  
Use aggregated CTR at each position, averaged across all ads:

```python
position_ctr = df.groupby("position")["clicked"].mean()
propensity = position_ctr / position_ctr[1]   # normalize to position 1
```

This conflates position bias with selection effects (better ads are shown at top), so it overestimates the bias. Use only if randomization data is unavailable and as a rough starting point.

### Worked numbers for IPS weighting

Suppose estimated propensities (from randomization experiment):
```
θ(1) = 1.00
θ(2) = 0.68
θ(3) = 0.45
θ(4) = 0.28
```

Training examples and their IPS weights:

| Example | Position | Clicked | IPS Weight |
|---------|----------|---------|------------|
| A       | 1        | 1       | 1/1.00 = 1.00 |
| B       | 2        | 1       | 1/0.68 = 1.47 |
| C       | 3        | 1       | 1/0.45 = 2.22 |
| D       | 4        | 0       | 1.00 (not re-weighted) |

Example C (position 3, clicked) gets 2.22× the weight of example A (position 1, clicked), because it was harder to be seen at position 3 — so that click is stronger evidence of relevance.

### Clipping propensity weights

IPS weights can become very large for low-position clicks (e.g., position 8 might have `θ = 0.05`, giving weight = 20). This causes high variance. Standard practice: clip at a maximum weight `w_max`:

```python
w_max = 10.0  # tune based on your position depth
weight = min(1.0 / propensity[position], w_max)
```

The tradeoff: clipping re-introduces some bias but reduces variance. A value of 5–10 is common in practice.

---

## Method 3: Two-Tower Factored Model

Explicitly separate the position tower from the relevance tower in the model architecture.

```
Input → [User/Ad/Query features] → Relevance Tower → r(ad)
Input → [Position feature only]  → Bias Tower      → θ(position)

P(click) = sigmoid(r(ad) + θ(position))   # additive in logit space
```

At training time, both towers are jointly learned. At inference, only the relevance tower is used.

This is architecturally equivalent to "position as a feature" (Method 1) but makes the separation explicit and allows you to use different learning rates or regularization strengths for the bias tower.

```python
# PyTorch sketch
class FactoredCTR(nn.Module):
    def __init__(self, feature_dim, n_positions):
        super().__init__()
        self.relevance = nn.Linear(feature_dim, 1)
        self.position_bias = nn.Embedding(n_positions, 1)

    def forward(self, features, position, training=True):
        r = self.relevance(features)
        if training:
            theta = self.position_bias(position)
            return torch.sigmoid(r + theta)
        else:
            return torch.sigmoid(r)   # position-free at inference
```

---

## Choosing a Method

| Situation | Recommended method |
|-----------|-------------------|
| Limited engineering resources, logistic regression | Position as feature (Method 1) |
| GBDT model, can't easily add IPS to training loop | Position as feature (Method 1) |
| Neural ranking model, explicit control desired | Two-tower factored model (Method 3) |
| Have randomization experiment data | IPS (Method 2) with measured propensities |
| Need to correct for bias in offline evaluation | IPS (Method 2) for evaluation, either method for training |
| Deep result pages (positions 6+) | EM-estimated propensities + IPS clipping |

---

## Calibration Check After Debiasing

After applying position debiasing, verify the IRON LAW (calibration) still holds. Debiasing can shift predicted probabilities so that `pCTR` no longer matches raw click frequency — but it should match **position-adjusted** click frequency.

**Correct calibration target post-debiasing:**

For each prediction bucket `[p_low, p_high]`, the calibration error is measured against clicks re-weighted by IPS:

```
calibration_error(bucket) = |mean(pCTR in bucket) - sum(y/θ(k)) / count(bucket)|
```

Do **not** compare to raw click rate in each bucket — that will show artificial miscalibration because the predicted scores are now position-agnostic while raw click rates include position effects.

### Reliability diagram procedure

1. Score all held-out impressions using position-agnostic inference.
2. Bucket into 10 deciles by predicted pCTR.
3. For each bucket, compute IPS-adjusted observed CTR: `Σ(click / θ(position)) / N_bucket`
4. Plot predicted vs IPS-adjusted observed. Should be close to diagonal.

---

## Common Mistakes

**Mistake 1: Applying position debiasing at training but not at inference normalization**  
If you train with position as a feature but forget to zero it at serving, you pass real positions at inference. This ranks by `θ × r` again — no gain.

**Mistake 2: Using raw click rate per position as propensity without controlling for selection**  
High positions get better ads. `CTR(position=1)` overestimates `θ(1)` because top ads are more relevant, not just more visible. This makes IPS weights too small for position 1 examples.

**Mistake 3: Not clipping IPS weights**  
Positions beyond 6–8 may have propensity estimates near zero. Unclipped weights dominate the gradient and destabilize training.

**Mistake 4: Forgetting the position-debiased model requires recalibration**  
After removing position from inference, predicted scores shift. Run Platt scaling on the debiased scores before using them in `AdRank = Bid × pCTR`. The bid math assumes absolute probability, not just relative ranking.

**Mistake 5: Applying one global position bias curve across all query types**  
Navigational queries (where users click the first result automatically) have a steeper position curve than exploratory queries. If your platform handles both, consider estimating separate propensity curves per query class or intent bucket.
