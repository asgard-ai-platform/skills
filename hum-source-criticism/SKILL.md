---
name: "hum-source-criticism"
description: "Evaluate source credibility using primary/secondary classification, internal/external criticism, triangulation, and misinformation detection. Use this skill when the user needs to assess whether information is trustworthy, evaluate research sources, fact-check claims, or detect misinformation — even if they say 'can I trust this source', 'is this real', 'how reliable is this data', or 'fact-check this for me'."
metadata:
  category: "WP-19 文學院/人文"
  tags: ["humanities", "source-criticism", "fact-checking", "information-literacy"]
---

# Source Criticism

## Overview

Source criticism is a systematic method for evaluating whether information is trustworthy. Originally from historical methodology, it's now essential for navigating an information environment flooded with misinformation, opinion-as-fact, and AI-generated content.

## Framework

```
IRON LAW: No Source Is Automatically Trustworthy

Every source — including academic journals, government data, and news from
reputable outlets — has potential biases, errors, and limitations. Credibility
is assessed, not assumed. "It's from the New York Times / 中央社" is not
sufficient — WHAT are they reporting, based on WHAT evidence, and do other
sources corroborate it?
```

### Source Classification

**Primary sources**: Direct evidence from the time/event (original documents, raw data, eyewitness accounts, original research, official records)

**Secondary sources**: Analysis or interpretation of primary sources (textbooks, review articles, news analysis, biographies)

**Tertiary sources**: Compilations of primary and secondary (encyclopedias, Wikipedia, databases) — starting points, not endpoints

### Four Tests of Source Credibility

**1. External Criticism** — Is the source authentic?
- Who created it? Are they who they claim to be?
- When was it created? Is the date consistent?
- Is it the original or has it been altered?
- Is the publication/platform reputable?

**2. Internal Criticism** — Is the content reliable?
- Does the author have expertise in this topic?
- What is the author's potential bias or interest?
- Is the evidence cited? Can it be verified?
- Is the reasoning logical? Are conclusions supported by the evidence?

**3. Triangulation** — Do multiple independent sources agree?
- Check 3+ independent sources (not copies of the same original report)
- "Independent" means different authors, different organizations, different methods
- Agreement across independent sources strengthens confidence

**4. Currency** — Is the information current enough?
- When was it published? Has the situation changed since then?
- For fast-moving topics (AI, policy, markets), even 6-month-old sources may be outdated

### Red Flags for Misinformation

| Red Flag | Description |
|----------|-----------|
| No author or organization identified | Who stands behind this claim? |
| Emotional language without evidence | Designed to provoke, not inform |
| No primary sources cited | Claims without traceable evidence |
| "Studies show" without naming the study | Vague appeals to authority |
| Single source amplified across many sites | Same claim copied, not independently verified |
| Too good to be true / too outrageous | Extreme claims require extreme evidence |
| URL/domain mimics reputable source | Fakecnn.com, bbc-news.co (not bbc.co.uk) |

## Output Format

```markdown
# Source Evaluation: {Source/Claim}

## Source Identity
- Author/Organization: {who}
- Publication: {where}
- Date: {when}
- Type: Primary / Secondary / Tertiary

## Credibility Assessment
| Test | Assessment | Evidence |
|------|-----------|---------|
| External (authentic?) | ✓/⚠/✗ | {reasoning} |
| Internal (reliable?) | ✓/⚠/✗ | {reasoning} |
| Triangulation (corroborated?) | ✓/⚠/✗ | {other sources checked} |
| Currency (current?) | ✓/⚠/✗ | {relevance of date} |

## Red Flags
- {any detected red flags}

## Verdict
- Credibility: High / Moderate / Low
- Recommended action: {trust / verify further / discard}
```

## Examples

### Correct Application
**Scenario:** Evaluating a viral social media post claiming "Taiwan's GDP will surpass South Korea's by 2027"

| Test | Assessment | Evidence |
|------|-----------|---------|
| External | ⚠ | Anonymous account, no institutional affiliation, chart has no data source |
| Internal | ✗ | Uses nominal GDP (not PPP), cherry-picks semiconductor sector projection, ignores exchange rate volatility |
| Triangulation | ✗ | IMF and World Bank projections show no such convergence; no reputable analyst makes this claim |
| Currency | ✓ | Posted this month |

**Red flags**: Emotional headline ("Taiwan DESTROYS Korea"), no primary data source cited, single unsourced chart
**Verdict**: Low credibility — discard ✓

### Incorrect Application
- "This is from Reuters, so it must be true" → Credibility assumed, not assessed. Even reputable sources can be wrong, outdated, or framing an issue in a particular way. Violates Iron Law.

## Gotchas

- **Bias ≠ unreliable**: Every source has a perspective. A labor union's report on working conditions is biased but may contain accurate data. Assess bias AND accuracy separately.
- **Wikipedia is a starting point**: It's a tertiary source with references. Follow the references to primary/secondary sources. Don't cite Wikipedia as evidence — cite what Wikipedia cites.
- **AI-generated content**: AI can produce convincing but fabricated "sources" (fake papers, fake quotes, fake statistics). Verify that cited sources actually exist.
- **Consensus ≠ truth, but it's a strong signal**: Scientific consensus (climate change, vaccine safety) is the strongest available evidence. Lone dissenting "experts" who contradict consensus need extraordinary evidence.
- **Source credibility is domain-specific**: A cardiologist is a credible source on heart disease but not on economics. Match expertise to the claim.

## References

- For CRAAP test (Currency, Relevance, Authority, Accuracy, Purpose), see `references/craap-test.md`
- For fact-checking tools and databases, see `references/fact-check-tools.md`
