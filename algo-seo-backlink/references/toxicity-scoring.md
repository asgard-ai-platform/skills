# Toxicity Scoring Methodology

Toxicity scoring assigns a numerical risk score to each referring domain so you can prioritize disavow candidates objectively. The goal is to separate "weak but harmless" links from "actively harmful" links — disavowing the former wastes authority; ignoring the latter invites manual penalties.

---

## Scoring Model

Each referring domain receives a **Toxicity Score (TS)** from 0–100 computed from four signal groups. Higher score = more toxic.

```
TS = w_auth × S_auth + w_rel × S_rel + w_pattern × S_pattern + w_anchor × S_anchor
```

Default weights (sum to 1.0):

| Signal Group | Variable | Weight |
|---|---|---|
| Authority inversion | S_auth | 0.30 |
| Topical irrelevance | S_rel | 0.25 |
| Link pattern signals | S_pattern | 0.30 |
| Anchor text risk | S_anchor | 0.15 |

Weights are tunable. If you have a history of PBN attacks, raise `w_pattern`. If you're in a niche where off-topic links are common (e.g., press releases), lower `w_rel`.

---

## Signal Group Definitions

### S_auth — Authority Inversion Score (0–100)

A low-authority domain linking to a high-authority target is suspicious; the direction should normally be opposite.

```
S_auth = max(0, 100 − DR_linking) if DR_linking < 15
       = max(0, 30 − DR_linking)  if 15 ≤ DR_linking < 30
       = 0                         if DR_linking ≥ 30
```

Practical table:

| DR of linking domain | S_auth |
|---|---|
| 0–4 | 96–100 |
| 5–9 | 91–95 |
| 10–14 | 86–90 |
| 15–19 | 11–15 |
| 20–29 | 1–10 |
| 30+ | 0 |

**Note:** DR 0–4 sites that have existed < 30 days get a flat `S_auth = 100` regardless.

---

### S_rel — Topical Irrelevance Score (0–100)

Relevance is estimated from topic overlap between the linking page and the target site's category. Use the linking page's category tag from Ahrefs/Moz, or run a simple keyword cosine similarity if you have crawl access.

**Rule-based proxy** (when you lack ML-based topic classification):

1. Pull the top-3 topic categories of your target domain (e.g., "E-commerce > Electronics")
2. Pull the Ahrefs-reported category for the linking domain
3. Apply this scoring table:

| Overlap level | Definition | S_rel |
|---|---|---|
| Exact match | Same L2 category | 0 |
| Adjacent | Same L1, different L2 (e.g., both "E-commerce" but different sub) | 20 |
| Distant | Different L1 but plausible (e.g., "Tech" → "Electronics") | 50 |
| Unrelated | No thematic overlap (e.g., casino → software) | 80 |
| Adversarial | Adult/gambling/pharma → non-adult target | 100 |

Foreign-language mismatch that also has unrelated topic: add +15 (cap at 100).

---

### S_pattern — Link Pattern Score (0–100)

This signal group uses boolean indicators, each contributing a fixed score. Scores stack and are capped at 100.

| Pattern | Detection method | Score |
|---|---|---|
| Footer/sitewide link | Same anchor text on 100+ pages of same domain | +40 |
| PBN indicator | Ahrefs: referring domain has 0 organic traffic + DR < 20 + same IP C-block as ≥ 3 other linking domains | +50 |
| Link farm | Page linking to you also links to 50+ unrelated root domains on same page | +45 |
| Paid link signal | Anchor is exact-match keyword + linking page is clearly advertorial without disclosure | +30 |
| Age manipulation | Domain registered < 6 months ago with 50+ outbound links | +25 |
| Redirect chain | Link passes through ≥ 2 hops before reaching target | +10 |
| Reciprocal link | You also link back to this domain from a non-editorial context | +15 |

**PBN C-block check** (quick shell method):
```bash
# Get /24 block from IP
dig +short example.com | awk -F. '{print $1"."$2"."$3}'
# Compare across all suspicious domains in your export
```

---

### S_anchor — Anchor Text Risk Score (0–100)

Anchor text alone is rarely sufficient to trigger toxicity, but it amplifies risk from other signals.

```
S_anchor = base_anchor_risk × amplifier
```

**Base anchor risk:**

| Anchor type | S_anchor base |
|---|---|
| Branded (your exact brand name) | 0 |
| Naked URL | 5 |
| Generic ("click here", "website") | 10 |
| Partial-match keyword | 30 |
| Exact-match keyword | 55 |
| Exact-match + location ("buy widgets NYC") | 70 |
| Unrelated or spun text | 65 |

**Amplifier** (multiplicative, 1.0–1.5):
- Apply 1.3× if the same anchor is used on every page of the linking domain (sitewide)
- Apply 1.5× if anchor contains money keywords in a niche known for spam (CBD, casino, forex, pharma)
- Default amplifier: 1.0

