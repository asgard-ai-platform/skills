---
name: "algo-rank-elo"
description: "Implement Elo rating system to rank items or players from pairwise comparison outcomes. Use this skill when the user needs to rank items from head-to-head matchups, build a competitive rating system, or evaluate relative quality from comparison data — even if they say 'player rating', 'ranking from comparisons', or 'competitive scoring system'."
metadata:
  category: "WP-44 排名演算法"
  tags: ["ranking", "elo", "pairwise-comparison", "rating-system"]
---

# Elo Rating System

## Overview

Elo assigns numerical ratings that update after each pairwise comparison. Winner gains points, loser loses points. The amount exchanged depends on expected vs actual outcome. Originally for chess, now used for sports, games, and A/B preference testing. Update runs in O(1) per match.

## When to Use

**Trigger conditions:**
- Ranking items from pairwise comparison data (A vs B outcomes)
- Building competitive rating systems for games or sports
- Crowdsourced quality evaluation through pairwise preferences

**When NOT to use:**
- When you have absolute scores, not pairwise comparisons (use direct ranking)
- When team dynamics matter more than individual skill (use TrueSkill)

## Algorithm

```
IRON LAW: Elo Assumes Each Matchup Is Independent and Stationary
Rating changes are based on surprise: beating a higher-rated opponent
gains more points than beating a lower-rated one. K-factor controls
update speed: high K (32) = volatile, fast adaptation. Low K (16) =
stable, slow adaptation. Choose K based on how quickly skill changes.
```

### Phase 1: Input Validation
Initialize all participants at base rating (typically 1500). Collect match results: winner, loser (or draw).
**Gate:** Valid match data, no self-matches.

### Phase 2: Core Algorithm
1. Expected score: E_A = 1 / (1 + 10^((R_B - R_A)/400))
2. Actual score: S_A = 1 (win), 0.5 (draw), 0 (loss)
3. Update: R_A_new = R_A + K × (S_A - E_A)
4. Process all matches sequentially (order matters for sequential Elo)

### Phase 3: Verification
Check: total rating points conserved (zero-sum). Rating distribution is reasonable (no extreme values from data errors).
**Gate:** Ratings conserved, top-ranked items pass sanity check.

### Phase 4: Output
Return sorted ratings with confidence indicators.

## Output Format

```json
{
  "ratings": [{"id": "player_A", "rating": 1720, "matches": 50, "wins": 35, "losses": 15}],
  "metadata": {"k_factor": 32, "initial_rating": 1500, "total_matches": 500}
}
```

## Examples

### Sample I/O
**Input:** Player A (1500) beats Player B (1500), K=32
**Expected:** E_A = 0.5, S_A = 1. R_A_new = 1500 + 32×(1-0.5) = 1516. R_B_new = 1484.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| 1500 beats 2000 | Large rating gain (~29 pts at K=32) | Huge upset, large surprise |
| 2000 beats 1500 | Small rating gain (~3 pts at K=32) | Expected outcome, minimal surprise |
| Draw between equals | No change | Expected outcome exactly matches actual |

## Gotchas

- **K-factor selection**: Too high = ratings oscillate. Too low = slow to reflect actual skill changes. Use variable K: higher for new participants, lower for established ones.
- **Order dependence**: Sequential Elo ratings depend on match processing order. For batch processing, use iterative Elo or Bradley-Terry model.
- **Inflation/deflation**: In open systems where participants enter/leave, average rating can drift. Use rating floors or periodic calibration.
- **Not designed for teams**: Standard Elo is for 1v1. For teams, average team ratings or use TrueSkill which models individual contribution within teams.
- **Rating ≠ win probability**: A 200-point rating gap implies ~76% expected win rate, but actual outcomes depend on context, form, and luck.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/elo.py` | Update Elo ratings (single match or batch) with zero-sum verification | `python scripts/elo.py --help` |

Run `python scripts/elo.py --verify` to execute built-in sanity tests.

## References

- For Bradley-Terry model (batch Elo), see `references/bradley-terry.md`
- For variable K-factor strategies, see `references/variable-k.md`
