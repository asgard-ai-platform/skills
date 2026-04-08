---
name: "biz-financial-ratios"
description: "Analyze financial health using ratio categories: profitability, liquidity, leverage, efficiency, and valuation. Use this skill when the user needs to assess a company's financial performance, compare companies, evaluate creditworthiness, or prepare financial due diligence — even if they say 'is this company financially healthy', 'analyze these financial statements', or 'compare these two companies'."
metadata:
  category: "WP-15 商學院—財務"
  tags: ["finance", "financial-ratios", "financial-analysis"]
---

# Financial Ratio Analysis

## Overview

Financial ratio analysis transforms raw financial statements into comparable metrics across five categories. Ratios are meaningful only in context — compare against industry benchmarks, historical trends, and peer companies.

## When to Use

**Trigger conditions:**
- User has financial statements and needs to assess company health
- User comparing financial performance across companies
- User performing due diligence or credit analysis
- User asks "is this company financially healthy?" or "analyze these numbers"

**When NOT to use:**
- For valuation → use DCF or comparables
- For ROE deep-dive → use DuPont Analysis
- For strategic assessment → use SWOT

## Framework

```
IRON LAW: Ratios Without Context Are Meaningless

A current ratio of 1.5 means nothing alone. Is 1.5 good? Compare to:
1. Industry average (retail ~1.2, manufacturing ~1.8)
2. Company's own trend (was it 2.0 last year? → declining liquidity)
3. Peers (competitor has 2.5? → relatively weak)

NEVER report a ratio without at least one comparison point.
```

```
IRON LAW: All Five Categories, Every Time

Analyzing only profitability misses a leveraged company about to default.
Analyzing only liquidity misses a profitable company's growth potential.
Cover all five categories for a complete picture.
```

### The Five Categories

**1. Profitability** — Is the company making money?
| Ratio | Formula | Measures |
|-------|---------|----------|
| Gross Margin | (Revenue - COGS) / Revenue | Production efficiency |
| Operating Margin | EBIT / Revenue | Core business profitability |
| Net Margin | Net Income / Revenue | Bottom-line profitability |
| ROE | Net Income / Equity | Return to shareholders |
| ROA | Net Income / Total Assets | Asset productivity |

**2. Liquidity** — Can it pay short-term obligations?
| Ratio | Formula | Healthy |
|-------|---------|---------|
| Current Ratio | Current Assets / Current Liabilities | > 1.5 |
| Quick Ratio | (Current Assets - Inventory) / Current Liabilities | > 1.0 |
| Cash Ratio | Cash / Current Liabilities | Context-dependent |

**3. Leverage** — How much debt is used?
| Ratio | Formula | Measures |
|-------|---------|----------|
| Debt-to-Equity | Total Liabilities / Equity | Capital structure |
| Interest Coverage | EBIT / Interest Expense | Ability to service debt |
| Debt-to-Assets | Total Liabilities / Total Assets | Asset financing |

> ⚠️ **"Debt" definition**: This skill (and the bundled script) defines "Debt" in the
> leverage ratios as **Total Liabilities** — not "long-term debt only" or "interest-bearing
> debt only". Both alternative definitions exist in textbooks and produce materially
> different ratios. If you need a different definition, document the choice explicitly
> and compute it manually; do not silently substitute.

**4. Efficiency** — How well are assets used?
| Ratio | Formula | Measures |
|-------|---------|----------|
| Inventory Turnover | COGS / Avg Inventory | Inventory management |
| Receivables Turnover | Revenue / Avg Receivables | Collection speed |
| Asset Turnover | Revenue / Total Assets | Asset productivity |
| Cash Conversion Cycle | DIO + DSO - DPO | Cash cycle speed |

**5. Valuation** — Is the stock fairly priced?
| Ratio | Formula | Measures |
|-------|---------|----------|
| P/E | Price / EPS | Price vs earnings |
| EV/EBITDA | Enterprise Value / EBITDA | Price vs cash generation |
| P/B | Price / Book Value per Share | Price vs net assets |
| Dividend Yield | Dividend per Share / Price | Income return |

### Analysis Process

1. **Calculate** all relevant ratios from financial statements
2. **Compare** against industry benchmarks and 3-year trend
3. **Identify** red flags (declining trends, outliers vs peers)
4. **Synthesize** a financial health verdict across all five categories
5. **Recommend** actions based on weak areas

## Output Format

> ⚠️ **Decimal vs percent**: The bundled script returns all profitability ratios
> (`gross_margin`, `operating_margin`, `net_margin`, `roa`, `roe`) as **decimals** —
> `0.35` means 35%, NOT `35.0`. Liquidity and leverage ratios are already unitless
> multiples (e.g. `current_ratio: 2.125`). Render percentages only in the human-facing
> markdown report, never in JSON outputs.

```markdown
# Financial Ratio Analysis: {Company}

## Summary Dashboard
| Category | Status | Key Metric |
|----------|--------|-----------|
| Profitability | 🟢/🟡/🔴 | {headline ratio} |
| Liquidity | 🟢/🟡/🔴 | {headline ratio} |
| Leverage | 🟢/🟡/🔴 | {headline ratio} |
| Efficiency | 🟢/🟡/🔴 | {headline ratio} |
| Valuation | 🟢/🟡/🔴 | {headline ratio} |

## Detailed Ratios
{Tables per category with ratio, value, industry avg, trend}

## Red Flags
- {specific concern with data}

## Overall Assessment
{Synthesized financial health verdict}
```

## Examples

### Correct Application
**Scenario:** Ratio analysis for a Taiwanese electronics manufacturer

| Ratio | Company | Industry | Trend | Flag |
|-------|---------|----------|-------|------|
| Gross Margin | 18% | 22% | ↓ from 21% | 🔴 Below peers, declining |
| Current Ratio | 1.8 | 1.5 | → stable | 🟢 Adequate |
| D/E | 1.2 | 0.8 | ↑ from 0.9 | 🟡 Rising leverage |
| Inventory Turnover | 4.2x | 6.0x | ↓ from 5.1x | 🔴 Slow inventory |

Synthesis: Profitability weakening + inventory building up + leverage rising = potential working capital crisis ahead ✓

### Incorrect Application
- Reported "Gross Margin 18%" as standalone fact → No comparison. Is 18% good or bad? Violates Iron Law: ratios without context.
- Only analyzed profitability ratios, missed D/E of 4.5x → Company appeared healthy by margins but was dangerously overleveraged. Violates Iron Law: all five categories.

## Gotchas

- **Industry matters enormously**: A 5% net margin is terrible for software (expect 20-30%) but excellent for grocery retail (expect 2-3%). Always benchmark within industry.
- **One-time items**: Restructuring charges, asset sales, or legal settlements distort ratios for that period. Use adjusted figures or note the distortion.
- **Seasonal businesses**: Ratios at different quarter-ends tell different stories. Use trailing 12-month or compare same quarter YoY.
- **Off-balance-sheet items**: Operating leases (pre-IFRS 16), special purpose vehicles, and contingent liabilities may not appear in standard ratios. Check footnotes.
- **Growth companies look "unhealthy"**: High-growth companies often have low profitability, high leverage, and negative cash flow by design. Context matters.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/financial_ratios.py` | Compute standard liquidity, leverage, profitability, and efficiency ratios | `python scripts/financial_ratios.py --help` |

Run `python scripts/financial_ratios.py --verify` to execute built-in sanity tests.

## References

- For industry-specific benchmark ranges, see `references/industry-benchmarks.md`
- For DuPont deep-dive on ROE, see the biz-dupont skill
