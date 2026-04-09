# Network-Based SIR Models

The standard SIR model assumes **homogeneous mixing**: every node contacts every other node with equal probability. Real social networks violate this in three ways that materially change spread dynamics:

1. **Degree heterogeneity** — a few hubs have orders-of-magnitude more connections than typical nodes
2. **Clustering** — your friends know each other, creating redundant exposure paths
3. **Community structure** — content must cross weak ties to jump between clusters

These are not minor corrections. For a power-law network (typical of social platforms), the effective epidemic threshold can drop to near zero, meaning even low-β content can go viral if seeded at the right nodes.

---

## Key Network Properties

| Property | Symbol | Effect on R0 | How to Estimate |
|----------|--------|-------------|-----------------|
| Mean degree | ⟨k⟩ | R0 ∝ ⟨k⟩ | Avg follower count in sample |
| Second moment of degree | ⟨k²⟩ | R0 ∝ ⟨k²⟩/⟨k⟩ | Variance + mean of degree dist |
| Clustering coefficient | C | Reduces effective β | Fraction of closed triangles |
| Assortativity | r | Hubs-to-hubs: amplifies; random: neutral | Degree correlation of connected pairs |

---

## Heterogeneous Mean-Field (HMF) Formulation

Rather than tracking S, I, R for the whole population, HMF groups nodes by degree k and tracks compartment fractions within each degree class.

### Variables

- S_k(t) — fraction of degree-k nodes that are Susceptible at time t
- I_k(t) — fraction of degree-k nodes that are Infected
- R_k(t) — fraction of degree-k nodes that are Recovered
- P(k) — degree distribution (probability a random node has degree k)
- Θ(t) — probability that a random edge points to an Infected node

### ODEs

```
dS_k/dt = -β k S_k Θ(t)
dI_k/dt =  β k S_k Θ(t) - γ I_k
dR_k/dt =  γ I_k
```

The coupling term Θ(t) links all degree classes:

```
Θ(t) = Σ_k [ k P(k) I_k(t) ] / ⟨k⟩
```

Θ is the probability that a randomly-chosen neighbor is currently infected. It weights by degree k because high-degree nodes appear more often as neighbors.

### Revised R0

The network-corrected basic reproduction number is:

```
R0_net = (β / γ) × (⟨k²⟩ / ⟨k⟩)
```

Compare to homogeneous SIR: `R0_hom = β N / γ`. The ratio `⟨k²⟩ / ⟨k⟩` is the **excess degree** — the expected number of additional neighbors you reach by following one edge.

For a Poisson (random) network: `⟨k²⟩ / ⟨k⟩ ≈ ⟨k⟩ + 1`, so HMF ≈ homogeneous.

For a power-law network P(k) ∝ k^(-α) with α ≤ 3: `⟨k²⟩` diverges (or is very large), so `R0_net ≫ R0_hom` — explaining why social platforms support viral spread at low per-contact β.

---

## Worked Example

### Setup

Suppose a meme spreads on a platform approximated by a truncated power-law degree distribution with:

- β = 0.05 (5% share probability per exposure)
- γ = 0.2 (average 5 days interested)
- ⟨k⟩ = 200 (average 200 followers)
- ⟨k²⟩ = 400,000 (variance dominated by a few large accounts)

### Homogeneous SIR estimate

```
R0_hom = β / γ = 0.05 / 0.2 = 0.25
```

Prediction: content dies out (R0 < 1). **Wrong.**

### Network-corrected estimate

```
⟨k²⟩ / ⟨k⟩ = 400,000 / 200 = 2000
R0_net = 0.25 × 2000 = 500
```

Prediction: explosive spread if seeded at even one hub. **Much closer to observed social media virality.**

### Why the gap is so large

The ratio `⟨k²⟩ / ⟨k⟩` = 2000 means the typical neighbor of a randomly-chosen person has 2000 connections. High-degree nodes are disproportionately represented as neighbors, acting as super-spreaders.

---

## Degree Distribution Profiles

Different platforms map to different degree distributions. Use the profile to select appropriate ⟨k²⟩/⟨k⟩ multiplier.

| Platform Type | Degree Distribution | ⟨k²⟩/⟨k⟩ Multiplier | Notes |
|--------------|---------------------|----------------------|-------|
| Twitter/X (public) | Power-law, α ≈ 2.1 | 500–5000 | Fat tail; hubs dominate |
| Facebook (friend graph) | Power-law, α ≈ 3.5 | 10–50 | Softer tail; more Poisson-like |
| LINE / WhatsApp groups | Near-regular | 2–5 | Group size bounded; HMF ≈ homogeneous |
| Reddit (subreddit) | Bimodal | 20–200 | Power users + lurkers |
| LinkedIn | Power-law, α ≈ 2.8 | 30–150 | Professional constraints on sharing |

For Taiwan-specific estimation, use PTT board structure (near-uniform board size, ~10k active users per popular board) and LINE group spread (bounded at 200–500).

---

## Epidemic Threshold on Networks

For HMF, the epidemic threshold condition is:

```
β/γ > ⟨k⟩ / ⟨k²⟩
```

This threshold drops toward zero as ⟨k²⟩ grows. For scale-free networks (α < 3), the threshold is effectively zero — any positive β/γ ratio produces eventual spread given enough time or a large enough seed.

**Implication for campaign design**: on platforms with fat-tailed degree distributions, the bottleneck is not R0 > 1. The bottleneck is time and seed placement. Content can have R0_net >> 1 but still not go viral if it never reaches a hub.

