---
name: "grad-contract-theory"
description: "Apply contract theory to design incentive-compatible agreements under moral hazard and adverse selection. Use this skill when the user needs to structure principal-agent contracts, evaluate compensation schemes, or analyze incomplete contract problems where parties cannot specify all contingencies ex ante."
metadata:
  category: "WP-27 賽局與制度經濟"
  tags: ["contract-theory", "moral-hazard", "adverse-selection", "principal-agent", "incentive-design", "Hart", "Holmstrom", "incomplete-contracts"]
---

# Contract Theory: Moral Hazard, Adverse Selection, and Incentive Design

## Overview

Contract theory studies how economic actors construct contractual arrangements in the presence of asymmetric information. The two canonical problems are moral hazard (hidden action — the agent's effort is unobservable) and adverse selection (hidden type — the agent's characteristics are private). The optimal contract balances the principal's desire for risk-sharing against the need to incentivize effort or truthful revelation. Hart and Holmstrom's contributions on incomplete contracts and incentive design form the modern foundation.

## When to Use

- Designing compensation, bonus, or commission structures for employees or contractors
- Evaluating insurance contracts for moral hazard (deductibles, copays) or adverse selection (screening)
- Structuring partnerships, franchise agreements, or procurement contracts with unobservable quality
- Analyzing incomplete contracts where not all states of the world can be specified

## When NOT to Use

- Both parties have symmetric information and trust is established (no incentive problem)
- The relationship is a one-shot anonymous transaction with no contractual enforcement
- Behavioral factors (reciprocity, intrinsic motivation) dominate monetary incentives

## Assumptions

```
IRON LAW: The optimal contract balances risk-sharing against incentive
provision — full insurance destroys incentives, full incentives impose
unbearable risk. There is no contract that achieves first-best when
information is asymmetric.
```

- The principal is risk-neutral; the agent is risk-averse (standard setup)
- The agent's action (effort) or type is private information
- Output is a noisy signal of the agent's effort: x = f(e) + epsilon
- Both parties are rational and can commit to the contract terms
- Courts can verify output but not effort (contractibility constraint)

## Methodology

**Step 1 — Classify the Information Problem**
Determine whether the core issue is moral hazard (hidden action after contracting), adverse selection (hidden type before contracting), or both. Identify who is the principal and who is the agent.

**Step 2 — Specify Constraints**
Write down: (1) the Incentive Compatibility constraint (IC) — the agent prefers the intended action/type revelation; (2) the Participation Constraint (PC/IR) — the agent accepts the contract over the outside option; (3) Limited Liability (LL) if applicable — payments cannot go below zero.

**Step 3 — Solve the Optimal Contract**
For moral hazard: maximize principal's expected profit subject to IC and PC. The optimal wage schedule w(x) satisfies the Holmstrom informativeness principle — pay should depend on output only insofar as it is informative about effort. For adverse selection: design a menu of contracts that induces self-selection (screening). Expect distortion at the bottom (inefficient allocation for low types) and efficiency at the top.

**Step 4 — Assess Completeness and Renegotiation**
Check whether the contract is complete (covers all verifiable contingencies) or incomplete (residual rights matter). If incomplete, apply Hart's property rights approach: allocate residual control rights to the party whose investment is most important. Consider renegotiation-proofness.

## Output Format

```markdown
## Contract Design Analysis: [Context]

### Information Problem
- **Type**: Moral hazard / Adverse selection / Both
- **Principal**: [who]
- **Agent**: [who]
- **Hidden variable**: [effort level / agent type / quality]

### Constraints
| Constraint                  | Expression           | Binding? |
|----------------------------|----------------------|----------|
| Incentive Compatibility     |                      |          |
| Participation (IR)          |                      |          |
| Limited Liability           |                      |          |

### Optimal Contract Structure
- **Fixed component**: [base salary / premium]
- **Variable component**: [bonus / piece rate / deductible]
- **Informativeness**: [which signals are used and why]

### First-Best vs. Second-Best Gap
- **First-best outcome**: [what would happen with full information]
- **Second-best distortion**: [what is sacrificed]
- **Welfare loss**: [qualitative or quantitative]

### Recommendation
[Contract terms and implementation guidance]
```

## Gotchas

- Multi-tasking (Holmstrom-Milgrom): incentivizing one measurable task crowds out effort on unmeasurable tasks — strong incentives can be counterproductive
- Ratchet effect: if the principal updates expectations based on past performance, the agent strategically underperforms early
- Career concerns (Holmstrom 1999) can substitute for explicit incentives — young agents work hard to build reputation even without bonuses
- Limited liability constraints shift power to the agent and can require the principal to leave rents (efficiency wages)
- In repeated relationships, relational contracts (self-enforcing, not court-enforced) often dominate formal contracts
- Intrinsic motivation can be crowded out by extrinsic incentives (Benabou-Tirole) — paying volunteers may reduce their effort

## References

- Holmstrom, B. (1979). "Moral Hazard and Observability." *Bell Journal of Economics*.
- Hart, O. & Moore, J. (1990). "Property Rights and the Nature of the Firm." *Journal of Political Economy*.
- Laffont, J.-J. & Martimort, D. (2002). *The Theory of Incentives: The Principal-Agent Model*.
- Bolton, P. & Dewatripont, M. (2005). *Contract Theory*. MIT Press.
