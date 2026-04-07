---
name: "grad-info-economics"
description: "Apply information economics to diagnose and remedy market failures caused by asymmetric information. Use this skill when the user needs to analyze adverse selection, moral hazard, or signaling and screening mechanisms, especially in insurance, labor, credit, or product quality markets."
metadata:
  category: "WP-27 賽局與制度經濟"
  tags: ["information-economics", "adverse-selection", "moral-hazard", "signaling", "screening", "market-for-lemons", "Akerlof", "Spence", "Stiglitz"]
---

# Information Economics: Adverse Selection, Moral Hazard, and Signaling

## Overview

Information economics studies how asymmetric information between parties causes market failures and shapes institutional responses. Akerlof's "market for lemons" shows adverse selection can collapse entire markets; Spence's signaling model shows informed parties can credibly convey quality through costly actions; Rothschild-Stiglitz screening shows uninformed parties can design menus that induce self-selection. Together, these frameworks explain why markets for insurance, credit, labor, and used goods systematically deviate from the competitive ideal and why institutions like warranties, credentials, and regulation exist.

## When to Use

- Diagnosing why a market is failing or shrinking (quality collapse, credit rationing, insurance death spirals)
- Evaluating whether a signal (degree, certification, warranty) is credible and efficient
- Designing screening mechanisms (menus, deductibles, trial periods) to sort heterogeneous agents
- Assessing policy interventions (mandatory disclosure, minimum standards, subsidized insurance)

## When NOT to Use

- Information is symmetric or costlessly verifiable (no asymmetry problem)
- The product is a pure experience good where reputation and repeat purchase fully resolve quality uncertainty
- The analysis requires modeling strategic interaction beyond bilateral (use full game-theoretic models)

## Assumptions

```
IRON LAW: Information asymmetry causes market failure — without
corrective mechanisms (signals, screens, warranties), bad drives out
good. Markets with severe adverse selection can unravel completely
(Akerlof's lemons result).
```

- One party (informed) has private information about quality, risk, or effort
- The other party (uninformed) cannot directly observe the relevant characteristic
- Agents are rational and respond to the information structure strategically
- Signals are costly, and the cost differs by type (single-crossing / Spence-Mirrlees condition)
- In competitive markets, cross-subsidization between types is unsustainable

## Methodology

**Step 1 — Identify the Information Asymmetry**
Classify: (a) Adverse selection (hidden type, pre-contractual) — the informed party's type affects the uninformed party's payoff; (b) Moral hazard (hidden action, post-contractual) — the informed party's effort is unobservable; (c) Both present simultaneously. Identify who is informed and who is uninformed.

**Step 2 — Model the Market Failure**
For adverse selection: show how pooling (offering a single contract) attracts disproportionately bad types, driving up costs, raising prices, and causing good types to exit — the unraveling dynamic. For moral hazard: show how insurance or contracting reduces the agent's incentive to exert effort or take precautions, increasing expected costs.

**Step 3 — Evaluate Corrective Mechanisms**
Signaling (informed party acts): identify the signal, verify the single-crossing condition (high types find the signal less costly), and check whether a separating equilibrium exists. Screening (uninformed party designs menu): design contracts that induce self-selection — typically, high types get efficient contracts while low types face quantity distortion. Other mechanisms: warranties, reputation, certification, mandatory disclosure, regulation.

**Step 4 — Assess Efficiency and Policy**
Compare the outcome against the full-information benchmark. Calculate welfare loss from: (a) missing trades (good types priced out); (b) signaling waste (resources spent on credentials that produce no direct value); (c) screening distortions (inefficient contracts for low types). Recommend whether market mechanisms suffice or government intervention is needed.

## Output Format

```markdown
## Information Economics Analysis: [Market / Context]

### Information Structure
- **Asymmetry type**: Adverse selection / Moral hazard / Both
- **Informed party**: [who knows what]
- **Uninformed party**: [who lacks what information]
- **Hidden variable**: [quality / risk type / effort level]

### Market Failure Diagnosis
- **Unraveling risk**: [high / medium / low]
- **Pooling outcome**: [what happens if all types are treated identically]
- **Separating outcome**: [what happens if types are distinguished]

### Corrective Mechanisms
| Mechanism      | Who Initiates | How It Works            | Effective? |
|---------------|---------------|-------------------------|------------|
| Signaling      | Informed      | [e.g., education]       |            |
| Screening      | Uninformed    | [e.g., deductible menu] |            |
| Warranty       | Informed      | [e.g., money-back]      |            |
| Regulation     | Government    | [e.g., mandatory disclosure] |       |

### Efficiency Assessment
- **Full-information benchmark**: [first-best outcome]
- **Welfare loss sources**: [missing trades / signaling waste / screening distortion]
- **Net welfare**: [second-best outcome vs. unregulated market]

### Recommendation
[Which mechanisms to deploy; whether policy intervention is warranted]
```

## Gotchas

- Signaling can be socially wasteful — if education serves only as a signal (not human capital), the resources spent on it are pure deadweight loss
- The Rothschild-Stiglitz model may have no Nash equilibrium in pure strategies when the proportion of high types is large — the Wilson anticipatory equilibrium or Riley reactive equilibrium are alternatives
- Moral hazard and adverse selection interact: insurance with deductibles (screening for adverse selection) also mitigates moral hazard, but the two problems may require conflicting contract designs
- Mandatory disclosure can backfire if it causes unraveling of previously stable pooling equilibria
- In repeated interactions, reputation can substitute for formal signals — but reputation is fragile and subject to end-game effects
- Digital platforms and big data are reducing information asymmetry in some markets (credit scoring, reviews) but creating new asymmetries in others (algorithmic pricing, data privacy)

## References

- Akerlof, G. (1970). "The Market for Lemons: Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*.
- Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics*.
- Rothschild, M. & Stiglitz, J. (1976). "Equilibrium in Competitive Insurance Markets." *Quarterly Journal of Economics*.
- Riley, J. (2001). "Silver Signals: Twenty-Five Years of Screening and Signaling." *Journal of Economic Literature*.
