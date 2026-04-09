---
name: "econ-game-theory"
description: "Apply basic game theory concepts including Nash equilibrium, dominant strategies, and the Prisoner's Dilemma to analyze strategic interactions. Use this skill when the user needs to model competitive decisions, predict rival behavior, design incentive mechanisms, or evaluate cooperation vs competition scenarios — even if they say 'what will our competitor do', 'should we cooperate or compete', or 'how do we set up the right incentives'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "game-theory", "strategy"]
---

# Game Theory Basics

## Overview

Game theory models strategic interactions where each player's outcome depends on others' choices. It provides tools to predict behavior, identify stable outcomes (equilibria), and design mechanisms that align incentives.

## Framework

```
IRON LAW: Define Players, Strategies, and Payoffs BEFORE Analyzing

Every game requires three elements explicitly defined:
1. Players — who are the decision-makers?
2. Strategies — what choices does each player have?
3. Payoffs — what does each player get for each combination of choices?

Analyzing a "game" without a payoff matrix is just storytelling.
```

### Analysis Steps

1. **Identify players** and their available strategies
2. **Build the payoff matrix** (simultaneous) or **game tree** (sequential)
3. **Check for dominant strategies** per player
4. **Find Nash Equilibrium** — where best responses intersect
5. **For sequential games**: apply backward induction from terminal nodes
6. **Evaluate efficiency** — is the NE Pareto optimal? If not, flag cooperation opportunity
3. The resulting path is the Subgame Perfect Equilibrium

## Output Format

```markdown
# Game Theory Analysis: {Situation}

## Game Setup
- Players: {list}
- Strategies: Player 1: {A, B}, Player 2: {X, Y}
- Type: Simultaneous / Sequential

## Payoff Matrix (simultaneous) or Game Tree (sequential)

|  | Player 2: X | Player 2: Y |
|---|---|---|
| Player 1: A | (a1, a2) | (b1, b2) |
| Player 1: B | (c1, c2) | (d1, d2) |

## Analysis
- Dominant strategies: {if any}
- Nash Equilibrium: {strategy combination, payoffs}
- Pareto optimal? {yes/no — if no, explain the cooperation opportunity}

## Strategic Implications
{What should each player do? What mechanism could improve outcomes?}
```

## Examples

### Correct Application
**Scenario:** Two bubble tea chains considering price cut

|  | Chain B: Hold Price | Chain B: Cut Price |
|---|---|---|
| Chain A: Hold Price | (80, 80) | (40, 100) |
| Chain A: Cut Price | (100, 40) | (60, 60) |

- Both have dominant strategy: Cut Price (100 > 80, 60 > 40)
- **Nash Equilibrium: (Cut, Cut) = (60, 60)** — a Prisoner's Dilemma ✓
- Both would prefer (Hold, Hold) = (80, 80) but can't sustain it without a binding agreement
- **Implication**: Price wars are the rational outcome. To escape, need repeated interaction (reputation), contracts, or differentiation that makes price less relevant.

### Incorrect Application
- "Our competitor will probably cooperate because it's better for everyone" → In a one-shot Prisoner's Dilemma, rational players defect. Cooperation requires repeated games or enforcement. Violates the model's prediction.

## Gotchas

- **Nash Equilibrium ≠ best outcome**: NE is stable, not optimal. The Prisoner's Dilemma NE is worse for both players than cooperation.
- **Multiple equilibria**: Many games have multiple NE. Additional criteria (focal points, risk dominance, Pareto dominance) help select among them.
- **Payoff estimation is the hard part**: The matrix is easy once payoffs are known. Estimating realistic payoffs requires market research and financial modeling.
- **Repeated games change everything**: In one-shot games, defection dominates. In repeated games, tit-for-tat and reputation effects enable cooperation.
- **Information matters**: Games with incomplete information (you don't know opponent's payoffs) or imperfect information (you don't see opponent's moves) require Bayesian analysis.
- **Mixed-strategy NE is the default, not the exception**: When no pure-strategy NE exists (e.g., matching pennies), agents often report "no equilibrium found" instead of computing the mixed strategy. Every finite game has at least one NE — if you can't find a pure one, solve for the mixing probabilities.

## References

- For repeated games and folk theorem, see `references/repeated-games.md`
- For mechanism design basics, see `references/mechanism-design.md`
