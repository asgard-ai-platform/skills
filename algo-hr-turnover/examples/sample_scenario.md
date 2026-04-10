# Example: TechStream 軟體工程師留任危機預測

## Scenario

TechStream 是一家台灣中型 SaaS 公司，員工約 800 人，其中軟體工程師 320 名。2025 年第三季工程部門離職率驟升至 22%（行業均值約 13%），HR 總監 Vivian 需要在 Q4 預算分配前，找出哪些工程師最可能在未來 12 個月離職，以及主要離職驅動因子，以便將留才預算集中在高風險人員。

Vivian 提供了過去 3 年的 HR 資料集（2022-2025），共 750 名工程師的歷史紀錄，其中含 163 筆已知離職事件（voluntarily departed）。

**可用特徵：**

| 特徵 | 類型 | 說明 |
|------|------|------|
| tenure_months | 數值 | 入職至今月數 |
| comp_ratio | 數值 | 薪資 / 市場中位數（Radford 基準） |
| months_since_promotion | 數值 | 上次晉升至今月數 |
| manager_change_2yr | 布林 | 過去 2 年是否換過主管 |
| perf_rating_last | 類別 | 上次績效評級 (1-5) |
| engagement_trend | 數值 | 最近 2 次員工調查分數差（正 = 改善） |
| commute_km | 數值 | 通勤距離（公里） |
| team_headcount_change | 數值 | 過去 6 個月團隊人數變化率 |

---

## Analysis

### Phase 1：Input Validation

**Gate 檢查：**
- 離職事件數 163 > 200 門檻 ⚠️ — 略低，但在可接受邊界（163 / 750 = 21.7% base rate，樣本數尚足）。告知 Vivian 模型信心區間較寬，建議加入 2021 年資料補足至 200+ 事件。
- 所有特徵均取自「離職前」時間點，無未來洩漏。
- 排除受保護屬性（性別、年齡、婚姻狀況）及代理變數（郵遞區號與族群高度相關，不納入）。

**Feature Engineering：**

```python
# tenure_bucket: 新手 / 成長期 / 資深 / 老鳥
df["tenure_bucket"] = pd.cut(df["tenure_months"],
    bins=[0, 12, 36, 72, 999],
    labels=["0-1yr", "1-3yr", "3-6yr", "6yr+"])

# comp_ratio 已標準化；< 0.90 視為低於市場
df["below_market"] = (df["comp_ratio"] < 0.90).astype(int)

# 晉升停滯：超過 30 個月未晉升
df["promotion_stalled"] = (df["months_since_promotion"] > 30).astype(int)

# 組織動盪複合指標
df["org_disruption"] = (
    df["manager_change_2yr"].astype(int) +
    (df["team_headcount_change"] < -0.15).astype(int)
)
```

### Phase 2：Core Algorithm

**模型選擇：** XGBoost（Vivian 的受眾為 CHRO，需要可解釋的 SHAP 輸出）+ Logistic Regression 作為解釋基線。

**Class Imbalance 處理：**
- 離職率 21.7%，中度不平衡。採用 `scale_pos_weight = (750-163)/163 ≈ 3.6`（XGBoost 內建）。
- 不使用 SMOTE（因樣本數偏少，合成資料會放大噪音）。

**訓練 / 驗證切分：**
- 時間序列切分：2022-2024 訓練，2025 H1 驗證（避免未來洩漏）。
- 訓練集：620 筆 / 驗證集：130 筆。

**超參數（簡化版）：**
```
n_estimators: 200
max_depth: 4
learning_rate: 0.05
subsample: 0.8
```

**驗證結果：**

| 指標 | 值 |
|------|----|
| AUC-ROC | 0.76 |
| Precision（Top Decile） | 58% |
| Recall（Top Decile） | 34% |
| F1（threshold=0.45） | 0.51 |

Gate 通過：AUC 0.76 > 0.70，Top Decile Precision 58% > 50%。

**SHAP 全局重要性（前 5 名）：**

| 排名 | 特徵 | 平均 |SHAP| |
|------|------|------|
| 1 | comp_ratio | 0.18 |
| 2 | months_since_promotion | 0.15 |
| 3 | engagement_trend | 0.12 |
| 4 | org_disruption | 0.09 |
| 5 | tenure_bucket (1-3yr) | 0.08 |

### Phase 3：Verification（回測）

回測：將 2025 H1 已離職的 28 人對照模型於 2024 年底的預測分數。
- 28 人中，21 人落在 Top Quartile（Risk ≥ 0.55） → 75% 捕獲率。
- 模型未捕獲的 7 人：5 人為「外部挖角突然接受」（engagement 當時仍正常），2 人為家庭因素（無法從 HR 資料預測）。

結論：模型對「可預防離職」捕獲率良好；不可預測的突發情況不計入模型缺陷。

---

## Result

### 風險分群（現有 320 名工程師）

| 風險層 | 閾值 | 人數 | 建議行動 |
|--------|------|------|---------|
| 🔴 High | ≥ 0.60 | 38 人（12%） | 立即 1-on-1、薪資調整、晉升快速通道 |
| 🟡 Medium | 0.40–0.59 | 74 人（23%） | 季度關懷 check-in、發展計畫 |
| 🟢 Low | < 0.40 | 208 人（65%） | 常規管理 |

### 代表性高風險員工輸出

```json
{
  "risk_scores": [
    {
      "employee_id": "E0472",
      "turnover_prob": 0.81,
      "risk_tier": "high",
      "top_drivers": [
        "comp_ratio_0.82",
        "no_promotion_38mo",
        "engagement_trend_-12pts",
        "manager_change_2yr"
      ]
    },
    {
      "employee_id": "E0319",
      "turnover_prob": 0.68,
      "risk_tier": "high",
      "top_drivers": [
        "comp_ratio_0.88",
        "tenure_bucket_1-3yr",
        "team_headcount_change_-22pct"
      ]
    }
  ],
  "metadata": {
    "model": "xgboost",
    "auc": 0.76,
    "prediction_window_months": 12,
    "cohort_size": 320,
    "high_risk_count": 38,
    "training_period": "2022-01_to_2024-12"
  }
}
```

### 留才預算建議

主要離職驅動為薪資低於市場（comp_ratio < 0.90 涵蓋 High Risk 群中 71%）與晉升停滯（> 30 個月，涵蓋 58%）。建議 Vivian 優先：

1. **薪資校正**：High Risk 群中 comp_ratio < 0.90 者（估 27 人），調至 0.95 以上。若平均調幅 8%、平均薪資 NTD 120K/月，年成本約 NTD 3.1M，遠低於一名資深工程師離職替換成本（估 NTD 80-120 萬）。
2. **晉升快速通道**：針對停滯 > 30 個月且績效評級 ≥ 4 者（估 14 人），在 Q4 績效循環中優先列入 promotion pipeline。
3. **組織穩定**：3 個異動最頻繁的團隊（team_headcount_change < -20%）請主管進行組織說明，避免謠言驅動離職。

> **⚠️ 注意（Iron Law）：** 模型輸出為風險機率，非判決。E0472 有 81% 離職風險，不代表該員工「已決定要走」，更不應在未經本人同意的情況下以「即將離職」標記納入其人事資料。HR 介入應以關懷與發展為框架，而非監控。
