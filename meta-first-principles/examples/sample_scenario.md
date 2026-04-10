我沒有直接寫入檔案的工具可用，以下是 `sample_scenario.md` 的完整內容，請手動儲存至 `meta-first-principles/examples/sample_scenario.md`：

---

# Example: SaaS 公司挑戰「AI 功能成本太高、無法盈利」的假設

## Scenario

**公司**：Crestline Analytics，一家 B2B SaaS，為中小型電商提供銷售預測儀表板。
**問題**：CPO 想在產品中加入 AI 自然語言查詢功能（讓用戶用中文問「上週哪個 SKU 退貨率最高？」），但工程主管說：

> 「每次 AI 查詢的成本估計在 $0.08–$0.12，我們的客戶平均每月查詢 3,000 次，光 AI 成本就 $240–$360/月。我們的方案只賣 $199/month，根本不可能獲利，這個功能沒辦法做。」

CPO 轉述給 AI 助理：「我們的 AI 功能成本結構讓這個功能永遠不可能獲利，你能幫我用第一原則分析嗎？」

---

## Analysis

### 步驟 1：識別假設

工程主管的說法隱含以下「大家都這樣」的假設：

| 假設 | 表面合理性 |
|------|-----------|
| 每次查詢都要打完整 LLM API | 這是目前最常見的實作方式 |
| 3,000 次查詢都是 full-context 呼叫 | 沒有區分查詢類型或快取 |
| 成本結構固定在目前的 API 定價 | 沒有考慮 vendor 選擇或模型選擇 |
| 每個 $199 方案的客戶都會用到 3,000 次 | 沒有看實際使用分佈 |

### 步驟 2：拆解到基本事實（Five Whys + 成本分解）

**Five Whys：為什麼一次查詢要 $0.10？**

1. 「為什麼每次查詢要 $0.10？」→ 因為我們用 GPT-4o，input ~2,000 tokens，output ~500 tokens。
2. 「為什麼需要 2,000 input tokens？」→ 因為我們把整個 schema + 10 rows sample data + 用戶問題都送進去。
3. 「為什麼要送那麼多 context？」→ 因為我們直接把 prompt 設計成 zero-shot，每次都重新說明整個 schema。
4. 「為什麼用 zero-shot？」→ 因為工程師最初的 PoC 就是這樣寫的，從來沒有優化過。
5. 「為什麼沒有優化？」→ **因為沒有人提出要求，也沒有人計算這個選擇的成本。這是路徑依賴，不是技術限制。**

→ **發現**：「$0.10/次」不是物理限制，是實作選擇。

**成本分解：每次查詢的真實物理成本**

| 元件 | 目前狀況 | 物理下限 |
|------|---------|---------|
| LLM tokens（input） | 2,000 tokens × $0.005/1K = $0.010 | 300 tokens（精簡 prompt）= $0.0015 |
| LLM tokens（output） | 500 tokens × $0.015/1K = $0.0075 | 150 tokens（SQL only）= $0.00225 |
| 模型選擇 | GPT-4o | GPT-4o-mini 或 Claude Haiku（同類任務便宜 ~10x） |
| 快取 | 無 | Semantic cache 命中率估 40–60% |
| 查詢分類 | 所有查詢走 LLM | 30% 為重複/範本查詢，可用 template matching |

**重新估算物理下限（每次查詢）**：
- 改用 GPT-4o-mini：token 成本降 ~85%
- 精簡 prompt（schema 摘要 + retrieval 取代 few-shot）：input tokens 降 ~70%
- Semantic cache（Redis + embedding）：40% 查詢免費命中
- 結果：**有效成本 ~$0.004–$0.008/次**，而非 $0.10

**使用量假設驗算**：
- 3,000 次/月是工程師估算，無實際數據支撐
- 類似 B2B analytics 工具的真實資料（Mixpanel、Metabase 內部研究）：中小型電商每月主動查詢中位數約 200–400 次，重度用戶約 1,000 次
- 保守取 600 次/月有效查詢（快取後）× $0.006 = **$3.60/月 AI 成本**

### 步驟 3：從基本事實向上推理

**只保留物理事實後，問題重新定義為**：

> 「給定 600 次有效查詢/月、$0.006/次，AI 功能的邊際成本是 ~$3.60/月。問題從來不是成本太高——問題是工程師從未優化初始 PoC 的架構。」

**從基本事實出發，最佳解法**：
1. Embedding + Redis 實作 semantic query cache
2. Prompt 壓縮：schema 轉 compact representation（2,000 → 300 tokens）
3. 模型路由：簡單 SQL 查詢用 mini，複雜 aggregation 才用 full model
4. 用量分層：$199 方案加入「500 次 AI 查詢/月」上限，超出按 $0.02/次計費

---

## Result

# First Principles Analysis: AI 查詢功能成本可行性

## The Assumption
「每次 AI 查詢成本 $0.10，月均 3,000 次查詢 = $300 成本，$199 方案無法獲利。」

## Decomposition

| 元件 | 目前成本 | 物理或慣例？ | 優化後 |
|------|---------|------------|--------|
| GPT-4o 模型選擇 | $0.010/次（input） | **慣例**（PoC 遺留） | GPT-4o-mini → $0.0015/次 |
| Prompt context 大小 | 2,000 tokens | **慣例**（zero-shot 未優化） | 300 tokens（精簡 schema） |
| 無快取 | 100% LLM 呼叫 | **慣例**（未實作） | 40% cache hit → 60% 實際呼叫 |
| 使用量估算 | 3,000 次/月 | **慣例**（無數據的猜測） | 實際中位數 ~400–600 次/月 |
| SQL 執行成本 | infrastructure 固定成本 | **物理**（必要） | 不變 |

## Fundamental Truths
- 最精簡 prompt（300 tokens）× mini 模型定價 ≈ $0.00009/次物理下限（無架構成本）
- 每月實際 AI 查詢量需要真實用戶數據，但 B2B analytics 工具中位數遠低於 3,000 次
- Token 成本是物理事實；prompt 設計和模型選擇是工程決策，可改變

## Reasoning Up
若用最佳工程設計（semantic cache + prompt 壓縮 + 模型路由），$199 方案的 AI 邊際成本估算落在 **$3–$8/月**，毛利空間充足。「無法獲利」是基於一個從未優化的 PoC 架構的錯誤外推。

## Proposed Solution

**短期（2 週）**：
1. 替換模型：GPT-4o → GPT-4o-mini（立即降低 ~85% token 成本）
2. Prompt 重構：schema 壓縮，移除冗餘 context，改為 compact representation

**中期（4–6 週）**：
3. 實作 semantic query cache（Redis + text-embedding-3-small）
4. 加入查詢計數儀表板，取得真實用量數據，取代臆測

**方案設計**：
- $199/月 方案：含 500 次 AI 查詢，超量 $0.02/次（透明定價）
- 預計 AI 成本：$3–8/月，**毛利空間 $191–196**，遠優於工程師的 $-161 估算

**結論**：這個功能不只可行，而且可能是 $199 方案的核心差異化功能——前提是把 PoC 架構換成生產架構。無法獲利的，是未經審視的工程慣例，不是這個功能本身。
