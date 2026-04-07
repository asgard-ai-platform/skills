---
name: "algo-seo-pagerank"
description: "Implement PageRank algorithm to compute web page importance scores using the random surfer model. Use this skill when the user needs to rank pages by link authority, build a simplified search ranking system, or understand how link structure determines page importance — even if they say 'which pages are most important', 'link analysis', or 'page authority score'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "pagerank", "graph-algorithm", "link-analysis"]
---

# PageRank Algorithm

## Overview

PageRank computes the importance of web pages by modeling a random surfer who follows links with probability d (damping factor) and jumps to a random page with probability 1-d. Converges in O(k * E) where k is iterations and E is number of edges.

## When to Use

**Trigger conditions:**
- Computing page importance from link graph structure
- Building link-based authority scoring systems
- Analyzing citation networks or any directed graph importance

**When NOT to use:**
- When you only need keyword relevance (use TF-IDF instead)
- When the graph is undirected or unweighted (consider centrality measures)

## Algorithm

```
IRON LAW: PageRank Convergence
- Damping factor d MUST be < 1 (typically 0.85)
- Without damping, rank sinks and spider traps break convergence
- Correctness invariant: sum of all PageRank values = 1.0
```

### Phase 1: Input Validation
Build adjacency list from link data. Verify: no self-loops counted, all nodes accounted for (including dangling nodes with no outlinks).
**Gate:** Graph is well-formed, dangling nodes identified.

### Phase 2: Core Algorithm
1. Initialize all N pages with PR = 1/N
2. For each iteration:
   - For each page p: PR(p) = (1-d)/N + d * Σ(PR(q)/L(q)) for all q linking to p
   - Distribute dangling node rank equally to all pages
3. Repeat until convergence (L1 norm change < ε, typically 1e-6)

### Phase 3: Verification
Check: all PR values sum to ~1.0. Compare top-k rankings against known authority pages.
**Gate:** |Σ PR - 1.0| < 0.001 and convergence achieved within max iterations.

### Phase 4: Output
Return sorted page scores with rank position.

## Output Format

```json
{
  "rankings": [{"page": "url", "score": 0.042, "rank": 1}],
  "metadata": {"nodes": 1000, "edges": 5000, "iterations": 45, "damping": 0.85, "converged": true}
}
```

## Examples

### Sample I/O
**Input:** Pages A→B, A→C, B→C, C→A (3 nodes, 4 edges, d=0.85)
**Expected Output:** C: 0.390, A: 0.327, B: 0.283 (approximate)

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Single node, no links | PR = 1.0 | Only node gets all rank |
| All nodes link to one | Target gets highest PR | Star topology concentrates rank |
| Dangling node (no outlinks) | Distribute its rank equally | Prevents rank leakage |

## Gotchas

- **Dangling nodes**: Pages with no outgoing links leak rank. Redistribute their rank equally across all pages each iteration.
- **Spider traps**: A group of pages that only link to each other accumulate rank. Damping factor prevents this but doesn't eliminate it entirely.
- **Convergence speed**: Dense graphs converge faster. Sparse graphs with long chains may need 100+ iterations.
- **Floating point accumulation**: For large graphs, use double precision. Single precision drifts noticeably after 50+ iterations.
- **Personalized PageRank**: Standard PageRank uses uniform random jump. For personalized recommendations, bias the jump vector toward seed pages.

## References

- For mathematical derivation of convergence proof, see `references/convergence-proof.md`
- For efficient sparse matrix implementation, see `references/sparse-implementation.md`
