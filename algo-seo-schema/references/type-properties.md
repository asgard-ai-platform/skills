# Type Properties by Schema.org Type

每個 Schema.org 類型都有**必填（Required）**、**建議（Recommended）**、**選填（Optional）**三種屬性層級。Google 會忽略缺少必填屬性的 schema；建議屬性影響富結果顯示的完整程度。

以下以 Google 實際強制執行的欄位為準，非 Schema.org 規格完整清單。

---

## FAQPage

**觸發富結果：** FAQ 折疊區塊（SERP 直接展開問答）

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"FAQPage"` |
| `mainEntity` | Required | Array of `Question` | 所有問答對的陣列 |
| `mainEntity[].@type` | Required | Text | `"Question"` |
| `mainEntity[].name` | Required | Text | 問題文字，需與頁面可見文字完全一致 |
| `mainEntity[].acceptedAnswer` | Required | `Answer` | |
| `mainEntity[].acceptedAnswer.@type` | Required | Text | `"Answer"` |
| `mainEntity[].acceptedAnswer.text` | Required | Text | 答案文字，支援 HTML subset |

**最小可用範本：**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "退貨期限是幾天？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "商品到貨後 7 天內可申請退貨，需保持原包裝完整。"
      }
    }
  ]
}
```

**常見錯誤：** `mainEntity` 寫成物件而非陣列（單題也必須用陣列）。

---

## Product

**觸發富結果：** 產品卡（價格、評分、庫存狀態）

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"Product"` |
| `name` | Required | Text | 產品名稱 |
| `offers` | Required | `Offer` 或 `AggregateOffer` | 定價資訊 |
| `offers.@type` | Required | Text | `"Offer"` |
| `offers.price` | Required | Number/Text | 數字字串，如 `"299"` |
| `offers.priceCurrency` | Required | Text | ISO 4217，如 `"TWD"` |
| `offers.availability` | Required | URL | `https://schema.org/InStock` 等 |
| `image` | Recommended | URL or Array | 產品圖，至少 1:1 比例 |
| `description` | Recommended | Text | |
| `brand` | Recommended | `Brand` | `{"@type":"Brand","name":"..."}` |
| `aggregateRating` | Recommended | `AggregateRating` | 顯示星級需要此欄位 |
| `aggregateRating.ratingValue` | Recommended | Number | 1.0–5.0 |
| `aggregateRating.reviewCount` | Recommended | Integer | 需有實際評論數量 |
| `sku` | Optional | Text | |
| `gtin` | Optional | Text | EAN / UPC |

**`offers.availability` 合法值：**

```
https://schema.org/InStock
https://schema.org/OutOfStock
https://schema.org/PreOrder
https://schema.org/Discontinued
```

**最小可用範本（含評分）：**

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "無線藍牙耳機 Pro X",
  "image": "https://example.com/images/headphone-pro-x.jpg",
  "description": "主動降噪，續航 30 小時。",
  "brand": {"@type": "Brand", "name": "SoundMax"},
  "offers": {
    "@type": "Offer",
    "price": "2990",
    "priceCurrency": "TWD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "reviewCount": "83"
  }
}
```

**IRON LAW 強化：** `aggregateRating.reviewCount` 必須對應頁面上實際可見的評論數。如果頁面顯示 5 則評論，schema 寫 83 屬於違規。

---

## Article / NewsArticle / BlogPosting

**觸發富結果：** Top Stories 輪播（NewsArticle 限定）、文章摘要

類型選擇決策樹：

```
是新聞媒體的時效性報導？
├── Yes → NewsArticle
└── No
    ├── 是個人或品牌部落格文章？ → BlogPosting
    └── 其他長篇內容 → Article
```

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | 見上方決策樹 |
| `headline` | Required | Text | 標題，≤ 110 字元 |
| `image` | Required | URL or Array | 至少 1200px 寬，16:9 優先 |
| `datePublished` | Required | DateTime | ISO 8601，`"2025-03-15T09:00:00+08:00"` |
| `dateModified` | Recommended | DateTime | 更新時間 |
| `author` | Required | `Person` 或 `Organization` | |
| `author.@type` | Required | Text | `"Person"` 或 `"Organization"` |
| `author.name` | Required | Text | |
| `publisher` | Recommended | `Organization` | |
| `publisher.name` | Recommended | Text | |
| `publisher.logo` | Recommended | `ImageObject` | 600×60px 以內 |

**`publisher.logo` 規格：**

```json
"publisher": {
  "@type": "Organization",
  "name": "Asgard Tech",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 300,
    "height": 60
  }
}
```

---

## BreadcrumbList

**觸發富結果：** SERP URL 路徑顯示（首頁 > 分類 > 商品）

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"BreadcrumbList"` |
| `itemListElement` | Required | Array of `ListItem` | 按層級排序 |
| `itemListElement[].@type` | Required | Text | `"ListItem"` |
| `itemListElement[].position` | Required | Integer | 從 1 開始 |
| `itemListElement[].name` | Required | Text | 層級名稱 |
| `itemListElement[].item` | Required（非末頁）| URL | 末頁可省略 |

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://example.com"},
    {"@type": "ListItem", "position": 2, "name": "耳機", "item": "https://example.com/headphones"},
    {"@type": "ListItem", "position": 3, "name": "無線藍牙耳機 Pro X"}
  ]
}
```

---

## HowTo

**觸發富結果：** 步驟式操作圖文（桌面版有時顯示縮圖）

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"HowTo"` |
| `name` | Required | Text | 操作標題 |
| `step` | Required | Array of `HowToStep` | |
| `step[].@type` | Required | Text | `"HowToStep"` |
| `step[].name` | Required | Text | 步驟標題 |
| `step[].text` | Required | Text | 步驟說明 |
| `step[].image` | Optional | URL | 步驟截圖 |
| `totalTime` | Recommended | Duration | ISO 8601，`"PT30M"` = 30 分鐘 |
| `estimatedCost` | Optional | `MonetaryAmount` | |

