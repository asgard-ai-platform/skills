---
name: "fin-earnings-summary"
description: "Summarize and analyze earnings calls (法說會) including financial highlights, management commentary, guidance, and analyst Q&A key takeaways. Use this skill when the user needs to digest an earnings call transcript, extract key financial data and forward guidance, compare actual results vs consensus estimates, or prepare for an investor meeting — even if they say 'summarize this earnings call', 'what did management say about next quarter', 'did they beat estimates', or 'key takeaways from the 法說會'."
metadata:
  category: "WP-08 財務投資"
  tags: ["finance", "earnings", "investor-relations", "analysis"]
---

# Earnings Call Summary & Analysis

## Framework

```
IRON LAW: Separate Facts from Spin

Management presentations emphasize positives and downplay negatives.
Your job is to extract: (1) hard numbers, (2) forward guidance with
specificity level, and (3) what management DIDN'T say (notable omissions).

"Strong momentum" without numbers is spin.
"Revenue grew 15% to NT$2.3B" is a fact.
```

### Earnings Call Structure

| Section | Duration | What to Extract |
|---------|----------|----------------|
| **Prepared Remarks** | 15-20 min | Revenue, EPS, margins, key metrics — actual vs guidance vs consensus |
| **Management Commentary** | 10-15 min | Forward guidance, strategic initiatives, market outlook |
| **Q&A** | 20-30 min | What analysts are worried about (revealed by their questions), management's candor level |

### Key Data Points to Extract

**Financial Highlights (vs Consensus)**
| Metric | Actual | Consensus | Beat/Miss | YoY Change |
|--------|--------|----------|-----------|-----------|
| Revenue | ${X} | ${X} | Beat/Miss by {%} | {%} |
| EPS | ${X} | ${X} | Beat/Miss by {%} | {%} |
| Gross Margin | {%} | {%} | ±{pp} | ±{pp} |
| Operating Margin | {%} | {%} | ±{pp} | ±{pp} |

**Forward Guidance**
| Metric | Guidance | Prior Guidance | Change | Specificity |
|--------|---------|---------------|--------|------------|
| Next Q Revenue | ${X}-${X} | ${X}-${X} | Raised/Maintained/Lowered | Specific/Vague |
| Full Year EPS | ${X}-${X} | ... | ... | ... |

**Qualitative Signals**
- New product/initiative announcements
- Market/demand commentary (strengthening, stable, weakening)
- Competitive positioning updates
- Capital allocation (buyback, dividend, M&A, capex)
- Tone: confident, cautious, defensive, evasive

### Analysis Steps

**Phase 1: Extract Numbers**
- Revenue, EPS, margins — actual vs consensus vs prior guidance
- Beat or miss on each line item

**Phase 2: Evaluate Guidance**
- Did they raise, maintain, or lower guidance?
- How specific is the guidance? (range vs vague)
- Implied assumptions (growth rate, margin trajectory)

**Phase 3: Read the Q&A**
- What are analysts asking? (reveals market concerns)
- Where does management deflect or give vague answers? (red flags)
- New information that wasn't in prepared remarks

**Phase 4: Compare to Market Reaction**
- Stock price move post-earnings
- Does the market reaction align with the numbers? (sometimes a beat is sold off = guidance disappointed)

## Output Format

```markdown
# Earnings Summary: {Company} — {Quarter}

## Headline
{One sentence: beat/miss + most important takeaway}

## Financial Highlights
| Metric | Actual | Consensus | vs Consensus | YoY |
|--------|--------|----------|-------------|-----|
| Revenue | ... | ... | ... | ... |
| EPS | ... | ... | ... | ... |

## Forward Guidance
| Metric | New Guidance | Prior | Change |
|--------|------------|-------|--------|
| ... | ... | ... | Raised/Maintained/Lowered |

## Management Commentary (Key Points)
1. {key point with quote}
2. {key point}

## Q&A Highlights
- **Analyst concern**: {topic} → **Management response**: {summary}
- **Notable omission**: {what wasn't addressed}

## Market Reaction
- Post-earnings move: {+/-X%}
- Interpretation: {why the market reacted this way}

## Investment Implication
{What this means for the investment thesis — bullish/neutral/bearish signal}
```

## Gotchas

- **Beats can be "low quality"**: Beating EPS by cutting costs while revenue misses is a low-quality beat. Revenue beats with margin expansion is high quality. Differentiate.
- **Guidance matters more than actuals**: The market prices in expectations. A company that beats Q3 but lowers Q4 guidance will often sell off. Focus on forward-looking signals.
- **Taiwan 法說會 specifics**: Many Taiwan companies (especially TSMC, MediaTek) hold English-language calls. Others are Chinese-only. MOPS has summary notes even if you can't attend live.
- **Consensus estimates can be stale**: If estimates haven't been updated recently, a "beat" may just mean the bar was set too low. Check when consensus was last revised.
- **One quarter doesn't make a trend**: Don't overreact to a single quarter. Look at 3-4 quarters to identify real trends vs noise.

## References

- For financial statement analysis, see the data-financial-analysis skill
- For Taiwan stock data sources, see the tw-stock-analysis skill
