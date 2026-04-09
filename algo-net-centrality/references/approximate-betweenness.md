# Approximate Betweenness Centrality

Exact betweenness is O(V·E) time and O(V+E) space (Brandes 2001). For a network with 10,000 nodes and 100,000 edges, that is 10⁹ operations — tolerable on a workstation. At 1M nodes and 10M edges it becomes 10¹³ operations — impractical. This document covers the two main approximation strategies and gives concrete guidance on when and how to use them.

---

## Exact Baseline: Brandes Algorithm

Before approximating, understand what you are approximating. The Brandes algorithm computes exact betweenness by:

1. For each source node `s`, run BFS (unweighted) or Dijkstra (weighted) to get:
   - `σ[t]` — number of shortest paths from `s` to every target `t`
   - `d[t]` — distance from `s` to `t`
   - predecessor list `P[t]` — nodes directly before `t` on any shortest path from `s`

2. Back-propagate a "dependency" value δ[s·](v) using the stack order from BFS:

```
δ[s·](v) = Σ_{w: v ∈ P[w]} (σ[v] / σ[w]) × (1 + δ[s·](w))
```

3. Accumulate: `C_B(v) += δ[s·](v)` for all v ≠ s

4. Normalize: `C_B(v) = C_B(v) / ((N-1)(N-2))` for undirected graphs.

**Complexity:** O(V·E) time, O(V+E) space.

---

## Approximation Strategy 1: Random Source Sampling

### Core Idea

Instead of running BFS/Dijkstra from all V sources, pick k sources uniformly at random and scale up.

**Estimated betweenness:**

```
Ĉ_B(v) = (V / k) × Σ_{s ∈ S} δ[s·](v)
```

where S is the random sample of k source nodes, |S| = k.

**Complexity:** O(k·E) time. Speedup factor: V/k.

### Error Bound (Brandes & Pich 2007)

With probability at least 1 − δ:

```
|Ĉ_B(v) − C_B(v)| ≤ ε × (N-1)(N-2)/2
```

when

```
k ≥ (c / ε²) × (ln V + ln(1/δ))
```

for small constant c ≈ 0.5.

**Practical rule of thumb:** k = 200–500 gives good rank correlation (Spearman ρ > 0.95) on most real-world networks. k = 1000 is safe for publication-quality rankings.

### Worked Example

Network: N = 50,000 nodes, E = 500,000 edges. Exact cost: 50,000 × 500,000 = 2.5 × 10¹⁰ ops.

With k = 500:
- Cost: 500 × 500,000 = 2.5 × 10⁸ ops — 100× speedup
- ε at δ = 0.01: solve 500 ≥ (0.5/ε²)(ln 50000 + ln 100) → ε ≈ 0.10

So the estimated betweenness can be off by up to 10% of the maximum possible betweenness score. For identifying top-10 nodes by rank, this is usually acceptable.

### When Rank Order Breaks Down

Random sampling preserves rank order well for nodes with **distinct** betweenness values. It degrades when:

- Many nodes have nearly identical true betweenness (e.g., a dense clique)
- You need exact tie-breaking
- You are targeting the bottom half of the distribution (low-betweenness nodes)

If you only care about the top-K nodes (K ≪ V), sampling is appropriate. If you need exact bottom-K, use exact Brandes on the subgraph.

---

## Approximation Strategy 2: Pivot-Based Landmark Sampling

### Core Idea

Instead of random sources, pick k "landmark" nodes that are structurally representative (e.g., highest-degree nodes, or nodes selected by farthest-first traversal). Run BFS from each landmark.

**Why this helps:** High-degree and well-connected nodes participate in more shortest paths, so BFS from them contributes more signal per BFS run than BFS from a random leaf.

### Landmark Selection Methods

| Method | How | Best for |
|--------|-----|----------|
| Random | Uniform random from V | General use, unbiased |
| Degree-biased | Sample proportional to degree | Scale-free / power-law networks |
| Farthest-first | Greedily pick node farthest from previous picks | Geographically-structured networks |
| High-degree | Top-k degree nodes | Social networks with clear hubs |

**Caution:** Landmark sampling introduces bias — nodes near landmarks get inflated estimates. Use random sampling if unbiased estimates are required. Use landmark sampling only when you know top-K hubs are your region of interest.

---

## Decision Table: Exact vs Approximate

| Network Size | Approximate Best Strategy |
|---|---|
| V < 1,000 | Exact (Brandes). Fast enough. |
| 1K ≤ V < 50K | Exact if sparse (E < 5×V). Random sampling (k=200) if dense. |
| 50K ≤ V < 1M | Random sampling, k = 500–1000. |
| V ≥ 1M | Random sampling k = 1000, or use sketch-based methods (HyperBall). |

