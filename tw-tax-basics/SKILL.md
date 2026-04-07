---
name: "tw-tax-basics"
description: "Navigate Taiwan's tax system including corporate income tax (營所稅), business tax (營業稅), personal income tax, withholding obligations, and startup tax incentives. Use this skill when the user needs to understand Taiwan tax obligations, calculate tax liability, file taxes, or plan for tax efficiency — even if they say 'how much tax do we owe', 'what's the corporate tax rate in Taiwan', 'tax filing deadlines', or 'are there startup tax breaks'."
metadata:
  category: "WP-05 台灣創業"
  tags: ["taiwan", "tax", "corporate-tax", "startup"]
---

# Taiwan Tax Basics

## Framework

```
IRON LAW: Three Taxes Every Taiwan Business Must Know

1. 營業稅 (Business Tax / VAT): 5% on sales, filed bimonthly
2. 營利事業所得稅 (Corporate Income Tax): 20% on profit, filed annually
3. 扣繳 (Withholding Tax): Withheld at source on payments to individuals/foreigners

Missing any filing deadline triggers penalties. Set up calendar reminders
for ALL filing dates at company registration.
```

### Tax Calendar

| Tax | Rate | Filing Frequency | Deadline |
|-----|------|-----------------|----------|
| 營業稅 (VAT) | 5% | Bimonthly | 15th of following odd month (Jan 15, Mar 15, May 15...) |
| 營所稅 (CIT) | 20% | Annual | May 1-31 (for prior year) |
| 暫繳 (Interim CIT) | 50% of prior year | Annual | September 1-30 |
| 扣繳 (Withholding) | Varies | Monthly + annual | 10th of following month; annual filing by Jan 31 |
| 個人綜所稅 | Progressive 5-40% | Annual | May 1-31 |

### Corporate Income Tax (營所稅)

```
Taxable Income = Revenue - Cost of Goods Sold - Operating Expenses - Non-operating Deductions
Tax = Taxable Income × 20%

Special cases:
- Taxable income ≤ NT$120,000: tax-free
- NT$120,001 ~ NT$500,000: half rate applied on amount exceeding $120K
- > NT$500,000: full 20% rate
```

**Common deductions**:
- Employee salaries and benefits
- Rent, utilities, office expenses
- Depreciation on fixed assets
- R&D expenses (additional 200% deduction under 產創條例)
- Bad debt (with proper documentation)

### Business Tax (營業稅 / VAT)

| Transaction | VAT Treatment |
|------------|--------------|
| Domestic sales | Charge 5% → collect from buyer → remit to government |
| Domestic purchases | Pay 5% → claim as input tax credit |
| Export sales | Zero-rated (0%) — can still claim input credits |
| Import purchases | Pay 5% at customs → claim as input credit |

**Filing**: Net VAT = Output tax (collected) - Input tax (paid). If negative (more input than output), get a refund.

### Withholding Tax (扣繳)

| Payment Type | Resident Rate | Non-Resident Rate |
|-------------|-------------|------------------|
| Salary | 5% (if monthly > certain threshold) | 6-18% |
| Professional service fees | 10% | 20% |
| Rent | 10% | 20% |
| Dividends | Included in personal income | 21% |
| Royalties | 10% | 20% |
| Interest | 10% | 20% |

### Startup Tax Incentives

| Incentive | What It Does | Who Qualifies |
|-----------|-------------|--------------|
| 產創條例 R&D 投資抵減 | 15% of R&D spend as tax credit (or 10% over 3 years) | Companies with qualifying R&D activities |
| 天使投資人減稅 | Individual investors can deduct up to NT$3M from income | Investment in startups < 2 years old, held 2+ years |
| 員工認股權 (ESOP) | Deferred taxation on stock options until exercise | Companies issuing employee stock options |
| 營所稅 小規模免稅 | Taxable income ≤ NT$120K exempt | Very small businesses |

## Output Format

```markdown
# Taiwan Tax Assessment: {Company}

## Tax Obligations
| Tax | Applicable? | Rate | Next Filing |
|-----|-----------|------|------------|
| 營業稅 | Y/N | 5% | {date} |
| 營所稅 | Y/N | 20% | {date} |
| 扣繳 | Y/N | varies | {date} |

## Estimated Tax Liability
| Tax | Estimated Amount | Notes |
|-----|-----------------|-------|
| 營業稅 (net) | NT${X}/bimonth | Output - Input |
| 營所稅 | NT${X}/year | Revenue - Expenses × 20% |

## Available Incentives
| Incentive | Eligible? | Estimated Benefit |
|-----------|----------|------------------|
| {incentive} | Y/N | NT${X} |

## Action Items
1. {immediate tax action needed}
```

## Gotchas

- **營業稅 and 營所稅 are different taxes**: 營業稅 is VAT on transactions (5%). 營所稅 is corporate income tax on profit (20%). Both are required. Don't confuse them.
- **Input VAT requires 統一發票**: You can only claim input tax credits with proper 統一發票 (uniform invoice). Receipts (收據) from non-registered vendors don't count.
- **Foreign service payments**: Paying a foreign SaaS provider (AWS, Google, etc.)? You must withhold 20% tax and report it, unless a tax treaty applies. Many startups miss this.
- **Transfer pricing for cross-border**: If you have related-party transactions with overseas entities, transfer pricing rules apply. Document arm's-length pricing.
- **This is educational guidance, not tax advice**: Taiwan tax law is amended frequently. Consult a licensed CPA (會計師) for specific tax situations and filings.

## References

- For e-invoice system, see the tw-einvoice-guide skill
- For detailed CIT deduction rules, see `references/cit-deductions.md`
