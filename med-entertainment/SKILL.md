---
name: "med-entertainment"
description: "Use when writing entertainment news — reviews, box office analysis, streaming reports, festival coverage, casting news — from supplied material (junkets, studio PR, embargoed reviews, interviews). Activates beat-specific discipline: press-junket disclosure, embargo-compliance, PR-vs-news, entertainment-law, industry-data literacy. Triggers: '寫電影評論', 'draft streaming piece', '整理藝人新聞', 'cover premiere', 'analyze box office'. Defers general workflow to med-news-reporter. NOT for fan content, movie marketing (mkt-*), or press releases (pr-press-release)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "entertainment-news", "film-tv-journalism", "press-ethics"]
---

# Entertainment News Reporting

> **This skill specializes med-news-reporter for the entertainment / film & TV beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **entertainment-beat-specific** discipline on top.

## Overview

Distilled from entertainment-journalism curricula at NCCU 傳播系、NTU 新聞所、Columbia Journalism School (Entertainment Reporting), USC Annenberg (Entertainment & Media), HKU JMSC (Arts & Culture). Covers the four main entertainment-news sub-types: **breaking entertainment news / film review / industry analysis / entertainment profile** reporting. Entertainment journalism carries acute risks around PR capture, embargo violation, defamation in celebrity context, and undisclosed conflicts that generic news discipline does not catch.

```
IRON LAW: Disclosed PR Is Not Independent Reporting

Anything supplied through PR channels — studio press junket, embargoed
press kit, paid advance screening, provided photograph, publicist-arranged
interview, or manufactured soundbite — carries a hidden agenda written by
the studio/agency, not independent observation. The piece must distinguish
clearly what came from PR (disclose it, mark it as the studio/agency framing)
versus what the reporter independently observed or verified.

Failing to make this distinction is the defining failure mode of entertainment
journalism: repeating PR talking points as independent assessment, accepting
junket-provided material as fact without verification, using studio-supplied
quotes as if they were freely given, publishing a photograph without noting
it is studio property with editorial use restrictions.

Default LLM behavior: smooth over the distinction, absorb PR framing,
omit the disclosure that a screening was paid, repeat PR vocabulary ("this
year's must-watch") without attribution. Override explicitly.
```

Why this is non-obvious: the PR material is often accurate and well-written. The violation is not "the fact is false" but "the source of this fact was not disclosed, and the framing it carries was presented as independent judgment." A sentence like "The film offers viewers a fresh take on family dynamics" may be true, but if that framing came from the studio press kit (verbatim or adapted), it must be attributed.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "The studio's description is accurate, so I can smooth it into the review" | Accuracy is not the issue. The issue is source attribution. If the phrasing or framing came from the studio, mark it as such. (E.g., "The studio calls it a 'fresh take'; in execution, the premise...") |
| "The press junket is a normal industry practice, I don't need to disclose it" | Industry normalcy ≠ ethical disclosure. Junket-screened films are tied to studio approval; readers deserve to know. Write "Screened at a studio-provided preview" or drop it entirely if it creates bias you cannot disclose. |
| "The embargo is just a courtesy; I can publish early if the story is ready" | Embargo is a contract. Breaking it (a) violates the journalist's professional credibility, (b) gets the outlet blacklisted by the studio, (c) undermines future embargoed access for peers. This is a hard line. |
| "The celebrity's publicist arranged the interview, so it's not a free agent" | Publicist-brokered interviews are standard. The disclosure is not "publicist-arranged" (assumed) but whether there were conditions (approval rights, off-limits topics, paid travel, quid pro quo). Disclose conditions; omit the obvious brokering. |
| "The PR photo is high-res and perfect; I'll use it without noting the source" | PR-provided images carry implicit editorial-use restrictions and are propaganda. Disclose: "Photo courtesy of [Studio]" or "Promotional still." If using a paparazzi photo instead, you've chosen differently. |
| "I'll use the studio's language ('blockbuster' / 'must-see') to sound professional" | Studio vocabulary is a form of framing. Replace with observable fact: instead of "epic scope", describe what scope means (runtime, number of countries, scale of sets). Let the reader decide if it's epic. |

