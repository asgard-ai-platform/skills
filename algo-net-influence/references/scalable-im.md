# Scalable Influence Maximization: Sketch-Based Methods

When the network exceeds ~100K nodes, CELF becomes impractical: 10,000 Monte Carlo simulations × greedy iterations × graph traversal cannot finish in reasonable time. Sketch-based methods replace simulation with precomputed random structures, reducing complexity from O(k·n·R·m) to near-linear.

---

## Why CELF Breaks at Scale

CELF complexity per greedy iteration:

```
O(R × m)    where R = Monte Carlo runs, m = number of edges
```

For a 10M-node social graph with average degree 20 (m = 200M edges), k = 50 seeds, R = 10,000:

```
50 iterations × 10,000 simulations × 200M edge traversals
= 100 trillion operations (impractical)
```

Sketch methods achieve:

```
O((k + l)(m + n) × log n / ε²)    for IMM
```

where ε is approximation error tolerance and l is a confidence parameter. For the same graph with ε = 0.1, l = 1, this is roughly 10⁹ — four orders of magnitude faster.

---

## Reverse Reachable (RR) Sets: The Core Primitive

All modern scalable algorithms (TIM, TIM+, IMM, OPIM) are built on **Reverse Reachable sets**.

### Definition

For a directed graph G and diffusion model (IC or LT), a **Random RR set** for node v is constructed by:

1. Sample a random "possible world" graph G' by including each edge independently with its propagation probability p(u→v)
2. In G', find all nodes that can reach v via a directed path
3. That set is one RR set rooted at v

Formally: `RR(v) = {u : u can reach v in G'}`

### Why This Works

**Key theorem** (Borgs et al. 2014): Node u covers RR set `RR(v)` if and only if seeding u would cause v to be influenced in that possible world.

