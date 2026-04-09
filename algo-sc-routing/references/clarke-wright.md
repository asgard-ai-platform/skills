# Clarke-Wright Savings Algorithm

## Core Idea

Start from the worst-case solution — every customer gets its own dedicated vehicle making a round trip to the depot. Then merge pairs of routes one at a time, picking the merge that saves the most distance, as long as capacity allows.

**Savings formula:**

```
s(i, j) = d(depot, i) + d(depot, j) − d(i, j)
```

Where:
- `d(depot, i)` = distance from depot to customer i
- `d(depot, j)` = distance from depot to customer j
- `d(i, j)` = distance between customers i and j

Merging the tail of one route ending at `i` with the head of another starting at `j` eliminates two depot legs and adds one direct customer-to-customer leg. The savings is how much distance you avoid.

---

## Algorithm Steps

### Step 0 — Initial Solution

Assign each customer its own route:
```
Route_1: depot → C1 → depot    cost = 2 * d(depot, C1)
Route_2: depot → C2 → depot    cost = 2 * d(depot, C2)
...
Route_n: depot → Cn → depot    cost = 2 * d(depot, Cn)
```

Total initial distance = `2 * Σ d(depot, Ci)` for all customers.

### Step 1 — Compute All Pairwise Savings

For every pair (i, j) where i ≠ j:
```
s(i, j) = d(depot, i) + d(depot, j) − d(i, j)
```

This produces `n*(n-1)/2` savings values. For 10 customers: 45 savings pairs.

### Step 2 — Sort Savings Descending

Build a savings list sorted from highest to lowest. High savings means merging those two routes avoids a lot of backtracking to depot.

### Step 3 — Greedy Merge

Iterate through the sorted savings list. For each pair (i, j) with savings `s(i, j)`, merge if ALL three conditions hold:

| Condition | Check |
|-----------|-------|
| **Interior check** | Customer i is at the *end* of its current route, and customer j is at the *start* of its current route |
| **Different routes** | i and j are not already on the same route |
| **Capacity check** | `load(route_i) + load(route_j) ≤ vehicle_capacity` |

If all three pass: concatenate route_i's sequence with route_j's sequence, removing the depot endpoint/startpoint between them.

If any condition fails: skip this pair and move to the next.

### Step 4 — Assign Remaining Routes to Vehicles

Routes that couldn't be merged remain as single-customer routes. Assign one vehicle per route. The number of vehicles used equals the number of routes remaining.

---

## Worked Example

### Setup

**Depot:** D at coordinates (0, 0)

**6 customers:**

| Customer | x  | y  | Demand |
|----------|----|----|--------|
| C1       | 2  | 1  | 100    |
| C2       | 3  | 2  | 150    |
| C3       | 1  | 4  | 200    |
| C4       | −1 | 3  | 120    |
| C5       | −2 | 1  | 180    |
| C6       | −1 | −1 | 90     |

**Vehicle capacity:** 500

### Distance Matrix (Euclidean, rounded to 2 decimals)

|    | D    | C1   | C2   | C3   | C4   | C5   | C6   |
|----|------|------|------|------|------|------|------|
| D  | 0    | 2.24 | 3.61 | 4.12 | 3.16 | 2.24 | 1.41 |
| C1 | 2.24 | 0    | 1.41 | 3.16 | 3.16 | 4.12 | 3.16 |
| C2 | 3.61 | 1.41 | 0    | 2.24 | 4.12 | 5.00 | 4.47 |
| C3 | 4.12 | 3.16 | 2.24 | 0    | 2.00 | 3.16 | 5.00 |
| C4 | 3.16 | 3.16 | 4.12 | 2.00 | 0    | 1.41 | 2.83 |
| C5 | 2.24 | 4.12 | 5.00 | 3.16 | 1.41 | 0    | 2.24 |
| C6 | 1.41 | 3.16 | 4.47 | 5.00 | 2.83 | 2.24 | 0    |

