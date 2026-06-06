# 估值橋與三法交叉驗證詳解

## 為何用三種方法

**單一方法的盲點**
- DCF：對假設敏感，GIGO 嚴重
- 可比公司：受市場情緒影響
- 可比交易：樣本稀少、可比性有限

**三法交叉的目的**
- 收斂估值區間
- 交叉驗證假設
- 應對不同利害關係人的溝通（投行偏交易法、PE 偏 DCF）

## 方法 1：DCF（Discounted Cash Flow）

### 五年模型基本結構

```
年度 1–5 預測期：
  營收 → 毛利 → EBITDA → 稅後 NOPAT → FCFF
  
終值（Terminal Value）：
  方法 A：Gordon Growth Model
    TV = FCFF(6) / (WACC − g)
  方法 B：Exit Multiple
    TV = EBITDA(5) × Multiple
  
企業價值：
  EV = Σ FCFF(t) / (1+WACC)^t + TV / (1+WACC)^5
```

### 關鍵假設敏感度

| 變數 | 變動 1% | 典型 EV 影響 |
|---|---|---|
| 營收成長率 | +1% | +5–8% |
| EBITDA Margin | +1pp | +8–12% |
| WACC | +1pp | −8–15% |
| Terminal Growth | +1pp | +5–10% |
| Exit Multiple | +1x | +10–20% |

**建議**：敏感度分析至少做 5 個變數 × 3 個情境。

### WACC 計算

```
WACC = (E/V) × Re + (D/V) × Rd × (1−T)

Re (Cost of Equity) = Rf + β × (Rm − Rf) + CSR
  CSR (Country/Company-Specific Risk Premium)
Rd (Cost of Debt) = 實際或平均借款利率
T = 實際稅率
```

**台灣併購案常見調整**
- 無風險利率：用 10 年期公債 ≈ 1.5%
- 市場風險溢酬：用美國 + 台灣溢酬 ≈ 7–8%
- Beta：用同業公開公司 Beta（Unlevered 後 Relevered）
- 小型公司溢酬：+2–5%
- 國家風險：跨境併購特別要加

### Terminal Value 警訊

**TV 佔 EV 比例**
- 健康範圍：60–75%
- 過高（> 80%）：預測期太短或 TV 假設過度樂觀
- 過低（< 50%）：預測期太長或 TV 假設太保守

**永續成長率（g）**
- 不得高於該國長期 GDP 成長率
- 一般 2–3%
- 新興市場可稍高（3–4%）

### DCF 常見作弊手法

1. 調高預測期成長率（「看好未來」）
2. 壓低 WACC（省略特定風險）
3. 調高 Terminal Growth
4. 調高 Exit Multiple
5. 調整稅率（用低估實際稅率）

**EMBA 作業防作弊**：至少列出 5 個敏感度變數；三法交叉驗證差距 > 30% 需重新檢視。

## 方法 2：可比公司法（Comparable Companies）

### 選擇可比公司

**篩選標準**
- 產業同屬（同 GICS / SIC 分類）
- 規模相近（營收、市值 ±50%）
- 地區相近（或至少同一經濟圈）
- 成長性相近
- 財務結構相近

**樣本數**
- 至少 5 家（避免單一影響）
- 10–15 家為佳
- 排除極端值（用中位數而非平均）

### 常用倍數

| 倍數 | 適用 | 警訊 |
|---|---|---|
| EV/EBITDA | 最通用、忽略資本結構 | 忽略折舊差異 |
| EV/EBIT | 考慮資本密集度 | 受會計政策影響 |
| EV/Revenue | 新創、高成長 | 忽略獲利能力 |
| P/E | 一般 | 受資本結構、一次性項目影響 |
| P/B | 資產密集業（銀行、不動產） | 不適用服務業 |
| EV/CUSTOMER | SaaS、電商 | 產業特定 |

### 上市公司倍數 vs. 控制權溢價

**問題**：可比上市公司倍數反映的是「少數股權」，併購是「控制權」

**調整**
- 一般控制權溢價：20–40%
- 併購交易倍數已含控制權溢價，不可再加
- 若用上市倍數：需加控制權溢價

**公式**
```
控制權估值 = 上市倍數 × 目標財務數字 × (1 + Control Premium)
```

## 方法 3：可比交易法（Precedent Transactions）

### 選擇可比交易

**篩選標準**
- 產業同屬
- 交易時間近（過去 3–5 年）
- 交易規模相近
- 結構相似（控制權收購 vs. 少數股權）
- 地區相近

