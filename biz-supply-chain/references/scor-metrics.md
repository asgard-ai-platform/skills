# SCOR Model Metrics Reference

SCOR 將指標分為三層：**Level 1（策略）→ Level 2（診斷）→ Level 3（追蹤）**。本文件聚焦在 Level 1 與 Level 2，涵蓋完整公式、產業基準與計算範例。

---

## 指標架構：Reliability / Responsiveness / Agility / Cost / Assets

SCOR 的五大屬性橫跨所有流程：

| 屬性 | 衡量什麼 | 主要代表指標 |
|------|---------|------------|
| **Reliability**（可靠度） | 你說到做到嗎？ | Perfect Order Rate |
| **Responsiveness**（回應速度） | 多快完成訂單？ | Order-to-Delivery Cycle |
| **Agility**（靈活度） | 能應對需求波動嗎？ | Upside Supply Chain Flexibility |
| **Cost**（成本） | 供應鏈運作成本多少？ | Total Supply Chain Cost |
| **Assets**（資產效率） | 資產利用率如何？ | Cash-to-Cash Cycle Time |

---

## Process 1：Plan

### 1.1 Forecast Accuracy（預測準確率）

```
Forecast Accuracy = 1 - (|Actual - Forecast| / Actual)
```

**計算範例：**

| SKU | 預測量 | 實際量 | |Actual - Forecast| | FA per SKU |
|-----|-------|-------|-------------------|-----------|
| A01 | 1,000 | 1,150 | 150 | 87.0% |
| A02 | 500 | 420 | 80 | 81.0% |
| A03 | 2,000 | 2,050 | 50 | 97.6% |

加權平均 FA（以銷售量加權）：
```
Weighted FA = Σ(Actual_i × FA_i) / Σ(Actual_i)
            = (1150 × 87.0% + 420 × 81.0% + 2050 × 97.6%) / (1150 + 420 + 2050)
            = (1000.5 + 340.2 + 2000.8) / 3620
            = 3341.5 / 3620
            = 92.3%
```

**產業基準：**
- 消費品（穩定品項）：85–92%
- 電子產品（季節性）：75–85%
- 時尚服飾：60–75%（天花板，因需求本質難預測）
- < 70% 視為警戒，需啟動 S&OP 改善

**常見陷阱：** 別用「平均絕對誤差（MAE）」取代 FA 向高層報告——MAE 沒有方向性，無法區分「短缺」與「積壓」。

---

### 1.2 Inventory Days（庫存天數）

```
Inventory Days (DOI) = Inventory Value / (Annual COGS / 365)
```

或等效地：
```
DOI = Inventory Value × 365 / Annual COGS
```

**三種分類計算（更有診斷價值）：**

| 庫存類型 | 公式 |
|---------|------|
| Raw Material DOI | Raw Material Inventory / (Annual Material Cost / 365) |
| WIP DOI | WIP Inventory / (Annual COGS / 365) |
| Finished Goods DOI | FG Inventory / (Annual COGS / 365) |

**產業基準（Finished Goods）：**
- 電商（快時尚）：15–25 天
- 消費電子：20–35 天
- 工業製造：30–60 天
- 汽車零件：45–90 天

**警示：** DOI 飆高通常是 Forecast Accuracy 低的滯後指標，先修 Plan 再看庫存改善。

---

### 1.3 Inventory Turnover（庫存周轉率）

```
Inventory Turnover = Annual COGS / Average Inventory
```
（DOI 的倒數乘以 365）

---

## Process 2：Source

### 2.1 Supplier On-Time Delivery Rate（供應商準時交貨率）

```
Supplier OTD = On-Time Deliveries / Total Deliveries × 100%
```

「準時」的定義必須事先與供應商白紙黑字約定：

| 定義版本 | 說明 |
|---------|------|
| **Strict** | 僅限合約日期當天 |
| **Window** | 合約日期 ±1 天 |
| **Early** | 提早交貨不罰，遲交才扣分 |

建議採用 **Strict** 版本做內部追蹤，Window 版本做供應商 SLA。

**供應商評分卡範例：**

