---
name: "med-international"
description: "Use when writing an international news piece — foreign affairs, diplomatic coverage, cross-border conflict, UN/multilateral updates, development news, or geopolitical analysis. Activates international-beat workflow: primary-source verification for distant claims, translation accuracy, conflict-side balance, regional context, source-chain auditing. Triggers on phrases like 'write this UN report', '寫一篇國際新聞', 'international story', 'draft conflict analysis', '整理聯合國決議', 'foreign affairs coverage'. Do NOT use for domestic political stories (use med-political), company press releases (use pr-press-release), or international business news (use med-business)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "international-news", "foreign-affairs", "media-ethics", "conflict-reporting"]
---

# International News Reporting

> **This skill specializes med-news-reporter for the international beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **international-affairs-specific** discipline on top: primary-source verification for distant events, translation accuracy, regional context, and conflict-side audit.

## Overview

Distilled from international journalism curricula at Columbia's Graduate School of Journalism (Global Journalism), Hong Kong Baptist University (MA International Journalism), Reuters Institute, and war-reporting bodies (Dart Center, CPJ, Thomson Foundation). Covers five main international-news sub-types: **breaking international news / diplomatic coverage / conflict reporting / UN/multilateral updates / development/humanitarian news**.

```
IRON LAW: Distance Is Not Authority

Claims about distant places — whether from official sources, international
media, or translated reports — need a transparent source chain tracing back
to a primary source (firsthand observation, official statement, or direct quote).
"According to international media" or "per Reuters reporting" does not qualify
as primary source. A Reuters cite of an unnamed US official is still an unnamed
US official, not Reuters' own reporting. Translated quotes must be re-verified
against the original language for politically loaded terms (regime/government,
occupied/disputed, freedom-fighter/militant). Distance through translation
or intermediary reporting compounds the risk; every link in the chain must
be visible to the reader so they can recalibrate the claim's authority.

Default LLM behavior is to accept a well-sourced second-hand report as if it
were primary source. Override that: when you cannot trace the claim back to
a named primary actor (official, eyewitness, document), flag it as indirect.
```

Why this is non-obvious: international news often arrives through layered translation and relay (foreign correspondent → news wire → local outlet). Each layer can introduce error, lose nuance, or shift framing imperceptibly. The reader cannot see those layers; the writer must expose them. "A UN spokesperson said" is primary; "media reports suggest" is not.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "Reuters reported this, so it's well-sourced" | Reuters is trustworthy, but if Reuters is citing an unnamed official, the sourcing ends with Reuters; the reader deserves to know they're reading an unnamed-source claim, not Reuters' own reporting. Layer the attribution. |
| "The translated quote means the same thing, close enough" | Political language trades on tiny word shifts. "Chinese government" vs "Beijing authorities" vs "the regime" signal different framings. Always check the original language for loaded terms, especially in cross-strait, Russia-Ukraine, Israel-Palestine contexts. |
| "I'll say 'various media reports' to show it's a well-known claim" | Vague aggregation ("various reports") hides the actual source tier and lets readers mistake opinion consensus for fact. Name the specific source tier (official statement, news wire, social media) even if you don't name the outlet. |
| "The country is unstable, so on-the-ground reporting is impossible" | This is exactly when you flag the gap. Don't invent a report from X when you only have a relay from Y. Tell readers "could not reach in-country sources, relying on exile/diaspora outlets" — that's honest metadata. |
| "The fixer/local contact says this is what's happening there" | Fixers are essential, but their political position shapes what they show you. If a fixer is from one side of an ethnic/sectarian divide, disclose that upstream of relying on their reporting. Fixer attribution is not transparent sourcing. |
| "International law experts all say this is genocide, so I can use that framing" | Genocide is a legal term (Rome Statute). If no tribunal has ruled, use "accused of genocide" / "claims of genocide" / "experts argue the incidents meet genocide criteria" — do not elevate accusation to judgment. |

---

## When to Use

