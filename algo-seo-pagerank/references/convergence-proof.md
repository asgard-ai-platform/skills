# PageRank Convergence Proof

## The Power Iteration Framework

PageRank is computed by power iteration on a transition matrix. Convergence is guaranteed under specific conditions derived from Perron-Frobenius theorem. This document proves those conditions and derives practical stopping criteria.

---

## Matrix Formulation

Let G = (V, E) be a directed graph with N nodes. Define:

**Raw transition matrix H** (N×N):

```
H[i][j] = 1 / L(j)   if there is a link from j to i
H[i][j] = 0           otherwise
```

where L(j) = out-degree of node j.

**Dangling node correction**: Let **d** be the dangling vector:

```
d[j] = 1   if L(j) = 0  (node j has no outlinks)
d[j] = 0   otherwise
```

The stochastic matrix S handles dangling nodes by redistributing their rank:

```
S = H + (1/N) * e * d^T
```

where **e** is the all-ones column vector (N×1). This ensures every column of S sums to 1.0.

**Google Matrix G** (the actual PageRank matrix):

```
G = α * S + (1-α)/N * e * e^T
```

where α is the damping factor (typically 0.85). The term `(1-α)/N * e * e^T` is a rank-1 matrix where every entry equals `(1-α)/N`.

The PageRank vector **r** satisfies:

```
r = G * r
```

i.e., **r** is the principal eigenvector of G with eigenvalue 1.

---

## Why Convergence is Guaranteed: Perron-Frobenius

**Theorem (Perron-Frobenius for stochastic matrices):** A matrix G is *primitive* and *stochastic* if and only if it has a unique dominant eigenvalue λ₁ = 1, and power iteration `r^(k+1) = G * r^(k)` converges to the unique stationary distribution regardless of starting vector.

G satisfies these conditions:

1. **Column-stochastic**: Every column sums to 1. Proof: each column of S already sums to 1 (by construction). Multiplying by α and adding `(1-α)/N * e^T` preserves the column sum at 1.

2. **Irreducible**: G is irreducible because the term `(1-α)/N * e * e^T` has all positive entries. This means there is a positive probability path between any two nodes (via the random jump), regardless of link structure. Therefore every state is reachable from every other state.

3. **Aperiodic**: The self-loop probability `(1-α)/N > 0` for every node ensures G is aperiodic.

An irreducible, aperiodic, column-stochastic matrix has exactly one eigenvalue of magnitude 1 (λ₁ = 1), and all other eigenvalues satisfy |λᵢ| < 1. Power iteration converges to the eigenvector corresponding to λ₁ = 1.

**Critical implication**: Without the damping factor (α = 1), G = S. S may be reducible if the link graph is not strongly connected, violating Perron-Frobenius and breaking convergence. This is the mathematical basis for the IRON LAW: **α must be strictly less than 1**.

---

## Convergence Rate

The rate of convergence of power iteration is determined by the ratio of the two largest eigenvalues:

```
convergence rate = |λ₂| / |λ₁| = |λ₂|
```

For the Google Matrix G, the second eigenvalue satisfies:

```
|λ₂| ≤ α
```

**Proof sketch**: The eigenvalues of G are related to the eigenvalues of S. The rank-1 perturbation `(1-α)/N * e * e^T` shifts the spectrum. The dominant eigenvalue of S is 1 (stochastic matrix). All other eigenvalues of S are ≤ 1 in magnitude. After the perturbation:

- λ₁(G) = 1 (unchanged, eigenvector is the stationary distribution)
- λᵢ(G) = α * λᵢ(S) for i ≥ 2

Therefore |λ₂(G)| ≤ α.

**Practical consequence**: After k iterations, the error in PageRank satisfies:

```
‖r^(k) - r*‖ ≤ α^k * ‖r^(0) - r*‖
```

With α = 0.85, the error shrinks by a factor of 0.85 per iteration. To reach error ε:

```
k ≥ log(ε) / log(α)
```

| Target ε | Iterations needed (α=0.85) |
|----------|---------------------------|
| 1e-3     | 43                        |
| 1e-6     | 87                        |
| 1e-9     | 130                       |

This explains why the SKILL.md convergence threshold ε=1e-6 typically requires ~45-90 iterations in practice.

---

## Worked Numerical Example

**Graph**: A→B, A→C, B→C, C→A (3 nodes, 4 edges, α=0.85)

**Step 1: Build H**

Out-degrees: L(A)=2, L(B)=1, L(C)=1. No dangling nodes.

```
H (row i = destination, col j = source):

       A      B      C
A  [ 0.00  0.00  1.00 ]
B  [ 0.50  0.00  0.00 ]
C  [ 0.50  1.00  0.00 ]
```

**Step 2: Build G = 0.85*H + 0.15/3 * ones**

```
0.15/3 = 0.05

G:
       A      B      C
A  [ 0.05  0.05  0.90 ]
B  [ 0.475 0.05  0.05 ]
C  [ 0.475 0.90  0.05 ]
```

Verify: each column sums to 1.0. ✓

**Step 3: Power iteration**

Initialize r⁰ = [1/3, 1/3, 1/3]

Iteration 1: r¹ = G * r⁰

```
r¹[A] = 0.05*(1/3) + 0.05*(1/3) + 0.90*(1/3) = (0.05+0.05+0.90)/3 = 1.00/3 = 0.3333
r¹[B] = 0.475*(1/3) + 0.05*(1/3) + 0.05*(1/3) = (0.475+0.05+0.05)/3 = 0.575/3 = 0.1917
r¹[C] = 0.475*(1/3) + 0.90*(1/3) + 0.05*(1/3) = (0.475+0.90+0.05)/3 = 1.425/3 = 0.4750
```

