---
name: "algo-rank-trueskill"
description: "Implement TrueSkill rating system for multiplayer and team-based competitive ranking. Use this skill when the user needs to rate players in team games, handle multiplayer (non-1v1) matchups, or build a matchmaking system with uncertainty tracking — even if they say 'team rating system', 'multiplayer ranking', or 'matchmaking rating'."
metadata:
  category: "WP-44 排名演算法"
  tags: ["ranking", "trueskill", "matchmaking", "bayesian-rating"]
---

# TrueSkill Rating System

## Overview

TrueSkill (Microsoft Research) models each player's skill as a Gaussian distribution N(μ, σ²) where μ is estimated skill and σ is uncertainty. Supports teams and multiplayer (not just 1v1). Conservative rating = μ - 3σ. Uncertainty decreases with more games. Uses Bayesian inference via message passing.

## When to Use

**Trigger conditions:**
- Rating players in team-based or multiplayer (3+ participant) games
- Building matchmaking systems that balance match quality
- When you need uncertainty estimates alongside skill ratings

**When NOT to use:**
- For simple 1v1 ranking with no uncertainty (Elo is simpler)
- For non-competitive ranking (product ratings — use Wilson Score)

## Algorithm

```
IRON LAW: Skill Rating Has TWO Components — Mean AND Uncertainty
TrueSkill represents skill as N(μ, σ²). New players have high σ
(uncertain). After many games, σ shrinks (confident). The conservative
rating μ - 3σ ensures players are ranked by their LIKELY MINIMUM
skill, not their estimated average. Never use μ alone for ranking.
```

### Phase 1: Input Validation
Initialize: μ₀ = 25, σ₀ = 25/3 (default). Collect match results with team compositions and finishing order.
**Gate:** Valid match results, team compositions defined.

### Phase 2: Core Algorithm
1. For each match, compute expected outcome from team skill distributions
2. Compare actual vs expected outcome
3. Update each player's (μ, σ) using Bayesian update:
   - μ shifts toward performance (up for winners, down for losers)
   - σ decreases (less uncertain after observing outcome)
   - Amount of update is proportional to σ (uncertain players change more)
4. Conservative rank = μ - 3σ

### Phase 3: Verification
Check: σ decreases over time for active players. Top-ranked players by conservative rating win more than expected. Match quality metric (draw probability) is reasonable.
**Gate:** Rating system produces intuitive rankings, σ converges.

### Phase 4: Output
Return player ratings with uncertainty bounds.

## Output Format

```json
{
  "ratings": [{"player": "P1", "mu": 32.5, "sigma": 2.1, "conservative": 26.2, "games_played": 50}],
  "metadata": {"initial_mu": 25, "initial_sigma": 8.33, "beta": 4.17, "tau": 0.083}
}
```

## Examples

### Sample I/O
**Input:** Team [A(25,8.3), B(25,8.3)] beats Team [C(25,8.3), D(25,8.3)]
**Expected:** A,B μ increases ~2-3 pts, σ decreases ~0.5. C,D μ decreases, σ decreases. Conservative ratings adjust.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New vs veteran player | New player μ changes more | Higher σ = more uncertainty = larger updates |
| 1v1 match | Degenerates to Elo-like behavior | TrueSkill reduces to simple case for 1v1 |
| Free-for-all (8 players) | All pairs compared | Multiplayer native support, unlike Elo |

## Gotchas

- **Computational cost**: Message passing in factor graphs is more expensive than Elo. For millions of players, use approximations (EP truncation).
- **Team skill aggregation**: TrueSkill sums individual Gaussians for team skill. This assumes independence — correlated player skills (practiced teams) are undermodeled.
- **Dynamic skill**: σ only decreases. If a player's skill genuinely changes (improvement or decline), add a small drift term τ per time period to increase σ gradually.
- **Partial play**: If a player joins mid-game or leaves early, their contribution is ambiguous. Need partial-play weight extension.
- **Patent status**: TrueSkill was patented by Microsoft (expired 2024). TrueSkill 2 adds more features but check licensing.

## References

- For TrueSkill factor graph derivation, see `references/factor-graph.md`
- For matchmaking quality metrics, see `references/matchmaking.md`