Therefore:
- The fraction of RR sets covered by a seed set S equals S's expected spread, normalized by n
- **Expected spread(S) = n × (# RR sets covered by at least one node in S) / (total RR sets)**

Greedy maximum coverage on RR sets → greedy influence maximization, but computed over a static collection rather than repeated simulation.

---

## IMM Algorithm (Influence Maximization via Martingales)

IMM (Tang et al. 2015) is the current practical standard. It achieves (1−1/e−ε) approximation with probability at least 1−n^(−l).

### Step 1: Estimate Required RR Set Count

```python
def estimate_theta(n, k, epsilon, l):
    """
    n: number of nodes
    k: seed set size
    epsilon: approximation error (e.g., 0.1 = 10% error)
    l: confidence parameter (e.g., 1 for 1 - 1/n failure prob)
    """
    alpha = sqrt(l * log(n) + log(2))
    beta  = sqrt((1 - 1/e) * (log(comb(n, k)) + l * log(n) + log(2)))
    # lower bound on optimal spread (OPT_guess from sampling)
    # Final theta computed after Phase 1 estimation
    return alpha, beta
```

IMM uses a two-phase approach so it doesn't need to know OPT (optimal spread) in advance.

### Step 2: Phase 1 — Estimate OPT

```python
def phase1_estimate_opt(G, k, epsilon, l):
    """Returns lower bound estimate of OPT."""
    n = len(G.nodes)
    rr_sets = []
    
    for i in range(1, int(log2(n))):
        # Sample 6(l log n + log log2 n)(2^i) RR sets
        x = (6 * (l * log(n) + log(log2(n))) * (2**i))
        while len(rr_sets) < x:
            v = random.choice(G.nodes)
            rr_sets.append(generate_rr_set(G, v))
        
        # Check if greedy covers enough
        seeds, coverage = greedy_max_coverage(rr_sets, k)
        fraction = coverage / len(rr_sets)
        
        if fraction >= (1 - 1/e) / (2**i):
            opt_prime = fraction * n / (1 + epsilon)
            return opt_prime, rr_sets
    
    return n / (2 * log2(n)), rr_sets
```

### Step 3: Phase 2 — Generate Final RR Sets

```python
def imm(G, k, epsilon=0.1, l=1):
    n = len(G.nodes)
    opt_prime, rr_sets = phase1_estimate_opt(G, k, epsilon, l)
    
    alpha = sqrt(l * log(n) + log(2))
    beta  = sqrt((1 - 1/e) * (log(comb(n, k)) + l * log(n) + log(2)))
    
    # Final RR set count
    theta = (2 + 2/3 * epsilon) * (alpha + beta)**2 * n / (epsilon**2 * opt_prime)
    
    # Generate remaining RR sets
    while len(rr_sets) < theta:
        v = random.choice(G.nodes)
        rr_sets.append(generate_rr_set(G, v))
    
    # Greedy max coverage
    seeds, _ = greedy_max_coverage(rr_sets, k)
    return seeds
```

### Generating One RR Set (IC Model)

```python
def generate_rr_set_ic(G, root):
    """
    Reverse BFS from root in a sampled possible world.
    G: directed graph with edge attr 'prob'
    root: target node
    Returns: set of nodes that can reach root
    """
    visited = {root}
    queue = deque([root])
    
    while queue:
        v = queue.popleft()
        for u in G.predecessors(v):          # walk edges BACKWARDS
            if u not in visited:
                p = G[u][v].get('prob', 0.1)
                if random.random() < p:       # edge included in possible world?
                    visited.add(u)
                    queue.append(u)
    
    return visited
```

**LT model variant**: instead of probabilistic edge traversal, randomly select one in-neighbor per node (with probability proportional to edge weight) and follow that single edge backwards.

---

## Greedy Maximum Coverage on RR Sets

```python
def greedy_max_coverage(rr_sets, k):
    """
    Standard greedy set cover on RR sets.
    Returns (seed_list, number_of_covered_rr_sets)
    """
    # Build inverted index: node → list of RR set indices it appears in
    node_to_rr = defaultdict(set)
    for i, rr in enumerate(rr_sets):
        for node in rr:
            node_to_rr[node].add(i)
    
    seeds = []
    covered = set()
    
    for _ in range(k):
        # Select node covering most uncovered RR sets
        best_node = max(node_to_rr.keys(),
                        key=lambda u: len(node_to_rr[u] - covered))
        seeds.append(best_node)
        covered |= node_to_rr[best_node]
        
        # Remove covered RR sets from index (lazy delete is fine)
        del node_to_rr[best_node]
    
    return seeds, len(covered)
```

Expected spread estimate from result:

```python
expected_spread = len(G.nodes) * len(covered) / len(rr_sets)
```

---

## Parameter Selection Guide

### Choosing ε (Approximation Error)

| ε | Approximation | RR sets needed | Use when |
|---|--------------|----------------|----------|
| 0.5 | ≥ 33% of optimal | ~10K–100K | Exploratory, fast runs |
| 0.1 | ≥ 57% of optimal | ~1M–10M | Standard production |
| 0.05 | ≥ 60% of optimal | ~4M–40M | High-stakes campaigns |
| 0.01 | ≥ 62% of optimal | ~100M+ | Academic benchmarking only |

The (1−1/e) ≈ 63% guarantee is the ceiling for any polynomial-time algorithm (unless P=NP). ε = 0.1 captures ~90% of that ceiling.

### Choosing l (Confidence)

Failure probability = n^(−l). For:
- n = 1M nodes, l = 1 → failure probability 10^(−6) (one-in-a-million)
- l = 1 is the standard default in all papers

### Memory Budget

Each RR set stores a variable-length node list. Empirically, average RR set size ≈ expected spread / n × n = expected spread nodes. If expected spread = 1000 and n = 1M:
- Average RR set: ~1000 nodes
- 1M RR sets × 1000 nodes × 8 bytes = 8GB RAM

**Practical limit**: For graphs with high spread, cap RR sets at ~500K–1M and accept slightly higher ε.

---

## Worked Example: 1M-Node Graph

**Setup:**
- n = 1,000,000 nodes
- m = 5,000,000 edges (avg degree 5)
- k = 20 seeds
- IC model, uniform p = 0.01
- ε = 0.1, l = 1

**Expected spread estimate:**
At p=0.01 with avg degree 5, mean cascade from single node ≈ 1/(1-5×0.01) = 1/0.95 ≈ 1.05 (near-zero spread). This is a subcritical network — seeds matter less.

Increase p = 0.05: mean cascade ≈ 1/(1-5×0.05) = 1/0.75 ≈ 4 nodes per seed, expected spread of 20 seeds ≈ 60–200 (depends on overlap).

**IMM runtime estimate:**
- Phase 1: generates ~log₂(n) = 20 batches, each up to ~6 × log(n) × 2^i RR sets → total ~500K RR sets
- Phase 2: θ ≈ 2M RR sets (typical for these parameters)
- RR set generation: 2M sets × avg 4 nodes/set × edge traversal → ~50M operations
- Wall time: ~5–30 seconds on a single machine (Python), <1s (C++)

---

## Comparison: IMM vs TIM+

Both achieve the same theoretical guarantee. Key practical differences:

| | TIM+ | IMM |
|--|------|-----|
| Phase 1 approach | Sampling-based OPT estimation | Martingale-based stopping criterion |
| Tightness | Can over-generate RR sets | Tighter bound (fewer RR sets on average) |
| Implementation complexity | Moderate | Slightly higher |
| Recommended | Legacy codebases | New implementations |

IMM generates 36%–50% fewer RR sets than TIM+ on average benchmarks. Prefer IMM.

---

## When IMM Is Still Too Slow

For billion-node graphs (Twitter-scale), further approximations exist:

**OPIM (One-Phase IMM):** removes the two-phase structure, better cache efficiency. ~2× faster than IMM with same guarantee.

**Sketch-based streaming:** precompute RR sets offline, update incrementally as edges change. Necessary for dynamic graphs.

**Sampling on ego-nets:** if the graph has community structure, run IMM independently per community and merge. Loses global optimality but scales to any size.

**Rule of thumb for choosing method:**

```
n < 100K:        CELF (exact, manageable)
100K < n < 10M:  IMM with ε=0.1
10M < n < 1B:    OPIM or distributed IMM (e.g., on Spark)
n > 1B:          Community-partitioned or streaming sketch
```

---

## Common Implementation Bugs

**Wrong edge direction in RR set generation**: RR sets traverse edges *backwards* (from target to potential influencers). Using forward traversal produces incorrect results that look plausible but systematically underperform.

**Reusing RR sets across seeds**: Each call to IMM must generate a *fresh* independent collection of RR sets. Reusing the same sets for a different k is statistically invalid.

**Forgetting the n multiplier**: Expected spread = `n × coverage_fraction`, not just `coverage_fraction`. Off by a factor of n is a common silent bug.

**Uniform vs weighted probability**: If your graph has heterogeneous edge weights, `generate_rr_set` must use per-edge probabilities. A single global `p` is a simplification that breaks when edge weights vary by 10×+.

**Undirected graphs**: In undirected graphs, each undirected edge becomes two directed edges in the RR traversal. Do not traverse an undirected edge in both directions in a single RR set construction — this double-counts and inflates spread estimates.