**Trigger conditions:**
- User supplies international-affairs material — UN press releases, diplomatic statements, foreign-government communiqués, international-correspondent reporting, cross-border event notes, humanitarian organization updates — and asks for a news piece.
- User asks for "international news" / "foreign affairs coverage" / "diplomatic report" / "UN update" / "conflict analysis" / "international briefing" / "國際新聞" / "整理聯合國決議" / "寫一篇國際分析".
- User paraphrases: "寫成國際新聞", "整理雙邊外交談判", "draft a piece on the crisis in X", "幫我做這份國際組織報告的報導", "turn this diplomatic statement into a story".

**Input signals:**
- Named countries, international organizations (UN, WHO, IMF, ICRC), foreign officials, cross-border events.
- Official statements from foreign governments, embassies, international agencies.
- Reporting from foreign correspondents, international news wires (Reuters, AP, AFP, BBC), diaspora/exile media.
- Translated material from non-English primary sources (foreign-language government statements, local media).
- Regional context clues (geopolitical stakes, historical conflict, treaty references, sanction/embargo mentions).

**When NOT to use:**
- Domestic-political story with international angle → primary use `med-political` (e.g., Taiwan election coverage, US Congress vote on foreign aid).
- International business / market / investment news → use `med-business`.
- Press release from a corporation's own voice → use `pr-press-release`.
- Humanitarian/development project coverage focused on implementing organization → use `ops-project-report` or humanitarian-specific skill if available.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1–3 and adds international-specific Steps 4–5 (Source Chain Audit and Regional Context Mapping).

### Step 1: Classify the international-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|-------------------|
| **Breaking international news** | Event (military action, natural disaster, election), press conference, announcement, 5W1H from official source | Official statement verification; casualty figures sourcing; geographic framing; early-edition caution |
| **Diplomatic coverage** | Bilateral talks, multilateral summit, treaty signing, foreign-visit, diplomatic protest (demarche, formal note) | Diplomatic protocol accuracy; sides' official positions; precondition/outcome separation; "no comment" transparency |
| **Conflict reporting** | Military operations, ceasefire, humanitarian access, refugee movement, civilian impact | Warring-sides balance; casualty verification; fixer/in-country-reporting disclosure; safety of reporting sources |
| **UN / multilateral updates** | UN resolution, agency report (WHO, UNHCR, OCHA), international negotiation outcome | Vote tally / abstention disclosure; resolution text vs. political intent; implementation gap flagging |
| **Development / humanitarian** | Aid response, disaster recovery, refugee camp, sanitation crisis, development project | Implementing vs. donor agency distinction; beneficiary vs. authority voice; supply-chain transparency |

### Step 2: Source vetting & source-chain tagging

Beyond med-news-reporter's source tiering, international reporting adds **chain transparency**:

- **Primary source**: Official statement (government spokesperson, signed treaty, UN vote record), eyewitness, named expert on record.
- **Secondary source**: News-wire reporting (Reuters, AP, AFP, BBC) citing primary or official source in text. If the wire cites "unnamed officials", that tier must be transparent to the reader.
- **Tertiary source**: One outlet reporting another outlet's reporting. Dangerous. Avoid relaying; cite the original.
- **Translation layer**: Quote originally in another language. Must check original for political framing; note translation source.
- **Fixer/local-contact reporting**: Essential for on-the-ground context, but disclose fixer's background / affiliation so reader can calibrate bias.

**Tag each claim in your material audit:**
- ✅ **Direct official**: "The Ukrainian government said…" (traced to official statement, quote, or press release).
- ⚠️ **Translated quote**: "The president said [QUOTE TRANSLATED FROM FRENCH]" — flag for re-verification against French original.
- ⚠️ **Wire reporting a source**: "Reuters reported that unnamed US officials said…" — keep the "unnamed" visible; do not upgrade to fact.
- ❌ **Relay of relay**: "Middle Eastern outlets report that some outlets suggest…" — unacceptable, break the chain and cite original or discard.

### Step 3: Political-sensitivity risk check

