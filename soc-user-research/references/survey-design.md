# Survey Design Reference

## When Surveys Are the Right Tool

Surveys answer **"how many"** and **"how prevalent"** questions. They fail at **"why"** questions.

Use a survey when:
- You need to measure something across a large population (n > 100)
- You've already done qualitative research and know what to measure
- You need to segment or compare across groups (age, usage tier, geography)
- You want to track a metric over time (NPS, satisfaction)

Do **not** use a survey when:
- You're still discovering what the real problem is (run interviews first)
- The topic is nuanced enough that context matters per respondent
- Your sample will be < 30 (descriptive stats become meaningless)

---

## Sample Size

### Minimum Viable Sample

For a single proportion (e.g., "% of users who experience X"):

```
n = (Z² × p × (1 - p)) / e²
```

| Symbol | Meaning | Typical default |
|--------|---------|----------------|
| Z | Z-score for confidence level | 1.96 (95% CI) |
| p | Expected proportion | 0.5 (maximizes variance when unknown) |
| e | Acceptable margin of error | 0.05 (±5%) |

**Worked example** — you want to know what % of users abandon checkout:

```
n = (1.96² × 0.5 × 0.5) / 0.05²
  = (3.84 × 0.25) / 0.0025
  = 0.96 / 0.0025
  = 384 respondents
```

If you expect the proportion is closer to 10% (rare event), you can shrink:

```
n = (1.96² × 0.10 × 0.90) / 0.05²
  = (3.84 × 0.09) / 0.0025
  = 138 respondents
```

### For Subgroup Comparisons

If you need to compare two segments (e.g., mobile vs. desktop users), each segment needs the minimum sample size independently. If mobile is 20% of traffic and you need 384 total for mobile, your total survey n ≥ 1,920.

### Practical rule of thumb

| Goal | Minimum n |
|------|-----------|
| General prevalence (±5%, 95% CI) | 385 |
| Two-group comparison | 385 per group |
| Track trend over time (detect 5pp shift) | 200 per wave |
| Pilot/exploratory | 30–50 (descriptive only, no significance claims) |

---

## Survey Structure

### Ordering Principle

```
Screener → General context → Specific topic → Attitude/ratings → Sensitive topics → Demographics
```

**Why this order:**
- Screeners disqualify ineligible respondents before they waste time
- General context questions prime recall without biasing specific answers
- Attitude questions after behavior questions (not before — priming effect)
- Demographics last: reduces abandonment by not opening with "How old are you?"

### Section-by-Section Guide

**1. Screener (1-3 questions)**

Must establish eligibility. Be explicit about disqualifying conditions.

```
Have you ordered food delivery in the past 30 days?
○ Yes → continue
○ No → [DISQUALIFY] Thank you, you don't qualify for this study.
```

Do not reveal why they're being screened — it biases who self-selects.

**2. Context / Behavioral recall (2-4 questions)**

Ask about the most recent relevant experience, not habits in general. Recency reduces false memory.

```
✓ "Think about the last time you placed a food delivery order.
   Approximately how long ago was that?"

✗ "How often do you usually order food delivery?"
   (People report aspirational habits, not actual behavior)
```

**3. Core topic questions (5-10 questions)**

This is the measurement section. Use validated scales where they exist (see Scales section below). Group related questions together.

**4. Attitude / satisfaction questions (2-4 questions)**

Place overall satisfaction or NPS here — after specific questions, so respondents have had a chance to reflect on the experience concretely.

**5. Open-ended (1-2 questions maximum)**

```
Is there anything else you'd like to share about your experience?
```

One open-ended is valuable. More than two creates survey fatigue and the responses become thin.

**6. Demographics (3-5 questions)**

Ask only what you'll actually use in analysis. Typical set:
- Age range (brackets, not exact year)
- Gender (with "prefer not to say")
- Location (region/country, not street address)
- Relevant behavioral segment (e.g., "How many times per month do you order delivery?")

---

## Question Writing

### The Double-Barrel Problem

A double-barreled question asks two things at once. You cannot know which the respondent is answering.

