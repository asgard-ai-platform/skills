---
name: "grad-behavioral-finance"
description: "Apply behavioral finance theory to identify systematic investor biases and their impact on asset prices. Use this skill when the user needs to analyze irrational market behavior, explain pricing anomalies through cognitive biases, diagnose investor decision errors, or when they ask 'why do investors hold losers too long', 'how does loss aversion affect pricing', or 'what biases drive this market pattern'."
metadata:
  category: "WP-26 財務理論"
  tags: ["behavioral-finance", "prospect-theory", "loss-aversion", "disposition-effect", "overconfidence", "Kahneman"]
---

# Behavioral Finance

## Overview

Behavioral finance challenges the rational-agent assumption by documenting systematic cognitive biases that affect investor decisions and market prices. Anchored in Kahneman and Tversky's prospect theory (1979), the field explains persistent anomalies that traditional finance cannot.

## When to Use

- Explaining market anomalies (momentum, bubbles, crashes) through investor psychology
- Diagnosing decision biases in portfolio management
- Designing de-biasing strategies for investment processes
- Evaluating why "rational" strategies underperform expectations

## When NOT to Use

- As a catch-all explanation for any price movement — biases must be identified specifically
- When standard rational models already explain the phenomenon adequately
- For normative portfolio construction without considering limits to arbitrage

## Assumptions

```
IRON LAW: Investors are NOT rational — systematic biases create
predictable pricing errors. These errors persist because arbitrage
is limited (costs, risk, horizon constraints).
```

Key assumptions:
1. Cognitive biases are systematic, not random — they create directional price effects
2. Limits to arbitrage prevent rational traders from fully correcting mispricings
3. Reference points and framing significantly affect decisions

## Methodology

### Step 1 — Identify the Behavioral Anomaly

Observe the pricing pattern or decision that deviates from rational expectations.

### Step 2 — Map to Specific Biases

| Bias | Description | Market Effect |
|------|-------------|---------------|
| Loss aversion | Losses hurt ~2x more than equivalent gains | Disposition effect, equity premium puzzle |
| Overconfidence | Overestimate precision of private information | Excessive trading, under-diversification |
| Herding | Follow the crowd regardless of private signal | Bubbles, momentum, crashes |
| Anchoring | Over-rely on initial reference points | Under-reaction to earnings surprises |
| Mental accounting | Treat money differently based on source/label | Portfolio segregation, house-money effect |

### Step 3 — Assess Limits to Arbitrage

- Fundamental risk, noise trader risk, implementation costs
- Short-selling constraints, model risk, horizon mismatch

### Step 4 — Propose De-biasing or Exploitation Strategy

- De-bias: pre-commitment rules, systematic rebalancing, checklists
- Exploit: contrarian strategies, but only if limits to arbitrage are manageable

## Output Format

```markdown
## Behavioral Finance Analysis: [Context]

### Observed Anomaly
- [Description of pricing pattern or decision error]

### Bias Diagnosis
| Bias | Evidence | Severity |
|------|----------|----------|
| [bias name] | [specific observation] | [High/Medium/Low] |

### Limits to Arbitrage
- [Why rational traders cannot fully correct this]

### Recommendations
1. [De-biasing strategy or trading implication]
2. [Process improvement]
```

## Gotchas

- Behavioral biases explain patterns but rarely predict timing — "the market can stay irrational longer than you can stay solvent"
- Not all anomalies are behavioral; some reflect rational risk compensation
- Prospect theory is descriptive, not prescriptive — it explains behavior, not optimal decisions
- Biases interact; loss aversion plus overconfidence can produce contradictory predictions
- Publication bias may inflate the number of "real" behavioral anomalies
- Institutional investors exhibit different biases than retail investors

## References

- Kahneman, D. & Tversky, A. (1979). Prospect theory: an analysis of decision under risk. *Econometrica*, 47(2), 263-292.
- Shleifer, A. & Vishny, R. (1997). The limits of arbitrage. *Journal of Finance*, 52(1), 35-55.
- Barberis, N. & Thaler, R. (2003). A survey of behavioral finance. *Handbook of the Economics of Finance*, 1, 1053-1128.
