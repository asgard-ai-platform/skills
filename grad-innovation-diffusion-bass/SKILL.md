---
name: "grad-innovation-diffusion-bass"
description: "Apply the Bass Diffusion Model (1969) to forecast innovation adoption using innovation and imitation coefficients. Use this skill when the user needs to forecast new product adoption curves, estimate market penetration timing, calibrate launch strategy based on diffusion dynamics, or when they ask 'how fast will this spread', 'when does adoption take off', or 'what is the expected S-curve'."
metadata:
  category: "WP-25 行銷理論"
  tags: ["Bass-model", "diffusion", "innovation", "adoption", "S-curve", "forecasting", "new-product"]
---

# Bass Diffusion Model

## Overview

The Bass model (1969) describes how new products are adopted through two forces: innovation (external influence, coefficient p) and imitation (internal/word-of-mouth influence, coefficient q). The resulting adoption follows an S-curve whose shape is entirely determined by p, q, and market potential m.

## When to Use

- Forecasting adoption trajectory for a new product or technology
- Estimating time-to-peak-sales and total market penetration
- Calibrating marketing spend between advertising (p) and word-of-mouth (q)
- Comparing diffusion patterns across product categories or markets

## When NOT to Use

- Repeat-purchase or consumable products (Bass models first adoption only)
- Markets with strong network effects requiring explicit network models
- When no analogous product data exists and p/q cannot be estimated

## Assumptions

```
IRON LAW: The ratio q/p determines adoption shape. High q/p means
word-of-mouth dominates and adoption exhibits a sharp peak; low q/p
means advertising-driven gradual uptake. This ratio is the single
most diagnostic parameter.
```

Key assumptions:
1. Market potential (m) is fixed and known
2. Adopters do not dis-adopt (no churn in the basic model)
3. The product does not change over the diffusion period
4. Innovation and imitation effects are independent and additive

## Methodology

### Step 1 — Define market potential (m)

Estimate the total addressable market. Use analogous products, surveys, or top-down market sizing. This is the ceiling of cumulative adoption.

### Step 2 — Estimate p and q coefficients

Sources for estimation:
- **Analogy**: Use p and q from similar products (Sultan, Farley, & Lehmann 1990 meta-analysis: average p = 0.03, q = 0.38)
- **Historical data**: Fit the Bass model to early adoption data via nonlinear least squares
- **Expert judgment**: Calibrate based on marketing plan intensity

### Step 3 — Generate the adoption curve

The Bass model hazard rate:

f(t) / [1 - F(t)] = p + q * F(t)

Where F(t) = cumulative adoption fraction at time t.

Key derived metrics:
- **Time to peak**: t* = [ln(q) - ln(p)] / (p + q)
- **Peak adoption rate**: f(t*) = m(p + q)^2 / (4q)
- **Inflection point**: When F(t) = (q - p) / (2q)

### Step 4 — Interpret and strategize

| q/p Ratio | Pattern | Strategy Implication |
|-----------|---------|---------------------|
| q/p > 20 | Sharp peak, WOM-driven | Seed early adopters aggressively |
| q/p = 5-20 | Moderate peak | Balance advertising and WOM |
| q/p < 5 | Gradual, advertising-driven | Sustain mass-media campaigns |

## Output Format

```markdown
## Bass Diffusion Forecast: [Product/Innovation]

### Parameters
- Market potential (m): [value]
- Innovation coefficient (p): [value] (source: [analogy/data/expert])
- Imitation coefficient (q): [value] (source: [analogy/data/expert])
- q/p ratio: [value] — [interpretation]

### Forecast
- Time to peak sales: t* = [value]
- Peak adoption rate: [value] units/period
- Time to 50% penetration: [value]
- Time to 90% penetration: [value]

### Strategic Implications
1. [Launch strategy based on q/p ratio]
2. [Marketing mix recommendation]
3. [Timing considerations]
```

## Gotchas

- Market potential (m) is the most sensitive parameter yet hardest to estimate — sensitivity-test it
- The basic Bass model assumes no price changes, competition entry, or product updates over time
- Generalized Bass Model (Bass et al., 1994) incorporates marketing mix variables — use it when price/advertising data exists
- Digital products often show higher q values due to social media amplification
- Do not extrapolate p and q from one geography to another without cultural adjustment
- Early data (pre-inflection) yields unstable parameter estimates; wait for at least 3-4 periods of sales data

## References

- Bass, F. M. (1969). A new product growth for model consumer durables. *Management Science*, 15(5), 215-227.
- Bass, F. M., Krishnan, T. V., & Jain, D. C. (1994). Why the Bass model fits without decision variables. *Marketing Science*, 13(3), 203-223.
- Sultan, F., Farley, J. U., & Lehmann, D. R. (1990). A meta-analysis of applications of diffusion models. *Journal of Marketing Research*, 27(1), 70-77.
