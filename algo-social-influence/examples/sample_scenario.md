# Example: 台灣機能服飾品牌網紅篩選

## Scenario

**APEX Running**（台灣中型跑步裝備品牌）正準備推出新款碳板跑鞋，預算 NT$600,000，目標受眾為 25–45 歲台灣跑者。行銷主任 Jessica 整理了五位候選網紅，要求依影響力排序並推薦最終名單。

候選資料（2026 年 Q1，各取最近 30 篇貼文均值）：

| Handle | 平台 | 粉絲數 | 平均按讚 | 平均留言 | 平均分享 | 主題 |
|--------|------|--------|----------|----------|----------|------|
| @runnerchris | Instagram | 480,000 | 2,100 | 48 | 12 | 路跑、賽事 |
| @taiwantrail | Instagram | 62,000 | 2,480 | 194 | 87 | 越野、裝備評測 |
| @fitnessmei | TikTok | 310,000 | 18,500 | 420 | 1,200 | 健身、生活風格 |
| @ultraken | Instagram | 28,000 | 1,540 | 312 | 95 | 超馬、訓練日誌 |
| @dailysports | Instagram | 890,000 | 1,780 | 31 | 8 | 泛運動 |

Jessica 額外提供：@runnerchris 曾被第三方工具標記 18% 可疑粉絲；@fitnessmei 屬於健身網紅，跑步內容佔比約 15%。

---

## Analysis

### Phase 1：輸入驗證

- 全部帳號均提供 30 篇以上貼文資料，通過最低樣本門檻（≥20 篇）。
- @runnerchris 可疑粉絲 18% → 有效粉絲調整為 480,000 × 0.82 = **393,600**。
- 平台基準差異：Instagram 平均互動率約 1.5–3%；TikTok 按讚型互動率基準 5–10%，需分平台正規化。

---

### Phase 2：核心算法

**權重設定**（碳板跑鞋 → 強調社群說服力，非純曝光）

| 維度 | 權重 |
|------|------|
| Reach | 0.20 |
| Engagement | 0.50 |
| Relevance | 0.30 |

#### Step 1：Reach Score（對數正規化，以百萬為上限）

```
Reach Score = log10(有效粉絲) / log10(1,000,000) × 100
```

| Handle | 有效粉絲 | Reach Score |
|--------|----------|-------------|
| @runnerchris | 393,600 | log10(393,600)/6 × 100 = **93.7** |
| @taiwantrail | 62,000 | **79.4** |
| @fitnessmei | 310,000 | **91.2** |
| @ultraken | 28,000 | **74.1** |
| @dailysports | 890,000 | **98.3** |

#### Step 2：Engagement Score（加權互動率，正規化至平台基準）

互動權重：分享 × 3、留言 × 2、按讚 × 1

```
加權互動 = (likes×1 + comments×2 + shares×3)
互動率 = 加權互動 / 有效粉絲 × 100
平台正規化分數 = (互動率 / 平台基準互動率) × 70  ← 上限 100
```

Instagram 基準加權互動率：約 2.5%；TikTok 基準：約 12%

| Handle | 加權互動 | 互動率(%) | 平台基準 | Engagement Score |
|--------|----------|-----------|----------|-----------------|
| @runnerchris | 2,100+96+36 = 2,232 | 2,232/393,600=0.57% | 2.5% | 0.57/2.5×70 = **15.9** |
| @taiwantrail | 2,480+388+261 = 3,129 | 3,129/62,000=5.05% | 2.5% | 5.05/2.5×70 = **100** (上限) |
| @fitnessmei | 18,500+840+3,600=22,940 | 22,940/310,000=7.4% | 12% | 7.4/12×70 = **43.2** |
| @ultraken | 1,540+624+285=2,449 | 2,449/28,000=8.75% | 2.5% | 8.75/2.5×70 = **100** (上限) |
| @dailysports | 1,780+62+24=1,866 | 1,866/890,000=0.21% | 2.5% | 0.21/2.5×70 = **5.9** |

#### Step 3：Relevance Score（跑步主題對齊度 × 受眾地區吻合度）

主題對齊（碳板跑鞋對應「路跑、超馬、越野裝備」），台灣受眾比例加成：

