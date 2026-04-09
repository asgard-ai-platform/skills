# Fact-Checking Tools & Databases

A curated reference for verifying claims, tracing sources, and detecting misinformation. Organized by use case.

---

## Quick Decision: Which Tool First?

```
Is this a factual claim about a real-world event or person?
├── Yes → Start with a general fact-checker (Snopes / PolitiFact / FactCheck.org)
│
Is this a scientific or health claim?
├── Yes → PubMed + Cochrane; check Retraction Watch for retracted papers
│
Is this a statistic or data point?
├── Yes → Trace to primary data source (government database, original study)
│
Is this an image or video?
├── Yes → Reverse image search (TinEye / Google Images) + InVID/WeVerify
│
Is this a news story?
├── Yes → AP Fact Check + Reuters Fact Check; check original source
│
Is this a Taiwanese/Chinese-language claim?
└── Yes → MyGoPen + Taiwan FactCheck Center + Cofacts
```

---

## General Fact-Checking Platforms

### International

| Platform | URL | Strength | Limitation |
|----------|-----|---------|-----------|
| Snopes | snopes.com | Deep investigation, long history | US-centric, slow on breaking news |
| PolitiFact | politifact.com | Structured verdict scale | US politics focus |
| FactCheck.org | factcheck.org | Annenberg-backed, non-partisan | US politics only |
| AFP Fact Check | factcheck.afp.com | Global, multilingual | Coverage uneven outside major regions |
| Reuters Fact Check | reuters.com/fact-check | Wire service speed, global reach | Shorter investigations |
| AP Fact Check | apnews.com/APFactCheck | High authority, wire credibility | Volume-limited |
| Full Fact | fullfact.org | UK-specific depth | UK-focused |

### Taiwan & Chinese-Language

| Platform | URL | Strength | Limitation |
|----------|-----|---------|-----------|
| MyGoPen 麥擱騙 | mygopen.com | Taiwanese LINE/FB rumors | Community-driven, variable depth |
| Taiwan FactCheck Center 台灣事實查核中心 | tfc-taiwan.org.tw | Professional, IFCN-certified | Slower turnaround |
| Cofacts 真的假的 | cofacts.tw | Crowdsourced; API available | Quality varies by contributor |
| Fake News Cleaner 假新聞清潔劑 | Line chatbot | Fast LINE integration | Chatbot only; no archive |

**IFCN Certification**: The International Fact-Checking Network (Poynter Institute) certifies platforms against a code of principles. Prefer IFCN-certified sources. Current certified list: poynter.org/ifcn/

---

## Image & Video Verification

### Reverse Image Search Workflow

**Goal**: Determine if an image is old, out-of-context, or fabricated.

**Step 1 — Upload or paste URL to:**
- Google Images (images.google.com → camera icon)
- TinEye (tineye.com) — finds oldest instance of image online
- Yandex Images — often finds images that Google misses, especially for Eastern European/Asian content

**Step 2 — Check the earliest date**: If an image claimed to show "yesterday's protest" first appeared online three years ago, it's being reused out of context.

**Step 3 — For video**: Use InVID / WeVerify browser plugin (invid-project.eu)
- Splits video into keyframes for reverse image search
- Checks metadata
- Works on YouTube, Twitter/X, Facebook

**Step 4 — Metadata check**: ExifTool (free CLI) extracts GPS coordinates, camera model, and timestamps embedded in JPEGs. A photo claimed to be from Location A but with GPS pointing to Location B is falsified.

```bash
# Check image metadata
exiftool suspicious_image.jpg | grep -E "GPS|Date|Camera|Location"
```

Note: Most social platforms strip EXIF on upload. Absence of metadata is not evidence of forgery — but presence is useful.

### AI-Generated Image Detection

These tools detect AI-generated images (accuracy varies; treat as one signal, not verdict):

| Tool | URL | Notes |
|------|-----|-------|
| Hive Moderation | hivemoderation.com/ai-generated-content | Commercial; free tier available |
| Illuminarty | illuminarty.ai | Free; works on uploaded images |
| AI or Not | aiornot.com | Simple UI; confidence score |

**Limitation**: Detection tools lag behind generation tools. A "human" verdict does not prove authenticity.

---

## Scientific & Medical Claims

### PubMed Search Strategy

For health/medical claims, the primary database is PubMed (pubmed.ncbi.nlm.nih.gov).

**Efficient query pattern:**
```
"[exact claim keyword]" AND (systematic review[pt] OR meta-analysis[pt])
```

Prioritize: systematic reviews > RCTs > cohort studies > case studies > expert opinion

**Check the journal**: Use SCImago Journal Rankings (scimagojr.com) to verify the journal is indexed and not predatory. A journal with no impact score and pay-to-publish model is a red flag.

### Retraction Watch

