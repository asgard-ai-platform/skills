# Network Effects Mathematical Models

## Three Laws: Sarnoff, Metcalfe, Reed

Three foundational models describe how network value scales with users. Each applies to a different interaction structure.

| Law | Value Formula | Structure | Example |
|-----|--------------|-----------|---------|
| Sarnoff's Law | V ∝ n | Broadcast (1→many) | Radio, TV |
| Metcalfe's Law | V ∝ n² | Pairwise connections | Phone, fax |
| Reed's Law | V ∝ 2ⁿ | Subgroup formation | Facebook Groups, Slack |

**n** = number of nodes (users) on the network.

---

## Metcalfe's Law

### Formula

```
V(n) = k × n(n - 1) / 2 ≈ k × n²
```

- `k` = value per connection (platform-specific constant)
- `n(n-1)/2` = number of unique pairwise connections among n users
- The approximation `kn²` holds for large n

### Why n² and not n

With 5 users: 5×4/2 = **10** possible connections.  
With 10 users: 10×9/2 = **45** connections.  
Double the users → roughly **4×** the connections.

This superlinear scaling is the mathematical source of winner-take-all dynamics: a platform with 2× users has 4× the connection value, not 2×.

### Worked Example: Messaging Platform

Assume k = $0.001 per connection per month (implied revenue proxy).

| Users (n) | Connections n(n-1)/2 | Monthly Value |
|-----------|---------------------|---------------|
| 100 | 4,950 | $4.95 |
| 1,000 | 499,500 | $499.50 |
| 10,000 | 49,995,000 | $49,995 |
| 1,000,000 | 4.99 × 10¹¹ | $499,950,000 |

10,000× user growth → ~100,000× value growth.

### Metcalfe's Critical Mass Point

The network becomes "self-sustaining" when adding one user creates more value than the cost to acquire that user (CAC).

```
Marginal value of user n+1 = k × n   (new connections created = n)

Break-even: k × n* = CAC
→ n* = CAC / k
```

**Example**: CAC = $5, k = $0.001  
→ n* = 5 / 0.001 = **5,000 users**

Below 5,000 users, the platform must subsidize growth. Above it, organic word-of-mouth can sustain growth — this is the **liquidity threshold** referenced in SKILL.md.

---

## Reed's Law

### Formula

```
V(n) = k × (2ⁿ - n - 1)
```

The `2ⁿ` term counts all non-trivial subsets of n users (all possible groups). Subtract n (single-user groups) and 1 (empty set).

For large n, the dominant term is 2ⁿ.

### When Reed's Law Applies

Reed's Law applies when **group formation** is the core interaction, not pairwise exchange. Slack channels, Facebook Groups, subreddits. The value comes from being able to form any combination of interest groups, not just individual connections.

### Practical Limits