### Step 1 — Compute Savings (top pairs only)

```
s(C1, C2) = d(D,C1) + d(D,C2) − d(C1,C2) = 2.24 + 3.61 − 1.41 = 4.44
s(C3, C4) = 4.12 + 3.16 − 2.00 = 5.28
s(C4, C5) = 3.16 + 2.24 − 1.41 = 4.00 (but note: C4 is interior after C3-C4 merge)
s(C5, C6) = 2.24 + 1.41 − 2.24 = 1.41
s(C2, C3) = 3.61 + 4.12 − 2.24 = 5.49
s(C1, C3) = 2.24 + 4.12 − 3.16 = 3.20
s(C4, C6) = 3.16 + 1.41 − 2.83 = 1.74
```

**Sorted savings list (descending):**

| Rank | Pair    | Savings |
|------|---------|---------|
| 1    | C2, C3  | 5.49    |
| 2    | C3, C4  | 5.28    |
| 3    | C1, C2  | 4.44    |
| 4    | C4, C5  | 4.00    |
| 5    | C1, C3  | 3.20    |
| 6    | C4, C6  | 1.74    |
| 7    | C5, C6  | 1.41    |

### Step 2 — Greedy Merges

**Initial routes:**
```
R1: D→C1→D  (load=100)
R2: D→C2→D  (load=150)
R3: D→C3→D  (load=200)
R4: D→C4→D  (load=120)
R5: D→C5→D  (load=180)
R6: D→C6→D  (load=90)
```

**Merge 1: C2, C3 (savings=5.49)**
- C2 is tail of R2, C3 is head of R3 ✓
- Different routes ✓
- Load: 150 + 200 = 350 ≤ 500 ✓
- **Result:** `R2: D→C2→C3→D` (load=350)

**Merge 2: C3, C4 (savings=5.28)**
- C3 is now *interior* in R2 — NOT at tail ✗
- **Skip**

**Merge 3: C1, C2 (savings=4.44)**
- C1 is tail of R1, C2 is head of R2 ✓
- Different routes ✓
- Load: 100 + 350 = 450 ≤ 500 ✓
- **Result:** `R1: D→C1→C2→C3→D` (load=450)

**Merge 4: C4, C5 (savings=4.00)**
- C4 is tail of R4, C5 is head of R5 ✓
- Different routes ✓
- Load: 120 + 180 = 300 ≤ 500 ✓
- **Result:** `R4: D→C4→C5→D` (load=300)

**Merge 5: C1, C3 (savings=3.20)**
- C1 is now interior in R1 ✗
- **Skip**

**Merge 6: C4, C6 (savings=1.74)**
- C4 is now interior in R4 ✗
- **Skip**

**Merge 7: C5, C6 (savings=1.41)**
- C5 is tail of R4, C6 is head of R6 ✓
- Different routes ✓
- Load: 300 + 90 = 390 ≤ 500 ✓
- **Result:** `R4: D→C4→C5→C6→D` (load=390)

### Final Routes

```
Route 1: D → C1 → C2 → C3 → D   load=450/500   dist≈ 2.24+1.41+2.24+4.12 = 10.01
Route 2: D → C4 → C5 → C6 → D   load=390/500   dist≈ 3.16+1.41+2.24+1.41 =  8.22
Total distance: 18.23
```

**Initial (all separate):** `2*(2.24+3.61+4.12+3.16+2.24+1.41) = 33.56`

**Savings achieved:** `33.56 − 18.23 = 15.33` (45.7% reduction)

---

## Implementation