---

## Seed Placement Strategy

Given network structure, seeding matters more than content quality at low β.

### Expected reach comparison

Seeding strategies ranked by total eventual infected (all else equal):

1. **Hub seeding** — target top-k nodes by degree. Fastest ignition.
2. **Friend-of-friend sampling** — pick random edges, seed the higher-degree endpoint. Approximates hub seeding without needing global degree data.
3. **Community bridge seeding** — target nodes with high betweenness centrality. Best for crossing community boundaries.
4. **Random seeding** — baseline. Only effective if R0_net >> 1.

### Friend-of-friend sampling (practical implementation)

When you cannot observe the full network, this heuristic selects high-degree nodes without a degree list:

```python
def friend_of_friend_sample(adjacency_list, n_seeds):
    """
    adjacency_list: dict {node_id: [neighbor_ids]}
    Returns n_seeds nodes biased toward high-degree nodes.
    """
    import random
    seeds = set()
    nodes = list(adjacency_list.keys())
    while len(seeds) < n_seeds:
        # pick a random node, then a random neighbor
        probe = random.choice(nodes)
        if adjacency_list[probe]:
            candidate = random.choice(adjacency_list[probe])
            seeds.add(candidate)
    return list(seeds)
```

The neighbor is biased toward high-degree nodes because high-degree nodes appear more often as neighbors — exactly the same logic as the Θ(t) term in HMF.

---

## Clustering Correction

HMF ignores clustering. When C (clustering coefficient) is high, the same node receives multiple exposures from the same source through triangles. This **wastes exposures** and reduces effective β.

Corrected effective transmission rate:

```
β_eff ≈ β × (1 - C × I_local)
```

where I_local is the local infection density in the neighborhood. For practical use: if C > 0.3, multiply β by 0.6–0.8 when estimating R0_net. Facebook groups and LINE group chats typically have C > 0.4.

---

## Numerical Integration for HMF

When you have an empirical degree distribution (from a sample), discretize it into K degree bins and integrate:

```python
import numpy as np
from scipy.integrate import solve_ivp

def hmf_sir(beta, gamma, pk, ks, I0_frac=0.001):
    """
    beta: float, transmission rate
    gamma: float, recovery rate
    pk: array, P(k) for each degree class (sums to 1)
    ks: array, degree values corresponding to pk
    I0_frac: initial fraction infected (uniform across classes)
    """
    k_mean = np.dot(pk, ks)
    n = len(ks)

    # Initial conditions: [S_0,...,S_{K-1}, I_0,...,I_{K-1}, R_0,...,R_{K-1}]
    S0 = (1 - I0_frac) * np.ones(n)
    I0 = I0_frac * np.ones(n)
    R0 = np.zeros(n)
    y0 = np.concatenate([S0, I0, R0])

    def rhs(t, y):
        S = y[:n]; I = y[n:2*n]; R = y[2*n:]
        # Theta: prob random edge points to infected node
        theta = np.dot(ks * pk, I) / k_mean
        dS = -beta * ks * S * theta
        dI =  beta * ks * S * theta - gamma * I
        dR =  gamma * I
        return np.concatenate([dS, dI, dR])

    sol = solve_ivp(rhs, [0, 60], y0, dense_output=True, max_step=0.5)

    # Aggregate to population-level compartments
    t_vals = np.linspace(0, 60, 121)
    y_vals = sol.sol(t_vals)
    S_pop = np.dot(pk, y_vals[:n])
    I_pop = np.dot(pk, y_vals[n:2*n])
    R_pop = np.dot(pk, y_vals[2*n:])
    return t_vals, S_pop, I_pop, R_pop
```

**Conservation check** (maps to Phase 3 in SKILL.md):

```python
assert np.allclose(S_pop + I_pop + R_pop, 1.0, atol=1e-6), "Conservation violated"
```

---

## When to Use HMF vs. Homogeneous SIR

| Condition | Use Homogeneous SIR | Use HMF |
|-----------|--------------------|----|
| Platform is closed group (LINE, Slack) | ✓ | — |
| Degree distribution is roughly uniform | ✓ | — |
| Quick back-of-envelope estimate needed | ✓ | — |
| Platform has public follower graph (Twitter, IG) | — | ✓ |
| Seeding strategy matters | — | ✓ |
| β estimated at < 0.1 per contact | — | ✓ |
| Need to compare seeding at hubs vs. random | — | ✓ |

Homogeneous SIR systematically **underestimates** R0 on power-law networks. If SIR predicts R0 < 1 but historical data shows the content went viral, suspect degree heterogeneity before concluding the model parameters are wrong.

---

## Parameter Lookup Shortcuts

When empirical data is unavailable, use these starting-point estimates:

| Scenario | β | γ | ⟨k²⟩/⟨k⟩ | R0_net |
|----------|---|---|-----------|--------|
| Meme on Twitter, broad appeal | 0.03–0.08 | 0.15–0.30 | 500–2000 | 50–1000 |
| Brand campaign on Instagram | 0.01–0.04 | 0.20–0.40 | 50–300 | 2–60 |
| News article on Facebook | 0.02–0.06 | 0.10–0.25 | 20–80 | 6–48 |
| Viral video in LINE groups | 0.10–0.30 | 0.30–0.60 | 3–8 | 0.5–8 |
| Professional content on LinkedIn | 0.01–0.03 | 0.20–0.40 | 30–100 | 1.5–15 |

These are rough calibration anchors. Always fit β and γ to early observed spread when possible (see `references/parameter-fitting.md`).
