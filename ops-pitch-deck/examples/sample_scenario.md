我沒有直接寫檔案的工具，直接輸出 markdown 內容讓你貼存：

---

# Example: SaaS 新創募資 Pitch Deck — ClearRoute 物流追蹤平台

## Scenario

**用戶情境：**

ClearRoute 是一家台灣新創，提供 B2B 跨境物流可視性 SaaS。創辦人 Amy Chen 正準備向早期 VC 募集 NT$45M（約 $1.5M USD）的 Seed+ 輪。她問：

> "我有一個投資人 meeting 在三週後，需要準備 pitch deck。公司做跨境物流追蹤，已經有 28 個付費客戶、月營收 NT$380K，MoM 成長 22%。我應該怎麼結構這個 deck？幫我把每張 slide 的內容整理出來。"

---

## Analysis

### 診斷：Amy 的強弱項

**最強信號（必須放第一位）：**
- MoM 22% 成長 → 年化超過 9 倍
- 28 個付費 B2B 客戶（B2B 每個客戶都算數）
- 月收 NT$380K → 年化 ARR ≈ NT$4.56M

**需要補強的洞見：**
- 市場規模需要有台灣 → 東南亞路徑的 bottom-up 計算
- Competition 2×2 不能只打「比 DHL 便宜」，要找到真正的差異化軸

**10-15 Slides 紀律：**
Amy 原本想加一張「Technology Architecture」slide，但這對早期 VC 不必要。砍掉 → 留 12 張。

---

## Result