```
✗ "How satisfied are you with the speed and accuracy of your orders?"
   (Fast but inaccurate → what rating do they give?)

✓ "How satisfied are you with the speed of your orders?"
✓ "How satisfied are you with the accuracy of your orders?"
```

**Diagnostic test**: Can you answer the question with one thought? If not, split it.

### Leading Questions

Leading questions contain the expected answer.

```
✗ "How easy was it to find what you were looking for?"
   (Assumes they found it; implies it should be easy)

✓ "Were you able to find what you were looking for today?"
   ○ Yes, easily
   ○ Yes, but it took effort
   ○ No
```

Other patterns that lead:
- "Don't you think…" → Never use
- "How much did you enjoy…" → Assumes enjoyment occurred
- "Why did you love…" → Assumes the sentiment

### Hypothetical Questions

```
✗ "Would you pay $5/month for an ad-free version?"
   (People dramatically overstate willingness to pay)

✓ Measure actual behavior via experiment (A/B test pricing)
✓ Or use conjoint analysis if you must survey (forces trade-offs)
```

Hypotheticals are acceptable only for screening (e.g., "If we invited you to a 60-min interview, would you be available?") — not for measuring preferences or behavior.

### Response Scale Consistency

Pick one direction and stick to it for the entire survey.

```
1 = Strongly disagree ... 5 = Strongly agree   ← pick this
5 = Strongly disagree ... 1 = Strongly agree   ← or this, but NEVER BOTH
```

Mixing directions within a survey causes response errors, especially on mobile.

---

## Validated Scales

Use these rather than inventing your own. They have established benchmarks and psychometric validation.

### Likert Scale (Agreement/Satisfaction)

5-point is sufficient for most purposes. 7-point adds precision but also burden.

```
5-point:
1 - Strongly disagree
2 - Disagree
3 - Neither agree nor disagree
4 - Agree
5 - Strongly agree
```

**Reporting**: Report mean and standard deviation, not just mean. A mean of 3.8 with SD 1.4 is very different from mean 3.8 with SD 0.4.

**Neutral midpoint debate**: Including a neutral option ("Neither") gives an escape hatch to uncertain respondents and produces more honest data. Removing it forces a position but creates noise from forced choices. **Recommendation**: Keep the neutral option unless you specifically need forced choice.

### Net Promoter Score (NPS)

```
"How likely are you to recommend [product/company] to a friend or colleague?"
0 (Not at all likely) — 10 (Extremely likely)
```

Calculate:
```
NPS = % Promoters (9–10) − % Detractors (0–6)
Passives (7–8) are excluded from the calculation
```

**Benchmarks by industry** (vary significantly — always compare to your own historical baseline first):

| Industry | Median NPS |
|----------|------------|
| Software/SaaS | 30–40 |
| E-commerce | 40–50 |
| Consumer apps | 25–35 |

**Limitations**: NPS is a single-number summary that masks distribution. A score of 30 could come from 65% Promoters / 35% Detractors or 45% Promoters / 15% Detractors — very different situations. Always report the underlying distribution.

Always follow NPS with: "What is the primary reason for your score?" (open text). Without this, the number is unactionable.

### System Usability Scale (SUS)

10-question scale measuring perceived usability. Ask after a usage session or about a specific product experience.

```
1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.
```

All responses: 1 (Strongly disagree) → 5 (Strongly agree)

**Scoring formula:**
```
Odd-numbered items (1,3,5,7,9):  score = response − 1
Even-numbered items (2,4,6,8,10): score = 5 − response
SUS = sum of all 10 adjusted scores × 2.5
Range: 0–100
```

**Interpretation:**

| SUS Score | Grade | Adjective |
|-----------|-------|-----------|
| ≥ 85 | A+ | Excellent |
| 78–84 | B | Good |
| 68–77 | C | OK |
| 51–67 | D | Poor |
| ≤ 50 | F | Unacceptable |

Industry average across products: ~68. Use this as a baseline, but compare to your product's own trend over time.

---

## Survey Fatigue and Length

### Completion Rate vs. Length

| Survey length | Estimated completion rate (cold email panel) |
|--------------|----------------------------------------------|
| < 5 min | 60–70% |
| 5–10 min | 40–60% |
| 10–15 min | 20–40% |
| > 15 min | < 20% |

