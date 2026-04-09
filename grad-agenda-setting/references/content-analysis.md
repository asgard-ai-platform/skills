# Content Analysis for Agenda-Setting Research

Content analysis in agenda-setting research serves one purpose: operationalizing the **media agenda** — converting media output into quantifiable salience scores that can be correlated with public agenda data.

---

## What to Count and Why

Agenda-setting research requires two kinds of measurement:

| Measure | What it captures | First-level or Second-level |
|---|---|---|
| **Story frequency** | How often an issue appears | First-level (object salience) |
| **Story prominence** | Where/how it appears | First-level (object salience) |
| **Attribute frequency** | Which characteristics of the issue appear | Second-level (attribute salience) |
| **Attribute tone** | How those characteristics are framed | Second-level (attribute salience) |

Do not conflate frequency with prominence. A story buried on page A14 should not carry the same salience weight as a front-page lead.

---

## Salience Scoring Formula

### Newspaper (Print / Online)

```
S_issue = Σ (w_i × f_i)
```

Where:
- `S_issue` = composite salience score for a given issue in a given time unit (e.g., one week)
- `f_i` = frequency count for placement category `i`
- `w_i` = placement weight for category `i`

**Standard placement weight scheme (McCombs & Shaw, 1972 protocol):**

| Placement | Weight (w) |
|---|---|
| Front page, above the fold, lead story | 6 |
| Front page, above the fold, non-lead | 5 |
| Front page, below the fold | 4 |
| Section front page (A section) | 3 |
| Interior page, > 12 column-inches | 2 |
| Interior page, ≤ 12 column-inches | 1 |
| Brief / single paragraph | 0.5 |

**Worked example:**

In a two-week window, "housing affordability" appears in the *New York Times* as:
- 1 front-page lead story → 1 × 6 = 6
- 2 front-page non-lead → 2 × 5 = 10
- 3 interior articles > 12 col-in → 3 × 2 = 6
- 4 briefs → 4 × 0.5 = 2

`S_housing = 6 + 10 + 6 + 2 = 24`

Repeat for each issue in your issue set, then rank them by `S_issue` to construct the media agenda for that time unit.

### Broadcast / Online Video

Replace column-inches with airtime:

| Segment position | Weight (w) |
|---|---|
| Lead story (first item) | 6 |
| Second or third item | 4 |
| Later in broadcast | 2 |
| Mentioned in passing (< 30 sec) | 0.5 |

### Social / Digital Media

For digital sources, prominence is less clearly defined. Use a hybrid:

```
S_digital = α × (mention_count) + β × (engagement_score) + γ × (trending_flag)
```

