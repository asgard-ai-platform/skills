# Example: SaaS 公司跨部門協作網絡分析

## Scenario

**公司：** Parchment Analytics（台北，150 人 SaaS 公司）
**情境：** 2026 年 Q1 組織重整後，HR 總監 Jenny Liu 想了解員工實際協作模式是否和組織架構圖吻合。她從 Slack workspace 匯出 2025-10-01 至 2025-12-31 三個月的訊息互動記錄（公開頻道訊息 + DM 次數統計，排除 bot）。

**用戶問題：**
> 「我有一份員工互動頻率表（CSV），想知道公司裡自然形成的『溝通圈』是什麼，看看和目前的 5 個部門分法是否一致。大約 130 名員工，3 個月資料。」

**資料格式（sample）：**
```csv
source,target,messages
alice.chen,bob.wu,142
alice.chen,carol.lin,88
bob.wu,dave.ho,201
...
```
共 2,847 條邊，平均權重 47 訊息/季。

---

## Analysis

### Phase 1：輸入驗證 & 圖建構

**節點：** 130 名員工（排除離職者 8 人後剩 122 個有效節點）
**邊：** 2,847 條（僅保留雙向互動總次數 ≥ 10 的邊，過濾後剩 1,983 條）
**孤立節點：** 3 名（新進員工 < 30 天），標記但排除於社群偵測之外

**Gate ✓** — 圖已載入，平均 degree = 32.5，密度 0.27（中等密集，適合 Louvain）

**Resolution limit 檢查（Iron Law）：**
- E = 1,983 條邊
- √(2E) ≈ √3,966 ≈ 63
- 結論：任何規模 < 63 人的社群理論上仍可偵測；但若存在規模 < 8-10 人的小圈子，可能被合併。→ 設 γ = 1.2 以抓較細粒度的社群。

### Phase 2：Louvain 執行

由於非確定性問題，執行 10 次取最高 modularity 的結果：

| 執行次數 | 社群數 | Modularity Q |
|---------|--------|-------------|
| Run 1   | 7      | 0.623       |
| Run 3   | 6      | 0.618       |
| Run 7   | 7      | **0.641**   ← 選用 |
| Run 10  | 8      | 0.629       |

**最佳結果：7 個社群，Q = 0.641**

### Phase 3：驗證 & 人工核對

**Gate 1 — Q > 0 ✓**（0.641 屬於強模組化結構）

**社群大小分佈：**

| 社群 ID | 規模 | 內部密度 | 前 3 高互動成員 |
|--------|------|---------|--------------|
| C0      | 38   | 0.51    | alice.chen, bob.wu, erin.kao |
| C1      | 22   | 0.63    | frank.lin, grace.wu, henry.chang |
| C2      | 18   | 0.58    | iris.chen, jason.ho, karen.liu |
| C3      | 15   | 0.44    | leo.wang, mia.sun, nina.tsai |
| C4      | 12   | 0.72    | oscar.chen, penny.yeh, quinn.wu |
| C5      | 11   | 0.69    | ryan.lin, sara.ho, tina.chen |
| C6      | 6    | 0.81    | uma.wu, victor.lin, wendy.kao |

**Gate 2 — 大小分佈 ✓**（最大社群 38 人，無「一個超大 + 全部 singleton」的異常）

**與官方部門對比（混淆矩陣摘要）：**

```
                C0   C1   C2   C3   C4   C5   C6
Engineering(52) 31    5    4    8    2    1    1
Product(28)      4   18    2    1    0    2    1
Sales(20)        1    0   11    0    7    1    0
Data(15)         2    0    1    8    1    2    1
HR/Ops(25)       0    1    0    0    2    5    3  ← 分散在多社群
```

**關鍵發現：**
1. **C0 = Engineering + Data 混合**：Data team 的 8 人與 Engineering 核心高度混融，顯示 Data 實際上與 Eng 耦合，而非獨立運作
2. **Sales 分裂為 C2 + C4**：Sales team 有兩個截然不同的溝通圈，調查後發現對應「企業客戶組」與「中小企業組」，兩組主管有各自的 Slack 群組文化
3. **C6（6人高密度群）= 跨部門核心橋接者**：包含 HR 總監、CTO、CMO 及 3 位 PM，是組織橋接節點
4. **HR/Ops 分散**：HR 成員出現在 5 個不同社群，符合其「支援性」角色定位

### Phase 4：Resolution 敏感性檢查

| γ 值 | 社群數 | Q     | 備注 |
|-----|-------|-------|-----|
| 0.8 | 4     | 0.587 | 過度合併，Sales 分裂消失 |
| 1.0 | 6     | 0.631 | 標準設定 |
| 1.2 | 7     | 0.641 | **選用**：揭露 Sales 內部分裂 |
| 1.5 | 11    | 0.608 | 過細，C6 被分解 |

γ = 1.2 是最佳解析度：Q 最高，且符合業務直覺。

---

## Result

```json
{
  "communities": [
    {"id": 0, "size": 38, "top_members": ["alice.chen", "bob.wu", "erin.kao"],
     "internal_density": 0.51, "label": "Engineering-Data融合圈"},
    {"id": 1, "size": 22, "top_members": ["frank.lin", "grace.wu", "henry.chang"],
     "internal_density": 0.63, "label": "Product Core"},
    {"id": 2, "size": 18, "top_members": ["iris.chen", "jason.ho", "karen.liu"],
     "internal_density": 0.58, "label": "Sales企業客戶組"},
    {"id": 3, "size": 15, "top_members": ["leo.wang", "mia.sun", "nina.tsai"],
     "internal_density": 0.44, "label": "Engineering Platform子團隊"},
    {"id": 4, "size": 12, "top_members": ["oscar.chen", "penny.yeh", "quinn.wu"],
     "internal_density": 0.72, "label": "Sales中小企業組"},
    {"id": 5, "size": 11, "top_members": ["ryan.lin", "sara.ho", "tina.chen"],
     "internal_density": 0.69, "label": "HR-Ops核心"},
    {"id": 6, "size": 6,  "top_members": ["uma.wu", "victor.lin", "wendy.kao"],
     "internal_density": 0.81, "label": "跨部門橋接者（高層）"}
  ],
  "summary": {
    "num_communities": 7,
    "modularity": 0.641,
    "largest": 38,
    "smallest": 6,
    "resolution_gamma": 1.2
  },
  "metadata": {
    "algorithm": "louvain",
    "runs": 10,
    "nodes": 122,
    "edges": 1983,
    "period": "2025-10-01 to 2025-12-31"
  }
}
```

**給 Jenny Liu 的建議：**

1. **組織架構與實際溝通有顯著落差**：偵測到 7 個通訊社群 vs 官方 5 個部門，主要差異在 Data team 實質上隸屬 Engineering 溝通圈，以及 Sales 已自然分成兩個次文化群。
2. **Q1 重整建議**：可考慮正式將 Data team 納入 Engineering 匯報線，或至少設置共同 PM；Sales 分組管理制度化。
3. **C6 橋接者需要保護**：這 6 人是組織的溝通樞紐，任何一人離職都會大幅降低跨部門資訊流通。
4. **限制**：本分析基於 Slack 訊息頻率，**不**代表工作品質或信任度，解讀社群意義需搭配 1:1 訪談確認。
