---
name: "algo-net-community"
description: "Implement Louvain community detection to discover densely connected groups in networks. Use this skill when the user needs to find communities or clusters in social/organizational networks, segment customers by interaction patterns, or analyze network modular structure — even if they say 'find groups in this network', 'community detection', or 'network clustering'."
metadata:
  category: "WP-46 網絡演算法"
  tags: ["network", "community-detection", "louvain", "modularity"]
---

# Louvain Community Detection

## Overview

Louvain algorithm detects communities by optimizing modularity — the fraction of edges within communities minus expected fraction if edges were random. A greedy, hierarchical algorithm that runs in O(n log n) for sparse graphs. Produces a hierarchy of communities at multiple resolutions.

## When to Use

**Trigger conditions:**
- Discovering natural groupings in social, organizational, or interaction networks
- Segmenting users/customers by behavioral similarity
- Analyzing modular structure of complex networks

**When NOT to use:**
- For overlapping communities (use DEMON or BigCLAM)
- When communities are pre-defined and you're classifying nodes (use label propagation)

## Algorithm

```
IRON LAW: Modularity Has a RESOLUTION LIMIT
Louvain optimizes modularity, which has a known resolution limit
(Fortunato & Barthélemy, 2007): it cannot detect communities smaller
than √(2E) where E = total edges. In large networks, small but real
communities may be merged. Use multi-resolution methods or Leiden
algorithm (improved Louvain) for better results.
```

### Phase 1: Input Validation
Build undirected weighted graph from interaction data. Edge weights represent interaction strength (frequency, duration, volume).
**Gate:** Graph loaded, no isolated nodes (or decide how to handle them).

### Phase 2: Core Algorithm
**Phase 1 — Local moves:**
1. Assign each node to its own community
2. For each node, compute modularity gain of moving to each neighbor's community
3. Move node to community with maximum positive gain
4. Repeat until no beneficial moves remain

**Phase 2 — Aggregation:**
5. Build new graph where nodes = communities, edges = sum of inter-community edges
6. Repeat Phase 1 on the aggregated graph
7. Continue until modularity stops improving

### Phase 3: Verification
Check: modularity Q > 0 (non-trivial partitioning), community sizes are reasonable (not one giant + many singletons), manual inspection of sample communities.
**Gate:** Modularity positive, community sizes follow power-law-like distribution.

### Phase 4: Output
Return community assignments with modularity score.

## Output Format

```json
{
  "communities": [{"id": 0, "size": 45, "top_members": ["Alice", "Bob"], "internal_density": 0.35}],
  "summary": {"num_communities": 12, "modularity": 0.65, "largest": 120, "smallest": 5},
  "metadata": {"algorithm": "louvain", "nodes": 500, "edges": 2000}
}
```

## Examples

### Sample I/O
**Input:** Email network of 200 employees, weighted by email frequency
**Expected:** Communities roughly corresponding to departments/teams, modularity ~0.5-0.7.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Complete graph | One community or random split | No modular structure |
| Disconnected components | Each component = community | Natural separation |
| Weighted vs unweighted | Different communities | Weights change modularity calculation |

## Gotchas

- **Non-deterministic**: Node processing order affects results. Run multiple times and select the partition with highest modularity, or use Leiden algorithm (more stable).
- **Resolution parameter**: Standard Louvain uses γ=1 in modularity. Varying γ reveals communities at different scales. γ>1 finds smaller communities; γ<1 finds larger ones.
- **Leiden > Louvain**: Louvain can produce badly connected communities (communities where removing one node disconnects them). Leiden algorithm fixes this guarantee.
- **Temporal stability**: In dynamic networks, community assignments can change drastically between snapshots even when the network changes minimally. Use temporal smoothing.
- **Interpretation**: Community detection finds structure, but interpreting WHY nodes cluster requires domain knowledge. Don't over-interpret automatically detected communities.

## References

- For Leiden algorithm (improved Louvain), see `references/leiden.md`
- For multi-resolution community detection, see `references/multi-resolution.md`
