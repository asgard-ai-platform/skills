# Multi-Resolution Community Detection

## The Resolution Limit Problem

Standard Louvain maximizes modularity Q with resolution parameter γ = 1:

```
Q = (1/2E) Σᵢⱼ [Aᵢⱼ - γ(kᵢkⱼ/2E)] δ(cᵢ, cⱼ)
```

Where:
- `Aᵢⱼ` = edge weight between nodes i and j
- `E` = total edge weight in graph
- `kᵢ` = weighted degree of node i
- `γ` = resolution parameter (default 1.0)
- `δ(cᵢ, cⱼ)` = 1 if i and j are in the same community, else 0

**The resolution limit** (Fortunato & Barthélemy, 2007): at γ = 1, Louvain cannot reliably detect communities with fewer than √(2E) internal edges. In a network with E = 10,000 edges, communities with fewer than ~141 internal edges may be merged into larger ones even if they are structurally distinct.

### When This Matters in Practice

| Network Size | E (edges) | Minimum Detectable Community Size |
|---|---|---|
| Small team (50 nodes) | ~200 | ~20 internal edges |
| Mid-size org (500 nodes) | ~5,000 | ~100 internal edges |
| Large social net (10k nodes) | ~500,000 | ~1,000 internal edges |
| Platform graph (100k nodes) | ~5M | ~3,162 internal edges |

If you have domain knowledge that real communities are smaller than these thresholds, you **must** use γ > 1 or switch to Leiden.

---

## Resolution Parameter γ: What It Controls

Increasing γ raises the "expected null model" baseline, making modularity gain harder to achieve within large communities. This forces the algorithm to split large communities into smaller ones.

| γ value | Effect | Use when |
|---|---|---|
| 0.25–0.5 | Merges small communities; finds macro-structure | Hierarchical overview, very large networks |
| 0.75–1.0 | Standard Louvain behavior | Default starting point |
| 1.5–2.0 | Finds finer-grained communities | Small teams inside large orgs |
| 3.0–5.0 | Very small communities; risk of over-fragmentation | Dense local cliques, known micro-structure |

**Caveat**: there is no universally correct γ. The "right" resolution depends on the question you are answering, not on a mathematical criterion.

---

## Multi-Resolution Workflow

Run Louvain across a sweep of γ values, then select the resolution that matches your analytical goal.

### Step 1: Sweep γ

```python
import community as community_louvain  # python-louvain library
import networkx as nx

def sweep_resolution(G, gammas):
    results = []
    for gamma in gammas:
        partition = community_louvain.best_partition(G, resolution=gamma)
        Q = community_louvain.modularity(partition, G)
        n_communities = len(set(partition.values()))
        sizes = sorted(
            [sum(1 for v in partition.values() if v == c)
             for c in set(partition.values())],
            reverse=True
        )
        results.append({
            "gamma": gamma,
            "modularity": Q,
            "n_communities": n_communities,
            "largest": sizes[0],
            "smallest": sizes[-1],
            "median_size": sizes[len(sizes)//2],
        })
    return results

gammas = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 5.0]
sweep = sweep_resolution(G, gammas)
```

### Step 2: Plot Stability Diagram

Plot `n_communities` vs `γ`. Look for **plateaus** — ranges of γ where the number of communities is stable. Plateaus indicate robust partition scales.

```
n_communities
     ^
  40 |              ╔═══════╗
  30 |         ╔════╝       ╚══╗
  20 |    ╔════╝               ╚═══
  10 |════╝
     +-----------------------------------> γ
     0.25  0.5  1.0  1.5  2.0  3.0  5.0
           ↑plateau↑    ↑plateau↑
```

Plateaus at specific γ ranges correspond to hierarchically nested community levels. Pick γ values inside plateaus, not on the transitions.

### Step 3: Check Modularity Landscape

Modularity Q often peaks and then declines as γ increases. This does **not** mean the peak γ is the best answer — it means that γ is where the algorithm most strongly separates communities from the null model. Communities at γ > peak can still be more meaningful for your use case.