| Handle | 主題分 /100 | 台灣受眾% | Relevance Score |
|--------|------------|-----------|-----------------|
| @runnerchris | 90（路跑賽事）| 92% | **87** |
| @taiwantrail | 85（越野裝備）| 95% | **86** |
| @fitnessmei | 25（健身為主）| 80% | **22** |
| @ultraken | 95（超馬訓練）| 98% | **94** |
| @dailysports | 40（泛運動）| 85% | **37** |

#### Step 4：Composite Influence Score

```
Influence = 0.20×Reach + 0.50×Engagement + 0.30×Relevance
```

| Handle | Reach×0.2 | Eng×0.5 | Rel×0.3 | **Influence Score** |
|--------|-----------|---------|---------|---------------------|
| @runnerchris | 18.7 | 8.0 | 26.1 | **52.8** |
| @taiwantrail | 15.9 | 50.0 | 25.8 | **91.7** |
| @fitnessmei | 18.2 | 21.6 | 6.6 | **46.4** |
| @ultraken | 14.8 | 50.0 | 28.2 | **93.0** |
| @dailysports | 19.7 | 3.0 | 11.1 | **33.8** |

### Phase 3：驗證

- @ultraken 歷史合作紀錄（鞋品牌 BrandX，2025 Q3）：官網 UTM 追蹤顯示 promo code 使用率 3.8%，高於該次活動平均 1.2%。✅ 高分有依據。
- @taiwantrail 近期裝備評測影片平均留言中 28% 含購買意圖關鍵字（「連結在哪」、「哪裡買」）。✅ 驗證通過。
- @dailysports 無跑鞋相關歷史合作紀錄，互動以「加油」類情感留言為主，實際轉換存疑。⚠️

---

## Result

### 排名輸出

```json
{
  "rankings": [
    {
      "account": "@ultraken",
      "influence_score": 93.0,
      "reach": 74.1,
      "engagement": 100,
      "relevance": 94,
      "note": "超馬社群高度信任，promo code 歷史轉換率 3.8%"
    },
    {
      "account": "@taiwantrail",
      "influence_score": 91.7,
      "reach": 79.4,
      "engagement": 100,
      "relevance": 86,
      "note": "裝備評測口碑強，留言購買意圖高"
    },
    {
      "account": "@runnerchris",
      "influence_score": 52.8,
      "reach": 93.7,
      "engagement": 15.9,
      "relevance": 87,
      "note": "觸及廣但互動弱，且含 18% 可疑粉絲，CP 值低"
    },
    {
      "account": "@fitnessmei",
      "influence_score": 46.4,
      "reach": 91.2,
      "engagement": 43.2,
      "relevance": 22,
      "note": "TikTok 互動佳，但受眾與碳板跑鞋主題高度不吻合"
    },
    {
      "account": "@dailysports",
      "influence_score": 33.8,
      "reach": 98.3,
      "engagement": 5.9,
      "relevance": 37,
      "note": "粉絲數最高但互動最差，泛運動定位與品牌訴求錯位"
    }
  ],
  "metadata": {
    "accounts_analyzed": 5,
    "weights": {"reach": 0.2, "engagement": 0.5, "relevance": 0.3},
    "platform_benchmarks": {"instagram": 2.5, "tiktok": 12},
    "bot_adjusted": ["@runnerchris"]
  }
}
```

### 預算建議

| 網紅 | 建議合作形式 | 預算配置 |
|------|------------|----------|
| @ultraken | 深度開箱 + 賽事贊助 | NT$280,000 |
| @taiwantrail | 裝備評測影片系列（3 集）| NT$220,000 |
| @runnerchris | 不建議本次合作 | — |
| @fitnessmei | 若需 TikTok 破圈，限定短影音 | NT$100,000（可選）|
| @dailysports | 排除 | — |

> **關鍵決策依據**：@dailysports 粉絲數最多，但 Influence Score 最低（33.8）。
> 依 IRON LAW：粉絲數 ≠ 影響力，其互動率僅 0.21%（平台基準的 8%），
> 投入等同把預算燒在空洞曝光，而非真實影響。
