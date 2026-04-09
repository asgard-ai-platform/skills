# Media Database & Pitch Tracking

## Journalist Database Structure

A media database is a living CRM. Each record must capture enough to personalize a pitch; generic contact lists fail because journalists remember irrelevant pitches and filter future ones.

### Minimum Fields Per Record

| Field | Why It Matters |
|-------|---------------|
| `name` | First name for email salutation |
| `outlet` | Publication / broadcast org |
| `beat` | Specific topic(s) they cover — NOT just "tech" but "fintech, SaaS, startup funding" |
| `format_pref` | Email / LINE / Twitter DM / phone |
| `language` | 中文 / English / bilingual |
| `timezone` | Matters for send timing |
| `last_contact` | Date of last outreach |
| `last_response` | Date of last reply |
| `stories_written` | Count of stories they've written based on your pitches |
| `notes` | Free text: their quirks, what they've said, recent pieces you've read |

### Tiering System

Tier every journalist before pitching. Re-tier quarterly.

```
Tier 1 — Relationship journalists
  Criteria: Has written about you OR your competitors at least 2×
            AND responded to at least one direct pitch
  Action: Personal email, offer exclusives first, follow on social

Tier 2 — Targeted cold contacts
  Criteria: Covers your beat closely but no prior relationship
  Action: Personalized cold pitch referencing their recent work

Tier 3 — Distribution blast
  Criteria: Beat adjacent; may cover if perfectly timed
  Action: Wire service or bulk send only; no personal effort

Never pitch: Outside beat, left the outlet, or explicitly asked to be removed
```

## Taiwan Media Landscape

### Print / Digital Outlets by Beat

| Outlet | Beat Focus | Language | Pitch Channel |
|--------|-----------|----------|---------------|
| 經濟日報 | Business, finance, macro | 中文 | Email + LINE |
| 工商時報 | Industry, manufacturing, finance | 中文 | Email |
| 數位時代 | Tech startups, digital transformation | 中文 | Email + Twitter |
| TechOrange | Startup ecosystem, product launches | 中文 | Email |
| Inside | Startup ecosystem, VC rounds | 中文 | Email |
| Meet創業智庫 | Entrepreneurship, SME | 中文 | Email + LINE |
| CommonWealth Magazine (天下) | Long-form business/economy | 中文 | Email (lead time: 3–4 weeks) |
| Business Today (今周刊) | Finance, wealth, macro | 中文 | Email (lead time: 2 weeks) |
| Reuters Taiwan | Major business/politics, English-language global pickup | English/中文 | Email |
| Bloomberg Taiwan bureau | Public companies, M&A, macro | English | Email only |
| Nikkei Asia (Taipei bureau) | Regional business, tech supply chain | English | Email |

### Wire Services Active in Taiwan

| Service | Use Case | Cost Range |
|---------|----------|------------|
| 中央通訊社 (CNA) | 中文 domestic distribution; feeds major newsrooms | $5,000–15,000 NTD per release |
| PR Newswire Asia | English + Chinese, SEO, international pickup | $800–2,500 USD per release |
| BusinessWire | English, US investor audience, cross-Pacific | $1,000–3,000 USD per release |
| Accesswire | Budget alternative, English | $250–500 USD per release |

CNA is the highest-leverage Taiwan-specific wire: most local newsrooms monitor it, and a CNA pickup creates secondary coverage elsewhere with no additional pitch effort.

### LINE as a Pitch Channel

Unlike email, LINE messages have near-100% open rates with Taiwan journalists. Rules for using it:

1. **Only after established contact** — do not cold-pitch via LINE
2. **3 sentences max** — link to full release or attach PDF
3. **Send during business hours** — 9 AM–6 PM; LINE messages at 11 PM are remembered negatively
4. **Message template**:

```
[姓名] 你好，[公司名] 今天發布 [一句話描述新聞]。
附上新聞稿，如有需要可安排採訪 [受訪者職稱]。謝謝！
[你的名字]
```

## Building a Database from Scratch

If you have zero contacts, use this sequence:

**Week 1: Competitive intelligence**
- Find the last 5 press releases from direct competitors
- Google each headline; find which journalists covered it
- Add each to database with outlet + beat + their article URL in `notes`

