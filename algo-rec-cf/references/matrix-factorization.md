# Matrix Factorization

Matrix factorization (MF) is the primary scalable alternative to neighborhood-based CF. Instead of computing pairwise similarities (O(U²) or O(I²)), MF learns compact latent factor vectors for each user and item. Recommendation reduces to a dot product.

## Core Model

Factorize the rating matrix **R** (U×I) into two low-rank matrices:

```
R ≈ P × Q^T
```

- **P** (U×K): user factor matrix, row `p_u` is user u's latent vector
- **Q** (I×K): item factor matrix, row `q_i` is item i's latent vector
- **K**: number of latent factors (typically 10–200)

Predicted rating:

```
r̂_ui = p_u · q_i = Σ_k (p_uk × q_ik)
```

Only observed entries in **R** are used during training. Unobserved entries are what you want to predict.

## Objective Function

Minimize regularized squared error over all observed ratings:

```
L = Σ_(u,i)∈Ω [ (r_ui - p_u · q_i)² + λ(‖p_u‖² + ‖q_i‖²) ]
```

- **Ω**: set of (user, item) pairs with observed ratings
- **λ**: regularization coefficient (prevents overfitting; typical range 0.01–0.1)
- **‖·‖²**: L2 norm (sum of squared vector elements)

The regularization terms penalize large factor values, acting as implicit shrinkage toward zero.

## Two Standard Training Approaches

### SGD (Stochastic Gradient Descent)

For each observed (u, i) pair, compute error and update:

```
e_ui = r_ui - p_u · q_i

p_u ← p_u + α × (e_ui × q_i - λ × p_u)
q_i ← q_i + α × (e_ui × p_u - λ × q_i)
```

- **α**: learning rate (typical range 0.001–0.01)
- Update `p_u` and `q_i` simultaneously using the pre-update values of the other

**When to use SGD:**
- Large datasets where ALS memory cost is prohibitive
- Online/incremental updates needed (new ratings arrive continuously)
- When you can shuffle training data

### ALS (Alternating Least Squares)

Fix Q, solve analytically for each p_u; then fix P, solve for each q_i. Repeat.

For a fixed Q, each p_u has a closed-form solution:

```
p_u = (Q_u^T Q_u + λI)^{-1} Q_u^T r_u
```

Where:
- `Q_u`: submatrix of Q with rows for items rated by user u (size: n_u × K)
- `r_u`: vector of user u's observed ratings (length n_u)
- `I`: K×K identity matrix

