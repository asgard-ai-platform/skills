直接撰寫檔案內容：

```markdown
# Example: 台灣運動用品電商搜尋品質緊急診斷

## Scenario

**公司：** SportHub Taiwan — 台灣中型運動用品電商，SKU 約 8 萬筆，月活躍用戶 40 萬。

**使用者問題（2026-03-28，產品經理 Jenny 提出）：**

> 上個月我們在 Google Ads 投了一波「無線耳機」的流量進來，但搜尋轉換率從 3.2% 掉到 1.8%，行銷費用燒掉了卻沒有換到訂單。搜尋結果「感覺很糟」，但我不知道哪裡壞了。請幫我診斷。

**現有數據（Jenny 提供的 2026-03 搜尋日誌摘要）：**

| 指標 | 數值 |
|------|------|
| 總搜尋次數 | 620,000 次 |
| 零結果率 | 14.3% |
| 第一頁 CTR | 19.2% |
| 加入購物車率（搜尋後） | 1.8% |
| 前 10 大失敗查詢 | 見下方 |

**前 10 大零結果查詢（依量排序）：**

1. `wireles earphone`（2,400 次）
2. `nike 慢跑鞋 男`（1,800 次）
3. `running shoes size 42`（1,500 次）
4. `藍芽耳機 防水`（1,200 次）
5. `AirPods 相容耳機`（980 次）
6. `瑜珈褲 女 高腰`（870 次）
7. `Garmin 手錶`（760 次）
8. `gift ideas`（720 次）
9. `跑步機 家用`（650 次）
10. `sport socks bulk`（480 次）

---

## Analysis

### Phase 1：輸入驗證 — 弱點定位

從 100 筆高量查詢樣本（取自 2026-03 日誌 top 100）進行四階段評估：

**階段評估結果：**

| 管線階段 | 失敗率 | 主要問題 |
|----------|--------|----------|
| Query Understanding | **高（38%）** | 拼寫錯誤未修正、無中英混合處理、無同義詞展開 |
| Retrieval | 中（15%） | 多欄位搜尋設定不完整（忽略 brand 欄位） |
| Ranking | 低（8%） | 基本 BM25 運作正常，但熱門度加權缺失 |
| Presentation | 低（5%） | 零結果頁無替代建議，使用者直接離開 |

**Gate 通過：** 弱點明確定位在 **Query Understanding（首要）** 與 **Retrieval（次要）**。

---

### Phase 2：核心演算法應用

#### 問題 1：拼寫錯誤未修正（Query Understanding）

`wireles earphone`（2,400 次零結果）：

- 編輯距離分析：`wireles` → `wireless`（距離 = 1），`earphone` → `earphone`（正確）
- 修正後查詢：`wireless earphone` → 應命中 423 筆 SKU
- **修復：** 實作 trigram 拼寫校正，覆蓋編輯距離 ≤ 2 的常見錯誤

#### 問題 2：中英混合查詢無法解析（Query Understanding）

`nike 慢跑鞋 男`（1,800 次零結果）：

- 系統以完整字串比對，無法拆解 `nike`（品牌）、`慢跑鞋`（品類）、`男`（屬性）
- **修復：** 實作屬性提取（NER）：
  - `nike` → `brand: Nike`
  - `慢跑鞋` → `category: 慢跑鞋`（含同義詞：running shoes）
  - `男` → `attribute: gender=male`
- 重構為結構化查詢後命中 612 筆 SKU

#### 問題 3：同義詞展開缺失（Query Understanding）

`藍芽耳機 防水`（1,200 次）實際有大量商品，但零結果原因：

- 商品資料庫使用 `藍牙耳機`（正體中文標準用字），`藍芽` 為常用口語寫法
- **修復：** 加入同義詞對：`藍芽 ↔ 藍牙`、`earphone ↔ earphones ↔ 耳機`、`wireless ↔ 無線`

> ⚠️ **注意（Gotcha）：** `AirPods 相容耳機` 不可擴展為 `AirPods ↔ 耳機`，AirPods 是品牌專有名稱，應作為品牌篩選條件，而非耳機的同義詞。

#### 問題 4：Brand 欄位未納入多欄位搜尋（Retrieval）

`Garmin 手錶`（760 次零結果）：

- 搜尋僅比對 `title` 與 `description`，`brand` 欄位被排除
- 商品標題為「Forerunner 255 GPS 跑錶」，`Garmin` 只存在 `brand` 欄位
- **修復：** 多欄位搜尋設定：
  ```
  title^3, brand^2, description^1, category^1
  ```

#### 問題 5：意圖分類缺失（Query Understanding）

`gift ideas`（720 次）：

- 非產品搜尋，屬於 **瀏覽意圖（browse intent）**
- 當前系統嘗試精確比對商品名稱，返回零結果
- **修復：** 分類為 browse intent，導向策劃頁面（「送禮推薦」專題），不走一般搜尋管線

#### 問題 6：零結果頁無 Fallback（Presentation）

所有零結果查詢直接顯示空白頁，使用者離開率 94%。

- **修復：** 零結果 fallback 策略：
  1. 鬆弛查詢（移除限制條件，如 size、color）後重試
  2. 顯示「你是否要找：{拼寫建議}」
  3. 顯示相關熱門品類連結

---

### Phase 3：驗證

以 2026-03 數據為基線，模擬修復後預估效果：

| 指標 | 修復前 | 修復後（預估） | 目標 |
|------|--------|---------------|------|
| 零結果率 | 14.3% | 4.8% | <5% |
| 第一頁 CTR | 19.2% | 28.5% | >30% |
| 加入購物車率 | 1.8% | 2.9% | >3% |
| 品牌查詢命中率 | 43% | 91% | >85% |

**Gate：** 零結果率與品牌命中率達標，CTR 與加購率接近目標，需上線後以 A/B test 驗證。

---

## Result

```json
{
  "audit": {
    "zero_result_rate": 0.143,
    "avg_ctr": 0.192,
    "top_failing_queries": [
      "wireles earphone",
      "nike 慢跑鞋 男",
      "藍芽耳機 防水",
      "Garmin 手錶",
      "gift ideas"
    ]
  },
  "recommendations": [
    {
      "stage": "query_understanding",
      "issue": "spell_correction_missing",
      "impact": "high",
      "fix": "實作 trigram 拼寫校正，覆蓋編輯距離 ≤ 2；預計消除 ~35% 零結果",
      "effort": "medium"
    },
    {
      "stage": "query_understanding",
      "issue": "synonym_expansion_missing",
      "impact": "high",
      "fix": "建立同義詞表：藍芽↔藍牙、wireless↔無線↔藍牙；勿將品牌名（AirPods）列為同義詞",
      "effort": "low"
    },
    {
      "stage": "query_understanding",
      "issue": "mixed_language_attribute_extraction_missing",
      "impact": "high",
      "fix": "實作中英混合 NER，提取 brand / category / attribute；支援「nike 慢跑鞋 男」類查詢",
      "effort": "high"
    },
    {
      "stage": "retrieval",
      "issue": "brand_field_not_indexed",
      "impact": "high",
      "fix": "多欄位搜尋加入 brand^2，修復品牌查詢零結果（Garmin、Garmin、Salomon 等）",
      "effort": "low"
    },
    {
      "stage": "query_understanding",
      "issue": "browse_intent_not_classified",
      "impact": "medium",
      "fix": "偵測瀏覽意圖查詢（gift ideas、best sellers），導向策劃頁而非商品搜尋",
      "effort": "medium"
    },
    {
      "stage": "presentation",
      "issue": "no_zero_result_fallback",
      "impact": "medium",
      "fix": "零結果頁加入：拼寫建議、鬆弛查詢結果、相關品類連結；降低使用者流失",
      "effort": "low"
    }
  ],
  "prioritized_order": [
    "spell_correction_missing",
    "brand_field_not_indexed",
    "synonym_expansion_missing",
    "no_zero_result_fallback",
    "browse_intent_not_classified",
    "mixed_language_attribute_extraction_missing"
  ],
  "metadata": {
    "queries_sampled": 100,
    "period": "2026-03",
    "weakest_stage": "query_understanding",
    "estimated_zero_result_rate_after_fix": 0.048
  }
}
```

**執行優先序說明：**

1. `brand_field_not_indexed` — 改一行設定，立即修復品牌查詢
2. `synonym_expansion_missing` — 低成本，高覆蓋
3. `spell_correction_missing` — 需工程實作，但影響最大
4. 中英混合 NER 排最後——工程成本最高，待前三項上線後以 A/B test 確認增量再投入
```
