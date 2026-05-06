---
name: "med-business"
description: "Use when writing financial news — earnings, IPO/M&A, regulatory changes, industry trends — from transcripts, filings, or investor materials. Activates business-beat workflow: financial-figure provenance, analyst-stake disclosure, securities-law risk, and number stewardship. Triggers on '寫一篇財報季報導', '分析這份財報', '整理 IPO 新聞', 'turn earnings call into a piece', 'write up M&A announcement'. Defers general craft to med-news-reporter. Do NOT use for press releases (pr-press-release), investment advice (fin-investment-thesis), or marketing (mkt-*)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "business-news", "finance-news", "earnings", "financial-reporting"]
---

# Business & Finance News Reporting

> **This skill specializes med-news-reporter for the business beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **business-beat-specific** discipline on top.

## Overview

Distilled from financial-journalism curricula at NCCU 新聞系、NTU 新聞研究所、Columbia Journalism Review (Business Desk), Medill (Business Journalism), CUNY Newmark, Reuters Institute. Covers the four main business-news sub-types: **earnings / IPO-M&A / regulatory-policy / industry-trend** reporting. Core mandate: every financial figure must trace to base period, scope (consolidated vs standalone; domestic vs group), source (CFO statement / 公開資訊觀測站 / analyst estimate), and confidence level (audited vs preliminary vs forecast). The non-obvious failure is when the literal number is correct but the missing context lets readers compare apples-to-oranges.

```
IRON LAW: Numbers Need Stewardship

Every financial figure in the piece — revenue, EPS, growth rate, margin,
valuation multiple — must explicitly carry FOUR metadata tags: (a) BASE
PERIOD / FISCAL YEAR (e.g., "113年度合併報表"), (b) SCOPE (consolidated
vs individual; domestic vs group; operating vs including-financial gains),
(c) SOURCE (CFO statement / 公開資訊觀測站 / analyst consensus / research
report), and (d) CONFIDENCE (audited / preliminary / forward-looking).
Without all four, the figure is marked [待查證] or omitted. Default LLM
behavior is to drop context for "cleaner prose" or assume implied scope
— this suppresses that default by requiring explicit stewardship. The
reader cannot infer scope from a number alone; ambiguity is not efficiency.
```

Why this is non-obvious: a headline "Company posts record 5B EPS" is technically true (audited, consolidated, 2025 FY) but sounds miraculous without the context that it's 50% higher than last year due to a one-time merger gain, not operating performance. When readers hear "record EPS", they assume baseline comparable operating earnings — a fundamental mismatch. Stewardship audit catches this by forcing every number to carry its scope flags.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "EPS growth was 30%, that's the key number, we don't need to explain consolidated vs individual" | Scope ambiguity is the #1 source of misleading financial journalism. The reported-to-media EPS (often consolidated, including one-time items) differs from operating EPS. Both numbers are "true"; omitting the qualifier lets readers confuse them. |
| "The press release says 營收成長 15%, I'll use that without checking if it's year-over-year or 2-year stack" | Base-period ambiguity is a gotcha. Always verify: Is 15% versus prior-year Q2 or full year? Is the comparison to 113年同期 or 累計? Mismatched bases are the #2 error. |
| "Analyst estimates are just opinions, not facts, so I can soften them as 'expected' instead of marking them as forecasts" | Analyst consensus is market material — forecast signals must be clearly marked as such. When you write 'expected to grow', readers hear 'will grow'. Use 'X firm projects' / 'consensus estimate' to signal uncertainty. |
| "The company's 本益比 of 12 is reasonable, so I can describe it as 'fairly valued' " | 本益比 is a metric, not a judgment. "Fairly valued" requires comparison to peer multiple, historical average, or growth rate context. The bare number 12× is incomplete. Omit judgment or add comparison. |
| "I'll round the margin from 24.3% to 'about 24%' for readability" | Rounding financial figures obscures precision. Use the reported number or mark as [estimated]. Readers trust journalists with numbers; small rounding is still fabrication. |
| "Market cap of 2.5T NT$ is big, readers don't need to know the share price and shares outstanding" | Implied scope: are we talking market cap at close? Intra-day? Converted at what exchange rate if international? Stating the date and share price (+count) lets readers verify and understand concentration risk. |

