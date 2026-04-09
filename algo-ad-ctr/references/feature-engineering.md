# Feature Engineering for CTR Prediction

## Feature Taxonomy

CTR features fall into five groups. Each group has different staleness characteristics and leakage risks.

| Group | Examples | Update Frequency | Leakage Risk |
|-------|----------|-----------------|--------------|
| User | demographics, device, location | Slow (days) | Low |
| Ad | category, creative type, landing page | Medium (hours) | Low |
| Query | keywords, intent category, length | Per-request | Low |
| Interaction | query-ad match score, semantic similarity | Per-request | Low |
| Historical CTR | ad CTR, query-ad CTR, user CTR | Fast (minutes) | **HIGH** |

Historical CTR features are the most predictive and the most dangerous. See the [Historical CTR Features](#historical-ctr-features) section.

---

## User Features

### Demographics
Binary or one-hot encoded. Avoid high cardinality (use top-N + `other` bucket).

```
age_bucket: [18-24, 25-34, 35-44, 45-54, 55+]
gender: [M, F, unknown]
income_bucket: [low, mid, high, unknown]
```

### Device
Strong signal: mobile users click differently from desktop users. Use three-way split:

```
device_type: [mobile, tablet, desktop]
```

Do NOT use device model — too high cardinality with no marginal gain over device_type.

### Recency
How recently the user was active. Bucket into log bins:

```
hours_since_last_session: log2 bins → [<1h, 1-2h, 2-4h, 4-8h, 8-24h, >24h]
```

### User Interest Embedding
If you have a user interest vector from browsing history, reduce to 8-16 dimensions via PCA or learned embedding before feeding into GBDT. Raw 128-dim embeddings cause overfitting in tree models.

---

## Ad Features

### Category Hierarchy
Use both leaf and parent category:

```
ad_category_leaf:   "Running Shoes"         → one-hot
ad_category_parent: "Sports & Outdoors"     → one-hot
```

Leaf alone is too sparse; parent alone loses specificity. Both gives the model fallback.

### Creative Type
```
creative_type: [text, image, video, carousel]
```

Video ads have position-independent CTR uplift of ~1.3-1.8× in most studies, but much higher view-through-without-click. Flag for calibration.

### Ad Age
Fresh ads lack historical signal. Use a freshness flag:

```python
ad_age_hours = (now - ad_created_at).total_seconds() / 3600
is_new_ad = int(ad_age_hours < 48)
```

Pair with cold-start fallback in historical CTR features (see below).

---

## Query Features

### Query Length
Short queries (1-2 tokens) are navigational; longer queries (4+) are transactional. Both extremes click differently.

```python
query_token_count = len(query.split())
query_length_bucket = (
    "short" if query_token_count <= 2 else
    "medium" if query_token_count <= 5 else
    "long"
)
```

### Query Intent Category
Classify query into intent: `informational`, `navigational`, `transactional`, `commercial_investigation`. Commercial investigation queries have the highest CTR on ads. Use a small classifier or regex rules for the top-volume query heads; bin long tail to `unknown`.

### Query Frequency
How often this exact query fires per day. Rare queries have high uncertainty; frequent queries have stable CTR patterns.

```python
query_frequency_bucket = (
    "head"  if daily_count > 10000 else
    "torso" if daily_count > 100 else
    "tail"
)
```

---

## Query-Ad Interaction Features

These capture *relevance* — the match between user intent and ad content.

### Keyword Overlap (BM25 Score)
Sparse but cheap. Compute BM25 between query tokens and ad title + body:

```
bm25_score = Σ_t IDF(t) × (tf × (k1+1)) / (tf + k1 × (1 - b + b × |d|/avgdl))
```

Typical parameters: k1=1.5, b=0.75. Bucket into 5 bins [0, low, mid, high, exact_match].

### Semantic Similarity
Cosine similarity between query embedding and ad embedding. Use the same embedding model for both. Bucket into 4 bins (quartiles over the training distribution):

```
semantic_sim_bucket: [q1, q2, q3, q4]
```

Do NOT use raw float similarity in GBDT — bucketing generalizes better and reduces sensitivity to embedding model changes.

### Exact Match Flag
Binary: does the query exactly contain the ad's primary keyword?

```python
is_exact_match = int(primary_keyword.lower() in query.lower())
```

High-precision signal; deserves its own feature separate from BM25.

---

## Historical CTR Features

**This is where 60-70% of CTR model predictive power comes from. It is also where leakage lives.**

### The Leakage Problem

Wrong approach:
```python
# WRONG: computes CTR using all data including current impression
ad_ctr = ad_clicks_total / ad_impressions_total
```

This leaks future clicks into training. The feature value during serving (computed from past data only) differs from the feature value during training (computed from all data). Your model trains on a distribution that doesn't exist at inference time.

Correct approach: **time-based split only**. The historical CTR feature for impression at time `t` must use only clicks/impressions with timestamp `< t`.

```python
# CORRECT: only events strictly before current impression
ad_ctr = ad_clicks_before_t / ad_impressions_before_t
```

### Smoothed CTR (Laplace / Beta Prior Smoothing)

Raw CTR is noisy for low-volume ads. Smooth toward a prior mean:

```
smoothed_CTR = (clicks + α) / (impressions + α + β)
```

Where `α` and `β` parameterize a Beta prior. If your overall average CTR is 3%, set `α=3, β=97` (prior equivalent to 100 pseudo-impressions). A new ad with 0 clicks, 0 impressions gets CTR = 3/100 = 0.03 — the global average.

**Worked example:**

| Ad | Clicks | Impressions | Raw CTR | Smoothed CTR (α=3, β=97) |
|----|--------|-------------|---------|--------------------------|
| A  | 0      | 0           | undefined | 0.030 |
| B  | 1      | 10          | 0.100   | 0.036 |
| C  | 50     | 1000        | 0.050   | 0.049 |
| D  | 500    | 10000       | 0.050   | 0.050 |

Ad B has only 10 impressions; raw CTR of 10% is noisy. Smoothed CTR pulls it toward 3.6%, which is a more credible estimate.

### EWMA CTR (Recency-Weighted)

For fast-changing ads (news, flash sales), older data should decay:

```
ewma_ctr_t = λ × ctr_yesterday + (1 - λ) × ctr_today
```

Or equivalently, maintain a running EWMA over hourly windows:

```python
def update_ewma(prev_ewma, new_ctr, lambda_=0.9):
    return lambda_ * prev_ewma + (1 - lambda_) * new_ctr
```

`λ=0.9` gives ~10-period half-life; `λ=0.95` gives ~20-period half-life. Tune based on how quickly ad CTR changes in your system.

### Feature Granularities to Compute

Compute historical CTR at multiple granularities and include all as separate features:

| Feature | Granularity | Notes |
|---------|-------------|-------|
| `ad_ctr` | ad-level | Baseline; high volume |
| `ad_query_ctr` | ad × query | Most predictive; sparse |
| `ad_position_ctr` | ad × position | Captures position bias per ad |
| `user_ctr` | user-level | User's own click tendency |
| `category_ctr` | ad category | Fallback for new ads |
| `query_ctr` | query-level | CTR on any ad for this query |

Do NOT drop sparse features — smooth them and let the model decide their weight.

### Logarithmic Transformation

Historical CTR features are right-skewed with values in [0, 1]. For logistic regression, apply log-odds transform:

```python
import math

def ctr_to_log_odds(ctr, eps=1e-6):
    ctr = max(eps, min(1 - eps, ctr))
    return math.log(ctr / (1 - ctr))
```

For GBDT, this transformation is usually unnecessary — trees split on thresholds and are invariant to monotonic transforms. But log-odds is valuable if you're mixing CTR features into a linear component.

---

## Cross Features

Cross features capture interactions that linear models miss.

### Explicit Crosses for Logistic Regression

Logistic regression cannot learn `device_type × ad_category` interaction automatically. Construct it explicitly:

```python
cross_feature = f"{device_type}_{ad_category_parent}"
# e.g., "mobile_Sports&Outdoors"
```

One-hot encode the cross. Prune crosses that have fewer than 1000 training examples to avoid noise.

### Decision Table: Which Crosses to Build

| Candidate Cross | Worth Building? | Reason |
|----------------|-----------------|--------|
| device × ad_category | Yes | Mobile CTR differs by category |
| query_intent × creative_type | Yes | Video underperforms on informational queries |
| user_age × ad_category | Sometimes | Use if your category is age-sensitive |
| position × query_length | No | Position bias already handled separately |
| user_gender × any | Carefully | Legal/fairness review required |

For GBDT, most crosses emerge naturally from tree splits. Explicit crosses add value only for logistic regression or shallow models.

---

## Position Bias and Why It's a Feature Problem

Position 1 gets ~2-3× more clicks than position 4 for the same ad, regardless of relevance. If you naively include `position` as a feature and train on logged clicks:

- The model learns that position 1 → high CTR
- At serving time, you use the model to *decide* which ad gets position 1
- Result: circular — model says position 1 has high CTR, puts ad there, confirms it

**Correct handling:**

1. Include position as a feature during training.
2. At inference, evaluate each ad at a *neutral position* (e.g., position 1, or all positions and take the average). Do not condition on the position you're assigning.
3. Alternatively, use position debiasing techniques (see `references/position-debiasing.md`).

The key rule: **position is a training feature, not an inference feature for ranking.**

---

## Missing Values

| Feature Type | Recommended Imputation |
|-------------|------------------------|
| Demographics (age, income) | Separate `unknown` bucket |
| Historical CTR | Smoothed prior (as above) |
| Query-ad match | 0 (no overlap is a real signal) |
| User recency | Maximum bucket ("cold user") |
| Embeddings | Zero vector (then flag with `has_embedding=0`) |

Do NOT impute with mean/median for CTR features — this conflates "no data" with "average performance", corrupting the cold-start fallback.

---

## Normalization

| Model Type | Normalization Needed? |
|------------|----------------------|
| Logistic Regression | Yes — standardize continuous features |
| GBDT (XGBoost, LightGBM) | No — trees are invariant to monotonic transforms |
| Neural net / deep model | Yes — layer-norm or batch-norm in embedding layers |

For logistic regression, standardize:
```python
x_normalized = (x - x_mean) / (x_std + 1e-8)
```

Compute `x_mean` and `x_std` on training data only. Apply the same statistics at serving time (save them with the model artifact).

---

## Feature Importance Sanity Checks

After training, verify the top features make business sense:

1. **query_ad_match** should rank in top 3. If it doesn't, check your match score computation.
2. **position** should have positive coefficient (higher position → more clicks). If it's negative, you have a data error.
3. **ad_ctr** (historical) should rank highly but not be #1. If it's #1 by a huge margin, check for leakage.
4. **user demographics** should rank below interaction features. Demographics alone are weak predictors; they matter more in cross features.

If historical CTR features dominate by 10× over all others, run a leakage audit: compare feature distributions between training time and serving time for the top-ranked impressions.
