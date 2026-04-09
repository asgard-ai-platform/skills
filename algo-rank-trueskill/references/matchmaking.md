# Matchmaking Quality Metrics

## What "Match Quality" Means in TrueSkill

TrueSkill defines match quality as the **probability of a draw** between the proposed teams. A draw is used as proxy for "evenly matched" — if neither team has a clear advantage, the draw probability is highest. This is not about whether draws literally occur in the game; it is a continuous fairness score in [0, 1].

High quality → teams are evenly matched → match outcome is informative → ratings update meaningfully.
Low quality → a strong team faces a weak team → outcome is nearly certain → little information gained.

---

## Match Quality Formula

### 2-Team Case

For Team 1 with players indexed *i* and Team 2 with players indexed *j*:

```
Δμ = Σ μ₁ᵢ  −  Σ μ₂ⱼ          (team mean difference)

σ²_diff = Σ σ²₁ᵢ + Σ σ²₂ⱼ      (sum of all player variances)

q = sqrt(2β² / (2β² + σ²_diff))
  × exp(−Δμ² / (2 × (2β² + σ²_diff)))
```

Where **β** is the "performance noise" parameter (default: `β = σ₀/2 = 25/6 ≈ 4.17`). β models how much luck / per-game randomness exists on top of skill. High-luck games should use a larger β.

The first term penalizes **uncertainty** (wide σ → lower quality).
The second term penalizes **skill imbalance** (large Δμ → lower quality).

### Interpretation

| q value | Meaning |
|---------|---------|
| > 0.50  | Excellent match — nearly coin-flip |
| 0.30–0.50 | Acceptable |
| 0.10–0.30 | Unbalanced — use only when queue is thin |
| < 0.10  | Do not create this match if alternatives exist |

These thresholds are empirical. Microsoft's original Xbox Live deployment used ~0.50 as the ideal target.

---

## Worked Example: 2v2 Match

**Players:**

| Player | μ    | σ   |
|--------|------|-----|
| A      | 30.0 | 3.0 |
| B      | 28.0 | 4.0 |
| C      | 25.0 | 5.0 |
| D      | 32.0 | 2.5 |

**Team 1:** A + B  
**Team 2:** C + D  

**Step 1 — Team means:**
```
μ_team1 = 30.0 + 28.0 = 58.0
μ_team2 = 25.0 + 32.0 = 57.0
Δμ = 58.0 − 57.0 = 1.0
```

**Step 2 — Variance sum:**
```
σ²_diff = 3.0² + 4.0² + 5.0² + 2.5²
        = 9 + 16 + 25 + 6.25
        = 56.25
```

**Step 3 — Parameters (default β = 4.17):**
```
2β² = 2 × 4.17² ≈ 34.77
denominator = 2β² + σ²_diff = 34.77 + 56.25 = 91.02
```

**Step 4 — Quality:**
```
term1 = sqrt(34.77 / 91.02) = sqrt(0.382) ≈ 0.618
term2 = exp(−1.0² / (2 × 91.02)) = exp(−0.0055) ≈ 0.9945
q = 0.618 × 0.9945 ≈ 0.615
```

**Result:** q ≈ 0.62 → excellent match. The skill gap is tiny (Δμ = 1.0), so quality is primarily limited by high σ of players C (new) and B (somewhat uncertain).

---

## Alternative Grouping

What if we swap D and B?

**Team 1:** A + D → μ = 62.0  
**Team 2:** B + C → μ = 53.0  

```
Δμ = 62.0 − 53.0 = 9.0
σ²_diff = 9 + 6.25 + 16 + 25 = 56.25   (same players, same sum)
denominator = 91.02

term1 = 0.618  (unchanged)
term2 = exp(−81 / 182.04) = exp(−0.445) ≈ 0.641
q = 0.618 × 0.641 ≈ 0.396
```

**Result:** q ≈ 0.40 → acceptable but clearly worse. This shows why A+D should not be stacked — the algorithm quantifies the imbalance.

---

## Matchmaking Procedure

Given a queue of players waiting for a match, the goal is to find a team assignment that maximizes q.

### For Small Queues (< ~20 players)

1. Generate all valid team splits from the candidate pool.
2. Compute q for each split.
3. Select the split with highest q, subject to waiting-time constraints.

For a pool of 4 players forming 2v2: there are 3 distinct splits (C(4,2)/2 = 3). Exhaustive is trivial.

### For Larger Queues

Exhaustive search is combinatorially expensive. Use greedy approaches:

```
procedure GREEDY_MATCH(queue, team_size):
  sort queue by conservative rating (μ − 3σ) descending
  
  while len(queue) >= 2 × team_size:
    # Take the top 2×team_size players as candidates
    candidates = queue[:2*team_size]
    
    # Try balanced split: top half vs bottom half
    team1 = candidates[:team_size]
    team2 = candidates[team_size:]
    q = match_quality(team1, team2)
    
    if q >= threshold:
      create_match(team1, team2)
      remove candidates from queue
    else:
      # Adjust: swap player with highest-σ on stronger team
      # with nearest-skill player on weaker team
      ...
```

