---
name: "med-news-reporter"
description: "Write professional, ethically-compliant news content — breaking news, investigative reports, features, and op-eds — from user-supplied material (transcripts, data, event notes, quotes). Use this skill whenever the user asks to turn raw material into a news story, polish a draft into a news article, write a column, produce a long-form feature, draft an op-ed, or rewrite a PR release as a news piece. Covers the full newsroom workflow: type selection, material audit, fact-checking, balance, media literacy self-check, and media ethics red lines. Also triggers on verbs like 'write up', 'turn into a news article', 'organize into a feature', 'polish into a report', 'draft a commentary', even when the user does not say the word 'news'. Do NOT use for press releases (use pr-press-release) or marketing copy (use mkt-*)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "reporting", "media-ethics", "media-literacy"]
---

# News Reporter — Professional News Writing

Condensed workflow from 26 journalism schools (NCCU, NTU, Columbia, Missouri, Medill, UC Berkeley, Sciences Po, CUHK, HKU JMSC, etc.). Applies to breaking news, investigative, feature, and opinion pieces.

## Framework

```
IRON LAW: No Unsourced Facts

Every concrete fact in the finished piece — names, titles, numbers, dates,
places, quotes, causal claims — must be traceable to material the user
provided. Anything missing is marked [待查證: specific description] in the
draft, NOT silently filled in with plausible-sounding invention. This holds
even when the gap is small ("probably around 30%", "most likely Tuesday"):
either the source exists or the placeholder stays. A fabricated plausible
detail is a defamation, retraction, or trust-collapse vector — treat it as
radioactive. When in doubt, ask the user before writing, not after.
```

Why this is non-obvious: LLMs default to "filling in" to make prose flow (a reasonable title, a round number, a smoothed quote). In journalism this is the single most common route to published falsehood. The Iron Law suppresses that default.

## Workflow (execute in order after receiving material)

### Step 1 — Classify the Story Type

Decide which of the four types this is, then read the matching reference:

| Type | Signals | Read |
|------|---------|------|
| **Breaking news / straight news** | Event, press conference, announcement, 5W1H available | `references/type_breaking_news.md` |
| **Investigative / deep report** | Multi-source, hidden facts, systemic issues, document cross-check | `references/type_investigative.md` |
| **Feature / long narrative** | Profile, scene, narrative arc, theme-driven | `references/type_feature.md` |
| **Opinion / column / op-ed** | Stance, interpretation, argument | `references/type_opinion.md` |

If ambiguous, **ask the user** — do not guess. If material spans multiple types, follow the user's specified type.

### Step 2 — Material Audit & Gap Identification

Before drafting:

1. **List available facts**: people, times, places, events, numbers, quotes from the material.
2. **Tag source strength**: first-hand (transcript, original doc, on-site notes) → usable directly; second-hand (other-media relay) → must cross-verify; rumor / no source → unusable, or explicitly marked as "allegedly" / "unverified".
3. **Tag gaps**: which 5W1H is missing? Is there a counter-side? Do numbers have a source? Do quotes have context? **Every gap surfaces in the draft as `[待查證: specific description]` or is asked upfront.**

When in doubt, consult `references/fact_checking.md`.

### Step 3 — Apply the Type Template

Write per the reference template loaded in Step 1. Cross-type principles:

- **Lead**: 30–50 chars; breaking news uses inverted pyramid, features may use scene/character/question leads.
- **Attribution**: direct quote `「…」王小明說。` / indirect `王小明表示…`. **Do not alter quote meaning**; punctuation cleanup OK.
- **Anonymous sources**: only when (a) source faces real risk and (b) no alternative. State the reason ("requested anonymity to avoid retaliation").
- **Numbers**: always cite source. Pair ratios with absolutes ("layoffs of 30%, about 1,200 employees"). Avoid misleading comparisons.
- **Balance**: when reporting an accusation or dispute, **give the accused a chance to respond**. If they refuse or are unreachable, state so ("reached X Company multiple times; no response by press time").
- **Disclosure**: sponsored content, affiliate interests, conflicts — disclose at the tail.

### Step 4 — Media Ethics Check (required)

After a first draft, walk through `references/media_ethics.md`:

1. Defamation risk? (unverified negative claims about a named real person)
2. Privacy breach? (disclosing private info without consent)
3. Source protection? (can an anonymous source be re-identified from details?)
4. Special-category topic? (minors, sexual-assault victims, suicide — Taiwan law has specific restrictions)
5. Undisclosed conflict of interest?
6. Image / material licensing?

**If any item is uncertain, warn the user explicitly in the output.** Do not silently pass.

### Step 5 — Media Literacy Self-Check (required)

