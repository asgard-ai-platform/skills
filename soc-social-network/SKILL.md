---
name: "soc-social-network"
description: "Apply social network analysis concepts including nodes, ties, centrality, structural holes, and strong/weak ties to map and analyze relationship structures. Use this skill when the user needs to understand influence patterns in an organization, identify key connectors, analyze information flow, or map stakeholder relationships — even if they say 'who are the influencers', 'how does information spread here', or 'map the relationships in our team'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "social-network-analysis", "organizational-behavior"]
---

# Social Network Analysis

## Overview

Social network analysis examines relationships (ties) between actors (nodes) to reveal structure invisible in org charts. It identifies who really holds influence, where information bottlenecks exist, and how ideas spread through a community.

## Framework

```
IRON LAW: Structure Determines Influence, Not Just Position

A mid-level manager who bridges two disconnected departments may have more
real influence than a VP who sits in a dense, well-connected cluster.
Network position (centrality, brokerage) determines influence more than
formal hierarchy.
```

### Core Concepts

| Concept | Definition | Why It Matters |
|---------|-----------|---------------|
| **Node** | An actor (person, org, entity) | Who's in the network |
| **Tie** | A relationship between nodes | How nodes are connected |
| **Strong tie** | Frequent, emotional, reciprocal relationship | Trust, support, reliable info |
| **Weak tie** (Granovetter) | Infrequent, casual, bridging relationship | Access to NEW information and opportunities |
| **Degree centrality** | Number of direct connections | Popularity, activity |
| **Betweenness centrality** | How often a node sits on shortest paths between others | Brokerage, gatekeeping, information control |
| **Closeness centrality** | Average distance to all other nodes | Speed of information reach |
| **Structural hole** (Burt) | Gap between two clusters, bridged by a broker | Source of competitive advantage — the broker controls information flow |

### Analysis Steps

1. **Define the network**: Who are the nodes? What constitutes a tie? (communication, trust, advice, collaboration)
2. **Collect data**: Surveys ("who do you go to for advice?"), email/Slack data, meeting co-attendance
3. **Map the network**: Visualize nodes and ties
4. **Calculate centrality metrics**: Degree, betweenness, closeness for each node
5. **Identify structural patterns**: Clusters, bridges, isolates, structural holes
6. **Interpret for action**: Who are the key connectors? Where are the bottlenecks?

## Output Format

```markdown
# Network Analysis: {Context}

## Network Definition
- Nodes: {who} (N = {count})
- Tie definition: {what constitutes a connection}
- Data source: {survey / communication data / observation}

## Key Metrics
| Node | Degree | Betweenness | Role |
|------|--------|-------------|------|
| {person} | {N connections} | {score} | Hub / Bridge / Isolate |

## Structural Findings
- Clusters: {identified groups}
- Bridges: {who connects clusters}
- Structural holes: {where gaps exist}
- Isolates: {disconnected nodes}

## Implications
1. {finding → action}
```

## Examples

### Correct Application
**Scenario:** Advice network in a 50-person startup
- Node with highest betweenness centrality: Product Manager (not the CEO) — she bridges engineering, design, and business teams
- Structural hole: Marketing team has zero direct ties to engineering — all communication goes through PM
- Implication: If PM leaves, information flow between 3 teams collapses. Need to create direct cross-functional ties ✓

### Incorrect Application
- "The CEO has the most connections, so he's the most influential" → CEO has high degree centrality (many ties) but may have low betweenness (everyone also connects to each other without needing the CEO). Violates Iron Law: structure determines influence, not just connection count.

## Gotchas

- **Granovetter's strength of weak ties**: Weak ties are MORE valuable for accessing new information and opportunities because they bridge different social circles. Strong ties share redundant information.
- **Network data is sensitive**: Mapping who talks to whom can feel like surveillance. Be transparent about purpose and anonymize where possible.
- **Networks change**: Relationships evolve. A network map is a snapshot. Remeasure periodically.
- **Centrality is context-dependent**: High centrality in the advice network ≠ high centrality in the friendship network. Define the tie type carefully.
- **Don't confuse correlation with causation**: Central people may perform better because of their position, OR they may be central because they perform well. Disentangling is hard.

## References

- For network visualization tools and methods, see `references/network-tools.md`