**When to use ALS:**
- Parallel/distributed training (each user's update is independent)
- Implicit feedback data (see `references/implicit-feedback.md` for confidence weighting)
- Faster convergence in practice for dense enough data

## Worked Example (3 users × 4 items, K=2)

**Rating matrix R** (0 = unobserved):

```
       item1  item2  item3  item4
user1:   4      0      0      1
user2:   0      5      0      3
user3:   0      4      1      0
```

**Initialize** P and Q randomly (e.g., from N(0, 0.1)):

```
P = [[0.12,  0.03],   # user1
     [-0.04, 0.09],   # user2
     [0.07, -0.02]]   # user3

Q = [[0.05,  0.11],   # item1
     [0.08, -0.06],   # item2
     [0.03,  0.07],   # item3
     [-0.09, 0.04]]   # item4
```

**SGD pass, α=0.01, λ=0.02 — one update for (user1, item1):**

```
r̂_11 = [0.12, 0.03] · [0.05, 0.11] = 0.0060 + 0.0033 = 0.0093
e_11  = 4.0 - 0.0093 = 3.9907

p_1_new = [0.12, 0.03] + 0.01 × (3.9907 × [0.05, 0.11] - 0.02 × [0.12, 0.03])
        = [0.12, 0.03] + 0.01 × ([0.1995, 0.4390] - [0.0024, 0.0006])
        = [0.12, 0.03] + [0.001971, 0.004384]
        = [0.121971, 0.034384]

q_1_new = [0.05, 0.11] + 0.01 × (3.9907 × [0.12, 0.03] - 0.02 × [0.05, 0.11])
        = [0.05, 0.11] + 0.01 × ([0.4789, 0.1197] - [0.001, 0.0022])
        = [0.05, 0.11] + [0.004779, 0.001175]
        = [0.054779, 0.111175]
```

After ~50–100 full passes over observed data, predictions converge. The final dot products `p_u · q_i` for unobserved cells are predicted ratings.

## Choosing K (Number of Latent Factors)

K controls the capacity–generalization tradeoff:

| K | Effect | Typical Use |
|---|--------|-------------|
| 10–20 | High regularization, fast | Sparse data, cold-start-prone datasets |
| 50–100 | Balanced | Most production systems |
| 200–500 | High capacity, slow | Dense data, nuanced taste modeling |

**Practical guidance:**
1. Start at K=50
2. Tune λ before tuning K (regularization has larger impact at small K)
3. Increase K only after λ is well-tuned; diminishing returns beyond K=200 for most datasets
4. Measure RMSE on held-out 20% validation split per the parent skill's Phase 3 gate

## Bias Extension

Plain MF misses systematic rating offsets. Add user and item biases:

```
r̂_ui = μ + b_u + b_i + p_u · q_i
```

- **μ**: global mean rating (scalar, computed once from training data)
- **b_u**: user bias (how much user u rates above/below μ on average)
- **b_i**: item bias (how much item i is rated above/below μ on average)

Biases are learned jointly with P and Q. Updated objective:

```
L = Σ_(u,i)∈Ω [ (r_ui - μ - b_u - b_i - p_u·q_i)² + λ(b_u² + b_i² + ‖p_u‖² + ‖q_i‖²) ]
```

SGD updates for biases:

```
e_ui = r_ui - r̂_ui

b_u ← b_u + α × (e_ui - λ × b_u)
b_i ← b_i + α × (e_ui - λ × b_i)
```

**In practice:** adding biases reduces RMSE by 5–10% over plain MF at negligible cost. Always include them.

## MF vs Neighborhood CF: When to Switch

| Condition | Neighborhood CF | Matrix Factorization |
|-----------|----------------|---------------------|
| Users < 10K | ✓ (manageable O(U²)) | Either |
| Users > 100K | ✗ (too slow) | ✓ |
| Items > 1M | ✗ (item-based too slow) | ✓ |
| Need explainability ("similar users liked X") | ✓ | ✗ (latent factors opaque) |
| Need fast inference after training | Either | ✓ (single dot product) |
| Incremental updates (real-time) | ✓ | SGD-MF only |
| Sparsity < 0.1% fill rate | Both degrade | MF degrades more gracefully |
| Implicit feedback (clicks/views) | Requires adjustment | ✓ (ALS-MF handles well) |

The IRON LAW from the parent skill applies equally: below 5+ ratings per user / item, MF latent vectors are poorly constrained. Regularization (λ) partially compensates, but sparse users still yield unreliable predictions. MF does not solve cold start — it defers it.

## Minimal Python Implementation (SGD, pure stdlib)

```python
import random
import math

def matrix_factorize(ratings, n_users, n_items, K=20, alpha=0.01,
                     lam=0.02, n_epochs=20, seed=42):
    """
    ratings: list of (user_id, item_id, rating) tuples — 0-indexed
    Returns: P (n_users x K), Q (n_items x K), b_u (n_users,), b_i (n_items,), mu
    """
    rng = random.Random(seed)
    init = lambda: [rng.gauss(0, 0.1) for _ in range(K)]

    P = [init() for _ in range(n_users)]
    Q = [init() for _ in range(n_items)]
    b_u = [0.0] * n_users
    b_i = [0.0] * n_items
    mu = sum(r for _, _, r in ratings) / len(ratings)

    for epoch in range(n_epochs):
        rng.shuffle(ratings)
        total_loss = 0.0
        for u, i, r in ratings:
            dot = sum(P[u][k] * Q[i][k] for k in range(K))
            e = r - mu - b_u[u] - b_i[i] - dot
            total_loss += e * e

            b_u[u] += alpha * (e - lam * b_u[u])
            b_i[i] += alpha * (e - lam * b_i[i])
            for k in range(K):
                pu_k = P[u][k]
                qi_k = Q[i][k]
                P[u][k] += alpha * (e * qi_k - lam * pu_k)
                Q[i][k] += alpha * (e * pu_k - lam * qi_k)

        rmse = math.sqrt(total_loss / len(ratings))
        # Optional: print(f"Epoch {epoch+1}: train RMSE = {rmse:.4f}")

    return P, Q, b_u, b_i, mu


def predict(u, i, P, Q, b_u, b_i, mu, rating_min=1.0, rating_max=5.0):
    K = len(P[u])
    dot = sum(P[u][k] * Q[i][k] for k in range(K))
    r_hat = mu + b_u[u] + b_i[i] + dot
    return max(rating_min, min(rating_max, r_hat))  # clamp to valid range
```

**Usage:**

```python
ratings = [
    (0, 0, 4), (0, 3, 1),   # user1
    (1, 1, 5), (1, 3, 3),   # user2
    (2, 1, 4), (2, 2, 1),   # user3
]
P, Q, b_u, b_i, mu = matrix_factorize(ratings, n_users=3, n_items=4, K=2)
score = predict(0, 2, P, Q, b_u, b_i, mu)  # predict user1 → item3
print(f"Predicted: {score:.2f}")
```

**Notes on the implementation:**
- Uses `pu_k = P[u][k]` before updating so both P and Q use pre-update values in the same step — required for correct SGD
- Clamping predicted ratings to `[rating_min, rating_max]` prevents nonsensical outputs
- For production scale, replace with NumPy vectorized updates or use `scipy.sparse`

## Common Failure Modes

**Divergence (loss goes to NaN):** α too large. Halve it. If still diverging, check for ratings on a non-normalized scale (e.g., 0–100 instead of 1–5) — center and scale first.

**RMSE plateaus above baseline:** λ too large (underfitting). Reduce λ by 10×. If still stuck, increase K.

**Overfitting (train RMSE drops, val RMSE rises):** λ too small. Increase λ or reduce K.

**All predictions cluster near μ:** Learning rate α too small, or n_epochs too few. Also check that at least a few hundred training samples exist — MF cannot learn meaningful factors from tiny datasets.

**Popularity bias persists:** Item bias b_i absorbs popularity signal, which is correct behavior. If you want to suppress it, cap b_i during training using `b_i[i] = max(-1.0, min(1.0, b_i[i]))`.