| 評分項目 | 權重 | 計算方式 | 本季得分 |
|---------|------|---------|---------|
| OTD Rate | 30% | 實際 OTD % | 88% → 26.4 |
| Defect Rate | 25% | 100% - Defect% | 98.5% → 24.6 |
| Lead Time Consistency | 20% | 1 - StdDev(LT)/Mean(LT) | 85% → 17.0 |
| Invoice Accuracy | 15% | Correct invoices / Total | 96% → 14.4 |
| Responsiveness | 10% | 問題回應 <48h 比率 | 90% → 9.0 |
| **Total** | 100% | | **91.4 / 100** |

分級：≥90 A 級（策略供應商）、75–89 B 級（改善計畫）、<75 C 級（尋求替代）

---

### 2.2 Supplier Defect Rate（供應商不良率）

```
Supplier Defect Rate = Defective Units Received / Total Units Received × 100%
```

**產業基準：**
- 汽車 Tier-1：< 50 PPM（parts per million）
- 消費電子：< 0.5%（5,000 PPM）
- 一般製造：< 1–2%

---

### 2.3 Total Landed Cost（完整採購成本）

採購決策不能只看 Unit Price：

```
Total Landed Cost = Unit Price
                  + Freight Cost
                  + Import Duty & Taxes
                  + Customs Brokerage
                  + Warehousing-in-Transit
                  + Inspection Cost
                  + Payment Terms Cost (if not Net-0)
```

**Payment Terms Cost 計算：**
```
Payment Terms Cost = Invoice Amount × Annual Cost of Capital × (Payment Days / 365)
```

範例：供應商 A 報價 $100/unit（Net 60），供應商 B 報價 $102/unit（Net 0），資金成本 8%：
```
A: $100 + $100 × 8% × (60/365) = $100 + $1.32 = $101.32
B: $102 + $0 = $102.00
```
→ 看似貴的 B 其實 Landed Cost 更高，但差距很小；若 A 的 OTD 更差，可能反而更貴。

---

## Process 3：Make

### 3.1 OEE（Overall Equipment Effectiveness，設備綜合效率）

```
OEE = Availability × Performance × Quality
```

三個因子分解：

```
Availability  = (Planned Production Time - Downtime) / Planned Production Time
Performance   = (Ideal Cycle Time × Total Units Produced) / Run Time
Quality       = Good Units / Total Units Started
```

**實際計算範例：**

- 每班計劃工時：8 小時 = 480 分鐘
- 計劃停機（換線、休息）：30 分鐘 → Planned Production Time = 450 分鐘
- 非計劃停機：45 分鐘 → Run Time = 405 分鐘
- Ideal Cycle Time：0.5 分鐘/件
- 實際生產：750 件
- 良品：720 件

```
Availability  = (450 - 45) / 450 = 405 / 450 = 90.0%
Performance   = (0.5 × 750) / 405 = 375 / 405 = 92.6%
Quality       = 720 / 750 = 96.0%

OEE = 90.0% × 92.6% × 96.0% = 80.0%
```

**產業基準：**
- World-class 製造：≥ 85%
- 一般製造平均：60–70%
- < 60%：嚴重問題，需立即啟動 TPM

**OEE 診斷方向：**

| 哪個因子低 | 根因方向 |
|-----------|---------|
| Availability 低 | 設備故障、維護不足、換線時間過長 |
| Performance 低 | 操作員技能、材料供給不穩、速度損失 |
| Quality 低 | 製程參數、材料品質、設計問題 |

---

### 3.2 Production Schedule Adherence（生產計劃達成率）

```
PSA = Actual Output / Planned Output × 100%
```

不要與 OEE 混淆：PSA 衡量「計劃執行率」，OEE 衡量「設備效率」。PSA 低可能是因為計劃本身不合理（需求預測差），而非生產能力問題。

---

## Process 4：Deliver

### 4.1 Perfect Order Rate（完美訂單率）——SCOR 最重要的 Level 1 指標

完美訂單 = 同時滿足以下四個條件的訂單：

```
Perfect Order Rate = (Orders On-Time) × (Orders In-Full) × (Orders Damage-Free) × (Orders with Correct Documentation) / Total Orders × 100%
```

**乘法結構（不是加法）** 是關鍵——任一環節失敗就不算完美訂單。

**計算範例：**

| 條件 | 達成率 |
|------|-------|
| On-Time | 96% |
| In-Full | 98% |
| Damage-Free | 99% |
| Correct Docs | 99.5% |
| **Perfect Order Rate** | **96% × 98% × 99% × 99.5% = 93.1%** |

