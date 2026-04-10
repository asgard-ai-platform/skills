直接寫入檔案：

```markdown
# Example: 台灣寢具品牌進軍馬來西亞市場的物流模式選擇

## Scenario

**公司背景**：眠好 (MianHao) 是一家台灣寢具品牌，主打竹纖維床墊套件，平均售價 TWD 3,800（約 USD 120）。目前在蝦皮台灣站每月銷售約 300 組。品牌負責人林小姐計畫在 2026 年 Q2 進入馬來西亞市場，在 Shopee Malaysia 和品牌官網同步銷售。

**問題**：林小姐詢問：「我們要用直郵還是先備貨在馬來西亞？一開始大概一個月能賣 80-120 組。我擔心運費太高，但又怕先備太多庫存賣不完。」

---

## Analysis

### Step 1：確認月訂單量 → 初步定位物流模型

根據決策框架：

```
Monthly orders to one country < 50 → Direct Mail
Monthly orders 50-500 → Consider Bonded Warehouse
Monthly orders > 500 → Overseas Warehouse justified
```

眠好預估月訂單 80-120 組，落在 **50-500 的保稅倉區間**，但尚未驗證市場需求，應先以低庫存風險的模式測試。

**初始建議方向**：直郵（市場驗證期）→ 視 3 個月實際數據決定是否轉保稅倉。

---

### Step 2：海關與稅務確認（馬來西亞）

| 因素 | 馬來西亞狀況 |
|------|------------|
| **De minimis 門檻** | RM 500（約 USD 108）— 低於此值免進口稅 |
| **眠好售價 USD 120** | **超過門檻**，需繳 Sales & Service Tax (SST) 約 10% |
| **HS Code** | 寢具類 6302（床用亞麻布製品）；竹纖維需確認成分混紡比例，影響 HS Code 分支 |
| **需要文件** | Commercial Invoice、Packing List、Certificate of Origin（台馬無 FTA，一般原產地證明即可）|
| **特殊限制** | 寢具無需進口許可證；若添加抗菌劑，需向 NPRA 確認化學品合規 |

**Landed Cost 計算（以 USD 120 單件為例）**：

| 項目 | 金額 |
|------|------|
| 商品成本（廠價） | USD 35 |
| 直郵運費（台灣→馬來西亞，2 kg） | USD 15 |
| 保險 | USD 1.5 |
| 進口稅（SST 10% × USD 120） | USD 12 |
| 合計 Landed Cost | **USD 63.5** |
| 售價 | USD 120 |
| 毛利率 | **47%** |

---

### Step 3：退貨成本壓力測試（IRON LAW 驗證）

寢具品類網購退貨率約 8-12%。取中間值 10%：

| 情境 | 計算 |
|------|------|
| 月銷量 100 組，退貨 10 組 | 10 件退回 |
| 退貨逆向運費（馬來西亞→台灣） | USD 18/件（含報關）|
| 退回後重整成本 | USD 5/件 |
| 退稅回收（SST） | 通常無法退，視報關方式 |
| **每月退貨損失** | USD 230（約 2.3% 月營收）|

**結論**：毛利率 47% 可承受 10% 退貨率，不觸發資金危機。若退貨率升至 20%（如尺寸問題爆發），每月額外損失 USD 460，需重新評估。

---

### Step 4：直郵 vs 保稅倉成本比較

以 **月訂單 100 組** 為基準試算：

| 模型 | 每單可變成本 | 月固定成本 | 月總成本 | 交貨時間 |
|------|------------|----------|---------|---------|
| **直郵（DHL/SF Express）** | USD 15（運費）+ USD 12（SST） = USD 27 | USD 0 | USD 2,700 | 7-14 工作天 |
| **保稅倉（Johor 自由貿易區）** | USD 6（本地配送）+ USD 12（SST，出倉時繳）= USD 18 | USD 800（倉租+操作費）| USD 2,600 | 2-4 天 |
| **海外倉（Shopee 馬來西亞倉）** | USD 4（含平台配送）| USD 1,200（頭程空運 + 入倉費）| USD 1,600 | 1-2 天 |

**損益平衡點分析**：

- 直郵 vs 保稅倉：月訂單 > **80 組** 保稅倉開始佔優
- 保稅倉 vs 海外倉：月訂單 > **200 組** 海外倉才划算（但需承擔庫存風險）

---

### Step 5：Phase 1 選擇與執行路徑

眠好 **尚未驗證馬來西亞需求**，不應貿然送大批貨進海外倉：

- Q2 前 3 個月（4-6月）：**直郵模式**，合作夥伴 SF Express MY 或 DHL Taiwan，建立文件模板
- 月訂單穩定超過 80 組且達 2 個連續月：評估轉進 **柔佛保稅倉**（接近新加坡物流樞紐，成本較低）
- 月訂單超過 200 組：重新評估 Shopee 官方倉或 Boxme MY 3PL

---

## Result

```markdown
# Cross-Border Logistics Plan: 竹纖維寢具 → 馬來西亞

## Current State
- Monthly orders: 預估 80-120 組（尚未驗證）
- Current model: 無（市場進入前）
- Avg delivery time: N/A

## Recommended Model
- **Phase 1（第 1-3 個月）**：Direct Mail（直郵）
- 理由：需求未驗證、庫存風險高；月訂單 < 保稅倉損益平衡點（80 組）；
  馬來西亞 de minimis USD 108，售價 USD 120 超過門檻需繳 SST，
  直郵與保稅倉稅負相同，固定成本優先最小化。
- **Phase 2（第 4 個月起，條件達成時）**：Bonded Warehouse（柔佛保稅倉）

## Cost Comparison（月訂單 100 組）
| Model | Per-Order Cost | Monthly Fixed | Total (100 orders) |
|-------|---------------|-------------|-------------------|
| Direct Mail | USD 27 | USD 0 | USD 2,700 |
| Bonded Warehouse | USD 18 | USD 800 | USD 2,600 |
| Overseas Warehouse | USD 4 | USD 1,200 | USD 1,600 |

> 海外倉雖然總成本最低，但需承擔頭程庫存風險 + 滯銷庫存資金佔用；
> 建議月訂單穩定達 200 組以上再評估。

## Implementation Plan
| Phase | Action | Timeline |
|-------|--------|----------|
| 1 | 申請台灣出口報單、備妥商業發票與裝箱單模板 | Week 1-2 |
| 1 | 在 Shopee MY 與品牌官網標示「7-14 工作天到貨」 | Week 1-2 |
| 1 | 與 SF Express 簽訂台馬小包協議價（100 件/月起跳） | Week 2 |
| 1 | 確認竹纖維 HS Code（建議聘台灣報關行確認 6302.22 或 6302.60）| Week 2 |
| 2 | 選定柔佛 FTZ 保稅倉，評估 Anchanto MY 或 iWarehouse | Month 3 |
| 2 | 串接 Shopee MY 訂單 API → 倉庫 WMS | Month 4 |
| 3 | 分析 SKU 退貨率，決定是否縮減 SKU 備貨種類 | Month 5+ |

## 退貨預算
- 預估退貨率：8-10%（寢具品類）
- 每月退貨損失上限：USD 230（10% 退貨率）
- 觸發警戒：退貨率 > 15% 需立即審查尺寸圖與商品說明頁
```
```
