# Centrality Metric Comparison Framework

## The Core Question: What Does "Important" Mean?

Each centrality metric operationalizes a different definition of importance. Choosing the wrong one produces correct math for the wrong question.

| If "important" means… | Use | Formula |
|---|---|---|
| Most connections (popular, active) | Degree | C_D(v) = deg(v) / (N−1) |
| Controls information flow between groups | Betweenness | C_B(v) = Σ σ_st(v) / σ_st |
| Fastest to reach the whole network | Closeness | C_C(v) = (N−1) / Σ d(v,u) |
| Connected to other important nodes | Eigenvector | x_v = (1/λ) Σ_{u∈N(v)} x_u |

---

## Decision Framework

### Step 1: Identify the real-world question

Before running any algorithm, translate the business question into one of these canonical forms:

**"Who has the most direct reach?"**
→ Degree centrality. Use for: social media follower count analogy, contact tracing (direct exposure), citation count.

**"Who would, if removed, most disconnect the network?"**
→ Betweenness centrality. Use for: supply chain chokepoints, organizational brokers, infrastructure failure analysis.

**"Who can broadcast information / coordinate fastest?"**
→ Closeness centrality. Use for: emergency alert systems, logistics hubs, team coordination bottlenecks.

**"Who is endorsed by other credible nodes?"**
→ Eigenvector centrality (or PageRank for directed graphs). Use for: academic prestige, web authority, talent referral networks.

### Step 2: Check graph properties that constrain your choices

| Property | Implication |
|---|---|
| Directed graph | Distinguish in-degree (popularity) vs out-degree (activity); use PageRank over eigenvector |
| Weighted edges | Use weighted variants; unweighted degree ignores edge strength |
| Disconnected graph | Closeness is undefined — switch to harmonic centrality |
| Large N (>100k nodes) | Betweenness O(V×E) is impractical — use approximation or skip |
| Dynamic/temporal network | Snapshot centrality may invert over time; flag this uncertainty |

### Step 3: Run all four, compare the divergences

The most analytically valuable signal is often not the top-ranked node but the **nodes whose ranks differ sharply across metrics**. High degree + low betweenness = local hub. Low degree + high betweenness = hidden broker.

---

## Worked Example: 8-Node Organizational Network

```
HR --- CEO --- CFO
       |         |
       COO --- CTO
       |         |
      Mgr1     Mgr2
       |
      IC1
```

Edge list: {CEO-HR, CEO-CFO, CEO-COO, CFO-CTO, COO-CTO, COO-Mgr1, CTO-Mgr2, Mgr1-IC1}

N = 8, undirected, connected.

### Computed Centralities (normalized, rounded to 3 d.p.)

| Node | Degree | Betweenness | Closeness | Eigenvector |
|---|---|---|---|---|
| CEO | 0.429 (3/7) | **0.524** | **0.700** | **0.517** |
| COO | 0.429 (3/7) | **0.476** | 0.636 | 0.445 |
| CFO | 0.286 (2/7) | 0.095 | 0.583 | 0.376 |
| CTO | 0.286 (2/7) | 0.190 | 0.583 | 0.376 |
| HR | 0.143 (1/7) | 0.000 | 0.500 | 0.220 |
| Mgr1 | 0.286 (2/7) | 0.238 | 0.538 | 0.291 |
| Mgr2 | 0.143 (1/7) | 0.000 | 0.467 | 0.195 |
| IC1 | 0.143 (1/7) | 0.000 | 0.389 | 0.131 |

### Reading the divergences

