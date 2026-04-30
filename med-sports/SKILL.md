---
name: "med-sports"
description: "Use when the user wants to write a sports news piece — game recaps, athlete profiles, league/rule changes, injury reports, trade announcements, doping/discipline coverage — from supplied material (box scores, interviews, official statements, stats, medical updates). Specializes med-news-reporter for the sports beat: era-adjusted stats, source vetting for sports data, medical/injury disclosure limits, athlete-as-public-figure doctrine, doping allegations vs. allegations, sports-betting sensitivity, and on-field performance ≠ off-field authority. Triggers on phrases like 'write up this game', 'turn into a sports feature', 'cover this athlete trade', 'draft a piece on this injury', '寫一篇 MLB 賽季報導', '整理 NBA 交易消息', '寫一篇選手專訪', 'draft an Olympic piece', '報導棒球禁賽風波'. Do NOT use for fantasy sports tips (use fin-*), gambling advice, team marketing/press releases (use pr-*), or player agents' PR (use pr-press-release)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "sports-news", "athletics", "media-ethics", "sports-governance"]
---

# Sports News Reporting

> **This skill specializes med-news-reporter for the sports beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **sports-beat-specific** discipline on top.

## Overview

Distilled from sports-journalism curricula at Ohio University Scripps, Northwestern Medill, University of Missouri, Arizona State Cronkite, University of Florida, and curricula in athletic governance (CPBL, NBA, IOC, WADA CAS procedures). Covers five main sports-news sub-types: **game/event coverage / athlete profile / league governance / injury/discipline / trade/transaction**.

```
IRON LAW: On-Field Performance ≠ Off-Field Authority

A player's elite on-court statistics are news; the same player's political
opinions, business endorsements, or social claims receive the same source-
vetting and attribution standards as any quoted figure. Do not treat
athletic celebrity as a free pass for unverified off-field claims, and do
not smuggle off-field judgments via on-field framing ("the controversial
striker scored twice" conflates sports fact with off-field stance). Separate
the performance data (verifiable, time-stamped, era-adjusted) from the claim
about what they meant or who they are off the field (requires the same rigor
as any other quoted figure's statement). When stats are accurate but used
to make a character claim, flag it.

Default LLM behavior is to assume athletic fame carries credibility across
domains. Override that assumption explicitly per subject.
```

Why this is non-obvious: sports readers are accustomed to athlete-celebrity conflation in tabloid press. Professional sports journalism must separate statistical fact from interpretive claim — especially when an athlete's behavior (kneeling, endorsement, political statement) is described alongside their game performance. The framing "activist star backhands a critic and scores twice" treats on-field dominance as authority for off-field views. This is the failure mode the Iron Law exists to catch.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "The player is famous, so their off-field opinion is newsworthy" | Fame in one domain (athletics) does not confer authority in another (politics, medicine, social policy). Quote them as an athlete-who-happens-to-comment, not as an expert. Verify claims independently. |
| "The coach said it, so it's coaching wisdom, not opinion" | Post-game soundbites are still attributed utterances, not facts. "Coach said X beats Y" ≠ "X beats Y". |
| "These stats prove the athlete is the 'best ever'" — followed by character praise | Stats without era-adjustment and comparable sample size can mislead. "Best ever" requires evidence, not just dominance in a single season or league. Always cite the era and sample. |
| "The injury report is from the team, so it's official" | Team injury reports are PR-filtered. Formal medical disclosures differ from "player is healthy and ready". Cross-check with league medical protocols if significant claim. |
| "The doping allegation is trending on social media / a prominent figure tweeted it" | Unsubstantiated doping allegations are defamatory. Use "allegation", "alleged", "claimed to have violated" (not "is a drug cheat"). Wait for WADA/CAS adjudication or corroboration. |
| "This player's controversial personal life is part of their public story" | Athletes have reasonable privacy expectation for family, mental health, medical info. Distinguish between public acts (on-field, on-camera, tournament) and private life (unless directly relevant to job performance or self-disclosed). |
| "The betting line shows this game is close, so I'll cite it as odds context" | Don't cite sports-betting lines as news sources or "neutral" metrics. Betting companies have financial interest in narrative and line movement. If the story is about betting, disclose the financial relationship. |

---

## When to Use

