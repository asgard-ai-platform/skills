# Prospect Theory — Mathematical Reference

Kahneman & Tversky (1979) replaced Expected Utility Theory with Prospect Theory after observing that people systematically violate rational-choice axioms. The 1992 revision (Cumulative Prospect Theory, Tversky & Kahneman) fixed a technical flaw in probability weighting and is the current standard form.

---

## The Core Departure from Expected Utility

Classical Expected Utility maximizes:

```
EU = Σ p(i) · u(x(i))
```

Where `u(x)` is a concave utility function over absolute wealth levels.

Prospect Theory replaces this with:

```
V = Σ π(p(i)) · v(x(i))
```

Two key substitutions:
1. `u(x)` → `v(x)`: value function over **gains/losses relative to a reference point**, not absolute wealth
2. `p` → `π(p)`: probability weighting function that distorts objective probabilities

---

## The Value Function

### Formula

Tversky & Kahneman (1992) estimated:

```
         x^α                 if x ≥ 0  (gain domain)
v(x) =
        −λ · (−x)^β         if x < 0  (loss domain)
```

Empirically estimated parameters:
- `α = β ≈ 0.88` (diminishing sensitivity in both domains)
- `λ ≈ 2.25` (loss aversion coefficient)

### What Each Parameter Controls

| Parameter | Effect | Business Implication |
|-----------|--------|---------------------|
| `α < 1` | Concave in gains → risk-averse for gains | People prefer certain $50 over 50% chance of $100 |
| `β < 1` | Convex in losses → risk-seeking for losses | People prefer 50% chance of −$100 over certain −$50 |
| `λ ≈ 2.25` | Losses feel 2.25× heavier than equivalent gains | Framing a $10 discount as "avoiding a $10 surcharge" is more persuasive |

### Worked Example: The Reflection Effect

**Gain frame problem:**
- Option A: $500 certain gain
- Option B: 50% chance of $1,000, 50% chance of $0

Most people choose A (risk-averse). EU says they should be indifferent if utility is linear.

**Loss frame problem (same numbers, reflected):**
- Option C: $500 certain loss
- Option D: 50% chance of $1,000 loss, 50% chance of $0 loss

Most people choose D (risk-seeking). Objectively C and D have the same expected value as A and B.

**This is the reflection effect**: risk preference flips depending on whether outcomes are framed as gains or losses.

Computing V for Option A vs B:

```python
def value(x, alpha=0.88, beta=0.88, lam=2.25):
    if x >= 0:
        return x ** alpha
    else:
        return -lam * ((-x) ** beta)

# Option A: certain $500 gain
V_A = value(500)           # → 500^0.88 ≈ 191.6

# Option B: 50% × $1000 + 50% × $0
# (ignoring probability weighting for now)
V_B = 0.5 * value(1000) + 0.5 * value(0)
    # → 0.5 × 1000^0.88 + 0 ≈ 0.5 × 354.8 ≈ 177.4

# V_A > V_B → predicts preference for certain gain ✓
```

---

## The Probability Weighting Function

Objective probabilities are not used directly. Instead, they are transformed by:

```
π(p) = p^γ / [p^γ + (1−p)^γ]^(1/γ)
```

Estimated: `γ ≈ 0.65` for gains, `δ ≈ 0.69` for losses (Tversky & Kahneman 1992).

### Key Properties

```
π(0) = 0        — impossible events are treated as impossible
π(1) = 1        — certain events are treated as certain
π(p) > p        — small probabilities are OVERweighted
π(p) < p        — medium-to-large probabilities are UNDERweighted
```

### Worked Table: π(p) at γ = 0.65

| Objective p | Weighted π(p) | Ratio π/p |
|-------------|--------------|-----------|
| 0.01        | 0.056        | 5.6×      |
| 0.05        | 0.131        | 2.6×      |
| 0.10        | 0.188        | 1.9×      |
| 0.30        | 0.354        | 1.2×      |
| 0.50        | 0.421        | 0.84×     |
| 0.90        | 0.710        | 0.79×     |
| 0.99        | 0.940        | 0.95×     |

```python
def pi(p, gamma=0.65):
    return p**gamma / (p**gamma + (1 - p)**gamma) ** (1 / gamma)
```

### Business Implications of Probability Weighting

**Lottery and insurance**: Both exploit probability distortion in opposite directions.
- Lottery: buyers overweight the tiny probability of winning (π(0.000001) >> 0.000001)
- Insurance: buyers overweight the tiny probability of catastrophe

**Marketing**: "1-in-100 chance to win a trip" feels more valuable than its expected value because π(0.01) ≈ 0.056 — perceived as a 1-in-18 chance.

**"99% uptime SLA"**: The 1% downtime risk is overweighted. Customers worry disproportionately about that 1%.

---

## Reference Point Dynamics

The reference point is not fixed — it shifts based on expectations, social comparisons, and context.

### Three Sources of Reference Points

| Source | Example | Design Implication |
|--------|---------|-------------------|
| Status quo | Current salary | Salary cuts feel like losses; raises feel like small gains |
| Expectation | Expected bonus amount | Delivering expected bonus = neutral; missing it = loss |
| Social comparison | Peer's salary | Learning a peer earns more resets reference point upward |

### Setting Reference Points Strategically

**Anchoring the reference point low** makes outcomes feel like gains:
- Show the "original price" ($2,000) before showing sale price ($1,400) → $600 gain framing
- Show competitor's worse feature set before showing yours → yours feels like an improvement

