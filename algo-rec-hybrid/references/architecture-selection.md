# Architecture Selection Guide — Hybrid Recommendation Systems

Five hybrid architectures exist. Picking the wrong one creates complexity with no payoff. This guide gives a concrete decision procedure: assess your data/constraints, answer four questions, arrive at one architecture.

---

## The Four Decision Questions

Work through these in order. Stop when you reach a definitive answer.

### Q1: Is your primary problem cold start?

Cold start = item or user has fewer than **N_threshold** interactions.
Typical values: N_threshold = 5–20 depending on domain (e-commerce: 10, news: 3, SaaS: 20).

- **Yes, cold start is the dominant pain** → go to Q2
- **No, you have sufficient interaction data for most users and items** → go to Q3

### Q2: Do your two methods produce scores that can be compared on a common scale?

Common scale = both scores are calibrated probabilities, or both are normalized relevance scores from the same range. Raw CF dot-product and TF-IDF cosine similarity are NOT on a common scale without normalization.

- **Yes, or you can normalize both** → **Weighted Hybrid**
- **No, or normalization is unreliable** → **Switching Hybrid**

### Q3: Does one method produce high recall / low precision, and another produce low recall / high precision?

High recall / low precision = returns many plausible candidates but noisy.
Low recall / high precision = returns few items but very targeted.

- **Yes** → **Cascade Hybrid** (high-recall method as Stage 1 filter, high-precision method as Stage 2 ranker)
- **No** → go to Q4

### Q4: Can one method's latent representations improve another method's feature space?

This requires: (a) one method produces dense embeddings or latent factors, and (b) the second method is a supervised model that can consume numerical features.

- **Yes** → **Feature Augmentation**
- **No, or you want a general-purpose blender that adapts online** → **Meta-level (Stacking)**

---

## Decision Table

| Primary Problem | Score Compatibility | Precision/Recall Asymmetry | Architecture |
|---|---|---|---|
| Cold start | Scores compatible | — | Weighted |
| Cold start | Scores incompatible | — | Switching |
| Accuracy/diversity at scale | — | Yes (one high-recall, one high-precision) | Cascade |
| Accuracy/diversity at scale | — | No | Feature Augmentation or Meta-level |

---

## Architecture Specs

### Weighted Hybrid

**Formula:**

```
score(u, i) = α × CF_score(u, i) + β × CB_score(u, i)
```

where α + β = 1 (or relax to α + β ≤ 1 if you allow abstaining).

**Normalization prerequisite** — before weighting, map both score distributions to [0, 1] using min-max across candidates for a given user query:

```
CF_norm(u, i) = (CF_raw(u, i) - min_j CF_raw(u, j)) /
                (max_j CF_raw(u, j) - min_j CF_raw(u, j))
```

Apply the same formula for CB_norm. Without this step, the higher-variance method dominates regardless of α.

**Weight initialization:** Start with α = 0.6, β = 0.4 (slight CF bias in most interaction-heavy domains). Tune via grid search on validation NDCG@10 in steps of 0.1.

**Worked numbers:**

```
Item X, User U:
  CF_raw = 0.82 (dot product of latent factors)
  CB_raw = 0.64 (cosine similarity)
  
After min-max across 200 candidates for User U:
  CF_norm = 0.71
  CB_norm = 0.83

With α=0.6, β=0.4:
  score = 0.6 × 0.71 + 0.4 × 0.83 = 0.426 + 0.332 = 0.758
```

**Failure mode:** If CF_raw has wider variance than CB_raw, min-max normalization may still under-represent CB signal for niche items (outlier CF scores compress the majority). Inspect score distributions before committing to this architecture.

---

### Switching Hybrid

**Core logic:**

```python
def recommend(user, item_catalog, threshold=10):
    n_interactions = len(interaction_history[user])
    
    if n_interactions >= threshold:
        return cf_model.predict(user, item_catalog)
    else:
        # Fall back to content-based using user profile signals
        # (demographics, explicit preferences, browsing context)
        return cb_model.predict(user_profile[user], item_catalog)
```

**Switch condition options** (choose one per deployment):

| Condition | When to use |
|---|---|
| `n_interactions >= N` | Interaction count is your data proxy for CF quality |
| `cf_confidence >= τ` | CF model exposes a confidence estimate (e.g., BPR posterior) |
| `item_age_days <= D` | Switching on item side: new items use CB |
| `is_new_user` | Binary flag from registration date |

**Hysteresis:** Avoid oscillation at the boundary. Once a user crosses the threshold and CF is used, do NOT switch back to CB unless interactions drop (e.g., account dormancy). Use a 30-day rolling window.

**Why this beats weighted for cold start:** Weighted hybrid still requires CF_score to be meaningful. For a user with 1 interaction, CF returns near-random scores; adding 60% of random noise to CB degrades quality. Switching avoids contaminating CB with meaningless CF output.

---

### Cascade Hybrid

**Stage structure:**

```
Stage 1 (Retrieval): content-based or popularity-based
  → Input: full item catalog (100K–10M items)
  → Output: candidate set C (200–2,000 items)
  → Optimize for: recall (don't miss relevant items)

Stage 2 (Ranking): collaborative filtering or learned ranker
  → Input: candidate set C
  → Output: top-K final recommendations
  → Optimize for: precision, NDCG
```

**Why the order matters:** CF (especially matrix factorization) is expensive at full catalog scale. Cascade lets you run CF only over a pre-filtered set, cutting latency by 10–100×. Running them in reverse (CF filter → CB rank) wastes the high-recall advantage of content-based.

