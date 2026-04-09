# Leiden Algorithm

Leiden is a refined community detection algorithm (Traag, Waltman & van Eck, 2019) that fixes two structural defects in Louvain:

1. **Badly connected communities** — Louvain can produce communities where a single node bridges two otherwise disconnected parts. Remove that node and the community splits. Leiden guarantees all communities are internally connected.
2. **Non-convergence to a local optimum** — Louvain's greedy local moves can cycle without converging to a true locally optimal partition. Leiden provably converges.

---

## The Core Defect Leiden Fixes

In Louvain Phase 1 (local moves), a node is moved to maximize:

```
ΔQ = [Σ_in + 2k_i,in] / (2m) - [(Σ_tot + k_i) / (2m)]²
     - Σ_in / (2m)    + (Σ_tot / 2m)²  + (k_i / 2m)²
```

Where:
- `Σ_in` = sum of edge weights inside the candidate community
- `Σ_tot` = sum of all edge weights incident to nodes in candidate community  
- `k_i` = sum of weights incident to node i
- `k_i,in` = sum of weights from i to nodes in candidate community
- `m` = total edge weight in graph

This local check only verifies that moving node `i` to the new community increases Q. It does **not** verify that the community left behind, or the community joined, remains internally connected.

**Concrete failure case:**

```
Community A: nodes {1, 2, 3, 4}
Edges within A: 1-2, 2-3, 3-4  (a path, not fully connected)

Node 2 connects 1 to the rest. If Louvain later moves node 2
out of A, community A becomes {1} and {3,4} — disconnected.
Louvain does not detect or prevent this.
```

---

## Leiden Algorithm: Step-by-Step

Leiden has three phases per iteration instead of Louvain's two.

### Phase 1 — Local Moving (same as Louvain)

For each node in random order:
1. Compute `ΔQ` for moving to each neighbor's community.
2. If `max(ΔQ) > 0`, move node to that community.
3. Add affected neighbors back to queue.
4. Repeat until queue empty.

**Difference from Louvain**: Leiden uses a fast queue-based implementation that processes only nodes whose neighborhood changed, making this phase faster in practice.

### Phase 2 — Refinement (NEW — not in Louvain)

After Phase 1 produces partition `P`, Leiden runs a **refinement** step:

1. Start with singleton partition `P_refined` (every node in its own community).
2. For each community `C` in `P`:
   a. Consider only nodes within `C`.
   b. A node `v` in `C` can only merge with a sub-community `S` if:
      - `S` is within `C` (no cross-community merges)
      - The merge is **well-connected**: edges from `v` to `S` must be ≥ threshold `θ`
   c. Use a probabilistic merge (not purely greedy) — accept sub-optimal moves with probability proportional to gain.
3. Output `P_refined`.

The threshold `θ` for well-connectedness:

```
θ(v, S) = γ · |v| · |S| / (2m)
```

Where `γ` is the resolution parameter (default 1.0) and `|v|`, `|S|` are the volumes (sum of edge weights) of node `v` and community `S`.

A merge is only allowed if `w(v, S) ≥ θ(v, S)` where `w(v, S)` is the weight of edges between `v` and `S`.

**Why this fixes badly connected communities**: By only allowing merges within the communities found in Phase 1, and enforcing the connectivity threshold, Leiden ensures the final refined communities are subsets of Phase 1 communities and internally well-connected.

### Phase 3 — Aggregation (same logic as Louvain, different input)

Aggregate `P_refined` (not `P` from Phase 1) into a new graph:
- Each sub-community in `P_refined` becomes a node.
- Edge weights between new nodes = sum of edges between their constituent nodes.
- Retain the Phase 1 partition `P` as the initial partition for the next iteration.

Repeat all three phases on the aggregated graph until modularity stops improving.

---

## Modularity Formula (with Resolution Parameter)

Standard modularity (γ = 1):

```
Q = (1/2m) · Σ_{ij} [A_ij - (k_i · k_j)/(2m)] · δ(c_i, c_j)
```

With resolution parameter γ:

```
Q_γ = (1/2m) · Σ_{ij} [A_ij - γ · (k_i · k_j)/(2m)] · δ(c_i, c_j)
```

Where:
- `A_ij` = edge weight between nodes i and j
- `k_i` = degree (or strength) of node i
- `δ(c_i, c_j)` = 1 if i and j in same community, else 0
- `m` = total edge weight / 2

**Resolution limit reminder** (from parent SKILL.md Iron Law): even with Leiden, optimizing Q_γ at γ=1 cannot detect communities smaller than √(2E). Increase γ to find smaller communities.

---

## Leiden vs Louvain: Decision Table

| Criterion | Louvain | Leiden |
|-----------|---------|--------|
| Community connectivity guaranteed | No | Yes |
| Convergence to local optimum | No (can cycle) | Yes |
| Speed (same graph) | Slightly faster | ~10-30% slower |
| Resolution control (γ) | Yes | Yes |
| Non-determinism | High (ordering effects) | Lower (probabilistic refinement averages out) |
| Implementation availability | `python-louvain`, `igraph`, `networkx` | `leidenalg` (Python), `igraph` ≥ 0.9 |
| Use when | Quick exploration, small graphs | Production, large graphs, need reproducibility |

**Default recommendation**: Use Leiden unless your library does not support it. The overhead is small and the correctness guarantees matter in practice.

---

## Worked Example: 8-Node Graph

```
Nodes: 1-8
Edges: 1-2 (w=3), 1-3 (w=2), 2-3 (w=3),   ← cluster A
       4-5 (w=3), 4-6 (w=2), 5-6 (w=3),   ← cluster B
       3-4 (w=1), 7-8 (w=2),               ← bridge + cluster C
       7-1 (w=0.5), 8-5 (w=0.5)            ← weak cross-edges

m = (3+2+3+3+2+3+1+2+0.5+0.5) / 2 = 10
```

**Phase 1 (Louvain-style local moves):**

Starting from singletons, local moves converge to:
- Community 0: {1, 2, 3}
- Community 1: {4, 5, 6}
- Community 2: {7, 8}

Q ≈ 0.62 (verify: internal edges dominate over expected random edges)

**Phase 2 (Leiden Refinement within each community):**

Within Community 0 = {1, 2, 3}:
- All pairs well-connected (edge 1-3 = 2 ≥ θ = 1·2·2/20 = 0.2) ✓
- Refinement keeps {1,2,3} together

Within Community 1 = {4,5,6}: same structure, kept together ✓

Within Community 2 = {7,8}: only one edge, kept together ✓

`P_refined` = same as `P` here (no substructure within communities).

**Phase 3 (Aggregation):**

New graph has 3 nodes (one per community). Inter-community edges:
- C0-C1: edge 3-4 (w=1)
- C0-C2: edge 7-1 (w=0.5)
- C1-C2: edge 8-5 (w=0.5)

Rerun Phase 1 on 3-node graph: no beneficial merges (merging would decrease Q). Terminates.

**Final result:**
```json
{
  "communities": [
    {"id": 0, "members": [1, 2, 3], "size": 3},
    {"id": 1, "members": [4, 5, 6], "size": 3},
    {"id": 2, "members": [7, 8],    "size": 2}
  ],
  "modularity": 0.62
}
```

---

## Python Implementation

Using `leidenalg` library:

```python
import leidenalg
import igraph as ig

def detect_communities_leiden(
    edge_list: list[tuple],  # [(src, dst, weight), ...]
    resolution: float = 1.0,
    n_iterations: int = 10,
    seed: int = 42,
) -> dict:
    """
    edge_list: list of (source, target, weight) tuples
    resolution: γ parameter; >1 → smaller communities, <1 → larger
    n_iterations: run N times, keep best modularity partition
    """
    # Build igraph
    vertices = sorted({v for e in edge_list for v in e[:2]})
    vertex_index = {v: i for i, v in enumerate(vertices)}

    g = ig.Graph()
    g.add_vertices(len(vertices))
    g.vs["name"] = vertices

    edges = [(vertex_index[s], vertex_index[t]) for s, t, _ in edge_list]
    weights = [w for _, _, w in edge_list]
    g.add_edges(edges)
    g.es["weight"] = weights

    # Run Leiden with CPM (Constant Potts Model) objective
    # CPM uses resolution parameter more cleanly than modularity
    partition = leidenalg.find_partition(
        g,
        leidenalg.CPMVertexPartition,
        resolution_parameter=resolution,
        weights="weight",
        n_iterations=n_iterations,
        seed=seed,
    )

    communities = []
    for i, community in enumerate(partition):
        members = [vertices[j] for j in community]
        subgraph = g.induced_subgraph(community)
        internal_edges = sum(subgraph.es["weight"])
        total_possible = len(community) * (len(community) - 1) / 2
        density = internal_edges / total_possible if total_possible > 0 else 0

        communities.append({
            "id": i,
            "size": len(members),
            "members": members,
            "internal_density": round(density, 3),
        })

    return {
        "communities": communities,
        "summary": {
            "num_communities": len(communities),
            "modularity": round(partition.modularity, 4),
            "quality": round(partition.quality(), 4),
            "resolution": resolution,
        },
        "metadata": {
            "algorithm": "leiden-cpm",
            "nodes": len(vertices),
            "edges": len(edge_list),
        },
    }
```

**CPM vs Modularity objective**: The code uses `CPMVertexPartition` (Constant Potts Model) rather than `ModularityVertexPartition`. CPM does not have the resolution limit that modularity has, and the `resolution_parameter` maps cleanly to community density — a community exists only if its internal edge density exceeds `resolution`. For most production use cases, CPM is preferable.

To use modularity instead:

```python
partition = leidenalg.find_partition(
    g,
    leidenalg.ModularityVertexPartition,  # inherits resolution limit
    weights="weight",
    n_iterations=n_iterations,
    seed=seed,
)
```

---

## Resolution Parameter Guidance

| γ value | Effect | When to use |
|---------|--------|-------------|
| 0.25 | Large communities (macro structure) | Org-level departments |
| 0.5 | Medium-large | Business units within departments |
| 1.0 (default) | Balanced | General exploration |
| 2.0 | Smaller communities | Sub-teams, affinity groups |
| 5.0+ | Very small communities | Pairs/triads, may over-fragment |

**Practical sweep**: run Leiden at γ ∈ {0.25, 0.5, 1.0, 2.0} and compare. Plot modularity vs num_communities. The "elbow" — where adding smaller γ barely increases modularity — is often the natural scale.

```python
results = {}
for gamma in [0.25, 0.5, 1.0, 2.0, 5.0]:
    r = detect_communities_leiden(edge_list, resolution=gamma)
    results[gamma] = {
        "n_communities": r["summary"]["num_communities"],
        "modularity": r["summary"]["modularity"],
    }
# Pick gamma where n_communities stops growing rapidly
```

---

## Verifying Community Quality

After running Leiden, check these three numbers before trusting the output:

**1. Modularity Q > 0.3**
Q < 0.3 suggests weak community structure. The network may be too dense or too sparse for meaningful communities.

**2. Conductance per community**
```
conductance(C) = cut(C, V\C) / min(vol(C), vol(V\C))
```
Low conductance (< 0.1) = well-separated community. High conductance (> 0.5) = community bleeds into the rest.

**3. Size distribution sanity check**
If > 50% of nodes are in one community, or > 30% of communities are singletons, something is wrong:
- One giant community: γ too low, or network has genuine hub-and-spoke structure
- Many singletons: γ too high, or graph has many weakly connected nodes

---

## Reference

Traag, V. A., Waltman, L., & van Eck, N. J. (2019). From Louvain to Leiden: guaranteeing well-connected communities. *Scientific Reports*, 9, 5233. https://doi.org/10.1038/s41598-019-41695-z

Fortunato, S., & Barthélemy, M. (2007). Resolution limit in community detection. *PNAS*, 104(1), 36-41. (Resolution limit applies to both Louvain and Leiden when using modularity objective.)
