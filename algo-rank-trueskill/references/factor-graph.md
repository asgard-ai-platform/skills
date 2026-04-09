# Factor Graph Derivation for TrueSkill

TrueSkill's core machinery is Expectation Propagation (EP) on a factor graph. This document derives the update equations from first principles and shows a complete worked example.

---

## Factor Graph Structure

A factor graph has two node types: **variable nodes** (circles) and **factor nodes** (squares). Edges connect factors to the variables they depend on.

For a single 1v1 match between Player 1 (wins) and Player 2 (loses):

```
s₁ ~ N(μ₁,σ₁²)    s₂ ~ N(μ₂,σ₂²)
     |                    |
   [f_p1]              [f_p2]      ← performance noise factors
     |                    |
    p₁                   p₂       ← performance variables
     |                    |
    [f_t1]              [f_t2]     ← team aggregation (trivial for 1-player teams)
     |                    |
    t₁                   t₂       ← team performance variables
     \                  /
       [f_diff]                   ← difference factor
           |
           d = t₁ - t₂            ← performance difference variable
           |
       [f_outcome]                ← outcome likelihood: I[d > ε]
```

### Variable Definitions

| Variable | Meaning | Prior Distribution |
|----------|---------|-------------------|
| `sᵢ` | True skill of player i | `N(μᵢ, σᵢ²)` |
| `pᵢ` | Performance in this match | `N(sᵢ, β²)` |
| `tⱼ` | Team j performance | `N(Σ μᵢ, Σ σᵢ² + nⱼβ²)` for nⱼ players |
| `d` | Performance difference (winner − loser) | `N(t₁ − t₂, σ²_t₁ + σ²_t₂)` |

### Factor Definitions

| Factor | Function |
|--------|----------|
| `f_p` | `N(pᵢ; sᵢ, β²)` — performance noise |
| `f_t` | `δ(tⱼ − Σ pᵢ)` — team sum (deterministic) |
| `f_diff` | `δ(d − (t₁ − t₂))` — difference (deterministic) |
| `f_outcome` | `I[d > ε]` for win, `I[|d| < ε]` for draw |

---

## Key Parameters

```
μ₀  = 25.0          (initial mean)
σ₀  = 25/3 ≈ 8.333  (initial std dev)
β   = σ₀/2 ≈ 4.167  (performance noise std dev)
τ   = σ₀/100 ≈ 0.0833  (skill drift per time period)
ε   = draw margin (derived from desired draw probability)
```

β controls how much a single game result matters relative to the prior. Larger β → noisier game → smaller per-game rating change. The default β = σ₀/2 means one game's uncertainty equals half the initial skill spread.

---

## Expectation Propagation Update

After marginalizing the performance and team variables (all Gaussian operations), the problem reduces to computing the posterior of `d` truncated by the outcome:

```
d ~ N(μ_d, c²)   where:
    μ_d = μ₁ − μ₂
    c²  = σ₁² + σ₂² + 2β²   (for 1v1; generalizes to team case below)
```

The truncated Gaussian moments are the only non-trivial computation. Define:

```
t = μ_d / c         (normalized difference)
ε̃ = ε / c          (normalized draw margin)
```

### V and W Functions (Win Case)

For a **win** (d > ε):

```
V_win(t, ε̃) = φ(t − ε̃) / Φ(t − ε̃)

W_win(t, ε̃) = V_win(t, ε̃) · (V_win(t, ε̃) + t − ε̃)
```

where φ is the standard normal PDF and Φ is the CDF.

### V and W Functions (Draw Case)

For a **draw** (|d| < ε):

```
V_draw(t, ε̃) = [φ(−ε̃ − t) − φ(ε̃ − t)] / [Φ(ε̃ − t) − Φ(−ε̃ − t)]

W_draw(t, ε̃) = [φ(ε̃ − t) + φ(−ε̃ − t)] / [Φ(ε̃ − t) − Φ(−ε̃ − t)]
                · V_draw(t, ε̃)     ← NOT the same formula as win case
```

Note: W_draw has a different structure because the constraint is a **bounded** interval rather than a half-line.

### Update Equations (1v1)

After computing V and W, propagate corrections back to skill variables:

**Winner (player 1):**
```
μ₁_new = μ₁ + (σ₁² / c) · V
σ₁_new² = σ₁² · [1 − (σ₁² / c²) · W]
```

**Loser (player 2):**
```
μ₂_new = μ₂ − (σ₂² / c) · V
σ₂_new² = σ₂² · [1 − (σ₂² / c²) · W]
```

