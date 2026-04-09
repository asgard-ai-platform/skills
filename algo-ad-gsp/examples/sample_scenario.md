# Example: 旅遊關鍵字廣告競標分析

## Scenario

TravelNow（機票比價平台）的廣告優化師 Emily 正在分析「便宜機票」這個關鍵字的競標策略。她從 Google Ads 後台看到上週的拍賣報告，想弄清楚為何競爭對手 AirDeal 雖然出價比 TravelNow 低，卻每次都排在更前面。她提供了以下原始數據：

| 廣告商 | 出價（CPC bid）| Quality Score |
|--------|--------------|---------------|
| TravelNow | $4.50 | 6 |
| AirDeal | $3.20 | 9 |
| FlightGuru | $5.00 | 4 |
| CheapWings | $2.80 | 7 |
| JetSearch | $1.50 | 8 |

Google 這個關鍵字目前開放 **3 個廣告版位**，最低出價門檻 $1.00。

Emily 的問題：
1. 各廣告商的實際排名為何？
2. TravelNow 的實際 CPC 是多少？
3. 為什麼排到第 2 位反而比第 1 位更划算？

---

## Analysis

### Phase 1：計算 Ad Rank

$$\text{AdRank}_i = \text{Bid}_i \times \text{QualityScore}_i$$

| 廣告商 | Bid | QS | Ad Rank |
|--------|-----|----|---------|
| AirDeal | $3.20 | 9 | **28.8** |
| TravelNow | $4.50 | 6 | **27.0** |
| CheapWings | $2.80 | 7 | **19.6** |
| JetSearch | $1.50 | 8 | **12.0** |
| FlightGuru | $5.00 | 4 | **20.0** |

排序（降冪）：AirDeal(28.8) > TravelNow(27.0) > FlightGuru(20.0) > CheapWings(19.6) > JetSearch(12.0)

只有 3 個版位，因此 JetSearch 未進入廣告位。

### Phase 2：GSP 定價計算

**規則：** 每位勝出者支付的 CPC = 下一位競爭者的 AdRank ÷ 自己的 QS

| 版位 | 廣告商 | Ad Rank | 定價依據（下一位 AdRank） | 實際 CPC |
|------|--------|---------|--------------------------|---------|
| #1 | AirDeal | 28.8 | TravelNow AdRank = 27.0 | 27.0 / 9 = **$3.00** |
| #2 | TravelNow | 27.0 | FlightGuru AdRank = 20.0 | 20.0 / 6 = **$3.33** |
| #3 | FlightGuru | 20.0 | CheapWings AdRank = 19.6 | 19.6 / 4 = **$4.90** |

> **第 3 版位的 FlightGuru**：出價 $5.00，實際付 $4.90，接近滿額；這是因為 QS 低（4分）導致必須靠高出價撐 AdRank，而 GSP 定價並不優待低 QS 廣告商。

### Phase 3：驗證

- AirDeal CPC $3.00 ≤ 出價 $3.20 ✓
- TravelNow CPC $3.33 ≤ 出價 $4.50 ✓
- FlightGuru CPC $4.90 ≤ 出價 $5.00 ✓
- 排名與 AdRank 順序一致 ✓

### Phase 4：投報率估算

假設該關鍵字版位 CTR 乘數（相對點擊率）：

| 版位 | CTR 乘數 | 預估每日點擊 | CPC | 每日廣告費 |
|------|---------|------------|-----|---------|
| #1（AirDeal） | 1.00 | 200 | $3.00 | $600 |
| #2（TravelNow） | 0.65 | 130 | $3.33 | $433 |
| #3（FlightGuru） | 0.35 | 70 | $4.90 | $343 |

**Emily 的核心問題解答：**

第 2 版位對 TravelNow 的效益分析，假設轉換率 2%、平均訂單價值 $180：

- 每日點擊 130，轉換 2.6 筆，收入 $468
- 每日廣告費 $433
- **ROAS = 468/433 ≈ 1.08**（邊際獲利）

若 TravelNow 把出價調高到 $4.90 試圖搶第 1 位（AdRank = 29.4）：
- 取代 AirDeal 後，CPC = TravelNow 原本 AdRank 27.0 / QS 6 = $4.50（反而付出價上限）
- 每日費用 ≈ 200 × $4.50 = $900，ROAS = 720/900 = 0.80（虧損）

---

## Result

```json
{
  "slots": [
    {
      "advertiser": "AirDeal",
      "position": 1,
      "ad_rank": 28.8,
      "cpc": 3.00,
      "est_clicks": 200
    },
    {
      "advertiser": "TravelNow",
      "position": 2,
      "ad_rank": 27.0,
      "cpc": 3.33,
      "est_clicks": 130
    },
    {
      "advertiser": "FlightGuru",
      "position": 3,
      "ad_rank": 20.0,
      "cpc": 4.90,
      "est_clicks": 70
    }
  ],
  "metadata": {
    "total_bidders": 5,
    "slots_available": 3,
    "auction_type": "gsp",
    "keyword": "便宜機票",
    "excluded": ["CheapWings", "JetSearch"]
  }
}
```

**給 Emily 的結論：**

1. **AirDeal 排第 1 的原因**：QS 9 分使 AdRank 達 28.8，高於 TravelNow 的 27.0——即使出價只有 $3.20 對 $4.50。
2. **TravelNow 的實際 CPC 為 $3.33**，而非出價的 $4.50，GSP 保護機制有效。
3. **第 2 位比第 1 位更划算**（此案例）：搶第 1 位需要 CPC 上升至 ~$4.50，ROAS 轉負；維持第 2 位 ROAS 仍為正。

**優化建議**：與其提高出價，TravelNow 應優先**提升 Quality Score**（改善廣告相關性和落地頁體驗）。QS 從 6 提高到 8，AdRank 升至 36.0，可以用 $2.25 的 CPC 坐穩第 1 位（成本反而更低）。

> **注意**：由於 GSP 不是誘因相容機制，以上計算假設其他競爭者不調整出價。實際上 AirDeal 若發現被超越，可能反應性地調高出價，導致納許均衡漂移。
