# Cohort LTV Projection from Retention Data

LTV (Lifetime Value) 是每個 cohort 在其整個生命週期內帶來的總收益現值。從 cohort retention 資料推算 LTV，是最直接、最少假設的方法——因為 retention 曲線本身就是從真實使用者行為觀測得到的。

---

## 核心公式

```
LTV = Σ (retention_n × ARPU_n × discount_n)
      for n = 0, 1, 2, ... until curve flattens near zero
```

| 變數 | 定義 |
|------|------|
| `retention_n` | Month n 的留存率（M0 = 1.0） |
| `ARPU_n` | Month n 的每活躍用戶平均收益 |
| `discount_n` | 第 n 期的折現因子 = `1 / (1 + r)^n`，r = 月折現率 |

若 ARPU 各月相同（簡化假設），可提出：

```
LTV = ARPU × Σ (retention_n × discount_n)
```

---

## 最小可用資料集

開始計算前，你需要：

1. **Retention matrix**：至少 6 個月觀測資料，或 retention 曲線已明顯趨平
2. **ARPU（per cohort, per month）**：訂閱制用 MRR/活躍用戶；交易制用月均消費/活躍用戶
3. **折現率**：B2C SaaS 常用 10% 年利率（≈ 0.80% 月利率）；若不確定，用 0 先算未折現 LTV

---

## 步驟一：整理 Cohort Retention 曲線

以下用虛構的 SaaS 產品示範。2024-01 cohort，起始 1,000 名用戶：

| 月份 | 存活人數 | Retention |
|------|---------|-----------|
| M0 | 1,000 | 100.0% |
| M1 | 650 | 65.0% |
| M2 | 480 | 48.0% |
| M3 | 400 | 40.0% |
| M4 | 370 | 37.0% |
| M5 | 355 | 35.5% |
| M6 | 348 | 34.8% |

曲線在 M4-M6 趨於平緩，表示已形成穩定核心用戶群（**flattening tail**）。

---

## 步驟二：決定要觀測多少個月

問題：資料只到 M6，但用戶可能繼續付款 2-3 年。

有三種處理方式：

### 方法 A：截斷計算（保守，有觀測值才算）

只計算已觀測的 M0–M6。LTV 被低估，但 100% 基於真實資料。

### 方法 B：外推平穩期（常用）

若 retention 曲線在 M4 後趨平，假設此後每月 retention = 最後幾期平均值，直到合理的截止月份（通常 24-36 個月）。

外推規則：
- 取 M4–M6 平均 retention：(37.0% + 35.5% + 34.8%) / 3 ≈ **35.8%**
- M7 以後每月 retention 固定為 35.8%（相對於 M0，不是環比）
- 截止月份設為 M24

### 方法 C：數學模型擬合（需要足夠資料點）

用 shifted-Beta-geometric (sBG) 模型或負二項模型擬合 retention 曲線，再預測未來。適合資料足夠（>12 個月觀測）且需要更精確 LTV 的場景。本文不展開；見 Fader & Hardie 2007。

---

## 步驟三：計算 LTV（方法 B，外推至 M24）

**假設**：
- ARPU = $20/月（固定，簡化）
- 月折現率 r = 0.83%（對應年化 10%）
- M7–M24 retention 固定為 35.8%

折現因子公式：`d_n = 1 / (1.0083)^n`

| 月份 | Retention | ARPU | Discount | 折現收益 |
|------|-----------|------|----------|---------|
| M0 | 100.0% | $20 | 1.0000 | $20.00 |
| M1 | 65.0% | $20 | 0.9918 | $12.89 |
| M2 | 48.0% | $20 | 0.9836 | $9.44 |
| M3 | 40.0% | $20 | 0.9754 | $7.80 |
| M4 | 37.0% | $20 | 0.9673 | $7.16 |
| M5 | 35.5% | $20 | 0.9593 | $6.81 |
| M6 | 34.8% | $20 | 0.9513 | $6.62 |
| M7 | 35.8% | $20 | 0.9434 | $6.76 |
| M8 | 35.8% | $20 | 0.9356 | $6.71 |
| … | … | … | … | … |
| M24 | 35.8% | $20 | 0.8195 | $5.87 |

**M0–M6 實測 LTV（折現）**：$20.00 + $12.89 + ... ≈ **$70.72**

**M7–M24 外推 LTV（折現）**：18 個月 × 35.8% × $20 × 平均折現因子(≈ 0.877) ≈ **$112.58**

**總 LTV（24 個月）≈ $183**

---

## 步驟四：Python 計算腳本