**Trigger conditions:**
- User supplies sports material — box scores, game transcripts, interview clips, injury updates, rule changes, trade announcements, athlete statements — and asks for a news piece.
- User asks for "game recap", "sports feature", "athlete profile", "league news", "injury report", "trade coverage", "Olympic coverage", or similar.
- User paraphrases: "寫一篇 MLB 賽季報導", "整理 NBA 交易消息", "把這場球寫成新聞稿", "cover this Olympic moment", "draft a piece on this coach's hiring", "寫一篇選手專訪".

**Input signals:**
- Named athletes, coaches, teams, leagues, games, events, statistics, medical/injury statements.
- Direct quotes from players, coaches, officials, or league representatives.
- Box scores, records, stats, rankings, era context.

**When NOT to use:**
- Gambling/fantasy sports tips (use fin-*; sports betting is a different regulatory domain).
- Team or league marketing material, official promotional content → use `pr-press-release` or `mkt-sports-content`.
- Player agent PR release → use `pr-press-release`.
- Athletic instruction / coaching how-to → use tech-* or domain-specific skill.
- Pure sports business / corporate strategy (M&A, sponsorship deals) → use `biz-*` or `fin-*` (unless the story is "league governing body did X").

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds sports-specific Step 7 (Stats Provenance & Performance-Authority Audit).

### Step 1: Classify the sports-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Game/event coverage** | Box score, play-by-play, result, player/team performance | Accuracy of stats; era context; avoiding "greatest ever" without qualification |
| **Athlete profile** | Life story, career arc, personality, off-field interests | Distinction between on-field fact and off-field opinion; privacy boundary; consent for personal details |
| **League governance** | Rule change, expansion, labor/CBA, discipline case, playoff format | Official decision source; stakeholder positions (players union, owners, athletes); implementation timeline |
| **Injury/medical** | Player health status, return timeline, surgery, mental health disclosure | Medical privacy law; team vs. public info; degree of disclosure propriety; player consent |
| **Trade/transaction** | Player signed, traded, released, drafted, retired | Contract/deal terms source; bidding competition (if reported); player statement; team official statement |

If the material spans sub-types (e.g. "star player traded due to injury"), classify by the **primary news driver**.

### Step 2: Source vetting & sports-data-specific discipline

**Every statistic or "first time since X" claim must carry provenance:**

- ❌ "The best shooting season in franchise history"
- ✅ "The best 3-point percentage (.485) in the franchise's 25-year history, according to Basketball-Reference and the team's official records, as of 2026"
- ✅ When era matters: "The 0.310 batting average is below his career .320 mark but above the league average of .268 in 2026" (explicit era context)

