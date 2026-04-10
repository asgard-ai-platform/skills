# Example: SaaS 新創薪酬競爭力稽核

## Scenario

**公司背景：** Telepath AI，台灣 B 輪 SaaS 新創，約 90 名員工，主要產品為企業客服 AI 平台。HR 總監 Jess Chen 正準備 2026 Q2 調薪週期，懷疑工程部門流失率偏高（過去 12 個月離職 6 人）與薪酬低於市場有關。

**可用數據：**
- 內部薪資資料：38 名工程師（含 IC 與 TL），基本薪 NT$1.2M–NT$2.6M
- Mercer Taiwan ICT Survey 2025-H2（2025 年 6 月資料收集）
- 員工性別資料可用，但年資記錄不完整（35% 缺漏）

**用戶問題：**
> 「我想知道我們工程師的薪資競爭力，有沒有人嚴重低於市場？另外請幫我看一下性別薪酬差距。」

---

## Analysis

### Phase 1：Input Validation

**職級對應（Job Matching）**

Telepath 內部職稱對應 Mercer 調查的「軟體開發 / ICT — 台灣中小型企業（< 500 人）」基準：

| 內部職稱 | 人數 | Mercer Benchmark Code | 對應條件 |
|----------|------|-----------------------|----------|
| Junior Engineer | 10 | SW-IC-2 | ≤ 2 年軟體開發經驗，無帶人責任 |
| Engineer | 14 | SW-IC-3 | 3–5 年，獨立交付功能 |
| Senior Engineer | 9 | SW-IC-4 | 6–9 年，跨團隊影響力 |
| Tech Lead | 5 | SW-TL-5 | 帶 3–6 人小組，仍含個人貢獻 |

> **注意：** 1 名頭銜為「Senior Engineer」但實際工作內容偏 Junior 的員工，降階至 SW-IC-2 計算。職稱不等於 job content。

**資料時效確認**

Mercer 2025-H2 資料收集於 2025 年 6 月，距今（2026 年 4 月）10 個月。台灣 ICT 市場 2025 年薪資成長率約 4.2%（Mercer projection）。

老化係數：`1 + 0.042 × (10/12) = 1.035`

**Gate 通過：** 職位已依工作內容對應完畢；調查資料需老化後使用。

---

### Phase 2：Core Algorithm

**市場基準老化後數值（NT$/年，已乘老化係數 1.035）**

| 職級 | P25（老化後） | P50（老化後） | P75（老化後） |
|------|--------------|--------------|--------------|
| SW-IC-2 (Junior) | 1,056,000 | 1,242,000 | 1,449,000 |
| SW-IC-3 (Engineer) | 1,449,000 | 1,759,000 | 2,070,000 |
| SW-IC-4 (Senior) | 1,863,000 | 2,277,000 | 2,691,000 |
| SW-TL-5 (Tech Lead) | 2,277,000 | 2,898,000 | 3,312,000 |

**Compa-Ratio 計算（各職級平均）**

| 職級 | 內部平均實際薪（NT$） | 市場 P50（NT$） | Compa-Ratio |
|------|---------------------|----------------|-------------|
| Junior (n=10) | 1,150,000 | 1,242,000 | **0.93** |
| Engineer (n=14) | 1,560,000 | 1,759,000 | **0.89** |
| Senior (n=9) | 2,050,000 | 2,277,000 | **0.90** |
| Tech Lead (n=5) | 2,780,000 | 2,898,000 | **0.96** |

**個人層級旗標（Below Band < P25）**

- Engineer 職級：3 人基本薪低於市場 P25（NT$1,449,000）；其中 1 人低至 NT$1,250,000（compa-ratio 0.71）
- Senior 職級：2 人低於 P25（NT$1,863,000）

合計 **5 人嚴重低於市場（< P25）**，建議列為調薪優先名單。

---

**性別薪酬分析**

| 性別 | 人數 | 平均 Compa-Ratio |
|------|------|-----------------|
| 男性 | 28 | 0.91 |
| 女性 | 10 | 0.88 |

原始差距：女性平均 compa-ratio 低 3.4%。

> **控制合法因素後：** 年資資料缺漏 35%，無法執行完整迴歸控制。以可用的 65% 員工（n=25）進行簡化回歸，控制職級後，性別係數 = −0.028（p = 0.09）。**在目前樣本下未達統計顯著（p < 0.05）**，但缺漏資料本身是風險——需先補齊年資資料才能正式結案。

---

### Phase 3：Verification

- Compa-ratio 分佈：0.71–1.08，整體偏低（正常範圍 0.85–1.15）
- 低於 P25 的 5 人均屬工作年資 3 年以上的 Engineer / Senior，是留才風險最高的族群
- 性別差距現有資料下未顯著，但分析受限於年資缺漏——**結論不完整，需補資料**

**Gate 通過（條件式）：** 主要競爭力分析完成；性別薪酬分析需待年資資料補齊後重跑。

---

## Result

```json
{
  "summary": {
    "avg_compa_ratio": 0.91,
    "below_band_pct": 13,
    "above_band_pct": 3
  },
  "by_role": [
    {"role": "Junior Engineer",  "market_p50": 1242000, "avg_actual": 1150000, "compa_ratio": 0.93},
    {"role": "Engineer",         "market_p50": 1759000, "avg_actual": 1560000, "compa_ratio": 0.89},
    {"role": "Senior Engineer",  "market_p50": 2277000, "avg_actual": 2050000, "compa_ratio": 0.90},
    {"role": "Tech Lead",        "market_p50": 2898000, "avg_actual": 2780000, "compa_ratio": 0.96}
  ],
  "priority_adjustments": [
    {"employee_id": "E-017", "role": "Engineer",        "actual": 1250000, "market_p25": 1449000, "gap": -199000},
    {"employee_id": "E-031", "role": "Engineer",        "actual": 1310000, "market_p25": 1449000, "gap": -139000},
    {"employee_id": "E-044", "role": "Senior Engineer", "actual": 1740000, "market_p25": 1863000, "gap": -123000}
  ],
  "equity_flags": [
    {
      "dimension": "gender",
      "gap_pct": 3.4,
      "statistically_significant": false,
      "caveat": "年資資料缺漏 35%，結論不確定；建議補齊後重新分析"
    }
  ],
  "metadata": {
    "employees": 38,
    "survey_source": "Mercer Taiwan ICT Survey",
    "survey_date": "2025-H2",
    "aging_factor": 1.035,
    "analysis_date": "2026-04-10"
  }
}
```

### 行動建議

1. **立即調薪（Q2 週期）：** 5 名低於 P25 員工納入優先名單，建議調整至 P40–P50 區間，預估年薪資成本增加約 NT$900K。
2. **Engineer 職級整體偏低（compa-ratio 0.89）：** 若預算允許，Engineer band midpoint 建議拉至 NT$1.75M，與市場 P50 對齊。
3. **性別薪酬分析：** 90 天內補齊年資資料，以 Engineer、Senior 兩個職級為優先，重跑迴歸。資料缺漏本身即為 HR 系統的稽核項目。
4. **流失率關聯：** 6 名離職者中，請 HR 確認職級分佈——若離職者集中於 Engineer / Senior，與 compa-ratio 0.89–0.90 高度一致，強化調薪正當性。
