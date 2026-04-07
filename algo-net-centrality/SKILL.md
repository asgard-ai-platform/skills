---
name: "algo-net-centrality"
description: "Calculate network centrality metrics to identify important nodes in graphs. Use this skill when the user needs to find key influencers, critical infrastructure nodes, or central actors in a network — even if they say 'who is most important in this network', 'key nodes', or 'network influence measurement'."
metadata:
  category: "WP-46 網絡演算法"
  tags: ["network", "centrality", "graph-analysis", "social-network"]
---

# Network Centrality Metrics

## Overview

Centrality measures quantify node importance in a network. Four classical metrics: degree (connections), betweenness (bridge role), closeness (proximity), eigenvector (connection quality). Each captures a different aspect of importance. Complexity ranges from O(V+E) for degree to O(V×E) for betweenness.

## When to Use

**Trigger conditions:**
- Identifying key influencers or critical nodes in social/organizational networks
- Analyzing network vulnerabilities (which node failure causes most damage)
- Comparing node importance across different dimensions

**When NOT to use:**
- For group/community detection (use community detection algorithms)
- For information spread modeling (use epidemic models)

## Algorithm

```
IRON LAW: Different Centrality Metrics Answer DIFFERENT Questions
- Degree: Who has the most connections? (popularity)
- Betweenness: Who bridges communities? (brokerage)
- Closeness: Who can reach everyone fastest? (efficiency)
- Eigenvector: Who is connected to important people? (prestige)
Using the WRONG metric answers the WRONG question. Choose based on
what "important" means in your context.
```

### Phase 1: Input Validation
Build network graph from edge list or adjacency matrix. Determine: directed vs undirected, weighted vs unweighted, connected vs disconnected.
**Gate:** Graph is well-formed, largest connected component identified.

### Phase 2: Core Algorithm
1. **Degree centrality:** C_D(v) = deg(v) / (N-1). O(V+E).
2. **Betweenness centrality:** C_B(v) = Σ(σ_st(v) / σ_st) for all s,t pairs. Fraction of shortest paths through v. O(V×E).
3. **Closeness centrality:** C_C(v) = (N-1) / Σd(v,u). Inverse of average shortest path. O(V×(V+E)).
4. **Eigenvector centrality:** Score proportional to sum of neighbors' scores. Power iteration until convergence. O(k×E).

### Phase 3: Verification
Check: centrality values normalized [0,1]. Top nodes by each metric may differ — this is expected and informative. Sanity check top-5 against domain knowledge.
**Gate:** All metrics computed, top nodes make intuitive sense.

### Phase 4: Output
Return centrality scores with multi-metric comparison.

## Output Format

```json
{
  "centralities": [{"node": "Alice", "degree": 0.85, "betweenness": 0.42, "closeness": 0.71, "eigenvector": 0.90}],
  "metadata": {"nodes": 500, "edges": 2000, "directed": false, "connected_components": 1}
}
```

## Examples

### Sample I/O
**Input:** 5-node undirected graph (bridge topology): edges = {(A,B), (A,C), (B,C), (C,D), (D,E)}
```
    A --- B
     \  /
      C
      |
      D --- E
```

**Expected centralities (normalized by N-1 = 4):**

| Node | Degree | Betweenness | Closeness | Eigenvector |
|------|--------|-------------|-----------|-------------|
| A | 0.50 (2/4) | 0.000 | 0.571 (4/7) | 0.452 |
| B | 0.50 (2/4) | 0.000 | 0.571 (4/7) | 0.452 |
| **C** | **0.75 (3/4)** | **0.667** | **0.800 (4/5)** | **0.628** |
| D | 0.50 (2/4) | 0.500 | 0.667 (4/6) | 0.386 |
| E | 0.25 (1/4) | 0.000 | 0.500 (4/8) | 0.201 |

Verify: **C is the bridge** — highest in ALL four metrics. E is the periphery — lowest in all metrics. A and B are symmetric (identical scores). D has nonzero betweenness (bridges C to E) but lower degree than C.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Star graph | Center has max all centralities | Hub dominates in all metrics |
| Disconnected graph | Closeness undefined for disconnected pairs | Use harmonic centrality instead |
| Directed graph | In-degree ≠ out-degree centrality | Popularity (in) vs activity (out) |

## Gotchas

- **Disconnected graphs**: Closeness centrality is undefined when nodes can't reach each other. Use harmonic centrality: C_H(v) = Σ(1/d(v,u)) as an alternative.
- **Scale dependence**: Raw centrality values depend on network size. Use normalized versions for cross-network comparison.
- **Betweenness is expensive**: O(V×E) makes it impractical for very large networks (millions of nodes). Use approximation algorithms (random sampling of shortest paths).
- **Dynamic networks**: Centrality in a snapshot may not reflect influence over time. Temporal centrality metrics exist but are more complex.
- **Correlation between metrics**: In many real networks, centrality metrics are correlated. But the DIFFERENCES are often the most informative (high degree but low betweenness = local hub, not broker).

## References

- For centrality metric comparison framework, see `references/metric-comparison.md`
- For approximate betweenness algorithms, see `references/approximate-betweenness.md`
