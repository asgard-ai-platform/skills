# Example: 遠距工作對員工心理健康影響的系統性文獻回顧

## Scenario

PhD 候選人 Maya Krishnan 就讀於新加坡管理大學（SMU）組織行為學系。她正在設計一份關於「遠距工作（remote work）對員工心理健康（psychological well-being）影響」的系統性回顧，作為她博士論文的第二章。指導教授要求她：

1. 建立一個可重製（reproducible）的搜尋策略
2. 使用 PRISMA 2020 格式記錄篩選流程
3. 建立清楚的納入/排除標準
4. 對納入研究進行品質評估

Maya 的問題：「我要怎麼系統性地設計這份文獻回顧？哪些資料庫要搜尋？怎麼決定哪些文章要納入？」

---

## Analysis

### Step 1：定義研究問題與協議

Maya 的主題是介入性問題（遠距工作作為一種工作安排），因此適合用 **PICO** 框架：

| 元素 | 定義 |
|------|------|
| **P**opulation | 全職受雇員工（不含學生、自由工作者） |
| **I**ntervention | 遠距工作（每週至少 2 天，持續 ≥ 1 個月） |
| **C**omparison | 辦公室工作（全辦公室或混合辦公，低於每週 2 天遠距） |
| **O**utcome | 心理健康指標：焦慮、憂鬱、工作倦怠、工作滿意度、孤立感 |

**PROSPERO 預先登錄**：協議於 2025 年 11 月提交，登錄號 CRD42025448321。

納入標準預先定義：
- 2020 年 1 月起發表（COVID 後遠距工作規模化時代）
- 量化或混合方法研究（含縱貫性調查、實驗設計、調查研究）
- 樣本數 ≥ 50 人
- 英文或中文發表

排除標準：
- 個案研究、意見文章、書評
- 自由工作者或臨時僱傭為唯一樣本
- 僅測量生產力，未包含心理健康結果

---

### Step 2：搜尋策略

Maya 搜尋 4 個資料庫（2026 年 1 月 15 日執行）：

| Database | Search String | Records |
|----------|--------------|---------|
| Scopus | `("remote work" OR "telework" OR "work from home") AND ("mental health" OR "psychological well-being" OR "burnout" OR "anxiety" OR "depression") AND ("employee" OR "worker")` | 1,847 |
| Web of Science | 同上（加 MeSH 術語 `Telecommuting`） | 1,203 |
| PsycINFO | `TI: (remote work OR telework) AND AB: (mental health OR well-being OR burnout)` | 892 |
| PubMed | `("Teleworking"[MeSH] OR "remote work") AND ("mental health"[MeSH] OR "burnout") AND 2020:2026[dp]` | 614 |

補充來源：
- 手動搜尋 *Journal of Applied Psychology*、*Work & Stress* 2023–2026 年期數
- 引用追蹤（backward chaining）：對已納入的 5 篇關鍵研究進行參考文獻掃描
- 灰色文獻：ILO 報告、Gallup 工作場所調查

**識別總計：4,556 筆記錄**

---

### Step 3：篩選流程（PRISMA Flow）

兩位獨立審閱者（Maya + 同實驗室 RA Lin Wei）各自篩選題目與摘要，以 Rayyan 系統管理衝突。

```
PRISMA Flow:

識別 (Identification)
├── 資料庫記錄：4,556
├── 灰色文獻：47
└── 引用追蹤新增：23
    總計識別：4,626

去除重複後：3,891 筆

標題/摘要篩選 (Screening)
├── 篩選：3,891
└── 排除：3,412
    主因：主題不符（主要為生產力、績效，非心理健康）

全文評估 (Eligibility)
├── 評估：479
└── 排除：361
    ├── 樣本不符（自由工作者）：89
    ├── 研究設計不符（個案研究/意見文章）：74
    ├── 樣本數 < 50：63
    ├── 遠距工作定義不明確（未達每週 2 天門檻）：81
    └── 無法取得全文：54

納入合成 (Included)
└── 納入：118 篇
    ├── 量化研究：93 篇
    └── 混合方法研究：25 篇

審閱者間信度：Cohen's κ = 0.81（標題/摘要篩選）；κ = 0.76（全文篩選）
衝突均透過討論解決，無需第三審閱者
```

---

### Step 4：資料萃取、品質評估與合成

**品質評估工具**：
- 量化調查研究：JBI 橫斷面研究清單（9 項）
- 縱貫研究：Newcastle-Ottawa Scale（NOS）
- 實驗設計：Cochrane Risk of Bias 2 (RoB 2)