Greedy sorting by conservative rating (μ − 3σ) clusters similar-skill players together before any splitting — this is the key efficiency trick.

### Waiting Time vs. Quality Tradeoff

Enforce a **quality floor that degrades with wait time**:

```python
def quality_threshold(wait_seconds: float) -> float:
    """Linearly relax quality requirement as player waits longer."""
    base_threshold = 0.50
    min_threshold  = 0.10
    decay_rate     = 0.002   # per second
    return max(min_threshold, base_threshold - decay_rate * wait_seconds)
```

After ~200 seconds of waiting, the threshold drops from 0.50 to 0.10. Tune `decay_rate` to match your game's acceptable wait time.

---

## Multi-Team Extension (Free-for-All / N-Way)

For N teams (e.g., 8-player free-for-all treated as 8 teams of 1):

TrueSkill computes quality over all **pairs** of teams:

```
q_total = product over all pairs (i, j) of:
    sqrt(2β² / (2β² + σ²ᵢ + σ²ⱼ))
    × exp(−(μᵢ − μⱼ)² / (2 × (2β² + σ²ᵢ + σ²ⱼ)))
```

For N=8 this is C(8,2) = 28 pair evaluations. Still tractable.

**Worked mini-example (3-way FFA):**

Players: A(μ=30, σ=3), B(μ=28, σ=3), C(μ=29, σ=3), β=4.17

```
Pairs: (A,B), (A,C), (B,C)

For (A,B): Δμ=2, σ²=18, denom=2×17.39+18=52.77
  pair_q = sqrt(34.77/52.77) × exp(−4/105.54) ≈ 0.812 × 0.962 = 0.781

For (A,C): Δμ=1, same σ, denom=52.77
  pair_q = 0.812 × exp(−1/105.54) ≈ 0.812 × 0.991 = 0.804

For (B,C): Δμ=1, same → 0.804

q_total = 0.781 × 0.804 × 0.804 ≈ 0.505
```

Overall match quality 0.505 → good. The skill spread (only 2 points across 3 players) produces a fair FFA.

---

## Skill Balance vs. Uncertainty in Quality

The formula combines two independent penalties. Understanding which is limiting informs action:

```
q_balance     = exp(−Δμ² / (2 × (2β² + σ²_diff)))  ← skill imbalance penalty
q_uncertainty = sqrt(2β² / (2β² + σ²_diff))          ← uncertainty penalty
q = q_balance × q_uncertainty
```

**Case 1:** q is low primarily because q_uncertainty is low  
→ Players have high σ (new to the system). Match quality will naturally improve after a few games. Do not re-queue; create the match.

**Case 2:** q is low primarily because q_balance is low  
→ Teams are skill-mismatched. Swap players or expand the candidate pool.

**Diagnostic code:**
```python
import math

def quality_components(team1, team2, beta=4.167):
    mu1 = sum(p['mu'] for p in team1)
    mu2 = sum(p['mu'] for p in team2)
    delta_mu = mu1 - mu2
    sigma_sq = sum(p['sigma']**2 for p in team1 + team2)
    denom = 2 * beta**2 + sigma_sq
    
    q_uncertainty = math.sqrt(2 * beta**2 / denom)
    q_balance = math.exp(-delta_mu**2 / (2 * denom))
    return {
        'q': q_uncertainty * q_balance,
        'q_uncertainty': q_uncertainty,
        'q_balance': q_balance,
        'limiting_factor': 'uncertainty' if q_uncertainty < q_balance else 'balance'
    }
```

---

## β Parameter Tuning

β controls how much per-game luck the model assumes. It directly affects quality scores.

| β relative to σ₀ | Interpretation | Effect on quality |
|---|---|---|
| β = σ₀/6 ≈ 1.4 | Very skill-dominant game | Quality scores are higher (skill matters, so balanced skill = good match) |
| β = σ₀/2 ≈ 4.2 | Default (moderate luck) | Baseline |
| β = σ₀ ≈ 8.3 | High luck/chaos game | Quality denominator grows; scores are more compressed toward 0.5 |

**To estimate β empirically:** Take a large sample of matches where the two teams had equal mean skill (Δμ ≈ 0). Measure the actual win rate of the "expected winner" (e.g., by random tiebreaker). If the true win rate is 55% when TrueSkill predicts 60%, β is too low.

---

## Reinforcement: Iron Law in Matchmaking Context

> **Never use μ alone for matchmaking.**

A player with μ = 30, σ = 8 is vastly different from μ = 30, σ = 1 in match quality calculations:

```
High-σ case (σ=8):   σ²_diff contribution = 64 → large denominator → lower q_uncertainty
Low-σ case (σ=1):    σ²_diff contribution = 1  → small denominator → higher q_uncertainty
```

Pairing a new player (high σ) with any opponent produces a lower quality score, correctly, because the outcome of that match carries less information. This is the system working as intended — do not override it by filtering matchmaking candidates on μ alone.
