---
name: "med-news-reporter"
description: "Use when the user wants to turn raw material — transcripts, interviews, event notes, data, direct quotes — into a publishable news piece (breaking news, investigative report, feature, or op-ed). Activates the full newsroom workflow: type selection, material audit, fact-checking, balance, media-ethics red lines, and media-literacy self-check. Also triggers on phrases like 'write up this transcript', 'turn into a news article', 'organize into a feature', 'polish into a report', 'draft an op-ed', '幫我寫成新聞稿', '潤成一篇報導', '整理成專訪', '寫一篇關於 X 的評論', '把逐字稿做成 feature' — even when the user does not say the word 'news'. Do NOT use for press releases (use pr-press-release) or marketing copy (use mkt-*)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "reporting", "media-ethics", "media-literacy"]
---

# News Reporter — Professional News Writing

## Overview

Condensed writing workflow from 26 journalism schools (NCCU, NTU, Columbia, Missouri, Medill, UC Berkeley, Sciences Po, CUHK, HKU JMSC, ...). Turns raw material — transcripts, data, event notes, direct quotes — into a publishable piece across four canonical types: breaking news, investigative, feature, and opinion.

```
IRON LAW: No Unsourced Facts

Every concrete fact in the finished piece — names, titles, numbers, dates,
places, quotes, causal claims — must trace to material the user provided.
Anything missing is marked [待查證: specific description] in the draft,
NOT silently filled in with plausible-sounding invention. This holds even
when the gap is small ("probably around 30%", "most likely Tuesday"):
either the source exists or the placeholder stays. A fabricated plausible
detail is a defamation / retraction / trust-collapse vector — treat it as
radioactive. When in doubt, ask the user before writing, not after.
```

Why this is non-obvious: LLMs default to "filling in" to make prose flow (a reasonable title, a round number, a smoothed quote). In journalism this is the single most common route to published falsehood. The Iron Law suppresses that default.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "The user said 'around 400', I'll round up to 500 for cleaner prose" | Any invented precision is fabrication. Use the supplied figure or [待查證]. |
| "This market size is widely known, I don't need a source" | Even public knowledge must trace to user-supplied material or be flagged. |
| "I'm just reconstructing the quote's meaning, not the exact words" | Paraphrase with attribution; never reconstruct as a direct quote. |
| "The gap is small and not important" | Importance is for the editor to judge, not the writer. Placeholder stays. |
| "Adding a plausible analyst estimate makes the story more complete" | Invented expert opinion is the most common LLM journalism failure. No. |

---

## When to Use

**Trigger conditions:**
- User supplies raw material (transcripts, interviews, event notes, data, press releases, logs) and asks for it to become a news-like piece.
- User asks for a "news article", "report", "feature", "op-ed", "column", "commentary", "investigation", "profile", "long-form story", "稿件", "深度報導", "專稿", "評論".
- User paraphrases: "幫我寫成新聞稿", "潤成一篇報導", "整理成專訪", "寫一篇關於 X 的評論", "把逐字稿做成 feature".
- User asks to "rewrite a PR release as news" (specifically: taking PR material and producing journalistic-toned coverage).

**Input signals:**
- Presence of named people, organizations, times, places, numbers, or direct quotations — i.e., material that could appear in a real news article.
- Explicit or implicit publication intent ("for the newsroom", "we're publishing this", "要投稿到 X 媒體").
- Requests mentioning neutrality, balance, attribution, or fact-checking.

**When NOT to use:**
- Press release or announcement from the subject company's own voice → use `pr-press-release`.
- Marketing copy, ad creative, landing-page copy → use `mkt-*`.
- Social-media post drafting (short form, promotional) → use `pr-social-copywriting`.
- Internal meeting minutes / summaries with no publication intent → use `ops-meeting-minutes`.

---

## Methodology

### Step 1: Classify the Story Type

Pick one of the four types, then read the matching reference:

| Type | Signals | Read |
|------|---------|------|
| **Breaking news / straight news** | Event, press conference, announcement, 5W1H available | `references/type_breaking_news.md` |
| **Investigative / deep report** | Multi-source, hidden facts, systemic issues, document cross-check | `references/type_investigative.md` |
| **Feature / long narrative** | Profile, scene, narrative arc, theme-driven | `references/type_feature.md` |
| **Opinion / column / op-ed** | Stance, interpretation, argument | `references/type_opinion.md` |

If ambiguous, **ask the user** — do not guess. If material spans multiple types, follow the user's specified type.

### Step 2: Material Audit & Gap Identification

Before drafting:

1. **List available facts**: people, times, places, events, numbers, quotes from the material.
2. **Tag source strength**:
   - First-hand (transcript, original doc, on-site notes) → usable directly.
   - Second-hand (other-media relay, forwarded message) → must cross-verify.
   - Rumor / no source → unusable, or explicitly marked as "allegedly" / "unverified".
