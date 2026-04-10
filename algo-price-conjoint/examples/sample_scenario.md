# Example: SaaS 專案管理工具定價與功能取捨

## Scenario

**公司：** Flowdesk（台灣 B2B SaaS 新創，目標市場：中小企業專案管理）

**PM 的問題：**
> 我們正在規劃 2026 Q3 的新方案改版。現有方案分 Free / Pro ($599/月) / Enterprise。市場研究顯示用戶最在意「AI 自動排程」、「整合數量（Slack/Jira/…）」和「價格」，但我們不知道這三者的相對重要性，也不確定 AI 功能值多少錢。能不能量化一下用戶的 WTP？

**資料：**
- 已完成 CBC 問卷，樣本 N=318（台灣中小企業 IT 採購決策者）
- 設計：3 屬性 × 3 levels，D-optimal 設計，12 選擇題組，每組 3 個方案 + 無購買選項

**屬性與水準：**
| 屬性 | Level 1 | Level 2 | Level 3 |
|------|---------|---------|---------|
| AI 自動排程 | 無 | 基礎（建議） | 全自動 |
| 整合數量 | 5 個 | 15 個 | 無限 |
| 月費（/用戶） | $299 | $599 | $999 |

---

## Analysis

### Phase 1: 輸入驗證

- **屬性獨立性：** AI 排程與整合數量互不依賴 ✓
- **水準現實性：** $999 是市場上游方案實際售價（Asana Business），不是假設 ✓
- **樣本：** N=318 > 200 最低門檻 ✓
- **設計：** D-optimal 12 task × 3 alternatives，每屬性在每位置出現頻率均衡 ✓

**Gate passed.**

---

### Phase 2: 模型估計（Hierarchical Bayes）

使用 HB-MNL 估計個體層級 part-worth utilities（先驗：normal hierarchical prior，MCMC 10,000 次迭代，burn-in 2,000）。

**Part-worth utilities（群體平均）：**

| 屬性 | 水準 | Part-worth |
|------|------|-----------|
| AI 排程 | 無 | −1.42 |
| AI 排程 | 基礎（建議） | +0.61 |
| AI 排程 | 全自動 | +1.89 |
| 整合數量 | 5 個 | −0.83 |
| 整合數量 | 15 個 | +0.44 |
| 整合數量 | 無限 | +0.97 |
| 月費 | $299 | +2.31 |
| 月費 | $599 | +0.18 |
| 月費 | $999 | −2.14 |

**屬性重要性計算：**
- AI 排程 range = 1.89 − (−1.42) = **3.31**
- 整合數量 range = 0.97 − (−0.83) = **1.80**
- 月費 range = 2.31 − (−2.14) = **4.45**
- 總和 = 9.56

| 屬性 | 重要性 |
|------|--------|
| 月費 | 46.5% |
| AI 排程 | 34.6% |
| 整合數量 | 18.8% |

**WTP 推導（utility-to-price conversion）：**

price coefficient（每 $100）= (2.31 − (−2.14)) / (($999 − $299) / $100) = 4.45 / 7 = **0.636 utils / $100**

- WTP for AI 排程（無 → 全自動）= 3.31 / 0.636 × $100 = **$520/用戶/月**
- WTP for AI 排程（無 → 基礎）= 2.03 / 0.636 × $100 = **$319/用戶/月**
- WTP for 整合（5 → 無限）= 1.80 / 0.636 × $100 = **$283/用戶/月**

---

### Phase 3: 驗證

**Holdout task（保留 2 題未納入估計）：**
- Holdout hit rate = **71.4%**（> 60% 門檻 ✓）
- 符號檢查：價格越高效用越低（−2.14 → −0.18 → +2.31，即 $999 < $599 < $299）✓
- AI 全自動 > 基礎 > 無 ✓

**Gate passed.**

---

### 潛在細分（Latent Class，2-segment 解）

| 區隔 | 比例 | 特徵 | AI 排程重要性 | 價格重要性 |
|------|------|------|--------------|-----------|
| 功能導向（Segment A） | 58% | 軟體/科技業 IT | 41% | 35% |
| 價格敏感（Segment B） | 42% | 傳統產業採購 | 22% | 58% |

> **關鍵發現：** Segment A 的 WTP for AI 全自動 ≈ $680，Segment B 僅 ≈ $310。

---

## Result

```json
{
  "attribute_importance": [
    {"attribute": "price", "importance_pct": 46.5},
    {"attribute": "ai_scheduling", "importance_pct": 34.6},
    {"attribute": "integrations", "importance_pct": 18.8}
  ],
  "part_worths": {
    "ai_scheduling": {"none": -1.42, "basic": 0.61, "full_auto": 1.89},
    "integrations": {"5": -0.83, "15": 0.44, "unlimited": 0.97},
    "price": {"$299": 2.31, "$599": 0.18, "$999": -2.14}
  },
  "wtp": {
    "ai_scheduling_none_to_full_auto": 520,
    "ai_scheduling_none_to_basic": 319,
    "integrations_5_to_unlimited": 283
  },
  "metadata": {
    "respondents": 318,
    "model": "hierarchical_bayes",
    "holdout_hit_rate": 0.714,
    "segments": 2
  }
}
```

**給 PM 的三點建議：**

1. **AI 全自動排程是最大差異化點**，WTP $520 遠超功能開發成本預估。建議做為新 Pro+ 方案的核心賣點，定價 $799/月仍在 Segment A（58% 市場）的接受區間內。

2. **整合數量效益邊際遞減**：從 5→15 個整合的 WTP ≈ $126，但 15→無限的增量 WTP 僅 ≈ $83。維持「Pro 方案 15 個整合」即可，無限整合留給 Enterprise，不需要在 Pro 層放滿。

3. **勿外插到 $299 以下或 $999 以上**：本研究設計範圍 $299–$999，在此範圍外的 WTP 估計不可靠——若考慮免費方案轉換率，需另設計 Free vs. Paid 的獨立 CBC 研究。
