# Implicit Feedback Matrix Factorization

Implicit feedback (clicks, views, purchases, play counts) differs fundamentally from explicit ratings: values are always non-negative, absence means "unknown" not "disliked", and confidence in an observation varies with quantity. Standard ALS minimizes squared error only on observed entries — wrong here because every unobserved entry is a candidate negative, not missing data.

This document covers the Hu et al. 2008 Weighted MF formulation, the ALS closed-form solution, confidence weight design, and a worked numerical example.

---

## The Core Problem

In explicit MF, the objective is:

```
minimize Σ_{(i,j) observed} (rᵢⱼ - uᵢ·vⱼ)² + λ(||U||² + ||V||²)
```

For implicit data, this fails because:

1. **You must predict on ALL (i,j) pairs**, not just observed ones — a user not buying an item is a weak negative signal.
2. **Observed entries are noisy** — one click might be accidental; 50 plays is strong evidence.
3. **Ignoring unobserved entries underestimates missing negatives** at inference time.

---

## Weighted Matrix Factorization (Hu et al. 2008)

### Preference and Confidence

Define two matrices from raw interaction counts dᵢⱼ:

**Preference** (binary):
```
pᵢⱼ = 1  if dᵢⱼ > 0
pᵢⱼ = 0  if dᵢⱼ = 0
```

**Confidence** (scales with count):
```
cᵢⱼ = 1 + α · dᵢⱼ
```

- α is a hyperparameter (typical range: 1–40; default 10 for play counts, 1 for binary clicks).
- Unobserved entries get cᵢⱼ = 1 (minimum confidence, not zero).
- Observed entries get cᵢⱼ > 1 proportional to how many times the user interacted.

### Objective

```
L = Σᵢ Σⱼ cᵢⱼ (pᵢⱼ - uᵢ·vⱼ)² + λ(||U||² + ||V||²)
```

**Key difference from explicit MF:** the sum is over **all** (i,j) pairs, not just observed ones. This is what forces the model to push predictions toward 0 for unobserved entries.

---

## ALS Closed-Form Solution

Because the loss includes all pairs, the per-user update becomes analytically tractable.

### Solving for user factors (fix V, update U)

For user i, the gradient w.r.t. uᵢ set to zero gives:

```
uᵢ = (V^T Cⁱ V + λI)⁻¹ V^T Cⁱ pᵢ
```

Where:
- **Cⁱ** is an n×n diagonal matrix with Cⁱⱼⱼ = cᵢⱼ
- **pᵢ** is the n-vector of preferences for user i
- **V^T Cⁱ V** is a k×k matrix

### Solving for item factors (fix U, update V)

Symmetric:
```
vⱼ = (U^T Cʲ U + λI)⁻¹ U^T Cʲ qⱼ
```

Where Cʲ is m×m diagonal and qⱼ is the m-vector of preferences for item j.

### Computational trick: avoid O(n²k) per user

Naive evaluation of V^T Cⁱ V costs O(n·k²). Use the decomposition:

```
V^T Cⁱ V = V^T V + V^T (Cⁱ - I) V
```

- **V^T V** (k×k) is precomputed once per ALS iteration: O(n·k²) total, shared by all users.
- **V^T (Cⁱ - I) V** only sums over non-zero entries for user i (i.e., observed interactions): O(nnzᵢ · k²) where nnzᵢ is the number of items user i interacted with.

Total per-iteration cost: **O(k² · (m+n) + k³ · (m+n) + nnz · k²)**

This is the reason implicit ALS scales — you only iterate over non-zeros in the inner loop.

---

## Worked Numerical Example

### Setup

3 users, 4 items. Raw interaction counts (0 = no interaction):

```
D = [[3, 1, 0, 0],
     [0, 0, 2, 4],
     [1, 0, 0, 1]]
```

k = 1 (rank-1 for hand-tractability), α = 10, λ = 0.1

### Step 1: Compute Preference and Confidence