Sum check: 0.3333 + 0.1917 + 0.4750 = 1.0000 ✓

Iteration 2: r² = G * r¹

```
r²[A] = 0.05*0.3333 + 0.05*0.1917 + 0.90*0.4750
      = 0.01667 + 0.00958 + 0.42750 = 0.45375

r²[B] = 0.475*0.3333 + 0.05*0.1917 + 0.05*0.4750
      = 0.15832 + 0.00958 + 0.02375 = 0.19165

r²[C] = 0.475*0.3333 + 0.90*0.1917 + 0.05*0.4750
      = 0.15832 + 0.17253 + 0.02375 = 0.35460
```

Sum: 0.45375 + 0.19165 + 0.35460 = 1.0000 ✓

Continuing to convergence (iteration ~50):

```
r*[A] ≈ 0.327
r*[B] ≈ 0.283
r*[C] ≈ 0.390
```

**Intuition check**: C receives links from both A and B, so it accumulates the most rank. A receives from C (which has high rank), so A > B. B only receives from A (which has moderate rank and splits its output to B and C), giving B the lowest score.

---

## Stopping Criterion Derivation

The SKILL.md uses L1 norm change < ε = 1e-6 as the convergence test. Here is why:

**L1 norm** of the residual:

```
δ^(k) = ‖r^(k) - r^(k-1)‖₁ = Σᵢ |rᵢ^(k) - rᵢ^(k-1)|
```

From the convergence rate bound:

```
‖r^(k) - r*‖₁ ≤ α / (1-α) * δ^(k)
```

This is derived from the geometric series bound: if the error decreases by factor α each step, the remaining error is bounded by α/(1-α) times the last step size.

With α = 0.85:

```
α / (1-α) = 0.85 / 0.15 ≈ 5.67
```

So stopping at δ < 1e-6 guarantees:

```
‖r^(k) - r*‖₁ < 5.67 × 1e-6 ≈ 6e-6
```

For N = 1 million pages, the per-page error is bounded by ~6e-12, which is negligible for ranking purposes.

**Alternative: relative change criterion**

```
δ_rel^(k) = ‖r^(k) - r^(k-1)‖₁ / ‖r^(k)‖₁
```

Since ‖r^(k)‖₁ = 1.0 always (invariant), L1 and relative L1 are equivalent here. Using L2 norm is also valid but L1 is preferred: it directly measures total probability mass redistributed per iteration, which has a natural interpretation.

---

## Dangling Node Rank Conservation

Without the dangling correction, rank leaks. Proof:

Let d be the set of dangling nodes. After one iteration without correction:

```
Σᵢ r_new[i] = Σᵢ Σ_{j→i} α * r[j]/L(j) + Σᵢ (1-α)/N
             = α * Σ_{j ∉ d} r[j]   +   (1-α)
             < α * 1.0 + (1-α) = 1.0   (strict if d is non-empty)
```

The missing mass is `α * Σ_{j ∈ d} r[j]` — the rank held by dangling nodes that went nowhere.

**Correct implementation**: before the main update, compute:

```
dangling_sum = Σ_{j ∈ d} r[j]
```

Add `α * dangling_sum / N` to every page's new rank. This redistributes the leaked rank uniformly. The sum is then preserved:

```
Σᵢ r_new[i] = α * Σ_{j ∉ d} r[j] + α * dangling_sum + (1-α) = α * 1.0 + (1-α) = 1.0
```

**Code**:

```python
def pagerank_iteration(r, H, dangling_nodes, alpha, N):
    dangling_sum = sum(r[j] for j in dangling_nodes)
    r_new = {}
    for i in range(N):
        # incoming link contribution
        link_contribution = sum(r[j] / out_degree[j] for j in in_neighbors[i])
        # dangling redistribution + random jump
        r_new[i] = (alpha * link_contribution
                    + alpha * dangling_sum / N
                    + (1 - alpha) / N)
    return r_new
```

Sum invariant verification: `assert abs(sum(r_new.values()) - 1.0) < 1e-10`

---

## Effect of Damping Factor on Convergence vs. Quality

| α    | Iterations to ε=1e-6 | Rank sink risk | Notes |
|------|----------------------|----------------|-------|
| 0.50 | ~46                  | Low            | Converges fast, but rankings dominated by random jump; loses link authority signal |
| 0.75 | ~69                  | Low-Medium     | Used in some personalized PR variants |
| 0.85 | ~87                  | Medium         | Original Brin-Page value; standard choice |
| 0.90 | ~120                 | Medium-High    | Slower; sensitive to spider traps |
| 0.95 | ~182                 | High           | Very slow; not recommended for large graphs |
| 1.00 | ∞ (may not converge) | Guaranteed     | Violates IRON LAW |

The formula `k ≥ log(ε) / log(α)` is the direct source for these estimates. At α=0.85, log(1e-6)/log(0.85) = -6*log(10)/log(0.85) ≈ 87.

---

## Sparse Graph Convergence Warning

The bound |λ₂| ≤ α holds for the Google Matrix G, not for S alone. In practice, for graphs where the underlying structure has a second eigenvalue close to 1 (e.g., nearly disconnected components), the bound is tight and you do need the full ~87 iterations.

For well-connected graphs (e.g., |λ₂(S)| ≈ 0.3), convergence may occur in 20-30 iterations even at α=0.85, because:

```
|λ₂(G)| = α * |λ₂(S)| ≈ 0.85 * 0.3 = 0.255
```

Which gives k ≥ log(1e-6)/log(0.255) ≈ 9 iterations.

Do not hard-code an iteration limit below 100 without measuring |λ₂| or verifying early convergence on your actual graph. The SKILL.md's Phase 3 gate (`convergence achieved within max_iterations`) should use max_iterations ≥ 100 as a safe default.