---

## When to Use

**Trigger conditions:**
- User supplies financial material — 財報新聞、法說會逐字稿、公開說明書、投資人簡報、SEC EDGAR filing、IPO 招股書、重大訊息、併購公告 — and asks for a news piece.
- User asks for "財報季報導" / "IPO 新聞" / "併購分析" / "監理解讀" / "產業趨勢報導" / "earnings story" / "M&A coverage" / "regulatory impact piece".
- User paraphrases: "把這份財報做成新聞", "法說會怎麼寫", "SEC filing 有什麼亮點", "整理成市場分析", "寫一篇產業動向".

**Input signals:**
- Named companies, financial metrics (revenue, EPS, margin, P/E, ROA, EBITDA), fiscal periods, accounting bases.
- Earnings transcripts, investor presentations, regulatory filings, 公開資訊觀測站 announcements, analyst reports.
- Direct quotes from CFO, investor-relations staff, analysts, regulators.

**When NOT to use:**
- Company press release in the company's own voice → use `pr-press-release`.
- Investment thesis or buy/sell recommendation → use `fin-investment-thesis`.
- Marketing copy promoting a stock / fund / investment product → use `mkt-*`.
- General economic news without company-specific angle → use `med-news-reporter` (not this beat).

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds a business-specific Step 4 (Number Provenance Audit).

### Step 1: Classify the business-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Earnings / quarterly results** | Fiscal quarter/year, 財報季, revenue/EPS/margin metrics, guidance, CFO commentary | Revenue scope (consolidated?); one-time items segregation; YoY/QoQ base-period clarity; FX impact disclosure |
| **IPO / M&A** | Initial public offering, merger, acquisition, spin-off, share buyback, capital raise | Valuation methodology; deal structure (all-stock / cash / mixed); regulatory approval status; pro-forma scope |
| **Regulatory / policy** | 金管會公告、央行決議、證交法修訂、會計準則變更、監管罰款 | Regulatory text source; impact on multiple companies or industry-wide; timeline for enforcement |
| **Industry trend** | Market shifts, competitor moves, supply-chain changes, sector rotation, technology disruption | Competitive positioning; addressable-market context; historical parallel (if claimed cyclical) |

If material spans sub-types (e.g., an earnings call with M&A announcement), classify by the **primary news driver**.

### Step 2: Source vetting & financial credibility

**Every number must carry four metadata flags:**

1. **Base period** — "113 年度" / "113 年 Q2" / "累計 1-6 月" / "2026 財年" (date ambiguity kills credibility)
2. **Scope** — 合併報表(consolidated) vs 個體/個別(individual); 國內(domestic) vs 國際(international); 持續營業(operating) vs including 停業部門; 經常(operating income) vs including 業外(non-operating/financial gains)
3. **Source** — CFO statement (audited) / 公開資訊觀測站 preliminary / analyst consensus / research firm estimate / internal forecast
4. **Confidence** — 已審定(audited) / 未審(unaudited) / 初步(preliminary) / 預估/展望(forward-looking, include risk disclaimer)