Beyond med-news-reporter's ethics, add international heat-map:

1. **Cross-strait language** (台灣/中國 framing):
   - "中國" (PRC only) vs "中華人民共和國" (official) vs "大陸" vs "中共".
   - "台灣" (neutral) vs "中華民國" (political) vs "島嶼" (descriptive).
   - "政府" (neutral) vs "當局" (implies non-legitimacy) vs "政權" (charged).
   - Document which term is used by which source; let reader see the framing choice.

2. **Conflict-terminology red lines**:
   - "Genocide": legal term (Rome Statute). Only use after tribunal judgment or note as "accusation" / "alleged".
   - "War crimes" / "crimes against humanity": similarly, use as accusation not fact unless adjudicated.
   - "Terrorist": designation varies by country (US, EU, UN lists differ). Note whose list, or use "designated terrorist by X" or "militant group".
   - "Regime" vs "government": "regime" carries delegitimacy. Reserve for autocracies, mark editorial choice if used.
   - "Occupation" vs "disputed": both are loaded. Use "territory controlled by X" + history, let reader decide framing.

3. **Diplomatic protocol sensitivity**:
   - "Demarche" (formal protest) vs "informal complaint" — upgrade changes meaning; be precise.
   - "Formal note" (official document) vs "aide-mémoire" (informal record) — different standing.
   - Sanctions tier: "asset freeze" ≠ "embargo" ≠ "restricted-measures regime". Each has legal precision; translate and mark.

4. **Stringer/fixer protection**:
   - Never identify fixer by name if they are in a conflict zone or work for a minority group. Use "local contact" / "research partner" generically.
   - Disclose fixer's background (e.g., "a contact from the X community") so reader understands potential perspective.
   - If fixer is physically at risk, note this and explain why anonymity is essential, but use their information only if corroborated elsewhere.

### Step 4: Source Chain Audit (international-specific)

For **every factual claim about a foreign event**, trace the chain backward:

1. **State the claim**: "20,000 refugees crossed the border."
2. **Trace the source in material**: Where did this number come from in the supplied material?
3. **Name the source tier**: 
   - ✅ Primary: "UNHCR's border statement from [date]" (official, verifiable).
   - ⚠️ Secondary: "Reuters reported UNHCR said…" (still primary claim, but one-step removed).
   - ❌ Tertiary: "Media reports suggest…" or "Regional outlets report…" (unacceptable, cite original).
4. **Check translation**: If originally in another language, verify framing. (E.g., does the French original say "réfugiés" [refugees] or "migrants"? The word choice matters.)
5. **Flag distance chains**: "According to international media, a source in the region said…" = three layers of indirection. Mark it; don't promote it to hard fact.

In the output footer, list any claims ranked ⚠️ or ❌ under "待查證" with their chain length so editor knows what needs verification.

### Step 5: Regional Context Mapping (international addition)

Before output, ensure the piece anchors claims in:

1. **Historical precedent**: "This is the third such event since [year]" — cite the prior two.
2. **Geopolitical actor alignment**: Who benefits from this event? Make it visible why each side is responding as they are.
3. **Treaty/obligation status**: If the claim involves a breach of agreement, name the agreement and the prior compliance record.
4. **Regional parallel**: "Similar to the situation in [neighboring country]" — cite the parallel explicitly so reader sees the comparison is deliberate.

This is not editorializing; it is providing the context that lets readers understand the claim's significance.

---

## Output Format

