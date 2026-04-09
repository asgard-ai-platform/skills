# Combinatorial VCG

Combinatorial VCG extends the standard position-auction VCG (covered in the parent SKILL.md) to settings where bidders can bid on **bundles** of items and may have non-additive valuations. This changes everything: the winner determination problem becomes NP-hard, and several additional pathologies appear.

---

## When Position Auction VCG Does Not Suffice

The parent SKILL.md assumes each bidder wants exactly one slot and slots are ranked by CTR. This implies:

- Optimal allocation = sort bidders by value, match top-K to top-K slots
- Polynomial time: O(N log N)

This breaks down when:

| Condition | Why Position Auction Fails |
|-----------|---------------------------|
| Bidder wants multiple placements simultaneously | Bundle valuations not captured |
| Complementarity: value({A,B}) > value({A}) + value({B}) | Additive assignment misses joint value |
| Substitutability: value({A,B}) < value({A}) + value({B}) | Overbidding risk under additive assumption |
| Items are not interchangeable slots but distinct inventory (mobile vs. desktop, video vs. display) | No natural CTR ordering |

**Concrete example where position auction VCG gives the wrong answer:**

Three bidders, two distinct ad slots (Slot A = mobile homepage, Slot B = desktop sidebar):

```
Bidder 1: value({A}) = 10, value({B}) = 6, value({A,B}) = 14
Bidder 2: value({A}) = 8,  value({B}) = 5, value({A,B}) = 11
Bidder 3: value({A}) = 3,  value({B}) = 9, value({A,B}) = 9
```

Position auction VCG (sort by value, assign greedily): gives slot A to B1 (value 10), slot B to B2 (value 8). Total welfare = 10 + 5 = 15. But B3 values slot B at 9 — this allocation is suboptimal.

Correct optimal: B1 takes slot A, B3 takes slot B. Welfare = 10 + 9 = **19**.

---

## Formal Setup

**Items:** M = {1, 2, ..., m} (distinct ad slots or inventory types)  
**Bidders:** N = {1, 2, ..., n}  
**Bundle bids:** Each bidder i submits valuations v_i(S) for every subset S ⊆ M  
**Allocation:** A = (S_1, S_2, ..., S_n) where S_i ∩ S_j = ∅ for i ≠ j (each item goes to at most one bidder)

**Welfare-maximizing allocation:**

```
A* = argmax Σ_i  v_i(S_i)
     subject to: S_i ∩ S_j = ∅  ∀ i ≠ j
```

**VCG payment for winner i:**

```
p_i = [ max allocation welfare excluding bidder i ]
    − [ welfare of all bidders except i in A* ]
```

More precisely:

```
p_i = W_{-i}* − (W* − v_i(S_i*))
```

Where:
- `W*` = total welfare under A* (the optimal allocation including i)
- `W_{-i}*` = optimal total welfare when bidder i is removed entirely
- `S_i*` = the bundle bidder i receives in A*

**Individual rationality check:** `v_i(S_i*) ≥ p_i` always holds under VCG (dominant strategy truthfulness guarantees non-negative surplus).

---

## Worked Example: Combinatorial VCG Step by Step

Using the three-bidder, two-slot example from above.

### Step 1: Winner Determination

Enumerate feasible allocations (slots A and B, each to at most one bidder):

| Allocation | Welfare |
|-----------|---------|
| B1{A,B} | 14 |
| B2{A,B} | 11 |
| B3{A,B} | 9 |
| B1{A}, B2{B} | 10 + 5 = 15 |
| B1{A}, B3{B} | 10 + 9 = **19** ← optimal |
| B2{A}, B1{B} | 8 + 6 = 14 |
| B2{A}, B3{B} | 8 + 9 = 17 |
| B3{A}, B1{B} | 3 + 6 = 9 |
| B3{A}, B2{B} | 3 + 5 = 8 |

**A\*** = {B1 → slot A, B3 → slot B}, **W\*** = 19.

### Step 2: VCG Payment for Bidder 1

Remove B1. Solve welfare maximization over {B2, B3}:

| Sub-allocation | Welfare |
|---------------|---------|
| B2{A,B} | 11 |
| B3{A,B} | 9 |
| B2{A}, B3{B} | 8 + 9 = **17** ← optimal |
| B3{A}, B2{B} | 3 + 5 = 8 |

W_{-1}* = 17. Welfare of others in A* = v_3(slot B) = 9.

