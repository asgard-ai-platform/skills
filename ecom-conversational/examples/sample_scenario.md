# Example: 台灣手工皮革品牌導入 LINE 對話式銷售

## Scenario

**Muji Leather Studio**（木質皮革工坊）是台北一家手工皮革品牌，年營收約 350 萬元。目前主要靠 Instagram 和實體快閃市集銷售。老闆 Amy 發現 Instagram DM 每週收到 80-100 則詢問訊息，但只有 12% 最終成交，因為：

1. Amy 一個人回覆 DM，常常忙於製作無法即時回應，客人等超過 2 小時就去別家買了
2. 詢問的問題 70% 都是同樣的：「有哪些顏色？」「可以刻字嗎？」「多久會到？」
3. 想要「賣通 LINE」但不知道從哪裡開始

Amy 的問題：「我想建一個 LINE 機器人幫我自動回覆客人、推薦產品、最好可以直接下單，怎麼做？」

---

## Analysis

### 1. 通路選擇

Amy 目前在 Instagram 收 DM，但 LINE 才是台灣消費者主力通訊工具（95% 滲透率，21M+ 用戶）。手工皮革客群以 25-45 歲為主，LINE 使用率遠高於 Instagram。

**決策**：
- **主力通路 → LINE Official Account**（非 Instagram DM）
- Instagram 保留作為品牌展示 + 導流入口（貼文加 LINE 連結）
- 預估月訊息量：80-100 則 × 4 週 = 320-400 則 → 需 **Premium 方案**（月費 800 元，5,000 則免費）

### 2. Iron Law 驗證

> **Conversation First, Commerce Second**：Help → Trust → Recommend → Convert

Amy 的失敗點在於跳過 Help 直接等客人問完就說「好，匯款給我」。機器人設計必須先解決問題，再順勢推薦。

### 3. Bot vs Human 分流設計

分析那 80-100 則 DM 的問題類型：

| 問題類型 | 佔比 | 處理方式 |
|---------|------|---------|
| 顏色/款式查詢 | 35% | **Bot** |
| 刻字/客製詢問 | 25% | Bot 先收需求 → **Amy 確認** |
| 價格與付款方式 | 20% | **Bot** |
| 到貨時間 | 15% | **Bot** |
| 退換貨/抱怨 | 5% | **立即轉人工** |

Bot 可處理 70%，Amy 只需親自回覆 30%（複雜客製 + 投訴）。以現況每週 90 則計算：Amy 只需回覆 **27 則**，從目前 90 則全部手動降低 70% 工作量。

### 4. Conversation Flow 設計

**Entry Points**：
- Instagram 貼文 bio 加「LINE 諮詢直購」→ 掃 QR code
- 蝦皮店頁加 LINE OA 標籤（客人問問題時引導）
- 快閃攤位放 QR 立牌

**Welcome Flow（前 3 則）**：

```
[自動歡迎訊息]
嗨！歡迎來到木質皮革工坊 🌿
我是 Amy 的小幫手，可以幫你：

👜 查詢商品款式與顏色
✏️ 了解客製刻字服務  
📦 確認出貨時間

請選擇你想了解的：
[查商品] [刻字客製] [訂單查詢]
```

**Product Discovery Flow（以最熱銷的短夾為例）**：

```
→ 點「查商品」
→ 「你在找哪一類？」
   [短夾] [長夾] [鑰匙圈] [相機包]
→ 點「短夾」→ 送出 Product Card（見下方）
→ 「需要加刻字嗎？＋150 元」
   [要，幫我客製] [不用，直接購買]
```

**Product Card 範本**：

```
╔══════════════════════════╗
║  [商品圖片: 短夾_棕色]   ║
║  復古植鞣短夾            ║
║  🎨 顏色：深棕 / 焦糖 / 黑║
║  💰 NT$1,280             ║
║  📦 手工製作，7-10 個工作天║
╠══════════════════════════╣
║  [立即訂購] [看更多圖]   ║
╚══════════════════════════╝
```

**Checkout 路徑**：
- 點「立即訂購」→ LIFF（LINE Front-end Framework）頁面填寫尺寸/顏色/刻字內容 → LINE Pay 付款
- 付款完成 → 自動回傳訂單確認訊息 + 預計出貨日

**Post-Purchase Sequence**：

| 時間點 | 訊息內容 |
|-------|---------|
| 付款後即時 | 訂單確認 + 手工製作說明（Amy 親自製作的故事，3 句話） |
| 出貨當天 | 出貨通知 + 追蹤連結 |
| 收貨後 7 天 | 「皮革保養小訣竅」圖文 + 詢問使用狀況 |
| 收貨後 30 天 | 「老客戶優先看新色」預購邀請 |

---

## Result

```markdown
# Conversational Commerce Plan: 木質皮革工坊

## Channel Selection
- Primary: LINE Official Account — 台灣 95% 滲透率，25-45 歲目標客群主力通訊工具
- Entry points: Instagram bio QR code、蝦皮店頁標籤、快閃市集 QR 立牌
- 方案: LINE Premium（月費 NT$800，5,000 則/月）

## Conversation Flow
1. Welcome: 歡迎 + Rich Menu 三選一（查商品 / 刻字客製 / 訂單查詢）
2. Discovery: 品類選單 → Product Card（圖、價格、工期）
3. Product Card: 商品圖 + 顏色選項 + 價格 + 出貨天數 + [立即訂購]
4. Checkout: LIFF 表單（顏色/刻字）→ LINE Pay 付款（全程不離開 LINE）
5. Post-purchase: 付款確認 → 出貨通知 → 7 天保養貼文 → 30 天老客優惠

## Bot vs Human Split
| Scenario | Handler | SLA |
|----------|---------|-----|
| 款式/顏色查詢 | Bot | 即時 |
| 價格/付款方式 | Bot | 即時 |
| 出貨時間查詢 | Bot | 即時 |
| 客製刻字需求確認 | Bot 收集 → Amy 確認 | Amy 4 小時內回覆 |
| 投訴 / 瑕疵品 | 立即轉 Amy | Amy 30 分鐘內回覆 |

## KPIs
| Metric | Target |
|--------|--------|
| Bot 回應時間 | < 3 秒 |
| Amy 人工回應時間 | < 4 小時（客製）/ 30 分鐘（投訴） |
| Bot Containment Rate | > 70%（現況 0%） |
| Conversation-to-purchase Rate | > 25%（現況 12%） |
| CSAT | > 4.2/5 |
```

**預估效益**（90 天後）：

- Amy 每週回覆工作量：90 則 → 27 則（省 3 小時/週）
- 成交率：12% → 目標 25%（減少等待流失）
- 月營收增量估算：400 則 × 25% × NT$1,280（均價）= 約 **NT$128,000**（vs. 現況 NT$61,440）

**第一步行動**：申請 LINE Official Account Premium、安裝 [MCP LINE OA 工具] 設定 Rich Menu，下週前完成 Welcome Flow 和 Product Card 設計。
