# Example: 電商首頁 Core Web Vitals 搶救

## Scenario

**公司：** FreshCart 生鮮電商（freshcart.tw）
**問題：** Google Search Console 顯示首頁「網頁體驗」評估失敗，近 28 天 CrUX 數據：

- LCP: 4.1s（Poor）
- INP: 220ms（Needs Improvement）
- CLS: 0.38（Poor）

行銷團隊注意到自然搜尋流量較上季下滑 18%，懷疑與 Core Web Vitals 失敗有關。工程師跑 Lighthouse 得到 LCP 2.8s、CLS 0.05——看起來通過了，但 Search Console 仍標示失敗。

**問題：** 「Lighthouse 明明過了，為什麼 Google 還說我們沒過？」

---

## Analysis

### Phase 1: Input Validation

**釐清 Lab vs Field 落差（IRON LAW）**

Lighthouse 在本機模擬快速 4G 裝置，但 CrUX 收集的是真實用戶的第 75 百分位數據。FreshCart 用戶中有 62% 使用 Android 中低階機型（CrUX 裝置分佈），與 Lighthouse 模擬環境差距顯著。

| Metric | Lighthouse (Lab) | CrUX P75 (Field) | 判定 |
|--------|-----------------|------------------|------|
| LCP    | 2.8s            | 4.1s             | Poor |
| INP    | 90ms            | 220ms            | Needs Improvement |
| CLS    | 0.05            | 0.38             | Poor |

**結論：** Lab 環境低估真實負載。現場存在三個獨立問題，需逐一追查。

---

### Phase 2: Core Algorithm

#### CLS = 0.38（優先修復，影響最大）

用 Chrome DevTools Performance 面板錄製首頁載入，WebPageTest 的 filmstrip 顯示：
- 第 1.2s：頁面渲染 hero banner
- 第 1.8s：header 廣告位（300×250）注入，推擠下方商品卡
- 第 2.4s：促銷浮動條從頂部滑入，再次推擠內容

**CLS 歸因：** 位移元素是商品卡，但**原因**是廣告位和浮動條未預留空間。

修復方案：
```html
<!-- 廣告容器預留高度 -->
<div class="ad-slot" style="min-height: 250px; width: 300px;">
  <!-- 廣告動態注入此處 -->
</div>

<!-- 促銷條改為 position:sticky，不推擠文件流 -->
<div class="promo-bar" style="position: sticky; top: 0;">
```

預估 CLS 改善至 0.06（Good）。

#### LCP = 4.1s（次優先）

LCP 元素為首頁 hero 圖片 `hero-banner-2026q2.jpg`（820KB，未壓縮）。

**分析路徑：**
1. TTFB: 380ms（可接受）
2. 圖片未設 `fetchpriority="high"` → 瀏覽器晚於第三方腳本載入
3. 圖片格式 JPEG，未提供 WebP/AVIF

修復方案：
```html
<!-- 加入 preload + fetchpriority -->
<link rel="preload" as="image" href="/images/hero-banner.avif"
      fetchpriority="high" type="image/avif">

<img src="/images/hero-banner.avif"
     fetchpriority="high"
     width="1200" height="500"
     alt="本週生鮮特惠">
```

同時壓縮至 AVIF 格式：820KB → 預估 ~95KB（-88%）。

預估 LCP 改善至 2.1s（Good）。

#### INP = 220ms（第三優先）

Profile 結果：用戶點擊「加入購物車」觸發一個 180ms 的長任務，其中包含：
- 同步 localStorage 讀寫（購物車狀態）：40ms
- 全頁重新渲染（React state 更新觸發 parent re-render）：130ms

修復方案：
```javascript
// 1. 將 localStorage 操作移至 requestIdleCallback
const addToCart = (item) => {
  // 立即更新 UI state（快速回饋）
  setCart(prev => [...prev, item]);

  // 延遲非關鍵的持久化
  requestIdleCallback(() => {
    localStorage.setItem('cart', JSON.stringify(cartRef.current));
  });
};

// 2. 用 React.memo 避免商品列表因購物車狀態更新而重渲
export const ProductGrid = React.memo(({ products }) => { ... });
```

預估 INP 改善至 ~85ms（Good）。

---

### Phase 3: Verification

**Lab 確認：**
部署至 staging 後跑 Lighthouse（Mobile，3× throttling）：

| Metric | Before | After (Lab) |
|--------|--------|-------------|
| LCP    | 2.8s   | 1.9s        |
| INP    | 90ms   | 65ms        |
| CLS    | 0.05   | 0.04        |

**注意：** Lab 分數改善不代表完成。需部署至 production 並等待 CrUX 28 天滾動窗口更新。

建議在 Search Console 設定「網頁體驗」警示，預計 2026-05-08 後確認 CrUX P75 數據。

---

## Result

```json
{
  "audit": {
    "lcp": {
      "value_ms": 4100,
      "status": "poor",
      "element": "hero-banner-2026q2.jpg",
      "fixes": ["convert-to-avif", "add-fetchpriority-high", "add-preload-hint"],
      "expected_after_ms": 2100
    },
    "inp": {
      "value_ms": 220,
      "status": "needs_improvement",
      "cause": "synchronous-localstorage + full-tree-rerender",
      "fixes": ["requestIdleCallback-for-persistence", "React.memo-on-ProductGrid"],
      "expected_after_ms": 85
    },
    "cls": {
      "value": 0.38,
      "status": "poor",
      "shifted_element": ".product-card",
      "root_cause": "ad-slot-no-reserved-space + promo-bar-in-document-flow",
      "fixes": ["min-height-on-ad-slot", "sticky-promo-bar"],
      "expected_after": 0.06
    }
  },
  "priority_order": ["cls", "lcp", "inp"],
  "metadata": {
    "url": "https://freshcart.tw/",
    "data_source": "crux",
    "device": "mobile",
    "crux_percentile": 75,
    "lab_tool": "lighthouse-12.x",
    "field_confirmation_date": "2026-05-08"
  }
}
```

**關鍵提醒：**
- Lighthouse 通過 ≠ Google 認定通過；永遠以 CrUX P75 為準
- CLS 修復優先於 LCP，因分數最差且修復成本最低
- 28 天後若 CrUX 仍未改善，排查 CDN cache 是否未清除舊版資源
