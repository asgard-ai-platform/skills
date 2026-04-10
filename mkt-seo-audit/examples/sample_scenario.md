直接撰寫範例檔案：

```markdown
# Example: 台灣 B2B SaaS 網站流量下滑診斷

## Scenario

**公司**：果核科技（Kernel Tech），台北，提供中小企業會計雲端 SaaS，官網 kerneltech.com.tw  
**情境**：行銷主管 Annie 發現 2026 年 Q1 自然搜尋流量較上季下滑 34%（GSC 數據：從每月 18,200 次點擊跌至 12,000 次），核心關鍵字「雲端會計軟體」排名從第 3 名跌至第 9 名。距離 Q2 業績目標還有 10 週，她需要知道原因與優先修復項目。

**用戶問題**：「為什麼我們的流量突然掉這麼多？能幫我做一次 SEO 健檢嗎？」

---

## Analysis

### Step 1：確認技術基礎前先鎖定時間點

GSC 數據顯示流量從 2026-01-14 週開始急遽下滑。對照歷史：
- 2025-12-28：IT 團隊部署新版網站（Next.js 重構），同時將舊 PHP 站下線
- 時間點高度吻合 → 技術遷移引入問題的可能性極高

**IRON LAW 驗證**：技術問題先排查，內容優化後做。

---

### Step 2：爬行與索引（Crawlability）

**robots.txt 檢查**  
發現 `kerneltech.com.tw/robots.txt` 包含：
```
User-agent: *
Disallow: /blog/
Disallow: /features/
```
這是遷移時的臨時設定，工程師忘記移除。  
→ **Google 已無法爬行 /blog/（52 篇文章）與 /features/（8 個產品頁）**，這兩個目錄貢獻舊站 61% 的自然流量。

**Sitemap 檢查**  
sitemap.xml 存在，但包含 134 個舊 PHP URL（如 `/features.php?id=3`），全數回傳 301 跳轉至新 URL，Google 需額外爬行回合。

**重定向鏈**  
Screaming Frog 掃描發現 23 個頁面存在 3 跳以上重定向鏈（舊 PHP → 新 Next.js 暫時路徑 → 最終 URL）。

**Canonical 標籤**  
新站首頁 canonical 指向 `http://kerneltech.com.tw`（HTTP），正式版為 HTTPS。全站約 40 個頁面因此有 canonical 錯誤。

---

### Step 3：Core Web Vitals（PageSpeed Insights，行動裝置）

| 指標 | 現況 | 目標 | 狀態 |
|------|------|------|------|
| LCP | 4.8s | < 2.5s | 🔴 |
| INP | 340ms | < 200ms | 🔴 |
| CLS | 0.09 | < 0.1 | 🟢 |

LCP 主因：Hero 圖片（1.2MB WebP）未使用 `priority` 屬性，Next.js Image 元件未觸發預載。  
INP 主因：第三方聊天套件（Intercom）在主執行緒載入，阻塞互動。

---

### Step 4：行動裝置相容性

Google 行動裝置相容性測試：通過（響應式設計正常）。  
但手動測試發現定價頁面的比較表格在 375px 螢幕寬度下需水平捲動 → 非嚴重但影響 UX。

---

### Step 5：核心頁面 On-Page 檢查（以「雲端會計軟體」目標頁為例）

| 元素 | 現況 | 問題 |
|------|------|------|
| Title tag | 「果核科技 - 雲端 ERP 解決方案」(34 chars) | 缺少主關鍵字「雲端會計軟體」 |
| Meta description | 空白 | 完全缺失，Google 自動截取內文 |
| H1 | 「讓帳務管理更輕鬆」| 無關鍵字，文案導向但 SEO 弱 |
| URL | `/solutions/accounting-cloud` | 可接受，但舊站為 `/features/cloud-accounting`，301 鏈中段 |
| 圖片 alt | 12 張產品截圖全為空 | 完全缺失 |
| 內部連結 | 首頁→此頁：0 個連結 | 遷移後內部連結斷裂 |

---

### Step 6：內容品質快速評估

- 部落格 52 篇文章因 robots.txt 被封鎖，現階段無法評估排名
- 產品頁面字數平均 380 字（舊站平均 820 字）→ 遷移時內容被大幅刪減
- 核心頁「雲端會計軟體」：競品前 3 名平均字數 2,100 字，果核目前 380 字 → 薄弱內容