```
P = [[1, 1, 0, 0],
     [0, 0, 1, 1],
     [1, 0, 0, 1]]

C = [[1+10·3, 1+10·1,    1,    1],   = [[31, 11,  1,  1],
     [     1,       1, 1+20, 1+40],      [ 1,  1, 21, 41],
     [  1+10,       1,    1, 1+10]]       [11,  1,  1, 11]]
```

### Step 2: Initialize V (item factors, 4×1)

```
V = [[0.5], [0.3], [0.7], [0.9]]
```

### Step 3: Update u₁ (user 0)

Precompute V^T V:
```
V^T V = 0.5² + 0.3² + 0.7² + 0.9² = 0.25 + 0.09 + 0.49 + 0.81 = 1.64
```

V^T (C⁰ - I) V = (31-1)·0.5² + (11-1)·0.3² + (1-1)·0.7² + (1-1)·0.9²
               = 30·0.25 + 10·0.09
               = 7.5 + 0.9 = 8.4

V^T C⁰ V = 1.64 + 8.4 = 10.04

V^T C⁰ p⁰ = 31·1·0.5 + 11·1·0.3 + 1·0·0.7 + 1·0·0.9
           = 15.5 + 3.3 = 18.8

u₁ = (10.04 + 0.1)⁻¹ · 18.8 = 18.8 / 10.14 ≈ 1.854
```

### Step 4: Predicted ratings after one ALS step

After converging (conceptually), users who interacted heavily with items get high predictions on those items, and near-zero on items they never touched.

Expected behavior for this example after full convergence:
- R̂[0][0] ≈ 1.0 (user 0 strongly prefers item 0, count=3)
- R̂[1][3] ≈ 1.0 (user 1 strongly prefers item 3, count=4)
- R̂[0][2] ≈ 0.0 (user 0 never touched item 2)

Note: predictions are in [0,1] (closer to preference space, not rating space).

---

## Confidence Weight Design

The linear scheme `cᵢⱼ = 1 + α·dᵢⱼ` is not the only option. Choose based on your interaction type.

| Interaction Type | Recommended Scheme | Notes |
|---|---|---|
| Play counts (music, video) | `1 + α·dᵢⱼ` (linear) | Hu et al. default; α=10-40 |
| Binary clicks | `1 + α·dᵢⱼ` with dᵢⱼ ∈ {0,1} | Equivalent to weighting positives by α+1 |
| Purchase amounts | `1 + α·log(1 + dᵢⱼ/ε)` (log) | Dampens outlier spenders; ε prevents log(0) |
| Time-on-page (seconds) | `1 + α·log(1 + dᵢⱼ/ε)` (log) | Outlier sessions dominate otherwise |
| Recency-weighted | `cᵢⱼ = 1 + α·dᵢⱼ·decay(tᵢⱼ)` | Multiply by e^(-β·Δt) for time decay |

**Tuning α:** α controls signal-to-noise between positives and negatives.
- α too small → model nearly ignores which items were interacted with
- α too large → model overfits to popular items (high-count interactions dominate)
- Grid search α ∈ {1, 5, 10, 20, 40} using Recall@K on held-out interactions

---

## Evaluation: RMSE Is Wrong for Implicit MF

Do not use RMSE. Use ranking metrics on held-out positive interactions:

**Recall@K:** For each user, hold out one interaction. Did it appear in top-K recommendations?
```
Recall@K = (# users where held-out item is in top-K) / (# total users)
```

**NDCG@K:** Normalized Discounted Cumulative Gain — discounts items ranked lower:
```
DCG@K  = Σₖ relevanceₖ / log₂(k+1)
NDCG@K = DCG@K / ideal_DCG@K
```

For binary implicit data, relevance ∈ {0,1}.

**Protocol:** Leave-one-out (hold out each user's most recent interaction for test). For evaluation speed with large item catalogs, sample 100-999 random negative items per user and rank the held-out positive among them.

---

## Negative Sampling vs. Full-Matrix ALS

Two implementation strategies:

### Full-matrix ALS (Hu et al.)
- Sums over all (i,j) pairs using the V^T V precomputation trick
- Exact solution; scales to millions of items if k is small
- Requires full item catalog in memory

### Sampled SGD (BPR / random negatives)
- Sample one negative per positive per step
- Much faster per iteration but noisier
- Required for very large item catalogs (> 10M items)

**Rule of thumb:** Use full ALS when n_items < 1M and you have dense GPU/CPU. Use sampled SGD (e.g., BPR) for larger catalogs or streaming updates.

---

## Python Reference Implementation

Minimal implicit ALS — pure stdlib + numpy (numpy is the de facto standard for matrix ops here).

```python
import numpy as np

def implicit_als(D, k=20, alpha=10, lam=0.01, n_iter=20):
    """
    D: (m, n) sparse matrix of raw interaction counts (numpy array or scipy sparse)
    Returns U (m, k), V (n, k)
    """
    m, n = D.shape
    # Preference and confidence
    P = (D > 0).astype(float)
    C = 1 + alpha * D  # (m, n)

    # Initialize factors
    rng = np.random.default_rng(42)
    U = rng.standard_normal((m, k)) * 0.01
    V = rng.standard_normal((n, k)) * 0.01

    for iteration in range(n_iter):
        # Update U: fix V
        VTV = V.T @ V  # (k, k), precomputed once
        for i in range(m):
            ci = C[i]          # (n,) confidence for user i
            pi = P[i]          # (n,) preference for user i
            # V^T (C^i - I) V: only non-zero entries
            nz = D[i] > 0
            VT_diag_V = VTV + (V[nz] * (ci[nz] - 1)[:, None]).T @ V[nz]
            A = VT_diag_V + lam * np.eye(k)
            b = (V * (ci * pi)[:, None]).sum(axis=0)
            U[i] = np.linalg.solve(A, b)

        # Update V: fix U
        UTU = U.T @ U  # (k, k)
        for j in range(n):
            cj = C[:, j]
            pj = P[:, j]
            nz = D[:, j] > 0
            UT_diag_U = UTU + (U[nz] * (cj[nz] - 1)[:, None]).T @ U[nz]
            A = UT_diag_U + lam * np.eye(k)
            b = (U * (cj * pj)[:, None]).sum(axis=0)
            V[j] = np.linalg.solve(A, b)

    return U, V


def recommend(U, V, user_id, top_n=10, exclude_seen=None):
    scores = U[user_id] @ V.T  # (n,)
    if exclude_seen:
        scores[exclude_seen] = -np.inf
    return np.argsort(scores)[::-1][:top_n]
```

**Note:** This is O(m·nnz_per_user·k²) and works for mid-scale problems. For production, use the `implicit` library (GPU-accelerated) or Spark ALS for distributed.

---

## Common Mistakes

**Using RMSE loss on implicit data** — RMSE treats unobserved as missing, so the model never learns to predict 0 for unseen items. Use weighted loss over all pairs.

**Setting α too high for binary click data** — With binary dᵢⱼ ∈ {0,1}, α=40 makes positives 41× more important than negatives. Often α=1-5 suffices for binary.

**Not excluding seen items at inference** — Implicit MF will recommend items already purchased. Always filter out training interactions before top-N selection.

**Evaluating Recall@K on too-small K** — With a catalog of 100K items, Recall@10 is nearly zero for any model. Report Recall@50 and Recall@100 as baselines alongside Recall@10.

**Forgetting that unobserved ≠ negative** — A user who hasn't bought an item may simply not know it exists. Implicit MF handles this gracefully by weighting unobserved entries at cᵢⱼ=1 rather than treating them as strong negatives.

---

## Reference

Hu, Y., Koren, Y., & Volinsky, C. (2008). Collaborative filtering for implicit feedback datasets. *ICDM 2008*, 263–272.
