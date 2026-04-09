# ALS vs SGD: Matrix Factorization Optimization Comparison

Matrix factorization can be trained with two fundamentally different optimizers. **ALS** (Alternating Least Squares) fixes one factor matrix and solves a closed-form least-squares problem for the other; **SGD** (Stochastic Gradient Descent) updates both matrices simultaneously using sampled observations. The choice has concrete consequences for convergence speed, parallelism, and implicit-feedback suitability.

---

## Objective Function (Shared)

Both optimize the same regularized squared error on observed entries Ω:

```
L(U, V) = Σ_{(i,j)∈Ω} (r_ij - u_i · v_j)² + λ(||U||²_F + ||V||²_F)
```

Where:
- R ∈ ℝ^{m×n}: user-item interaction matrix (m users, n items)
- U ∈ ℝ^{m×k}: user latent factor matrix
- V ∈ ℝ^{n×k}: item latent factor matrix
- k: rank (number of latent factors)
- λ: L2 regularization coefficient
- Ω: set of observed (user, item) pairs

---

## ALS: Alternating Least Squares

### Derivation

Fix V, treat as a standard ridge regression for each user i:

```
∂L/∂u_i = -2 Σ_{j:(i,j)∈Ω} (r_ij - u_i · v_j) v_j + 2λu_i = 0
```

Rearranging yields a k×k linear system:

```
u_i = (V_i^T V_i + λI)^{-1} V_i^T r_i
```

Where:
- `V_i` = submatrix of V containing only items rated by user i (shape: |Ω_i| × k)
- `r_i` = vector of ratings by user i (shape: |Ω_i|)
- `λI` = regularization term (k×k)

Symmetric update for each item j:

```
v_j = (U_j^T U_j + λI)^{-1} U_j^T r_j
```

### ALS Step-by-Step (Worked Example)

**Setup:** 3 users, 3 items, k=1, λ=0.01

```
R = [[5, 3, 0],   # user 0 rated items 0,1
     [4, 0, 2],   # user 1 rated items 0,2
     [0, 1, 1]]   # user 2 rated items 1,2
```

**Initialize:** V = [[2.0], [1.0], [1.0]] (items × k)

**Iteration 1 — Solve U (fix V):**

User 0 rated items 0, 1 → V_0 = [[2.0], [1.0]], r_0 = [5, 3]
```
V_0^T V_0 = [[4.0 + 1.0]] = [[5.0]]
V_0^T V_0 + λI = [[5.01]]
V_0^T r_0 = [2.0×5 + 1.0×3] = [13.0]
u_0 = 13.0 / 5.01 ≈ 2.595
```

User 1 rated items 0, 2 → V_1 = [[2.0], [1.0]], r_1 = [4, 2]
```
V_1^T V_1 + λI = [[5.01]]
V_1^T r_1 = [2.0×4 + 1.0×2] = [10.0]
u_1 = 10.0 / 5.01 ≈ 1.996
```

User 2 rated items 1, 2 → V_2 = [[1.0], [1.0]], r_2 = [1, 1]
```
V_2^T V_2 + λI = [[2.01]]
V_2^T r_2 = [1.0×1 + 1.0×1] = [2.0]
u_2 = 2.0 / 2.01 ≈ 0.995
```

**After U update:** U ≈ [[2.595], [1.996], [0.995]]

**Iteration 1 — Solve V (fix U):** symmetric, same arithmetic.

ALS converges to the values shown in SKILL.md after ~50 iterations.

### ALS Computational Cost Per Iteration

Each user update requires solving a k×k system:
- Cost per user: O(|Ω_i| × k + k³)  — the k³ is the matrix inversion
- Total: O(nnz × k + (m+n) × k³)

For large k (k > 200), the k³ term dominates. ALS is expensive per iteration but converges in fewer iterations than SGD.

---

## SGD: Stochastic Gradient Descent

### Update Rules

For each observed rating (i, j, r_ij), compute prediction error:

```
e_ij = r_ij - u_i · v_j
```

Update both factors simultaneously:

```
u_i ← u_i + η (e_ij · v_j - λ · u_i)
v_j ← v_j + η (e_ij · u_i - λ · v_j)
```

Where η = learning rate.