Use the med-news-reporter base format, with these international additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 即時國際新聞 / 外交報導 / 衝突分析 / UN決議整理 / 人道新聞
**字數**: approx. XXX
**消息來源層級**: 一手官方聲明 N / 一手現場 N / 新聞通訊社 N / 二手引述 N / 匿名背景 N
**外交/衝突敏感詞彙檢核**:
- 兩岸用語: ✅ / ⚠️ (列出用語及其來源的定義方式)
- 衝突術語 (戰爭罪/種族滅絕/恐怖分子): ✅ / N/A / ⚠️ (列出升級或降級的用語)
- 佔領 vs 爭議領土: ✅ / N/A / ⚠️
**源流稽核** (Source Chain Audit):
- 距離最遠的宣稱 (farthest claim): [稱述] — 源流: [primary → secondary → ...] — 驗證狀態: [✅一手 / ⚠️二手 / ❌待查]
- 翻譯用語檢驗: ✅ / N/A / ⚠️ (列出需原文確認的政治詞彙)
- 記者/線人保護: ✅ / N/A / ⚠️ (列出未充分匿名的風險)
**區域脈絡補全**:
- 歷史前例: ✅ / N/A / ⚠️ (列出提及但未標源的歷史平行)
- 地緣政治利益方: ✅ / ⚠️ (列出受事件影響的各方)
- 條約/義務基礎: ✅ / N/A / ⚠️
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

### Good Example

**Scenario:** User supplies (a) official UN OCHA situation report on cross-border refugee flow from Region A, with date/UNHCR figure of 47,500 internally displaced + 12,000 crossed border; (b) Reuters article citing UNHCR and naming the field coordinator; (c) translated statement from the Region A government (original in Arabic, user provides English translation); (d) testimony from a diaspora-run NGO; (e) brief note: "fixer on the ground is from the Region B minority, has relatives in Region A".

**Analysis:**

1. Step 1: classified as **humanitarian/conflict-adjacent** (population movement, not active military ops).
2. Step 2: source chain audit — UNHCR figure is primary ✅, Reuters cite of UNHCR is secondary (acceptable if transparent) ⚠️, diaspora NGO is advocacy source ⚠️, government statement is primary but translated ⚠️.
3. Step 3: sensitivity check — the fixer is from a minority that may be on one side of the conflict. Must disclose this in the piece ("contacts from Region B provided on-the-ground perspective") without naming the fixer.
4. Step 4: translate the Arabic statement — does "إزاحة" mean "displacement" or "uprooting"? Check original; note if the Arabic framing is stronger/weaker.
5. Step 5: context mapping — "This is the second major displacement in the region in 18 months; prior displacement in [date] crossed [number]. Regional treaty X (signed [year]) requires signatory nations to grant asylum; [Country] has historically [accepted/rejected] such flows."

Result: piece cites UNHCR directly, transparently layers Reuters reporting, discloses diaspora-NGO perspective, notes fixer background, re-checks translation, anchors in regional history. Reader can recalibrate claim credibility.

### Bad Example

**Scenario:** Same input. Writer (a) cites "47,500 internally displaced per media reports" without naming UNHCR or Reuters, (b) quotes government statement without noting it was translated or checking original framing, (c) includes diaspora-NGO statistics as if they were official, (d) mentions fixer's on-the-ground perspective without disclosing fixer is from Region B minority and thus may have perspective bias, (e) does not anchor refugee flow in prior flows or treaty obligations, (f) uses "occupation of Region A" framing without noting this is contested terminology.

**What went wrong:**
- (a) Obscuring source chain ("media reports") hides that the figure is official (UNHCR), reader cannot recalibrate.
- (b) Unverified translation: if the original said something politically different, reader won't know.
- (c) Treating NGO statistics as official blurs advocacy and fact.
- (d) Undisclosed fixer bias is a classic conflict-reporting failure; reader cannot account for perspective.
- (e) Missing historical anchor makes the flow seem unprecedented when it is pattern (Iron Law violation: distance makes verification even more critical).
- (f) Using "occupation" without noting this is contested means the writer chose a frame for the reader without transparency.

Net: each error individually might pass a basic fact-check, but cumulatively the piece pushes the reader toward one side's framing without revealing the editorial choices. Iron Law violation: distance + translation + fixer + framing = chain where authority is inflated.

---

## Gotchas