**Source tier tagging** (extends med-news-reporter's tiering with financial-specific tiers):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Official disclosure** | 公開資訊觀測站, SEC EDGAR, company-filed 年報/季報, CFO statement | Direct citation; audited flag clearly marked |
| **Investor-facing material** | Earnings transcript, investor presentation, guidance, earnings call Q&A | Label as "company guidance" / "CFO stated"; distinguish from audit attestation |
| **Research / analyst** | Sell-side reports, consensus estimates, analyst downgrades | Always disclose analyst's firm name, rating (buy/hold/sell), if stock held. State "consensus estimates" if multiple firms |
| **Market data** | Price, trading volume, index levels, analyst-consensus tickers | Timestamp (close vs intra-day), exchange-rate basis if international |
| **Second-hand media** | News relay, competitor claims about the target | Requires cross-check with primary source before using |

### Step 3: Business-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **內線交易 / 市場操縱** (證交法 §155, §157-1):
   - 重大訊息 publication timing: 公開資訊觀測站 timestamp, not press-release timing. If material info disclosed before 公開資訊觀測站 publication, that is non-public — reporting it may expose risk.
   - Embargo rules: some companies embargo financial information until official release time; publishing early can expose the reporter to liability.

2. **會計舞弊紅旗** — watch for:
   - Revenue recognition shifting (e.g., quarter-end channel-stuffing, sales to related parties, side agreements)
   - Margin compression with no explanation (could signal pricing power loss or cost hiding)
   - Huge accounts-receivable growth without revenue growth (cash-flow risk)
   - One-time items that repeat (no longer "one-time"; operating deterioration masked)
   - Related-party transaction spike (transfer pricing risk)

3. **估值斷言需避免** — never write:
   - ❌ "The stock is fairly/overvalued at 12× P/E" (requires multiple-comparison context)
   - ❌ "Company is worth 100B" (absent valuation method disclosure)
   - ✅ "Stock trades at 12× P/E vs peer median 18×, suggesting discount or slower growth"

4. **匯率影響揭露** — when international revenue/EPS is cited:
   - Always state currency basis. If reporting "EPS $2.50 USD", note if converted at spot or fixed rate.
   - When Y-o-Y comparisons span periods with different FX rates, disclose FX headwind/tailwind separately from operating impact.

5. **重大訊息揭露合規**:
   - 公開資訊觀測站 公告 = 官方發布 — use as primary source.
   - 公司新聞稿 ≠ 公開資訊觀測站 公告 — they can have different timestamps and scopes.
   - Report based on 公開資訊觀測站 timestamp + regulatory-filing scope, not company PR spin.

### Step 4: Number Provenance Audit (business-specific addition)

For **every** financial figure in the draft:

1. **Trace to source material** — find the exact line in the earnings transcript, filing, or 公開資訊觀測站 announcement.
2. **Tag base period** — write the fiscal year/quarter in parentheses: "營收 100 億 (113年度)", not just "營收 100 億".
3. **Declare scope** — if the figure is consolidated, write it; if it's guidance, mark "展望". If unusual (e.g., pro-forma), say so.
4. **Check for one-time items** — if EPS or margin is boosted by a gain, segregate: "Operating EPS $1.20, including $0.30 one-time merger gain".
5. **Validate comparisons** — if claiming "grew 15%", verify: versus what base year/quarter? Same period last year or trailing-twelve-months? Same scope?

---

## Output Format

Use the med-news-reporter base format, with these business-beat additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 財報季報導 / IPO新聞 / 併購分析 / 監理解讀 / 產業趨勢
**字數**: approx. XXX
**消息來源層級**: 公開資訊觀測站 N / 財報/法說會 N / 分析師 N / 媒體轉述 N
**財務數字稽核**:
- 基期 (fiscal year/quarter) 完整性: ✅ / ⚠️ (列出未標的數字)
- 範圍 (consolidated/individual, operating/including one-time) 清晰: ✅ / ⚠️ (列出未指明的)
- 來源與可信度 (audited/preliminary/forecast) 標記: ✅ / ⚠️ (列出未確認的)
- 匯率基準 (if applicable): ✅ / N/A / ⚠️
- 一次性項目隔離: ✅ / N/A / ⚠️ (如有列出影響幅度)
**分析師利益揭露**: ✅ (列出所有分析師所屬機構 + 評級) / N/A / ⚠️
**會計舞弊紅旗檢查**: ✅ / ⚠️ (列出可疑項目)
**估值斷言**: ✅ (無不當斷言) / ⚠️ (列出待補充比較基準的)
**證交法合規檢查**:
- 重大訊息揭露時點 (公開資訊觀測站 vs 新聞稿時差): ✅ / ⚠️
- 內線交易風險: ✅ / ⚠️ (列出可疑之處)
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

### Good Example

**Scenario:** User supplies (a) 103 Tech Corp 113年度年報 & 法說會逐字稿 (audited consolidated statement); (b) 公開資訊觀測站 重大訊息 (published 2026-04-15 12:30); (c) two sell-side analyst reports (one "buy" rated, one "neutral", both from top-3 brokers, with latest price targets); (d) peer comparison from Bloomberg (P/E multiples of 5 competitors). Request: ~1,000-word earnings story analyzing the year, growth drivers, and valuation context.

**Analysis:**

1. Step 1: classified as **earnings reporting** (annual results with guidance implications) → focus on revenue scope, margin one-time segregation, YoY base-period clarity.
2. Step 2: Source vetting — 年報 is audited (Tier 1, 已審定); 法說會逐字稿 is investor-facing (Tier 1, 來自公司); analyst reports are Tier 2 (include firm name + rating); Bloomberg is market data (Tier 1, 時間戳記重要).
3. Step 3: Risk check — examine revenue for related-party sales spike; check if guidance has side agreements or channel-stuffing patterns; look for margin compression signals.
4. Step 4 (Number Audit):
   - "營收 500 億" → write "113年度合併營收 500 億元,同期 112年度 450 億,年成長 11.1%"
   - "EPS 2.50 元" → write "基本每股盈餘 2.50 元 (113年度,已審定);其中包括業外投資收益 0.30 元"
   - "預估今年成長 8%" → write "公司展望 114 年營收成長 8% (保守估計,面臨匯率與原料成本變數)"
   - Peer comparison: "本益比 15× vs 同業平均 18× … 反映市場對成長率的差異評估"
5. Output footer标示数字完整性 ✅, 分析师利益揭露 (两名分析师名字+评级+机构), 无会计舞弊信号 ✅, 估值对标完备 ✅.

**Result:** 读者可独立验证每个数字的基期、范围、来源;可区分运营增长 vs 一次性收益;可理解分析师评级背后的利益关系。

### Bad Example

**Scenario:** Same input material. Writer produces a "rosy" story by (a) stating "103 Tech posts record 500B revenue" without mentioning it's consolidated and includes a one-time acquisition; (b) claiming "EPS 2.50 is strong growth" without checking it includes a 0.30 one-time item (actual operating EPS only 2.20); (c) citing one analyst's "buy" rating as justification that stock is "undervalued" without disclosing the analyst owns 5% of the firm and has conflicts; (d) stating "P/E of 15 is attractive" without peer comparison; (e) omitting the 4-day gap between 公開資訊觀測站 publication and company press release.

**What went wrong:**

- (a) & (b): Scope ambiguity and one-time masking. Both the 500B and 2.50 EPS are literally true, but reader confuses operating performance with windfall gains. Iron Law violation: missing stewardship metadata.
- (c): Analyst conflict undisclosed. If the analyst's firm holds stock, that holding shapes the rating; reader needs to know. Same if the analyst is compensated by deal fees.
- (d): Valuation without context. "Attractive" requires comparison. 15× versus 18× peer average tells one story; versus 12× historical average tells another.
- (e): Timing gap ignored. If company disclosed in 公開資訊觀測站 on day X and press release on day X+4, and the reporter relied on the press release without noting the official disclosure timestamp, readers misunderstand what counts as "material" information.

**Net effect:** Story reads fluent and "positive", but every number is decontextualized. Readers cannot independently assess the company's actual operating performance vs. one-time boosts, or evaluate analyst credibility. This is the failure mode the Stewardship Audit exists to catch.

---

## Gotchas

- **「同期」「同比」「年增」的基期容易混** — 「113年度營收同比成長 10%」vs 「113年第2季同比成長」— 前者是 vs 112年度全年,後者是 vs 112年 Q2。永遠寫清楚對比期間,不要假設讀者能推斷。混淆基期是財經新聞最常見的欺騙(刻意或無意)。
- **「合併」「個體」帳目數字不可混用** — 某些公司個體淨利 50 億,合併報表淨利 80 億(因子公司貢獻)。若文中既引個體又引合併而未說明,讀者會混淆。始終聲明你用的是哪一份,尤其跨段落引數字時。
- **分析師評級「都有利益關係」,必須揭露** — 「某投行上調目標價」時,務必寫出 (a) 該投行是否為公司的財務顧問/主承銷商 / 融資提供者(證券法上須揭露), (b) 該投行是否持股(利益衝突). 「研究獨立」不代表無衝突;讀者有權知道投行的經濟利益。
- **「預期」「預估」「展望」是法律概念** — 若寫「公司預期今年營收 100 億」,該預期必須來自官方指引(年報、法說會、公開聲明),不能是你的推測或分析師猜測。「展望」與「宣布」的法律後果不同(展望有 safe harbor, 宣布無)。
- **匯率換算的基準易生誤解** — 「美國子公司營收 $100M USD」若未說明是月底匯率、月均、還是歷史成本,國際讀者無法驗算。跨幣別報導時永遠附匯率日期與匯率數字,让讀者能追蹤 FX impact。
- **「本益比」「股價淨值比」無脈絡就無意義** — 12× P/E 在成長股集中的產業是便宜,在成熟產業是昂貴。寫倍數前,必須給對標(「同業平均 18×」或「公司 5 年平均 15×」),否則讀者無法判斷。避免使用「合理」「偏高」這類無基礎的斷言。
- **一次性項目重複出現代表隱瞞常態營運衰退** — 若財報連 3 季都有「一次性」收益/損失,這不再是「一次性」,而是常態。當你看到重複的「一次性」旗標,這是會計舞弊紅旗,應列入稿件待查項目。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 財經線消息來源、機構、官方資料庫 (公開資訊觀測站、TWSE、金管會、央行、主計總處、SEC EDGAR、Bloomberg) | Step 2 source vetting |
| `references/glossary.md` | 財務、會計、市場專業術語對照與定義 (GAAP/IFRS, EPS/ROE/EBITDA, 重大訊息, M&A, 量化寬鬆) 與常見誤用 | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 證交法 §155 操縱市場、§157-1 內線交易、利益衝突揭露、財報新聞時間敏感性、Analyst disclosure | Step 3 risk check |
| `references/financial_statements_reading.md` | 三大表判讀:資產負債表/損益表/現金流量表警訊指標、會計舞弊紅旗、本益比與股價淨值比脈絡化 | Step 4 Number Audit |
| `references/market_data_reading.md` | 指數計算口徑、報酬率年化、技術指標限制、單日波動 vs 趨勢、匯率報導基準 | When citing market data / multi-period comparisons |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `data-financial-analysis` — deeper analysis of financial metrics & ratio modeling
- `stat-hypothesis-testing` — for statistical rigor in trend claims
- `hum-source-criticism` — source vetting frameworks for analyst credibility

---

## Limitations

- **Does not detect accounting fraud algorithmically.** This skill flags red-flag patterns (revenue timing, margin compression, related-party spikes); it does not perform forensic accounting or access internal controls audit. Fraud detection requires specialist expertise.
- **Does not perform live fact verification.** This skill flags claims that need verification (e.g., "CEO says $2B revenue, check against filing"); it does not access SEC EDGAR, 公開資訊觀測站, or company databases in real time. Editor must verify or supply.
- **Valuation methods are not within scope.** DCF, comparable-company, precedent-transaction analyses are covered in `data-financial-analysis` and `fin-investment-thesis`. This skill assumes valuation inputs are supplied and checks only the metadata (source, assumptions disclosed).
- **Jurisdictional scope:** Legal references (證交法, 上市公司規範, GAAP vs IFRS) reflect Taiwan. For US (SEC rules, Reg FD, Sarbanes-Oxley), EU (IFRS, MAR), HK, PRC, or other jurisdictions, principles still apply but specific statutes and thresholds differ.
- **Not an earnings-call transcription service.** If the user supplies an audio/video earnings call without a transcript, this skill does not transcribe it; user must provide transcript or use external transcription tool first.
