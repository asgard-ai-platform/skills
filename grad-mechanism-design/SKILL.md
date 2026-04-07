---
name: "grad-mechanism-design"
description: "Apply mechanism design (reverse game theory) to engineer incentive-compatible rules for allocation problems. Use this skill when the user needs to design auctions, voting systems, or matching markets, or when evaluating whether a proposed mechanism satisfies incentive compatibility and individual rationality constraints."
metadata:
  category: "WP-27 賽局與制度經濟"
  tags: ["mechanism-design", "incentive-compatibility", "revelation-principle", "Myerson-Satterthwaite", "auction-design", "matching-markets"]
---

# Mechanism Design: Reverse Game Theory and Incentive Compatibility

## Overview

Mechanism design is the engineering side of game theory: instead of analyzing given games, you design the rules so that self-interested agents produce a desired outcome. The central tool is the revelation principle, which shows that any implementable outcome can be achieved by a direct mechanism where truth-telling is optimal. The field underpins auction design, voting systems, matching markets, and regulatory frameworks.

## When to Use

- Designing allocation rules (auctions, matching, resource sharing) where participants have private information
- Evaluating whether a proposed institution or platform incentivizes truthful behavior
- Assessing trade-offs between efficiency, budget balance, and participation constraints

## When NOT to Use

- Agents are fully cooperative with no private information (no incentive problem exists)
- The environment is too complex to model agent types (use behavioral experiments instead)
- You need a quick heuristic rather than a formal guarantee

## Assumptions

```
IRON LAW: A mechanism is incentive-compatible ONLY if truth-telling is a
dominant strategy — no mechanism can simultaneously maximize efficiency,
budget balance, and individual rationality (Myerson-Satterthwaite theorem).
```

- Agents are rational and maximize expected utility
- Each agent has private information (type) drawn from a known prior distribution
- The designer commits to the mechanism rules before agents act
- Transfers (payments) are feasible and quasi-linear utility applies

## Methodology

**Step 1 — Define the Design Problem**
Specify the set of agents, their type spaces, the outcome space, and the social choice function you want to implement. Identify the objective: efficiency, revenue, fairness, or a weighted combination.

**Step 2 — Apply the Revelation Principle**
Restrict attention to direct revelation mechanisms. For each agent, the mechanism asks for a reported type and maps the profile of reports to an outcome and transfers. Check whether truthful reporting constitutes a Bayesian Nash equilibrium (BNE-IC) or dominant strategy equilibrium (DSIC).

**Step 3 — Verify Constraints**
Check three core constraints: (1) Incentive Compatibility — no agent gains by misreporting; (2) Individual Rationality — each agent is at least as well off participating as not; (3) Budget Balance — the designer does not run a deficit. Apply Myerson-Satterthwaite to determine which constraints can co-exist.

**Step 4 — Characterize and Optimize**
Use the envelope theorem to derive the payment rule from the allocation rule. Optimize the objective subject to binding constraints. Report which trade-offs are unavoidable.

## Output Format

```markdown
## Mechanism Design Analysis: [Context]

### Design Problem
- **Agents**: [who participates]
- **Type space**: [private information each agent holds]
- **Outcome space**: [possible allocations]
- **Objective**: [efficiency / revenue / fairness]

### Proposed Mechanism
- **Allocation rule**: [how outcomes map to reports]
- **Payment rule**: [transfers as function of reports]

### Constraint Verification
| Constraint                | Satisfied? | Notes |
|--------------------------|------------|-------|
| Incentive Compatibility  | Yes / No   |       |
| Individual Rationality   | Yes / No   |       |
| Budget Balance           | Yes / No   |       |

### Impossibility Trade-offs
[Which constraints conflict per Myerson-Satterthwaite; what the designer must sacrifice]

### Recommendation
[Chosen mechanism and rationale]
```

## Gotchas

- The revelation principle guarantees existence of a direct mechanism but says nothing about practical simplicity — real-world mechanisms often use indirect formats for behavioral reasons
- Myerson-Satterthwaite impossibility applies to bilateral trade with private values; multilateral settings may escape it
- DSIC is stronger than BNE-IC; many practical mechanisms (e.g., VCG) are DSIC but may violate budget balance
- Correlation among agent types can be exploited (Cremer-McLean) to extract full surplus, but requires strong distributional knowledge
- Implementation in undominated strategies vs. full implementation vs. partial implementation are distinct solution concepts — specify which you mean
- Behavioral agents (bounded rationality, spite, fairness concerns) can break mechanisms that are theoretically incentive-compatible

## References

- Myerson, R. (1981). "Optimal Auction Design." *Mathematics of Operations Research*.
- Myerson, R. & Satterthwaite, M. (1983). "Efficient Mechanisms for Bilateral Trading." *Journal of Economic Theory*.
- Mas-Colell, A., Whinston, M. & Green, J. (1995). *Microeconomic Theory*, Ch. 23.
- Borgers, T. (2015). *An Introduction to the Theory of Mechanism Design*.