**Anchoring the reference point high** is dangerous:
- Overpromise and underdeliver → outcome is a loss relative to expectation, even if objectively good

---

## The Four-Quadrant Decision Pattern

Combining value function shape and probability weighting produces a predictable 2×2 pattern:

```
                HIGH probability      LOW probability
              ┌─────────────────────┬─────────────────────┐
  GAINS       │ Risk-AVERSE         │ Risk-SEEKING        │
              │ (concave gain curve)│ (overweighted prob) │
              │ → take certain gain │ → buy lottery       │
              ├─────────────────────┼─────────────────────┤
  LOSSES      │ Risk-SEEKING        │ Risk-AVERSE         │
              │ (convex loss curve) │ (overweighted prob) │
              │ → gamble to avoid   │ → buy insurance     │
              │   certain loss      │                     │
              └─────────────────────┴─────────────────────┘
```

### Worked Application: Debt Collection

A debtor owes NT$100,000. The collection agency offers a settlement.

**Offer framing A (gain frame):**
> "Pay NT$60,000 now and we'll forgive the remaining NT$40,000."

Debtor is in the upper-left quadrant (high-probability gain). Likely to accept — risk-averse, prefers certain gain.

**Offer framing B (loss frame):**
> "If you don't pay NT$60,000 now, you'll continue to owe NT$100,000."

Debtor is in the lower-left quadrant (high-probability loss). May gamble and refuse — risk-seeking to avoid a certain large loss.

**Verdict**: Framing A gets higher acceptance rates for equivalent economic offers. The reference point is set to NT$0 owed in A (a gain of NT$40,000 forgiven) vs NT$100,000 owed in B (a loss of NT$60,000).

---

## Loss Aversion: Isolating λ

The λ ≈ 2.25 estimate comes from indifference experiments. Participants were asked: "How much would you need to gain to accept a 50/50 bet to lose $X?"

For `x = $100 loss`:
- Participants required a gain of ~$225 before accepting
- Implies λ = 225/100 = 2.25

### λ Is Not Constant

Research shows λ varies by:
- **Stake size**: λ is higher for smaller stakes (people are more loss-averse about $10 than $10,000 proportionally)
- **Domain**: λ is higher for health outcomes than money
- **Individual**: ranges from ~1.4 to ~4.5 across populations

For business design, assume λ ∈ [1.5, 2.5] as a practical range. Never assume λ = 1 (standard utility theory).

---

## Practical Calculation: Evaluating a Marketing Intervention

**Scenario**: Should a subscription service use gain framing or loss framing in its re-engagement email?

**Gain frame**: "Come back and get 2 free months"  
**Loss frame**: "You're missing out on 2 months of features you've already paid for"

```python
# Simplified V calculation (ignoring probability weighting for certain outcomes)

alpha = 0.88
lam = 2.25

def v(x, alpha=alpha, lam=lam):
    if x >= 0:
        return x ** alpha
    else:
        return -lam * ((-x) ** alpha)

# Gain frame: reference point = current state (no subscription)
# Outcome: +2 months = +$20 value
V_gain = v(20)           # → 20^0.88 ≈ 14.2

# Loss frame: reference point = "already paid for it"
# Outcome: currently losing $20/month of value
V_loss = v(-20)          # → -2.25 × 20^0.88 ≈ -31.9
# Absolute value: 31.9 — the loss feels stronger

# The loss frame generates ~2.25× stronger motivation ✓
# But: loss frames can also generate negative affect toward the brand
```

**Caveat**: Stronger motivation ≠ always better. Loss frames can increase anxiety and reduce brand trust. A/B test before deploying.

---

## Common Misapplications

**Misapplication 1: Treating λ as fixed at exactly 2**

The "losses hurt twice as much" rule-of-thumb is a useful shorthand, but λ = 2.25 is an empirical average with wide individual variation. Do not design systems that require λ = 2.0 to function correctly.

**Misapplication 2: Ignoring the reference point**

"Loss framing is always stronger" is wrong. Loss framing only applies when the reference point is set above the current state. If someone has no prior expectation (zero reference point), there is no loss to frame.

**Misapplication 3: Stacking multiple loss frames**

Each additional loss frame competes for the same emotional register. One strong loss frame outperforms three weak ones. Nudge fatigue applies to loss framing specifically.

**Misapplication 4: Conflating loss aversion with risk aversion**

- **Loss aversion**: sensitivity to outcomes coded as losses vs gains (value function asymmetry)
- **Risk aversion**: preference for certainty over equal expected value (concavity of utility)

Prospect Theory has both. They are separable. A person can be loss-averse but risk-seeking (lower-left quadrant).

---

## Key Papers for Deeper Study

| Paper | Key Contribution |
|-------|-----------------|
| Kahneman & Tversky (1979), *Econometrica* | Original prospect theory; value function, probability weighting |
| Tversky & Kahneman (1992), *Journal of Risk and Uncertainty* | Cumulative Prospect Theory; rank-dependent weighting; revised parameters |
| Thaler (1980), *Journal of Economic Behavior & Organization* | Mental accounting; introduced the endowment effect |
| Kahneman, Knetsch & Thaler (1990), *Journal of Political Economy* | Endowment effect experiments (WTP vs WTA asymmetry) |
| Tom et al. (2007), *Science* | Neural basis of loss aversion in the ventral striatum |