```
p_1 = 17 − 9 = 8
```

Bidder 1 values slot A at 10, pays 8. Surplus = 2. ✓

### Step 3: VCG Payment for Bidder 3

Remove B3. Solve welfare maximization over {B1, B2}:

| Sub-allocation | Welfare |
|---------------|---------|
| B1{A,B} | 14 |
| B2{A,B} | 11 |
| B1{A}, B2{B} | 10 + 5 = **15** ← optimal |
| B2{A}, B1{B} | 8 + 6 = 14 |

W_{-3}* = 15. Welfare of others in A* = v_1(slot A) = 10.

```
p_3 = 15 − 10 = 5
```

Bidder 3 values slot B at 9, pays 5. Surplus = 4. ✓

### Summary

| Winner | Bundle | Valuation | VCG Payment | Surplus |
|--------|--------|-----------|-------------|---------|
| B1 | {A} | 10 | **8** | 2 |
| B3 | {B} | 9 | **5** | 4 |

**Total welfare:** 19. **Total revenue:** 13.

Compare to position auction VCG (wrong allocation B1→A, B2→B, welfare=15): revenue would be lower AND welfare is suboptimal.

---

## Computational Complexity

### Winner Determination Problem (WDP)

WDP is equivalent to **weighted set packing** — NP-hard in general.

Input size: with m items and n bidders, each bidder can submit up to 2^m bundle bids. Exact enumeration is doubly exponential in the worst case.

**Why it's hard:**  
Consider 4 items {A, B, C, D}. Bidder 1 bids on {A,B}, Bidder 2 on {B,C}, Bidder 3 on {A,C,D}. Checking whether Bidder 1 + Bidder 3 beats Bidder 2 + any others requires checking conflicts across all combinations.

### Where It Becomes Polynomial

| Auction Structure | Complexity | Reason |
|------------------|------------|--------|
| Position auction (parent SKILL.md) | O(N log N) | Assignment problem; no bundles |
| Each bidder wants exactly one item | O(N log N) | Sort and assign |
| Items form a tree structure | Polynomial | DP on tree |
| General combinatorial | NP-hard | Weighted set packing reduction |

For ad platforms running combinatorial auctions on heterogeneous inventory (video + display + mobile + retargeting), even computing the optimal allocation is NP-hard.

### Practical Approximation Approaches

**1. LP Relaxation + Branch and Bound**

Relax the integer constraint (allow fractional allocation). Solve LP in polynomial time. Use LP bound to prune the branch-and-bound tree. Works well in practice if bids are sparse.

```python
# Conceptual structure (not runnable without a MIP solver)
from scipy.optimize import linprog  # inadequate for MIP; use PuLP or OR-Tools

# Decision variable x[i][S] = 1 if bidder i gets bundle S
# Objective: maximize Σ_i Σ_S  v_i(S) * x[i][S]
# Constraints:
#   Σ_i Σ_{S ∋ j}  x[i][S] <= 1  for each item j  (each item assigned once)
#   Σ_S x[i][S] <= 1              for each bidder i  (each bidder gets one bundle)
#   x[i][S] ∈ {0, 1}
```

**2. Greedy Approximation (Ratio ≥ 1/m)**

Sort bundles by bid/size ratio. Assign greedily if no conflict. Gives at most m-approximation where m = number of items. Fast but not incentive compatible.

**3. VCG with Approximation (VCG-A)**

Run an approximation algorithm A instead of exact welfare maximization. Compute payments using the same externality formula.

