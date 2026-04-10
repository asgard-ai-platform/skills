# Example: 台灣電商網站反向連結健檢

## Scenario

**用戶問題：**

> 我們是台灣中型家具電商「木質家居」（mokuzai.tw），近三個月自然搜尋流量下降 22%。SEO 顧問懷疑是 Google 懲罰導致，請幫我們評估反向連結品質，找出需要 disavow 的有毒連結，並評估整體連結輪廓健康狀況。

**背景資訊：**
- 網站上線 4 年，主要商品：實木餐桌、沙發、收納家具
- 2024 年底曾委託外包公司做「SEO 衝排名」，事後發現對方使用批量建連結
- 從 Ahrefs 匯出 487 條反向連結，涵蓋 234 個 referring domains
- 匯出日期：2025-03-10

---

## Analysis

### Phase 1：Input Validation

匯出資料確認欄位完整：

| 欄位 | 狀態 |
|------|------|
| Referring domain | ✅ |
| Domain Rating (DR) | ✅ |
| Anchor text | ✅ |
| Link type (do/nofollow) | ✅ |
| First seen date | ✅ |

**Gate passed** — 487 條連結，234 個 referring domains，資料可進行分析。

---

### Phase 2：Core Algorithm

**步驟 1：依 referring domain 去重**

487 條原始連結 → 234 個唯一 referring domains（部分站點貢獻多條連結，去重後以最高 DR 連結代表）。

**步驟 2：DR 分佈評分**

| DR 區間 | Domains 數 | 佔比 | 評分 |
|---------|-----------|------|------|
| DR 60+ | 18 | 7.7% | 高品質 |
| DR 20–59 | 67 | 28.6% | 中等 |
| DR 1–19 | 89 | 38.0% | 低品質 |
| DR 0 (新站/死站) | 60 | 25.6% | 可疑 |

平均 DR：**21.3**（台灣電商平均水準約 28–35，偏低）

**步驟 3：有毒連結標記**

篩選條件：

1. DR < 10 且連結超過 3 條（批量建連結特徵）
2. 非中文、非英文語系（越南語、俄語垃圾連結農場）
3. 網域含 `bestlinks`、`seolinkfarm`、`guestpost99` 等已知 PBN 名稱模式
4. 連結頁面標題與家具完全無關（如：博弈、藥品、成人內容）

標記結果：**41 個 referring domains 列為有毒**

| 類型 | 數量 | 典型特徵 |
|------|------|---------|
| 連結農場 (link farm) | 19 | DR 0–3，頁面只有連結清單，無實質內容 |
| PBN 網域 | 12 | DR 8–15，多個網域指向同一 IP 段 |
| 無關語系垃圾站 | 7 | .ru / .vn 網域，頁面為俄文/越文 |
| 已下線但仍被計算的死站 | 3 | HTTP 500，但 Ahrefs 仍顯示歷史連結 |

**步驟 4：錨文字分佈分析**

| 錨文字類型 | 佔比 | 健康基準 | 狀態 |
|-----------|------|---------|------|
| 品牌名（木質家居、mokuzai） | 12% | 30–50% | ⚠️ 偏低 |
| 裸網址（mokuzai.tw） | 8% | 15–25% | ⚠️ 偏低 |
| 精確關鍵字（實木餐桌推薦） | 41% | < 10% | 🔴 嚴重過高 |
| 部分關鍵字（餐桌、家具） | 28% | 10–20% | ⚠️ 偏高 |
| 雜項（點此、更多） | 11% | 10–20% | ✅ 正常 |

**診斷**：精確關鍵字錨文字達 41%，遠超安全值 (<10%)，這是人工建連結的典型特徵，與外包 SEO 公司的操作高度吻合。這是觸發 Google 懲罰的主要嫌疑。

---

### Phase 3：Verification

**交叉驗證**：

- 將 41 個有毒 domains 比對 Moz Spam Score > 60 的黑名單，確認 37 個重疊
- 4 個 DR 低但未出現在黑名單的 domains 進行人工覆核：
  - 2 個確認為新創小型部落格，非垃圾站 → 移出 disavow 清單
  - 2 個確認為連結農場 → 維持 disavow

**最終有毒清單：39 個 referring domains**

**Gate passed** — Anchor profile 異常確認，有毒連結清單核實完成。

---

### Phase 4：連結輪廓健康總結

**時間序列異常**：

檢查 first seen date — 2024 年 10 月至 11 月間出現 **單月新增 78 個 referring domains**，遠超正常月均 5–8 個。這個爆量時間點與外包 SEO 操作時間吻合，也是 Google 演算法更新觸發懲罰的典型信號。

---

## Result

```json
{
  "profile": {
    "referring_domains": 234,
    "avg_dr": 21.3,
    "toxic_count": 39,
    "anchor_diversity": 0.31,
    "dr_distribution": {
      "dr_60_plus": "7.7%",
      "dr_20_59": "28.6%",
      "dr_1_19": "38.0%",
      "dr_0": "25.6%"
    },
    "exact_match_anchor_ratio": "41%",
    "health_score": "Poor — Penalty Risk High"
  },
  "actions": [
    {
      "type": "disavow",
      "domains": [
        "bestlinks99.ru",
        "seofarm-tw.com",
        "guestpost-asia.vn",
        "... (共 39 個 domains)"
      ],
      "reason": "link farm pattern / PBN / 無關語系垃圾站",
      "priority": "high",
      "deadline": "2025-03-20 前提交 Google Disavow Tool"
    },
    {
      "type": "anchor_text_rebalancing",
      "target": "精確關鍵字錨文字降至 10% 以下",
      "method": "停止任何人工建連結；透過 PR 與媒體曝光獲取品牌錨文字自然連結",
      "priority": "high"
    },
    {
      "type": "link_building",
      "focus": "DR 40+ 台灣家居 / 設計 / 生活風格媒體",
      "targets": ["La Vie 行動家", "Shopping Design", "品味台灣生活"],
      "method": "內容合作、產品評測、專家專欄",
      "priority": "medium"
    }
  ],
  "risk_flags": [
    "2024-10 單月爆量 78 個 referring domains — Google spam filter 觸發風險",
    "41% exact-match anchor ratio — 遠超安全值，演算法懲罰主因",
    "DR 0 死站佔 25.6% — 拉低整體輪廓品質"
  ],
  "metadata": {
    "tool": "ahrefs",
    "export_date": "2025-03-10",
    "analysis_date": "2025-03-12",
    "analyst": "algo-seo-backlink"
  }
}
```

**行動摘要：**

1. **立即（本週）**：提交 39 個 domains 的 disavow 檔案至 Google Search Console
2. **短期（1–3 個月）**：停止所有人工建連結，等待 Google 重新爬取並生效
3. **中期（3–6 個月）**：透過真實內容合作取得 5–10 條 DR 40+ 高品質連結，稀釋現有不健康錨文字比例
4. **預期**：Disavow 生效約需 2–3 個月；流量恢復需 4–6 個月，視 Google 重新評估時間而定

> **注意**：DA/DR 是 Ahrefs/Moz 的第三方估算值，非 Google 官方指標。Disavow 檔案提交後無法即時看到效果，切勿因等待焦慮而重複提交或額外操作。