---

## Result

```markdown
# SEO Audit: kerneltech.com.tw

## Summary
| Category | Score | Priority Issues |
|----------|-------|----------------|
| Crawlability | 🔴 | robots.txt 封鎖 /blog/ 與 /features/ |
| Speed | 🔴 | LCP 4.8s（目標 2.5s），INP 340ms |
| Mobile | 🟡 | 定價頁表格水平溢出 |
| On-Page | 🔴 | 核心頁 title/H1/meta 均缺少主關鍵字 |
| Content | 🔴 | 遷移後內容字數削減 54%，/blog/ 完全不可索引 |
| Backlinks | 🟢 | 域名授權穩定（DA 38），無毒性連結問題 |

## Critical Issues（立即修復，本週內）

1. **robots.txt 誤封鎖**  
   移除 `Disallow: /blog/` 與 `Disallow: /features/`  
   影響：恢復 Google 爬行 60 個頁面；預估 4-6 週後索引量回升  
   修復：編輯 `public/robots.txt`，重新提交 sitemap 至 GSC

2. **Canonical HTTP → HTTPS 錯誤**  
   全站 canonical 標籤改為 `https://` 開頭  
   影響：避免 Google 將流量分散至 HTTP 版本  
   修復：在 Next.js `<Head>` 設定 canonical 使用環境變數注入 HTTPS origin

3. **核心產品頁 Title + H1 + Meta**  
   `/solutions/accounting-cloud` 改為：  
   - Title：`雲端會計軟體 | 果核科技 — 中小企業首選`（26 chars）  
   - H1：`台灣中小企業雲端會計軟體`  
   - Meta：`果核雲端會計軟體，自動對帳、一鍵報稅，3 分鐘上手。立即免費試用。`（54 chars）

## High Priority（30 天內）

1. **修復重定向鏈**：23 個 3 跳以上頁面改為直接 301（舊 PHP URL → 最終 Next.js URL），預計減少爬行預算浪費 40%

2. **LCP 優化**：Hero 圖片加 `priority` 屬性啟用預載；Intercom 改為 lazy load（`defer` 策略），目標 LCP < 2.5s

3. **Sitemap 更新**：移除 134 個舊 PHP URL，僅保留現行 HTTPS canonical URL

4. **恢復內容字數**：優先補充「雲端會計軟體」頁面至 1,500 字以上，加入功能說明、使用情境、FAQ

5. **內部連結重建**：首頁、定價頁各加入 2 個錨文字連結指向核心產品頁（錨文字：「雲端會計軟體」）

## Opportunities

1. **部落格解封後快速提交**：robots.txt 修復後立即至 GSC 提交 sitemap，52 篇文章可在 2-4 週內重新進入索引
2. **「會計軟體推薦」長尾關鍵字**：月搜尋量 1,900（Ahrefs），競品 DR < 30，可用現有部落格文章切入
3. **Google 我的商家（台灣本地 SEO）**：果核目前無 GBP，補建後可在「台北會計軟體」等本地查詢獲得額外曝光

## Action Plan
| Priority | Action | Impact | Effort | Timeline |
|----------|--------|--------|--------|----------|
| 1 | 修復 robots.txt | H | L | 本週 |
| 2 | 修正全站 canonical | H | L | 本週 |
| 3 | 核心頁 On-Page 優化 | H | L | 本週 |
| 4 | 修復重定向鏈 | M | M | 第 2 週 |
| 5 | LCP/INP 效能優化 | H | M | 第 2-3 週 |
| 6 | Sitemap 更新 | M | L | 第 2 週 |
| 7 | 核心頁內容擴充至 1,500 字 | H | M | 第 3-4 週 |
| 8 | 內部連結重建 | M | L | 第 3 週 |
| 9 | 建立 Google Business Profile | M | L | 第 4 週 |
```

> **預期時間線**：robots.txt + canonical 修復後 4-6 週內 GSC 索引量應回升至遷移前水平；排名回到第 3 名預估需 8-12 週，視 Google 重新爬行速度而定。SEO 結果以季為單位衡量，Q2 末（2026-06）前應能看到顯著回升。
```