品質評估摘要（前 6 篇代表性研究）：

| Study | Tool | Rating | Key Concerns |
|-------|------|--------|--------------|
| Xiao et al. (2021), n=1,066 | JBI | High | 橫斷面設計，無法推論因果 |
| Wang et al. (2023), n=2,341 | NOS | Moderate | 自評量表，社會期許偏誤風險 |
| Schmitt & Riedl (2024), n=843 | NOS | High | 追蹤 18 個月，失訪率 12% |
| Park et al. (2022), n=156 | RoB 2 | High | 隨機分派，但樣本限科技業 |
| Chen & Liu (2025), n=3,102 | JBI | Moderate | 測量時點跨 COVID 高峰，混淆效應強 |
| Russo et al. (2023), n=417 | JBI | Low | 回憶偏誤，招募自社群媒體 |

**合成方法**：
- 因研究在測量工具（PHQ-9、GHQ-12、MBI 等）和樣本上異質性高（I² > 70%），不適合直接 meta-analysis
- 採用**敘事合成（narrative synthesis）**，輔以投票計數法（vote counting）呈現效應方向

---

## Result

```markdown
## Systematic Review: 遠距工作對員工心理健康的影響 (2020–2026)

### Protocol
- Question framework: PICO
- Registration: PROSPERO CRD42025448321
- Databases searched: Scopus, Web of Science, PsycINFO, PubMed
- Date range: 2020-01-01 to 2026-01-15

### Search Strategy
| Database | Search String | Records Found |
|----------|--------------|---------------|
| Scopus | ("remote work" OR "telework" OR "work from home") AND ("mental health" OR "psychological well-being" OR "burnout") AND ("employee" OR "worker") | 1,847 |
| Web of Science | 同上 + MeSH: Telecommuting | 1,203 |
| PsycINFO | TI: (remote work OR telework) AND AB: (mental health OR burnout) | 892 |
| PubMed | "Teleworking"[MeSH] AND "mental health"[MeSH] AND 2020:2026[dp] | 614 |

### PRISMA Flow
- Identified: 4,626 records
- Duplicates removed: 735
- Screened (title/abstract): 3,891
- Excluded at screening: 3,412
- Full-text assessed: 479
- Excluded at full-text: 361 (reasons: 樣本不符 89、設計不符 74、樣本數不足 63、定義不明 81、無全文 54)
- Included in synthesis: 118

### Inclusion/Exclusion Criteria
| Criterion | Include | Exclude |
|-----------|---------|---------|
| Population | 全職受雇員工，樣本數 ≥ 50 | 自由工作者、學生、臨時工 |
| Study type | 量化或混合方法研究 | 個案研究、意見文章 |
| Language | 英文、中文 | 其他語言 |
| Date | 2020-01-01 起 | 2019 年以前 |
| Intervention | 遠距工作 ≥ 每週 2 天，持續 ≥ 1 個月 | 遠距工作定義不明確者 |

### Quality Assessment Summary
| Study | Tool Used | Overall Rating | Key Concerns |
|-------|-----------|---------------|--------------|
| Xiao et al. (2021) | JBI | High | 橫斷面，因果推論受限 |
| Wang et al. (2023) | NOS | Moderate | 自評量表偏誤 |
| Schmitt & Riedl (2024) | NOS | High | 18 個月追蹤，失訪率可接受 |
| Park et al. (2022) | RoB 2 | High | 樣本侷限科技業 |

### Synthesis
- **工作倦怠**：118 篇中 71 篇（60%）顯示遠距工作與更高倦怠相關，主要驅動因素為工作/生活邊界模糊（work-life boundary erosion）；高品質縱貫研究（n=4）結果一致
- **焦慮與憂鬱**：結果分歧（43% 改善，38% 惡化）；調節因子包括居家環境品質、有無子女及個人自主性
- **工作滿意度**：多數研究（67%）顯示正向效應，強化「遠距工作≠心理健康惡化」的簡化假設不成立
- Gaps identified: 缺乏針對非科技業、非西方情境的研究；混合辦公（hybrid）的最佳劑量尚無共識

### Limitations
- 搜尋限英文與中文，可能遺漏其他語言高品質研究
- 大多數研究橫斷面設計，因果方向無法確定
- COVID 封鎖期間強制遠距與自願遠距工作者的心理健康軌跡可能不同，但多數研究未加以區分
```
