# Network Visualization Tools & Methods

## Tool Selection Matrix

| Tool | Best For | Data Input | Output | Cost |
|------|----------|-----------|--------|------|
| **Gephi** | Publication-quality layouts, large networks (1k+ nodes) | CSV edge list, GraphML, GEXF | Static image, interactive HTML | Free |
| **Cytoscape** | Biological/org networks with attribute overlays | CSV, GraphML, JSON | Interactive, exportable | Free |
| **NetworkX** (Python) | Metric computation, scripted analysis | Any (via code) | Metrics, pyplot | Free |
| **Flourish** | Non-technical stakeholders, quick viz | CSV | Web-embeddable interactive | Free/Paid |
| **NodeXL** | Excel users, social media imports | Excel, Twitter/email APIs | Excel charts + metrics | Free (basic) |
| **Kumu** | Stakeholder maps, collaborative editing | CSV, JSON | Web-based interactive | Freemium |

**Default recommendation**: Use **NetworkX** to compute metrics, **Gephi** to visualize. They complement each other — NetworkX has no GUI but full algorithmic control; Gephi has powerful visual layouts but limited scripting.

---

## Data Format: Edge List (Universal Starting Point)

Every tool accepts an edge list. Build this first.

```csv
source,target,weight,tie_type
Alice,Bob,3,advice
Alice,Carol,1,advice
Bob,Dave,5,advice
Carol,Dave,2,advice
Dave,Eve,1,advice
Bob,Eve,4,advice
```

- `source`, `target`: node identifiers (names, IDs)
- `weight`: interaction frequency or tie strength (optional but useful)
- `tie_type`: if you're mapping multiple networks (advice vs. friendship), keep separate edge lists

**Directed vs. undirected**: "Alice advises Bob" is directed (A→B ≠ B→A). "Alice and Bob collaborate" is undirected. Advice networks are almost always directed.

---

## NetworkX: Computing Centrality Metrics

Install: `pip install networkx`

### Complete workflow for an advice network

```python
import networkx as nx
import csv

# 1. Load edge list
G = nx.DiGraph()  # DiGraph = directed; Graph = undirected
with open("edges.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        G.add_edge(row["source"], row["target"],
                   weight=int(row["weight"]))

# 2. Basic stats
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.3f}")
# Density = actual edges / possible edges. 
# For 10 nodes directed: max possible = 90.
# Low density (<0.1) = sparse, info bottlenecks likely.

# 3. Centrality metrics
degree_in  = dict(G.in_degree(weight="weight"))   # who gets asked
degree_out = dict(G.out_degree(weight="weight"))  # who asks others
betweenness = nx.betweenness_centrality(G, weight="weight", normalized=True)
closeness   = nx.closeness_centrality(G)

# 4. Print ranked results
print("\n--- In-Degree (Most Sought for Advice) ---")
for node, score in sorted(degree_in.items(), key=lambda x: -x[1])[:5]:
    print(f"  {node}: {score}")

print("\n--- Betweenness (Brokers / Gatekeepers) ---")
for node, score in sorted(betweenness.items(), key=lambda x: -x[1])[:5]:
    print(f"  {node}: {score:.3f}")

# 5. Detect communities (clusters)
G_undirected = G.to_undirected()
communities = nx.community.greedy_modularity_communities(G_undirected)
for i, comm in enumerate(communities):
    print(f"Cluster {i+1}: {sorted(comm)}")
```

### Structural holes: identifying brokers

NetworkX does not compute Burt's constraint directly in older versions. Use this manual calculation:

```python
def burt_constraint(G, node):
    """
    Lower constraint = more structural holes = more brokerage power.
    Ranges 0 to 1. <0.3 = strong broker position.
    """
    neighbors = list(G.successors(node)) + list(G.predecessors(node))
    neighbors = list(set(neighbors) - {node})
    if len(neighbors) < 2:
        return 1.0  # fully constrained (no brokerage possible)
    
    constraint = 0
    for j in neighbors:
        # proportion of i's ties that go to j
        p_ij = (G.has_edge(node, j) + G.has_edge(j, node)) / (2 * len(neighbors))
        
        mutual = 0
        for q in neighbors:
            if q == j:
                continue
            p_iq = (G.has_edge(node, q) + G.has_edge(q, node)) / (2 * len(neighbors))
            p_qj = (G.has_edge(q, j) + G.has_edge(j, q)) / (2 * len(neighbors))
            mutual += p_iq * p_qj
        
        constraint += (p_ij + mutual) ** 2
    return constraint

for node in G.nodes():
    c = burt_constraint(G, node)
    print(f"{node}: constraint={c:.3f}  {'BROKER' if c < 0.3 else ''}")
```

---

## Gephi: Layout & Visualization

### Setup steps

1. Export from NetworkX:
   ```python
   nx.write_gexf(G, "network.gexf")
   ```
2. Open `network.gexf` in Gephi (File → Open)
3. In **Overview** tab:
   - Run **Force Atlas 2** layout: nodes with more connections cluster toward center; disconnected nodes drift outward
   - Set **Scaling** = 10–30 for readability
   - Enable **Prevent Overlap**
   - Stop layout when stable (no more movement)
4. In **Statistics** panel, run:
   - Network Diameter → computes betweenness centrality, closeness centrality automatically
   - Modularity → detects communities, assigns color column
5. In **Appearance** panel:
   - Node **Size** → rank by Betweenness Centrality (size = influence as broker)
   - Node **Color** → partition by Modularity Class (color = cluster)
   - Label nodes by name

### Layout algorithm choice

