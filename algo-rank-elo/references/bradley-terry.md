# Bradley-Terry Model

## What It Solves

Sequential Elo has an order-dependence problem: process matches A→B→C vs C→B→A and you get different final ratings, even with identical outcomes. This violates the intuition that the *set* of results should determine ratings, not the order you feed them in.

Bradley-Terry (BT) fixes this by treating the entire match history as a single optimization problem. Instead of updating ratings one match at a time, it fits a probability model to all matches simultaneously via Maximum Likelihood Estimation (MLE).

**Trade-off summary:**

| | Sequential Elo | Bradley-Terry |
|---|---|---|
| Order-dependent | Yes | No |
| Handles new matches incrementally | Yes | No (re-fit required) |
| Handles incomplete round-robins | Poor | Good |
| Computational cost | O(1) per match | O(n² · iterations) |
| Provides uncertainty estimate | No | Yes (via Fisher info) |
| Draws supported natively | With modification | Yes (Davidson extension) |

Use BT when you have a **batch of matches collected upfront** and want a stable, order-independent ranking. Use Elo when matches arrive in a stream and you need live ratings.

---

## The Model

Each participant i has a latent strength parameter β_i > 0.

The probability that i beats j in a head-to-head matchup:

```
P(i beats j) = β_i / (β_i + β_j)
```

Equivalently, defining r_i = log(β_i) (the log-strength, analogous to an Elo rating):

```
P(i beats j) = 1 / (1 + exp(r_j - r_i))
               = sigmoid(r_i - r_j)
```

This is the same logistic function Elo uses for expected score — but here we estimate all r_i jointly rather than updating them sequentially.

**Identifiability constraint:** The model is only identified up to a global shift. Fix this by anchoring one participant's rating (e.g., r_0 = 0) or by constraining sum(r_i) = 0.

---

## MLE via Iterative Reweighted Algorithm

The standard fitting algorithm (Zermelo 1929 / Ford 1957) is a fixed-point iteration:

```
β_i^(new) = W_i / Σ_{j ≠ i} (n_ij / (β_i^(old) + β_j^(old)))
```

Where:
- W_i = total wins for participant i (draws count as 0.5)
- n_ij = total matches played between i and j (n_ij = n_ji)
- Sum is over all opponents j

Repeat until convergence (|β_i^(new) − β_i^(old)| < ε for all i).

**Convergence:** Guaranteed when the comparison graph is connected (every participant is reachable from every other via match chains). If the graph is disconnected, fit each component separately.

---

## Worked Example

**Setup:** 4 players (A, B, C, D). Match results:

| Match | Winner | Loser |
|-------|--------|-------|
| A vs B | A | B |
| A vs C | A | C |
| B vs C | C | B |
| B vs D | B | D |
| C vs D | C | D |
| A vs D | A | D |

**Win counts:** A=3, B=1, C=2, D=0

D has zero wins — BT is undefined with β_D = 0. See "Zero-Win Problem" below.

**Revised setup** — give D one win to make the example tractable:

| Player | Wins | Losses | Opponents faced |
|--------|------|--------|-----------------|
| A | 3 | 0 | B, C, D |
| B | 1 | 2 | A, C, D |
| C | 2 | 1 | A, B, D |
| D | 1 | 2 | A, B, C |  ← D beats B this time |

Match counts (symmetric): n_AB=1, n_AC=1, n_AD=1, n_BC=1, n_BD=1, n_CD=1

**Iteration 0:** Initialize β = [1, 1, 1, 1]

**Iteration 1 — compute β_A:**
```
denominator = n_AB/(β_A+β_B) + n_AC/(β_A+β_C) + n_AD/(β_A+β_D)
            = 1/(1+1) + 1/(1+1) + 1/(1+1)
            = 0.5 + 0.5 + 0.5 = 1.5
β_A^(1) = W_A / denom = 3 / 1.5 = 2.000
```

**Iteration 1 — compute β_B:**
```
denom = 1/(1+1) + 1/(1+1) + 1/(1+1) = 1.5
β_B^(1) = 1 / 1.5 = 0.667
```

**Iteration 1 — compute β_C:**
```
denom = 1/(1+1) + 1/(1+1) + 1/(1+1) = 1.5
β_C^(1) = 2 / 1.5 = 1.333
```

**Iteration 1 — compute β_D:**
```
denom = 1/(1+1) + 1/(1+1) + 1/(1+1) = 1.5
β_D^(1) = 1 / 1.5 = 0.667
```

After iteration 1: β = [2.000, 0.667, 1.333, 0.667]

**Iteration 2 — compute β_A:**
```
denom = 1/(2+0.667) + 1/(2+1.333) + 1/(2+0.667)
      = 0.375 + 0.300 + 0.375 = 1.050
β_A^(2) = 3 / 1.050 = 2.857
```

**Iteration 2 — compute β_C:**
```
denom = 1/(2.857+0.667) + 1/(0.667+1.333) + 1/(1.333+0.667)
      = 0.284 + 0.500 + 0.500 = 1.284
β_C^(2) = 2 / 1.284 = 1.558
```

After several iterations (converged to 4 decimal places):

| Player | β (strength) | r = log(β) | Rank |
|--------|-------------|------------|------|
| A | 3.421 | 1.230 | 1 |
| C | 1.469 | 0.385 | 2 |
| B | 0.622 | -0.475 | 3 |
| D | 0.622 | -0.475 | 4 |