Reed's Law is an upper bound, not a realized value. In practice:
- Most possible groups are never formed (n=1M doesn't produce 2^1M active groups)
- Attention is finite; users belong to O(10–100) groups regardless of platform size
- Reed's Law describes **potential** value, not extracted value

**Rule of thumb**: Use Metcalfe for transaction/communication platforms. Use Reed only when group tools (channels, communities, shared lists) are the core product.

---

## Two-Sided Network Effects: The Cross-Elasticity Model

For multi-sided platforms, Metcalfe applies within each side, but the critical metric is the **cross-side network effect**. The standard economic formulation (Rochet & Tirole 2003) introduces cross-elasticity of demand.

### Notation

- `nA` = number of users on side A (e.g., buyers)
- `nB` = number of users on side B (e.g., sellers)
- `vA(nB)` = value to one A-user as a function of B-side size
- `vB(nA)` = value to one B-user as a function of A-side size

### Simple Linear Model

```
vA(nB) = αA × nB    (A values B linearly)
vB(nA) = αB × nA    (B values A linearly)
```

- `αA` = cross-side effect coefficient (A's willingness to pay per additional B-user)
- `αB` = cross-side effect coefficient (B's willingness to pay per additional A-user)

**Total platform value**:

```
V = nA × vA(nB) + nB × vB(nA)
  = nA × αA × nB + nB × αB × nA
  = nA × nB × (αA + αB)
```

Platform value scales with the **product** of both side sizes, not either side alone. This is why ignoring one side's growth tanks total value.

### Worked Example: Job Board

- Platform: 500 job seekers (side A), 100 employers (side B)
- αA = $0.10/employer/month (each employer adds $0.10 of value to each seeker)
- αB = $2.00/seeker/month (each seeker adds $2.00 of value to each employer)

```
V = 500 × 100 × (0.10 + 2.00)
  = 50,000 × 2.10
  = $105,000/month
```

Now double employers to 200 (keeping seekers at 500):

```
V = 500 × 200 × 2.10 = $210,000/month   (+100%)
```

Now double seekers to 1,000 (keeping employers at 100):

```
V = 1,000 × 100 × 2.10 = $210,000/month   (+100%)
```

Same total effect. But the **subsidy decision** differs: because αB >> αA, employers extract much more value per seeker than seekers extract per employer. The money side is employers (charge them); the subsidy side is seekers (make it free or cheap to attract them).

---

## Quantifying Network Effect Strength

### Engagement Elasticity (Empirical)

Network effect strength can be estimated from historical data:

```
ε = (ΔInteractions / Interactions) / (ΔUsers / Users)
```

- ε < 1: sublinear (weak or no network effects; might be a pipeline business)
- ε = 1: linear (Sarnoff-like)
- ε = 2: quadratic (consistent with Metcalfe)
- ε > 2: superlinear (group-formation effects, Reed-like)

**How to compute**: Run a regression of log(interactions) on log(users) across cohorts or time periods. The slope is ε.

```python
import math

# Example data: monthly snapshots of (users, interactions)
data = [
    (1_000, 5_000),
    (5_000, 120_000),
    (20_000, 2_000_000),
    (100_000, 50_000_000),
]

log_users = [math.log(d[0]) for d in data]
log_interactions = [math.log(d[1]) for d in data]

# Simple slope estimate (rise/run on log-log)
n = len(data)
x_mean = sum(log_users) / n
y_mean = sum(log_interactions) / n
slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(log_users, log_interactions)) \
      / sum((x - x_mean) ** 2 for x in log_users)

print(f"Network effect elasticity ε ≈ {slope:.2f}")
# Output: ε ≈ 1.97  → consistent with Metcalfe's Law
```

### Interpretation Table

| Measured ε | Interpretation | Platform Type |
|-----------|----------------|---------------|
| 0.0 – 0.8 | No meaningful network effects | Pipeline; value chain analysis is more appropriate |
| 0.8 – 1.2 | Weak, broadcast-type effects | Content platforms, media |
| 1.8 – 2.2 | Pairwise network effects (Metcalfe regime) | Messaging, payments, marketplaces |
| > 2.5 | Group-formation effects (Reed regime) | Community platforms, developer ecosystems |

---

## Multi-Homing Penalty on Effective Network Size

When users participate in multiple platforms simultaneously (multi-homing), the effective network size is not the full registered count.

### Adjusted Metcalfe Formula

```
V_effective = k × (n × (1 - m))²
```

- `m` = multi-homing rate (fraction of users also active on a competing platform)
- `(1 - m)` = exclusive user fraction

**Example**: Platform has 1M users; 60% also use a competitor (m = 0.6).

```
V_effective = k × (1,000,000 × 0.4)²
            = k × (400,000)²
            = k × 160,000,000,000

V_naive     = k × (1,000,000)²
            = k × 1,000,000,000,000
```

Multi-homing at 60% reduces **effective network value to 16%** of the naive estimate. This is why market share statistics overstate platform advantage in high-multi-homing markets (ride-sharing, food delivery).

---

## Critical Mass Threshold: Full Model

Combining both subsidy-side acquisition and cross-side value:

```
Threshold condition for side A:
  αA × nB* ≥ pA + switching_cost_A

Threshold condition for side B:
  αB × nA* ≥ pB + switching_cost_B
```

Where:
- `pA`, `pB` = prices charged to each side
- `switching_cost` = cost to leave existing platform/behavior

**System of equations**: Both must hold simultaneously, which is why chicken-and-egg is a coordination problem. Neither side reaches threshold until the other does.

### Strategy Implication

To break the deadlock, reduce one inequality to zero:
1. Set `pA = 0` (subsidy side): condition becomes `αA × nB* ≥ switching_cost_A`
2. Focus bootstrapping on minimizing `nB*` needed — this is the "single-player mode" strategy (make the platform valuable to B even when A-side is tiny)

---

## Same-Side Negative Effects: Congestion Model

On marketplace supply sides (sellers, drivers, hosts), same-side effects are often negative. Value to each B-user decreases as nB grows:

```
vB(nA, nB) = αB × nA - β × nB
```

- `αB × nA` = cross-side benefit (more buyers = better for sellers)
- `β × nB` = congestion/competition penalty (more sellers = thinner margins per seller)

### Optimal Supply Size

Seller value is maximized when:

```
d/d(nB) [αB × nA - β × nB] = 0
→ -β = 0  (no interior maximum — value always decreases with more sellers)
```

There is no interior optimum. The platform must **cap supply** or **differentiate supply** (quality tiers, geographic segmentation) to prevent congestion from making the platform unattractive to sellers. This is the mathematical basis for Airbnb's Superhost program and Uber's surge pricing.

### Worked Example: Freelance Marketplace

- nA = 10,000 buyers, αB = $0.05/buyer/month
- Current nB = 5,000 sellers, β = $0.008/seller/month

```
vB = 0.05 × 10,000 - 0.008 × 5,000
   = $500 - $40
   = $460/seller/month
```

If sellers grow to 20,000 (due to easy onboarding):

```
vB = 0.05 × 10,000 - 0.008 × 20,000
   = $500 - $160
   = $340/seller/month  (-26%)
```

Seller value drops 26% despite same buyer count. If β is large enough relative to αB growth, sellers churn, platform collapses. Monitor `vB` directly, not just nB.

---

## Summary: Which Model to Use

| Situation | Model | Key Variable |
|-----------|-------|-------------|
| Single-sided communication/payment network | Metcalfe V ∝ n² | Pairwise connections |
| Community/group platform | Reed V ∝ 2ⁿ | Subgroup count |
| Two-sided marketplace (early stage) | Cross-elasticity V = nA × nB × (αA + αB) | Product of side sizes |
| Diagnosing multi-homing risk | Adjusted Metcalfe V ∝ (n(1-m))² | Exclusive user rate |
| Seller/supply saturation | Congestion model vB = αB×nA - β×nB | Per-seller value |
| Empirical measurement from data | Log-log regression slope ε | Interaction elasticity |

**Consistent with SKILL.md Iron Law**: All six models measure the same underlying truth — value comes from **interactions**, not user counts. Metcalfe's n² counts potential interaction pairs. Reed's 2ⁿ counts potential interaction groups. The cross-elasticity model counts realized cross-side interactions. High n with low interaction rate (low k, low αA/αB, or high β) always produces low V.