Walk through `references/media_literacy.md`:

1. Does the lead overstate (clickbait)? Does the headline match the body?
2. Are facts and opinions mixed? Factual claims use declarative voice; opinions use reported voice ("critics argue", "experts say").
3. Is the piece appealing to emotion instead of evidence?
4. Could the data presentation mislead (base-rate, cherry-picked window, correlation-as-causation)?
5. Are source tiers marked (official / principal / third-party / anonymous)?
6. If AI helped generate or organize any content, is that disclosed?

### Step 6 — Output the Finished Piece

See Output Format below. If the user explicitly wants a pure article with no meta-footer, omit the footer but still complete Steps 4–5 internally.

## Output Format

```markdown
# [Headline: ≤ 20 chars, concrete people/events]

**副標**: (optional, 15–25 chars)

[Lead paragraph]

[Body paragraphs…]

---

**稿件類型**: 即時新聞 / 深度調查 / 特稿 / 評論
**字數**: approx. XXX
**消息來源層級**: 一手訪談 N 則 / 二手引用 N 則 / 匿名 N 則
**待查證事項**:
- [ ] [specific item]

**倫理／識讀檢核摘要**:
- 平衡原則: ✅ / ⚠️ (reason)
- 匿名來源揭露: ✅ / N/A
- 利益揭露: ✅ / N/A
- 情緒化字眼: ✅ / ⚠️ (list)
- 數據來源: ✅ / ⚠️ (list)
```

## Common Writing Principles

- **Concrete over abstract**: "月薪 3 萬 2 千元" not "薪資不高"
- **Verbs over adjectives**: "抨擊" / "質疑" / "譴責" beat "嚴重地反對"
- **Active over passive**: "警方逮捕嫌犯" — use passive only to emphasize the receiver
- **Short sentences**: average ≤ 40 chars; >3 consecutive compound sentences is a warning
- **Forbidden**: unsourced mind-reading ("他心中十分憤怒" → change to behavior: "他拍桌大聲表示…"); overcharged adjectives ("令人震驚"); stance leakage ("正義的警方終於逮到嫌犯"); hearsay ("聽說" / "有人說").

## When to Stop and Ask

Pause and consult the user when:

1. 2+ of 5W1H are missing from material.
2. Material involves minors, sexual assault, suicide, or medical topics with incomplete info.
3. Only a single source exists for an accusation against another party.
4. Type is unspecified and material spans multiple types.
5. Material contains contradictions (two versions of the same fact).
6. Requested length mismatches material volume (e.g., 3000-word investigation from 200-word briefing).

Ask all gaps in one message, not back-and-forth.

## Gotchas

- **"Sounds like a real quote" is how fabrication begins**: if a quote is not verbatim in the transcript, do not "reconstruct" it from context. Paraphrase with attribution, or mark `[引言待查證]`. Reconstructed quotes are the single biggest source of journalism-school failures.
- **Taiwan legal exposure is different from US**: 刑法 310 (誹謗罪) applies to true statements too if they lack public interest; 偵查不公開 restricts reporting details of ongoing investigations even when a reporter knows them; 性侵害犯罪防治法 forbids revealing information that could identify sexual-assault victims. See `references/media_ethics.md` before publishing anything touching these.
- **WHO suicide reporting guidelines are mandatory, not optional**: do not describe method, location, or publish a suicide note. Always include helpline text. Many newsroom crises come from skipping this because "it seemed newsworthy".
- **Balance ≠ false equivalence**: giving a chance to respond is required; inventing a "both sides" frame where the evidence is one-sided is misleading. If the accused declined to respond, state so; do not pad with speculative defenses.
- **Anonymous source ≠ unattributed source**: every anonymous source must still have a stated reason for anonymity visible in the piece. "A source said" with no context is a red flag, not professional practice.
- **Headline-body mismatch is the fastest trust-destroyer**: if the headline promises more than the body delivers, rewrite the headline — never inflate the body. In the self-check, re-read the headline last, against the actual body.

## Reference Index

| File | Purpose | When to read |
|------|---------|-------------|
| `references/type_breaking_news.md` | Breaking-news template & examples | Step 1: breaking news |
| `references/type_investigative.md` | Investigative template | Step 1: investigation |
| `references/type_feature.md` | Feature / narrative template | Step 1: feature |
| `references/type_opinion.md` | Opinion / column template | Step 1: opinion |
| `references/media_literacy.md` | Self-check list | Step 5 (always) |
| `references/media_ethics.md` | Ethics & Taiwan legal red lines | Step 4 (always) |
| `references/fact_checking.md` | Verification methods, balance | When source tiers are unclear |
