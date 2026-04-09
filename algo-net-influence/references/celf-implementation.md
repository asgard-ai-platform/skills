# CELF Implementation

## Why CELF Exists

Naive greedy influence maximization evaluates the marginal gain of every candidate node at every round. With `n` nodes, `k` seeds, and `R` Monte Carlo runs, the cost is:

```
O(k × n × R) simulations
```

At `n=10,000`, `k=20`, `R=10,000`: **2 billion simulations**. CELF reduces this by exploiting **submodularity**.

### Submodularity Guarantee

A function `f` is submodular if for any sets A ⊆ B and any element v ∉ B:

```
f(A ∪ {v}) - f(A)  ≥  f(B ∪ {v}) - f(B)
```

In plain terms: the marginal gain of adding node `v` to a **smaller** seed set is always **at least as large** as adding it to a **larger** seed set. Influence spread `σ(S)` satisfies this property under both IC and LT models.

**Consequence for CELF**: A node's marginal gain computed in round `t` is an **upper bound** on its marginal gain in any future round `t' > t`. If the upper bound is less than the best current candidate's gain, this node cannot win — skip re-evaluation.

---

## The CELF Algorithm

### Data Structure

Each candidate node maintains a tuple in a max-heap:

```
(marginal_gain, node_id, last_updated_round)
```

`last_updated_round` records which greedy round produced the stored `marginal_gain`.

### Pseudocode

```
CELF(G, k, R):
    S = {}                          # seed set
    heap = max-heap, keyed by marginal_gain

    # Round 0: compute σ({v}) for all nodes
    for each node v in G:
        gain = monte_carlo(G, {v}, R)
        heap.push( (gain, v, round=0) )

    for round in 1..k:
        while True:
            (gain, v, last_round) = heap.peek()

            if last_round == round:          # gain is current → take it
                heap.pop()
                S = S ∪ {v}
                break

            # gain is stale → recompute marginal gain
            new_gain = monte_carlo(G, S ∪ {v}, R) - sigma(S)
            heap.update(v, new_gain, round)  # re-insert with fresh gain

    return S, sigma(S)
```

**Key invariant**: a node is selected only when its stored gain was computed **this round** (meaning no cheaper recomputation could improve it).

---

## Worked Example (5 Nodes)

Network: nodes {A, B, C, D, E}, IC model, p=0.5 per edge.

True spread values (from exhaustive enumeration, small graph):

| Seed set | σ(S) |
|---|---|
| {A} | 3.2 |
| {B} | 2.8 |
| {C} | 2.1 |
| {D} | 1.9 |
| {E} | 1.5 |
| {A,B} | 4.0 |
| {A,C} | 4.5 |
| {A,B,C} | 5.1 |

**Goal**: select k=2 seeds.

### Round 1 (initialization)

Compute `σ({v})` for all nodes:

```
heap = [(3.2, A, r=0), (2.8, B, r=0), (2.1, C, r=0), (1.9, D, r=0), (1.5, E, r=0)]
```

Peek: `(3.2, A, r=0)`. Round is 1 but `last_round=0` — stale? **No** — in round 1, `last_round=0` means "never updated". Greedy implementations handle this by treating round 1 initialization as `last_round = current_round`. Let's use `last_round=1` after initialization.

Re-stating with corrected convention (`last_round` initialized to current round):

```
# After round 1 init, all nodes have last_round=1
heap = [(3.2, A, r=1), (2.8, B, r=1), (2.1, C, r=1), (1.9, D, r=1), (1.5, E, r=1)]
```

Peek: `(3.2, A, r=1)`. `last_round == 1` → **select A**. S = {A}, σ(S) = 3.2.

### Round 2

heap = [(2.8, B, r=1), (2.1, C, r=1), (1.9, D, r=1), (1.5, E, r=1)]

Peek: `(2.8, B, r=1)`. `last_round=1 ≠ 2` → recompute.

```
new_gain(B) = σ({A,B}) - σ({A}) = 4.0 - 3.2 = 0.8
heap.update(B, 0.8, r=2)
```

heap = [(2.1, C, r=1), (1.9, D, r=1), (1.5, E, r=1), (0.8, B, r=2)]

Peek: `(2.1, C, r=1)`. Stale → recompute.

```
new_gain(C) = σ({A,C}) - σ({A}) = 4.5 - 3.2 = 1.3
heap.update(C, 1.3, r=2)
```

heap = [(1.9, D, r=1), (1.5, E, r=1), (1.3, C, r=2), (0.8, B, r=2)]

Peek: `(1.9, D, r=1)`. Stale → recompute.

```
new_gain(D) = σ({A,D}) - σ({A}) = 3.6 - 3.2 = 0.4
heap.update(D, 0.4, r=2)
```

heap = [(1.5, E, r=1), (1.3, C, r=2), (0.8, B, r=2), (0.4, D, r=2)]

Peek: `(1.5, E, r=1)`. Stale → recompute.

```
new_gain(E) = σ({A,E}) - σ({A}) = 3.4 - 3.2 = 0.2
heap.update(E, 0.2, r=2)
```

heap = [(1.3, C, r=2), (0.8, B, r=2), (0.4, D, r=2), (0.2, E, r=2)]

Peek: `(1.3, C, r=2)`. `last_round == 2` → **select C**. S = {A, C}, σ(S) = 4.5.

**Result**: seeds = {A, C}, spread = 4.5. Only 1+4=5 re-evaluations in round 2, versus 4 full evaluations with naive greedy. The savings scale dramatically with `n`.

---

## Monte Carlo Simulation for σ(S)

```python
import random

