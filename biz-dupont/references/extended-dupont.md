# Extended DuPont Analysis (5-Factor Decomposition)

5-factor DuPont 在 3-factor 基礎上將 Net Profit Margin 拆解為三個子因子，讓分析者看清楚稅負、利息負擔、與營業獲利能力各自對 ROE 的貢獻。

---

## 公式結構

### 3-Factor（基礎）

```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
    = (Net Income / Revenue) × (Revenue / Total Assets) × (Total Assets / Equity)
```

### 5-Factor（擴展）

```
ROE = Tax Burden × Interest Burden × Operating Margin × Asset Turnover × Equity Multiplier

    = (Net Income / EBT)
    × (EBT / EBIT)
    × (EBIT / Revenue)
    × (Revenue / Total Assets)
    × (Total Assets / Equity)
```

其中：
- **EBT** = Earnings Before Tax（稅前盈餘）
- **EBIT** = Earnings Before Interest and Tax（息前稅前盈餘）

### 因子定義速查

| 因子 | 公式 | 範圍 | 直覺解釋 |
|------|------|------|----------|
| Tax Burden（稅負率） | Net Income / EBT | 0–1 | 每賺 1 元稅前盈餘保留多少；稅率越高，數值越低 |
| Interest Burden（利息負擔） | EBT / EBIT | 通常 < 1 | 每賺 1 元 EBIT 扣掉利息後剩多少；負債越重，數值越低 |
| Operating Margin（營業利益率） | EBIT / Revenue | 可負值 | 核心業務本身的獲利能力，不受稅與資本結構影響 |
| Asset Turnover（資產週轉率） | Revenue / Total Assets | — | 同 3-factor，不變 |
| Equity Multiplier（槓桿倍數） | Total Assets / Equity | ≥ 1 | 同 3-factor，不變 |

> **注意**：Tax Burden 與 Interest Burden 的直覺是「留下的比例」，不是「被扣掉的比例」。Tax Burden = 0.75 表示稅後保留 75%，有效稅率約 25%。

---

## 何時用 5-Factor 而非 3-Factor

| 情境 | 建議 |
|------|------|
| 跨國企業比較（稅率不同） | **用 5-factor**，隔離 Tax Burden 差異 |
| 比較有息負債差異很大的同業 | **用 5-factor**，隔離 Interest Burden |
| 快速診斷、單一公司趨勢 | 3-factor 足夠 |
| 公司負債極少、稅率穩定 | 5-factor 增加複雜度但增益有限 |
| 負股東權益情況 | 兩者都失效，改用 ROIC 或 ROCE |

---

## 逐步計算程序

### Step 1：從損益表取值

```
Revenue        = 營業收入淨額
EBIT           = 營業利益（Operating Income）
                 若報表未列，可用 EBT + Interest Expense 還原
EBT            = 稅前淨利（Pre-tax Income）
Net Income     = 本期淨利
```

### Step 2：從資產負債表取值

```
Total Assets   = 資產總額（建議取期初期末平均）
Equity         = 股東權益總額（同樣建議平均）
```

### Step 3：計算五個因子

```python
tax_burden       = net_income / ebt           # 若 ebt < 0 須特殊處理
interest_burden  = ebt / ebit                 # 若 ebit < 0 須標註
operating_margin = ebit / revenue
asset_turnover   = revenue / total_assets
equity_multiplier = total_assets / equity

roe_check = (tax_burden * interest_burden * operating_margin
             * asset_turnover * equity_multiplier)
# roe_check 應等於 net_income / equity（允許浮點誤差）
```

### Step 4：驗證乘積

中間項目的分子分母相消後：

```
(Net Income/EBT) × (EBT/EBIT) × (EBIT/Revenue) × (Revenue/Assets) × (Assets/Equity)
= Net Income / Equity
= ROE  ✓
```

若計算結果與直接算出的 ROE 誤差超過 0.1%，先檢查是否混用了不同時間點的資產負債數字。

---

## 完整試算範例

### 情境：台灣兩家製造商 A 與 B

| 損益/資產負債科目 | 公司 A | 公司 B |
|------------------|--------|--------|
| Revenue | 10,000 | 10,000 |
| EBIT | 1,200 | 1,200 |
| Interest Expense | 100 | 600 |
| EBT | 1,100 | 600 |
| Tax (25%) | 275 | 150 |
| Net Income | 825 | 450 |
| Total Assets | 8,000 | 8,000 |
| Equity | 5,000 | 2,000 |

### 計算 5 個因子

| 因子 | 公司 A | 公司 B |
|------|--------|--------|
| Tax Burden | 825/1,100 = **0.750** | 450/600 = **0.750** |
| Interest Burden | 1,100/1,200 = **0.917** | 600/1,200 = **0.500** |
| Operating Margin | 1,200/10,000 = **12.0%** | 1,200/10,000 = **12.0%** |
| Asset Turnover | 10,000/8,000 = **1.25×** | 10,000/8,000 = **1.25×** |
| Equity Multiplier | 8,000/5,000 = **1.60×** | 8,000/2,000 = **4.00×** |
| **ROE** | 0.750×0.917×0.12×1.25×1.60 = **16.5%** | 0.750×0.500×0.12×1.25×4.00 = **22.5%** |

