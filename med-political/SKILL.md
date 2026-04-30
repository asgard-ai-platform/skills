---
name: "med-political"
description: "Use when the user wants to write a political news piece — election coverage, legislative reporting, policy analysis, official-statement coverage, poll interpretation, or political profile — from supplied material (transcripts, press releases, poll data, vote records, leaked documents, interviews). Activates political-beat-specific workflow on top of the general news-reporter workflow: stance tagging, poll-reading discipline, defamation/election-law red lines, and frame-neutrality audit. Also triggers on phrases like 'write up this 質詢', 'turn into an election report', 'analyze this poll', '幫我寫成政策追蹤報導', '寫一篇選戰分析', '把這份立委發言整理成新聞', 'cover this candidate's policy platform'. Defers general news craft to med-news-reporter; do NOT use for press releases (use pr-press-release) or government PR (use pr-*)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "political-news", "elections", "policy", "media-ethics"]
---

# Political News Reporting

> **This skill specializes med-news-reporter for the political beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **political-beat-specific** discipline on top.

## Overview

Distilled from political-journalism curricula at NCCU 政治系、NTU 政治系、Columbia Journalism School (Politics), Medill (Politics & Policy), Sciences Po École de journalisme. Covers the four main political-news sub-types: **election / legislative / policy / official-statement** reporting.

```
IRON LAW: No Stealth Bias

Political reporting carries stance through dozens of micro-choices that
each pass a literal fact-check but together push the reader toward a
conclusion: which adjective ("controversial" / "embattled" / "popular"),
whose quote leads, who gets the last word, where the contextualizing
data sits, which framing ("crackdown" vs "enforcement"), which timeline
("after the scandal" vs "during the second term"). Every such choice
must be either deliberately neutral or its slant disclosed. The reader
is owed a piece they can read without absorbing your verdict by osmosis.

Default LLM behavior is to pick the most "natural-sounding" word,
which in political contexts almost always carries the dominant-media
frame as bias. Override that default explicitly.
```

Why this is non-obvious: the literal-fact-check passes ("the bill failed 35-40, the polling shows 47%") while the cumulative effect of word-choice and ordering quietly endorses a side. This is the failure mode that gets political reporting accused of bias by every side — usually correctly.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "'Controversial' is just a description, everyone uses it" | Adjective-level frames are the single most common channel for stealth bias. Use the specific dispute, not a labeled judgment. ("opposed by labor unions" not "controversial"). |
| "I'll lead with the strongest soundbite for narrative impact" | Whose soundbite leads = whose frame leads. Lead-quote selection is a stance choice; alternate sides or use a non-quote lead. |
| "The opposition response is just boilerplate denial, I can summarize" | "Summarizing" the rebuttal-side while quoting the accusing-side verbatim is the textbook one-sided structure. Quote both or summarize both. |
| "The poll headline is enough — adding methodology is in-the-weeds" | A headline poll number without sample / MOE / date / who paid is misleading by omission. Always include the four. |
| "This anonymous campaign source is well-placed, I'll just say 'a source close to the campaign'" | Anonymous negative claims about named politicians need (a) real risk to the source AND (b) editor sign-off AND (c) corroboration. "A source said" with no risk justification = professional malpractice in political reporting. |
| "The accused didn't respond by deadline, the story can run as-is" | Political accusation pieces require the response window be stated explicitly in the piece ("contacted X repeatedly between Y date and Z, no response"). Silent omission = imbalance. |

---

## When to Use

**Trigger conditions:**
- User supplies political material — 立法院質詢、政府記者會、政策白皮書、候選人政見、選戰文宣、民調數據、投票記錄、洩密文件、政治人物訪談 — and asks for a news piece.
- User asks for "選戰報導" / "政策分析" / "立委質詢整理" / "election coverage" / "policy tracker" / "political profile" / "campaign news".
- User paraphrases: "幫我把這份質詢做成新聞", "寫一篇選舉觀察", "整理成政策追蹤", "draft a piece on this vote", "analyze this poll".