Where `α`, `β`, `γ` are weights summing to 1.0, set based on your theoretical priority. If you are measuring *elite media* agenda-setting (editors' choices), weight `α` heavily. If measuring *participatory* agenda-setting, weight `β` and `γ` more.

**Warning:** Social media salience metrics are highly platform-specific and change as platforms alter their algorithms. Document your operationalization explicitly, and do not compare social salience scores across years unless you verify the platform's measurement API has not changed.

---

## Sampling Strategy

### Universe Definition

Specify:
1. **Media outlets** — which publications/channels represent "the media agenda" you are studying? For national-level agenda-setting, use the top-5 circulation newspapers + major broadcast networks as a defensible baseline.
2. **Time period** — must bracket the public opinion measurement date, with enough lead time to capture the lag. Rule of thumb: collect media data **8–12 weeks before** the public agenda measurement point.
3. **Issue set** — the list of issues you will code. Define this before coding begins. Adding issues after seeing data introduces confirmation bias.

### Constructed Week Sampling

For studies spanning months or years, a **constructed week** sample is standard:

1. Identify your study period (e.g., 12 months)
2. Randomly select 2 Mondays, 2 Tuesdays, ... 2 Sundays from across the year
3. This gives you ~14 days of coverage that generalizes to the full year without requiring you to code every issue

**Why not random days?** Day-of-week effects exist (Sunday editions are larger; Monday news is thinner). Constructed weeks control for this.

### Minimum Sample Size

For a single outlet, a constructed week (~14 issues/editions) is adequate for yearly estimates. For sub-period analysis (monthly agenda shifts), code all issues in each month.

---

## Codebook Structure

A minimal codebook for first-level agenda-setting:

```
UNIT OF ANALYSIS: Individual story/article

Variables to code per unit:
  1. story_id       — unique identifier
  2. date           — YYYY-MM-DD
  3. outlet         — coded name of media outlet
  4. placement_code — integer 1–7 per placement scheme above
  5. word_count     — total word count of story
  6. issue_primary  — primary issue coded (from issue set)
  7. issue_secondary — secondary issue if present (or "none")
  8. photo_present  — 0/1
  9. photo_size     — "large" / "small" / "none"
```

For second-level coding, add:

```
  10. attribute_list — list of attributes mentioned (from attribute codebook)
  11. attribute_tone — per attribute: +1 positive / 0 neutral / -1 negative
```

---

## Inter-Coder Reliability

Agenda-setting content analysis requires at least two coders. Report reliability **before** using the data.

### Krippendorff's Alpha (recommended)

Preferred over percent agreement because it accounts for chance agreement and works for nominal, ordinal, and interval data.

```
α = 1 - (D_o / D_e)
```

Where:
- `D_o` = observed disagreement
- `D_e` = expected disagreement (based on distribution of codes)

**Acceptable thresholds:**

| α value | Interpretation |
|---|---|
| ≥ 0.80 | Acceptable for most purposes |
| 0.67–0.79 | Acceptable for exploratory research; note as limitation |
| < 0.67 | Do not use data; revise codebook and retrain |

### What to test reliability on

Test on **at minimum 10% of your sample**, randomly selected and coded independently by both coders before one coder sees the other's work.

Test each variable separately. It is common for `placement_code` to have α ≥ 0.90 while `issue_primary` has α closer to 0.70. Report per-variable alphas.

### Issue Category Reliability is the Hard Part

The typical weak point in agenda-setting content analysis is issue classification, not placement coding. Improve it by:

1. Writing **decision rules** for ambiguous cases in the codebook (e.g., "stories about inflation AND unemployment: classify under the issue that occupies ≥ 60% of word count; if tie, use `issue_primary = 'economy_general'`")
2. Running a training round before the reliability test: have both coders independently code 10 "practice" stories, discuss disagreements, update the codebook
3. Including example stories in the codebook for each issue category

---

## Constructing the Time Series

For agenda-setting correlation analysis, you need a **salience time series** for each issue, not a single score.

Aggregate salience scores into time units (typically weeks or months):

```python
# Pseudocode — adapt to your data format
for each time_unit t:
    for each issue i:
        media_salience[i][t] = sum(w_j for all stories j 
                                   where story.issue == i 
                                   and story.date in t)
```

Then construct a parallel time series for the **public agenda** from survey data (e.g., Gallup "Most Important Problem" percentage for each issue by month).

**Align the axes before computing correlation.** Media salience in week `t` should be correlated with public salience at time `t + lag`, not at time `t`. Test multiple lag values (2, 4, 6, 8 weeks) and report which lag produces the strongest correlation — this is part of your findings, not p-hacking, as long as you pre-register the range.

---

## Cross-Outlet Aggregation

When your media agenda includes multiple outlets, you must decide how to combine their salience scores.

**Option A — Unweighted mean:**
```
S_combined[i][t] = mean(S_outlet_k[i][t] for k in outlets)
```
Use when all outlets are treated as equal representatives of "the media."

**Option B — Circulation-weighted mean:**
```
S_combined[i][t] = Σ (circ_k / Σ circ) × S_outlet_k[i][t]
```
Use when you want larger-circulation outlets to carry more weight. Requires reliable circulation data, which is increasingly difficult to obtain for digital outlets.

**Option C — Factor score:**
Run a principal components analysis across outlet salience scores. The first component is your "media agenda factor." Use when you want to capture shared variance and suppress outlet idiosyncrasies.

**Most published agenda-setting studies use Option A.** Use Option B or C only if you have a theoretical reason to weight outlets differently, and document the decision.

---

## Validity Threats Specific to This Measurement Context

**1. Source agenda ≠ media agenda**
Wire service stories (AP, Reuters) appear in hundreds of outlets. Counting them once per outlet inflates their apparent salience. If your outlets heavily re-publish wire content, consider coding wire stories separately or deduplicate by story origin.

**2. Seasonality confounds**
Political issues spike during election cycles; economic issues spike during downturns. If your study period contains a structural break (election, crisis), control for it in your correlation analysis or limit the study window to avoid spanning the break.

**3. Issue definition drift**
"Immigration" as coded in 2005 may not capture the same phenomena as "immigration" in 2025. If studying long time periods, verify that your issue categories remain conceptually stable or document when and how you adjusted them.

**4. Online-print discrepancy**
Many publications now publish online-first content that never appears in print. Decide in advance whether your unit of analysis is the print edition, the website, or both — and stick to it. Mixed sampling creates incomparable placement scores.

---

## Checklist Before Running Correlation Analysis

- [ ] Codebook finalized before coding began (no post-hoc category additions)
- [ ] Inter-coder α ≥ 0.80 on `issue_primary`; ≥ 0.85 on `placement_code`
- [ ] Time series constructed with consistent time units
- [ ] Lag range specified before computing correlations
- [ ] Issue set covers ≥ 90% of stories in your sample (avoid a catch-all "other" category > 10%)
- [ ] Media salience scores are on the same scale across time units (normalize by total stories per period if outlet output volume changed substantially)
