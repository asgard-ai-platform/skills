# Example: E-commerce Product Page Schema for 台灣保健品牌

## Scenario

**公司：** VitaPlus 健康生技（台灣電商品牌）
**需求：** 產品頁面在 Google 搜尋結果中只顯示普通藍色連結，競爭對手頁面卻有星級評分、價格、庫存狀態等 rich snippet。SEO 負責人想為主力商品「薑黃複方膠囊 60 粒裝」的產品頁加上 structured data。

頁面可見內容（用戶看得到的）：
- 商品名稱：薑黃複方膠囊 60 粒裝
- 品牌：VitaPlus
- 價格：NT$890
- 庫存：有庫存
- 評分：4.6 顆星（共 312 則評價）
- 描述：含天然薑黃素 500mg + 黑胡椒萃取，增強吸收率。
- SKU：VP-TURMERIC-60

---

## Analysis

### Phase 1: Input Validation

**頁面類型識別：** Product（電商商品頁）

**必填屬性確認（Google Product 要求）：**

| 屬性 | 可見內容 | 狀態 |
|------|---------|------|
| `name` | 薑黃複方膠囊 60 粒裝 | ✅ |
| `offers.price` | NT$890 | ✅ |
| `offers.priceCurrency` | TWD | ✅ |
| `offers.availability` | 有庫存 | ✅ |
| `aggregateRating.ratingValue` | 4.6 | ✅ |
| `aggregateRating.reviewCount` | 312 | ✅ |

Gate 通過：所有必填欄位在頁面上均可見。

### Phase 2: Core Algorithm

**Type 選擇：** `Product`（最具體，優於 `Thing`）

**屬性映射：**
- `name` → 頁面 H1 標題
- `brand.@type` → `Brand`，`name` → "VitaPlus"
- `offers` → 巢狀 `Offer` 物件，包含價格、幣別、庫存
- `offers.availability` → `https://schema.org/InStock`（對應頁面「有庫存」文字）
- `aggregateRating` → 巢狀物件，`ratingValue: 4.6`，`reviewCount: 312`
- `sku` → VP-TURMERIC-60

**巢狀結構確認：** `Product > Offer`（一層），`Product > AggregateRating`（一層）— 深度可控，無風險。

**IRON LAW 檢查：**
> 頁面上沒有顯示 `description` 以外的長文字嗎？→ 有，描述文字可見，安全加入。
> 評分 4.6 / 312 則是頁面上真實顯示的數字？→ 是。✅

### Phase 3: Verification 計畫

產生後應貼入 [Google Rich Results Test](https://search.google.com/test/rich-results)，確認：
- 偵測到 Product rich result
- `errors: 0`
- `offers` 和 `aggregateRating` 均展開無缺漏

---

## Result

```json
{
  "schema": {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "薑黃複方膠囊 60 粒裝",
    "sku": "VP-TURMERIC-60",
    "description": "含天然薑黃素 500mg + 黑胡椒萃取，增強吸收率。",
    "brand": {
      "@type": "Brand",
      "name": "VitaPlus"
    },
    "offers": {
      "@type": "Offer",
      "price": "890",
      "priceCurrency": "TWD",
      "availability": "https://schema.org/InStock",
      "url": "https://www.vitaplus.com.tw/products/turmeric-60"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.6",
      "reviewCount": "312"
    }
  },
  "validation": {
    "errors": 0,
    "warnings": 1,
    "eligible_rich_results": ["Product snippet", "Review snippet"]
  }
}
```

**注意事項：**
- `warnings: 1`：未提供 `image` 欄位。Google 建議加入，但非必填。應補上商品主圖 URL（`"image": "https://www.vitaplus.com.tw/images/turmeric-60.jpg"`）以最大化 rich result 展示機率。
- `offers.url` 應指向規範 URL（canonical），避免 variant 頁面造成重複。

**插入位置：**

```html
<head>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "薑黃複方膠囊 60 粒裝",
    ...
  }
  </script>
</head>
```

**預期效果：** 通過 Google Rich Results Test 後，Search Console 會在「豐富結果」報表中出現 Product 項目，約 2–4 週索引後 SERP 開始顯示星級與價格卡片。
