# Example: 員工數位工具採用行為的 SEM 模型驗證

## Scenario

TalentSync 是一家台灣 B2B SaaS 公司，旗下 HR 平台於 2024 年導入 AI 排班助手功能。產品研究團隊在導入六個月後針對 312 名企業用戶進行問卷調查，欲驗證以下理論模型：

> **感知有用性（PU）** 和 **感知易用性（PEOU）** 共同影響 **使用意圖（BI）**，且 PEOU 同時透過 PU 間接影響 BI（TAM 架構延伸）。此外，**組織支持（OS）** 被假設正向影響 PU。

研究員 Wendy 的問題：「我的問卷回收了 312 份，每個構念有 3-4 題 Likert 量表，我要怎麼驗證整個理論模型？測量模型跟結構模型到底先做哪個？」

問卷題項：
- **PU** (4 items): PU1–PU4 — 「這個 AI 功能提升我的工作效率」等
- **PEOU** (3 items): PEOU1–PEOU3 — 「這個系統容易學習」等
- **OS** (3 items): OS1–OS3 — 「我的主管鼓勵使用此系統」等
- **BI** (3 items): BI1–BI3 — 「我打算在未來持續使用此功能」等

---

## Analysis

### Step 1 — 確認先決條件

- N = 312，估計參數約 38（13 個因素負荷 + 6 條結構路徑 + 殘差），N/param ≈ 8.2
  - **邊緣通過**（略低於理想的 10:1），須在限制部分中說明
- 偏態係數全在 ±1.5 內，峰度未超過 ±3；採用 **MLR（Robust ML）**估計以防非常態影響
- 使用 R `lavaan` 套件進行兩步驟分析（Anderson & Gerbing, 1988）

---

### Step 2 — 測量模型（CFA）

**lavaan 模型語法：**

```r
cfa_model <- '
  PU   =~ PU1 + PU2 + PU3 + PU4
  PEOU =~ PEOU1 + PEOU2 + PEOU3
  OS   =~ OS1 + OS2 + OS3
  BI   =~ BI1 + BI2 + BI3
'
fit_cfa <- cfa(cfa_model, data = talentsync_df,
               estimator = "MLR", std.lv = TRUE)
```

**標準化因素負荷（所有 p < .001）：**

| 構念 | 題項 | Std. Loading | AVE | CR |
|------|------|-------------|-----|-----|
| PU | PU1 | 0.78 | — | — |
| PU | PU2 | 0.82 | — | — |
| PU | PU3 | 0.75 | — | — |
| PU | PU4 | 0.80 | **0.62** | **0.87** |
| PEOU | PEOU1 | 0.71 | — | — |
| PEOU | PEOU2 | 0.84 | — | — |
| PEOU | PEOU3 | 0.79 | **0.61** | **0.82** |
| OS | OS1 | 0.68 | — | — |
| OS | OS2 | 0.76 | — | — |
| OS | OS3 | 0.73 | **0.52** | **0.77** |
| BI | BI1 | 0.86 | — | — |
| BI | BI2 | 0.88 | — | — |
| BI | BI3 | 0.83 | **0.73** | **0.89** |

收斂效度（AVE ≥ 0.50，CR ≥ 0.70）全數通過。

**區別效度（Fornell-Larcker 準則）：** 各構念 AVE 平方根均大於其與他構念的相關係數，通過區別效度檢驗。

---

### Step 3 — 測量模型配適度評估

| Index | Value | Threshold | Assessment |
|-------|-------|-----------|------------|
| CFI | 0.96 | ≥ 0.90 | ✓ Pass |
| TLI | 0.95 | ≥ 0.90 | ✓ Pass |
| RMSEA | 0.051 | ≤ 0.08 | ✓ Pass |
| SRMR | 0.049 | ≤ 0.08 | ✓ Pass |
| χ²/df | 1.87 | ≤ 3.0 | ✓ Pass |