In-app surveys (triggered during session) can be slightly longer because respondent context is fresh.

### Reducing Fatigue Without Cutting Questions

- **Matrix questions**: Group related Likert items into a table (cuts visual length significantly)
- **Conditional logic**: Skip questions that don't apply (e.g., if they said "No" to using a feature, skip the feature satisfaction questions)
- **Progress indicator**: Show "Question 5 of 12" — respondents are less likely to abandon when they can see the end
- **Mobile-first layout**: If > 50% of respondents are on mobile, avoid matrix grids (they render poorly)

---

## Analysis Procedure

### Step 1: Data Cleaning

Before any analysis:

1. Remove incomplete responses (< 50% completion rate per respondent)
2. Check completion time — remove anyone who completed in < 1/3 the expected time (likely clicking through randomly)
3. Check open-text responses for gibberish or copy-paste spam
4. Verify screener logic was enforced — look for disqualified respondents who slipped through

### Step 2: Descriptive Statistics

For every closed-ended question, compute:
- **Mean** (for scales)
- **Standard deviation** (spread)
- **Frequency distribution** (% per response option)

Always look at distribution before reporting mean. A bimodal distribution (half 1s, half 5s) with a mean of 3 is misleading — it signals a segmented population, not a neutral one.

### Step 3: Cross-Tabulation

Segment responses by key groupings:

```
Example: satisfaction score by user tenure

          New (< 30d)   Mid (30–180d)   Power (180d+)
Mean NPS       22            38               61
n              84           147              203
```

This reveals whether satisfaction problems are onboarding issues or long-term friction.

Common segmentation variables:
- Usage frequency (light / medium / heavy)
- Platform (iOS / Android / web)
- Acquisition channel (organic / paid / referral)
- Geography

### Step 4: Statistical Significance for Comparisons

When comparing two groups, use a two-proportion z-test or t-test. Do not report differences without checking significance.

**For proportions** (e.g., "Group A: 42% satisfied; Group B: 51% satisfied"):

```
z = (p1 - p2) / sqrt(p̄(1-p̄)(1/n1 + 1/n2))

where p̄ = (x1 + x2) / (n1 + n2)  [pooled proportion]
```

Reject null hypothesis (no difference) if |z| > 1.96 (p < 0.05).

**For means** (e.g., NPS scores): use Welch's t-test if sample sizes differ.

**Report effect size alongside p-value.** A difference can be statistically significant but practically irrelevant (e.g., NPS of 41 vs. 43 with n=5,000 per group: significant, but 2 points is noise). Cohen's d for means:

```
d = (mean1 - mean2) / pooled SD

Small: d = 0.2
Medium: d = 0.5
Large: d = 0.8
```

### Step 5: Open-Text Analysis

For the 1-2 open-ended questions:
1. Read all responses first without categorizing
2. Identify 5-8 recurring themes
3. Code each response to one primary theme (or "Other")
4. Report theme frequency + 2-3 representative verbatim quotes per theme

Do not paraphrase quotes in your report. Use verbatim text in quotation marks. Attribution: use only anonymized identifiers (R-042, not name or email).

---

## Common Analysis Mistakes

**Mistake: Reporting mean on a non-interval scale**

Likert scales are ordinal — the gap between 1 and 2 may not equal the gap between 4 and 5. Strictly speaking, you should report median and mode. In practice, most researchers report means for 5+ point scales because the error is small, but be aware of the limitation.

**Mistake: n < 30 cross-tab cells**

If a subgroup has fewer than 30 respondents, do not report statistics for that cell as conclusive. Flag it explicitly: "n=18; interpret with caution."

**Mistake: Ignoring non-response bias**

People who complete your survey are systematically different from people who don't. Those who are very happy or very unhappy respond more than neutral users. If your completion rate is < 30%, your sample may not represent the population. Acknowledge this limitation in any report.

**Mistake: Treating correlation as causation**

"Users who use the app 5+ times/week have NPS of 65; users who use it 1x/week have NPS of 30" does not mean frequency drives satisfaction. Both could be caused by a third variable (e.g., users who get value use it more AND rate it higher). Survey data identifies relationships, not causal direction.