The term `σᵢ² / c` is the **sensitivity weight** — players with higher σ (more uncertain) receive larger μ updates and larger σ reductions. This is why new players converge faster.

---

## Worked Example: Two New Players, First Match

Setup: Player 1 beats Player 2. Both start at `(μ=25, σ=8.333)`. No draw margin (ε=0).

### Step 1: Compute c

```
c² = σ₁² + σ₂² + 2β²
   = 8.333² + 8.333² + 2 · 4.167²
   = 69.44 + 69.44 + 34.72
   = 173.60

c  = √173.60 ≈ 13.175
```

### Step 2: Compute t

```
t = (μ₁ − μ₂) / c = (25 − 25) / 13.175 = 0.000
```

Equal players → zero normalized difference.

### Step 3: Evaluate V and W

At t=0, ε̃=0 (no draw margin):

```
φ(0) = 1/√(2π) ≈ 0.3989
Φ(0) = 0.5

V_win(0, 0) = φ(0) / Φ(0) = 0.3989 / 0.5 = 0.7979

W_win(0, 0) = V · (V + t − ε̃) = 0.7979 · (0.7979 + 0) = 0.6367
```

### Step 4: Apply Updates

Sensitivity weights:
```
σ₁²/c = 69.44 / 13.175 = 5.271
σ₁²/c² = 69.44 / 173.60 = 0.4000
```

**Winner (Player 1):**
```
μ₁_new = 25 + 5.271 · 0.7979 = 25 + 4.207 = 29.207
σ₁_new² = 69.44 · (1 − 0.4000 · 0.6367)
        = 69.44 · (1 − 0.2547)
        = 69.44 · 0.7453
        = 51.76
σ₁_new  = √51.76 ≈ 7.194
```

**Loser (Player 2):**
```
μ₂_new = 25 − 4.207 = 20.793
σ₂_new  ≈ 7.194   (same σ reduction, symmetric case)
```

### Step 5: Conservative Ratings

```
conservative₁ = μ₁_new − 3·σ₁_new = 29.207 − 3·7.194 = 29.207 − 21.582 = 7.625
conservative₂ = μ₂_new − 3·σ₂_new = 20.793 − 21.582 = −0.789
```

After one game, Player 1 ranks above Player 2 by conservative rating even though σ is still high. With 0 as the floor concept, the -0.789 signals Player 2 is still very uncertain and not yet definitively low-skilled.

---

## Team Extension

For team j with players `{i₁, i₂, ..., iₙ}`, the team performance is:

```
tⱼ ~ N(Σ μᵢ, Σ σᵢ² + n·β²)
```

The key change: `c²` now sums over ALL players across ALL teams:

```
c² = Σ_{all teams j} Σ_{players i in j} (σᵢ² + β²)
```

For a 2v2 match with teams {A,B} vs {C,D}:

```
c² = (σ_A² + β²) + (σ_B² + β²) + (σ_C² + β²) + (σ_D² + β²)
```

The V and W values are computed once per match, then each player's update uses their individual `σᵢ²/c` weight:

```
# Winning team players:
μᵢ_new = μᵢ + (σᵢ²/c) · V

# Losing team players:
μᵢ_new = μᵢ − (σᵢ²/c) · V

# All players (σ update is same direction regardless of win/loss):
σᵢ_new² = σᵢ² · [1 − (σᵢ²/c²) · W]
```

This is the structural reason why a high-σ player (newcomer) placed on an experienced team gains/loses more per game than their teammates — their individual weight `σᵢ²/c` is larger.

---

## Multiplayer Free-for-All (Rank Order)

For k teams/players with ranked finishing positions, TrueSkill decomposes the k-way outcome into k−1 pairwise comparisons between adjacent ranks:

```
Rank 1 beat Rank 2:  update (R1 vs R2) with win
Rank 2 beat Rank 3:  update (R2 vs R3) with win
...
Rank k−1 beat Rank k: update (R(k-1) vs Rk) with win
```

Each pairwise comparison uses the same V/W machinery. This is an approximation — it ignores the joint constraint that Rank 1 also beat Ranks 3, 4, ... — but it is computationally efficient and works well in practice.

The more rigorous approach integrates over all pairwise constraints simultaneously via loopy BP, but for games with ≤ 16 players the sequential-pairs approximation has negligible accuracy loss.

---

## Numerical Stability Notes

