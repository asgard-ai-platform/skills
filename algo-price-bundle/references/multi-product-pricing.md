# Multi-Product Pricing Optimization

Multi-product pricing differs fundamentally from single-product pricing: prices interact through demand cross-elasticities and bundle substitution effects. This reference covers the optimization mechanics for 2–N product portfolios, with and without bundling.

---

## Core Framework: Joint Profit Maximization

For a portfolio of N products sold to M customer segments, the optimization problem is:

```
Maximize Σ_s Σ_p [ n_s · x_sp · (p_p - c_p) ]

Where:
  s = segment index (1..M)
  p = product index (1..N)
  n_s = number of customers in segment s
  x_sp = purchase indicator: 1 if segment s buys product p, 0 otherwise
  p_p = price of product p
  c_p = marginal cost of product p
```

`x_sp` is determined by willingness-to-pay (WTP):  
`x_sp = 1` if `WTP_sp ≥ p_p`, else 0.

The bundle adds a composite product:

```
WTP_s(bundle) = Σ_p WTP_sp  (additive valuations, no complementarity)
x_s(bundle) = 1 if WTP_s(bundle) ≥ p_bundle AND bundle provides surplus ≥ individual purchases
```

Under mixed bundling, the segment chooses whichever option yields highest consumer surplus:

```
CS_s(individual) = Σ_p max(WTP_sp - p_p, 0)
CS_s(bundle)     = WTP_s(bundle) - p_bundle

Segment s buys: argmax{ CS_s(individual), CS_s(bundle), 0 }
```

---

## Two-Product Worked Example

### Setup

| Segment | Size | WTP(A) | WTP(B) |
|---------|------|--------|--------|
| S1 | 100 | $80 | $30 |
| S2 | 100 | $30 | $70 |
| S3 | 50  | $60 | $60 |

Marginal costs: c_A = $10, c_B = $10.

### Step 1: Individual Pricing Candidates

Enumerate candidate prices for A: {$80, $60, $30}  
Enumerate candidate prices for B: {$70, $60, $30}

For each combination, compute who buys and total profit:

| p_A | p_B | A buyers | B buyers | Profit A | Profit B | Total |
|-----|-----|----------|----------|----------|----------|-------|
| $80 | $70 | 100 (S1) | 100 (S2) | $7,000 | $6,000 | $13,000 |
| $80 | $60 | 100 (S1) | 150 (S2+S3) | $7,000 | $7,500 | $14,500 |
| $60 | $70 | 150 (S1+S3) | 100 (S2) | $7,500 | $6,000 | $13,500 |
| $60 | $60 | 150 (S1+S3) | 150 (S2+S3) | $7,500 | $7,500 | **$15,000** |
| $30 | $70 | 250 (all) | 100 (S2) | $5,000 | $6,000 | $11,000 |

**Individual pricing optimum: p_A=$60, p_B=$60, profit=$15,000**

### Step 2: Pure Bundle Price Candidates

Bundle WTP per segment: S1=$110, S2=$100, S3=$120

Candidate bundle prices: {$120, $110, $100}

| p_bundle | Buyers | Revenue | Profit (−$20 cost/unit) |
|----------|--------|---------|-------------------------|
| $120 | 50 (S3) | $6,000 | $5,000 |
| $110 | 150 (S1+S3) | $16,500 | $13,500 |
| $100 | 250 (all) | $25,000 | **$20,000** |

**Pure bundle optimum: p_bundle=$100, profit=$20,000**

### Step 3: Mixed Bundle Optimization

Now test combinations of (p_A, p_B, p_bundle) simultaneously.

At p_A=$80, p_B=$70, p_bundle=$100:

For each segment, compute CS:

```
S1: CS(individual) = max(80-80,0) + max(30-70,0) = $0
    CS(bundle)     = 110 - 100 = $10   → buys bundle
    
S2: CS(individual) = max(30-80,0) + max(70-70,0) = $0
    CS(bundle)     = 100 - 100 = $0    → indifferent, assume buys bundle
    
S3: CS(individual) = max(60-80,0) + max(60-70,0) = $0
    CS(bundle)     = 120 - 100 = $20   → buys bundle
```

All 250 customers buy bundle at $100: profit = 250×($100−$20) = **$20,000**

Try p_A=$80, p_B=$30, p_bundle=$100:

```
S1: CS(individual) = 0 + 0 = $0; CS(bundle) = $10 → bundle
S2: CS(individual) = 0 + max(70-30,0) = $40; CS(bundle) = 0 → buys B individually
S3: CS(individual) = 0 + max(60-30,0) = $30; CS(bundle) = $20 → buys B individually
```

Revenue: S1 buys bundle (100×$80 profit + 0) → actually 100×($100-$20)=$8,000  
S2 buys B only: 100×($30-$10)=$2,000  
S3 buys B only: 50×($30-$10)=$1,000  
**Total: $11,000** — worse.

Try p_A=$60, p_B=$60, p_bundle=$100:

```
S1: CS(individual) = max(80-60,0) + 0 = $20; CS(bundle) = $10 → buys A individually
S2: CS(individual) = 0 + max(70-60,0) = $10; CS(bundle) = $0 → buys B individually
S3: CS(individual) = 0 + 0 = $0; CS(bundle) = $20 → buys bundle
```

Revenue:  
S1: 100×($60-$10) = $5,000  
S2: 100×($60-$10) = $5,000  
S3: 50×($100-$20) = $4,000  
**Total: $14,000** — worse than pure bundle.

**Result summary:**

| Strategy | Profit |
|----------|--------|
| Individual (p_A=$60, p_B=$60) | $15,000 |
| Pure bundle (p=$100) | $20,000 |
| Mixed bundle (best found) | $20,000 |

In this example, pure and mixed bundling tie at the same profit. This occurs when the valuation floor of the weakest segment exactly equals the bundle price — no segment benefits from buying individually at any price that also captures the low-WTP segments.

---

## N-Product Extension

### Exponential Complexity Problem

With N products, the candidate pricing space is:

- Individual prices: M candidate prices per product → M^N combinations
- Bundle options: 2^N possible subsets

For N=5, M=5 price points: 5^5 = 3,125 individual combinations × 32 bundle subsets = ~100K evaluations. Tractable by brute force.

For N=10: ~10^10 × 1,024 = intractable. Use the following reduction strategies.

### Reduction Strategy 1: Hierarchical Bundling

Instead of optimizing all 2^N subsets, offer tiered bundles:

```
Tier structure:
  Level 0: Individual products (sold separately)
  Level 1: Category bundles (products in same category)
  Level 2: Mega bundle (all or most products)
```

This reduces bundle SKUs from 2^N to N + C + 1 where C = number of categories.

**Rule of thumb:** Once N > 6, add one bundle tier per doubling of N rather than enumerating all subsets.

### Reduction Strategy 2: Segment Aggregation

If two segments have similar WTP vectors (Euclidean distance < ε), merge them. Reduces M without significant accuracy loss.

```python
def merge_segments(segments, eps=5.0):
    """
    segments: list of (size, wtp_vector)
    Returns merged segment list.
    """
    merged = []
    used = set()
    for i, (n_i, wtp_i) in enumerate(segments):
        if i in used:
            continue
        group = [(n_i, wtp_i)]
        for j, (n_j, wtp_j) in enumerate(segments[i+1:], start=i+1):
            if j in used:
                continue
            dist = sum((a-b)**2 for a, b in zip(wtp_i, wtp_j))**0.5
            if dist < eps:
                group.append((n_j, wtp_j))
                used.add(j)
        total_n = sum(g[0] for g in group)
        avg_wtp = [sum(g[0]*g[1][k] for g in group)/total_n
                   for k in range(len(wtp_i))]
        merged.append((total_n, avg_wtp))
        used.add(i)
    return merged
```

### Reduction Strategy 3: Independent Subproblems

If the valuation correlation matrix shows near-zero correlation between product clusters, split the optimization into independent sub-problems.

```
Correlation matrix check:
  Compute corr(WTP_i, WTP_j) for all i≠j
  If |corr(A, B)| < 0.1 AND |corr(A, C)| < 0.1:
    → A is pricing-independent; optimize A alone
```

---

## Cross-Elasticity Adjustments (When Demand Is Not Step-Function)

The worked example uses step-function demand (buy/no-buy). For continuous demand, substitute:

```
D_p(p_p) = a_p - b_p · p_p + Σ_{q≠p} γ_pq · p_q

Where:
  b_p  = own-price sensitivity
  γ_pq = cross-price elasticity coefficient (positive = substitutes, negative = complements)
```