def monte_carlo(graph, seed_set, R=10_000):
    """
    Estimate σ(S) under Independent Cascade.
    graph: dict {node: [(neighbor, probability), ...]}
    seed_set: set of seed nodes
    Returns: float, mean spread over R trials
    """
    total = 0
    for _ in range(R):
        active = set(seed_set)
        queue = list(seed_set)
        while queue:
            node = queue.pop()
            for neighbor, prob in graph[node]:
                if neighbor not in active and random.random() < prob:
                    active.add(neighbor)
                    queue.append(neighbor)
        total += len(active)
    return total / R
```

**Variance note**: with R=1,000 and spread ~500 on a 10K-node graph, the 95% confidence interval is roughly ±15 nodes (~3%). With R=10,000 it narrows to ±5 nodes (~1%). Use R≥10,000 when marginal gains between top candidates are close.

---

## Full Python Implementation

```python
import heapq
import random
from collections import defaultdict

def celf(graph, k, R=10_000):
    """
    CELF greedy influence maximization under Independent Cascade.

    Parameters
    ----------
    graph : dict[node, list[(neighbor, prob)]]
        Adjacency list with edge propagation probabilities.
    k : int
        Number of seeds to select.
    R : int
        Monte Carlo simulation runs for spread estimation.

    Returns
    -------
    seeds : list[node]  (in selection order)
    expected_spread : float
    marginal_gains : list[float]
    """
    nodes = list(graph.keys())
    seeds = []
    seed_set = set()
    current_spread = 0.0
    marginal_gains = []

    # Max-heap stored as negated gains (Python heapq is min-heap)
    # Entry: (-gain, node, last_round)
    heap = []

    # Round 1: initialize all marginal gains
    for v in nodes:
        gain = monte_carlo(graph, {v}, R)
        heapq.heappush(heap, (-gain, v, 1))

    for current_round in range(1, k + 1):
        while True:
            neg_gain, v, last_round = heapq.heappop(heap)

            if last_round == current_round:
                # Gain is fresh — select this node
                seeds.append(v)
                seed_set.add(v)
                actual_gain = -neg_gain
                marginal_gains.append(actual_gain)
                current_spread += actual_gain
                break

            # Stale: recompute marginal gain
            new_spread = monte_carlo(graph, seed_set | {v}, R)
            new_gain = new_spread - current_spread
            heapq.heappush(heap, (-new_gain, v, current_round))

    return seeds, current_spread, marginal_gains