| Layout | When to use |
|--------|-------------|
| **Force Atlas 2** | Default for most social networks. Physics-based, community structure emerges naturally |
| **Yifan Hu** | Large networks (500+ nodes), faster convergence |
| **Fruchterman-Reingold** | Smaller networks (<100 nodes), more even spacing |
| **Circular** | When you want to compare a specific node's connections across the ring; less useful for structure discovery |

---

## Worked Example: 8-Person Team Advice Network

### Raw survey data

Question asked: "In the past month, who did you seek advice from about work problems?" (multi-select)

| Person | Sought advice from |
|--------|--------------------|
| Alice | Bob, Carol |
| Bob | Dave |
| Carol | Bob, Dave |
| Dave | — |
| Eve | Bob, Dave |
| Frank | Carol, Dave |
| Grace | Alice, Bob |
| Hiro | Eve |

### Computed metrics

```
Node    In-degree  Out-degree  Betweenness  Role
Dave    4          0           0.286        Hub (pure receiver of advice)
Bob     4          1           0.214        Hub + mild broker
Carol   1          2           0.048        Local connector
Alice   1          2           0.024        Local connector
Eve     1          1           0.143        Bridge (Hiro's only path to network)
Frank   0          2           0.000        Peripheral
Grace   0          2           0.000        Peripheral
Hiro    0          1           0.000        Isolate (depends entirely on Eve)
```

### Interpretation applying the Iron Law

Dave has **zero out-degree** (never seeks advice) and **high in-degree** — everyone goes to him. But his **betweenness is not the highest** because Bob also connects multiple clusters. If Dave leaves, Bob absorbs most traffic. If **Eve** leaves, Hiro is completely cut off. Eve's betweenness (0.143) is high relative to her degree — textbook structural hole brokerage.

**Action implications**:
- Create direct tie: Frank → Bob (reduce Dave's load)
- Create direct tie: Hiro → Bob or Carol (eliminate single point of failure via Eve)
- Bob is undervalued: high centrality with no formal authority

---

## Kumu: Stakeholder Maps for Non-Technical Audiences

Kumu (kumu.io) is the best option when:
- Stakeholders need to explore the map interactively
- You want to present findings without installing software
- The network has qualitative attributes (relationship type, sentiment)

### Import format

```csv
# Elements sheet (nodes)
Label,Type,Department
Alice,Person,Engineering
Bob,Person,Product
Carol,Person,Design

# Connections sheet (edges)  
From,To,Type,Strength
Alice,Bob,Advice,Strong
Bob,Carol,Advice,Weak
```

Upload via: Project → Import → Excel/CSV template

**Limitation**: Kumu does not compute betweenness centrality. Use NetworkX first for metrics, Kumu only for presentation.

---

## Email/Slack Network Extraction (Without Surveys)

Survey-based data has social desirability bias (people list who they *should* consult, not who they actually do). Communication data is more honest.

### From email headers (with consent)

```python
import email
import mailbox
from collections import defaultdict

tie_counts = defaultdict(int)

mbox = mailbox.mbox("inbox.mbox")
for message in mbox:
    sender = email.utils.parseaddr(message["From"])[1]
    recipients = message.get_all("To", []) + message.get_all("Cc", [])
    for r_field in recipients:
        for name, addr in email.utils.getaddresses([r_field]):
            if addr and addr != sender:
                tie_counts[(sender, addr)] += 1

# Write edge list
with open("email_edges.csv", "w") as f:
    f.write("source,target,weight\n")
    for (src, tgt), count in tie_counts.items():
        if count >= 3:  # filter noise: only persistent ties
            f.write(f"{src},{tgt},{count}\n")
```

**Privacy note**: Always anonymize before analysis. Replace email addresses with role codes (ENG-01, PM-02) before sharing any visualization with third parties.

### Threshold decision

| Threshold (min messages) | Effect |
|--------------------------|--------|
| 1 | Includes noise (mass emails, newsletters) |
| 3–5 | Recommended starting point for monthly data |
| 10+ | Only strong, repeated ties visible |

Start at 5, reduce if the graph is too sparse, increase if it's too dense to read.

---

## Common Metric Formulas

### Degree centrality (normalized)

```
C_D(v) = deg(v) / (n - 1)
```
Where `n` = total nodes. For directed networks, compute separately for in-degree and out-degree.

### Betweenness centrality (normalized)

```
C_B(v) = Σ_{s≠v≠t} [σ(s,t|v) / σ(s,t)] / [(n-1)(n-2)]
```
- `σ(s,t)` = number of shortest paths between s and t
- `σ(s,t|v)` = number of those paths passing through v
- Denominator normalizes to [0,1]

NetworkX handles this; you rarely need to compute manually. Know the formula to explain what the number *means* to stakeholders: "0.28 means this person sits on 28% of all shortest communication paths."

### Network density

```
Density = E / [N × (N-1)]     # directed
Density = 2E / [N × (N-1)]    # undirected
```
- `E` = number of edges, `N` = number of nodes
- Dense networks (>0.5): high redundancy, slow diffusion of external info
- Sparse networks (<0.1): fast diffusion of novel info, high brokerage opportunities

---

## Output Checklist Before Sharing a Network Map

- [ ] Tie definition stated explicitly (advice / friendship / collaboration / communication)
- [ ] Data collection method noted (survey / email / observation)
- [ ] Time window specified (past month / past quarter)
- [ ] Node anonymization applied if sharing outside the team
- [ ] Centrality metric used for node sizing is labeled in the legend
- [ ] Community coloring explained in legend
- [ ] At least one structural finding called out (not just "here is the map")
- [ ] Caveats on snapshot limitation included if presenting to decision-makers
