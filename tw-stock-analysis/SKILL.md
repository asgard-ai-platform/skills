---
name: "tw-stock-analysis"
description: "Analyze Taiwan-listed stocks using fundamental analysis including EPS, P/E ratio, dividend yield, and financial statement review. Use this skill when the user needs to evaluate a Taiwan stock, compare TWSE/TPEx-listed companies, assess valuation, or review earnings — even if they say 'should I buy this stock', 'analyze 台積電', 'is this stock overvalued', or 'compare these two Taiwan companies'."
metadata:
  category: "WP-08 財務投資"
  tags: ["finance", "taiwan-stocks", "fundamental-analysis", "investment"]
---

# Taiwan Stock Fundamental Analysis

## Framework

```
IRON LAW: Valuation Is Relative — Compare to Peers and History

A P/E of 20 is cheap for a growth tech stock but expensive for a mature
utility. ALWAYS compare to: (1) industry peers, (2) the stock's own
historical range, and (3) the broader market (TAIEX average P/E ~14-18).
A single number in isolation is meaningless.
```

### Key Metrics for Taiwan Stocks

| Metric | Formula | What It Tells You | Data Source |
|--------|---------|------------------|------------|
| **EPS** | Net Income / Shares Outstanding | Profitability per share | 公開資訊觀測站 (MOPS) |
| **P/E Ratio** | Stock Price / EPS | How much market pays per dollar of earnings | Yahoo Finance TW, Goodinfo |
| **P/B Ratio** | Stock Price / Book Value per Share | Premium to net assets | MOPS |
| **Dividend Yield** | Annual Dividend / Stock Price | Income return | 公開資訊觀測站 |
| **Payout Ratio** | Dividends / Net Income | Sustainability of dividends | Calculated |
| **ROE** | Net Income / Shareholders' Equity | Return on equity | MOPS |
| **Debt-to-Equity** | Total Debt / Equity | Financial leverage | MOPS |
| **Revenue Growth** | (Current Rev - Prior Rev) / Prior Rev | Top-line momentum | Monthly revenue reports |

### Taiwan-Specific Data Sources

| Source | What It Has | URL |
|--------|-----------|-----|
| 公開資訊觀測站 (MOPS) | Financial statements, dividends, insider trading | mops.twse.com.tw |
| 台灣證券交易所 (TWSE) | Stock prices, trading volume, indices | www.twse.com.tw |
| Goodinfo | Historical financials, dividend history, technical data | goodinfo.tw |
| 證交所月營收 | Monthly revenue announcements (by the 10th) | MOPS + news |

### Analysis Steps

**Phase 1: Business Understanding**
- What does the company do? Which industry/sector?
- Who are the main competitors?
- What drives revenue? (products, segments, geographies)

**Phase 2: Financial Health**
- Revenue trend (monthly data unique to Taiwan market — check 月營收)
- Profitability: EPS trend, operating margin trend
- Balance sheet: D/E ratio, current ratio, cash position
- Cash flow: operating CF positive? Free cash flow trend?

**Phase 3: Valuation**
- P/E vs peers, vs own 5-year range, vs TAIEX average
- P/B vs peers (especially for asset-heavy industries)
- Dividend yield vs peers and vs Taiwan 10-year bond yield (~1.5%)

**Phase 4: Growth & Risk**
- Revenue growth rate vs industry
- Capex plans (MOPS announcements)
- Concentration risk (customer, product, geography)
- Regulatory and geopolitical risks

### Taiwan Market Specifics

| Feature | Detail |
|---------|--------|
| **Monthly revenue disclosure** | Listed companies report monthly revenue by the 10th — unique to Taiwan, provides more timely data than quarterly reports |
| **Dividend culture** | Taiwan investors heavily favor dividend stocks. High-yield stocks trade at a premium. |
| **Ex-dividend price adjustment** | Taiwan stocks drop by the dividend amount on ex-date. This is normal, not a loss. |
| **Day trading tax** | Securities transaction tax: 0.3% (0.15% for day trades). Factor into short-term trading costs. |
| **Foreign investor influence** | 外資 (foreign institutional investors) buying/selling data is public and significantly moves stock prices. Monitor 三大法人 (three institutional investors) data. |

## Output Format

```markdown
# Stock Analysis: {Company Name} ({Stock Code})

## Company Overview
- Industry: {sector}
- Market cap: NT${X}B
- Main business: {description}

## Financial Summary
| Metric | Current | 3-Year Avg | Peer Avg | Assessment |
|--------|---------|-----------|---------|-----------|
| EPS | NT${X} | NT${X} | NT${X} | Above/Below |
| P/E | {X}x | {X}x | {X}x | Cheap/Fair/Expensive |
| Dividend Yield | {%} | {%} | {%} | ... |
| ROE | {%} | {%} | {%} | ... |
| D/E | {X} | {X} | {X} | ... |

## Revenue Trend (Monthly)
| Month | Revenue (NT$M) | YoY Growth |
|-------|-------------|-----------|
| {month} | {amount} | {%} |

## Valuation Assessment
{Cheap / Fair / Expensive — with rationale comparing to peers and history}

## Key Risks
1. {risk}

## Investment Thesis
{Bull case vs bear case in 2-3 sentences each}
```

## Gotchas

- **EPS can be distorted by one-time items**: Check if EPS includes asset sales, legal settlements, or write-offs. Use "recurring EPS" (本業 EPS) for trend analysis.
- **Monthly revenue ≠ profitability**: A company growing revenue 30% might have declining margins. Revenue growth without margin analysis is incomplete.
- **Dividend yield trap**: A stock yielding 8% may be cheap for a reason (declining business, unsustainable payout). Check if the payout ratio > 80% — that may not be sustainable.
- **Taiwan stock prices adjust for dividends**: Unlike US stocks, Taiwan stock prices drop by the cash dividend amount on ex-date. A NT$100 stock paying NT$5 opens at NT$95. This is not a loss — you received NT$5 in cash.
- **This is educational analysis, not investment advice**: All investment carries risk. Past performance does not predict future results. Consult a licensed financial advisor.

## References

- For DCF valuation methodology, see the biz-dcf skill
- For financial ratio deep-dive, see the biz-financial-ratios skill
