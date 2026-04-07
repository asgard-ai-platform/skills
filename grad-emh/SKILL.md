---
name: "grad-emh"
description: "Apply the Efficient Market Hypothesis (Fama, 1970) to evaluate information incorporation in asset prices across weak, semi-strong, and strong forms. Use this skill when the user needs to assess market efficiency, determine if a trading strategy can generate abnormal returns, evaluate event studies, or when they ask 'can technical analysis work', 'does the market already know this', or 'is this anomaly exploitable'."
metadata:
  category: "WP-26 財務理論"
  tags: ["EMH", "efficient-market", "Fama", "market-efficiency", "information", "anomalies"]
---

# Efficient Market Hypothesis (EMH)

## Overview

The Efficient Market Hypothesis (Fama, 1970) posits that asset prices fully reflect available information, making it impossible to consistently earn abnormal returns. EMH is organized into three forms — weak, semi-strong, and strong — each defined by the information set reflected in prices.

## When to Use

- Evaluating whether a trading strategy exploits genuine inefficiency
- Designing event studies (semi-strong form test)
- Assessing if active management adds value over passive indexing
- Debating the validity of technical or fundamental analysis

## When NOT to Use

- As justification to ignore all market anomalies without investigation
- When markets are clearly illiquid or informationally segmented
- For normative claims — EMH describes price behavior, not what prices "should" be

## Assumptions

```
IRON LAW: In an efficient market, prices reflect available information —
beating the market consistently requires either superior information
or accepting more risk. No free lunch.
```

Key assumptions:
1. Large number of rational, profit-maximizing participants
2. Information is costless and available simultaneously to all participants
3. Transaction costs do not prevent trading on information
4. Investors react quickly and unbiasedly to new information

## Methodology

### Step 1 — Identify the Information Set

- Weak form: past prices and trading volume only
- Semi-strong form: all publicly available information
- Strong form: all information including private/insider information

### Step 2 — Determine the Testable Implication

| Form | Information Reflected | Implication |
|------|----------------------|-------------|
| Weak | Historical prices | Technical analysis cannot earn excess returns |
| Semi-strong | All public info | Fundamental analysis cannot earn excess returns |
| Strong | All info (public + private) | Even insiders cannot earn excess returns |

### Step 3 — Select Appropriate Test

- Weak: autocorrelation tests, runs tests, filter rules
- Semi-strong: event studies (abnormal returns around announcements)
- Strong: insider trading profitability studies

### Step 4 — Interpret Results with Joint-Hypothesis Awareness

Any test of efficiency is simultaneously a test of the asset pricing model used to define "abnormal" return.

## Output Format

```markdown
## EMH Assessment: [Market / Strategy]

### Efficiency Form Tested
- Form: [weak / semi-strong / strong]
- Information set: [description]

### Evidence
| Test | Result | Supports Efficiency? |
|------|--------|---------------------|
| [test name] | [finding] | [Yes/No/Ambiguous] |

### Known Anomalies in This Context
- [List relevant anomalies and their current status]

### Conclusion
- [Efficiency assessment with caveats]
- [Joint-hypothesis caveat]
```

## Gotchas

- Joint-hypothesis problem: you cannot test efficiency without assuming an equilibrium model
- Grossman-Stiglitz paradox (1980): if markets are perfectly efficient, no one has incentive to gather information
- Anomalies (momentum, value, size) persist but may reflect risk or data mining
- EMH does not claim prices are always "correct" — only that mispricings are not systematically exploitable
- Market efficiency varies by market segment; large-cap equities are more efficient than micro-caps
- Behavioral finance provides systematic counterexamples but does not necessarily invalidate EMH

## References

- Fama, E. (1970). Efficient capital markets: a review of theory and empirical work. *Journal of Finance*, 25(2), 383-417.
- Grossman, S. & Stiglitz, J. (1980). On the impossibility of informationally efficient markets. *American Economic Review*, 70(3), 393-408.
- Malkiel, B. (2003). The efficient market hypothesis and its critics. *Journal of Economic Perspectives*, 17(1), 59-82.