---

## When to Use

**Trigger conditions:**
- User supplies entertainment material — 新片首映、電影評論、票房數據、串流平台數據、藝人宣傳、影視產業新聞、影評 embargo、製片公司新聞稿、影展報導 — and asks for a news piece.
- User asks for "影評" / "票房分析" / "新片評測" / "streaming coverage" / "entertainment feature" / "celebrity profile" / "industry trend analysis".
- User paraphrases: "幫我寫成電影評論", "把試映心得整理成報導", "寫一篇票房分析", "turn this junket transcript into a review", "analyze this streaming data".

**Input signals:**
- Named films, studios, actors, streaming platforms, box office numbers, ratings (Rotten Tomatoes / IMDb / Metacritic), production details, release dates.
- Direct quotes from filmmakers, cast, critics, industry analysts.
- Embargo-marked material (often specified with "Do not publish before [date/time]").

**When NOT to use:**
- Studio / agency press release in the agency's own voice → use `pr-press-release`.
- Fan content, aggregation of social-media takes, or non-journalism commentary → not journalism; decline.
- Movie marketing / ad copy → use `mkt-*` skills.
- Pure entertainment industry analysis without news angle (e.g., "here's how the streaming wars work") → use `ops-*` or industry-analysis skills.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds entertainment-specific Step 7 (PR Provenance Audit).

### Step 1: Classify the entertainment-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Breaking entertainment news** | Announcement, casting, signing, deal, film wrapped, festival selection, release-date shift | Who, what, when, industry impact; quote from studio / talent |
| **Film / entertainment review** | Embargo date provided, screening attended, pre-release material, evaluative judgment | Embargo compliance; independent viewing; distinction between supplied framing and observed detail |
| **Industry / trend analysis** | Box office patterns, streaming metrics, talent movement, franchise strategy, platform competition | Data sourcing and cross-verification; industry-data literacy red lines |
| **Entertainment profile** | Actor / director / producer profile, career retrospective, behind-the-scenes feature | Access (paid junket? free? negotiated?); disclosure of conditions |

If material spans sub-types (e.g., review + box office data), classify by primary news driver.

### Step 2: Entertainment-specific source vetting & PR-provenance tagging

**Every piece of information must be tagged by its provenance:**

- ❌ Vague: "The film's sweeping cinematography captures..." (where did this judgment come from? the studio press kit? your own viewing?)
- ✅ Specific: "The cinematographer used 140 locations across four countries (per production notes); in the film, the global scope..." (fact + source + observation)
- ✅ Disclosed PR: "The studio calls this 'emotionally intimate'; by contrast, the opening 30 minutes rely on voice-over rather than action..."

