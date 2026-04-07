---
name: "algo-sc-routing"
description: "Solve vehicle routing problems to optimize delivery routes under capacity and time constraints. Use this skill when the user needs to plan delivery routes, minimize transportation costs, or optimize fleet utilization — even if they say 'delivery route optimization', 'fleet routing', or 'minimize driving distance'."
metadata:
  category: "WP-41 供應鏈演算法"
  tags: ["supply-chain", "vrp", "routing", "logistics"]
---

# Vehicle Routing Problem (VRP)

## Overview

VRP determines optimal routes for a fleet of vehicles to serve a set of customers from a depot, minimizing total distance or cost. NP-hard — exact solutions only feasible for small instances (< 25 nodes). Practical solutions use heuristics (Clarke-Wright savings, sweep) or metaheuristics (simulated annealing, genetic algorithm).

## When to Use

**Trigger conditions:**
- Planning daily delivery routes for a fleet of vehicles
- Minimizing total travel distance/time under capacity constraints
- Optimizing route assignments across multiple vehicles

**When NOT to use:**
- For single-vehicle route optimization (use TSP solvers)
- For real-time dynamic routing with continuous order arrivals (use online algorithms)

## Algorithm

```
IRON LAW: VRP Is NP-Hard — Exact Solutions Don't Scale
For n customers, the solution space grows factorially. Exact methods
(branch and bound) work for n < 25. For real-world problems (50-1000+
customers), heuristics are REQUIRED. A good heuristic solution within
5% of optimal is far more valuable than an optimal solution that takes
hours to compute.
```

### Phase 1: Input Validation
Collect: depot location, customer locations and demands, vehicle capacity, number of vehicles, time windows (if applicable), distance/time matrix.
**Gate:** All locations geocoded, demand doesn't exceed vehicle capacity per customer.

### Phase 2: Core Algorithm
**Clarke-Wright Savings Heuristic:**
1. Start with each customer on its own route (depot → customer → depot)
2. Compute savings for merging route pairs: s(i,j) = d(depot,i) + d(depot,j) - d(i,j)
3. Sort savings descending
4. Merge routes greedily if capacity constraint allows
5. Improve with 2-opt (swap edges within routes) and or-opt (move customers between routes)

### Phase 3: Verification
Check: all customers visited exactly once, no vehicle exceeds capacity, all routes start and end at depot. Compare total distance against lower bound.
**Gate:** All constraints satisfied, solution within 10% of lower bound.

### Phase 4: Output
Return routes with sequence, distance, and load.

## Output Format

```json
{
  "routes": [{"vehicle": 1, "sequence": ["depot", "C3", "C7", "C1", "depot"], "distance_km": 45, "load": 850, "capacity": 1000}],
  "summary": {"total_distance_km": 180, "vehicles_used": 4, "utilization_avg": 0.82},
  "metadata": {"customers": 30, "method": "clarke_wright_2opt", "computation_ms": 150}
}
```

## Examples

### Sample I/O
**Input:** 10 customers, 2 vehicles (cap=500), depot at center
**Expected:** 2 routes, each serving ~5 customers, total distance minimized by geographic clustering.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| One customer demand > capacity | Infeasible or split delivery | Need split delivery VRP variant |
| All customers co-located | Minimal routing, capacity-limited trips | Distance is trivial, trips determined by load |
| Tight time windows | More vehicles needed | Time constraints may prevent full-capacity routes |

## Gotchas

- **Distance matrix quality**: Road distance ≠ Euclidean distance. Use actual road network distances (Google Maps, OSRM) for practical routing.
- **Time windows add complexity**: VRPTW (VRP with Time Windows) is significantly harder. Customers requiring specific delivery windows fragment routes.
- **Dynamic vs static**: Real-world routing has cancellations, additions, and traffic. Plan static routes but allow dynamic re-optimization.
- **Driver constraints**: Maximum driving hours, break requirements, and overtime costs add practical constraints not in the basic model.
- **Return to depot**: Standard VRP assumes routes return to depot. Open VRP (routes end at last customer) needs different formulation.

## References

- For Clarke-Wright algorithm implementation, see `references/clarke-wright.md`
- For metaheuristic approaches (SA, GA), see `references/metaheuristics.md`
