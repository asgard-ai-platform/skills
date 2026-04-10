# Example: 電商會員流失預測前的 EDA — PChome 商城訂單資料集

## Scenario

PChome 商城資料科學團隊準備建立「會員 90 天流失預測」模型。分析師拿到一份從
2024-01-01 到 2025-03-31 的訂單與會員資料，共 15 個欄位、約 320,000 筆紀錄，
想知道：「這份資料的狀況如何？有沒有問題要先處理？」

原始資料欄位：
`member_id`, `order_date`, `order_amount`, `item_count`, `category`,
`payment_method`, `is_member_plus`, `member_since`, `last_login_days`,
`refund_amount`, `coupon_used`, `device_type`, `region`, `support_tickets`,
`churned_90d`（目標變數，1 = 90 天內未再購買）

---

## Analysis

### Step 0：先切分，再探索

資料集共 320,412 筆，依 `member_id` 做 stratified split（按 `churned_90d` 分層）：

- Train: 256,329 筆（80%）
- Test: 64,083 筆（20%）

**後續所有 EDA 只看 train set。** 資料品質檢查（空值、型別、重複）例外，可先
在全資料集跑一次，但分布分析嚴格限於 train。

---

### Step 1：資料品質掃描（全資料集）

| Issue | 欄位 | 數量 / 比例 | 初步行動 |
|-------|------|------------|---------|
| 缺失值 | `refund_amount` | 87,213 / 27.2% | 見下方 MNAR 分析 |
| 缺失值 | `last_login_days` | 4,109 / 1.3% | 隨機缺失，中位數補值 |
| 缺失值 | `support_tickets` | 891 / 0.3% | 補 0（無票=0 張） |
| 重複 member_id | — | 312 筆（同一 member_id 出現兩次，訂單日期不同） | 保留，為正常多筆訂單 |
| 異常值 | `order_amount` | 23 筆 > 500,000 | 調查後為企業採購帳號，標記但保留 |

**`refund_amount` 缺失值 MNAR 調查：**

缺失的 87,213 筆中，92% 的 `is_member_plus = 0`（非 Plus 會員）。
交叉比對退款流程文件：非 Plus 會員走第三方退款，系統不回寫
`refund_amount`，故缺失 = 「非 Plus 會員未退款或退款金額未記錄」，
屬 MNAR（Missing Not at Random）。

**處置**：不用均值填補。新增二元欄位 `refund_data_available`（0/1），
`refund_amount` 缺失處填 0，並在模型階段與 `is_member_plus` 交互作用。

---

### Step 2：單變數分布（Train Set，N = 256,329）

| 變數 | Mean | Median | Std | Min | Max | 分布形狀 |
|------|------|--------|-----|-----|-----|---------|
| `order_amount` | 1,842 | 890 | 4,210 | 59 | 498,000 | 重度右偏（log-normal） |
| `item_count` | 2.4 | 2 | 1.9 | 1 | 48 | 右偏，眾數 = 1 |
| `last_login_days` | 34.2 | 18 | 51.7 | 0 | 365 | 右偏 |
| `support_tickets` | 0.31 | 0 | 0.82 | 0 | 12 | 零膨脹計數分布 |

`order_amount` 建議 log 轉換後再用於模型；`support_tickets` 考慮用
Poisson 或負二項分布。

---

### Step 3：雙變數分析與 Simpson's Paradox 檢查

**初始發現**：`coupon_used = 1` 的會員，流失率 41%，比未使用折價券的 38% 高。
→ 表面上「用折價券的人更容易流失」。

**分層後（按 `is_member_plus`）：**

| 族群 | coupon_used=1 流失率 | coupon_used=0 流失率 |
|------|---------------------|---------------------|
| Plus 會員 | 22% | 28% |
| 非 Plus 會員 | 51% | 58% |

**兩個子群組內，使用折價券的人流失率都比較低。** 聚合趨勢反轉 = Simpson's
Paradox。原因：非 Plus 會員佔折價券使用者的 78%，拉高了整體流失率。

**結論**：折價券本身可能有留客效果，但效果被 Plus 會員身份遮蔽。建模時必須
加入 `coupon_used × is_member_plus` 交互項，或分群建模。

---

### Step 4：資料洩漏偵測

計算所有數值特徵與 `churned_90d` 的 Pearson r：

| 特徵 | r | 備註 |
|------|---|------|
| `refund_amount` | **0.97** | 🚨 洩漏嫌疑 |
| `last_login_days` | 0.61 | 合理，登入越久越容易流失 |
| `support_tickets` | 0.38 | 合理 |
| `order_amount` | -0.22 | 合理，高消費黏著度高 |

`refund_amount` 與目標相關係數 0.97——調查後發現：**退款紀錄本身是在訂單
週期結束後才寫入的**，若使用者的觀察窗是「過去 90 天」，高退款金額直接等於
「已發生流失行為後的後續退款」，是目標的結果而非原因。

**處置**：從特徵集移除 `refund_amount`，保留 `refund_data_available` 二元欄位。

---

## Result

# EDA Report: PChome 訂單會員資料集（Train Set）

## Dataset Overview
- Rows: 256,329（Train），320,412（全）
- Date range: 2024-01-01 — 2025-03-31
- Key columns: 訂單行為（9）、會員屬性（4）、目標（1）

## Data Quality

| Issue | 欄位 | 數量 / 比例 | 行動 |
|-------|------|------------|------|
| MNAR 缺失 | `refund_amount` | 87,213 / 27.2% | 補 0 + 新增 `refund_data_available` |
| 隨機缺失 | `last_login_days` | 4,109 / 1.3% | 中位數補值（18 天） |
| 稀疏缺失 | `support_tickets` | 891 / 0.3% | 補 0 |
| 企業帳號異常值 | `order_amount` | 23 筆 | 標記 `is_corporate=1`，保留 |

## Key Statistics

| Variable | Mean | Median | Std | Min | Max | Distribution |
|----------|------|--------|-----|-----|-----|-------------|
| `order_amount` | 1,842 | 890 | 4,210 | 59 | 498,000 | 重度右偏 |
| `item_count` | 2.4 | 2 | 1.9 | 1 | 48 | 右偏 |
| `last_login_days` | 34.2 | 18 | 51.7 | 0 | 365 | 右偏 |
| `support_tickets` | 0.31 | 0 | 0.82 | 0 | 12 | 零膨脹 |

## Key Findings
1. **折價券使用與流失率呈 Simpson's Paradox**：聚合看似正相關（r = +0.06），
   分層後兩個子群組內均為負相關；Plus 會員身份是混淆變數，建模須加交互項。
2. **`refund_amount` 為目標洩漏特徵**（r = 0.97）：退款為流失的結果，非原因，
   已從特徵集移除。
3. **`refund_amount` 缺失為 MNAR**，與 `is_member_plus` 高度相關，均值填補
   會引入系統偏差；改用二元可用性旗標取代。

## Recommendations
- `order_amount` 做 log1p 轉換後進模型
- 加入 `coupon_used × is_member_plus` 交互特徵
- 分層分析應延伸至 `region` 與 `device_type`（是否也有 Simpson's Paradox 尚未檢查）
- `support_tickets` 考慮使用 Poisson 迴歸或負二項分布處理零膨脹問題