**Candidate set sizing heuristic:**

```
|C| = max(K × 20, 200)
```

For K=10, use at least 200 candidates. Smaller sets risk Stage 2 having no good options if Stage 1 is imperfect.

**Recall budget:** Monitor Stage 1 recall against ground truth. If relevant items appear in C less than 85% of the time, your cascade ceiling for NDCG is ~0.85 no matter how good Stage 2 is. Fix Stage 1 before tuning Stage 2.

**Concrete example — e-commerce:**

```
Stage 1 (Content-Based TF-IDF + category filter):
  Input: 500,000 products
  Filters: same top-2 categories as user's last 5 purchases
  Returns: 400 candidates

Stage 2 (Matrix Factorization BPR):
  Re-scores 400 candidates with user's latent vector
  Returns: top-10

Latency: Stage 1 = 8ms (pre-indexed), Stage 2 = 3ms → total 11ms
vs. MF over full catalog: ~200ms (unacceptable for real-time)
```

---

### Feature Augmentation

**Direction:** CF → Content-Based is most common.

**Mechanism:** Extract CF latent factors as additional features for a content-based supervised ranker.

```python
# Step 1: train CF model, extract user and item embeddings
cf_model.fit(interaction_matrix)
user_embedding = cf_model.user_factors[user_id]   # shape: (K,)
item_embedding = cf_model.item_factors[item_id]   # shape: (K,)

# Step 2: concatenate with content features
content_features = tfidf_vectorizer.transform(item_description)  # shape: (V,)
augmented_features = np.concatenate([
    content_features.toarray().flatten(),
    item_embedding,
    user_embedding,
    np.array([np.dot(user_embedding, item_embedding)])  # interaction term
])  # shape: (V + 2K + 1,)

# Step 3: train supervised ranker on augmented features
ranker = LightGBM(objective='lambdarank')
ranker.fit(X_augmented_train, y_relevance_train)
```

**Leakage warning (reinforcing SKILL.md Iron Law):** When building `X_augmented_train`, the CF embeddings must be trained **only on the training split** of interactions. If you train CF on all interactions including test-period ones, item_embedding encodes future behavior → inflated offline metrics that collapse in production.

Safe pipeline:

```
interactions → time split → train_interactions / test_interactions
train_interactions → CF model → embeddings
embeddings + content → augmented features (train only)
augmented features → ranker training
test_interactions → evaluation only (no embedding from test leaks in)
```

**When this beats Weighted:** When your content signal (text, categories, attributes) is rich but CF alone is mediocre (sparse matrix, <50 interactions per user on average). CF embeddings inject collaborative signal into the content model without requiring CF to produce good standalone scores.

---

### Meta-Level (Stacking)

**Structure:**

```
Base models:          CF_score(u, i),  CB_score(u, i),  Popularity_score(i)
                                ↓               ↓                ↓
Meta-model input:   [CF_score, CB_score, Popularity_score, user_n_interactions, item_age, ...]
Meta-model output:  final_score(u, i)
```

**Meta-model choices:**

| Model | When appropriate |
|---|---|
| Logistic regression (linear) | Interpretable weights; see which component dominates |
| Gradient boosted trees (LightGBM) | Non-linear blending; captures context-dependent weighting |
| Neural network | Large training data; want end-to-end learned blending |

**Training the meta-model:**

Use **out-of-fold predictions** (k-fold on training data) to generate meta-features, never the base model's own training predictions:

```
1. Split training data into 5 folds
2. For each fold k:
   a. Train CF and CB on folds 1..k-1, k+1..5
   b. Generate CF_score and CB_score on fold k
3. Concatenate: you now have out-of-fold scores for all training examples
4. Train meta-model on these out-of-fold scores
5. For production: train CF and CB on ALL training data, meta-model weights stay fixed
```

**Complexity cost:** This architecture has the highest maintenance burden — you must retrain CF, CB, and the meta-model on a schedule. Before adopting, confirm that:
1. Weighted or switching hybrid falls below your accuracy target
2. You have enough labeled data for the meta-model (minimum ~50K user-item pairs with ground truth relevance)

---

## Architecture Complexity vs. Benefit

Roughly ordered from lowest to highest operational complexity:

```
Switching < Weighted < Cascade < Feature Augmentation < Meta-level
```

The first architecture that meets your accuracy target wins. This is not a spectrum where "more complex = better".

**Benchmark the increment:** Before adding complexity, measure:

```
Lift = NDCG_hybrid@10 - NDCG_best_single@10
```

A lift < 0.01 in NDCG@10 rarely justifies the complexity increase. A lift ≥ 0.03 usually does.

---

## Common Mismatches to Avoid

**Weighted hybrid with incompatible scores:** Using raw CF dot product (range: −∞ to +∞) and cosine similarity (range: −1 to 1) without normalization. The CF score will dominate regardless of α.

**Switching hybrid with a premature threshold:** Setting N_threshold = 50 when median user has 8 interactions. 80% of users get CB, defeating the purpose of having CF at all. Profile your interaction distribution before setting threshold.

**Cascade with Stage 1 recall below 80%:** Stage 2 cannot recover items Stage 1 dropped. Measure Stage 1 recall against held-out ground truth before tuning Stage 2 at all.

**Feature augmentation without time-based train/test split:** Using random 80/20 split allows CF to see future interactions during embedding training. Always split by time (e.g., train on months 1–10, evaluate on month 11).

**Meta-level on small datasets:** Stacking overfits easily. If you have fewer than 10K unique users with ≥5 interactions, use a simpler architecture.