**資料來源**
- Bloomberg M&A Database
- Capital IQ / FactSet
- Mergermarket
- 台灣：公開資訊觀測站重大訊息 + 併購法處分公告
- 新聞檢索

### 可比交易倍數的優勢

- 已反映控制權溢價
- 反映併購市場實況
- 對同業公信力強

### 可比交易倍數的限制

- 樣本稀少（特別是台灣中小型）
- 揭露有限（私有交易細節不全）
- 時間差距（市場環境變化）
- 特殊情境（財務困境、敵意收購）

### 使用建議

- 取中位數而非平均
- 分類比較（戰略買家 vs. 財務買家）
- 剔除異常值
- 至少 3 件才有意義

## 估值橋（Valuation Bridge）

### EV to Equity Value 橋

**概念**：從企業價值到股權價值的調整

```
Enterprise Value (EV)
  − Total Debt（有息負債）
  + Cash and Cash Equivalents
  = Net Debt 調整後

  − Minority Interest（少數股東權益）
  − Preferred Stock（特別股）
  + Investments in Associates（權益法投資）
  − Pension Deficit（退休金未提撥）
  − Contingent Liabilities（或有負債，機率加權）
  − Tax Liabilities（特定稅務負債）
  
  = Equity Value
```

### Standalone to Transaction Bridge（重點）

**EMBA 最常考：為何市場估值 ≠ 交易對價**

```
Standalone Value（獨立經營價值）
  基於 DCF 或可比公司法

  + Control Premium（控制權溢價）
    一般 20–40%
    
  + Synergy Value Share（綜效分享）
    綜效 NPV × 分享比例
    買方通常拿 60–70%，賣方 30–40%
    
  − DD Adjustments（DD 發現調整）
    收入品質、訴訟、環安衛、技術過時

  − Working Capital Adjustment
    相對於正常化 WC 的差額

  − Tax Structure Adjustments
    買方優化結構未能充分享受的部分

  − Transaction Costs（買方）
    投行費、律師費、稅務顧問費
    
  = Transaction Value（交易對價）
```

### Bridge 的戰略意義

**對買方**
- Standalone 是「底線」
- Synergy 分享是「可談判空間」
- DD 發現是「殺價依據」

**對賣方**
- 強調 Control Premium 正當性
- 強調 Synergy 多由賣方創造
- 接受必要的 DD 調整

### 實務談判區間

```
買方底線 ← ─────── Deal Zone ─────── → 賣方底線
Standalone + 50% Synergy        Standalone + 80% Synergy
```

## 三法交叉驗證

### 收斂分析

```
Method          Low    Median    High
DCF             20億   24億      28億
可比公司        22億   26億      32億
可比交易        25億   28億      33億

合併中位數：26 億（Equity Value）
談判區間：24–30 億
```

### 不收斂時的原因

**三法差距 > 30% 常見原因**
- DCF 假設過度樂觀／保守
- 可比公司選擇不當
- 可比交易樣本太少或時期不適當
- 目標公司特殊性（單一資產過度影響）

**處理方式**
- 加權平均（依可信度賦權）
- 明確說明方法差異
- 進階：Monte Carlo 模擬

## 特殊情境估值

### 1. 高成長公司（SaaS、科技新創）

- DCF 不適用（未來獲利）
- 可比公司法用 EV/Revenue + Rule of 40
- 關鍵指標：ARR、NRR、CAC Payback

### 2. 財務困境公司

- DCF 難用
- 清算價值（Liquidation Value）
- 資產價值（Asset-based）
- Forced Sale 折扣 20–40%

### 3. 控股公司（Holding Company）

- 分業別估值後加總
- 扣控股折扣（10–25%）
- 考慮稅務結構

### 4. 家族企業

- 流動性折扣（10–30%）
- 關鍵人依賴風險
- 家族議題風險

### 5. 跨境併購

- 匯率風險
- 國家風險溢酬
- 稅務結構影響

## 估值報告結構

```
1. 執行摘要
   估值區間與建議對價

2. 三法詳細分析
   2.1 DCF
   2.2 可比公司
   2.3 可比交易

3. 估值橋
   3.1 EV to Equity
   3.2 Standalone to Transaction

4. 敏感度分析

5. 特殊調整說明
   DD 影響、WC 調整、或有負債

6. 結論與建議
   目標價、區間、談判策略

7. 附件
   Comps 清單、交易樣本、假設總表
```
