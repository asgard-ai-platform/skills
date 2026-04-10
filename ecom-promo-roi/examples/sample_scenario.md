# Example: 雙11折扣活動值得嗎？

## Scenario

**FreshBox** 是一家台灣中型生鮮電商，每月約有 NT$8M 營收。2025 年 11 月，行銷主管 Ivy 跑來問：

> 「我們雙11辦了一個『全館8折』活動，當周營收衝到 NT$3.2M，但老闆問我這個活動到底賺了還是賠了？還有，下次年終我要不要改成滿千送百？」

她提供以下數據：
- 活動期間：2025/11/11–11/17（7 天）
- 活動形式：全館 8 折（即 20% off）
- 活動期間總營收：NT$3,200,000
- 同期廣告投放：NT$180,000
- 一般周平均營收（非旺季）：NT$1,150,000
- 去年雙11同期營收：NT$1,350,000（去年未辦活動，自然旺季峰值）
- 公司平均毛利率：38%
- 活動結束後次周（11/18–11/24）營收：NT$720,000（明顯低谷）

---

## Analysis

### Phase 1：建立 Baseline

去年同期雙11自然峰值為 NT$1,350,000，今年整體 GMV 趨勢約成長 12%，調整後 baseline 估計：

```
Adjusted Baseline = NT$1,350,000 × 1.12 = NT$1,512,000
```

### Phase 2：計算 Incremental Impact

**促銷週 Incremental：**
```
Incremental Revenue (promo week) = NT$3,200,000 - NT$1,512,000 = NT$1,688,000
```

**考慮 Pull-Forward（次周低谷）：**

次周實際營收 NT$720,000，一般正常周約 NT$1,150,000
```
Pull-Forward Amount = NT$1,150,000 - NT$720,000 = NT$430,000
```
這 NT$430,000 是顧客提早購買、下周少買的部分，不屬於真正增量。

**淨 Incremental Revenue：**
```
Net Incremental Revenue = NT$1,688,000 - NT$430,000 = NT$1,258,000
```

**Incremental Gross Profit（按原始毛利率 38%，但促銷後實際讓利 20%）：**

促銷期間售出商品的有效毛利率：
```
Effective Margin = 38% - 20% = 18%
```
（讓利 20% 直接壓縮毛利，假設 COGS 不變）

```
Incremental Gross Profit = NT$1,258,000 × 18% = NT$226,440
```

### Phase 3：計算完整 Promo Cost

| 成本項目 | 金額 |
|---------|------|
| 廣告投放 | NT$180,000 |
| 倉儲加班（爆量出貨）| NT$45,000（估）|
| 客服 spike（退換貨增加）| NT$20,000（估）|
| **Promo Cost 合計** | **NT$245,000** |

> 注意：折扣本身已反映在有效毛利率 18% 中，不再重複計算。

### Phase 4：計算 ROI

```
Promo ROI = (Incremental Gross Profit - Promo Cost) / Promo Cost
           = (NT$226,440 - NT$245,000) / NT$245,000
           = -NT$18,560 / NT$245,000
           = -7.6%
```

**結論：這次全館8折活動小幅虧損。**

### 滿千送百（$ Off）情境模擬

若改為「滿 NT$1,000 送 NT$100」（等效折扣率約 10%，且僅在高 AOV 訂單觸發）：

假設：
- 觸發率 65%（部分訂單未達門檻）
- 等效平均折扣率 = 10% × 65% = 6.5%
- 仍假設相同的 NT$1,688,000 Incremental（保守），同樣 NT$430,000 pull-forward

```
Effective Margin = 38% - 6.5% = 31.5%
Incremental Gross Profit = NT$1,258,000 × 31.5% = NT$396,270
Promo ROI = (NT$396,270 - NT$245,000) / NT$245,000 = +61.7%
```

---

## Result

```markdown
# Promo ROI Report: FreshBox 雙11全館8折 2025

## Promo Summary
- Type: % Discount（全館 20% off）
- Period: 2025/11/11–11/17
- Offer: 全館 8 折，無門檻

## Results
| Metric | Value |
|--------|-------|
| Total Revenue (promo period) | NT$3,200,000 |
| Baseline Revenue (estimated) | NT$1,512,000 |
| **Incremental Revenue (gross)** | **NT$1,688,000** |
| Pull-Forward (次周低谷調整) | -NT$430,000 |
| **Net Incremental Revenue** | **NT$1,258,000** |
| Incremental Gross Profit (@ 18%) | NT$226,440 |
| Promo Cost (ads + ops) | NT$245,000 |
| **Promo ROI** | **-7.6%** |

## Profitability Assessment
**小幅虧損。** 表面上的 NT$3.2M 亮眼數字掩蓋了兩個問題：
1. NT$1.5M 的基礎量本來就會發生，促銷只帶來 NT$1.26M 真正增量
2. 20% 折扣壓縮了本就不高的毛利，每賣一塊錢增量只剩 0.18 元毛利

## Recommendation
**修改：勿重複 20% 全館折扣；改為滿千送百。**

模擬顯示同樣活動規模下，滿千送百的 ROI 可達 +61.7%，原因：
- 平均有效折扣率從 20% 降至 6.5%
- 設定消費門檻同時拉升 AOV
- 保護了品牌訂價形象，不訓練顧客「等打折」

**額外觀察**：需追蹤本次活動帶來的新客比例。若新客佔比 > 30% 且後續回購率正常，
-7.6% 的 ROI 可能因 LTV 而翻正——建議 60 天後回頭驗算新客貢獻。
```