**Source tier tagging** (extends med-news-reporter's tiering with sports-specific tiers):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Official league record** | Box scores (NBA.com, MLB.com, CPBL, official league stats), rule book, official standings | Direct citation; note source entity |
| **Third-party verified database** | Baseball-Reference, Basketball-Reference, Sports-Reference, ESPN Stats, PFF (for NFL) | Cite source; note version/update date if material |
| **Team official statement** | Coach quote, team press release, official injury report | Quote directly; label as team-sourced; note any PR filtering |
| **Athlete on-record quote** | Post-game interview, press conference, official statement | Direct quote per med-news-reporter; distinguish from off-hand comment or social media |
| **Analyst / commentator opinion** | Ex-player analysis, sports journalist prediction, coach speculation | Label as analysis/opinion; do not treat as fact |
| **Social media / fan / rumor** | Athlete tweet, player agent leak, beat reporter speculation | Unusable until corroborated; or explicitly flagged as "unconfirmed report" if novel and newsworthy |

### Step 3: Sports-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **禁藥和紀律指控 (Doping/Discipline Allegations)**:
   - Until WADA/CAS adjudication or formal league charge is filed, use "涉嫌違規" (alleged to have violated) / "藥檢呈陽性" (tested positive, if announced) — NOT "使用禁藥" (uses banned drugs / is a drug cheat). The first is fact; the second presumes guilt.
   - Include investigation timeline: "pending CAS review" / "awaiting formal hearing" / "under independent investigation".
   - Distinguish between player suspension (league imposed) and medical suspension (injury/testing recovery) in headlines.

2. **傷停資訊與醫療揭露**:
   - Official team statement vs. player-disclosed medical info have different legal weights. Team says "day-to-day" (PR-standard); player says "tore ACL" (medical info they volunteered).
   - Do not speculate on severity or recovery timeline beyond what is officially stated or player-disclosed.
   - Mental health / substance abuse disclosures: treated as medical information with high privacy expectation unless the athlete self-disclosed publicly.

3. **球員私生活邊界**:
   - Athletes are public figures in on-field domain. Off-field: family details, medical conditions, relationship status, sexuality, religious beliefs — require newsworthiness threshold (public act, athlete's own disclosure, or legitimate performance impact).
   - Minors (family members under 18): special protection; do not identify or disclose information without explicit consent.

4. **賭盤相關敏感性 (Sports Betting Disclosure)**:
   - Do not cite sportsbook odds/lines as "neutral" context or data source. If the story is about betting, disclose the financial interest of betting companies.
   - Allegations of match-fixing / game-rigging: high burden of proof. Use "alleged" until adjudicated. Source must be law enforcement, formal investigation, or credible multi-party corroboration.
   - Player-betting-on-own-sport is a conflict; distinguish from coverage of legal sports betting market (which is news, but disclose its financial/reputational stake).

5. **국제경기 & 올림픽 규정**:
   - Olympic eligibility, IOC sanction status, national federation approval — cite rule source and athlete's current eligibility status.
   - Host country / geopolitical tensions: report neutrally; do not conflate athlete's national identity with political conflict unless explicitly stated by athlete/federation.

### Step 4: Stats Provenance Audit (sports-specific addition)

Before output, sweep the draft for:

1. **"Greatest" / "first" / "only" / "unprecedented" superlatives**: every such claim must cite:
   - The database/source searched (e.g., "according to Baseball-Reference", "per official Olympic records")
   - The scope (e.g., "in franchise history", "since league's 1990 founding", "in this tournament")
   - The era (e.g., "in the shot-clock era" [NBA since 1985], "post-three-point-line adoption" [MLB/baseball comparisons across eras need rule context])
   - Sample size / context (e.g., "in 50+ games", "over a full season, not mid-season pace")

2. **Comparison audit**: 
   - Cross-era comparisons (1980s vs. 2026) require era-adjustment context: rule changes, league expansion, training medicine, analytics adoption, salary cap effects.
   - Cross-league comparisons (MLB vs. NPB, NBA vs. EuroLeague): note league size, competition level, sample differences.
   - ❌ "5 home runs in 10 games is unprecedented" (without era: in which league? which era? which level of play?)
   - ✅ "5 home runs in 10 games is the fastest-ever pace for a debut-season player in CPBL history (since 1990), though early-season pace often regresses over a full season".

3. **Injury-timeline realism**: medical claims should not exceed evidence:
   - ❌ "He'll return in 4 weeks" (without medical source; is this team speculation or team medical staff statement?)
   - ✅ "The team said the player would return in 4 weeks; he ruptured his ACL in the 2nd quarter" (distinguishes team timeline from confirmed injury fact).

4. **Performance-vs.-Context**: 
   - A .350 batting average is a fact; saying it "proves he's the best hitter" requires comparison and era context.
   - If the narrative suggests off-field conclusions (maturity, leadership, mental toughness) from on-field stats, flag it: these are interpretations, not facts.

---

## Output Format

Use the med-news-reporter base format, with these sports additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 即時賽事 / 運動員專訪 / 轉隊消息 / 傷停更新 / 聯盟治理
**字數**: approx. XXX
**消息來源層級**: 官方記錄 N / 隊方 N / 運動員本人 N / 分析評論 N / 民間謠傳 N
**統計數據稽核**:
- 「最佳 / 首次 / 從未」superlatives: ✅ / ⚠️ (列出未限定範圍的)
- 跨時代比較: ✅ / N/A / ⚠️ (列出未加註 era 或規則背景的)
- 跨聯盟比較: ✅ / N/A / ⚠️ (列出未加註聯盟差異的)
**醫療 / 紀律敏感項目**:
- 禁藥指控: ✅ (使用「涉嫌」) / N/A / ⚠️ (列出標籤誤用)
- 傷停資訊來源: ✅ (官方) / ⚠️ (球隊 PR / 推測分開呈現)
- 球員私生活邊界: ✅ / ⚠️ (列出可能越界的細節)
- 賭盤相關: N/A / ⚠️ (若提及,是否揭露財務利益)
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Gotchas

- **禁藥指控前未等 WADA 決議就寫成定論**: WADA/CAS 程序可能耗時 2-4 年。案件未審結前,一律用「涉嫌違反反禁藥規則」「藥檢呈陽性,待進一步檢驗」,不可寫「使用禁藥」或「是禁藥使用者」。這是誹謗線。
- **「跨時代最佳」沒有 era 背景就是誤導**: NBA 三分線距離改過、MLB 球的彈性歷年不同、打擊率通膨與通縮週期不同。同樣的數字在不同 era 意義相差 20-30%。「歷史最佳打擊率」必須明確說:相對於該 era 的聯盟平均與同期水準。
- **球隊 PR 與教練氣話區分**: 球隊發出的「球員狀態絕佳、已準備上場」是 PR。教練賽後 5 分鐘內的火氣發言(「對手犯規被吹漏掉,這判決糟糕透頂」)通常隔天被冷卻。用「賽後激動表示」而非「強烈抨擊」,並註記時間點。
- **球員私生活 / 家庭不是自動公眾人物素材**: 即使球員是名星,未成年家族成員、离婚細節、精神健康狀況有合理隱私期待。除非球員自己公開或直接影響場上表現,否則不應成為報導。
- **跨聯盟「只有 X 曾在球隊 Y 時期做過」的說法需查證多數據庫**: 有時一個數據庫漏掉某隊歷史(尤其小聯盟、海外聯賽)。用多數據庫交叉檢查。
- **未成年運動員的報導特殊保護**: 高中青少棒選手需依兒少法保護;不可揭露身分細節 / 就讀學校名稱(除非家長或本人明示同意)。
- **「球賽預測」與「分析」是不同的來源**: 前者是賭盤導向的猜測;後者是基於已知數據的專家評估。不可混淆,也不能把賭盤當作「市場共識」的代理。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 體育新聞消息來源、國際聯盟與數據庫、台灣體育治理機構 | Step 2 source vetting |
| `references/glossary.md` | 體育統計術語、計算公式、跨聯盟術語對照 (ERA/WHIP、TS%/PER、打擊率/上壘率) | When unfamiliar sports terminology appears |
| `references/ethics_and_law.md` | 球員隱私 / 醫療揭露、禁藥程序、兒少法保護、賭盤敏感性、未成年運動員 | Step 3 risk check |
| `references/sports_data_reading.md` | 進階數據 vs. 傳統數據、sample size、era-adjusted 比較、樣本不足陷阱 | Step 4 Stats Provenance Audit |
| `references/sports_governance.md` | 各聯盟治理結構 (CPBL, MLB, NBA, IOC)、勞資協議、選秀規則、轉隊規則 | When covering league/governance stories |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-business` — for sports business / corporate strategy stories (sponsorship, broadcasting rights, franchise valuation)
- `stat-hypothesis-testing` — for statistical claims and era-adjustment rigor
- `hum-source-criticism` — for deeper vetting of sports-data sources and databases

---

## Limitations

- **Does not verify live athletic performances**: this skill flags statistical claims and sources; it does not watch games or verify play-by-play accuracy. Rely on official league box scores and third-party databases.
- **Medical expertise scope**: this skill notes disclosure limits and privacy considerations; it does not make medical judgments. For injury prognosis or medical claims, consult sports-medicine sources or sports-medicine literature.
- **League-specific rules**: CPBL rules, MLB rules, NBA rules, IOC rules differ. This skill notes when to cite rule sources; it does not encode every league's rulebook. Always cite the governing body.
- **Doping adjudication**: WADA/CAS procedures are complex and multi-year. This skill teaches terminology discipline ("alleged" vs. "convicted"), but does not predict case outcomes or legal strategy. Cite case status only as formally announced.
- **Betting regulation**: sports betting is heavily regulated (Taiwan運彩, MLB/NBA licensing, UK Gambling Commission, etc.). This skill notes conflict-of-interest and disclosure requirements; it does not provide betting-law advice. When reporting on betting-related stories, consult legal counsel on disclosure obligations.