```python
import math
from itertools import combinations

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def clarke_wright(depot, customers, capacity):
    """
    depot: (x, y)
    customers: list of {"id": str, "coords": (x,y), "demand": int}
    capacity: int
    Returns list of routes, each route is a list of customer ids.
    """
    ids = [c["id"] for c in customers]
    demand = {c["id"]: c["demand"] for c in customers}
    coords = {c["id"]: c["coords"] for c in customers}

    # Precompute distances
    def dist(a, b):
        ca = coords[a] if a != "depot" else depot
        cb = coords[b] if b != "depot" else depot
        return euclidean(ca, cb)

    # Step 1: compute savings
    savings = []
    for i, j in combinations(ids, 2):
        s = dist("depot", i) + dist("depot", j) - dist(i, j)
        savings.append((s, i, j))
    savings.sort(reverse=True)

    # Step 2: initialize routes — one per customer
    # route_of[cid] = route index
    routes = [[cid] for cid in ids]
    route_of = {cid: idx for idx, cid in enumerate(ids)}
    loads = {idx: demand[cid] for idx, cid in enumerate(ids)}

    def active_route(cid):
        return route_of[cid]

    # Step 3: greedy merge
    for s, i, j in savings:
        ri = active_route(i)
        rj = active_route(j)

        if ri == rj:
            continue  # already on same route

        route_i = routes[ri]
        route_j = routes[rj]

        if route_i is None or route_j is None:
            continue  # route was merged away

        # i must be last in its route, j must be first in its route
        i_is_tail = (route_i[-1] == i)
        j_is_head = (route_j[0] == j)

        if not (i_is_tail and j_is_head):
            # Try the reverse: j is tail of rj, i is head of ri
            j_is_tail = (route_j[-1] == j)
            i_is_head = (route_i[0] == i)
            if j_is_tail and i_is_head:
                # Merge rj → ri
                i, j = j, i
                ri, rj = rj, ri
                route_i, route_j = route_j, route_i
            else:
                continue

        if loads[ri] + loads[rj] > capacity:
            continue

        # Merge: append route_j to end of route_i
        merged = route_i + route_j
        routes[ri] = merged
        routes[rj] = None
        loads[ri] += loads[rj]

        for cid in route_j:
            route_of[cid] = ri

    return [r for r in routes if r is not None]
```

**Usage:**

```python
depot = (0, 0)
customers = [
    {"id": "C1", "coords": (2, 1),  "demand": 100},
    {"id": "C2", "coords": (3, 2),  "demand": 150},
    {"id": "C3", "coords": (1, 4),  "demand": 200},
    {"id": "C4", "coords": (-1, 3), "demand": 120},
    {"id": "C5", "coords": (-2, 1), "demand": 180},
    {"id": "C6", "coords": (-1,-1), "demand": 90},
]
routes = clarke_wright(depot, customers, capacity=500)
# [['C1','C2','C3'], ['C4','C5','C6']]
```

---

## Interior Node Problem

The most common implementation bug: when merging `(i, j)`, customer `i` must be the **last node** in its route and `j` must be the **first node** in its route. Once a customer becomes interior (neither first nor last), it is ineligible for further merges at that position.

```
Route: D → C1 → C2 → C3 → D
              ↑          ↑
           interior    tail (eligible)
head (eligible)
```

**Implication:** early high-savings merges lock customers into interior positions, potentially blocking later merges. This is the fundamental greediness trade-off — Clarke-Wright does not backtrack.

If a savings pair (i, j) is blocked because i is interior, consider:
1. Trying (j, i) — reversed direction (i as head, j as tail), captured in the implementation above
2. Accepting the block and moving on
3. Running multiple passes with different tie-breaking orders (parallel Clarke-Wright variant)

---

## 2-Opt Local Search (Post-Processing)

Clarke-Wright produces a feasible solution. Apply 2-opt within each route to improve it.

**2-opt within a route:**

```
Before: ... → A → B → C → D → ...
                ↕ swap edges (A,B) and (C,D)
After:  ... → A → C → B → D → ...
        (segment B→C is reversed)
```

**Improvement condition:** swap edges (A→B) and (C→D) if:
```
d(A,B) + d(C,D) > d(A,C) + d(B,D)
```

