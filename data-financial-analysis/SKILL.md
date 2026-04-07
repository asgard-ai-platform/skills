---
name: "data-financial-analysis"
description: "Interpret the three core financial statements (income statement, balance sheet, cash flow statement) to assess business health and performance. Use this skill when the user needs to read financial statements, understand profitability vs cash flow, evaluate a company's financial position, or prepare for investor/board meetings — even if they say 'explain these financials', 'are we making money', 'read this annual report', or 'what do these numbers mean'."
metadata:
  category: "WP-04 數據分析"
  tags: ["data-analysis", "financial-statements", "accounting"]
---

# Financial Statement Analysis

## Framework

```
IRON LAW: Read All Three Statements Together

A company can be profitable (Income Statement) but cash-poor (Cash Flow Statement).
A company can have high assets (Balance Sheet) funded entirely by debt.
Reading one statement alone gives an incomplete — and potentially misleading — picture.
ALWAYS read all three and check for consistency.
```

### The Three Statements

**Income Statement (損益表)** — Did we make money THIS PERIOD?
- Revenue → Gross Profit → Operating Income → Net Income
- Key: Revenue recognition ≠ cash received. Accrual accounting records revenue when earned, not when paid.

**Balance Sheet (資產負債表)** — What do we own and owe RIGHT NOW?
- Assets = Liabilities + Shareholders' Equity
- Key: This is a SNAPSHOT at one point in time, not a period.

**Cash Flow Statement (現金流量表)** — Where did cash come from and go?
- Operating activities (core business cash generation)
- Investing activities (capex, acquisitions, asset sales)
- Financing activities (debt, equity, dividends)
- Key: Operating cash flow is the most important — it shows if the core business generates cash.

### Red Flags Across Statements

| Red Flag | What It Means |
|----------|-------------|
| Revenue growing but operating cash flow declining | Possible revenue recognition issues, rising receivables |
| Net income positive but free cash flow negative | Earnings driven by accruals, not cash; heavy capex |
| Assets growing faster than revenue | Inefficient asset utilization |
| Debt growing faster than equity | Increasing leverage risk |
| Inventory growing faster than revenue | Possible obsolescence, demand slowdown |

### Analysis Steps

1. **Read Income Statement**: Is the company profitable? At which level (gross, operating, net)?
2. **Read Balance Sheet**: What's the capital structure? How liquid is it?
3. **Read Cash Flow**: Is operating cash flow positive? Where is cash going?
4. **Cross-check**: Revenue growth vs cash flow growth, net income vs operating cash flow
5. **Trend**: 3-5 year trend for key metrics
6. **Benchmark**: Compare to industry peers

## Output Format

```markdown
# Financial Statement Analysis: {Company} — {Period}

## Income Statement Highlights
| Metric | Current | Prior Year | Change |
|--------|---------|-----------|--------|
| Revenue | ${X} | ${X} | {%} |
| Gross Margin | {%} | {%} | {±pp} |
| Operating Margin | {%} | {%} | {±pp} |
| Net Income | ${X} | ${X} | {%} |

## Balance Sheet Highlights
| Metric | Current | Prior Year |
|--------|---------|-----------|
| Total Assets | ${X} | ${X} |
| Total Debt | ${X} | ${X} |
| D/E Ratio | {X} | {X} |
| Current Ratio | {X} | {X} |

## Cash Flow Highlights
| Category | Amount |
|----------|--------|
| Operating CF | ${X} |
| Investing CF | ${X} |
| Financing CF | ${X} |
| Free Cash Flow | ${X} |

## Red Flags
- {any detected}

## Overall Assessment
{Financial health verdict with key rationale}
```

## Gotchas

- **Revenue ≠ cash**: Under accrual accounting, revenue is recorded when earned (product delivered), not when cash is received. Check accounts receivable to see how much revenue is still uncollected.
- **EBITDA is not cash flow**: EBITDA ignores capex, working capital changes, and taxes — all of which are real cash costs. Use free cash flow for cash analysis.
- **One-time items distort trends**: Restructuring charges, asset sales, legal settlements create one-time spikes or dips. Use "adjusted" or "normalized" figures for trend analysis.
- **Taiwan IFRS vs US GAAP**: Taiwan-listed companies use IFRS (TIFRSs). Some treatment differs from US GAAP (lease accounting, revenue recognition details). Note which standard applies.

## References

- For financial ratio analysis deep-dive, see the biz-financial-ratios skill
- For DuPont ROE decomposition, see the biz-dupont skill
