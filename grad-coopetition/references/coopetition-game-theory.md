# Coopetition Game Theory Foundations

Co-opetition draws on **cooperative game theory** — specifically the theory of coalition formation and value distribution — rather than the non-cooperative Nash equilibrium tradition. Understanding this distinction is essential to applying the framework correctly.

---

## Non-Cooperative vs. Cooperative Game Theory

| Dimension | Non-Cooperative (Nash) | Cooperative (Co-opetition) |
|---|---|---|
| Unit of analysis | Individual strategies | Coalitions of players |
| Outcome | Equilibrium strategies | Division of jointly-created value |
| Assumption | Players act independently | Players can form binding agreements |
| Key concept | Best response, Nash equilibrium | Core, Shapley value, added value |
| Porter relevance | High (rivalry analysis) | Low |
| Brandenburger/Nalebuff relevance | Partial (Tactics lever) | High (Added Value lever) |

Co-opetition uses cooperative game theory for **who captures how much value** and borrows non-cooperative concepts only when analyzing tactical signaling (the T in PARTS).

---

## The Characteristic Function: Defining the Game

A cooperative game is defined by:
- A set of players **N** = {1, 2, ..., n}
- A characteristic function **v(S)** that assigns a value to every coalition S ⊆ N

**v(S)** = the total value coalition S can create *on its own*, without the remaining players.

### Worked Example: Simple Supply Chain Game

Players: Buyer (B), Seller (S), Complementor (C)

Suppose:
- Buyer values the product at **$100**
- Seller's cost to produce = **$40**
- Complementor (e.g., software that makes hardware more useful) adds **$30** to buyer's valuation

Characteristic values:

| Coalition | v(S) | Reasoning |
|---|---|---|
| {B} | 0 | Buyer alone captures nothing without a transaction |
| {S} | 0 | Seller alone captures nothing without a buyer |
| {C} | 0 | Complementor alone captures nothing |
| {B, S} | 60 | Buyer pays up to $100, seller costs $40; surplus = $60 |
| {B, C} | 0 | No product to buy; C's value unrealized |
| {S, C} | 0 | No buyer |
| {B, S, C} | 90 | Buyer now values at $130 (product + complement); seller still costs $40; surplus = $90 |

**Key observation**: v({B,S,C}) = 90 > v({B,S}) + v({C}) = 60. The complementor *creates* $30 of additional value. This is why complementors belong in the Value Net.

---

## Added Value: The Game-Theoretic Definition

Brandenburger and Nalebuff define **Added Value** formally as:

```
AV(i) = v(N) − v(N \ {i})
```

Where:
- **v(N)** = value of the grand coalition (everyone)
- **v(N \ {i})** = value of the coalition without player i
- **AV(i)** = player i's marginal contribution to the grand coalition

Using the numbers above:

| Player | v(N) | v(N \ {i}) | AV(i) |
|---|---|---|---|
| Buyer (B) | 90 | v({S,C}) = 0 | 90 |
| Seller (S) | 90 | v({B,C}) = 0 | 90 |
| Complementor (C) | 90 | v({B,S}) = 60 | 30 |

**The Iron Law implication**: No player can capture more than their added value. The complementor cannot negotiate more than $30 — the exact value they add to the game. This gives a *ceiling* on bargaining outcomes, not a precise prediction.

Note: AV(B) + AV(S) + AV(C) = 210 > 90 = v(N). This is normal; individual added values can sum to more than total value when players are interdependent (each is essential). It means multiple division points are feasible — there is no unique "correct" split.

---

## The Core: Which Allocations Are Stable?

An allocation (x_B, x_S, x_C) is in the **core** if:
1. **Feasibility**: x_B + x_S + x_C = v(N) = 90
2. **Individual rationality**: each x_i ≥ v({i}) = 0
3. **Coalition rationality**: for every coalition S, Σ x_i (i ∈ S) ≥ v(S)

Check coalition {B,S}:
- Constraint: x_B + x_S ≥ v({B,S}) = 60
- Therefore: x_C ≤ 90 − 60 = **30** ✓ (consistent with AV(C) = 30)

The core establishes that the complementor can capture **at most $30** — any more, and the buyer and seller would jointly defect and form their own coalition.

### What Happens When the Core Is Empty?

If no stable allocation exists (all coalitions can defect profitably), the game is said to have an **empty core**. This signals:
- Chronic instability in the value network
- Alliances that will constantly reform
- Need to change the game via PARTS rather than negotiate within it

**Practical test**: if you cannot find a value split where every sub-coalition is better off staying in the grand coalition, your current value network has an empty core. Fix: change the rules (R in PARTS) to make defection costly, or add a complementor to change v(S) for key coalitions.

---

## The Shapley Value: A Unique Fair Division

When the core is non-empty but has multiple feasible splits, the **Shapley value** provides one principled answer. It gives each player their *average marginal contribution* across all possible orderings of player entry.

Formula for player i:

```
φ_i = Σ_{S ⊆ N\{i}} [ |S|! (|N|−|S|−1)! / |N|! ] × [v(S ∪ {i}) − v(S)]
```

For our 3-player game, there are 3! = 6 orderings:

| Order | Marginal contribution of C |
|---|---|
| B → S → C | v({B,S,C}) − v({B,S}) = 90 − 60 = **30** |
| B → C → S | v({B,C,S}) − v({B,C}) = 90 − 0 = **90** |
| S → B → C | v({S,B,C}) − v({S,B}) = 90 − 60 = **30** |
| S → C → B | v({S,C,B}) − v({S,C}) = 90 − 0 = **90** |
| C → B → S | v({C,B,S}) − v({C,B,S\C ∪ C}) = tricky: v({C,B,S}) − v({B,C}) = 90 − 0 = **90** |
| C → S → B | v({C,S,B}) − v({S,C}) = 90 − 0 = **90** |

φ_C = (30 + 90 + 30 + 90 + 90 + 90) / 6 = 420 / 6 = **70**

Wait — this exceeds the core constraint of ≤ 30. This means the Shapley value falls *outside* the core for this specific game, which is possible. The Shapley value is normatively "fair" but not necessarily stable.

**Practical implication**: when Shapley value > core allocation for a player, that player has bargaining leverage *in theory* but cannot actually capture it without destabilizing the coalition. The core constraint is the binding constraint in practice.

---

## Non-Cooperative Concepts: When Nash Equilibrium Applies in PARTS

The PARTS framework's **Tactics lever** is where non-cooperative game theory re-enters. Two specific mechanisms:

### 1. Commitment as a Binding Move

In a sequential game, a credible commitment changes the game tree. If Firm A publicly commits to match any competitor price cut (most-favored-nation clause), it eliminates the incentive for competitors to cut price. The Nash equilibrium of the resulting game differs from the game without the commitment.

```
Without MFN clause:
  Competitor cuts price → A must respond or lose share → Price war
  Nash equilibrium: lower prices for all

With MFN clause:
  Competitor knows A must match → cutting price also cuts competitor margin
  Nash equilibrium: stable prices
```

The MFN clause is a **Rules change** (R in PARTS) that alters Nash equilibria via commitment.

### 2. Signaling and Information Asymmetry

When one player has private information, signaling games (a non-cooperative concept) determine whether communication is credible. The co-opetition insight is that *revealing* information to a complementor can be mutually beneficial, while revealing it to a competitor is dangerous.

Decision rule for information sharing:

| Recipient | Sharing increases their AV? | Sharing decreases your AV? | Action |
|---|---|---|---|
| Complementor | Yes | No | Share; grows total v(N) |
| Complementor | Yes | Yes | Negotiate IP firewall first |
| Competitor | Yes | Yes | Do not share |
| Competitor | No | No | Share only if Rules benefit (e.g., standard-setting) |

---

## Superadditivity and When It Breaks Down

Standard cooperative game theory assumes **superadditivity**:

```
v(S ∪ T) ≥ v(S) + v(T) for all disjoint S, T
```

Cooperation is always weakly beneficial. In practice, superadditivity can fail when:

1. **Integration costs** exceed synergies (merger destroys value)
2. **Regulatory barriers** prevent certain coalitions (antitrust blocks a merger)
3. **Cultural incompatibility** in alliances creates negative joint value

When you observe sub-additivity in a specific coalition, do NOT force that cooperation. The PARTS move is to either fix the integration mechanism or de-link the games (Scope lever).

---

## Transferable vs. Non-Transferable Utility

The framework above assumes **transferable utility (TU)** — value created can be redistributed freely via side payments. This is the clean case.

In practice, **non-transferable utility (NTU)** constraints appear as:

| Constraint | Example | PARTS lever to address it |
|---|---|---|
| Regulatory (cannot pay a regulator) | Pharma alliance with price controls | Rules — change regulatory environment |
| Reputational (cash payment signals low quality) | Luxury brand licensing fee caps | Tactics — restructure deal as equity |
| Operational (cannot transfer factory efficiency) | JV with knowledge transfer limits | Scope — narrow the cooperation perimeter |

When diagnosing a stuck negotiation, check whether the parties are in a TU game or an NTU game. Many failed alliances are TU analyses applied to NTU situations.

---

## Quick Diagnostic: Which Game-Theoretic Concept Applies?

```
What are you analyzing?
│
├─ Who should be in the game? ──────────────────── Added Value (AV(i))
│
├─ Will this allocation hold? ──────────────────── Core stability check
│
├─ What is "fair" if multiple splits are stable? ── Shapley value
│
├─ Can we make a move that changes equilibrium? ─── Commitment / Nash
│
└─ Is this TU or NTU? ──────────────────────────── Check regulatory/operational constraints
```

---

## Limitations of the Framework

- **v(S) is rarely observable**: characteristic function values must be estimated. Errors compound when computing Shapley values.
- **Shapley assumes symmetric probability over orderings**: in real negotiations, bargaining power is not symmetric. Shapley is a normative benchmark, not a prediction.
- **The core can be empty or very large**: when the core is large, game theory underdetermines the outcome. Negotiation, culture, and relationship history fill the gap — none of which are in the model.
- **Dynamic games**: PARTS is explicitly about changing the game over time; standard cooperative game theory is static. For repeated or dynamic games, the folk theorem (non-cooperative) or dynamic core concepts (less standard) are needed.

**Bottom line**: Use the game theory foundations for **diagnosis and bounding** (who can capture what, which allocations are stable), not for precise prediction of negotiated outcomes.
