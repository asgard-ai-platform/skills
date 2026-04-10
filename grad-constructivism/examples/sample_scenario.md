# Example: Onboarding Junior Data Analysts at FinSight Analytics

## Scenario

FinSight Analytics (台北，50人規模的金融數據新創) 的 L&D 負責人 Maya Chen 面臨以下問題：

> 我們每季招募 4–6 位應屆畢業生擔任 Junior Data Analyst。他們都有統計背景，但第一個月常常卡在「知道公式、不知道怎麼用在真實 case」的困境。我們現在的做法是讓他們讀內部 wiki + 跟著 senior 看 dashboard，但 3 個月後獨立產出報告的品質參差不齊。請幫我重新設計這段 onboarding。

**目前做法的問題：**
- Wiki 閱讀 = 被動接收，無法建構應用知識
- 看 dashboard = 無任何 ZPD 介入，junior 只能模仿表面形式
- 沒有評估 prior knowledge 就一視同仁餵相同內容

---

## Analysis

### Step 1: Assess Prior Knowledge

Junior 的入職背景差異顯著：

| 背景類型 | 比例 | 已知 | 缺口 |
|---------|------|------|------|
| 統計/數學系 | ~50% | 假設檢定、迴歸概念 | 業務邏輯、SQL、stakeholder 溝通 |
| 資管/財金系 | ~30% | 基本 Excel 分析、財務知識 | 統計嚴謹性、Python/SQL |
| 資工系 | ~20% | 程式能力強 | 金融領域知識、解讀業務問題 |

**Prior knowledge 陷阱**：統計系學生熟悉 p-value，但在 FinSight 的 context 中，他們的 schema 是「顯著 = 重要」— 這是常見誤解。新構知識若建立在此錯誤 schema 上，會強化「統計顯著 = 業務顯著」的錯誤信念，必須在第一週直接打破。

### Step 2: Design Authentic Tasks

原本的 wiki + dashboard 任務是**脫離脈絡的知識傳遞**。重新設計為三個真實情境任務，以 FinSight 實際業務場景為骨架：

1. **Task A（第 1–2 週）**：分析一筆已知答案的客戶流失數據集（去識別化真實數據），找出哪些特徵與流失相關，並向「模擬 PM」口頭報告發現。
2. **Task B（第 3–4 週）**：接手一份 Senior 寫到一半的 SQL query + 分析草稿，找出邏輯缺口，補完並撰寫 executive summary。
3. **Task C（第 5–8 週）**：獨立接一個 mini-project（由 Senior 預先範疇化的小型 client request），從問題定義到交付報告全程負責。

每個任務都是 FinSight 真實工作的縮小版，失敗成本低但情境成本高 — 符合 situated learning 要求。

### Step 3: Scaffold the ZPD

針對每個 background 類型，ZPD 起點不同，但 scaffolding 結構相同：

**Task A — High Support（模型→教練）**
- Senior 示範一個完整的 analysis workflow（思考大聲說出來，verbalized reasoning）
- Junior 用相同數據重跑，Senior 在旁提示但不給答案
- 每日 10 分鐘 check-in：「你現在卡在哪？你的假設是什麼？」

**Task B — Medium Support（教練→提示）**
- Junior 收到不完整的 artifact，必須自己診斷缺口
- Senior 每週 1 次 code review（只問問題，不直接改）
- Peer pair（兩位 junior 互看對方的 SQL，互提問題）

**Task C — Low Support（提示→淡出）**
- Junior 自主排程，Senior 只在 junior 主動求助時介入
- Fading 機制：第 5 週可問任何問題；第 6 週只能問「我已試過 X 和 Y，還有什麼方向？」；第 7–8 週 Senior 扮演 client，不再給技術提示

**ZPD 監控指標**：若 junior 在 Task A 超過 2 小時無進展，立即升級支援（frustration zone 警訊）；若 junior 不需任何提示完成 Task A，直接跳至 Task B 第二週（boredom zone 警訊）。

### Step 4: Enable Social Construction

加入兩個社交建構結構：

- **Weekly Sense-Making Circle（每週五 30 分鐘）**：全體 junior 輪流分享本週「我原本以為 X，但實際上是 Y」— 強制語言化 schema 衝突，讓個別認知衝突轉為集體協商
- **Cross-background Pairing**：統計系 + 資工系配對（互補先備知識），財金系 + 統計系配對（商業 vs. 嚴謹性張力）

---

## Result

```markdown
# Constructivist Learning Design: FinSight Junior DA Onboarding (8-Week)

## Learner Analysis
- Prior knowledge: 統計/程式/財金背景各異；共同缺口為業務情境判斷與 stakeholder 溝通
- Developmental level: 可在指導下執行單步分析，無法獨立完成端到端 analytical workflow
- ZPD target: 在低強度提示下，獨立定義問題、執行分析、交付 executive-level 報告

## Learning Environment
- Authentic task: 去識別化真實客戶數據 + 真實 client request（mini-project）
- Social interaction: Cross-background peer pairing + Weekly Sense-Making Circle
- Multiple perspectives: PM 視角（Task A oral report）、Senior 視角（Task B code review）、Client 視角（Task C 角色扮演）

## Scaffolding Plan
| Phase | Support Level | Activities | Fading Strategy |
|-------|-------------|------------|-----------------|
| Week 1–2 | High | Senior 示範 + 每日 10-min check-in + junior 重跑相同數據 | Senior 從「示範」轉「只問問題」 |
| Week 3–4 | Medium | 接手不完整 artifact + peer code review + 每週 1 次 senior Q&A | Senior 從「每週」改「每兩週」介入 |
| Week 5–8 | Low | 獨立 mini-project；第 7–8 週 senior 扮演 client，不給技術提示 | Junior 主動求助才介入；介入只問方向不給答案 |

## Assessment
- Process assessment: Weekly Sense-Making Circle 記錄（schema 衝突次數、解決品質）；Senior 在 code review 中追蹤「問問題品質」進步曲線
- Authentic assessment: Task C 最終報告由真實 PM 評分（不知道是 onboarding 作業），標準與正式 client deliverable 相同
```

**預期改善**：原本 3 個月後品質參差不齊的根本原因是「沒有 ZPD 介入 + 沒有 schema 衝突機會」。此設計的核心改變：
1. 每個 junior 的 scaffolding 強度根據 ZPD 動態調整（非一視同仁）
2. 錯誤的 prior knowledge（如「統計顯著 = 業務顯著」）在 Task A oral report 中被 PM 角色直接挑戰，強制重構
3. 第 8 週結束時的獨立交付，本身就是 fading 完成的驗證
