---
name: "grad-signaling"
description: "Apply signaling theory (Spence, 1973) to analyze how agents communicate private information through costly, credible signals under information asymmetry. Use this skill when the user needs to evaluate whether a corporate action serves as a credible signal, analyze dividend or IPO signaling, assess separating vs pooling equilibria, or when they ask 'why do firms pay dividends', 'is this signal credible', or 'how does underpricing signal quality'."
metadata:
  category: "WP-26 財務理論"
  tags: ["signaling", "Spence", "information-asymmetry", "separating-equilibrium", "dividends", "IPO-underpricing"]
---

# Signaling Theory

## Overview

Signaling theory (Spence, 1973) explains how informed parties credibly communicate private information to uninformed parties through costly actions. In finance, firms signal quality through dividends, capital structure, underpricing, and other mechanisms that are too costly for low-quality firms to mimic.

## When to Use

- Analyzing why firms pay dividends despite tax disadvantage
- Evaluating IPO underpricing as a quality signal
- Assessing whether a corporate action conveys credible private information
- Designing mechanisms to separate high-quality from low-quality issuers

## When NOT to Use

- When information asymmetry is minimal (both sides have equal information)
- For cheap-talk communication (costless signals are not credible)
- When the signaling cost exceeds the benefit to the signaler

## Assumptions

```
IRON LAW: A signal is credible ONLY if it is costly to fake — cheap
talk is not a signal. For a separating equilibrium, the signal must
be differentially costly: affordable for high-quality types but
prohibitively expensive for low-quality types.
```

Key assumptions:
1. Information asymmetry exists between sender and receiver
2. Signal cost is negatively correlated with quality (single-crossing property)
3. Receivers rationally update beliefs based on observed signals
4. Equilibrium can be separating (types distinguished) or pooling (types indistinguishable)

## Methodology

### Step 1 — Identify Asymmetry and Parties

- Who is the informed party (sender)? What private information do they hold?
- Who is the uninformed party (receiver)? What decision do they make?

### Step 2 — Identify the Signal and Its Cost Structure

| Financial Signal | Sender | Costly Because |
|-----------------|--------|----------------|
| Dividends | Firm managers | Commits cash flow, tax cost |
| IPO underpricing | Issuing firm | Leaves money on the table |
| Debt issuance | Firm managers | Fixed obligations, bankruptcy risk |
| Share buybacks | Firm managers | Depletes cash reserves |
| Education (Spence) | Job applicant | Time, money, effort |

### Step 3 — Assess Equilibrium Type

- **Separating:** High-quality types signal, low-quality types do not. Receiver can distinguish.
- **Pooling:** All types take the same action. Receiver cannot distinguish.
- Key test: Is the signal cost differential sufficient to sustain separation?

### Step 4 — Evaluate Signal Credibility

Checklist for credible signal:
- Is it costly to the sender?
- Is it more costly for low-quality senders?
- Can the receiver observe the signal?
- Is the signal difficult to fake or replicate cheaply?

## Output Format

```markdown
## Signaling Analysis: [Corporate Action / Context]

### Information Structure
- Sender: [who] with private info about [what]
- Receiver: [who] making decision about [what]

### Signal Assessment
| Criterion | Assessment |
|-----------|------------|
| Observable? | [Yes/No] |
| Costly? | [Yes/No — how] |
| Differentially costly? | [Yes/No — why] |
| Credible? | [Yes/No] |

### Equilibrium
- Type: [Separating / Pooling / Semi-separating]
- Stability: [Robust / Fragile — why]

### Implications
- [What rational receivers should infer]
- [Strategic recommendation for sender]
```

## Gotchas

- Not every costly action is a signal — it must be observed by the receiver and differentially costly
- Multiple equilibria often exist; which one obtains depends on off-equilibrium beliefs
- Signal costs represent deadweight loss to society, even if individually rational
- Over-signaling occurs when competition escalates signal costs beyond social optimum
- Empirical identification is hard — correlation between signals and quality does not prove signaling
- Institutional context matters: mandatory disclosure regulations can substitute for costly signaling

## References

- Spence, M. (1973). Job market signaling. *Quarterly Journal of Economics*, 87(3), 355-374.
- Ross, S. (1977). The determination of financial structure: the incentive-signalling approach. *Bell Journal of Economics*, 8(1), 23-40.
- Allen, F. & Faulhaber, G. (1989). Signalling by underpricing in the IPO market. *Journal of Financial Economics*, 23(2), 303-323.