Profit:

```
π = Σ_p (p_p - c_p) · D_p(p_p, p_{-p})
```

First-order conditions (set ∂π/∂p_p = 0 for each p):

```
D_p + (p_p - c_p)·(-b_p) + Σ_{q≠p} (p_q - c_q)·γ_qp = 0
```

This is a linear system in prices. In matrix form:

```
[∂²π/∂p²] · p* = RHS vector
```

Solve with standard linear algebra. The matrix is (N×N) with diagonal entries `-2b_p` and off-diagonal `γ_pq + γ_qp`.

**When to use this vs. discrete WTP model:**
- Use discrete WTP when you have segment-level survey data (common in B2B, SaaS pricing).
- Use continuous demand when you have historical transaction volume at multiple price points (common in retail, e-commerce).

---

## Bundle Discount Calibration

Given an optimal bundle price p_bundle and individual prices p_A, p_B, the effective discount is:

```
Absolute discount = (p_A + p_B) - p_bundle
Relative discount = Absolute discount / (p_A + p_B)
```

**Perception threshold (empirical rule):** Bundles below 10% discount are rarely perceived as deals. Bundles above 35% discount trigger quality suspicion.

Target zone: **15–30% relative discount**.

If the profit-maximizing bundle price implies a discount outside this zone:

| Situation | Adjustment |
|-----------|------------|
| Discount < 10% | Consider not bundling; communicate value differently |
| Discount 10–15% | Bundle if valuation data strongly supports it; add non-price benefits |
| Discount 15–30% | Optimal zone; proceed |
| Discount > 30% | Raise individual prices OR reframe bundle as new SKU |

---

## Practical Optimization Procedure (2–5 Products)

```
INPUT:
  segments: [(n_s, [WTP_s1, WTP_s2, ..., WTP_sN])]
  costs:    [c_1, c_2, ..., c_N]
  price_grid_steps: integer (default 10)

STEP 1 — Build price grid
  For each product p:
    min_price_p = min(WTP_sp for all s where WTP_sp > c_p)
    max_price_p = max(WTP_sp for all s)
    price_candidates_p = linspace(min_price_p, max_price_p, steps)

STEP 2 — Individual pricing baseline
  Enumerate all combinations of price_candidates
  For each combination: compute profit (no bundles)
  Record best_individual_profit, best_individual_prices

STEP 3 — Bundle price grid
  For each non-trivial subset B of products (|B| >= 2):
    WTP_s(B) = Σ_{p∈B} WTP_sp
    bundle_price_candidates = linspace(min WTP_s(B), max WTP_s(B), steps)

STEP 4 — Mixed bundle optimization
  For each combo of (individual prices, bundle prices for each subset):
    For each segment s:
      Compute CS for each available option (individual products, each bundle)
      Assign segment to max-CS option
    Compute total profit
  Record best_mixed_profit, best_mixed_config

STEP 5 — Select dominant strategy
  If best_mixed_profit >= best_individual_profit * 1.02:  # 2% improvement threshold
    Recommend mixed bundling
  Elif best_pure_bundle_profit > best_individual_profit:
    Recommend pure bundling
  Else:
    Recommend individual pricing

OUTPUT: prices dict + profit comparison + strategy recommendation
```

The 2% threshold in Step 5 prevents recommending marginal bundle complexity when gains are noise-level.

---

## Common Failure Modes in Multi-Product Optimization

**Ignoring cannibalization direction**  
Mixed bundling can *reduce* profit if the bundle price is set too low and pulls high-value customers away from full-price individual purchases. Always verify that `CS_s(bundle) < CS_s(individual)` for your highest-WTP segments.

**Single-segment WTP assumption**  
Using average WTP across segments instead of segment-level data destroys the heterogeneity that makes bundling profitable. Bundling captures surplus *because* segments differ; averaging erases that signal.

**Bundle as pure discount signal**  
If p_bundle = p_A + p_B − ε, customers infer individual prices are overpriced. Set individual prices first at levels you can defend, then position bundle as a separate value proposition.

**Omitting marginal cost from bundle**  
When physical goods are bundled, shipping/handling costs often scale with bundle size. Forgetting COGS on the second unit is a common spreadsheet error that makes bundles appear more profitable than they are.
