# Mechanism Design Basics

Mechanism design is "reverse game theory": instead of analyzing a given game, you **design the rules of the game** to produce a desired outcome. The designer moves first by choosing a mechanism; players then play the resulting game.

## The Core Problem

In standard game theory analysis, payoffs and rules are fixed — you predict behavior. In mechanism design, you control the rules and want to engineer a specific equilibrium.

**Setting**: A designer wants outcome `o*` (e.g., efficient allocation, maximum revenue). Players have **private information** (types `θᵢ`) the designer cannot observe. The designer must get players to **voluntarily reveal** their private information and act accordingly.

```
Designer goal: choose mechanism M = (message space, outcome rule)
               such that truthful reporting is a Nash Equilibrium
               and the resulting outcome is desirable.
```

## The Two Binding Constraints

Every viable mechanism must satisfy both conditions simultaneously:

### 1. Incentive Compatibility (IC)
Each player maximizes their payoff by reporting their true type `θᵢ`.

```
IC: u_i(θ_i, θ_i) ≥ u_i(θ̂_i, θ_i)   for all θ_i, θ̂_i
```

In plain language: no player gains by lying. If IC fails, the mechanism breaks down because players game it.

### 2. Individual Rationality (IR)
Each player prefers to participate over not participating.

```
IR: u_i(θ_i, θ_i) ≥ u_i(outside option)   for all θ_i
```

In plain language: no player is forced to lose by joining. If IR fails, players opt out.

**IRON LAW**: A mechanism that violates IC or IR fails in practice, even if the "right" outcome looks good on paper. Check both before claiming a mechanism works.

---

## The Revelation Principle

> **Any outcome achievable by any mechanism can also be achieved by a direct, incentive-compatible mechanism in which players simply report their types.**

This is the most important theorem in mechanism design. It means you can restrict your search to **direct revelation mechanisms** (DRM) without loss of generality:
- Designer asks: "what is your type?"
- Players respond with a report `r_i`
- Designer maps reports to outcomes

You don't need to consider elaborate message spaces, auctions with bidding rounds, or indirect schemes — if the outcome is achievable, it's achievable with simple truth-telling.

**Practical implication**: To design a mechanism, just find an IC + IR allocation rule. The message space is always "report your type."

---

## Worked Example: Efficient Public Good Provision

**Situation**: A firm is deciding whether to invest in a quality-improvement project. Two business units (BU-A, BU-B) each privately know their benefit. The project costs 120 and benefits are either High (100) or Low (20).

**The designer wants**: Build the project if and only if total benefit ≥ 120.

**The naive approach (fails)**: Just ask each BU their benefit. Both will underreport to avoid paying the cost.

**Mechanism design solution**: Use the **Vickrey-Clarke-Groves (VCG) mechanism**.

### VCG Mechanism — Step by Step

**Step 1 — Collect reports**

Each BU reports their benefit: `r_A` and `r_B`.

**Step 2 — Make the efficient decision**

Build the project if `r_A + r_B ≥ 120`, don't build otherwise.

**Step 3 — Charge each player a VCG tax**

The VCG tax charges each player the **externality they impose on others**:

```
Tax_i = [Optimal social welfare WITHOUT player i] − [Welfare of others in the chosen outcome]
```

For player A:
```
Tax_A = max(r_B, 0) − max(r_A + r_B − 120, 0) × 0 − ...
```

Simplified for the binary case:

| r_A | r_B | Build? | Tax_A | Tax_B |
|-----|-----|--------|-------|-------|
| 100 | 100 | Yes | max(0, 120 − 100) = 20 | 20 |
| 100 | 20  | No  | 0 | 0 |
| 20  | 100 | No  | 0 | 0 |
| 20  | 20  | No  | 0 | 0 |

**Step 4 — Verify IC**

When BU-A's true benefit is 100 and BU-B reports 100:
- Truth: Project built, BU-A gets 100 − 20 = **80**
- Lie (report 20): Project NOT built, BU-A gets 0

Truth-telling is strictly better. IC holds.

When BU-A's true benefit is 20 and BU-B reports 100:
- Truth: Project NOT built (20 + 100 = 120, borderline — assume exactly 120 means build)
- BU-A gets 20 − 0 = **20** (gets benefit, pays no tax because 120 − 100 = 20 tax, net = 0)

**Step 5 — Verify IR**

VCG taxes are always ≥ 0, and each player receives their full value when the project is built. IR holds.

### VCG Properties

| Property | Holds? | Notes |
|----------|--------|-------|
| Incentive Compatible | ✓ | Truth-telling is dominant strategy |
| Individual Rational | ✓ | No player is made worse off |
| Efficient | ✓ | Project built iff total benefit ≥ cost |
| Budget Balanced | ✗ | Designer may collect less than project cost |

The **budget balance failure** is VCG's main weakness. Total taxes collected may not cover the project cost — a subsidy may be required from the designer.

---

## Auction Design as Mechanism Design

The most practical application. Seller wants to allocate a good to the highest-value buyer and maximize revenue.

### Second-Price (Vickrey) Auction

**Rules**: Highest bidder wins; pays the second-highest bid.

**Why it works (IC proof)**:

Suppose your true value is `v`. You bid `b`. The highest other bid is `m`.