**Input signals:**
- Named politicians, parties, government agencies, election candidates, civic organizations.
- Poll numbers, vote tallies, legislative bill numbers, policy documents.
- Direct quotes from officials, candidates, campaign staff, opposition figures.

**When NOT to use:**
- Government / agency press release in the agency's own voice → use `pr-press-release`.
- Op-ed / commentary / column on a political topic → use `med-news-reporter` with type=opinion (this skill is for news, not commentary; though Gotchas here still apply).
- Pure international relations / diplomacy without domestic-political angle → use `med-international`.
- Election campaign marketing / ads → not a journalism use case; decline.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds a political-specific Step 7 (Frame Neutrality Audit).

### Step 1: Classify the political-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Election coverage** | Candidate, campaign, polling, primary, vote share | Candidate stance attribution; equal time / equal scrutiny across candidates; poll discipline |
| **Legislative** | Bill / 法案、立委質詢、committee, vote, amendment | Vote record citation; bill text vs summary; conflict-of-interest disclosure on sponsors |
| **Policy** | White paper, agency rule, regulation, budget line | Policy text + impact-affected parties + opposing experts + cost estimate source |
| **Official statement / press conference** | Speech, press conference, official communiqué | Verbatim quote + context (when, where, in response to what) + counter-position |

If the material spans sub-types (e.g. a candidate's policy speech), classify by the *primary news driver*, not the genre.

### Step 2: Source vetting & stance tagging

**Every named political actor in the piece must carry a stance tag** at first mention, and the tag must be specific enough to let readers calibrate the quote:

- ❌ Vague: 「立委王大明表示...」
- ✅ Specific: 「民進黨立委、社會福利及衛生環境委員會召委王大明表示...」
- ✅ When stake matters: 「兼任 X 公司獨立董事的國民黨立委王大明表示...」(if the bill affects X)

**Source tier tagging** (extends med-news-reporter's tiering with political-specific tiers):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Public record** | 立法院公報、政府公報、選舉公報、官方記者會逐字稿 | Direct citation; no further attribution needed |
| **Named source on record** | 政治人物本人、有職稱發言 | Direct quote with stance tag |
| **Background source** | 「不具名的黨內人士」 | Requires named editor sign-off + risk justification + corroboration |
| **Adversarial source** | 對手陣營、爆料者 | Doubled scrutiny; corroborate before publishing |
| **Polling** | Released polls | Always include sample/MOE/methodology/sponsor/dates — see `references/poll_reading.md` |

### Step 3: Political-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **公職人員選舉罷免法** considerations:
   - Election period restrictions on poll publication (typically 投票日前 10 日禁止公布民調).
   - Equal-treatment principle for candidates: if you give Candidate A 300 words of accusation, Candidate B's response gets equivalent space, not a one-sentence dismissal.

2. **誹謗 (刑法 310)** in political context:
   - Negative claims about politicians have heightened "public interest" defense, BUT the defense requires **reasonable belief in truth at time of publication** and **public-benefit purpose**. Do not assume "it's a politician, so I can say anything".
   - Allegations from opposition figures are still allegations; report them as accusations, not facts: 「對手陣營指稱」not 「事實上王大明...」.

3. **預算/財政數字** must include base-year, scope, and source:
   - ❌ "撥款 50 億" (over what period? from which budget? confirmed or proposed?)
   - ✅ "編列 113 年度公務預算 50 億元,屬經常門" / "三年期計畫累計 50 億"

4. **政府機關保密** vs **新聞自由**:
   - 機密文件報導:確認文件真實性 + 報導具公益性 + 來源同意 + 給對方回應機會。
   - 偵查不公開:涉及檢調案件時,即使取得資訊,也需衡量是否造成偵查阻礙或當事人權益侵害。

### Step 4: Frame Neutrality Audit (political-specific addition)

Before output, sweep the draft for:

1. **Adjective audit**: highlight every evaluative adjective ("controversial", "embattled", "popular", "hardline", "moderate", "extreme"). For each: replace with the specific underlying fact, OR cite who calls them that, OR delete.
2. **Quote-order audit**: count first-quote-from-each-side. If the same side leads in 3+ paragraphs, restructure.
3. **Last-word audit**: who gets the last quote? In a contested piece, the last word should be either neutral or alternated across pieces in a series.
4. **Frame-word check**: "crackdown" vs "enforcement", "regime" vs "government", "scheme" vs "program", "claim" vs "say". Each pair carries a stance. Use the more neutral term unless the loaded term is itself the news.
5. **Implied causation**: "after the scandal" implies the scandal caused the next event. Prefer "in date X" or explicit causal evidence.
6. **Background-context placement**: where you place the contextualizing fact (high vs low in the story) shapes the reader's frame. Place the most-relevant counter-context near the strongest claim.

---

## Output Format

Use the med-news-reporter base format, with these political additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 即時政治新聞 / 政策深度 / 選戰分析 / 質詢整理
**字數**: approx. XXX
**消息來源層級**: 公開記錄 N / 具名 N / 背景 N / 對手陣營 N / 民調 N
**政治平衡稽核**:
- Stance tag 完整性: ✅ / ⚠️ (列出未標的)
- 兩造機會: ✅ / ⚠️ (列出未取得回應的一方 + 已嘗試聯繫紀錄)
- 民調引用完備: ✅ / N/A / ⚠️ (列出缺項: 樣本 / MOE / 方法 / 委託方 / 日期)
- Frame neutrality: ✅ / ⚠️ (列出 audit 中替換或保留的字詞)
**選舉法 / 誹謗風險**:
- 選罷法時段限制: ✅ / N/A / ⚠️
- 對名譽指控之合理查證紀錄: ✅ / N/A / ⚠️
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

### Good Example

**Scenario:** User supplies (a) 立法院公報節錄一段民進黨立委王大明對勞動部長林小華的口頭質詢逐字稿,內容批評最低工資調整幅度過低;(b) 勞動部隔日新聞稿回應;(c) 主計總處公布的物價指數;(d) 一份委託方為勞工團體、樣本 1,068、MOE ±3.0% 的民意調查,顯示 62% 民眾認為調幅不足。要求寫一篇 800 字政策追蹤報導。

**Analysis:**
1. Step 1: classified as **policy** sub-type (政策追蹤),因為焦點是政策爭議而非選舉。
2. Step 2: stance tag — 王大明標註「民進黨立委、社會福利及衛生環境委員會委員」;林小華標註「勞動部長」;民調明確標註委託方「全國產業總工會」、樣本、MOE、日期。
3. Step 3: 預算數字審視 — 質詢提到「最低工資 27,470 元」屬公開公告數字,可直接引用;物價指數明確引用主計總處公告期別。
4. Step 4 (Frame Audit):
   - "controversial 27,470" → 改為 "全國產業總工會稱調幅不足、勞動部稱已參酌物價漲幅的 27,470 元"
   - 王大明質詢被引述後,林小華回應放在第二段(避免「只給批評者發言」)。
   - 民調來自勞工團體委託,在內文明示「委託單位為全國產業總工會」(避免讀者誤以為中立民調)。
5. Output footer 標示 stance、兩造皆取得回應、民調委託方揭露。

Result: 同時讓批評方與政策方有充分發言空間;讀者可以自己判斷;沒有「正義立委挑戰拖延部長」式的 framing。

### Bad Example

**Scenario:** Same input. Writer (a) leads with王大明 the strongest critical soundbite without reference to 林小華's response until paragraph 4, (b) describes the調幅 as "保守的", (c) cites the民調 as "民調顯示六成民眾認為調幅不足" without noting it was union-funded, (d) attributes anonymously: 「黨內人士透露,部長對工會壓力反應不足」without justification, (e) ends with 王大明's "勞動部該真正聽到勞工的聲音" line as last word.

**What went wrong:**
- (a) Lead-quote selection puts the criticism frame in the reader's head before the policy is described — Iron Law violation (stealth bias via ordering).
- (b) "保守的" is an evaluative adjective without attribution. Even if true, must cite who calls it that.
- (c) Omitting the funding source of the poll is misleading by omission. The headline number changes meaning when reader knows the union funded it.
- (d) Anonymous source for negative claim about a named official with no risk justification is professional malpractice.
- (e) Last-word selection reinforces the lead frame — same Iron Law violation closing the loop.

Net: every individual sentence is "true", but the cumulative effect is an editorial in the shape of a news piece. This is exactly the failure mode the Frame Neutrality Audit exists to catch.

---

## Gotchas

- **「不具名黨內人士」是一條紅線, 不是隨手可用的標籤**: anonymous sources for negative political claims need editor sign-off, risk justification, and corroboration. If the user supplies an unattributed quote that smells political, ask whether it can be on-record before quoting it; if not, mark `[匿名: 待確認可否揭露 + 取得交叉佐證]`.
- **民調引用未附四項基本資訊就是違反專業**: 樣本數、誤差範圍、調查方法 (CATI / 網路 / 實體)、委託方/執行方、調查日期 — 缺一不可。Beware the LLM tendency to drop this for "cleaner prose"; this footer is the protection against poll-as-spin.
- **選舉期間時段禁制需查證**: Taiwan 的選罷法禁止投票日前 10 日內公布特定民調(實際條文與年份請查證最新版)。誤觸時段禁制可能導致下架或法律責任。在選戰期間發稿前要查日期。
- **質詢 ≠ 事實**: 立委在質詢中提出的「指控」具言論免責 (憲法 73),但媒體轉述若以「事實」呈現會喪失保護。一律用「立委質詢時指出」「立委指稱」等轉述語氣,不可寫「事實上王大明在某某時間做了某某事」(除非另有獨立查證)。
- **「政府消息來源」不是消息來源**: 政府機關發出的訊息分官方公告(可引)、新聞稿(可引但須標註)、不具名背景簡報(高風險,需獨立查證)。三者混為一談會誤導讀者對訊息可信度的判讀。
- **預算數字與時間軸**: 政策報導極易出現「撥款 50 億」這種無基期、無範圍的數字。永遠標明:預算年度 / 是否包括以前年度承接 / 經常門 vs 資本門 / 該數字來源 (主計總處/部會/智庫)。
- **平等對待原則 (equal time)**: 在選戰報導,各候選人(尤其主要對手)的曝光度、批評強度、回應機會應大致對等。否則容易構成偏頗報導之指控。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 政治線消息來源、機構、官方資料庫、政府公開資訊清單 | Step 2 source vetting |
| `references/glossary.md` | 政治、立法、選舉專業術語對照與定義 | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 選罷法、誹謗、洩密、偵查不公開、平等對待原則 | Step 3 risk check |
| `references/poll_reading.md` | 民意調查判讀:樣本、MOE、加權、委託方、發布時段 | Whenever a poll is cited |
| `references/frames_and_neutrality.md` | 常見框架陷阱、loaded language 對照表、平衡寫法範例 | Step 4 Frame Neutrality Audit |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-international` — for international/diplomatic political stories
- `hum-rhetoric` — deeper analysis of persuasion structures (useful for op-ed evaluation)
- `hum-source-criticism` — source vetting frameworks
- `stat-hypothesis-testing` / `data-financial-analysis` — for data-driven political pieces

---

## Limitations

- **Jurisdictional scope**: legal references (選罷法、刑法 310、偵查不公開) reflect Taiwan law. For US (1A jurisprudence), UK (Defamation Act 2013), HK, or PRC contexts, the principles still apply but specific statutes and thresholds differ — substitute jurisdiction-specific references.
- **Does not perform live fact verification**: this skill flags claims that need verification; it does not check live legislative records, vote tallies, or news archives. Editor must verify or supply.
- **Not a poll-design skill**: judging poll *quality* (sampling frame validity, question wording bias) is partially covered in `references/poll_reading.md`, but for deep methodological critique use `stat-hypothesis-testing` and `grad-survey-design`.
- **Election-period restrictions are time-sensitive**: cited dates and prohibitions reflect the regulatory framework at writing time; always verify against current 中央選舉委員會 / 立法院 announcements before publishing.
- **Political opinion / op-ed** is out of scope; this skill is for news. For commentary, use `med-news-reporter` with `type=opinion` and apply this file's Gotchas as a sanity check.