def monte_carlo(graph, seed_set, R):
    total = 0
    for _ in range(R):
        active = set(seed_set)
        frontier = list(seed_set)
        while frontier:
            node = frontier.pop()
            for neighbor, prob in graph.get(node, []):
                if neighbor not in active and random.random() < prob:
                    active.add(neighbor)
                    frontier.append(neighbor)
        total += len(active)
    return total / R
```

### Usage

```python
# Build graph: {node: [(neighbor, prob), ...]}
g = {
    "A": [("B", 0.4), ("C", 0.3)],
    "B": [("D", 0.5), ("E", 0.2)],
    "C": [("E", 0.6)],
    "D": [],
    "E": [],
}

seeds, spread, gains = celf(g, k=2, R=10_000)
print(f"Seeds: {seeds}")
print(f"Expected spread: {spread:.1f}")
print(f"Marginal gains: {gains}")
```

---

## CELF++ Extension

CELF++ (Goyal et al., 2011) adds one further optimization: during the **previous round's** winner evaluation, record the **second-best** candidate's gain as a byproduct. This avoids one Monte Carlo call per round.

The gain: ~35% additional speedup over CELF on typical social networks. The complexity: maintaining a `prev_best` pointer per heap entry.

**Practical verdict**: CELF is sufficient for most deployments. Implement CELF++ only when profiling shows Monte Carlo calls dominate runtime and you need the final 35%.

---

## Tuning R: Monte Carlo Run Count

| Network size | Recommended R | Rationale |
|---|---|---|
| < 1,000 nodes | 1,000 | Variance low due to small spread |
| 1,000–50,000 | 10,000 | Standard; ~1% CI on spread estimates |
| 50,000–500,000 | 10,000 with variance check | Increase if top-2 gains within 5% of each other |
| > 500,000 | Switch to IMM/TIM+ | CELF too slow; use sketch-based methods |

**Variance check heuristic**: after each round, if `|gain_1 - gain_2| / gain_1 < 0.05`, double R for that round only.

---

## Complexity Summary

| Algorithm | Simulations | Speedup vs Naive |
|---|---|---|
| Naive greedy | O(k × n × R) | 1× |
| CELF | O(k × n' × R), n' ≪ n | ~700× (empirical) |
| CELF++ | Slightly fewer MC calls than CELF | ~35% over CELF |

The 700× figure (Leskovec et al., 2007) was measured on a 15K-node LiveJournal graph with k=50. Real speedup depends on graph structure: dense, uniform graphs benefit less; skewed degree distributions benefit more because the heap quickly identifies a small set of competitive candidates.

---

## Common Bugs

**Bug 1: comparing gains across rounds without re-evaluation**
```python
# WRONG: selecting v because its old gain looks best
if heap[0].gain > best_so_far:
    select(heap[0].node)  # gain may be from round 1
```
Always check `last_round == current_round` before selecting.

**Bug 2: σ(S) recomputed from scratch each time**
```python
# SLOW: re-simulating entire seed set spread
new_gain = monte_carlo(graph, seed_set | {v}, R) - monte_carlo(graph, seed_set, R)
```
Cache `current_spread` and update incrementally: `new_gain = monte_carlo(graph, seed_set | {v}, R) - current_spread`.

**Bug 3: directed vs undirected edges**

IC propagation follows **directed** edges. If your adjacency list treats edges as undirected, you will overestimate spread for nodes adjacent to high-in-degree hubs.

**Bug 4: heap ties broken arbitrarily**

Python's heap breaks ties by the second element (node id). If node ids are non-comparable types (e.g., strings vs ints), add a tie-break counter:

```python
heapq.heappush(heap, (-gain, counter, v, last_round))
counter += 1
```
