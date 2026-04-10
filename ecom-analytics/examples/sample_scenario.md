# Example: 母嬰品牌「小熊窩」Q4 營收下滑診斷

## Scenario

小熊窩（BearNest）是台灣中高端母嬰用品電商，主打有機棉寢具與嬰兒護膚品。行銷主管 Vivian 發現 2025 年 11 月整月營收 NT$1,820,000，比去年同期 NT$2,310,000 少了 21%，距離雙 11 衝刺目標更差了將近 30%。她問：「為什麼業績掉這麼多？我們的 GA4 數據要怎麼看？」

GA4 匯出數據（2025/11/01–11/30 vs 2024/11/01–11/30）：

| 指標 | 2025/11 | 2024/11 |
|------|---------|---------|
| Sessions | 48,200 | 44,100 |
| Product Views | 31,330 | 30,870 |
| Add to Cart | 3,856 | 4,939 |
| Begin Checkout | 2,120 | 3,210 |
| Purchase | 910 | 1,287 |
| Revenue | NT$1,820,000 | NT$2,310,000 |
| AOV | NT$2,000 | NT$1,795 |

---

## Analysis

### Phase 1: Traffic Check

Sessions **增加 9.3%**（48,200 vs 44,100），流量本身不是問題。代表廣告投放或 SEO 沒有明顯衰退，問題不在獲客端。

進一步確認流量品質：Product Views / Sessions = 65% vs 70%，略降但不顯著。排除流量品質大幅惡化。

> 結論：獲客階段 ✅ 正常，甚至略優於去年。

---

### Phase 2: Conversion Check — 找出最大斷點

逐層計算漏斗轉換率：

| 階段 | 2025/11 | 2024/11 | YoY 變化 |
|------|---------|---------|----------|
| Sessions → Product View | 65.0% | 70.0% | −5.0 pp |
| Product View → Add to Cart | **12.3%** | **16.0%** | **−3.7 pp** ← 最大斷點 |
| Add to Cart → Checkout | 55.0% | 65.0% | −10.0 pp |
| Checkout → Purchase | 42.9% | 40.1% | +2.8 pp |
| **Overall Conversion** | **1.89%** | **2.92%** | **−1.03 pp** |

**Product View → Add to Cart** 從 16% 掉到 12.3%，是整條漏斗中絕對值跌幅最大的關卡。加入購物車人數少了 1,083 人，往下游估算造成的營收缺口：

1,083 × 55% (ATC→Checkout) × 42.9% (Checkout→Purchase) × NT$2,000 = **約 NT$511,000**

這幾乎完整解釋了 NT$490,000 的營收差距。

Checkout → Purchase 轉換率今年反而略升（42.9% vs 40.1%），說明結帳流程與付款體驗沒有問題，AOV 也從 NT$1,795 升至 NT$2,000（+11.4%），排除商品定價與折扣侵蝕利潤的問題。

> 結論：問題集中在 **商品頁 → 加入購物車** 這一關。

---

### Phase 3: Revenue Check

| 指標 | 2025/11 | 2024/11 |
|------|---------|---------|
| Revenue per Session | NT$37.8 | NT$52.4 |
| AOV | NT$2,000 | NT$1,795 |
| 訂單數 | 910 | 1,287 |

Revenue per Session 下滑 27.9%，主因是訂單數大幅減少，而非 AOV 下降。AOV 上升可能反映高價品（寢具組）促銷力度較強，低價品（護膚品）銷售比例下滑。

> 結論：收益結構本身尚健康，但單位流量產出嚴重下滑，根源仍在轉換斷點。

---

### Phase 4: 假設根因

Product View → Add to Cart 在雙 11 旺季反而惡化，結合 AOV 上升，推測可能原因：

1. **雙 11 促銷設計問題**：去年可能有單品折扣或滿額贈，今年若改為「滿 NT$3,000 折 NT$300」，對猶豫的訪客誘因不足（尤其客單價落在 NT$1,500–2,000 的護膚品）。
2. **商品頁 A/B 測試或改版**：若 11 月初有改版，可能影響加購意願（建議對照 GA4 `view_item` 事件的 `item_category` 拆解，確認是哪類商品轉換率下滑）。
3. **競品搶量**：台灣雙 11 有機棉母嬰市場競爭加劇，競品若提供更強折扣，訪客比價後離開。

---

## Result

```markdown
# E-Commerce Performance Report: 小熊窩 BearNest

## Summary Dashboard
| Metric | 2025/11 | 2024/11 | Change | Status |
|--------|---------|---------|--------|--------|
| Sessions | 48,200 | 44,100 | +9.3% | 🟢 |
| Conversion Rate | 1.89% | 2.92% | −1.03 pp | 🔴 |
| AOV | NT$2,000 | NT$1,795 | +11.4% | 🟢 |
| Revenue | NT$1,820,000 | NT$2,310,000 | −21.2% | 🔴 |

## Funnel Analysis
| Stage | Volume | Rate | Drop-off vs LY | Benchmark |
|-------|--------|------|----------------|-----------|
| Sessions | 48,200 | 100% | — | — |
| Product Views | 31,330 | 65.0% | −5.0 pp | — |
| Add to Cart | 3,856 | 12.3% | **−3.7 pp** | 5–10% |
| Checkout | 2,120 | 55.0% | −10.0 pp | 40–60% of ATC |
| Purchase | 910 | 1.89% | −1.03 pp | 1–3% overall |

## Diagnosis
- Primary issue: **Engagement → Conversion（商品頁加購）** — Add to Cart rate 從 16% 跌至 12.3%
- Root cause: 雙 11 促銷門檻可能對客單價 NT$1,500–2,000 的護膚品訪客吸引力不足；
  或商品頁改版影響購買意圖。AOV 上升但訂單數銳減，顯示高價品促銷有效，但主力 SKU 轉換失守。

## Recommendations
1. **立即**：在 GA4 中拆解 `add_to_cart` 事件的 `item_category`，找出是哪個品類的
   加購率下滑最嚴重（護膚品 vs 寢具）。
2. **本月**：針對護膚品系列加入低門檻促銷（如「任 2 件 85 折」），降低猶豫訪客的決策成本。
3. **下月**：對商品頁進行 A/B 測試——加入社群評價數、庫存倒數或「雙 11 加購立折」
   banner，直接在商品頁給予轉換誘因。
4. **長期**：建立 Revenue per Session by Channel 看板，雙 11 前兩週即可預警，
   不必等月底才發現問題。
```
