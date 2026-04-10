我直接撰寫範例檔案內容：

```markdown
# Example: 新創電商 App 的病毒式行銷種子選擇

## Scenario

**公司：** Shoprise — 台灣新創跨境電商 App，專注東南亞市場
**時間：** 2026 年 Q2 新品上線前
**問題：**

Shoprise 行銷團隊準備在印尼 Instagram 用戶社群中推廣新功能「一鍵跨境比價」。他們已爬取一份印尼電商 KOL/用戶互動圖：50,000 個節點（用戶帳號），230,000 條有向邊（一個用戶分享後另一用戶互動過）。預算只夠免費送出 10 份試用禮包，也就是最多選 **k=10** 個種子用戶。

團隊的第一直覺是「選追蹤者最多的前 10 名 KOL」，但 Growth Lead 懷疑這樣會有嚴重的影響力重疊，想知道 Greedy CELF 到底能多比 top-degree 好。

---

## Analysis

### Phase 1：輸入驗證

| 項目 | 值 |
|------|-----|
| 節點數 | 50,000 |
| 邊數 | 230,000（有向） |
| 擴散模型 | Independent Cascade（IC） |
| 邊傳播機率 | 加權反入度：`p(u→v) = 1 / in_degree(v)`，上限 0.1 |
| k（種子數） | 10 |
| Monte Carlo 模擬次數 | 10,000 |

**模型選擇理由：** IC 適合「一次性分享」行為（看到貼文分享就結束），LT 更適合需要多次曝光才採納的場景（如技術產品）。電商 App 分享屬一次性觸發，選 IC。

**Gate 通過：** 圖載入完整，無孤立節點占比 < 5%，k=10 已定義。

---

### Phase 2：CELF 執行過程（節錄）

初始化 `S = ∅`，對全部 50,000 節點跑第一輪邊際增益估計。

**第 1 輪選擇：**

| 候選節點 | 粉絲數（in-degree 排名） | 邊際增益 σ({v}) |
|----------|--------------------------|-----------------|
| `@fashionid_rina` | #1（82K 粉絲） | 412 |
| `@techreview_budi` | #3（61K 粉絲） | 387 |
| `@lifestylejkt_sari` | #2（74K 粉絲） | 351 |
| `@shopdeals_medan` | #18（21K 粉絲） | 396 |

> `@shopdeals_medan` 雖然粉絲數排第 18，邊際增益卻排第 2——因為她的受眾與 `@fashionid_rina` 重疊極低，且活躍互動率高。

→ **選入 S：`@fashionid_rina`（邊際增益 412）**

**CELF 剪枝效果：** 第 2 輪起，73% 的節點因上界 ≤ 當前最佳值而跳過重新計算，有效評估節點從 50,000 降至 ~13,500。

**前 5 輪選擇結果：**

| 輪次 | 選入節點 | 邊際增益 | 粉絲數排名 |
|------|----------|----------|------------|
| 1 | `@fashionid_rina` | 412 | #1 |
| 2 | `@shopdeals_medan` | 389 | #18 |
| 3 | `@techreview_budi` | 341 | #3 |
| 4 | `@komunitas_hemat_sby` | 298 | #47（社群帳號） |
| 5 | `@travelblogger_lombok` | 267 | #9 |

注意：排名 #2 的 `@lifestylejkt_sari` 直到第 7 輪才被選入，因為她的受眾與 `@fashionid_rina` 重疊達 68%，邊際增益在 S 已有 rina 後驟降。

---

### Phase 3：與基準線比較

所有結果均為 R=10,000 次 Monte Carlo 平均值：

| 策略 | 期望觸及人數 | 相對 Greedy |
|------|-------------|-------------|
| 隨機 10 人 | 730 | −71% |
| Top-10 by Degree（直覺法） | 1,940 | −24% |
| Top-10 by PageRank | 2,180 | −15% |
| **Greedy CELF（本方法）** | **2,547** | — |

**Gate 通過：** Greedy（2,547）顯著優於 Degree heuristic（1,940），差距 607 人（+31%）。差距主因：Degree heuristic 的 top-10 中有 4 對帳號受眾重疊超過 50%，嚴重浪費種子預算。

---

### Phase 4：輸出

```json
{
  "seeds": [
    {"node": "@fashionid_rina",       "marginal_gain": 412, "selection_order": 1},
    {"node": "@shopdeals_medan",      "marginal_gain": 389, "selection_order": 2},
    {"node": "@techreview_budi",      "marginal_gain": 341, "selection_order": 3},
    {"node": "@komunitas_hemat_sby",  "marginal_gain": 298, "selection_order": 4},
    {"node": "@travelblogger_lombok", "marginal_gain": 267, "selection_order": 5},
    {"node": "@parentingid_dewi",     "marginal_gain": 241, "selection_order": 6},
    {"node": "@lifestylejkt_sari",    "marginal_gain": 198, "selection_order": 7},
    {"node": "@gadgetzone_sby",       "marginal_gain": 176, "selection_order": 8},
    {"node": "@foodie_makassar",      "marginal_gain": 159, "selection_order": 9},
    {"node": "@smebizid_bandung",     "marginal_gain": 144, "selection_order": 10}
  ],
  "expected_spread": 2547,
  "baselines": {
    "random":      730,
    "top_degree":  1940,
    "top_pagerank": 2180,
    "greedy":      2547
  },
  "metadata": {
    "k": 10,
    "model": "independent_cascade",
    "propagation_prob": "weighted_inverse_indegree_cap_0.1",
    "mc_simulations": 10000,
    "nodes": 50000,
    "edges": 230000,
    "celf_nodes_evaluated": 13500
  }
}
```

---

## Result

**建議：** 將 10 份試用禮包寄給上表中按 `selection_order` 排序的種子用戶，預期觸及 **~2,547 人**，比直覺選 Top-10 大 V 多觸及 **607 人（+31%）**。

**關鍵洞察：**
- `@shopdeals_medan`（粉絲排名 #18）是第 2 顆種子，因為她覆蓋的是棉蘭地區的中小型買家社群，與雅加達 KOL 受眾完全不重疊。
- 若改用 LT 模型（例如推廣需要多次接觸才採納的 B2B 工具），最優種子集合會不同——`@komunitas_hemat_sby` 這類社群帳號可能排名更前，因為它能反覆觸達同一批高門檻用戶。
- 下一步可用實際歷史分享資料校正邊傳播機率，取代目前的 `1/in_degree` 估計，預期能再提升準確度 10-15%。
```

這就是最終的 `sample_scenario.md` 內容。要我直接寫入檔案嗎？
