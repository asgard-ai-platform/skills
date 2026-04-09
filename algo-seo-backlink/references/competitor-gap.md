# Competitor Backlink Gap Analysis

Backlink gap analysis finds referring domains that link to one or more competitors but **not** to your site. The output is a prioritized list of link acquisition targets — domains where you have a plausible case for earning a link because they already link to similar content.

---

## Core Concept: Gap Score

For each referring domain found in competitor profiles, compute a **Gap Score** to rank acquisition priority:

```
Gap Score = DR × Relevance × Exclusivity_Bonus × (1 - Difficulty)
```

| Variable | Range | Definition |
|---|---|---|
| `DR` | 0–100 | Ahrefs Domain Rating (or Moz DA) of the linking domain |
| `Relevance` | 0.0–1.0 | Topical match between linking domain and your site |
| `Exclusivity_Bonus` | 1.0–1.5 | Multiplier for domains that link to fewer competitors |
| `Difficulty` | 0.0–1.0 | Estimated effort to acquire the link |

**Exclusivity Bonus table:**

| Competitors linked | Bonus |
|---|---|
| 1 of your 3 competitors | 1.5 |
| 2 of your 3 competitors | 1.2 |
| 3 of your 3 competitors | 1.0 |

Rationale: a domain that links to only one competitor is a niche source — harder to scale, but if you land it, you close a moat. A domain that links to all three is already pattern-matching your category; easier to approach with a similar pitch.

---

## Step-by-Step Procedure

### Step 1: Export competitor backlink profiles

Pull referring domain lists (not individual URLs) from Ahrefs or Moz for:
- Your site: `site_A`
- Competitor 1: `site_B`
- Competitor 2: `site_C`
- Competitor 3: `site_D`

**Required fields per domain:**
```
referring_domain | DR | linking_to_pages | anchor_sample | dofollow_count
```

Deduplicate at the domain level. One entry per referring domain regardless of how many individual backlinks it sends.

### Step 2: Compute the union and difference sets

```python
# Pseudocode
all_competitor_domains = B_domains | C_domains | D_domains
gap_domains = all_competitor_domains - A_domains
```

`gap_domains` is your raw target universe. This is typically 200–2000 domains depending on competitor profile size.

### Step 3: Assign relevance scores

Relevance cannot be automated fully. Use a two-pass approach:

**Pass 1 — Automated category filter:**
Classify each gap domain by its primary topic using its homepage content or a lookup table. Assign `Relevance = 0` if the domain is off-category (e.g., a gambling site linking to a competitor's press release).

| Domain category match | Relevance score |
|---|---|
| Same niche, editorial content | 0.9 |
| Adjacent niche, topical overlap | 0.6 |
| General news / media | 0.4 |
| Unrelated but high DR | 0.2 |
| Clearly off-topic | 0.0 |

**Pass 2 — Manual review for top 50 candidates** after scoring. Override automated classification when needed.

### Step 4: Assign difficulty scores

Difficulty is estimated from link type patterns and domain characteristics:

| Signal | Difficulty adjustment |
|---|---|
| Competitor link is editorial (in-content) | +0.3 |
| Domain has a "write for us" page | −0.3 |
| Domain links to 10+ external sites in your niche | −0.2 |
| Domain only links outward to brands with 10k+ followers | +0.4 |
| Link appears to be paid/sponsored | +0.5 (avoid) |

Cap difficulty at 0.9. If difficulty ≥ 0.85, deprioritize unless DR > 80.

### Step 5: Score and rank

Apply the Gap Score formula. Sort descending. Work the top 30–50 as your active outreach pipeline.

---

## Worked Example

**Scenario:** E-commerce site selling ergonomic office chairs (site A). Three competitors: B, C, D.

**Raw export (excerpt, gap domains only):**

| Domain | DR | Links to | Dofollow |
|---|---|---|---|
| workplacewellness.org | 62 | B, C | yes |
| officehacks.net | 44 | B only | yes |
| remoteworkreview.com | 71 | B, C, D | yes |
| dealstoday.io | 28 | C only | yes |
| ergonomics-journal.com | 55 | B, C | yes |

**Scoring:**

`workplacewellness.org`
- DR = 62
- Relevance = 0.9 (ergonomics/wellness blog)
- Exclusivity Bonus = 1.2 (links to 2 of 3 competitors)
- Difficulty = 0.35 (has guest post page, links broadly)
- **Gap Score = 62 × 0.9 × 1.2 × (1 − 0.35) = 62 × 0.9 × 1.2 × 0.65 = 43.5**

`officehacks.net`
- DR = 44
- Relevance = 0.6 (general office productivity, adjacent)
- Exclusivity Bonus = 1.5 (only links to 1 competitor)
- Difficulty = 0.4
- **Gap Score = 44 × 0.6 × 1.5 × 0.60 = 23.8**

`remoteworkreview.com`
- DR = 71
- Relevance = 0.9
- Exclusivity Bonus = 1.0 (links to all 3)
- Difficulty = 0.3
- **Gap Score = 71 × 0.9 × 1.0 × 0.70 = 44.7**

`dealstoday.io`
- DR = 28
- Relevance = 0.2 (deals aggregator, irrelevant)
- Exclusivity Bonus = 1.5
- Difficulty = 0.2
- **Gap Score = 28 × 0.2 × 1.5 × 0.80 = 6.7**

`ergonomics-journal.com`
- DR = 55
- Relevance = 0.9
- Exclusivity Bonus = 1.2
- Difficulty = 0.6 (academic-style site, low outreach response rate)
- **Gap Score = 55 × 0.9 × 1.2 × 0.40 = 23.8**

**Ranked output:**

| Rank | Domain | Gap Score | Action |
|---|---|---|---|
| 1 | remoteworkreview.com | 44.7 | Outreach: chair review feature |
| 2 | workplacewellness.org | 43.5 | Guest post pitch |
| 3 | officehacks.net | 23.8 | Resource link pitch |
| 3 | ergonomics-journal.com | 23.8 | Data study / citation |
| 5 | dealstoday.io | 6.7 | Skip |

---

## Link Type Determines Pitch Strategy

The reason a competitor earned a link tells you what angle to use:

| Link type found on gap domain | Likely reason competitor got it | Your pitch |
|---|---|---|
| In-content editorial mention | Competitor was cited as a resource or example | Produce competing or complementary resource; pitch as "alternative" |
| Roundup / "best of" list | Competitor was included in a curated list | Ask to be added; provide brief differentiator |
| Guest post byline | Competitor contributed content | Pitch your own guest post on adjacent topic |
| Product review | Competitor provided product for review | Offer product sample or PR contact |
| Interview / quote | Competitor was quoted as an expert | Position yourself as additional expert source |
| News mention | Competitor did something newsworthy | Requires a different strategy (PR, not link building) |

You can infer link type from: URL path of the linking page, anchor text, surrounding page text, page title.

---

## Prioritization Beyond Gap Score

Gap Score ranks quality × effort. Layer two additional filters before finalizing your outreach list:

**Filter 1 — Cluster by link type**
Group your top 30 domains by the pitch type they require (roundup vs. guest post vs. resource). Cluster outreach to avoid context-switching. Running 10 roundup pitches in parallel is more efficient than alternating pitch types.

**Filter 2 — Linking page traffic**
A DR 50 domain with one referring page that gets zero organic traffic passes zero referral traffic even if the link counts for authority. Use Ahrefs' "Top Pages" filter or check the linking URL directly. Deprioritize high-DR domains where the specific linking page has UR < 10 and no organic traffic.

---

## What Gap Analysis Cannot Tell You

- **Why** the competitor earned the link. A competitor may have gotten a link from a journalist who covered them specifically — that link is not replicable by outreach.
- **Whether** the gap domain will respond. Response rates for cold link outreach average 5–15%. Use gap score to prioritize, not to guarantee conversion.
- **Link quality degradation over time.** A domain's DR when you export it is a snapshot. Domains decay. Re-run gap analysis every quarter.

---

## Anti-Patterns

**Chasing all-competitor domains only.** Domains that link to all three competitors are the easiest to justify approaching, but they are also the most saturated. Mix in exclusivity-1 domains (bonus 1.5) even if their individual Gap Score is moderate.

**Ignoring anchor text on the gap domain.** If the gap domain links to your competitor with exact-match "ergonomic office chairs," approach cautiously. Over-indexed exact-match anchors in your profile are a spam signal (per parent SKILL.md Gotchas). Request branded or URL anchor when you earn the link.

**Treating gap analysis as a one-time task.** Competitors earn and lose links continuously. A gap that didn't exist three months ago may now be your highest-priority target.

**Using individual backlink URLs instead of domains.** Analyzing 50,000 individual URLs produces noise. The referring domain is the unit of analysis. One domain sending 200 links is one outreach target, not 200.