retractedpapers.science (or retractionwatch.com) — searchable database of retracted papers. AI tools frequently cite retracted papers without flagging them. Before using any academic paper as evidence:

1. Paste DOI or title into Retraction Watch
2. Check PubMed for "retraction notice" linked to the paper
3. Check the journal's own correction/retraction notices

### Cochrane Library

cochranelibrary.com — gold standard for systematic reviews of medical interventions. Free to access. If a health claim contradicts Cochrane consensus, the burden of proof is on the claim.

---

## Statistics & Data Verification

### Tracing a Statistic to Its Primary Source

A claim like "73% of Taiwanese teenagers experience online bullying" is meaningless without knowing:
- Who conducted the study
- Sample size and methodology
- When it was conducted
- How "online bullying" was defined

**Standard trace procedure:**

1. Search the exact number + keyword in Google (`"73%" Taiwan teenagers bullying`)
2. Find the news articles citing it — find which organization they attribute
3. Go directly to that organization's publications page
4. Locate the original report, not the press release
5. Read the methodology section

If step 3-5 fails (the study doesn't appear to exist), the statistic is fabricated or garbled beyond verification.

### Key Primary Data Sources (Taiwan & Global)

| Data type | Source |
|-----------|--------|
| Taiwan economic/demographic | 主計總處 dgbas.gov.tw |
| Taiwan health statistics | 衛福部統計處 mohw.gov.tw |
| Taiwan crime statistics | 內政部警政署 npa.gov.tw |
| Global economic | IMF Data (imf.org/en/Data), World Bank Open Data |
| Global health | WHO Global Health Observatory |
| US government data | data.gov |
| Trade statistics | UN Comtrade (comtrade.un.org) |

---

## Domain & Website Credibility Checks

### WHOIS Lookup

Verify domain registration date and registrant. A "news site" registered 3 weeks ago is a red flag.

- whois.domaintools.com
- who.is

### Media Bias / Outlet Rating

| Tool | URL | Notes |
|------|-----|-------|
| Media Bias/Fact Check | mediabiasfactcheck.com | US-centric; covers major global outlets; shows factual reporting score |
| AllSides | allsides.com | US political lean spectrum; less useful for Taiwan |

**Caution**: These ratings are assessments, not verdicts. A "left-leaning" outlet can publish accurate data. Use them to understand perspective, not to dismiss entirely.

### Wayback Machine

web.archive.org — check if a website's content has been quietly changed. Paste the URL to see snapshots over time. Useful when a source claims "we always reported it this way."

---

## Structured Verification Workflow

For a claim requiring thorough investigation, follow this sequence:

```
Step 1: Characterize the claim
  - What type? (event, statistic, quote, image, scientific claim)
  - Select appropriate tools from above

Step 2: Search fact-check databases first
  - Has this already been debunked or verified?
  - If yes: review the primary evidence cited in that fact-check, don't just cite the fact-check itself

Step 3: Trace to primary source
  - Find the original document, dataset, or statement
  - Verify it exists and says what it's claimed to say

Step 4: Cross-check with independent sources
  - At least 2 additional independent sources
  - "Independent" = different authors, different organizations, different methods
  - Wire services (AP, Reuters) reporting the same fact counts as corroboration
  - 10 outlets that all cite the same original AP story do not count as 10 sources

Step 5: Assess what remains uncertain
  - Record what you could not verify
  - Distinguish "not verified" from "disproven"
```

---

## Applying the Iron Law with Tools

> No Source Is Automatically Trustworthy — including fact-checkers themselves.

Fact-checking platforms can be:
- **Wrong**: They work at speed; corrections happen
- **Incomplete**: A "partly false" verdict on one version of a claim doesn't adjudicate all versions
- **Biased in selection**: Which claims get fact-checked reflects editorial priorities
- **Outdated**: A 2019 "true" verdict on an evolving situation may no longer hold

**Correct use of a fact-check result:**
- The fact-check is a secondary source. Treat it as one input.
- Follow its citations to the primary evidence.
- A claim is corroborated by the primary evidence it cites — not by the fact-checker's conclusion alone.

**Incorrect use:**
- "Snopes says it's false, so it's false." This is substituting one authority for your own analysis. Acceptable as a quick screen; not acceptable as a final verdict in serious research.

---

## Taiwan-Specific Misinformation Patterns

Understanding common vectors improves tool selection:

| Pattern | Common platform | Recommended tool |
|---------|----------------|-----------------|
| Line group health rumors | LINE | MyGoPen, Cofacts chatbot |
| Manipulated election/political images | Facebook, X | Reverse image + Taiwan FactCheck Center |
| Fabricated government announcements | LINE, Facebook | Official agency website primary check |
| Reused footage presented as current events | X, YouTube | InVID keyframe + TinEye |
| Fake statistics about Taiwan's economy | News sites, X | 主計總處 + IMF direct verification |
