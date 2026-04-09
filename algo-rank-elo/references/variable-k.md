# Variable K-Factor Strategies

K-factor determines how much a single match can shift ratings. Fixed K is simple but wrong for most real systems: a newcomer's first 10 matches should move their rating more than a veteran's 500th match.

---

## The Core Problem with Fixed K

Fixed K=32 applied uniformly means:

- A 5-match newcomer oscillates wildly — one lucky win inflates their rating
- A 2000-rated veteran with 500 matches can be knocked down 32 points by a single upset, which understates their reliability
- New entrants and departing participants cause inflation/deflation because their rating trajectory is unbalanced

Variable K solves this by making update speed proportional to **how much new information a match provides**.

---

## K-Factor Decision Framework

### Primary axis: Match count (reliability)

| Matches Played | Recommended K | Rationale |
|----------------|--------------|-----------|
| 0–30           | 40           | High uncertainty; ratings must move fast to reach true level |
| 31–100         | 32           | Moderate uncertainty; standard update speed |
| 101+           | 16           | Low uncertainty; established rating; protect stability |

FIDE (chess) uses exactly this three-tier system (K=40/20/10 for Elo < 2300 / < 2400 / ≥ 2400 high-rated).

### Secondary axis: Rating level (high-rated stability)

High-rated players are well-measured. A rating of 2400 built over 300 matches should not move 32 points from a single loss. FIDE applies K=10 to players rated ≥ 2400 regardless of match count.

Decision table combining both axes:

| Matches | Rating < threshold | Rating ≥ threshold |
|---------|-------------------|-------------------|
| 0–30    | K = 40            | K = 40            |
| 31–100  | K = 32            | K = 16            |
| 101+    | K = 16            | K = 10            |

Set the "high-rated threshold" at the natural elite boundary for your domain (2400 in chess, can be ~1800 for smaller pools).

---

## Worked Example

Three players, all start at 1500.

**Setup:**
- Alice: 5 matches played → K=40
- Bob: 80 matches played → K=32
- Carol: 200 matches played → K=16

**Match 1: Alice (1500) beats Carol (1500)**

```
E_Alice = 1 / (1 + 10^((1500-1500)/400)) = 0.5
S_Alice = 1 (win)

R_Alice_new = 1500 + 40 × (1 - 0.5) = 1500 + 20 = 1520
R_Carol_new = 1500 + 16 × (0 - 0.5) = 1500 - 8 = 1492
```

Note: **not zero-sum**. Alice gains 20, Carol loses 8. Net: +12 points injected.

This is intentional for newcomers — they need to rise fast. The tradeoff is mild rating inflation; see [Inflation Mitigation](#inflation-mitigation) below.

**Match 2: Bob (1500) beats Carol (1492)**

```
E_Bob = 1 / (1 + 10^((1492-1500)/400)) = 1 / (1 + 10^(-0.02)) = 0.511
S_Bob = 1

R_Bob_new = 1500 + 32 × (1 - 0.511) = 1500 + 15.6 = 1516
R_Carol_new = 1492 + 16 × (0 - 0.489) = 1492 - 7.8 = 1484
```

---

## Formula: Dynamic K by Match Count

If you want a smooth curve rather than tiers:

```
K(n) = K_min + (K_max - K_min) × exp(-n / τ)
```

Where:
- `n` = matches played
- `K_min` = floor K for established players (e.g. 16)
- `K_max` = starting K for newcomers (e.g. 48)
- `τ` = decay constant (e.g. 50 — after 50 matches, K drops to ~37% of its starting excess)

Example values at τ=50, K_min=16, K_max=48:

| n  | K(n) |
|----|------|
| 0  | 48.0 |
| 10 | 42.2 |
| 30 | 33.6 |
| 50 | 27.8 |
| 100| 20.1 |
| 200| 16.3 |

Smooth decay avoids the discontinuity where a player crosses a tier boundary and suddenly their K drops — which can cause rating manipulation (intentionally losing to stay in a higher-K tier).

---

## Inflation Mitigation

Variable K breaks zero-sum when newcomers have K > established players. The newcomer gains more points than their opponent loses. Over time, the total rating pool grows.

**Option 1: Rating floor injection**
Accept the inflation; periodically recalibrate by resetting all ratings proportionally toward the mean. Simple, but disrupts user expectations.

**Option 2: Symmetric K**
When K_winner ≠ K_loser, use the *winner's K* for the winner and the *loser's K* for the loser, but track the delta:

```
loser_loss = K_loser × (E_loser - S_loser)   # this is always negative
winner_gain = K_winner × (S_winner - E_winner) # always positive
net_injection = winner_gain - abs(loser_loss)
```

If net_injection > 0, deduct it from the winner's gain proportionally. Keeps zero-sum while still letting newcomers move faster on *losses* (not just wins).

**Option 3: Provisional period**
Keep newcomers in a "provisional" pool with their own K. Provisional ratings are displayed but flagged. After 30 matches, graduate them to the main pool with a one-time K flush. This is what most chess federations use.

For most applications, Option 3 is simplest to implement and explain.

---

## Implementation Snippet

```python
def get_k_factor(matches_played: int, rating: float,
                 high_rating_threshold: float = 2400) -> float:
    """Three-tier K-factor (FIDE-style)."""
    if matches_played <= 30:
        return 40
    if rating >= high_rating_threshold:
        return 10
    if matches_played <= 100:
        return 32
    return 16


def update_elo(r_a: float, r_b: float,
               score_a: float,
               k_a: float, k_b: float) -> tuple[float, float]:
    """
    score_a: 1=win, 0.5=draw, 0=loss (for player A)
    Returns (new_r_a, new_r_b).
    Not zero-sum when k_a != k_b.
    """
    e_a = 1 / (1 + 10 ** ((r_b - r_a) / 400))
    e_b = 1 - e_a
    score_b = 1 - score_a
    new_r_a = r_a + k_a * (score_a - e_a)
    new_r_b = r_b + k_b * (score_b - e_b)
    return new_r_a, new_r_b
```

Usage:

```python
# Alice (5 matches) beats Carol (200 matches)
k_alice = get_k_factor(matches_played=5, rating=1500)   # → 40
k_carol = get_k_factor(matches_played=200, rating=1500) # → 16

new_alice, new_carol = update_elo(1500, 1500, score_a=1.0, k_a=40, k_b=16)
# new_alice = 1520.0, new_carol = 1492.0
```

---

## Common Mistakes

**Applying K reduction too early.** If you drop to K=16 after 30 matches, underrated newcomers get stuck below their true level. Use 30 matches as the provisional threshold only when combined with a higher initial K (≥ 40).

**Using rating level as the sole axis.** A player who has played 500 matches all at K=32 and reached 1800 should have a lower K than a newcomer who has played 5 matches and is temporarily at 1800 due to variance. Match count is a more reliable signal than current rating.

**Symmetric K in the presence of rating tiers.** If Alice (K=40) loses to Carol (K=16), Carol gains 16×0.5=8 and Alice loses 40×0.5=20. Net: −12 rating points removed from the pool. This is deflation. Track it.

**Forgetting to update K bucket after each match.** If you cache the K value at session start and process 30 matches in a batch, a newcomer might transition tiers mid-batch. Recompute K before each match.

---

## When Fixed K Is Acceptable

- Pool is stable: participants rarely enter or leave
- All participants have a similar match history (no newcomers)
- You need simplicity and explainability above accuracy

In those cases, K=32 is a sensible default with no further tuning required.