**CRITICAL:** VCG-A loses the truthfulness guarantee. Bidders may have incentive to misreport if the approximation creates non-monotone allocation rules (winning less doesn't always yield higher payment).

---

## Combinatorial VCG Pathologies

### 1. Revenue Non-Monotonicity (Stronger Than Position Auction Case)

In position auctions, adding a slot can decrease revenue ("lonely bidder" issue). In combinatorial auctions, this effect is amplified: adding a bidder or an item can decrease total VCG revenue in unintuitive ways.

**Example:** Two items {A, B}, two bidders:
- B1: v({A}) = 10, v({B}) = 10, v({A,B}) = 10
- B2: v({A}) = 9,  v({B}) = 9,  v({A,B}) = 9

Optimal: B1 gets {A,B}, welfare = 10. W_{-1}* = 9 (B2 gets {A,B}). Payment = 9 - 0 = 9.

Now add B3: v({A}) = 5, v({B}) = 0:
New optimal: B1 gets {A,B}, welfare = 10. W_{-1}* = max(B2{A,B}=9, B2{A}+B3{}=9, B2{B}+B3{A}=9+5=14?). Wait — B3 only wants A, B2 gets B.

W_{-1}* = B2{B} + B3{A} = 9 + 5 = 14. Payment = 14 - 0 = 14. Revenue **increased** here.

The direction of the effect depends on the specific bid landscape. The takeaway: revenue is not monotone in the number of bidders or items. This makes budget forecasting for combinatorial VCG unreliable.

### 2. Collusion Is Easier in Combinatorial Settings

In position auctions, collusion requires coordinating bids across a ranking. In combinatorial auctions, colluding bidders can partition the item space, bid only on their partition, and eliminate each other's externalities entirely:

```
Without collusion:
  B1 bids on {A,B}, B2 bids on {A,B} — they compete, payments are high.

With collusion:
  B1 agrees to bid only on {A}, B2 bids only on {B}.
  No conflict → externality = 0 → both pay 0.
```

This is a fundamental weakness of VCG in combinatorial settings. No simple mechanism can simultaneously achieve truthfulness, efficiency, and collusion-resistance (Myerson-Satterthwaite theorem implications).

### 3. Computational VCG Payments

Even if you solve the WDP optimally, computing VCG payments requires solving n+1 optimization problems (one for the full set, one for each winner removed). If WDP takes time T, payments cost O(n × T).

For large auctions (n = 1000 bidders, m = 10 items), this means 1001 NP-hard subproblems per auction. In practice, platforms time-box the solver and accept approximate payments, which breaks truthfulness.

### 4. Exposure Problem for Bidders

In a combinatorial auction, a bidder who wants bundle {A,B} but only wins {A} may be worse off than not participating at all (if v({A}) < 0 due to stranded costs). VCG handles this by allowing bids on the full bundle — if the bidder only wins a subset, they pay 0 for items outside their winning bundle.

However, bidders must **correctly express** their bundle valuations. If a bidder submits only single-item bids, they may end up with an unwanted partial bundle. This is a UI/UX and information-revelation problem, not a mechanism flaw per se.

---

## When Combinatorial VCG Is Actually Used

Almost nowhere in production ad platforms. The documented cases:

| Context | Status |
|---------|--------|
| Spectrum auctions (FCC, government) | Used; justified by regulatory truthfulness requirements |
| Academic research benchmark | Widely used for comparison |
| Small-scale B2B media buys (negotiated) | Occasionally, as a reference pricing model |
| Display + video + search bundle deals | Not used; platforms prefer simplified rules |

The computational cost, collusion vulnerability, and revenue unpredictability make combinatorial VCG impractical for high-frequency programmatic auctions (RTB). The theoretical elegance does not translate to operational viability at scale.

---

## Decision Framework: Position Auction VCG vs. Combinatorial VCG

```
Is each bidder interested in at most one slot?
├── YES → Use position auction VCG (parent SKILL.md)
│         O(N log N), revenue-predictable, operationally simple
└── NO  → Bidders want bundles across heterogeneous inventory
          ├── Can bids be decomposed additively without loss?
          │   ├── YES → Treat as independent position auctions
          │   └── NO  → Combinatorial auction needed
          │             ├── m ≤ 4 items? → Exact VCG feasible (2^4 = 16 subsets)
          │             ├── m ≤ 20 items, sparse bids? → LP + B&B
          │             └── m > 20 or dense bids? → Approximation only;
          │                  truthfulness is lost; consider alternative mechanisms
          └── Revenue requirement?
              └── If strict revenue targets needed, VCG is wrong choice regardless
                  (IRON LAW: VCG optimizes welfare, not revenue)
```

---

## Reference Formula Summary

| Quantity | Formula |
|---------|---------|
| Optimal allocation | A\* = argmax Σ_i v_i(S_i) s.t. disjoint bundles |
| Total welfare | W\* = Σ_i v_i(S_i\*) |
| Welfare without bidder i | W_{-i}\* = max allocation over N \ {i} |
| VCG payment | p_i = W_{-i}\* − (W\* − v_i(S_i\*)) |
| Individual rationality | v_i(S_i\*) − p_i ≥ 0, always holds under truthful VCG |
| Revenue | R = Σ_i p_i ≤ W\* (VCG never extracts full welfare as revenue) |
