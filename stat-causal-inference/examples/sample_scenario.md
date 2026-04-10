以下是 `stat-causal-inference/examples/sample_scenario.md` 的內容：

```markdown
# Example: 電商平台免運費門檻調整對訂單金額的因果效應

## Scenario

**公司**：ShopStream（台灣中型電商平台，月活躍用戶約 80 萬）

**情境**：2025 年 10 月 1 日，ShopStream 將免運費門檻從 NT$499 調降至 NT$299，僅對「北部區域」用戶（台北、新北、基隆、桃園）執行，南部與中部維持 NT$499。行銷分析師 Amber 拿著報告說：

> 「政策上線後第 4 週，北部用戶平均客單價從 NT$612 提升到 NT$748，漲了 NT$136（+22%）。這是因為我們的政策嗎？」

資料：
- 北部用戶（treated）：2025 年 9 月（pre）、10 月（post）各 4 週，約 42,000 筆訂單
- 南中部用戶（control）：相同時間窗，約 61,000 筆訂單
- 南中部同期客單價：pre NT$598 → post NT$631（+NT$33）

---

## Analysis

### Step 1：定義因果問題

- **Treatment**：免運費門檻從 NT$499 → NT$299
- **Outcome**：平均訂單金額（AOV, Average Order Value）
- **Counterfactual**：「如果北部用戶的門檻沒有調降，他們的 AOV 在 10 月會是多少？」

北部 AOV 漲了 NT$136，但這不能直接歸因政策。原因可能包含：
- 10 月雙十連假帶動整體消費
- 北部用戶的購物季節性本來就高於南部
- 其他同期行銷活動

### Step 2：識別威脅

| 威脅來源 | 說明 |
|---------|------|
| 季節性（Seasonality） | 雙十連假在全台影響相似，但北部消費力可能彈性更大 |
| 組合差異（Composition） | 北部與南部用戶的產品偏好、所得水準不同 |
| 其他行銷干擾 | 同期是否有北部限定的行銷活動？（Amber 確認：無） |
| 均值回歸 | 北部是否在政策前異常低？（查看 8 月數據後確認正常） |

### Step 3：選擇方法 — Difference-in-Differences（DID）

**理由**：
- 政策在特定地理群體推行，產生自然的 treated / control 分組
- 有政策前（pre）與政策後（post）的時間序列
- 適合 DID

**關鍵假設**：Parallel Trends（平行趨勢）  
若沒有政策介入，北部與南中部 AOV 應以相似速率變化。

**平行趨勢預測試（Pre-treatment check）**：

| 週次 | 北部 AOV | 南中部 AOV | 差距（北 - 南中） |
|------|---------|-----------|----------------|
| 8月第1週 | NT$598 | NT$581 | +NT$17 |
| 8月第2週 | NT$603 | NT$585 | +NT$18 |
| 8月第3週 | NT$601 | NT$583 | +NT$18 |
| 8月第4週 | NT$608 | NT$590 | +NT$18 |
| 9月第1週（pre） | NT$611 | NT$594 | +NT$17 |
| 9月第4週（pre） | NT$614 | NT$601 | +NT$13 |

→ 前 6 週差距穩定在 NT$13–18，趨勢大致平行，平行趨勢假設**初步成立**。

### Step 4：DID 估計

$$\text{DID} = (Y_{\text{北部,post}} - Y_{\text{北部,pre}}) - (Y_{\text{南中部,post}} - Y_{\text{南中部,pre}})$$

代入數字：

$$\text{DID} = (748 - 612) - (631 - 598) = 136 - 33 = \mathbf{NT\$103}$$

**解讀**：排除時間共同趨勢後，政策使北部用戶的平均訂單金額提升約 **NT$103**（+16.8%）。

### Step 5：統計顯著性（迴歸形式）

對訂單層級資料（每筆訂單為一個觀察值）跑以下迴歸：

```
AOV_i = β0 + β1·Post_t + β2·Treated_g + β3·(Post_t × Treated_g) + ε_i
```

| 係數 | 估計值 | 標準誤 | 95% CI |
|------|--------|--------|--------|
| β0（intercept） | 598 | — | — |
| β1（Post） | 33 | 4.1 | [25, 41] |
| β2（Treated） | 14 | 5.3 | [4, 24] |
| **β3（DID 因果效應）** | **103** | **6.8** | **[90, 117]** |

p-value < 0.001，效應顯著。

### Step 6：穩健性檢查

1. **安慰劑測試（Placebo test）**：把「政策日期」偽造為 2025 年 8 月 1 日（無政策），重跑 DID → DID 估計 = NT$2，p = 0.71。✅ 無虛假效應。
2. **排除雙十連假週**（10 月第 2 週）：DID = NT$97，與主估計差異在 CI 內。✅ 穩健。
3. **不同控制群**：僅用中部（排除南部）重跑 → DID = NT$99。✅ 穩健。

---

## Result

```markdown
# Causal Analysis: 免運費門檻調降（NT$499→NT$299）→ 訂單金額（AOV）

## Causal Question
- Treatment: 北部區域免運費門檻從 NT$499 調降至 NT$299（2025-10-01）
- Outcome: 平均訂單金額（AOV）
- Counterfactual: 若門檻未調降，北部 10 月 AOV 預估維持在 NT$645 左右（= NT$612 + 南中部的同期漲幅 NT$33）

## Identification Strategy
- Method: Difference-in-Differences（DID）
- Rationale: 政策在北部地理分組推行，南中部為自然控制組；有清楚的 pre/post 時間切點
- Key assumption: Parallel Trends — 若無政策，北部與南中部 AOV 會以相似速率變動
- Assumption test: Pre-treatment 6 週趨勢差距穩定（NT$13–18），視覺與統計上支持平行趨勢；安慰劑測試 DID ≈ 0，通過

## Results
- Estimated causal effect: **+NT$103**（95% CI: [90, 117]）
- Robustness checks:
  - 排除連假週：NT$97 ✅
  - 替換控制群（僅中部）：NT$99 ✅
  - 安慰劑日期測試：NT$2，不顯著 ✅

## Limitations
1. 平行趨勢在 post 期間是假設，無法直接驗證
2. 北部與南中部用戶組合差異（所得、品類偏好）若在 10 月出現突變，DID 會高估
3. SUTVA 潛在違反：南部用戶若知道北部有優惠而延遲購買，控制組可能被污染（目前無跡象，但需監控）
4. 效應可能包含「囤貨效應」——用戶一次買更多，但購買頻率可能下降，需追蹤 30 天總消費額
```

**建議行動**：
- 政策估計可在全台推廣，預期每筆訂單貢獻 +NT$103 AOV
- 推廣前需確認毛利率：若免運費成本 > NT$103 × 毛利率，則擴大效益有限
- 追蹤 30 天用戶層級總消費（LTV 影響），避免只看單筆 AOV
```

請確認後我再把這份內容寫入 `stat-causal-inference/examples/sample_scenario.md`。