3. **Tag gaps**: which 5W1H is missing? Is there a counter-side? Do numbers have a source? Do quotes have context? **Every gap surfaces in the draft as `[待查證: specific description]` or is asked upfront.**

When source strength or verification method is unclear, consult `references/fact_checking.md`.

### Step 3: Apply the Type Template

> **Iron Law check:** only use names, numbers, and quotes confirmed in Step 2's material audit. Any missing fact → `[待查證: description]`, not fill-in.

Write per the reference template loaded in Step 1. Cross-type principles:

- **Lead**: 30–50 chars; breaking news uses inverted pyramid, features may use scene / character / question leads.
- **Attribution**: direct quote `「…」王小明說。` / indirect `王小明表示…`. **Do not alter quote meaning**; punctuation cleanup is OK.
- **Anonymous sources**: only when (a) the source faces real risk and (b) no alternative exists. State the reason ("requested anonymity to avoid retaliation").
- **Numbers**: always cite the source. Pair ratios with absolutes ("layoffs of 30%, about 1,200 employees"). Avoid misleading comparisons.
- **Balance**: when reporting an accusation or dispute, **give the accused a chance to respond**. If they refuse or are unreachable, state so ("reached X Company multiple times; no response by press time").
- **Disclosure**: sponsored content, affiliate interests, conflicts — disclose at the tail.

Writing-style defaults:

- **Concrete over abstract**: "月薪 3 萬 2 千元" not "薪資不高".
- **Verbs over adjectives**: "抨擊" / "質疑" / "譴責" beat "嚴重地反對".
- **Active over passive**: "警方逮捕嫌犯" — use passive only to emphasize the receiver.
- **Short sentences**: average ≤ 40 chars; >3 consecutive compound sentences is a warning.
- **Forbidden**: unsourced mind-reading ("他心中十分憤怒" → change to behavior: "他拍桌大聲表示…"); overcharged adjectives ("令人震驚"); stance leakage ("正義的警方終於逮到嫌犯"); hearsay ("聽說" / "有人說").

### Step 4: Media Ethics Check (required)

**YOU MUST complete every item below in `references/media_ethics.md` before producing the output.** Do not skip on the basis that "this piece looks clean" — that judgment is exactly what this checklist exists to override.

1. Defamation risk? (unverified negative claims about a named real person)
2. Privacy breach? (disclosing private info without consent)
3. Source protection? (can an anonymous source be re-identified from details?)
4. Special-category topic? (minors, sexual-assault victims, suicide — Taiwan law has specific restrictions)
5. Undisclosed conflict of interest?
6. Image / material licensing?

**If any item is uncertain, warn the user explicitly in the output.** Do not silently pass.

### Step 5: Media Literacy Self-Check (required)

**YOU MUST complete every item below in `references/media_literacy.md` before producing the output.** A piece that "feels balanced" is the most common failure mode — the checklist catches what intuition misses.

1. Does the lead overstate (clickbait)? Does the headline match the body?
2. Are facts and opinions mixed? Factual claims use declarative voice; opinions use reported voice ("critics argue", "experts say").
3. Is the piece appealing to emotion instead of evidence?
4. Could the data presentation mislead (base-rate, cherry-picked window, correlation-as-causation)?
5. Are source tiers marked (official / principal / third-party / anonymous)?
6. If AI helped generate or organize any content, is that disclosed?

### Step 6: Output the Finished Piece

Emit per the Output Format below. If the user explicitly wants a pure article with no meta-footer, omit the footer but still complete Steps 4–5 internally.

**Stop and ask the user** when:

1. 2+ of 5W1H are missing from material.
2. Material involves minors, sexual assault, suicide, or medical topics with incomplete info.
3. Only a single source exists for an accusation against another party.
4. Type is unspecified and material spans multiple types.
5. Material contains contradictions (two versions of the same fact).
6. Requested length mismatches material volume (e.g., 3000-word investigation from 200-word briefing).

Ask all gaps in one message, not back-and-forth.

---

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

---

## Examples

### Good Example

**Scenario:** User provides a 1,200-word press-conference transcript from a Taipei restaurant-SaaS startup announcing Series A funding. Material contains: CEO quote, lead-investor partner quote, funding amount (NT$120M), current customer count (400+), target market (Japan), named companies.