---

## Event

**觸發富結果：** 活動卡（日期、地點、票價）

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"Event"` |
| `name` | Required | Text | 活動名稱 |
| `startDate` | Required | DateTime | ISO 8601 含時區 |
| `endDate` | Recommended | DateTime | |
| `location` | Required | `Place` 或 `VirtualLocation` | |
| `location.@type` | Required | Text | |
| `location.name` | Required（Place）| Text | 場館名稱 |
| `location.address` | Required（Place）| `PostalAddress` 或 Text | |
| `eventStatus` | Recommended | URL | `https://schema.org/EventScheduled` 等 |
| `eventAttendanceMode` | Recommended | URL | 線上/線下/混合 |
| `offers` | Optional | `Offer` | 票價資訊 |

**`eventAttendanceMode` 合法值：**

```
https://schema.org/OfflineEventAttendanceMode   # 實體
https://schema.org/OnlineEventAttendanceMode    # 線上
https://schema.org/MixedEventAttendanceMode     # 混合
```

---

## Organization / LocalBusiness

**觸發富結果：** 知識圖譜側欄、本地商家資訊

`LocalBusiness` 繼承 `Organization`，並新增地址與營業時間。

| 屬性 | 層級 | 類型 | 說明 |
|------|------|------|------|
| `@type` | Required | Text | `"LocalBusiness"` 或子類型如 `"Restaurant"` |
| `name` | Required | Text | |
| `address` | Required | `PostalAddress` | |
| `address.streetAddress` | Required | Text | |
| `address.addressLocality` | Required | Text | 城市 |
| `address.addressRegion` | Optional | Text | 縣市 |
| `address.addressCountry` | Required | Text | ISO 3166-1，`"TW"` |
| `telephone` | Recommended | Text | `"+886-2-1234-5678"` |
| `openingHoursSpecification` | Recommended | Array | 每天營業時間 |
| `geo` | Recommended | `GeoCoordinates` | 緯度/經度 |

**`openingHoursSpecification` 範本：**

```json
"openingHoursSpecification": [
  {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  },
  {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Saturday"],
    "opens": "10:00",
    "closes": "16:00"
  }
]
```

---

## 多類型組合（同一頁面）

當一個頁面需要多種 schema（例如：商品頁同時需要 Product + BreadcrumbList），使用 JSON 陣列：

```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [...]
  },
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "...",
    "offers": {...}
  }
]
</script>
```

也可用單一 `<script>` 標籤放置多個，或分開成多個 `<script>` 標籤，Google 均可接受。

---

## 必填屬性速查表

| Schema 類型 | 絕對必填（缺少即被忽略） |
|------------|------------------------|
| FAQPage | `mainEntity[].name`, `mainEntity[].acceptedAnswer.text` |
| Product | `name`, `offers.price`, `offers.priceCurrency`, `offers.availability` |
| Article | `headline`, `image`, `datePublished`, `author.name` |
| NewsArticle | 同 Article（`publisher` 對 Top Stories 實質必填） |
| BreadcrumbList | `itemListElement[].position`, `itemListElement[].name` |
| HowTo | `name`, `step[].name`, `step[].text` |
| Event | `name`, `startDate`, `location` |
| LocalBusiness | `name`, `address.streetAddress`, `address.addressCountry` |

---

## 類型特殊性原則的實際應用

從通用到具體的類型鏈，選擇最具體的有效類型：

```
Thing
└── Organization
    └── LocalBusiness
        ├── FoodEstablishment
        │   ├── Restaurant
        │   ├── CafeOrCoffeeShop
        │   └── FastFoodRestaurant
        └── Store
            ├── ClothingStore
            └── ElectronicsStore

CreativeWork
└── Article
    ├── NewsArticle
    │   └── ReportageNewsArticle
    ├── BlogPosting
    │   └── LiveBlogPosting
    └── TechArticle
```

選擇錯誤不會產生錯誤，但會減少富結果資格。`BlogPosting` 不具備 Top Stories 資格；`NewsArticle` 才有。
