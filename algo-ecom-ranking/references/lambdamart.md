# LambdaMART Implementation for E-Commerce Ranking

## What LambdaMART Is

LambdaMART = LambdaRank (gradient computation) + MART (gradient-boosted decision trees).

It is a **listwise** learning-to-rank algorithm. Rather than predicting a relevance score directly, it learns to order items by computing gradients that push relevant items up and irrelevant items down within the same query group. This makes it directly optimize ranking metrics like NDCG.

**Why LambdaMART instead of pointwise regression or pairwise SVM for e-commerce:**
- Pointwise regression (predict CTR independently) ignores inter-item ordering effects
- Pairwise SVM scales as O(n²) pairs per query; LambdaMART approximates this efficiently
- LambdaMART directly approximates NDCG gradient, which matches e-commerce evaluation metrics

## Core Math

### Lambda Gradient

For a query with documents i and j where i is ranked above j, the lambda weight is:

```
λ_ij = -σ / (1 + exp(σ(s_i - s_j))) × |ΔNDCG_ij|
```

Where:
- `σ` = sigmoid steepness (typically 1.0)
- `s_i`, `s_j` = current model scores for document i and j
- `|ΔNDCG_ij|` = absolute change in NDCG from swapping i and j

The gradient for document i accumulated across all pairs:

```
λ_i = Σ_{j: relevant > i} λ_ij - Σ_{j: i > relevant} λ_ij
```

The key insight: **ΔNDCG acts as a multiplicative weight**, giving larger updates to swaps at the top of the ranking (positions 1-10) than swaps deep in the list.

### NDCG and ΔNDCG

```
DCG@k = Σ_{i=1}^{k} (2^rel_i - 1) / log₂(i + 1)
NDCG@k = DCG@k / IDCG@k
```

For a swap of documents at positions i and j:

```
ΔNDCG = |DCG_after_swap - DCG_before_swap| / IDCG
       = |(2^rel_i - 1)(1/log₂(pos_j+1) - 1/log₂(pos_i+1))
          + (2^rel_j - 1)(1/log₂(pos_i+1) - 1/log₂(pos_j+1))| / IDCG
```

Concretely, swapping rank 1 and rank 2 produces a much larger ΔNDCG than swapping rank 50 and rank 51.

### MART: Gradient Boosted Trees

Each boosting iteration fits a regression tree to the lambdas:

```
F_m(x) = F_{m-1}(x) + η × h_m(x)
```

Where `h_m` is a tree trained to predict `λ_i` for each document. The leaves are then optimized with a Newton step:

```
leaf_value = Σ_{i ∈ leaf} λ_i / Σ_{i ∈ leaf} |λ_i|(1 - |λ_i|/N)
```

## Relevance Labels for E-Commerce

Unlike web search (editorial labels 0-4), e-commerce must derive labels from behavioral signals.

### Label Construction

| Signal | Label | Notes |
|--------|-------|-------|
| Purchase | 4 | Strongest positive signal |
| Add-to-cart (no purchase) | 3 | Strong intent signal |
| Click + long dwell (>30s) | 2 | Engaged click |
| Click + quick bounce | 1 | Weak signal, may be noise |
| Impression only (skipped) | 0 | Negative signal |

**Partial label scheme (recommended for sparse purchase data):**

If fewer than 5% of queries have purchase events, use a two-level scheme:
- Label 1 = clicked (not purchased)
- Label 2 = purchased

This prevents the model from seeing only 0s and 1s in training.

### Aggregation Window

Aggregate behavioral signals over a **sliding 30-day window**, weighted by recency:

```python
def compute_label(events, today):
    score = 0.0
    for event in events:
        days_ago = (today - event.date).days
        decay = 0.95 ** days_ago          # 5% daily decay
        if event.type == "purchase":
            score += 4 * decay
        elif event.type == "add_to_cart":
            score += 3 * decay
        elif event.type == "click":
            dwell = event.dwell_seconds
            score += (2 if dwell > 30 else 1) * decay
    # Discretize to 0-4
    if score == 0:
        return 0
    elif score < 1.0:
        return 1
    elif score < 2.5:
        return 2
    elif score < 5.0:
        return 3
    else:
        return 4
```

## Feature Set

### Feature Groups

**Text match features (computed per query-product pair):**
- `bm25_title`: BM25 score on product title
- `bm25_description`: BM25 score on full description
- `exact_match`: binary — query terms appear verbatim in title
- `query_coverage`: fraction of query tokens matched in title

**Behavioral features (aggregated, position-debiased):**
- `ctr_30d`: click-through rate over 30 days (debiased)
- `cvr_30d`: conversion rate (purchases / clicks)
- `add_to_cart_rate`: add-to-cart events / impressions
- `revenue_per_impression`: average revenue per impression

**Product quality features (static):**
- `avg_rating`: 1-5 star average
- `review_count_log`: log(1 + review_count) — log-scale avoids outlier dominance
- `recency_score`: 1 / (1 + days_since_listed / 30) — penalizes stale listings
- `image_quality_score`: if available from image QA pipeline