**Critical:** use the OLD u_i value to update v_j within the same observation. Do not use the already-updated u_i.

### SGD Step-by-Step (Same Example)

**Setup:** Same 3×3 matrix, k=1, λ=0.01, η=0.01

**Initialize:** U = [[0.5], [0.5], [0.5]], V = [[0.5], [0.5], [0.5]]

**Epoch 1, observation (0, 0, 5):** user 0, item 0, rating 5
```
e = 5 - (0.5 × 0.5) = 5 - 0.25 = 4.75
u_0_new = 0.5 + 0.01 × (4.75 × 0.5 - 0.01 × 0.5)
        = 0.5 + 0.01 × (2.375 - 0.005)
        = 0.5 + 0.02370 = 0.52370

v_0_new = 0.5 + 0.01 × (4.75 × 0.5 - 0.01 × 0.5)
        = 0.52370  (symmetric in k=1 case)
```

SGD takes many epochs (typically 20-200) to converge, with learning rate decay.

### Learning Rate Schedule

Fixed η often diverges or converges slowly. Common schedules:

| Schedule | Formula | When |
|---|---|---|
| Constant | η_t = η₀ | Debugging only |
| Step decay | η_t = η₀ × γ^⌊t/step⌋ | Simple, common |
| 1/t decay | η_t = η₀ / (1 + decay × t) | Theoretical guarantees |
| AdaGrad | η_i = η₀ / √(Σ g²_i) | Sparse features |

For most MF with explicit ratings: step decay with γ=0.9 every 10 epochs works well. Start with η₀ ≈ 0.01.

---

## Direct Comparison

| Property | ALS | SGD |
|---|---|---|
| Update style | Closed-form per user/item | Stochastic gradient per observation |
| Iterations to converge | 10–30 | 20–200 epochs |
| Cost per iteration | O(nnz × k + (m+n) × k³) | O(nnz × k) |
| Parallelism | Trivially parallel (each user independent) | Harder (Hogwild or lock-based) |
| Hyperparameters | λ only | λ, η, schedule |
| Implicit feedback | Natural (weighted ALS, Hu et al.) | Requires explicit negative sampling |
| Memory | Stores all of U, V, plus k×k temp matrices | Same U, V; no temp matrices |
| Cold start sensitivity | Higher (solves full system with few observations) | Lower (just slower updates) |
| Large k (k > 200) | Expensive — k³ dominates | Linear in k — preferred |

---

## Decision Framework

```
START
│
├─ Is feedback implicit (clicks, views, purchases)?
│   └─ YES → Use weighted ALS (wALS). SGD requires complex negative sampling.
│
├─ Is k > 200?
│   └─ YES → Prefer SGD. ALS k³ inversion becomes bottleneck.
│
├─ Can you parallelize across machines (Spark, distributed)?
│   └─ YES → ALS parallelizes trivially. Use ALS.
│
├─ Single machine, explicit ratings, k ≤ 100?
│   └─ YES → Either works. ALS converges in fewer iterations.
│
└─ Need fast iteration on hyperparameters?
    └─ YES → SGD is easier to tune interactively (only η + λ).
```

---

## Implicit Feedback: Why ALS Wins

For implicit data (binary: 1=observed, 0=not observed), the Hu et al. (2008) weighted ALS formulation assigns confidence weights c_ij:

```
c_ij = 1 + α × f_ij
```

Where f_ij = raw frequency (number of plays, clicks). The objective becomes:

```
L = Σ_{i,j} c_ij (p_ij - u_i · v_j)² + λ(||U||² + ||V||²)
```

Where p_ij = 1 if observed, 0 otherwise (preference, not rating).

**Key property:** the summation is now over ALL (i,j) pairs (not just observed). This changes the ALS update to:

```
u_i = (V^T C_i V + λI)^{-1} V^T C_i p_i
```

Where C_i = diagonal matrix of confidence weights for user i.

The trick: decompose `V^T C_i V = V^T V + V^T (C_i - I) V`. Since C_i - I is sparse (only observed items have c_ij > 1), this reduces cost from O(n × k²) to O(nnz_i × k²). ALS handles this algebraically; SGD would need to explicitly iterate all (i,j) pairs each epoch, which is O(m×n) — prohibitive.