### Step 4: Validate Against Ground Truth (If Available)

If you have partial labels (e.g., known department membership for 20% of nodes), compute Normalized Mutual Information (NMI) for each γ partition:

```python
from sklearn.metrics import normalized_mutual_info_score

# labeled_nodes: dict {node_id: true_label}
def nmi_for_partition(partition, labeled_nodes):
    nodes = list(labeled_nodes.keys())
    true_labels = [labeled_nodes[n] for n in nodes]
    pred_labels = [partition[n] for n in nodes]
    return normalized_mutual_info_score(true_labels, pred_labels)
```

Select γ that maximizes NMI over the labeled subset.

---

## Worked Example: 500-Node Organizational Network

**Setup:** 500 employees, 4,800 email edges weighted by monthly frequency. Known ground truth: 8 departments of size 40–80 people.

**Resolution limit check:** √(2 × 4800) ≈ 98. Communities with fewer than ~98 internal edges may be missed at γ = 1. Departments of size 40 with internal density ~0.3 have ~240 internal edges — safely above limit.

**Sweep results:**

| γ | Q | Communities | Largest | Smallest | Notes |
|---|---|---|---|---|---|
| 0.25 | 0.41 | 3 | 280 | 60 | Over-merged |
| 0.5 | 0.55 | 6 | 140 | 30 | Close but missing 2 depts |
| 1.0 | 0.63 | 9 | 95 | 22 | Near ground truth (8 depts) |
| 1.5 | 0.58 | 14 | 60 | 8 | Starting to split teams |
| 2.0 | 0.49 | 22 | 45 | 3 | Sub-team level |
| 3.0 | 0.37 | 38 | 30 | 1 | Working group level |

**Decision:** γ = 1.0 gives 9 communities (Q = 0.63), NMI = 0.81 against known departments. The extra community corresponds to a cross-functional project team — a real structure not in the org chart. Accept γ = 1.0 for department-level analysis.

**Secondary question — finding sub-teams:** Use γ = 2.0 to zoom in, then filter to only nodes within one specific department to confirm sub-team structure.

---

## Hierarchical Nesting Analysis

Multi-resolution detection reveals a dendrogram-like hierarchy. Two communities at fine resolution γ₂ are "nested" within a community at coarse resolution γ₁ if:

- Their node sets are subsets of the coarser community
- The coarser γ₁ partition is obtained by merging the fine-resolution partition

To check nesting consistency:

```python
def compute_nesting_matrix(partitions_by_gamma, gammas):
    """
    Returns matrix M where M[i][j] = fraction of community i at gamma[i]
    whose nodes fall in the same community at gamma[j] (j < i = coarser).
    """
    gammas_sorted = sorted(gammas)
    nesting = {}
    for idx_fine, g_fine in enumerate(gammas_sorted[1:], 1):
        g_coarse = gammas_sorted[idx_fine - 1]
        p_fine = partitions_by_gamma[g_fine]
        p_coarse = partitions_by_gamma[g_coarse]
        for comm_fine in set(p_fine.values()):
            nodes_fine = [n for n, c in p_fine.items() if c == comm_fine]
            coarse_labels = [p_coarse[n] for n in nodes_fine]
            dominant = max(set(coarse_labels), key=coarse_labels.count)
            purity = coarse_labels.count(dominant) / len(coarse_labels)
            nesting[(g_coarse, g_fine, comm_fine)] = purity
    return nesting
```

Purity > 0.85 → community at fine scale is cleanly nested inside one coarse-scale community.
Purity < 0.60 → community at fine scale straddles coarse-scale boundaries — likely an artifact of resolution transition, not a real sub-structure.

---

## Choosing Between Scales: Decision Framework

