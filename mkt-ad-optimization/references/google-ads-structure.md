# Google Ads Account Structure

Account 結構直接影響演算法的學習效率、報表的可讀性、以及優化操作的顆粒度。結構錯誤往往是「廣告沒效」的根本原因，而非出價或素材問題。

---

## 三層架構

```
Account
└── Campaign（預算、目標、網路、地理）
    └── Ad Group（主題、受眾、出價）
        └── Ad（文案、素材、最終 URL）
                + Keywords / Audiences
```

每一層只控制它自己的變數：

| 層級 | 控制什麼 | 不要在這層做什麼 |
|------|---------|----------------|
| Campaign | 日預算、出價策略、廣告網路、地理、裝置調整 | 不要用一個 campaign 混合多個商業目標 |
| Ad Group | 關鍵字主題群、受眾、Ad Group 出價上限 | 不要放超過 20 個關鍵字 |
| Ad | 標題、描述、最終 URL | 不要讓 ad 的承諾與 landing page 不符 |

---

## Campaign 類型選擇

| 場景 | Campaign 類型 | 備註 |
|------|--------------|------|
| 使用者主動搜尋產品/服務 | Search | 台灣最高轉換意圖 |
| 視覺產品、再行銷 | Display | CPC 低但意圖弱 |
| 影片品牌曝光 | Video (YouTube) | 用於漏斗上層 |
| 全自動、有足夠轉換資料 | Performance Max | 需 50+ 轉換/月才有效 |
| 實體門市導流 | Local | 需 Google Business Profile |

> **不要** 把 Search 和 Display 混在同一個 campaign（「搜尋聯播網含多媒體廣告」）。預算會流向 Display，但你的報表卻看不清楚。

---

## Search Campaign 結構原則

### SKAG vs STAG vs 主題群組

三種主流結構，各有適用情境：

| 結構 | 定義 | 優點 | 缺點 |
|------|------|------|------|
| **SKAG** (Single Keyword Ad Group) | 每個 ad group 只有 1 個關鍵字 | 出價最精準、QS 易優化 | 管理成本極高，smart bidding 資料分散 |
| **STAG** (Single Theme Ad Group) | 每個 ad group 5-15 個語意相近關鍵字 | 轉換資料集中、smart bidding 表現較好 | 出價顆粒度較粗 |
| **主題群組** | 依產品/服務線分群，每群 15-20 個關鍵字 | 適合中小帳號，資料集中 | 難以針對高價值關鍵字單獨優化 |

**2024 年後建議**：使用 STAG，原因是 Google Smart Bidding 需要足夠的 ad group 層級轉換資料，SKAG 的轉換訊號太稀疏，導致演算法無法有效學習。

### 實際分群範例（健身房招生）

```
Campaign: Search - 健身房招生 (Target CPA: NT$500)
│
├── Ad Group: 健身房 品牌詞
│   Keywords: [健身工廠], [world gym], [健身房 推薦]
│   Bid: +50% (brand intent)
│
├── Ad Group: 個人訓練
│   Keywords: [私人教練], [個人教練 費用], [PT 課程]
│   Bid: base
│
├── Ad Group: 地區 + 健身
│   Keywords: [信義區健身房], [台北 健身], [內湖 gym]
│   Bid: base (location modifier if needed)
│
└── Ad Group: 課程/方案
    Keywords: [健身月票], [健身房 費用], [gym 辦卡]
    Bid: -20% (higher funnel)
```

---

## 關鍵字比對類型

| 比對類型 | 語法 | 觸發邏輯 | 適用時機 |
|---------|------|---------|---------|
| 廣泛比對 | `關鍵字` | 相關搜尋（含同義詞、拼字錯誤） | 搭配 Smart Bidding 探索新搜尋詞 |
| 詞組比對 | `"關鍵字"` | 含此詞組的搜尋 | 兼顧覆蓋與控制 |
| 完全比對 | `[關鍵字]` | 幾乎完全相同的搜尋 | 高價值、高成本關鍵字 |

**實務分層策略**：

```
高出價完全比對  [私人教練 台北]        → 最高意圖，不浪費預算
中出價詞組比對  "個人訓練"             → 捕捉長尾變體
低出價廣泛比對  健身教練               → 搭配 Smart Bidding 探索
```

廣泛比對 + Target CPA/ROAS 是目前 Google 官方建議的預設組合，但**前提是帳號有足夠轉換資料**（建議 30+ 次/月）。新帳號、新 campaign 先從詞組比對開始。

---

## 否定關鍵字（Negative Keywords）

否定關鍵字是 Search Campaign 最高 ROI 的優化動作。每週審查搜尋詞報告一次。

### 帳號層 vs Campaign 層 vs Ad Group 層

| 層級 | 用途 | 範例 |
|------|------|------|
| 帳號層否定清單 | 永遠不想觸發的詞（節省跨 campaign 設定） | `免費`, `破解`, `二手` |
| Campaign 層 | 此 campaign 主題外的詞 | 在「個人訓練」campaign 否定 `健身器材 購買` |
| Ad Group 層 | 防止 ad group 互搶流量 | 在「地區詞」ad group 否定品牌詞（品牌詞有專屬 ad group） |

### 常見應立即加入的否定詞（健身/服務業通用）

```
免費
試用
ptt
dcard
評價
缺點
薪水
徵才
職缺
工讀
```

### 防止 Ad Group 互搶流量（Cross-Group Negatives）

當同一 campaign 有多個 ad group，Google 可能把同一個搜尋詞分配給「錯誤」的 ad group。解法：