**Avoiding Φ(x) ≈ 0:** When `t − ε̃ << 0` (highly mismatched players, underdog wins), Φ(t − ε̃) approaches 0 and V blows up. Clamp V to a maximum (e.g., `V ≤ 5.0`) or equivalently clamp input `t − ε̃ ≥ −5`.

**σ floor:** After each update, `σᵢ_new² < σᵢ²` always. But over many games σ can shrink toward zero, making ratings too rigid. The dynamics factor τ prevents this by adding a small variance increment before each match:

```python
σᵢ = sqrt(σᵢ² + τ²)   # applied before match, not after
```

With `τ = σ₀/100 ≈ 0.0833`, a player needs roughly `(σ₀/τ)² = 10000` games before τ becomes the dominant factor.

**W must stay in (0, 1):** W is the fractional variance reduction. If floating-point errors push W outside (0, 1), clamp to [0.0001, 0.9999] before applying the σ update.

---

## Python Implementation of Core EP Step

```python
import math

def _norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)

def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2)))

def v_win(t: float, eps: float) -> float:
    """V function for win outcome."""
    denom = _norm_cdf(t - eps)
    denom = max(denom, 1e-10)  # numerical floor
    return _norm_pdf(t - eps) / denom

def w_win(t: float, eps: float) -> float:
    """W function for win outcome."""
    v = v_win(t, eps)
    return v * (v + t - eps)

def v_draw(t: float, eps: float) -> float:
    """V function for draw outcome."""
    num = _norm_pdf(eps - t) - _norm_pdf(-eps - t)
    denom = _norm_cdf(eps - t) - _norm_cdf(-eps - t)
    denom = max(denom, 1e-10)
    return num / denom

def w_draw(t: float, eps: float) -> float:
    """W function for draw outcome."""
    v = v_draw(t, eps)
    num = _norm_pdf(eps - t) + _norm_pdf(-eps - t)
    denom = _norm_cdf(eps - t) - _norm_cdf(-eps - t)
    denom = max(denom, 1e-10)
    return (num / denom) * v   # note: different from w_win

def trueskill_1v1_update(
    mu1: float, sigma1: float,   # winner
    mu2: float, sigma2: float,   # loser
    beta: float,
    eps: float = 0.0,
    draw: bool = False,
) -> tuple:
    """
    Returns updated (mu1, sigma1, mu2, sigma2).
    """
    c_sq = sigma1**2 + sigma2**2 + 2 * beta**2
    c = math.sqrt(c_sq)
    t = (mu1 - mu2) / c
    eps_norm = eps / c

    if draw:
        v = v_draw(t, eps_norm)
        w = w_draw(t, eps_norm)
        sign1, sign2 = 1.0, 1.0   # both move toward each other
    else:
        v = v_win(t, eps_norm)
        w = w_win(t, eps_norm)
        sign1, sign2 = 1.0, -1.0

    mu1_new    = mu1 + sign1 * (sigma1**2 / c) * v
    sigma1_new = math.sqrt(sigma1**2 * (1 - (sigma1**2 / c_sq) * w))

    mu2_new    = mu2 + sign2 * (sigma2**2 / c) * v
    sigma2_new = math.sqrt(sigma2**2 * (1 - (sigma2**2 / c_sq) * w))

    return mu1_new, sigma1_new, mu2_new, sigma2_new
```

Verification against the worked example:
```python
mu1, s1, mu2, s2 = trueskill_1v1_update(25, 8.333, 25, 8.333, beta=4.167)
assert abs(mu1 - 29.207) < 0.01   # winner gains ~4.2
assert abs(mu2 - 20.793) < 0.01   # loser loses ~4.2
assert abs(s1 - 7.194) < 0.01     # both σ decrease to ~7.19
assert abs(s2 - 7.194) < 0.01
```

---

## Draw Margin Calibration

The draw margin ε is set to match a target draw probability p_draw. For 1v1 with equal-strength players:

```
p_draw ≈ 2·Φ(ε/c) − 1   (when μ₁ ≈ μ₂)
```

Solving for ε:
```
ε = c · Φ⁻¹((p_draw + 1) / 2)
```

For the default `p_draw = 0.1` (10% draws), with two fresh players:
```
Φ⁻¹(0.55) ≈ 0.1257
ε = 13.175 · 0.1257 ≈ 1.657
```

When ε = 0 (no draws allowed), V_win at equal players = 0.7979. With ε = 1.657, V_win drops to ≈ 0.66 because the outcome is less informative (draws absorb some probability mass). Larger draw margins → smaller per-game updates.