**Conclusion:** For implicit feedback, use weighted ALS. SGD on implicit data requires careful negative sampling strategy and is significantly harder to tune.

---

## Convergence Behavior

**ALS** typically shows monotonically decreasing training loss. Each solve is optimal given the other matrix fixed — training RMSE decreases every half-iteration.

**SGD** shows noisy loss curves due to stochastic sampling. With proper learning rate decay, it converges to comparable final RMSE but the path is noisier.

Empirical observation on MovieLens-1M (explicit ratings, k=50):

| Method | Iterations to RMSE < 0.92 | Wall time (single core) |
|---|---|---|
| ALS | ~15 | ~45s |
| SGD (η=0.01, step decay) | ~60 epochs | ~30s |
| SGD (AdaGrad) | ~40 epochs | ~35s |

ALS converges in fewer iterations; SGD can be faster wall-time on single core because per-iteration cost is lower. On distributed systems, ALS's trivial parallelism reverses this.

---

## Practical Hyperparameter Ranges

**ALS:**
- λ: [0.001, 1.0] — typical 0.01–0.1. Cross-validate on validation RMSE.
- k: [10, 200] — see IRON LAW in SKILL.md. Start at 50.
- Iterations: 20 is usually sufficient; check plateau on validation RMSE.

**SGD:**
- λ: same as ALS
- η₀: [0.001, 0.1] — start at 0.01. If loss diverges, halve it.
- Decay: step decay 0.9 per 10 epochs
- Epochs: 50–100. Monitor validation RMSE; stop when it plateaus.
- Batch size: pure SGD (batch=1) works; mini-batch (256–4096) improves GPU utilization.

---

## Code Skeleton: ALS Core Update

```python
import numpy as np

def als_update_users(R_csr, V, lam, k):
    """
    R_csr: scipy.sparse.csr_matrix (m x n)
    V: item factors (n x k)
    Returns updated U (m x k)
    """
    m = R_csr.shape[0]
    U = np.zeros((m, k))
    VTV = V.T @ V  # k x k, precomputed once per half-iteration
    reg = lam * np.eye(k)

    for i in range(m):
        # indices and ratings for user i
        row = R_csr.getrow(i)
        cols = row.indices
        if len(cols) == 0:
            continue  # no ratings — leave as zero
        ratings = row.data
        Vi = V[cols]  # |Ω_i| x k

        # A = V_i^T V_i + λI  (could also use VTV with correction for density)
        A = Vi.T @ Vi + reg
        b = Vi.T @ ratings
        U[i] = np.linalg.solve(A, b)

    return U

def als(R_csr, k=50, lam=0.01, n_iter=20):
    m, n = R_csr.shape
    rng = np.random.default_rng(42)
    U = rng.normal(0, 0.1, (m, k))
    V = rng.normal(0, 0.1, (n, k))

    R_csc = R_csr.tocsc()
    for t in range(n_iter):
        U = als_update_users(R_csr, V, lam, k)
        V = als_update_users(R_csc, U, lam, k)
    return U, V
```

## Code Skeleton: SGD Core Update

```python
def sgd(R_csr, k=50, lam=0.01, lr=0.01, n_epochs=50, lr_decay=0.9):
    m, n = R_csr.shape
    rng = np.random.default_rng(42)
    U = rng.normal(0, 0.1, (m, k))
    V = rng.normal(0, 0.1, (n, k))

    R_coo = R_csr.tocoo()
    rows, cols, data = R_coo.row, R_coo.col, R_coo.data
    idx = np.arange(len(data))

    eta = lr
    for epoch in range(n_epochs):
        rng.shuffle(idx)
        for t in idx:
            i, j, r = rows[t], cols[t], data[t]
            err = r - U[i] @ V[j]
            # save old U[i] before update
            ui_old = U[i].copy()
            U[i] += eta * (err * V[j] - lam * U[i])
            V[j] += eta * (err * ui_old - lam * V[j])

        if (epoch + 1) % 10 == 0:
            eta *= lr_decay

    return U, V
```

The `ui_old = U[i].copy()` is mandatory. Updating V[j] with already-modified U[i] introduces bias and slows convergence.
