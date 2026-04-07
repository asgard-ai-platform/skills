---
name: "algo-net-influence"
description: "Solve the influence maximization problem to select optimal seed nodes for maximum information spread. Use this skill when the user needs to choose seed users for viral campaigns, maximize network reach under a budget constraint, or compare seeding strategies — even if they say 'who should we seed first', 'maximize viral reach', or 'optimal influencer selection'."
metadata:
  category: "WP-46 網絡演算法"
  tags: ["network", "influence-maximization", "seed-selection", "viral-marketing"]
---

# Influence Maximization

## Overview

Influence maximization selects k seed nodes in a network to maximize expected spread under a diffusion model (Independent Cascade or Linear Threshold). NP-hard, but the greedy algorithm achieves (1-1/e) ≈ 63% approximation guarantee due to submodularity. Practical for networks up to millions of nodes with CELF optimization.

## When to Use

**Trigger conditions:**
- Selecting k influencers/users to seed a viral marketing campaign
- Maximizing information spread under a fixed budget (k seeds)
- Comparing seeding strategies (degree-based vs greedy vs random)

**When NOT to use:**
- When measuring existing influence (use centrality metrics)
- For community structure analysis (use community detection)

## Algorithm

```
IRON LAW: Greedy With Lazy Evaluation (CELF) Is the Practical Standard
The naive greedy algorithm requires O(k × n × R) simulations where
R = Monte Carlo runs (10,000+). CELF exploits submodularity to skip
unnecessary evaluations, achieving 700x speedup. Always use CELF
over naive greedy. Simple heuristics (top-k by degree) are fast
but can perform 50%+ worse than greedy.
```

### Phase 1: Input Validation
Build network graph. Choose diffusion model: Independent Cascade (probability per edge) or Linear Threshold (threshold per node). Set k (number of seeds) and propagation probabilities.
**Gate:** Graph loaded, diffusion model selected, k defined.

### Phase 2: Core Algorithm
**Greedy with CELF:**
1. Initialize: seed set S = ∅
2. For each candidate node, estimate marginal gain: σ(S∪{v}) - σ(S) via Monte Carlo simulation (R=10,000 runs)
3. Select node with highest marginal gain, add to S
4. CELF optimization: reuse previous marginal gains, only re-evaluate when a node's upper bound exceeds current best
5. Repeat until |S| = k

### Phase 3: Verification
Compare greedy result against baselines: random seeds, top-k degree, top-k PageRank. Greedy should significantly outperform.
**Gate:** Greedy spread > degree heuristic spread, difference is meaningful.

### Phase 4: Output
Return seed set with expected spread and comparison.

## Output Format

```json
{
  "seeds": [{"node": "user_42", "marginal_gain": 150, "selection_order": 1}],
  "expected_spread": 2500,
  "baselines": {"random": 800, "top_degree": 1900, "greedy": 2500},
  "metadata": {"k": 10, "model": "independent_cascade", "mc_simulations": 10000, "nodes": 50000}
}
```

## Examples

### Sample I/O
**Input:** Social network 10K nodes, k=5 seeds, IC model with p=0.1 per edge
**Expected:** Greedy selects diverse, well-positioned seeds (not all high-degree), expected spread ~500-1000.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| k=1 | Node with highest individual spread | Single seed, no overlap consideration |
| k > number of communities | One seed per community optimal | Diversity beats concentration |
| Very sparse graph (low p) | Small spread regardless of seeds | Network can't propagate with low probability |

## Gotchas

- **Monte Carlo variance**: With R=1000, spread estimates have ~5% variance. Use R=10,000+ for stable results, especially when comparing close candidates.
- **Diffusion model choice matters**: IC and LT produce different optimal seed sets. IC favors high-degree nodes; LT favors nodes that can trigger cascades.
- **Propagation probability estimation**: Real-world edge probabilities are unknown. Common approaches: uniform (p=0.01-0.1), weighted inverse degree (1/in-degree), or learned from cascade data.
- **Overlap penalty**: Greedy naturally handles overlap (submodularity). Heuristics that independently select top nodes waste seeds on overlapping influence spheres.
- **Scalability**: Even with CELF, millions of nodes require further approximation (sketch-based methods like IMM or TIM+).

## References

- For CELF and CELF++ implementation, see `references/celf-implementation.md`
- For scalable influence maximization (IMM), see `references/scalable-im.md`