**修正指標（MI）：** MI 最高項為 PU1 與 PU3 的殘差共變（MI = 8.4）。因兩題語意相近（皆涉及「效率」），**決定不修正**——修正缺乏理論依據且可能過度配適。

---

### Step 4 — 結構模型估計

**lavaan 結構路徑語法：**

```r
sem_model <- '
  PU   =~ PU1 + PU2 + PU3 + PU4
  PEOU =~ PEOU1 + PEOU2 + PEOU3
  OS   =~ OS1 + OS2 + OS3
  BI   =~ BI1 + BI2 + BI3

  # 結構路徑
  PU ~ PEOU + OS
  BI ~ PU + PEOU
'
fit_sem <- sem(sem_model, data = talentsync_df,
               estimator = "MLR", std.lv = TRUE)
```

**結構路徑結果：**

| Path | Std. β | S.E. | p-value | Supported? |
|------|--------|------|---------|------------|
| PEOU → PU | 0.51 | 0.07 | < .001 | Yes |
| OS → PU | 0.34 | 0.08 | < .001 | Yes |
| PU → BI | 0.47 | 0.09 | < .001 | Yes |
| PEOU → BI | 0.22 | 0.09 | .015 | Yes |

**內生構念解釋變異量：**
- R²(PU) = 0.48（PEOU + OS 共解釋 48% 的 PU 變異）
- R²(BI) = 0.54

**間接效果（Bootstrapping, 5,000 次抽樣）：**

| 間接路徑 | 間接效果 | 95% CI | 顯著？ |
|----------|---------|--------|--------|
| PEOU → PU → BI | 0.24 | [0.13, 0.37] | Yes |
| OS → PU → BI | 0.16 | [0.07, 0.27] | Yes |

PEOU 對 BI 的直接效果（0.22）加上間接效果（0.24）顯示 PU 為**部分中介**，非完全中介。

---

## Result

## SEM Analysis: TalentSync AI 排班助手採用行為模型

### Measurement Model (CFA)

| Construct | Indicator | Std. Loading | AVE | CR |
|-----------|-----------|-------------|-----|-----|
| PU | PU1–PU4 | 0.75–0.82 | 0.62 | 0.87 |
| PEOU | PEOU1–PEOU3 | 0.71–0.84 | 0.61 | 0.82 |
| OS | OS1–OS3 | 0.68–0.76 | 0.52 | 0.77 |
| BI | BI1–BI3 | 0.83–0.88 | 0.73 | 0.89 |

### Model Fit

| Index | Value | Threshold | Assessment |
|-------|-------|-----------|------------|
| CFI | 0.96 | ≥ 0.90 | Pass |
| TLI | 0.95 | ≥ 0.90 | Pass |
| RMSEA | 0.051 | ≤ 0.08 | Pass |
| SRMR | 0.049 | ≤ 0.08 | Pass |

### Structural Paths

| Path | Std. β | S.E. | p-value | Supported? |
|------|--------|------|---------|------------|
| PEOU → PU | 0.51 | 0.07 | < .001 | Yes |
| OS → PU | 0.34 | 0.08 | < .001 | Yes |
| PU → BI | 0.47 | 0.09 | < .001 | Yes |
| PEOU → BI | 0.22 | 0.09 | .015 | Yes |

### Key Findings

- 整體模型配適度良好，TAM 延伸架構獲得支持
- **感知易用性（PEOU）** 是影響使用意圖最重要的前因，直接效果（β = 0.22）與透過 PU 的間接效果（β = 0.24）相當，顯示 PU 為**部分中介**
- **組織支持（OS）** 透過 PU 間接影響使用意圖（95% CI: [0.07, 0.27]），產品推廣策略應同時改善介面易用性及爭取主管背書
- R²(BI) = 0.54，模型具備良好的解釋力

### Limitations

- N/parameter 比（8.2:1）略低於建議的 10:1，路徑係數標準誤可能略為低估
- 橫截面設計無法排除等效模型（例如 BI → PU 方向之反向因果）
- 共同方法變異（CMV）風險存在，建議後續研究混合客觀行為日誌數據
