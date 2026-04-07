---
name: "fin-modeling"
description: "Build three-statement financial models (Income Statement, Balance Sheet, Cash Flow) with revenue forecasting, assumption management, and scenario analysis. Use this skill when the user needs to project financials, build a fundraising model, create financial projections for a business plan, or evaluate M&A targets — even if they say 'build a financial model', 'project our revenue', 'how much money will we make next year', or 'model this acquisition'."
metadata:
  category: "WP-08 財務投資"
  tags: ["finance", "financial-modeling", "forecasting", "three-statement"]
---

# Three-Statement Financial Modeling

## Framework

```
IRON LAW: The Three Statements Must Balance

Assets = Liabilities + Equity (Balance Sheet identity)
Net Income flows from IS to BS (retained earnings)
Cash flow bridges IS and BS through working capital and capex

If your model doesn't balance, there's an error. Check the cash line on
the BS against the ending cash on the CF statement. They MUST match.
```

### Model Architecture

```
[Assumptions Page] → drives everything
    ↓
[Income Statement] → Revenue, costs, taxes → Net Income
    ↓
[Balance Sheet] → Assets, liabilities, equity → must balance
    ↓
[Cash Flow Statement] → Start cash + Operating + Investing + Financing = End cash
    ↓
[Outputs: DCF, Returns, Scenarios]
```

### Revenue Forecasting Methods

| Method | How | Best For |
|--------|-----|----------|
| **Top-down** | Market size × market share × price | New markets, macro-driven |
| **Bottom-up** | Units × price, or customers × ARPU | Established products, SaaS |
| **Run-rate** | Current monthly × 12, adjusted for growth | Near-term projections |
| **Cohort-based** | New cohort revenue + existing cohort retention | Subscription businesses |

### Key Assumptions to Document

| Category | Assumptions |
|----------|------------|
| **Revenue** | Growth rate, pricing, volume, churn (if subscription) |
| **COGS** | Gross margin trajectory, input cost inflation |
| **OpEx** | Headcount plan, salary inflation, marketing as % of revenue |
| **Working Capital** | DSO (days sales outstanding), DPO (days payable), DIO (days inventory) |
| **CapEx** | Capital expenditure as % of revenue or specific projects |
| **Tax** | Effective tax rate, tax loss carryforwards |
| **Financing** | Debt schedule, interest rates, equity raises |

### Building Steps

**Phase 1: Assumptions**
1. Document all assumptions on a dedicated page
2. Color code: blue = input, black = formula, green = linked from another sheet
3. Each assumption must have a source or rationale

**Phase 2: Income Statement**
4. Build revenue line from assumptions
5. COGS and gross profit
6. Operating expenses by category
7. EBITDA, depreciation, EBIT
8. Interest, taxes, net income

**Phase 3: Balance Sheet**
9. Working capital items from IS drivers (DSO × Revenue/365, etc.)
10. Fixed assets: prior period + capex - depreciation
11. Debt schedule: prior period + new borrowing - repayment
12. Equity: prior period + net income - dividends + equity raises
13. **CHECK: Assets = Liabilities + Equity**

**Phase 4: Cash Flow**
14. Start with net income
15. Add back non-cash items (depreciation, amortization)
16. Working capital changes (from BS period-over-period)
17. CapEx (investing)
18. Debt and equity changes (financing)
19. **CHECK: Ending cash = BS cash line**

**Phase 5: Scenarios**
20. Base case (most likely assumptions)
21. Bull case (optimistic — higher growth, better margins)
22. Bear case (pessimistic — lower growth, margin pressure)

## Output Format

```markdown
# Financial Model: {Company} — {Projection Period}

## Key Assumptions
| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Source |
|-----------|-----|-----|-----|-----|-----|--------|
| Revenue growth | {%} | {%} | {%} | {%} | {%} | {basis} |
| Gross margin | {%} | ... | ... | ... | ... | ... |
| OpEx growth | {%} | ... | ... | ... | ... | ... |

## Projected Income Statement
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|-----|-----|-----|-----|-----|
| Revenue | ${X} | ... | ... | ... | ... |
| Gross Profit | ${X} | ... | ... | ... | ... |
| EBITDA | ${X} | ... | ... | ... | ... |
| Net Income | ${X} | ... | ... | ... | ... |

## Scenario Comparison
| Metric (Y5) | Bear | Base | Bull |
|-------------|------|------|------|
| Revenue | ${X} | ${X} | ${X} |
| Net Income | ${X} | ${X} | ${X} |
| FCF | ${X} | ${X} | ${X} |

## Balance Check
- BS balances: ✓/✗
- CF ending cash = BS cash: ✓/✗
```

## Gotchas

- **Revenue is the most sensitive assumption**: A 2% difference in growth rate compounds enormously over 5 years. Always present a range, not a point estimate.
- **Working capital is often forgotten**: Fast-growing companies consume cash in working capital (building inventory, extending credit). A profitable company can run out of cash if working capital isn't modeled.
- **Circular references with interest**: Interest expense depends on debt balance, which depends on cash (which may require more debt). Break the circularity with an iterative calculation or prior-period debt balance.
- **Granularity should match certainty**: Model Year 1 monthly, Year 2 quarterly, Years 3-5 annually. Detailed monthly projections for Year 5 are false precision.
- **Assumptions page is the most important page**: Nobody should need to dig into formulas to understand what drives your model. All assumptions visible, documented, and changeable in one place.

## References

- For DCF valuation built on the three-statement model, see the biz-dcf skill
- For spreadsheet best practices, see `references/modeling-best-practices.md`