```python
def compute_ltv(retentions, arpu_per_month, monthly_discount_rate=0.0083,
                plateau_retention=None, project_to_month=24):
    """
    retentions: list of observed retention rates, e.g. [1.0, 0.65, 0.48, ...]
                Index = month number (M0 = index 0)
    arpu_per_month: float or list; if float, assumed constant
    plateau_retention: float; if set, extend curve beyond observed data
    project_to_month: final month to include in LTV calculation
    """
    if isinstance(arpu_per_month, (int, float)):
        arpu_per_month = [arpu_per_month] * (project_to_month + 1)

    full_retentions = list(retentions)

    # extend with plateau if needed
    if plateau_retention is not None:
        while len(full_retentions) <= project_to_month:
            full_retentions.append(plateau_retention)

    ltv = 0.0
    breakdown = []
    for n in range(min(len(full_retentions), project_to_month + 1)):
        ret = full_retentions[n]
        arpu = arpu_per_month[n] if n < len(arpu_per_month) else arpu_per_month[-1]
        discount = 1 / (1 + monthly_discount_rate) ** n
        contribution = ret * arpu * discount
        ltv += contribution
        breakdown.append({
            "month": n,
            "retention": ret,
            "arpu": arpu,
            "discount": round(discount, 4),
            "contribution": round(contribution, 2),
            "cumulative_ltv": round(ltv, 2)
        })

    return ltv, breakdown


# 使用範例
retentions = [1.0, 0.65, 0.48, 0.40, 0.37, 0.355, 0.348]
ltv, breakdown = compute_ltv(
    retentions=retentions,
    arpu_per_month=20,
    monthly_discount_rate=0.0083,
    plateau_retention=0.358,
    project_to_month=24
)
print(f"24-month LTV: ${ltv:.2f}")
for row in breakdown[:8]:
    print(row)
```

---

## Cohort 間的 LTV 比較

計算多個 cohort 的 LTV 後，建立比較表：

| Cohort | M1 Ret | M3 Ret | M6 Ret | Plateau | 24M LTV |
|--------|--------|--------|--------|---------|---------|
| 2024-01 | 65% | 40% | 35% | 35.8% | $183 |
| 2024-02 | 60% | 35% | 30% | 30.2% | $157 |
| 2024-03 | 70% | 48% | 41% | 40.5% | $208 |
| 2024-04 | 68% | 45% | 39% | — | 待補 |

**閱讀要點**：

- 2024-03 cohort LTV 比 2024-01 高 14%——此時間點發生了什麼？（對應到產品 changelog、onboarding 改版、行銷渠道切換）
- 2024-02 是最差 cohort——排查是否為特定獲客渠道帶來低質量用戶

---

## ARPU 不恆定時的處理

訂閱制常見情況：早期月份 ARPU 較低（試用、折扣），後期趨於穩定。

```python
# 非均一 ARPU 範例
arpu_schedule = [
    5.0,   # M0: 試用月 $5
    15.0,  # M1: 標準月費開始
    20.0,  # M2
    20.0,  # M3+
]
# 傳入 list 即可；腳本會對超出部分使用最後一個值
ltv, _ = compute_ltv(
    retentions=retentions,
    arpu_per_month=arpu_schedule,
    plateau_retention=0.358,
    project_to_month=24
)
```

電商（非訂閱）：ARPU 可能隨 cohort 年齡增加（老客戶購買頻率提升）。此時建議觀測「月均消費 by cohort age」作為 ARPU 輸入，而非全局 ARPU。

---

## 折現率選取指引

| 場景 | 建議月折現率 | 年化等效 |
|------|------------|---------|
| 早期新創（資本成本高） | 1.5–2.0% | 19–27% |
| 成長期 SaaS | 0.8–1.0% | 10–13% |
| 穩定大公司 | 0.4–0.6% | 5–7% |
| 不折現（比較基準） | 0% | 0% |

若不確定，**先用 0% 算名義 LTV**，再用 10% 年化算折現 LTV，兩個數字一起報告。折現的影響在 24 個月 LTV 中通常為 10-15%，不是決定性差異。

---

## 常見陷阱

**把 M0 retention = 100% 的收益重複計算**：M0 是獲客當月，cost 通常在同期計算，LTV 包含 M0 收益是正確的——但 CAC 比較時要確認兩者口徑一致（都含或都不含 M0）。

**外推過於激進**：retention 曲線尚未趨平（仍在下降）就假設 plateau，會嚴重高估 LTV。至少等到「連續 2–3 個月環比降幅 < 1pp」才啟用 plateau 假設。

**用全局 ARPU 代替 cohort-specific ARPU**：不同 cohort 可能來自不同渠道，消費力有差異。用全局 ARPU 會把高消費 cohort 的 LTV 低估、低消費 cohort 的 LTV 高估。

**忽略 cohort 大小**：10 人 cohort 的 LTV 估算方差極大，不應與 1,000 人 cohort 同等權重比較。報告時附上 cohort 大小。

**LTV > CAC 就停止分析**：LTV/CAC > 3 是常見門檻，但更重要的是 **payback period**（幾個月回收 CAC）。LTV 很高但 payback 需要 18 個月，現金流壓力同樣致命。

---

## Payback Period 計算

```
Payback Period = 最小 n，使得 cumulative_ltv(n) >= CAC
```

從上方 `breakdown` 表的 `cumulative_ltv` 欄位直接讀取即可：

```python
cac = 80  # 獲客成本 $80

payback = None
for row in breakdown:
    if row["cumulative_ltv"] >= cac:
        payback = row["month"]
        break

print(f"Payback period: Month {payback}")
# → Payback period: Month 6
```

若 24 個月內 `cumulative_ltv` 仍未超過 CAC，該 cohort 是虧損的。
