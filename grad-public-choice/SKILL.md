---
name: "grad-public-choice"
description: "Apply public choice theory to analyze political decision-making as rational self-interested behavior. Use this skill when the user needs to evaluate government policy failures, rent-seeking costs, voting outcomes, or bureaucratic incentives, especially when the assumption of benevolent government is questionable."
metadata:
  category: "WP-27 賽局與制度經濟"
  tags: ["public-choice", "Buchanan", "Tullock", "rent-seeking", "median-voter", "logrolling", "government-failure", "constitutional-economics"]
---

# Public Choice Theory: Rational Politics, Rent-Seeking, and Government Failure

## Overview

Public choice applies economic reasoning — rational self-interest, strategic behavior, and equilibrium analysis — to political decision-making. Politicians, bureaucrats, voters, and lobbyists are modeled as utility maximizers, not benevolent social planners. The theory explains phenomena such as rent-seeking, logrolling, pork-barrel spending, regulatory capture, and the systematic divergence between public interest and political outcomes. Buchanan and Tullock's foundational work treats constitutional rules as the ultimate mechanism design problem.

## When to Use

- Analyzing why a government policy produces outcomes that diverge from stated objectives
- Estimating the deadweight loss from rent-seeking and lobbying activities
- Predicting election outcomes or legislative bargaining using median voter or spatial models
- Designing constitutional rules or institutional reforms to constrain political opportunism

## When NOT to Use

- The analysis assumes a benevolent social planner by design (normative welfare economics)
- Political actors are genuinely constrained by strong norms, courts, or transparency (minimal agency problem)
- The question is about market failure, not government failure

## Assumptions

```
IRON LAW: Public officials are NOT benevolent social planners — they
respond to incentives just like market participants. Policy outcomes
reflect the preferences of those with political power, not the
preferences of society at large.
```

- Politicians maximize votes (or probability of re-election)
- Bureaucrats maximize budget size or discretionary authority (Niskanen model)
- Voters are rationally ignorant — the cost of becoming informed exceeds the expected benefit of a single vote
- Interest groups form when concentrated benefits exceed organization costs (Olson's logic of collective action)
- Constitutional rules are the meta-game that shapes all subsequent political games

## Methodology

**Step 1 — Identify the Political Market**
Map the actors: voters, politicians, bureaucrats, interest groups. Specify what each actor maximizes and the constraints they face (electoral cycles, budget rules, information costs).

**Step 2 — Apply the Relevant Model**
Choose from: (a) Median Voter Theorem — in single-dimensional, single-peaked preference space, the median voter's preferred policy wins under majority rule; (b) Rent-seeking model — agents spend real resources to capture a transfer, dissipating up to the full value of the rent; (c) Logrolling / vote trading — minorities trade votes across issues to pass legislation that fails majority support on each issue individually; (d) Bureaucracy model — budget-maximizing bureaus produce beyond efficient output.

**Step 3 — Estimate Government Failure Costs**
Quantify: (a) Tullock rectangle — resources spent on rent-seeking; (b) Allocative distortion from policies that reflect political rather than economic efficiency; (c) X-inefficiency within government agencies lacking competitive pressure. Compare against the market failure the policy aims to correct.

**Step 4 — Propose Institutional Remedies**
Recommend constitutional or institutional design changes: supermajority requirements, sunset clauses, independent agencies, fiscal rules, transparency mandates, or decentralization (Tiebout competition). Evaluate trade-offs between flexibility and constraint.

## Output Format

```markdown
## Public Choice Analysis: [Policy / Institution]

### Political Actors
| Actor           | Objective             | Key Constraint         |
|----------------|-----------------------|------------------------|
| Voters          |                       |                        |
| Politicians     |                       |                        |
| Bureaucrats     |                       |                        |
| Interest groups |                       |                        |

### Model Applied
- **Framework**: Median voter / Rent-seeking / Logrolling / Bureaucracy
- **Prediction**: [what the model predicts will happen]
- **Observed outcome**: [what actually happens — consistent?]

### Government Failure Costs
| Cost Category          | Estimate / Description |
|-----------------------|----------------------|
| Rent-seeking expenditure |                    |
| Allocative distortion    |                    |
| X-inefficiency           |                    |

### Market Failure vs. Government Failure
- **Market failure being addressed**: [externality / public good / monopoly]
- **Government failure introduced**: [rent-seeking / capture / inefficiency]
- **Net assessment**: [intervention improves welfare? or worsens it?]

### Institutional Recommendations
[Specific reforms with rationale]
```

## Gotchas

- Rational ignorance does not mean voters are stupid — it means the marginal cost of information exceeds the marginal benefit given one vote's influence
- The median voter theorem requires single-peaked preferences and a single policy dimension — with multiple dimensions, cycling (Arrow's impossibility) can occur
- Rent-seeking dissipation can exceed 100% of the rent when contestants are risk-loving or misinformed about competition
- Public choice does not claim all government action is bad — it claims the incentive structure must be analyzed, not assumed benevolent
- Buchanan distinguished between "politics without romance" (positive analysis) and constitutional political economy (normative design of rules)
- Regulatory capture (Stigler) is a specific form of rent-seeking where the regulated industry controls the regulator — independence alone is insufficient

## References

- Buchanan, J. & Tullock, G. (1962). *The Calculus of Consent*. University of Michigan Press.
- Tullock, G. (1967). "The Welfare Costs of Tariffs, Monopolies, and Theft." *Western Economic Journal*.
- Olson, M. (1965). *The Logic of Collective Action*. Harvard University Press.
- Mueller, D. (2003). *Public Choice III*. Cambridge University Press.