(Normalized so sum of β = 6.134; or equivalently fix β_A = 1 and scale everything else.)

**Verify win probability:** P(A beats C) = 3.421 / (3.421 + 1.469) = 0.70. A beat C in actual data ✓.

---

## Python Implementation

```python
def bradley_terry(wins: dict[str, float],
                  matches: dict[tuple[str, str], int],
                  max_iter: int = 1000,
                  tol: float = 1e-8) -> dict[str, float]:
    """
    Fit Bradley-Terry model.

    Args:
        wins:    {player: total wins} (draws count 0.5)
        matches: {(i, j): count} — symmetric, i < j alphabetically
        max_iter: max iterations
        tol:     convergence threshold on max abs change in beta

    Returns:
        {player: beta} normalized so mean(beta) = 1
    """
    players = list(wins.keys())
    beta = {p: 1.0 for p in players}

    # Build symmetric match-count lookup
    n = {}
    for (i, j), count in matches.items():
        n[(i, j)] = count
        n[(j, i)] = count

    for _ in range(max_iter):
        new_beta = {}
        for p in players:
            denom = sum(
                n.get((p, q), 0) / (beta[p] + beta[q])
                for q in players if q != p
            )
            if denom == 0:
                new_beta[p] = beta[p]
            else:
                new_beta[p] = wins[p] / denom

        # Normalize: fix mean(beta) = 1
        mean_b = sum(new_beta.values()) / len(players)
        new_beta = {p: v / mean_b for p, v in new_beta.items()}

        # Check convergence
        max_change = max(abs(new_beta[p] - beta[p]) for p in players)
        beta = new_beta
        if max_change < tol:
            break

    return beta


def win_probability(beta: dict[str, float], i: str, j: str) -> float:
    return beta[i] / (beta[i] + beta[j])
```

---

## Zero-Win and Zero-Loss Problem

If any participant has W_i = 0 (never won), MLE gives β_i → 0. Similarly, if any participant never lost, β_i → ∞. The model breaks because maximum likelihood is not finite.

**Solutions:**

1. **Add-0.5 smoothing (simplest):** Add 0.5 pseudo-wins and 0.5 pseudo-losses to every participant before fitting. This regularizes toward equal strength.

2. **Laplace prior (Bayesian):** Place a log-normal prior on β_i. Equivalent to adding a small prior match count ν against an "average" opponent with β = 1:
   ```
   β_i^(new) = (W_i + ν/2) / (Σ_{j} n_ij/(β_i+β_j) + ν/(β_i+1))
   ```
   ν = 1 is a weakly informative default.

3. **Exclude undefeated/winless from ranking:** Report them separately. Valid when the data is genuinely sparse and you don't trust the extrapolation.

---

## Handling Draws: Davidson Extension

Standard BT has no draw probability. Davidson (1970) adds a draw parameter ν ≥ 0:

```
P(i beats j) = β_i / (β_i + ν√(β_i β_j) + β_j)
P(draw)      = ν√(β_i β_j) / (β_i + ν√(β_i β_j) + β_j)
P(j beats i) = β_j / (β_i + ν√(β_i β_j) + β_j)
```

When ν = 0, this reduces to standard BT. Fit ν alongside β_i via joint MLE.

If draws are rare (< 5% of matches), the simpler approach is to count draws as 0.5 win / 0.5 loss and use standard BT without modification.

---

## Converting β to Elo-Compatible Ratings

The BT log-strength r_i = log(β_i) is directly interpretable as an Elo-like rating on any scale. To put it on the standard Elo 400-point scale:

```
Elo_i = 400 × log10(β_i) + base_rating
```

Where base_rating = 1500 by convention.

**Why 400?** In standard Elo, a 400-point gap implies P(higher beats lower) = 1/(1+10^(-1)) = 10/11 ≈ 0.909. This matches BT because:
```
P(i beats j) = 1 / (1 + 10^((r_j - r_i)/400))  ← Elo formula
             = 1 / (1 + β_j/β_i)                ← BT formula
```
These are identical when β_i = 10^(r_i/400).

**Practical conversion:**
```python
import math

def beta_to_elo(beta: dict[str, float], base: float = 1500) -> dict[str, float]:
    mean_log = sum(math.log10(v) for v in beta.values()) / len(beta)
    return {
        p: base + 400 * (math.log10(b) - mean_log)
        for p, b in beta.items()
    }
```

This centers the rating distribution at `base` (1500).

---

## When to Prefer BT over Sequential Elo

Use this decision table:

| Condition | Prefer |
|-----------|--------|
| Matches arrive in real time, need live ratings | Elo |
| Full match history available before ranking | BT |
| Match order is arbitrary / administratively determined | BT |
| You need a 95% confidence interval on ratings | BT |
| Participants enter/leave frequently | Elo (with variable K) |
| Tournament bracket with seeding that depends on ratings | Elo (BT can't update mid-tournament) |
| Sparse data (< 5 matches per participant) | BT + Laplace prior |
| Crowdsourced pairwise preferences (A/B testing) | BT |

**The one-line rule:** If you can answer "what is the final ranking over this fixed dataset?", use BT. If you need "what is the current rating after this match?", use Elo.