**Price features:**
- `price_percentile`: product price vs. category distribution (0-1)
- `price_competitiveness`: 1 - (price / median_category_price), clipped to [-1, 1]
- `has_promotion`: binary

**Inventory / availability:**
- `stock_score`: 1.0 if in-stock, 0.3 if low-stock, 0.0 if out-of-stock
- `shipping_days`: 0 = same-day, higher = slower

### Feature Normalization

LambdaMART (tree-based) is **invariant to monotone feature transforms**, so standardization is not required. However, clip extreme outliers to prevent trees from wasting splits on noise:

```python
CLIP_BOUNDS = {
    "bm25_title":       (0, 50),
    "review_count_log": (0, 10),
    "ctr_30d":          (0, 1),
    "cvr_30d":          (0, 1),
    "price_percentile": (0, 1),
}

def clip_features(row):
    for col, (lo, hi) in CLIP_BOUNDS.items():
        row[col] = max(lo, min(hi, row[col]))
    return row
```

## Training Data Format

LambdaMART expects data grouped by query. Standard format (libsvm/ranklib):

```
# label qid:N feat1:v1 feat2:v2 ...
4 qid:1 1:0.85 2:0.42 3:0.91 4:0.78 5:0.67
2 qid:1 1:0.30 2:0.88 3:0.45 4:0.23 5:0.55
0 qid:1 1:0.10 2:0.05 3:0.20 4:0.15 5:0.30
3 qid:2 1:0.72 2:0.61 3:0.83 4:0.90 5:0.44
```

Each row = one product-query pair. The model learns only within-query orderings; it never compares across queries.

**Minimum training set size:** ~10,000 unique queries with at least 2 distinct labels each. Fewer than this and LambdaMART will overfit to query-specific patterns.

## Training with XGBoost (Practical Code)

XGBoost supports LambdaMART via `objective="rank:ndcg"`.

```python
import xgboost as xgb
import numpy as np

def train_lambdamart(X_train, y_train, qid_train,
                     X_val, y_val, qid_val):
    """
    X_train: np.ndarray of shape (n_samples, n_features)
    y_train: np.ndarray of int labels 0-4
    qid_train: np.ndarray of query group IDs (must be sorted)
    """
    # Compute group sizes (XGBoost needs counts, not IDs)
    _, train_counts = np.unique(qid_train, return_counts=True)
    _, val_counts   = np.unique(qid_val,   return_counts=True)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtrain.set_group(train_counts)

    dval = xgb.DMatrix(X_val, label=y_val)
    dval.set_group(val_counts)

    params = {
        "objective":        "rank:ndcg",
        "eval_metric":      "ndcg@10",
        "eta":              0.05,          # learning rate
        "max_depth":        6,
        "min_child_weight": 50,            # prevent small-leaf overfitting
        "subsample":        0.8,
        "colsample_bytree": 0.8,
        "lambda":           1.0,           # L2 regularization
        "alpha":            0.1,           # L1 regularization
        "ndcg_exp_gain":    True,          # use 2^rel - 1 gain form
    }

    model = xgb.train(
        params,
        dtrain,
        num_boost_round=500,
        evals=[(dtrain, "train"), (dval, "val")],
        early_stopping_rounds=20,
        verbose_eval=50,
    )

    return model


def predict_and_rank(model, X_query, product_ids):
    """Score products for a single query, return ranked list."""
    dmatrix = xgb.DMatrix(X_query)
    scores  = model.predict(dmatrix)
    ranked  = sorted(zip(product_ids, scores),
                     key=lambda x: x[1], reverse=True)
    return ranked
```

### Hyperparameter Guidance

| Parameter | Recommended Start | Rationale |
|-----------|------------------|-----------|
| `eta` | 0.05 | Lower LR + more rounds = better generalization |
| `max_depth` | 5–7 | Deeper = more feature interactions captured |
| `min_child_weight` | 30–100 | Prevents overfitting to rare query-product pairs |
| `num_boost_round` | 300–1000 with early stopping | Let early stopping decide |
| `subsample` | 0.7–0.9 | Stochastic gradient boosting reduces variance |
| `colsample_bytree` | 0.6–0.9 | Feature bagging helps with correlated features |

## Blending LTR Score with Business Boost

As defined in SKILL.md:

```
final_score = α × LTR_score + (1-α) × business_boost
```

**LTR_score normalization**: LambdaMART outputs raw scores with no fixed range. Normalize per-query with min-max before blending:

```python
def normalize_ltr_scores(scores):
    lo, hi = scores.min(), scores.max()
    if hi == lo:
        return np.ones_like(scores) * 0.5
    return (scores - lo) / (hi - lo)
```

**business_boost construction:**

```python
def compute_business_boost(product):
    margin_score = min(product.gross_margin / 0.40, 1.0)  # cap at 40% margin
    stock_score  = product.stock_score                      # 0, 0.3, or 1.0
    promo_bonus  = 0.1 if product.has_promotion else 0.0
    return 0.5 * margin_score + 0.4 * stock_score + 0.1 * promo_bonus
```