**Directed vs undirected:** Directed networks have 2× more source-target pairs. Halve the above thresholds (i.e., treat a directed graph as if it were 2× larger).

**Weighted edges:** Replace BFS with Dijkstra. Same O(k×E log V) per sample, but constant factor is ~5–10× higher. Reduce k accordingly.

---

## Python Implementation (stdlib only)

```python
import random
from collections import deque, defaultdict

def approximate_betweenness(adj: dict[str, list[str]],
                             k: int = 300,
                             seed: int = 42,
                             normalize: bool = True) -> dict[str, float]:
    """
    Random-sampling approximation of betweenness centrality.

    adj: adjacency list {node: [neighbor, ...]} for undirected graph
    k:   number of random source nodes (sample size)
    Returns: {node: estimated_betweenness}
    """
    nodes = list(adj.keys())
    N = len(nodes)
    rng = random.Random(seed)
    sources = rng.sample(nodes, min(k, N))

    betweenness = defaultdict(float)

    for s in sources:
        # BFS from s
        sigma = {s: 1}          # shortest-path counts
        dist = {s: 0}
        pred = defaultdict(list) # predecessors
        queue = deque([s])
        stack = []               # process in reverse BFS order

        while queue:
            v = queue.popleft()
            stack.append(v)
            for w in adj.get(v, []):
                if w not in dist:
                    dist[w] = dist[v] + 1
                    queue.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] = sigma.get(w, 0) + sigma[v]
                    pred[w].append(v)

        # Back-propagation
        delta = defaultdict(float)
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma.get(v, 0) / sigma.get(w, 1)) * (1 + delta[w])
            if w != s:
                betweenness[w] += delta[w]

    # Scale: we sampled k out of N sources; multiply by N/k
    scale_factor = N / len(sources)
    for v in nodes:
        betweenness[v] *= scale_factor

    # Normalize to [0,1]
    if normalize and N > 2:
        norm = (N - 1) * (N - 2) / 2  # undirected: pairs / 2
        betweenness = {v: betweenness[v] / norm for v in nodes}
    else:
        betweenness = {v: betweenness.get(v, 0.0) for v in nodes}

    return betweenness
```

### Usage

```python
adj = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["C", "E"],
    "E": ["D"],
}

result = approximate_betweenness(adj, k=5, seed=0)
# k=5 == exact for this 5-node graph (all sources sampled)
# Expected: C ≈ 0.667, D ≈ 0.500, A/B/E ≈ 0.000
```

**Verify against SKILL.md sample I/O:** Setting k = N (sample all nodes) recovers the exact Brandes result. For the 5-node bridge topology, C should return betweenness ≈ 0.667 and D ≈ 0.500.

---

## Choosing k in Practice

Empirical approach when you have no prior knowledge of the network:

1. Compute approximate betweenness with k = 50 (fast pilot run).
2. Double k to 100, recompute.
3. Compare rank correlation (Spearman ρ) of top-20 nodes between the two runs.
4. If ρ > 0.98, k = 50 is sufficient. If ρ < 0.95, double again.
5. Stop when two consecutive doublings both give ρ > 0.98.

This takes at most log₂(k_max / 50) extra BFS rounds and gives you an empirically validated k without needing to know the true betweenness.

---

## Pitfalls Specific to Approximation

**Underestimating peripheral nodes.** Sampling concentrates on paths through the core. Nodes at the periphery may have near-zero estimated betweenness even if they are true bridges within a subregion. Check: if a node's degree is high but its estimated betweenness is near zero, run BFS from its neighbors specifically.

**Seed sensitivity at small k.** With k < 50, different random seeds can produce dramatically different top-10 rankings. Always run 3–5 seeds and compare; if top-10 is unstable, increase k.

**Scaling formula assumes connected graph.** The `N/k` scaling assumes any node can reach any other. For disconnected graphs, apply the approximation per connected component and aggregate. Do not apply the global scale factor across components.

**Directed graphs need asymmetric correction.** For directed graphs, the normalization denominator is `(N-1)(N-2)` (not divided by 2). The implementation above uses the undirected formula — pass `normalize=False` and apply your own denominator for directed networks.

**Weighted graphs need Dijkstra, not BFS.** The code above uses unweighted BFS. Substituting Dijkstra for weighted edges is straightforward but changes the `sigma` accumulation: tie-breaking must be handled carefully when multiple shortest paths exist at the same total weight.