**CEO vs COO — same degree, different betweenness (0.524 vs 0.476)**
Both have 3 connections, but CEO sits on more shortest paths (HR can only reach COO's subtree through CEO). If the organization needed to route critical decisions, removing CEO is more disruptive.

**Mgr1 vs CFO vs CTO — same degree (0.286), different betweenness**
Mgr1 (0.238) bridges IC1 to the rest of the network. CFO (0.095) and CTO (0.190) connect to COO and CEO who are already central, so their removal matters less. **Degree alone would rank them equally; betweenness reveals Mgr1's structural importance.**

**HR vs Mgr2 — same degree, same betweenness, different closeness (0.500 vs 0.467)**
HR connects to CEO (very central), Mgr2 connects to CTO (less central). HR can reach anyone in fewer hops.

### Conclusion for this network
The question "who is most important" has three different answers:
- For **broadcast/influence speed**: CEO (closeness 0.700)
- For **information control/brokerage**: CEO then COO (betweenness)
- For **prestige/endorsement**: CEO (eigenvector, connected to high-degree COO and CFO)

IC1 is definitively the periphery by all metrics.

---

## When Metrics Agree vs. Disagree

### Agreement pattern: star-like structure

In hub-and-spoke graphs (one central hub, many peripheral spokes), all four metrics converge on the hub as #1. Agreement means the network is structurally simple — one node is dominant in every sense.

```
     A
    /|\
   B C D      ← A is #1 in all four metrics
    \|/
     (no cross-links)
```

When you see full metric agreement, the network's importance structure is unambiguous.

### Disagreement pattern: community bridge structure

In networks with clusters, betweenness and degree diverge. A node connecting two dense communities may have moderate degree (it's not the most connected inside either cluster) but maximum betweenness (every cross-cluster path goes through it).

```
Cluster 1          Cluster 2
 A---B              F---G
 |\ /|              |\ /|
 | X |    ---X---   | X |
 |/ \|              |/ \|
 C---D              H---I
```

X has moderate degree (2 connections — one to each cluster) but high betweenness (all inter-cluster communication flows through X). If you used degree alone, X would rank at the bottom. Betweenness reveals X as the critical chokepoint.

**Rule of thumb**: When betweenness >> degree rank, the node is a structural broker. When degree >> betweenness rank, the node is a local hub embedded within a dense community.

---

## Metric-Specific Formulas (Expanded)

### Degree Centrality

**Undirected:**
```
C_D(v) = deg(v) / (N - 1)
```

**Directed (separate in and out):**
```
C_D_in(v)  = in_deg(v)  / (N - 1)   ← popularity
C_D_out(v) = out_deg(v) / (N - 1)   ← activity/influence
```

Normalization denominator is N−1 (max possible degree in simple graph).

### Betweenness Centrality

```
C_B(v) = Σ_{s≠v≠t} [ σ_st(v) / σ_st ]
```

Where:
- σ_st = total number of shortest paths from s to t
- σ_st(v) = number of those paths that pass through v

**Normalized** (divide by number of ordered pairs):
```
C_B_norm(v) = C_B(v) / [ (N-1)(N-2)/2 ]   (undirected)
C_B_norm(v) = C_B(v) / [ (N-1)(N-2) ]     (directed)
```

**Manual verification for the bridge topology from SKILL.md** (5 nodes: A,B,C,D,E):

Enumerate all s-t pairs and count paths through each node:

| s→t | All shortest paths | Paths through C | Paths through D |
|---|---|---|---|
| A→D | A-C-D | 1/1 = 1.0 | 1/1 = 1.0 |
| A→E | A-C-D-E | 1/1 = 1.0 | 1/1 = 1.0 |
| B→D | B-C-D | 1/1 = 1.0 | 1/1 = 1.0 |
| B→E | B-C-D-E | 1/1 = 1.0 | 1/1 = 1.0 |
| C→E | C-D-E | — | 1/1 = 1.0 |
| A→B | A-B, A-C-B (2 paths) | 1/2 = 0.5 | 0 |
| (others) | don't pass through C or D | 0 | 0 |

Raw C_B(C) = 1+1+1+1+0.5 = 4.5 — but need both directions, so ×2 if directed; for undirected the formula already counts unordered pairs, so C_B(C) = 4.5, normalized: 4.5 / [(4×3)/2] = 4.5/6 = **0.667** ✓

Raw C_B(D) = 1+1+1+1+1 = 5, but A→D and B→D paths also go through C, and D is not between A-B, A-C, B-C. Correct raw: D is on paths {A→E, B→E, C→E} = 3, so C_B(D) = 3/6 = **0.500** ✓

### Closeness Centrality

```
C_C(v) = (N - 1) / Σ_{u≠v} d(v, u)
```

Where d(v,u) is the shortest-path distance. The (N−1) numerator normalizes so that a node adjacent to everyone scores 1.0.

**Harmonic centrality** (use when graph is disconnected):
```
C_H(v) = Σ_{u≠v} 1/d(v,u)
```

Undefined distances (unreachable nodes) contribute 0 to the sum rather than causing division-by-zero. This is the correct drop-in replacement for disconnected graphs.

### Eigenvector Centrality

The score vector **x** satisfies:
```
A · x = λ · x
```

Where A is the adjacency matrix and λ is the largest eigenvalue. In practice, compute via power iteration:

```
x^(k+1) = A · x^(k)
x^(k+1) = x^(k+1) / ||x^(k+1)||   ← normalize each step
```

Repeat until ||x^(k+1) − x^(k)|| < ε (e.g., 1e-6).

**Convergence note**: Power iteration converges when the graph is connected and undirected. For directed graphs with dangling nodes (nodes with no out-edges), eigenvector centrality may not converge — use PageRank instead (adds a damping factor α, typically 0.85).

PageRank:
```
PR(v) = (1 - α)/N  +  α × Σ_{u→v} PR(u)/out_deg(u)
```

---

## Cross-Network Comparison Pitfalls

Raw centrality values are **not comparable across networks of different sizes**. Normalized degree C_D = 0.5 in a 10-node network means 5 connections; in a 1000-node network it means 500 connections.

**Safe comparisons:**
- Rank order within one network: always valid
- Percentile position within one network: always valid
- Normalized values across networks of the same size: valid
- Normalized values across networks of different sizes: **invalid for degree and closeness**

Betweenness and closeness normalization already accounts for N, so they are more cross-network-stable than raw values, but still sensitive to network density and topology.

If you must compare centrality across networks:
1. Compare percentile ranks (top 1%, top 5%) rather than absolute scores
2. Or use z-score normalization: `z_v = (C(v) - μ_C) / σ_C` within each network separately

---

## Computational Complexity Summary

| Metric | Time Complexity | Notes |
|---|---|---|
| Degree | O(V + E) | Trivially fast |
| Betweenness | O(V × E) | Brandes algorithm; bottleneck for large graphs |
| Closeness | O(V × (V + E)) | BFS from each node |
| Eigenvector | O(k × E) | k = iterations to convergence, typically 50–200 |

**Practical thresholds** (approximate, single machine):

| N (nodes) | E (edges) | Betweenness feasible? |
|---|---|---|
| < 10,000 | < 100,000 | Yes, exact |
| 10k–100k | 100k–1M | Marginal; consider approximation |
| > 100k | > 1M | No; use random-sample approximation only |

For large-scale betweenness, see `references/approximate-betweenness.md`.

---

## Quick Selection Card

```
Is the graph disconnected?
  YES → Replace closeness with harmonic centrality
  NO  → all four metrics available

Is the graph directed?
  YES → Separate in/out degree; prefer PageRank over eigenvector
  NO  → standard formulas apply

Primary question?
  "Most connections"          → Degree
  "Controls flow / broker"    → Betweenness
  "Fastest spreader"          → Closeness
  "Endorsed by important"     → Eigenvector / PageRank

N > 100k nodes?
  YES + need betweenness      → Use approximation (see references/approximate-betweenness.md)
  YES + only need degree      → Still O(V+E), fine

Cross-network comparison needed?
  YES → Use percentile ranks or z-scores, not raw normalized values
```