**α tuning:**

| α value | Behavior | When to use |
|---------|----------|-------------|
| 0.9 | LTR-dominant | Sufficient click data (>6 months), trust the model |
| 0.7 | Balanced | Default starting point |
| 0.5 | Business-heavy | New model, not yet validated; or margin pressure |
| 0.3 | Override mode | Promotional campaigns, inventory clearance |

Start at α = 0.7 and tune via A/B test on revenue per search.

## Worked Example: Scoring Three Products

Query: "wireless earbuds". Three candidates after BM25 retrieval.

| Feature | Product A (AirPods Pro) | Product B (Unknown Brand) | Product C (Sony WF-1000XM5) |
|---------|------------------------|--------------------------|------------------------------|
| bm25_title | 0.82 | 0.91 | 0.76 |
| ctr_30d (debiased) | 0.18 | 0.04 | 0.14 |
| cvr_30d | 0.09 | 0.01 | 0.07 |
| avg_rating | 4.7 | 3.8 | 4.6 |
| review_count_log | 9.2 | 2.1 | 7.8 |
| stock_score | 1.0 | 1.0 | 0.3 |
| gross_margin | 0.35 | 0.48 | 0.28 |

After LambdaMART inference:
- LTR_score raw: A=2.31, B=0.47, C=1.98
- LTR_score normalized: A=1.00, B=0.00, C=0.82

Business boost:
- A: 0.5×(0.35/0.40) + 0.4×1.0 + 0.0 = 0.44 + 0.40 = 0.84
- B: 0.5×1.0 + 0.4×1.0 + 0.0 = 0.90
- C: 0.5×(0.28/0.40) + 0.4×0.3 + 0.0 = 0.35 + 0.12 = 0.47

Final score at α = 0.7:
- A: 0.7×1.00 + 0.3×0.84 = **0.952** → Rank 1
- C: 0.7×0.82 + 0.3×0.47 = **0.715** → Rank 2
- B: 0.7×0.00 + 0.3×0.90 = **0.270** → Rank 3

Observation: Product B had the highest BM25 and highest margin but ranked last because behavioral signals (CTR, CVR, rating, reviews) were poor — consistent with the IRON LAW that relevance alone is insufficient.

## Common Failure Modes

**Model learns position, not quality.** If training data is not position-debiased, the model learns "items at position 1 get clicked" rather than "good items get clicked." Symptom: NDCG is high offline but A/B test shows no CTR lift. Fix: use inverse propensity weighting (see `references/position-debiasing.md`).

**Feature leakage from labels.** If CTR is computed over the same period as label construction, the model sees circular signal. Fix: use a **hold-out label window** — features from week 1–4, labels from week 5–6.

**Query group contamination.** If training data is not strictly grouped by query (i.e., rows from query Q1 are intermixed with Q2), LambdaMART will produce garbage. XGBoost requires `set_group()` called with correctly ordered, non-shuffled query groups. Always sort by `qid` before splitting into features/labels/groups.

**Category imbalance.** If 80% of training queries are clothing and 5% are electronics, the model will be poorly calibrated for electronics. Either oversample underrepresented categories or train per-category models when traffic is sufficient.

**Score collapse at inference.** For new queries with no click history, all behavioral features are 0 or NaN. Impute with category median (not global median), otherwise the model degrades to near-random ordering.

```python
def impute_cold_start(row, category_medians):
    behavioral_cols = ["ctr_30d", "cvr_30d", "add_to_cart_rate",
                       "revenue_per_impression"]
    cat = row["category"]
    for col in behavioral_cols:
        if np.isnan(row[col]):
            row[col] = category_medians.get((cat, col), 0.0)
    return row
```

## Offline Evaluation Before A/B Test

Run evaluation on a **held-out query set** (not seen during training):

```python
from sklearn.metrics import ndcg_score

def evaluate_model(model, X_test, y_test, qid_test, k=10):
    dmatrix = xgb.DMatrix(X_test)
    scores  = model.predict(dmatrix)

    ndcg_scores = []
    for qid in np.unique(qid_test):
        mask = qid_test == qid
        if mask.sum() < 2:          # need at least 2 items to rank
            continue
        y_true = y_test[mask].reshape(1, -1)
        y_pred = scores[mask].reshape(1, -1)
        ndcg_scores.append(ndcg_score(y_true, y_pred, k=k))

    return {
        "ndcg_at_10_mean": np.mean(ndcg_scores),
        "ndcg_at_10_p50":  np.percentile(ndcg_scores, 50),
        "ndcg_at_10_p10":  np.percentile(ndcg_scores, 10),  # worst-case tail
        "n_queries":       len(ndcg_scores),
    }
```

**Deployment gate:** LambdaMART model must exceed BM25 baseline NDCG@10 by ≥ 5% on the held-out set before proceeding to A/B test. A smaller improvement is within noise and does not justify the added operational complexity of serving an LTR model.
