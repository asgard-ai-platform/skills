# Example: AI 推論晶片測試製程的自製或外包決策

## Scenario

**公司**：Nexora Semiconductor（化名），台灣中型 IC 設計公司，2025 年起量產邊緣 AI 推論晶片（EdgeMind-3）。

**問題**：Nexora 目前將晶片最終測試（Final Test）外包給第三方測試廠 Alphatest。EdgeMind-3 具備自訂稀疏運算單元，需要 Nexora 工程師與 Alphatest 共同開發測試程式（test program），耗費 6 個月。Alphatest 每年僅處理 Nexora 一款產品，但客戶開始要求出貨交期縮短至 3 週（原為 8 週）。

VP of Operations 問：「我們應該買設備自建測試線，還是繼續外包 Alphatest？如果外包，合約條款要怎麼談？」

---

## Analysis

### Step 1：評估資產專屬性（Asset Specificity）— 主要判斷變數

**人力資產專屬性（Human asset specificity）— 高**
EdgeMind-3 的稀疏運算測試向量由 Nexora 內部架構師設計，Alphatest 需指派 2 名工程師接受 6 個月培訓才能操作。這批知識離開 Nexora 脈絡即失去大部分價值。

**實體資產專屬性（Physical asset specificity）— 中高**
EdgeMind-3 要求 ATE（Automated Test Equipment）搭載客製化 load board 及特殊探針卡，單套 NRE 成本約 NT$800 萬，且規格由 Nexora 獨家設計。Alphatest 若失去 Nexora 訂單，設備利用率驟降。

**時間專屬性（Temporal specificity）— 高**
客戶要求交期 3 週，測試產能在出貨窗口外無法替代；若 Alphatest 排程衝突或設備故障，違約成本直接由 Nexora 承擔。

**綜合評估：資產專屬性 → 高（偏向 hierarchy 信號）**

---

### Step 2：評估不確定性（Uncertainty）

**技術不確定性 — 高**
EdgeMind-3 每 12–18 個月改版一次（die shrink + 新稀疏演算法），每次改版均需重寫測試程式。合約難以事先規定 2 年後的測試規格與費率。

**行為不確定性（opportunism 風險）— 中高**
Alphatest 掌握 Nexora 的測試 know-how 後，可能對競爭對手晶片廠提供類似服務，或在議價時利用轉換成本（switching cost）要求漲價。2024 年已出現一次費率談判破裂，最終 Nexora 妥協漲價 18%。

**市場不確定性 — 中**
AI 晶片市場需求波動大，季度出貨量差異可達 ±40%，使固定產能規劃困難。

**綜合評估：不確定性 → 高**

---

### Step 3：評估交易頻率（Frequency）

EdgeMind-3 每季出貨，每月進行 2–3 批測試排程調整；改版週期 18 個月內需重談測試條件。此為**高頻、持續性交易**，治理成本可分攤於多次交易上，支持建立更正式治理結構。

**綜合評估：頻率 → 高**

---

### Step 4：治理結構對應

| 維度 | 評估 | 信號 |
|------|------|------|
| 資產專屬性 | 高（人力 + 實體 + 時間） | → Hierarchy |
| 不確定性 | 高（技術 + 行為） | → Hierarchy |
| 頻率 | 高 | → 正式治理值得投資 |

**純 TCE 預測：Hierarchy（自建測試線）**

然而，Nexora 目前年營收 NT$12 億，自建完整 Final Test 產線（ATE × 4 台 + 廠房）初始資本支出約 NT$3.5 億，佔年營收 29%，財務約束明顯。此為**邊界條件**：TCE 指向 hierarchy，但資本限制使純 hierarchy 短期不可行。

**修正建議：Hybrid（混合治理）搭配明確防護機制**

---

### Step 5：設計 Hybrid 防護機制（Safeguards）

因資產專屬性與不確定性皆高，hybrid 合約必須內建以下保護：

1. **Dedicated capacity clause（專屬產能條款）**：合約明定 Alphatest 保留 Nexora 專用機台 2 台，不得對外開放排程，Nexora 支付月保留費 NT$80 萬作為「押金」（hostage）。

2. **IP 隔離條款**：Nexora 所有測試程式、load board 設計文件列為 Nexora 財產，Alphatest 工程師簽署保密協議，並禁止承接 EdgeMind 直接競品（定義明確，排除同類稀疏運算架構晶片）。

3. **費率鎖定 + 通膨調整公式**：基礎費率鎖定 2 年，調整幅度以 CPI + 設備折舊指數為上限，消除行為不確定性中的議價風險。

4. **轉換路徑保留（partial insourcing option）**：Nexora 採購 1 台 ATE 作為工程驗證站，培養內部測試工程師 3 名。若 Alphatest 再次違反 SLA 超過 2 次／年，可在 6 個月內轉為 70% 自測。

5. **SLA + 懲罰條款**：交期逾 3 週觸發每日 0.5% 訂單金額罰款，上限 10%。

---

## Result

```markdown
## TCE Governance Analysis: Nexora EdgeMind-3 Final Test

### Transaction Profile
| Dimension | Assessment | Evidence |
|-----------|-----------|----------|
| Asset Specificity | 高 — 人力（6 個月培訓）+ 實體（NRE NT$800 萬客製 load board）+ 時間（3 週交期窗口） | 測試程式開發史、設備規格書 |
| Uncertainty | 高 — 技術（18 個月改版週期）+ 行為（2024 費率談判破裂、競品洩漏風險） | 產品藍圖、合約談判記錄 |
| Frequency | 高 — 每月多批次排程，每季出貨 | 生產排程資料 |

### Governance Recommendation
- **建議結構**：Hybrid（長期專屬合約 + 部分自建能力）
- **理由**：純 hierarchy 為 TCE 最適解，但 NT$3.5 億資本支出佔年營收 29%，財務限制使其不可行；純 market 因資產專屬性高，將導致 Alphatest 套牢（hold-up）風險。Hybrid 以合約防護機制複製 hierarchy 的保護效果。
- **必要防護措施**：
  1. 專屬產能條款（月保留費 NT$80 萬）
  2. IP 隔離 + 競品禁止條款
  3. 費率鎖定 2 年（CPI 連動上限）
  4. 內部 ATE × 1 台 + 工程師 3 名（partial insourcing option）
  5. SLA 罰款 0.5%／天

### Risk of Misalignment
- **現況治理**：Hybrid（但無防護機制，接近純 market）
- **可預期的無效率**：
  - 套牢風險：Alphatest 已利用轉換成本漲價 18%，下次改版談判將重演
  - 時間專屬性未被保護：排程衝突直接導致客戶交期違約
  - IP 外洩路徑未封閉：測試 know-how 可能流向競品
- **矯正路徑**：簽訂上述 hybrid 合約；若 18 個月內 SLA 違反 ≥ 2 次，啟動自建評估（屆時累積內部能力後 capex 門檻降低）
```
