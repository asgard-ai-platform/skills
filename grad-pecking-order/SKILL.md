---
name: "grad-pecking-order"
description: "Apply pecking order theory (Myers and Majluf, 1984) to analyze how information asymmetry drives financing hierarchy decisions. Use this skill when the user needs to explain why firms prefer internal over external financing, interpret equity issuance as a negative signal, evaluate capital raising decisions, or when they ask 'why did the stock drop on the equity offering', 'should we use debt or equity', or 'why do firms hoard cash'."
metadata:
  category: "WP-26 財務理論"
  tags: ["pecking-order", "information-asymmetry", "Myers-Majluf", "financing-hierarchy", "adverse-selection"]
---

# Pecking Order Theory

## Overview

Pecking order theory (Myers & Majluf, 1984) argues that firms follow a strict financing hierarchy — internal funds first, then debt, then equity — driven by information asymmetry between managers and outside investors. Unlike tradeoff theory, there is no target leverage ratio.

## When to Use

- Explaining why firms accumulate cash rather than return it
- Interpreting market reactions to financing announcements
- Predicting financing choices based on information environment
- Analyzing why high-profit firms often have low leverage

## When NOT to Use

- When the firm has minimal information asymmetry (e.g., transparent regulated utilities)
- For firms that actively target a leverage ratio (tradeoff theory better fits)
- When tax considerations clearly dominate financing choices

## Assumptions

```
IRON LAW: Firms prefer internal financing first because external
financing signals negative private information. Equity issuance is
the most informationally sensitive — and therefore most costly — source.
```

Key assumptions:
1. Managers know more about firm value than outside investors
2. Managers act in the interest of existing shareholders
3. Investors rationally discount securities issued by better-informed insiders
4. Transaction costs increase from internal funds to debt to equity

## Methodology

### Step 1 — Assess Information Asymmetry

- How transparent is the firm's business? (R&D-intensive = high asymmetry)
- What is the track record of management communication?
- How complex are the firm's assets to value externally?

### Step 2 — Identify Available Financing Sources

| Source | Adverse Selection Cost | Pecking Order Rank |
|--------|----------------------|-------------------|
| Retained earnings | None | 1st (preferred) |
| Bank debt (secured) | Low | 2nd |
| Public debt (bonds) | Medium | 3rd |
| Convertible debt | Medium-High | 4th |
| Equity issuance | Highest | Last resort |

### Step 3 — Predict or Explain Financing Choice

- Sufficient internal funds: no external financing needed
- Internal funds insufficient: issue safest security first (debt before equity)
- Equity issuance: signals management believes shares are overvalued

### Step 4 — Evaluate Market Reaction

- Equity issuance announcement: expect negative stock price reaction (-2% to -3% typical)
- Debt issuance: modest or neutral reaction
- Internal financing: no signaling effect

## Output Format

```markdown
## Pecking Order Analysis: [Firm / Decision]

### Information Environment
- Asymmetry level: [High / Medium / Low]
- Key drivers: [R&D intensity, asset complexity, etc.]

### Financing Decision
| Option | Available | Adverse Selection Cost | Chosen? |
|--------|-----------|----------------------|---------|
| Internal funds | [Y/N] | None | [Y/N] |
| Debt | [Y/N] | [Low/Medium] | [Y/N] |
| Equity | [Y/N] | [High] | [Y/N] |

### Signaling Implications
- [Expected market reaction and rationale]

### Assessment
- [Consistent with pecking order? If not, why?]
```

## Gotchas

- Pecking order predicts no target leverage — leverage is the cumulative result of past financing needs
- The theory better explains large, mature firms; startups often must issue equity
- Empirical evidence is mixed — some firms clearly target leverage ratios
- Information asymmetry varies over time; post-earnings or post-audit windows reduce it
- Does not explain why some firms issue equity when they have cash (empire building, market timing)
- Hybrid securities (convertibles, preferred) blur the hierarchy boundaries

## References

- Myers, S. & Majluf, N. (1984). Corporate financing and investment decisions when firms have information that investors do not have. *Journal of Financial Economics*, 13(2), 187-221.
- Myers, S. (1984). The capital structure puzzle. *Journal of Finance*, 39(3), 575-592.
- Frank, M. & Goyal, V. (2003). Testing the pecking order theory of capital structure. *Journal of Financial Economics*, 67(2), 217-248.