**Source tier tagging** (extends med-news-reporter's tiering with entertainment-specific tiers):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Public record** | Box Office Mojo (US), local grosses (Taiwan: 電影票房新聞稿), IMDb/RT/Metacritic public scores | Direct citation; no further disclosure |
| **Studio official** | Press release, press junket, studio-provided stills, official production notes | **MUST disclose** ("per studio press materials", "at a studio-hosted screening", "Photo © [Studio]") |
| **Independent critic / analyst** | Freelance film critic, box-office analyst unaffiliated with studio, third-party streaming researcher | Direct quote with affiliation; no special disclosure needed |
| **Talent on record** | Actor interview, director statement, publicist-arranged press call | Must note: any conditions? (approval rights, off-limits topics, paid travel?) |
| **Embargo-marked material** | Press review, critic screening, embargoed press kit | **CRITICAL**: never publish before embargo lift. Note in piece: "review embargoed until [date]" if necessary. |
| **Streaming platform self-report** | Netflix "top 10 hours", Disney+ "accounts engaged", Apple TV+ data (if disclosed) | Always note: platform-reported, not independent verification. Cross-platform comparison invalid. |

### Step 3: Entertainment-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **Embargo violation**: 
   - Every piece marked with an embargo date is a contract. Breaking it results in blacklist. If material is embargoed until Friday 9am, do not publish Thursday 10pm.
   - If the user asks you to publish before embargo lifts, stop and flag: `[待查證: 此素材有 embargo 標記至 X 日期時間;違反會導致媒體被列黑名單。確認可發佈?]`.

2. **演員隱私 vs 公眾人物** (celebrity privacy vs. public figure):
   - Public figure (named actor, director) has lower privacy expectation BUT not zero. Avoid revealing: home address, family members' identities (esp. minor children), medical details, relationship status (unless already public), workplace schedules that enable stalking.
   - 未成年演員: extra protection. 兒少法 restricts disclosure. Do not reveal age, school, family details beyond what is necessary for the news.

3. **肖像權與宣傳劇照** (publicity images vs. paparazzi):
   - Publicity still (from studio): comes with usage restrictions. Disclose source. Some studios restrict use to "in context of film review" — respect that.
   - Paparazzi photo (of actor on the street): different legal status. Disclose source. Be alert to stalking / harassment overtones.

4. **評論 vs 個人攻擊** (criticism vs. personal attack):
   - Criticizing a film ("the dialogue fell flat") is fair comment.
   - Criticizing an actor's professional choice ("casting choice felt stiff") is fair comment.
   - Criticizing an actor's appearance ("she looks tired", "he's aged badly") or personal life ("her romance with X is suspicious") crosses into personal attack. High defamation risk + harmful.

5. **置入性行銷揭露** (product placement / brand integration):
   - If a character drinks a named brand prominently (and the brand paid for placement or the product was branded in post), disclose it: "Note: contains paid brand integration for [Brand]."
   - If the studio provided a promotional tie-in (e.g. "the film partners with [Fast Food Chain]"), you can cover it as a business story, but mark it clearly.

6. **粉絲評分 vs 評論家評分** (audience score vs. critic score):
   - Rotten Tomatoes: cite both Tomatometer (critics) and Audience Score. Note: audience score is vulnerable to brigading / review-bombing. If a film is surrounded by controversy, mention that explicitly.
   - IMDb: cite the number and date polled. IMDb scores can shift 0.5 points in hours if a fandom organizes.

### Step 4: PR Provenance Audit (entertainment-specific addition)

Before output, sweep the draft for every non-trivial fact and ask: **"Where did I get this information?"**

For each fact, trace back:
- Is it from a studio press kit or press junket? → Disclose.
- Is it from an independent source (critic, analyst, public data)? → No special disclosure.
- Is it from a publicity photo? → Credit source.
- Is it from an interview? → Was it on-record or with conditions? Disclose conditions if any.
- Is it from streaming platform data? → Note it's self-reported and platform-specific.

If you cannot answer "where did I get this", it stays out of the piece or is marked `[待查證]`.

---

## Output Format

Use the med-news-reporter base format, with these entertainment additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 即時娛樂新聞 / 影評 / 產業分析 / 人物專訪
**字數**: approx. XXX
**消息來源層級**: 獨立評論 N / 製作方官方 N / 藝人親訪 N / 串流平台自報 N
**PR 來源揭露稽核**:
- 新聞稿 / 試映會 / 宣傳劇照: ✅ / ⚠️ (列出未揭露的項目)
- Embargo 合規: ✅ / ⚠️ (列出 embargo 日期 + 符合狀況)
- 獨立觀察 vs PR 框架: ✅ / ⚠️ (列出混淆的段落)
**串流平台數據**:
- 來源: ✅ / N/A / ⚠️ (平台自報 vs 獨立研究?)
- 跨平台比較警告: ⚠️ (如果有, 列出不可比之處)
**藝人隱私 / 肖像權**:
- 未成年演員保護: ✅ / N/A / ⚠️
- 隱私邊界: ✅ / ⚠️ (列出敏感揭露)
**名譽 / 評論邊界**:
- 評論 vs 個人攻擊: ✅ / ⚠️ (列出潛在攻擊性字眼)
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

### Good Example

**Scenario:** User supplies (a) official press materials from a fictional studio (「範例影業」Demo Pictures) announcing 「示範之夜」 Demo Night premiere, including 王大明 (director) and 林小華 (lead actress); (b) a studio-provided still from the film; (c) ticket sales data from 國家電影中心; (d) an embargo-marked critic preview from a film-review outlet, embargoed until Friday 2pm; (e) a Rotten Tomatoes link showing 78% critics / 64% audience; (f) platform data from Netflix showing the film in "Top 10" for Taiwan. User asks for a 600-word release-day review piece.

**Analysis:**
1. Step 1: classified as **review** (embargo-marked material, evaluative content) → emphasize independent viewing + embargo compliance.
2. Step 2: source tagging —
   - Studio press materials → disclose in piece ("Per studio materials...") or omit if not independently verified.
   - Photo → disclose source ("Photo © Demo Pictures").
   - Ticket sales → cite 國家電影中心 as source; this is public record.
   - Embargo-marked preview → **CRITICAL**: count the embargo time. If it lifts Friday 2pm and the user wants to publish today (Thursday), flag this; if Friday 5pm, OK to proceed.
   - RT scores → cite both critics (78%) and audience (64%); note audience score can shift.
   - Netflix "Top 10" → note this is self-reported Netflix data; do not compare to other platforms' metrics.
3. Step 3: risk checks —
   - Embargo: confirmed it lifts before the user's desired publish time.
   - Privacy: director and actress are public figures; no undisclosed personal details.
   - Evaluation: review should criticize the film, not the actors' appearance or personal lives.
4. Step 4 (PR Provenance Audit):
   - Opening paragraph draws on independent viewing observation, not studio press kit → no disclosure.
   - If writer uses a description that mirrors studio materials verbatim ("a breathtaking meditation on memory"), mark it: disclose the framing came from studio, or replace with independent description.
   - Photo → include credit line "Photo courtesy of Demo Pictures".
   - RT scores → cite both tiers; note audience score reflects both genuine reviews and possible brigading (if any controversy exists).
5. Output footer: lists embargo status (✅ compliant), RT tiers cited, Netflix data noted as self-reported, studio-provided materials disclosed at article bottom.

Result: Review is publishable without ethics red flags. Reader understands which judgments came from independent viewing vs. studio framing. Embargo is observed. Data sources are disclosed.

### Bad Example

**Scenario:** Same input. Writer produces a piece by (a) opening with "「示範之夜」offers a breathtaking meditation on memory — a testament to 王大明's visionary direction" (verbatim from studio press kit, unmarked), (b) using the studio photo without credit line, (c) citing RT as "critics and audiences praise the film" without mentioning the 14-point gap (78% vs 64%) or the brigading potential, (d) stating the film is "the #1 most-watched film on Netflix globally" (actually it's top 10 in Taiwan; writer invented the "globally" part to match supply PR framing), (e) including intimate details about 林小華's childhood and family (sourced from an old paparazzi interview, not disclosed, borders on privacy breach), (f) publishing the piece Thursday 10am (embargo lifts Friday 2pm — violation).

**What went wrong:**
- (a) Verbatim studio framing unmarked = plagiarism + bias. Even if true, the framing choice (why "visionary" and not "ambitious"?) comes from PR. Must disclose or replace with independent language.
- (b) No photo credit = rights violation and failure to disclose studio origin.
- (c) Hiding the RT score gap is misleading. The gap suggests audience backlash or brigading; reader cannot make informed judgment without seeing it.
- (d) "Globally #1" is invented. Studio "Top 10 in Taiwan" got expanded into "#1 globally". Factual fabrication.
- (e) Undisclosed privacy invasion. 林小華's childhood is personal; including it without her consent and without news relevance crosses the line.
- (f) Embargo violation = blacklist from studio, damages journalist credibility, undermines peer access.

Net: every single item is an entertainment-journalism-specific gotcha that a generic news-reporter skill would not catch.

---

## Gotchas

- **Embargo is a contract, not a suggestion**: 影評 embargo 通常在發片前 24-48 小時解除;違反會被製片公司列入黑名單,影響後續採訪與試映機會。如果素材標記「Do not publish before 2026-05-02 14:00」,嚴格遵守時間。提前一小時發佈會被視為違反。
- **「新聞稿」vs「獨立評論」的界線在字句**: 如果描述(例如 "breathtaking meditation on memory")逐字或高度相似出現在製片方新聞稿,就來自 PR,必須揭露或替換。光是改個詞序("memory meditation, breathtaking")還是同一個 PR 框架。
- **宣傳劇照無版權揭露就是侵權**: 製片公司提供的照片附帶隱含版權。務必註明「Photo © [Studio Name]」或「Promotional still courtesy of...」。omitting credit 是侵權+不揭露 PR 來源的雙重失誤。
- **串流平台數據不可跨平台比較**: Netflix 用「小時數」(watch hours), Disney+ 用「帳戶數」(accounts engaged), Apple TV+ 通常不公布詳細數字。宣稱「Netflix 上最受歡迎電影」時絕不能同時比較「Disney+ 也在前 10」— 計算口徑完全不同,此比較誤導讀者。
- **Rotten Tomatoes audience score 易被刷分**: 粉絲或反對者可集體投票影響 audience score。引用時務必 (a) 明確區分 Tomatometer (critics) 與 Audience Score, (b) 提及高度爭議的電影可能有刷分現象, (c) 看發布日期是否有明顯波動。
- **「未成年演員」受兒少法保護**: 台灣 兒少法 限制未成年人隱私揭露。不得揭露未成年演員真實姓名、就讀學校、家庭成員、住所等,除非絕對必要且由法定代理人同意。若製片方提供的素材含有此類資訊,應主動刪除。
- **評論「電影」vs 攻擊「人」的差別**: 寫「劇本對白顯得生硬」可接受; 寫「女主角演得生硬」也可接受; 但「女主角看起來疲憊」「他明顯衰老了」跨入人身攻擊,有名譽侵害風險。
- **置入性行銷必須揭露**: 如果電影中角色飲用名牌飲料且該品牌付費置入,文中應註記「Note: contains paid brand integration」。若製片公司與連鎖餐飲合作推廣,可以報導此業務合作,但須明確標記為商業新聞而非內容評論。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 娛樂線消息來源、製片機構、串流平台、獨立評論家資料庫 | Step 2 source vetting |
| `references/glossary.md` | 娛樂 / 電影 / 票房 / 串流專業術語 | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 藝人隱私、肖像權、未成年演員保護、名譽侵害、置入性行銷法律框架 | Step 3 risk check |
| `references/pr_vs_news.md` | Junket / embargo / 製片方公開資料 / 藝人受訪條件的處理 | Step 2-3 PR disclosure |
| `references/industry_data_reading.md` | 票房數字可信度判讀、串流自報數據陷阱、評分網站操縱、數據比較紅線 | Whenever industry metrics are cited |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-culture` — for arts/culture journalism (overlaps on criticism craft, separate beat focus)
- `hum-rhetoric` — frame analysis (useful for detecting PR framing)
- `data-financial-analysis` — box office / revenue deep dives
- `pr-press-release` — for writing press releases (not journalism)

---

## Limitations

- **Jurisdictional scope**: legal references (兒少法、著作權法、肖像權) reflect Taiwan law. For US (1A + Right of Privacy), UK (Defamation Act 2013), HK contexts, principles apply but statutes differ — substitute jurisdiction-specific references.
- **Does not verify external data**: this skill flags claims that need verification; it does not check live Box Office Mojo, verify streaming numbers, or cross-check RT scores in real-time. Editor must verify or supply.
- **Embargo timing is user's responsibility**: this skill reminds the user of embargo dates in the material; it cannot enforce embargo-aware scheduling at publish time. User (or CMS system) must ensure scheduled posts respect embargo.
- **Not a PR-extraction skill**: if the user wants to convert a press release into news language, use `med-news-reporter` + this skill's Gotchas; this skill does not automate the conversion.
- **Entertainment-news specific**: focuses on film, TV, streaming, and celebrity. Does not cover music journalism, gaming journalism, or broader arts/culture reporting (use `med-culture` for arts/culture).