Cap result at 100.

---

## Composite Score Interpretation

```
TS_final = 0.30 × S_auth + 0.25 × S_rel + 0.30 × S_pattern + 0.15 × S_anchor
```

| TS_final | Classification | Recommended action |
|---|---|---|
| 0–19 | Clean | No action |
| 20–39 | Weak | Monitor; no disavow |
| 40–59 | Suspicious | Manual review required |
| 60–79 | Likely toxic | Add to disavow candidate list |
| 80–100 | Confirmed toxic | Disavow immediately |

---

## Worked Example

**Scenario:** A domain `cheapmeds-discounts.ru` links to an e-commerce electronics site.

**Step 1 — S_auth**
DR = 3 → `S_auth = 97`

**Step 2 — S_rel**
Linking domain category: Pharma/Health. Target site: Electronics E-commerce.
Overlap: Adversarial (pharma → non-pharma) → `S_rel = 100`

**Step 3 — S_pattern**
- Footer/sitewide? Yes (same anchor on 200+ pages): +40
- PBN? 0 organic traffic + DR 3 + shares C-block with 4 other linking domains: +50
- Subtotal before cap: 90 → `S_pattern = 90`

**Step 4 — S_anchor**
Anchor: "cheap cialis online" → exact-match + pharma niche amplifier
Base: 70 (exact-match + location-style) × 1.5 = 105 → capped at 100 → `S_anchor = 100`

**Composite:**
```
TS = 0.30×97 + 0.25×100 + 0.30×90 + 0.15×100
   = 29.1 + 25.0 + 27.0 + 15.0
   = 96.1 → Confirmed toxic → Disavow immediately
```

---

## Batch Scoring Procedure

When processing a full backlink export (typical: hundreds to thousands of domains):

1. **Deduplicate first.** Collapse all links from the same root domain into one row. Use the highest-authority page on that domain as the representative link.

2. **Auto-score using rules.** Apply the four signal groups programmatically. Most tools export enough data to compute S_auth (DR), S_rel (category), and S_anchor (anchor text). S_pattern requires cross-domain analysis.

3. **Triage by bucket:**
   - TS ≥ 80: auto-add to disavow file
   - TS 60–79: export to manual review spreadsheet
   - TS < 60: no action

4. **Manual review of the 60–79 bucket.** For each: open the linking page, check for editorial context, confirm pattern signals. Override up or down as needed.

5. **Never disavow the 40–59 range** without a strong editorial reason. These are usually old, low-quality directories or scrapers — mostly harmless.

---

## Disavow File Format

Google's disavow tool accepts domain-level and URL-level entries:

```
# Generated 2025-01-15 | Batch: 2025-Q1 audit
# TS ≥ 80: confirmed toxic
domain:cheapmeds-discounts.ru
domain:casino-backlinks-4u.net
domain:seo-links-farm-xyz.com

# TS 60–79: reviewed manually, confirmed
domain:irrelevant-directory-1998.info
```

**Rules:**
- Use `domain:` prefix to disavow all links from a root domain; use full URLs only when you want to preserve other links from the same domain (rare)
- One entry per line; `#` comments allowed
- Filename must be `.txt`, UTF-8 encoded
- Submit via Google Search Console → Links → Disavow

---

## Common False Positives

These patterns look toxic but usually aren't:

| Pattern | Why it looks toxic | Why it isn't |
|---|---|---|
| High-DA news site, exact-match anchor | S_anchor elevated | News sites editorially choose anchors; trust the editorial context |
| Old directory (DR 5, created 2003) | Low DR | Directories from pre-2010 often have historic trust Google discounts but doesn't penalize |
| Foreign-language domain, irrelevant topic | S_rel = 80 | If it's a legitimate import/export partner mention, relevance scoring fails |
| Competitor's site linking to yours | Pattern signals unclear | Competitor links are rarely manufactured; usually accidental or comparative |

When manual review reveals a false positive, override the classification and document the reason. Keep a suppression list to avoid re-flagging the same domains in future audits.

---

## Limitations of This Model

- **DA/DR are estimates.** Moz DA and Ahrefs DR disagree on 20–30% of domains. A domain scoring DR 12 in Ahrefs might be DA 35 in Moz. Use the tool you're most familiar with consistently across an audit, not a mix.
- **Google does not publish a toxicity API.** This model approximates Google's spam signals based on observed penalty patterns and Search Quality Evaluator Guidelines. It is not derived from Google's actual classifier.
- **Manual penalties ≠ algorithmic filtering.** Google's SpamBrain may already be ignoring a link algorithmically; a manual action is a separate, human-reviewed process. If you have no manual action in Search Console, your toxic links may already be discounted.
- **Disavow is irreversible in the short term.** Once submitted, a disavow file takes weeks to process and Google does not "un-process" it immediately if you remove entries. Err toward caution.