**Analysis:**
1. Step 1: classified as breaking news (event-driven, 5W1H complete) → load `references/type_breaking_news.md`.
2. Step 2: material audit — 5W1H intact; all numbers trace to transcript; two direct quotes properly attributed; gap identified: no Japan-market sizing number supplied. Flagged as `[待查證: 日本餐飲 SaaS 滲透率來源]` in draft.
3. Step 3: inverted pyramid lead — WHO (startup) + WHAT (NT$120M Series A) + WHEN (today) + WHY (Japan expansion). Supporting paras add data, investor quote, product detail. CEO quote used verbatim.
4. Step 4: ethics check — no minors / victims / private-info risk; no undisclosed conflict; one investor name is a major VC (public info).
5. Step 5: literacy check — no clickbait; facts and investor's forward-looking statement clearly separated ("Partner X said the team 'could reach…'"); numbers paired with sources.
6. Output includes meta footer flagging the one `[待查證]` item and balance rating.

Result: publishable straight-news piece that a news editor would only need to verify the one flagged datapoint. No invented facts, no stance leakage, no ethics hazards.

### Bad Example

**Scenario:** Same input material as above. Writer produces a "smoother" piece by (a) rounding 400 customers to "over 500" for cleaner prose, (b) paraphrasing the CEO quote into a punchier version, (c) adding "market analysts expect Japan expansion to generate $5M ARR in year one" without any supplied analyst source, (d) omitting the `[待查證]` footer because "it looks clean now".

**What went wrong:**
- (a) fabricated a larger customer number — Iron Law violation. Even a "rounding up" is falsification.
- (b) quote modification changes attribution. Even if meaning is preserved, it's not what the person said — defamation / accuracy exposure.
- (c) invented an "analyst expectation" — a classic LLM hallucination pattern. An editor would pull this immediately and kill the piece.
- (d) removing the audit footer looks polished but hides the real trust problem: without `[待查證]` flags, a downstream editor has no signal that item (c) was never verified.

Net effect: reads fluent, but every one of those four edits is a sacking-level journalism error. The Iron Law's whole point is to block these defaults.

---

## Gotchas

- **"Sounds like a real quote" is how fabrication begins**: if a quote is not verbatim in the transcript, do not "reconstruct" it from context. Paraphrase with attribution, or mark `[引言待查證]`. Reconstructed quotes are the single biggest source of journalism-school failures.
- **Taiwan legal exposure differs from US**: 刑法 310 (誹謗罪) applies to true statements too if they lack public interest; 偵查不公開 restricts reporting details of ongoing investigations even when a reporter knows them; 性侵害犯罪防治法 forbids revealing information that could identify sexual-assault victims. See `references/media_ethics.md` before publishing anything touching these.
- **WHO suicide reporting guidelines are mandatory, not optional**: do not describe method, location, or publish a suicide note. Always include helpline text. Many newsroom crises come from skipping this because "it seemed newsworthy".
- **Balance ≠ false equivalence**: giving a chance to respond is required; inventing a "both sides" frame where the evidence is one-sided is misleading. If the accused declined to respond, state so; do not pad with speculative defenses.
- **Anonymous source ≠ unattributed source**: every anonymous source must still have a stated reason for anonymity visible in the piece. "A source said" with no context is a red flag, not professional practice.
- **Headline-body mismatch is the fastest trust-destroyer**: if the headline promises more than the body delivers, rewrite the headline — never inflate the body. In the self-check, re-read the headline last, against the actual body.

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/type_breaking_news.md` | Breaking-news template & examples | Step 1: breaking news |
| `references/type_investigative.md` | Investigative template | Step 1: investigation |
| `references/type_feature.md` | Feature / narrative template | Step 1: feature |
| `references/type_opinion.md` | Opinion / column template | Step 1: opinion |
| `references/media_literacy.md` | Self-check list | Step 5 (always) |
| `references/media_ethics.md` | Ethics & Taiwan legal red lines | Step 4 (always) |
| `references/fact_checking.md` | Verification methods, balance | When source tiers are unclear |

Related skills: `pr-press-release` (for company-voice announcements), `pr-crisis-communication` (for crisis-period messaging), `hum-source-criticism` (for deeper source-vetting frameworks), `hum-ethics` (for moral-framework reasoning).

---

## Limitations

- **Does not verify factual claims against external sources.** This skill checks internal consistency and flags gaps; it does not perform live fact-checking against databases, court records, or other external systems. The user must do this or provide verified material.
- **Taiwan-centric legal framing.** Media ethics and legal red lines reference Taiwan law (刑法 310、個資法、偵查不公開、性侵害犯罪防治法、兒少法). For US / EU / HK jurisdictions, the general principles still apply but specific statutes need substitution.
- **Long-form investigations beyond ~5,000 words.** For book-length projects, multi-part series, or documentary treatments, the templates here cover single-article craft; narrative architecture across a series needs additional planning beyond this skill.
- **Not a substitute for legal review.** When the piece contains a named accusation, publishing without attorney review is still risky regardless of this skill's ethics pass.
- **Does not generate its own original reporting.** If the supplied material is insufficient, this skill flags the gap — it will not go find additional sources.