**Week 2: Beat mapping**
- Pick 3 keywords that define your announcement (e.g., "AI fintech Taiwan")
- Search Google News, filter past 6 months
- Add every bylined journalist who wrote a relevant piece

**Week 3: Outlet scanning**
- Visit masthead/team pages of top-tier outlets
- Cross-reference their recent bylines against your beat keywords
- Only add journalists with ≥ 2 relevant recent articles

**Result**: A database of 30–60 qualified contacts is more valuable than a purchased list of 5,000.

### Do Not Buy Generic Lists

Purchased media lists (e.g., Cision bulk export) have two failure modes:
- Stale data: journalists change beats frequently; 20–30% of records are wrong within 12 months
- No context: you cannot personalize without knowing what they've written

Use purchased lists only to cross-reference and fill gaps, not as primary source.

## Pitch Tracking Log

Every outreach needs a timestamped record. Minimum columns for a pitch log spreadsheet:

```
date_sent | journalist | outlet | subject_line | tier | channel | 
follow_up_date | status | outcome | notes
```

Status values (keep these standardized):
- `sent` — delivered, no reply
- `opened` — email opened (if using tracking), no reply
- `replied` — any reply received
- `interested` — requested more info or interview
- `covered` — published a story
- `passed` — declined, reason noted
- `no_send` — in database but excluded from this campaign

### Follow-Up Cadence

```
Day 0: Send pitch
Day 3–4: One follow-up if no reply (email only, not LINE)
Day 7: Mark as "sent/no response" — stop following up

Exception: If a journalist replied "maybe later" or "send when X happens",
flag for a future date and re-engage then. Never follow up more than twice
on the same release.
```

Follow-up email template:

```
Subject: Re: [original subject]

Hi [Name],

Quick follow-up on my note from [Day]. [One sentence reminder of the news hook.]

Happy to share additional data or arrange a 15-min call with [spokesperson].

[Your name]
```

## Scoring a Journalist for Fit

Before adding to a pitch list, run a quick 5-point score:

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Beat match | Unrelated | Adjacent | Direct match |
| Recent activity | No byline in 6mo | 1–2 articles | 3+ articles |
| Prior coverage | Never covered your space | Covered competitors | Covered you directly |
| Outlet tier | Tier 3 / low reach | Mid-tier | Top-tier / Tier 1 |
| Language fit | Release lang mismatch | Bilingual | Exact match |

**Score 7–10**: Tier 1 or 2 — personalized pitch  
**Score 4–6**: Tier 3 — wire/bulk only  
**Score < 4**: Do not pitch this release

## Maintenance Schedule

| Cadence | Action |
|---------|--------|
| After every pitch campaign | Update `last_contact`, `status`, `outcome` for all records |
| Monthly | Verify Tier 1 contacts still cover the same beat (scan their recent bylines) |
| Quarterly | Re-tier all journalists; remove records with no engagement in 12 months |
| After any coverage | Tag `stories_written++`, add article URL to `notes`, move to Tier 1 if not already |

## Tracking Coverage ROI

After a campaign closes (typically 2 weeks post-send), calculate:

```
Pitch-to-coverage rate = stories_covered / pitches_sent × 100%

Industry baseline:
  Cold blast:          1–3%
  Targeted Tier 2:     5–15%
  Tier 1 relationship: 20–50%

Cost per placement (wire campaigns):
  CPP = total_wire_cost / stories_covered
  
  Example: NT$10,000 CNA release → 4 downstream stories = NT$2,500 CPP
```

Track CPP over time to decide whether wire spend is justified versus direct pitch effort.

## Red Flags When Using AI to Draft Pitches

Journalists read hundreds of pitches. Patterns that trigger immediate delete:

- Opening with "I hope this email finds you well"
- Describing your product as "revolutionary", "game-changing", or "disruptive" without data
- CC'ing multiple journalists in a visible To/CC field (shows mass blast)
- Subject line: "Press Release:" — this is a filter keyword for deletion
- Sending from a generic `pr@company.com` address with no named sender

Use a named sender address (`jane.chen@company.com`) and a subject line written as a news headline, not a label.