```
Ad Group A: 個人訓練
  Negative: [健身月票], [辦卡]

Ad Group B: 健身月票
  Negative: [個人訓練], [私人教練]
```

這樣每個搜尋詞只會對應到語意最相近的 ad group。

---

## Quality Score 與帳號結構的關係

Quality Score (QS) 由三個因素組成：

```
QS (1-10) = f(預期 CTR, 廣告關聯性, 到達頁面體驗)
```

結構直接影響「廣告關聯性」分項：當 ad group 內的關鍵字主題越集中，廣告文案越容易包含關鍵字，QS 越高。

**QS 對出價的影響**：

```
實際 CPC = 下一名出價 / 你的 QS × (下一名 QS / 你的出價)
         ≈ 競爭者廣告排名 / 你的 QS + NT$0.01
```

**實際數字範例**：

| 廣告主 | 出價 | QS | 廣告排名 | 實際 CPC |
|-------|------|----|---------|---------|
| 你 | NT$10 | 8 | 80 | ~NT$3.75 |
| 競爭者 A | NT$15 | 4 | 60 | ~NT$10.01 |
| 競爭者 B | NT$8 | 6 | 48 | — |

你出價比競爭者 A 低 33%，但因為 QS 高出 2 倍，廣告排名更高、CPC 更低。

**提升 QS 的結構手段**：

1. Ad group 主題緊縮（每組只含語意相近的關鍵字）
2. 廣告文案的標題欄位包含目標關鍵字
3. Landing page URL 與廣告主題匹配（`/personal-training` 不要指向首頁）

---

## Responsive Search Ads（RSA）結構

每個 ad group 建議 1 個 RSA（Google 已停止 Expanded Text Ads 的新增）。

```
RSA 結構：
  - 最多 15 個標題（每個 ≤ 30 字元）
  - 最多 4 個描述（每個 ≤ 90 字元）
  - Google 自動測試組合，選最高 CTR 的組合展示
```

**Pin 的使用**：如果有必須出現的文案（品牌名、法規聲明），使用 Pin 固定到特定位置。但 Pin 過多會限制 Google 的組合能力，建議 Pin 的標題不超過 2 個。

**15 個標題的分配建議**：

| 類型 | 數量 | 範例 |
|------|------|------|
| 關鍵字插入（含主要關鍵字） | 3-4 | `台北個人訓練課程` |
| 利益訴求（Benefit） | 3-4 | `12週體態改造計畫` |
| 信任指標（Social Proof） | 2-3 | `已協助500位學員達標` |
| CTA | 2-3 | `免費體驗課 立即預約` |
| 差異化 | 2-3 | `教練皆有國際認證` |

---

## Campaign 預算分配邏輯

### 帳號總預算分配原則

不要讓所有 campaign 搶同一個預算池。先依漏斗位置分配：

```
總預算分配建議（電商 / 服務業）：

品牌關鍵字 Campaign    10-15%  ← 低 CPA，保護品牌
高意圖搜尋 Campaign    40-50%  ← 核心轉換來源
競品 Campaign          10-15%  ← 可選，視競爭強度
再行銷 Campaign        15-20%  ← ROAS 通常最高
Display/YouTube        10-15%  ← 漏斗上層
```

### 新帳號建立順序

```
Week 1-2:   品牌詞 Campaign（成本低、轉換快，快速累積轉換資料）
Week 2-4:   核心高意圖 Campaign（搭配手動 CPC 或 Maximize Conversions）
Month 2:    擴展到再行銷（需要足夠的網站流量）
Month 2-3:  切換 Smart Bidding（此時有足夠轉換資料讓演算法學習）
Month 3+:   競品 / Display / YouTube
```

---

## Smart Bidding 的啟動門檻

Smart Bidding 在資料不足時表現會比手動出價更差。

| 出價策略 | 建議啟動條件 |
|---------|------------|
| Maximize Conversions | 無特定門檻，但至少要有轉換追蹤設定正確 |
| Target CPA | 同一 campaign 每月 30+ 次轉換（Google 建議 50+） |
| Target ROAS | 同一 campaign 每月 50+ 次轉換 |
| Enhanced CPC | 任何時候都可以，作為手動→smart bidding 的過渡 |

**學習期（Learning Period）**：

- 切換出價策略後，會進入 7-14 天的學習期
- 學習期內 CPA 可能上升 20-40%，屬正常現象
- **不要**在學習期內頻繁調整預算或出價目標（±20% 以上的調整會重啟學習期）
- 判斷是否脫離學習期：看 Campaign 狀態欄是否顯示「學習中」

---

## 常見結構錯誤與修正

| 錯誤 | 症狀 | 修正方式 |
|------|------|---------|
| 單一 campaign 放所有關鍵字 | 無法針對高價值關鍵字提高預算 | 依主題/漏斗位置拆分 campaign |
| Ad Group 關鍵字超過 20 個 | QS 低、廣告關聯性差 | 依語意重新分群，每組 5-15 個 |
| Search + Display 混合 campaign | 報表混濁，預算被 Display 吸走 | 拆成獨立 campaign |
| 從未加否定關鍵字 | 大量不相關點擊，CPA 高 | 每週審查搜尋詞報告，定期加否定詞 |
| 新帳號直接用 Target CPA | 演算法無資料可學習，CPA 失控 | 先用 Maximize Conversions 累積資料 |
| 所有廣告指向首頁 | 低 QS、低 CVR | 每個 ad group 對應主題相符的 landing page |