即使每個環節都在 96–99.5% 之間，完美訂單率只有 93.1%。這就是為什麼末端客戶體驗往往比企業內部認知的差。

**產業基準：**
- 電商領先企業：≥ 95%
- 一般 B2C：88–93%
- B2B 製造業：90–95%

---

### 4.2 Order-to-Delivery Cycle Time（訂單交付週期）

```
O2D Cycle = Order Receipt → Order Processing → Warehouse Pick/Pack → Carrier Pickup → In-Transit → Last-Mile Delivery
```

分段追蹤，而非只看總時間：

| 階段 | 說明 | 典型時間（電商） |
|------|------|----------------|
| Order Processing | 訂單確認、付款核對、ERP 建單 | 0–4 小時 |
| Pick & Pack | 揀貨、包裝、標籤 | 2–24 小時 |
| Carrier Pickup | 等待取件 | 0–24 小時 |
| In-Transit | 幹線運輸 | 12–72 小時 |
| Last-Mile | 配送至消費者 | 4–24 小時 |

**分段追蹤才能定位瓶頸**：若 O2D 偏長，先看哪個階段的 P95 時間最大，而非整體平均。

---

### 4.3 Fill Rate vs. Order Fill Rate（填充率）

兩個常被混淆的指標：

```
Line Fill Rate  = Order Lines Shipped Complete / Total Order Lines
Order Fill Rate = Orders Shipped Complete / Total Orders
```

Order Fill Rate 更嚴格——一張訂單中任一 line item 缺貨就不算完整出貨。

---

## Process 5：Return

### 5.1 Return Rate（退貨率）

```
Return Rate = Units Returned / Units Shipped × 100%
```

退貨分類對診斷更有價值：

| 退貨原因 | 典型比率（電商） | 處置方向 |
|---------|---------------|---------|
| 商品描述不符 | 20–30% | 修改商品文案、圖片 |
| 尺寸/規格不符 | 25–35% | 尺碼建議工具、詳細規格 |
| 品質問題 | 10–20% | 追溯至 Make/Source |
| 物流損壞 | 5–15% | 包材升級、物流商 SLA |
| 買家改變心意 | 15–25% | 退貨政策設計 |

**產業基準：**
- 服飾電商：25–40%（天然高，不必恐慌）
- 消費電子：5–15%
- 工業品：< 3%

---

### 5.2 Reverse Logistics Cost Rate

```
RL Cost Rate = Total Reverse Logistics Cost / Total Forward Logistics Cost × 100%
```

業界估計：退貨處理成本約為正向出貨成本的 **1.5–2.5 倍**，因為需要增加揀選、檢驗、再分類、維修或銷毀等工序。

---

## Level 1 Dashboard 完整基準彙整

| Process | 指標 | 世界級基準 | 警戒線 |
|---------|------|-----------|-------|
| Plan | Forecast Accuracy | ≥ 85% | < 70% |
| Plan | Inventory DOI | 視品類 | 超過品類均值 50% |
| Source | Supplier OTD | ≥ 95% | < 85% |
| Source | Supplier Defect Rate | < 0.5% | > 2% |
| Make | OEE | ≥ 85% | < 65% |
| Make | PSA | ≥ 95% | < 85% |
| Deliver | Perfect Order Rate | ≥ 95% | < 88% |
| Deliver | O2D Cycle | 視通路 | 超過競品均值 |
| Return | Return Rate | 視品類 | 超過品類均值 20% |

---

## 優先序：當多個流程同時低於警戒線

遵循 TOC（Theory of Constraints）邏輯——找出制約點，不要同時改善所有流程：

1. **計算每個流程與基準的 Gap %**（Current vs. Benchmark）
2. **評估 Gap 對客戶體驗的影響**（Deliver 的 Gap 直接影響客戶，Plan 的 Gap 是根因）
3. **改善順序**：根因 Process 優先（通常是 Plan），即使症狀出現在 Deliver

**決策矩陣：**

| 症狀 | 表面流程 | 真正根因（優先改） |
|------|---------|----------------|
| 常常缺貨 | Deliver | Plan（FA 低）或 Source（OTD 低）|
| 客戶等太久 | Deliver | Make（OEE 低→產能不足）|
| 庫存堆積 | Plan | Plan（FA 低，預測偏高）|
| 退貨率高（品質原因） | Return | Make 或 Source |
| 總成本高 | Cost | 需跨流程分解，逐一排查 |