- **"據國際媒體報導" 是藏匿源流的港口**: "International media reports" obscures whether it's an official statement relayed by Reuters (primary-source-tier), or one outlet citing another outlet (tertiary). Name the source tier. If you only have "multiple outlets reported this", flag it as consensus-not-fact and cite one outlet specifically.
- **翻譯不只是換字,也換政治框架**: 中文的「政府」vs 英文的 "regime", 或阿拉伯文的「إزاحة」(uprooting) vs 英文的 "displacement" 帶著不同政治色彩。翻譯完成後,一律回查原文確認政治詞彙是否升級/降級。無原文則標 `[翻譯來源待確認]`。
- **匿名的線人比名字的線人風險更高**: 線人身份保護是對的,但匿名線人的政治立場對編輯台必須透明("一位來自 X 社群的在地接觸人")。如果線人來自衝突某一方,這個背景應該在編輯台記錄,即使不公開。如果線人未充分保護(可被當地反對勢力識別),不應使用其信息。
- **「據聯合國報告」 ≠ 聯合國官方立場**: UN OCHA 報告是事實回報;UN 大會決議是成員國投票;UN 秘書長聲明是秘書長個人立場。三者混為一談會誤導讀者對聯合國一致性的認知。引述時必須區分。
- **制裁/禁運 / 資產凍結各有法律意涵**: "sanction" 在不同脈絡意涵不同(美國清單 vs EU 清單 vs UN 清單)。必須標明「根據 X 清單的制裁」。"embargo" 與 "asset freeze" 與 "restricted measure" 各有具體法律定義;翻譯時易模糊。
- **「佔領」vs 「爭議領土」vs 「控制」的選詞都是框架**: 不同國家對同一片領土的稱呼不同。使用 "territory controlled by X" 加歷史脈絡讓讀者自判,不應單邊用 "occupied" 或 "disputed" 除非該用語是報導對象的官方立場(若是,則註明來源)。
- **戰爭罪 / 反人類罪 / 種族滅絕的使用必須極度謹慎**: 這些是羅馬規約定義的法律術語,只有國際法庭判決才能確認。新聞報導應使用「指控」「涉嫌」「據指控」,不可升級為既成事實除非判決已出。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 國際消息來源 (UN, WHO, IMF, 各國外交部、駐外使館、新聞通訊社、國際NGO) 、線人安全 | Step 2 source vetting |
| `references/glossary.md` | 外交與國際關係術語對照與敏感詞彙 (雙邊vs多邊、條約vs協定vs MOU、demarche、外交豁免) | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 戰地報導安全、衝突方平衡原則、人道主義原則、線人保護、兩岸用語敏感度、戰爭罪/反人類罪用語審慎度 | Step 3 risk check |
| `references/regional_briefings.md` | 台海、印太、歐盟、中東、非洲、拉美各區域的關鍵 stakeholder 與必讀來源 | Regional context anchoring |
| `references/translation_and_attribution.md` | 翻譯陷阱、透過二手媒體 vs 一手接觸、跨時差日期標示、地名/人名標準化 | Step 4-5 source chain & translation checks |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-political` — for domestic political stories with international dimension
- `med-business` — for international business/market/investment news
- `hum-source-criticism` — deeper source-vetting frameworks
- `hum-ethics` — moral-framework reasoning on conflicts / human rights

---

## Limitations

- **Does not perform live fact verification**: this skill flags claims that need verification; it does not access live UN databases, government press releases, or cross-reference against current news archives. Editor must verify or supply.
- **Geopolitical context is time-sensitive**: regional alignments, treaty obligations, and sanction lists change. Always verify against current primary sources (UN, State Dept, EU EEAS, MOFA) before publishing.
- **Does not generate original on-the-ground reporting**: if the supplied material lacks in-country sources, this skill flags the gap — it will not find fixers or conduct interviews.
- **Translator bias**: even with translation-layer checking, a translator's choice of words influences framing. When high-stakes political language is involved, original-language review by a native speaker is mandatory.
- **Fixer safety is a judgment call, not a formula**: this skill guides disclosure and protection; it does not replace on-the-ground risk assessment by editors and fixers themselves.