**Case 1**: `v > m` (you're the highest-value buyer)
- Bid `b > m`: You win, pay `m`. Payoff = `v − m > 0`. ✓
- Bid `b < m`: You lose. Payoff = 0. Worse. ✗
- Bid truthfully `b = v`: You win, pay `m`. Same as above. ✓

**Case 2**: `v < m` (you're NOT the highest-value buyer)
- Bid `b < m`: You lose. Payoff = 0.
- Bid `b > m`: You win, pay `m > v`. Payoff = `v − m < 0`. Worse. ✗
- Bid truthfully `b = v < m`: You lose. Payoff = 0. Same. ✓

Conclusion: bidding your true value is a **dominant strategy**. The second-price auction is incentive compatible regardless of others' strategies.

### First-Price vs. Second-Price Comparison

|  | First-Price | Second-Price |
|--|-------------|--------------|
| Payment rule | Pay your bid | Pay second-highest bid |
| Dominant strategy | No (shade your bid) | Yes (bid true value) |
| Designer's expected revenue | Equal (Revenue Equivalence Theorem) | Equal |
| Simplicity | Simple payment rule | Simple strategy for bidders |
| Common use | Government contracts, procurement | Google Ads (hybrid), art auctions |

**Revenue Equivalence Theorem**: Under regularity conditions (symmetric, risk-neutral bidders with iid private values), all standard auction formats yield the **same expected revenue** to the seller. This is a powerful negative result — you cannot gain revenue by choosing an exotic auction format; you gain by improving participation or information.

---

## Mechanism Design for Incentive Problems (Inside Firms)

Beyond auctions, mechanism design applies to any principal-agent setting.

**Setup**: Principal (manager) wants Agent (employee) to exert effort `e`. Agent privately knows their cost of effort `c(e)`. Principal observes output `q = e + noise`, not effort directly.

### The Optimal Contract Structure

The principal offers a menu of contracts `{(w_L, w_H)}`:
- `w_H` = wage if output is high
- `w_L` = wage if output is low

**IC constraint**: Agent prefers the contract designed for their type over misrepresenting.

**IR constraint**: Agent prefers any contract over quitting (outside wage `ū`).

**Optimal contract tradeoff**:

```
High-effort agent: full insurance impossible → faces risk (w_H > w_L)
Low-effort agent: offered a flat wage (w_H = w_L = ū)
```

The principal deliberately makes the high-effort contract "risky" to deter low-effort agents from claiming it. This is **screening**: using contract structure to separate types.

### Practical Application: Sales Commission Design

| Agent type | Optimal structure | Why |
|------------|------------------|-----|
| High-effort salesperson | Base + high variable commission | IC: low-effort rep won't accept the risk |
| Risk-averse salesperson | Higher base, lower commission | IR: must offer enough insurance to retain them |
| Ambiguous productivity | Offer a menu: low-base/high-commission OR high-base/low-commission | Let agents self-select their type |

**The screening menu principle**: Never offer only one contract if agent types differ. A menu forces agents to reveal their type through self-selection, giving you more information at no cost.

---

## Common Failure Modes

**Gaming the message space**: If you don't use a direct revelation mechanism, players find indirect ways to signal false types. Fix: switch to a DRM where the only message is "report your type."

**IC without IR**: A mechanism can be perfectly incentive compatible but players still opt out. Always check the outside option. If agents can quit, IR is binding.

**IR without IC**: Agent participates but misreports to get a better deal. Participation alone doesn't mean honesty.

**Ignoring multi-dimensionality**: VCG and Vickrey auctions work cleanly with one-dimensional types (single value). When agents have multi-dimensional private information (e.g., both valuation and cost), the mechanism design problem becomes much harder and closed-form solutions rarely exist.

**Budget balance vs. efficiency trade-off (Myerson-Satterthwaite)**: For bilateral trade with private values, no mechanism can simultaneously achieve efficiency, IC, IR, and budget balance. You must sacrifice one. In practice, most markets sacrifice efficiency (gains from trade are sometimes left on the table) to maintain budget balance and participation.

---

## Quick Decision Guide

```
What do you want to design?          →  Mechanism type to use

Sell one item to highest-value buyer →  Second-price auction (dominant strategy IC)
Maximize revenue from auction        →  Myerson optimal auction (virtual values)
Allocate public good efficiently     →  VCG (may require subsidy)
Screen agent effort types            →  Contract menu (high/low base-commission)
Match workers to jobs                →  Deferred acceptance algorithm (stable matching)
Elicit honest expert forecasts       →  Proper scoring rule (Brier score, log score)
```

---

## Key Formulas Reference

**VCG tax for player i**:
```
t_i(r) = max_{x} Σ_{j≠i} v_j(x, r_j) − Σ_{j≠i} v_j(x*(r), r_j)
```
where `x*(r)` is the efficient outcome given reports `r`, and the first term is the best outcome for others if player i didn't exist.

**Myerson virtual value** (for revenue-maximizing auctions):
```
ψ(v) = v − (1 − F(v)) / f(v)
```
where `F(v)` is the CDF of buyer valuations and `f(v)` is the PDF. Sell to the buyer with the highest positive virtual value.

**Brier scoring rule** (eliciting honest probability forecasts):
```
Score = 1 − (forecast − outcome)²
```
Maximized in expectation by reporting your true probability belief. Use this whenever you need honest probability estimates from agents who might otherwise shade their forecasts.