```python
def two_opt(route, dist_fn):
    """
    route: list of customer ids (depot not included)
    dist_fn: callable(a, b) -> float, handles "depot" as special id
    """
    improved = True
    while improved:
        improved = False
        for i in range(len(route) - 1):
            for j in range(i + 2, len(route)):
                a = route[i-1] if i > 0 else "depot"
                b = route[i]
                c = route[j]
                d = route[j+1] if j < len(route)-1 else "depot"

                before = dist_fn(a, b) + dist_fn(c, d)
                after  = dist_fn(a, c) + dist_fn(b, d)

                if after < before - 1e-10:
                    route[i:j+1] = route[i:j+1][::-1]
                    improved = True
    return route
```

Apply 2-opt per route after Clarke-Wright completes. For a route of length k, one full 2-opt pass is O(k²). Repeat until no improvement found — convergence is typically fast (3–5 passes).

---

## Or-Opt: Moving Customers Between Routes

2-opt improves within routes. Or-opt moves one or more customers from one route to another.

**Single-customer or-opt:**
Remove customer `c` from route A, insert it into the best position in route B, if:
1. Route B has capacity for `demand(c)` after removal from A
2. The total distance decreases

```
Route A: D→C1→C2→C3→D   →   D→C1→C3→D   (C2 removed)
Route B: D→C4→C5→D       →   D→C4→C2→C5→D (C2 inserted between C4 and C5)
```

**Insertion cost for customer `c` between nodes `p` and `q`:**
```
Δ_insert = d(p, c) + d(c, q) − d(p, q)
```

**Removal gain for customer `c` between `prev` and `next`:**
```
Δ_remove = d(prev, c) + d(c, next) − d(prev, next)
```

**Net improvement:**
```
improvement = Δ_remove − Δ_insert
```
Accept move if `improvement > 0` and capacity allows.

---

## Practical Limits and Complexity

| Phase | Complexity | Bottleneck |
|-------|------------|------------|
| Savings computation | O(n²) | n pairs |
| Savings sort | O(n² log n) | dominates for large n |
| Greedy merge | O(n²) with route lookups | |
| 2-opt per route | O(k² * passes) per route | k = route length |
| Or-opt | O(n² * routes) per pass | |

**Rule of thumb for wall-clock time (Python, single-threaded):**

| n customers | Clarke-Wright | + 2-opt |
|-------------|--------------|---------|
| 50          | < 10 ms      | < 50 ms |
| 200         | < 100 ms     | < 500 ms |
| 1,000       | ~1 s         | ~10 s   |
| 5,000       | ~30 s        | minutes |

For n > 1,000, pre-cluster customers geographically (k-means or geographic sectors) before applying Clarke-Wright within each cluster. This reduces the effective n and avoids computing savings across customers that will never merge.

---

## Solution Quality

Clarke-Wright typically produces solutions within **10–20% of optimal** on random instances. Performance degrades when:

- Customers are not geographically clustered (random spread)
- Vehicle capacity is very tight (few merge opportunities)
- Time windows are dense (VRPTW variant blocks merges)

Expected solution quality relative to optimal:

| Instance type | Typical gap |
|---------------|-------------|
| Clustered customers | 5–10% |
| Uniformly distributed | 10–15% |
| Tight capacity (fill rate > 90%) | 15–25% |
| With time windows | 20–30% |

For gaps > 15%, consider running Clarke-Wright as the initialization step for a metaheuristic (simulated annealing or genetic algorithm) rather than as the final solution. See `references/metaheuristics.md`.

---

## Parallel Clarke-Wright Variant

The sequential version processes savings one at a time. The **parallel variant** allows multiple merges to be evaluated simultaneously and picks non-conflicting merges:

1. Compute all savings (same as sequential)
2. Find the highest-savings feasible merge
3. Apply it
4. Remove all savings pairs that now violate the interior/head/tail constraint due to the merge
5. Repeat from step 2

The parallel variant produces identical or slightly better results at the same asymptotic complexity. Most textbook implementations use the sequential version for simplicity; use parallel if you observe the sequential version making poor early merges that block better later ones.