### 診斷

- 兩家公司的 **Operating Margin、Asset Turnover、Tax Burden 完全相同** — 核心業務獲利能力一致。
- ROE 差距完全來自 **Interest Burden（0.917 vs 0.500）** 與 **Equity Multiplier（1.60× vs 4.00×）**：公司 B 大量舉債，利息吃掉一半 EBIT，但槓桿拉高了 ROE。
- 若用 3-factor 分析，Net Profit Margin（A: 8.25% vs B: 4.50%）會顯示 A 獲利能力更好，掩蓋了「B 的 ROE 來自純粹財務槓桿」這個事實。

> **Iron Law 強化**：公司 B 的 Equity Multiplier = 4.0×，Interest Burden = 0.50，已符合「槓桿為主要 ROE 驅動力」的紅旗條件。必須在報告中明確標注槓桿風險，不得僅以 ROE 22.5% 定性為優異表現。

---

## 跨稅率比較的隔離技術

當比較不同稅率國家（例如台灣 vs 新加坡 vs 美國）的公司時：

### 做法：固定稅率後比較

1. 找出各公司的**標準化稅率**（可用行業平均值，如 20%）
2. 計算**標準化 Net Income** = EBT × (1 − 標準化稅率)
3. 用標準化數字計算 3-factor ROE
4. 差異即為「排除稅率效果後的營運/槓桿差距」

### 或者：直接比較 5-factor 中的子因子

| 公司 | Tax Burden | Interest Burden | Op. Margin | Turnover | Multiplier | ROE |
|------|-----------|----------------|-----------|---------|------------|-----|
| 台廠（稅率 20%） | 0.80 | 0.92 | 10% | 1.5× | 2.0× | 22.1% |
| 新加坡同業（稅率 17%） | 0.83 | 0.95 | 10% | 1.5× | 2.0× | 23.5% |
| 美廠（稅率 21%） | 0.79 | 0.88 | 10% | 1.5× | 2.0× | 20.9% |

結論：Operating Margin、Turnover、Multiplier 三者相同 → ROE 差距純屬稅率與利率環境差異，非核心競爭力差距。

---

## 特殊情況處理

### 情況 1：EBIT 為負

Interest Burden = EBT / EBIT 在 EBIT < 0 時數學上仍可計算，但方向性會逆轉（例如 EBT = -80, EBIT = -100 → Interest Burden = 0.80，表面上「利息負擔不重」，實際上是公司虧損狀態）。

**處置方式**：

- 標記「虧損年度，5-factor 分解方向性失真」
- 改以絕對值報告：EBIT loss = X，Interest Expense = Y，EBT loss = X+Y
- 不繪製因子趨勢圖，改用瀑布圖（waterfall chart）呈現損益缺口

### 情況 2：EBT 為負、Net Income 為正

發生於稅務利益（deferred tax asset 認列）大於 EBT 損失時。Tax Burden > 1。

**處置方式**：標注「稅務利益年度」，並補充一次性稅務項目說明。5-factor 數學上成立，但解讀需特別說明。

### 情況 3：負股東權益

Equity Multiplier 無意義（可能為負值或極大值）。

**替代做法**：

| 替代指標 | 公式 | 適用原因 |
|---------|------|---------|
| ROIC | NOPAT / Invested Capital | 排除資本結構影響 |
| ROCE | EBIT / Capital Employed | Capital Employed = Assets − Current Liabilities |
| ROA | Net Income / Total Assets | 完全排除 Equity 的問題 |

---

## 與 3-Factor 的對應關係

5-factor 的前三項乘積等於 3-factor 的 Net Profit Margin：

```
Net Profit Margin（3-factor）
= Tax Burden × Interest Burden × Operating Margin（5-factor）
= (Net Income/EBT) × (EBT/EBIT) × (EBIT/Revenue)
= Net Income / Revenue  ✓
```

因此 **5-factor 是 3-factor 的嚴格超集**；任何 3-factor 分析都可以「升級」為 5-factor，只需額外取得 EBIT 和 EBT 數字。

---

## 快速判斷樹：哪個因子需要深挖？

```
ROE 下滑
│
├─ Operating Margin 下滑？
│   ├─ 是 → 核心業務問題：定價力、成本控制、產品組合
│   └─ 否 ↓
│
├─ Asset Turnover 下滑？
│   ├─ 是 → 效率問題：應收帳款天數、庫存週轉、閒置產能
│   └─ 否 ↓
│
├─ Interest Burden 下滑？
│   ├─ 是 → 利息負擔加重：新增借款？利率上升？
│   └─ 否 ↓
│
├─ Tax Burden 下滑？
│   ├─ 是 → 稅率上升或優惠到期：確認稅務變動
│   └─ 否 ↓
│
└─ Equity Multiplier 下滑？
    └─ 是 → 去槓桿：還債、增資稀釋，ROE 下滑但財務更健康
               （此情況 ROE 下滑未必是壞事）
```
