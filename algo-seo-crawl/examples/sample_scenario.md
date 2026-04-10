# Example: E-commerce Site Audit Before Replatforming

## Scenario

Pinkoi（台灣設計師電商平台）的工程師 Maya 正在準備將網站從舊版 PHP 架構遷移到 Next.js。她需要在遷移前徹底了解現有的網站結構：有哪些頁面類型、連結深度分佈、孤立頁面、以及爬蟲陷阱。她問道：

> "我需要在遷移前把 pinkoi.com 的所有商品分類頁和靜態內容頁都 crawl 一遍，掌握頁面總數和連結結構，這樣才能驗證遷移後頁面都有對應的新 URL。max 3 層深度，先跑 500 頁的 pilot。"

---

## Analysis

### Phase 1: Input Validation

**Seed URL:** `https://www.pinkoi.com`
**Scope:** Same domain only（`www.pinkoi.com`），排除 `blog.pinkoi.com`
**Limits:** max_depth=3, max_pages=500

**robots.txt check** — 先 GET `https://www.pinkoi.com/robots.txt`：

```
User-agent: *
Disallow: /cart
Disallow: /checkout
Disallow: /account
Disallow: /api/
Crawl-delay: 2
```

Gate ✅：seed URL 合法、robots.txt 解析完成、crawl-delay 設為 **2 秒**（非預設 1 秒）、禁止路徑清單已載入。

---

### Phase 2: Core Algorithm

**Frontier 初始化：**

```python
frontier = PriorityQueue()
frontier.put((0, "https://www.pinkoi.com"))  # (depth, url)
visited = set()
per_domain_semaphore = asyncio.Semaphore(3)  # 同域最多 3 並發
crawl_delay = 2.0  # from robots.txt
```

**URL 正規化規則（避免重複抓取）：**

| 原始 URL | 正規化後 |
|---------|---------|
| `https://www.pinkoi.com/category/Home/` | `https://www.pinkoi.com/category/home` |
| `https://www.pinkoi.com/product/abc?ref=banner&sort=new` | `https://www.pinkoi.com/product/abc?ref=banner&sort=new`（query params 排序後保留） |
| `http://www.pinkoi.com/category/art` | `https://www.pinkoi.com/category/art`（HTTP→HTTPS 正規化） |

**Trap 偵測（實際遇到的問題）：**

爬到第 2 層時發現 URL 模式：
```
/search?q=ring&page=1
/search?q=ring&page=2
...
/search?q=ring&page=847
```

→ 設定 URL pattern filter：`/search` 路徑加入黑名單（分頁搜尋屬爬蟲陷阱，非結構性頁面）。

**Redirect 處理：**

`/category/Stationery` → 301 → `/category/stationery` → 追蹤，最終 URL 入庫，原 URL 記錄為 redirect。超過 5 跳即停止並記錄錯誤。

---

### Phase 3: Crawl 執行結果摘要（500 頁 pilot）

深度分佈：

| Depth | 頁數 |
|-------|------|
| 0 | 1（首頁）|
| 1 | 47 |
| 2 | 312 |
| 3 | 140 |

發現的頁面類型（從 URL 模式 + `<title>` 推斷）：

| 類型 | 數量 | 範例 |
|------|------|------|
| 分類頁 | 89 | `/category/jewelry` |
| 設計師店舖頁 | 203 | `/store/sunflower-studio` |
| 商品頁 | 157 | `/product/3b2k9o2` |
| 靜態內容頁 | 31 | `/about`, `/press`, `/sustainability` |
| Redirect（301）| 14 | `/category/Stationery` |
| 軟 404 | 6 | 狀態碼 200 但 `<title>` 含「找不到頁面」|
| robots.txt 拒絕 | 0 | ✅ 正確跳過 |

---

### Phase 4: Verification

```
✅ robots.txt 違規: 0 筆（/cart, /checkout, /account, /api/ 皆未進入 frontier）
✅ 重複頁面: 0 筆（URL 正規化有效）
✅ 爬蟲陷阱: /search 分頁攔截成功，節省約 800+ 個無效 URL
⚠️  軟 404 偵測到 6 筆，需人工確認是否為廢棄頁面
⚠️  14 個 301 redirect 來源 URL 需在遷移計畫中建立對應規則
```

---

## Result

```json
{
  "pages": [
    {"url": "https://www.pinkoi.com", "status": 200, "title": "Pinkoi — 亞洲領先設計購物平台", "links_out": 87, "depth": 0},
    {"url": "https://www.pinkoi.com/category/jewelry", "status": 200, "title": "珠寶首飾 | Pinkoi", "links_out": 43, "depth": 1},
    {"url": "https://www.pinkoi.com/store/sunflower-studio", "status": 200, "title": "向日葵工作室 | Pinkoi", "links_out": 12, "depth": 2},
    {"url": "https://www.pinkoi.com/category/Stationery", "status": 301, "title": null, "links_out": 0, "depth": 1, "redirect_to": "https://www.pinkoi.com/category/stationery"}
  ],
  "metadata": {
    "pages_crawled": 500,
    "errors": 6,
    "redirects": 14,
    "soft_404s": 6,
    "traps_blocked": 847,
    "duration_seconds": 1040,
    "domain": "www.pinkoi.com",
    "crawl_delay_used": 2.0,
    "robots_violations": 0
  }
}
```

**Maya 的後續行動：**

1. 將 14 個 301 來源 URL 加入 Next.js 的 `next.config.js` redirects 清單
2. 針對 6 個軟 404 頁面確認是否保留——若廢棄，在新架構中返回真正的 410
3. Pilot 通過後，移除 max_pages 限制，對完整站台執行深度 4 的全量爬取，預計抓取約 8,000–12,000 頁
