---
name: "grad-strat-agency"
description: "Apply Agency Theory (Jensen and Meckling, 1976) to diagnose principal-agent problems — moral hazard, adverse selection — and design governance mechanisms to align interests. Use this skill when the user needs to analyze conflicts of interest between owners and managers, design incentive or monitoring structures, evaluate corporate governance effectiveness, or when they ask 'how do we ensure managers act in shareholders interest', 'why is this incentive plan failing', or 'what governance mechanisms reduce agency costs'."
metadata:
  category: "WP-23 策略管理理論"
  tags: ["strategy", "agency-theory", "Jensen-Meckling", "principal-agent", "corporate-governance", "moral-hazard"]
---

# Agency Theory

## Overview

Agency theory addresses the relationship where one party (principal) delegates work to another (agent) whose interests may diverge. Jensen and Meckling (1976) formalized how the separation of ownership and control creates agency costs: monitoring costs, bonding costs, and residual loss.

## When to Use

- Analyzing owner-manager conflicts in corporate governance
- Designing executive compensation and incentive plans
- Evaluating board effectiveness and monitoring structures
- Assessing governance in franchising, partnerships, or supply chains

## Assumptions

```
IRON LAW: Agency costs are unavoidable — the goal is to minimize
TOTAL agency costs (monitoring + bonding + residual loss).
Eliminating one cost type often increases another. Optimal
governance minimizes the sum, not any single component.
```

Key assumptions:
1. **Goal divergence** — Agents have self-interest that may conflict with principals
2. **Information asymmetry** — Agents possess private information
3. **Risk preferences differ** — Agents are typically more risk-averse than diversified principals

## Methodology

### Agency Problem Types

| Problem | When | Mechanism |
|---------|------|-----------|
| **Moral hazard** | Post-contract; agent effort is unobservable | Hidden action |
| **Adverse selection** | Pre-contract; agent type is unobservable | Hidden information |
| **Hold-up** | Post-investment; agent exploits lock-in | Relationship-specific investment |

### Agency Cost Components

1. **Monitoring costs** — Expenses by principal to observe agent behavior (audits, boards, reporting)
2. **Bonding costs** — Expenses by agent to signal alignment (certifications, guarantees)
3. **Residual loss** — Remaining welfare loss despite monitoring and bonding

### Governance Design Steps

1. **Identify the principal-agent relationship** — Who delegates? Who acts?
2. **Diagnose the agency problem** — Moral hazard, adverse selection, or both?
3. **Assess information asymmetry** — What can the principal observe?
4. **Design mechanisms:**
   - **Outcome-based contracts** — Align incentives (bonuses, stock options, profit sharing)
   - **Behavior-based monitoring** — Observe and constrain (board oversight, audits, reporting)
   - **Bonding mechanisms** — Agent credible commitments (warranties, certifications)
5. **Evaluate total cost** — Ensure mechanism cost does not exceed agency cost saved

## Output Format

```markdown
## Agency Analysis: [Context]

### Principal-Agent Map
| Principal | Agent | Delegation | Key Conflict |
|-----------|-------|-----------|--------------|
| [who]     | [who] | [what]    | [goal divergence] |

### Agency Problem Diagnosis
- Type: [moral hazard / adverse selection / both]
- Information asymmetry: ...
- Observable vs unobservable: ...

### Governance Mechanisms
| Mechanism | Type | Cost | Expected Effect |
|-----------|------|------|-----------------|
| [name]    | [monitoring/bonding/incentive] | [est.] | [reduction in...] |

### Total Agency Cost Assessment
- Monitoring costs: ...
- Bonding costs: ...
- Estimated residual loss: ...
```

## Examples

### Good Example
Analyzing CEO compensation: principal (shareholders) faces moral hazard (CEO effort unobservable). Design combines outcome-based incentives (stock options aligned with long-term value) with behavior-based monitoring (independent board, audit committee). Evaluates trade-off between monitoring intensity and incentive pay.

### Bad Example
Proposing "more monitoring" without considering that excessive monitoring increases costs and may crowd out intrinsic motivation. Agency theory requires minimizing total agency costs, not maximizing control.

## Gotchas

- Multiple principals with conflicting goals (shareholders vs debtholders vs employees) complicate analysis
- Stock options can create perverse incentives (short-term manipulation, excessive risk-taking)
- Agency theory assumes self-interest; it may underweight stewardship motivations
- Board independence does not automatically equal effective monitoring
- In non-corporate contexts (franchises, alliances), identify who is principal and who is agent carefully

## References

- Jensen, M. & Meckling, W. (1976). Theory of the firm: Managerial behavior, agency costs and ownership structure. *Journal of Financial Economics*, 3(4), 305-360.
- Eisenhardt, K. (1989). Agency theory: An assessment and review. *Academy of Management Review*, 14(1), 57-74.
- Fama, E. & Jensen, M. (1983). Separation of ownership and control. *Journal of Law and Economics*, 26(2), 301-325.