```
START: What question are you answering?
│
├─ "High-level segments, strategic view"
│    → Use γ ∈ [0.5, 1.0], target 5–15 communities
│    → Validate: communities should be interpretable by a domain expert in < 5 minutes
│
├─ "Team-level structure inside a known macro-group"
│    → Run full sweep, then filter to that macro-group
│    → Re-run Louvain on the subgraph (avoids resolution limit for that region)
│    → Use γ ∈ [1.0, 2.0] on subgraph
│
├─ "Known community sizes don't match output"
│    → Check if expected size is below √(2E) → resolution limit in effect
│    → Increase γ until expected size range appears in output
│    → Or switch to Leiden with partition_type = RBConfigurationVertexPartition
│
└─ "Need to report structure at multiple levels simultaneously"
     → Use three γ values: coarse (plateau 1), standard (plateau 2), fine (plateau 3)
     → Report hierarchy as nested JSON
     → Flag low-purity (<0.60) nodes as "cross-boundary" in output
```

---

## Stability Across Runs

Because Louvain is non-deterministic, the same γ may produce different partitions across runs. Measure stability with the **Adjusted Rand Index (ARI)** between repeated runs:

```python
from sklearn.metrics import adjusted_rand_score
import numpy as np

def stability_score(G, gamma, n_runs=10):
    partitions = []
    nodes = sorted(G.nodes())
    for _ in range(n_runs):
        p = community_louvain.best_partition(G, resolution=gamma)
        partitions.append([p[n] for n in nodes])
    
    scores = []
    for i in range(n_runs):
        for j in range(i+1, n_runs):
            scores.append(adjusted_rand_score(partitions[i], partitions[j]))
    return np.mean(scores), np.std(scores)

# Example output: mean ARI = 0.91, std = 0.04 → stable partition
# Example output: mean ARI = 0.52, std = 0.18 → unstable, interpret with caution
```

**Rule of thumb:**
- Mean ARI > 0.90 → stable, trust the partition
- Mean ARI 0.70–0.90 → moderate stability; report top-3 members per community rather than exact assignments
- Mean ARI < 0.70 → unstable at this γ; this γ is likely on a transition boundary — shift γ to a nearby plateau

---

## Relationship to Leiden Algorithm

Leiden (Traag et al., 2019) uses the same generalized modularity with γ but adds a refinement phase that guarantees **well-connected communities** — no community where removing a single node disconnects it. For multi-resolution analysis:

- Leiden is more stable across runs (higher mean ARI at same γ)
- Leiden's `find_partition` accepts `resolution_parameter` directly
- The γ sweep and plateau analysis procedure above applies identically to Leiden

```python
import leidenalg
import igraph as ig

def leiden_sweep(G_igraph, gammas):
    results = []
    for gamma in gammas:
        partition = leidenalg.find_partition(
            G_igraph,
            leidenalg.RBConfigurationVertexPartition,
            resolution_parameter=gamma,
            n_iterations=10,
            seed=42  # reproducible
        )
        results.append({
            "gamma": gamma,
            "modularity": partition.modularity,
            "n_communities": len(partition),
        })
    return results
```

Leiden with a fixed seed is deterministic; set `seed=42` when you need reproducibility across runs.

---

## Common Failure Modes

**Over-fragmentation at high γ**: Q drops sharply and many singleton or size-2 communities appear. This is not meaningful structure — it means γ exceeds the network's natural modularity scale. Reduce γ.

**Plateau missing entirely**: The n_communities vs γ curve is monotonically increasing with no flat region. This indicates the network has no strong hierarchical structure, or is close to a random graph. Multi-resolution analysis will not yield stable insights; report single-scale result with a confidence caveat.

**Giant community + many tiny ones**: Symptom of a hub-and-spoke network structure, not resolution parameter error. No γ value will produce balanced communities if the underlying network is hub-dominated. Investigate degree distribution before concluding about resolution.

**NMI peak disagrees with modularity peak**: Trust NMI if you have labels. Modularity maximization is a heuristic; NMI against ground truth is a direct measure of what you care about.