```markdown
# Pitch Deck Outline: ClearRoute

## Slide-by-Slide Content

### 1. Title
- Company: ClearRoute
- Tagline: Real-time visibility for cross-border logistics — built for Taiwan's exporters
- Presenter: Amy Chen, CEO & Co-founder | amy@clearroute.io

---

### 2. Problem
- Pain point: 台灣中小型出口商平均每週花費 12 小時追蹤貨物狀態，橫跨 4–6 個不同物流商的系統，無法提供客戶即時更新
- 實際損失："延誤不透明" 是 B2B 出口商客訴第一名；每次 claim 處理平均費時 3 天、成本 NT$15,000
- Who has this problem: 台灣年營收 NT$10M–500M 的製造業出口商（約 28,000 家）

---

### 3. Solution
- What we do: 單一儀表板整合所有主要物流商 API，提供端對端貨況追蹤 + 異常即時警報
- How it works:
  - 接入 FedEx、UPS、DHL、台灣本地 7 家物流商
  - AI 異常偵測：當貨物偏離預定路線超過 4 小時，自動通知負責人
  - 白標客戶入口：出口商的客戶可用品牌化頁面查詢自己的貨況

---

### 4. Product
- 主畫面：地圖 + 即時貨況 timeline，同時顯示 150 個活躍出貨
- 警報中心：依嚴重程度分級（紅/黃/綠），平均每日節省 2.3 小時人工追蹤
- 客戶入口截圖：客戶自助查詢，減少 60% 客服電話量（以現有客戶平均值）

---

### 5. Market
- TAM: $8.2B — 全球中小型出口商物流 SaaS（Gartner 2025）
- SAM: $320M — 台灣 + 東南亞六國製造業出口商（28,000 + 85,000 家，ARPU $1,200/yr）
- SOM: NT$180M（$6M USD）at Y3 — 攻下台灣市場 12%（→ 3,360 客戶）
  - 計算方法：bottom-up，目前轉換率 3.2%，預期透過通路合作提升至 5%

---

### 6. Business Model
- Revenue model: 年訂閱 SaaS（月繳或年繳，年繳 9 折）
- 定價：
  - Starter NT$4,800/月（1–50 出貨/月）
  - Growth NT$12,000/月（51–300 出貨/月）→ 佔現有客戶 70%
  - Enterprise 客製報價（300+ 出貨）
- Unit economics（基於現有 28 客戶）：
  - 平均 MRR/客戶：NT$13,600
  - CAC：NT$28,000（直銷）
  - LTV（假設 36 個月留存）：NT$489,600
  - LTV/CAC：**17.5x**

---

### 7. Traction
- ARR：NT$4.56M（月收 NT$380K）
- MoM 成長：22%（連續 6 個月）
- 付費客戶：28 家，0 churned（100% retention，12 個月）
- NPS：72
- Pipeline：42 家進入 trial，預計 Q2 轉換 15 家
- 里程碑：
  - 2025-08：MVP 上線
  - 2025-11：第一個付費客戶
  - 2026-02：整合台灣前 7 大物流商
  - 2026-04：NT$380K MRR（今天）

---

### 8. Competition
- 2×2 軸：**整合深度**（橫軸，低→高） vs **中小企業友好度**（縱軸，低→高）
- 市場現況：
  - 左下：自建 Excel 追蹤（間接競爭）
  - 左上：Flexport — 貴、以大型企業為主，需要客製導入
  - 右下：FourKites、project44 — 整合強但 UI 複雜、定價 $30K+ USD/yr
  - **右上：ClearRoute** — 台灣物流商深度整合 + 30 分鐘上線、NT$5K 起跳

---

### 9. Team
- Amy Chen（CEO）：前 Shopee 台灣物流運營主管 5 年，親手建過 300+ 供應商 API 整合
- Kevin Liu（CTO）：前 TSMC IT 架構師，API gateway 專家，開源貢獻者（logistics-sdk，1.2K stars）
- Iris Wang（Sales）：前 91APP 企業客戶總監，帶出 NT$120M ARR 業績

---

### 10. Financials
|          | Y1（2026）  | Y2（2027）  | Y3（2028）  |
|----------|------------|------------|------------|
| 客戶數     | 120        | 480        | 1,400      |
| ARR      | NT$19.6M   | NT$78.4M   | NT$228M    |
| 毛利率     | 68%        | 72%        | 76%        |
| 淨虧損     | (NT$18M)   | (NT$12M)   | NT$8M      |

**關鍵假設：**
- 客戶成長：Y1 以直銷為主（CAC NT$28K）；Y2 起通路合作（物流商 referral，CAC 降至 NT$12K）
- 毛利率提升：API 成本固定，客戶增加攤薄
- Y3 損益平衡：客戶數 900 家時達到

---

### 11. The Ask
- Raising: NT$45M（Seed+）
- Use of funds:
  - 產品 & 工程 40%（NT$18M）— 擴充東南亞物流商整合、AI 異常預測
  - Sales & Marketing 35%（NT$15.75M）— 新增 4 位企業 AE，開展物流商通路
  - 營運 & 法務 25%（NT$11.25M）— 財務、合規、辦公室
- 本輪達到的里程碑：
  - 120 付費客戶（目前 28）
  - 進入新加坡與越南市場（各 20 家試點）
  - ARR NT$19.6M → 具備 Series A 基礎

---

### 12. Contact
- Amy Chen — amy@clearroute.io
- Demo 預約：calendly.com/clearroute-demo
- Data room 已備妥，可在本次 meeting 後立即提供

---

## Design Guidelines
- Font size: ≥ 24pt（簡報字體）、正文用 Inter 或 Noto Sans
- Max words per slide: 30–40
- Slide 7（Traction）用折線圖顯示 MoM 成長曲線，視覺衝擊優先
- Slide 8（Competition）用 2×2 矩陣，ClearRoute 用品牌色標記
- 配色：深藍底 + 白字（正式感），accent 用 teal（物流/地圖聯想）
```

---

**Amy 應備的補充材料（Email 版 Deck 差異）：**

簡報版（meeting 用）：每張 slide ≤ 40 字，大圖優先。  
Email 版（投資人事前閱讀）：每張 slide 加一段說明文字，數字加腳註說明來源。  
Financial model：bottom-up Excel，Amy 在 Q&A 時需能解釋每個假設怎麼來。
