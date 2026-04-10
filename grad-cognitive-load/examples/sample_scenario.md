# Example: SaaS Onboarding Tutorial Overhaul at Finlink

## Scenario

Finlink 是一家 B2B 財務整合 SaaS，產品連接 ERP、銀行 API 與會計系統。產品經理 Priya 帶著以下問題來：

> 「我們新用戶的 Day-7 啟用率只有 23%，但產品本身並不複雜。用戶支援票的頭號問題是：『我看了文件還是不知道怎麼設定第一個 Integration』。我們的 onboarding 文件有圖、有影片、有步驟清單，感覺已經很豐富了，為什麼還是沒用？」

Priya 分享了現有 onboarding flow 的結構：

- **第 1 頁**：介紹頁，含 3 分鐘的產品概覽影片（旁白 + 同步字幕）
- **第 2 頁**：12 步驟的設定清單，每步驟附截圖，截圖說明文字放在頁面右側欄
- **第 3 頁**：API key 生成教學，說明文字與對應欄位截圖分開放（說明在上，截圖在下）
- **第 4 頁**：「進階設定」（webhook、retry policy、rate limit），與基礎設定合併在同一頁
- **第 5 頁**：常見錯誤排查，含 8 個錯誤碼說明，每個附 3–5 個可能原因

目標用戶：財務部門行政人員，有 ERP 操作經驗，**無** API 或整合開發背景。

---

## Analysis

### Step 1 — 分析元素互動性（Intrinsic Load）

Finlink 第一個 Integration 設定的核心任務包含以下必須**同時理解**的元素：

| 元素 | 說明 |
|------|------|
| API key 的用途 | 為什麼需要、存在哪裡 |
| 來源系統（ERP）的憑證 | 如何取得、對應哪個欄位 |
| 目標系統（銀行/會計）的憑證 | 同上 |
| Integration 類型選擇 | 實時 vs 批次 vs webhook |
| 欄位對映邏輯 | 來源欄位 → 目標欄位的語意對應 |

這 5 組元素彼此相依（例如：沒理解 API key 用途，就無法正確填入憑證欄位），屬於**高元素互動性**，intrinsic load 本身就偏高。

**結論**：Intrinsic load = High；設計不應再增加任何不必要負擔，且需要 worked example 來降低新手負荷。

---

### Step 2 — 外在認知負荷稽核

| 來源 | 是否存在 | 嚴重度 | 說明 |
|------|----------|--------|------|
| 分割注意力（split-attention） | **是** | **High** | 第 2、3 頁：截圖與說明文字空間分離，用戶需在畫面間跳視整合 |
| 冗餘（redundancy） | **是** | High | 第 1 頁：旁白與同步字幕傳達完全相同內容，佔用雙通道但無互補效益 |
| 瞬逝資訊（transient info） | **是** | Med | 3 分鐘影片無暫停點，資訊消失後無法回溯細節 |
| 專業逆轉（expertise reversal） | **否** | — | 目標受眾為新手，逐步引導合適 |
| 誘人細節（seductive details） | **是** | High | 第 4 頁：webhook/retry policy 對完成第一個 Integration 毫無必要，卻與基礎設定同頁呈現 |
| 過早負荷（premature interactivity） | **是** | High | 第 5 頁的 8 個錯誤碼在用戶尚未完成設定前就出現，形成無法錨定的抽象清單 |

**最大問題**：第 2、3 頁的分割注意力效應 + 第 4 頁的誘人細節，預計消耗 WM 容量的主要部分。

---

### Step 3 — 負荷預算估算

```
Intrinsic load:   High (5 個高互動元素，新手無既有 schema)
Extraneous load:  High (split-attention × 2 頁 + redundancy + seductive details)
Germane load:     幾乎為零（無 worked example、無自我解釋機制）
────────────────────────────────────────
估算總負荷:       超出 WM 容量
可削減空間:       Extraneous 高（設計缺陷，可控）
```

這解釋了為何「圖文俱全」仍然無效：外在負荷耗盡 WM，根本沒有剩餘容量進行 schema 建構。

---

### Step 4 — 重新設計建議

**A. 消除分割注意力（最高優先）**
- 第 2、3 頁：將說明文字直接標注在截圖上（callout 標籤），不要放在側欄或段落上方
- 對 API key 欄位：在截圖內以紅框圈出並附內嵌文字，而非另起一段描述

**B. 去除冗餘通道**
- 第 1 頁影片：旁白 + 字幕二選一；建議保留旁白，移除重複字幕，改以**關鍵詞標題卡**強調重點（互補而非重複）

**C. 分割（Segmenting）並設立學習關卡**

重新分頁：

| 新頁 | 內容 | 對應負荷策略 |
|------|------|-------------|
| 頁 1 | Worked example：用 Acme Corp 示範完整設定一個 Integration（只用預設值） | 降低 intrinsic load |
| 頁 2 | 用戶自己操作：跟著 guided checklist 完成第一個 Integration（重複相同結構） | Fading + schema transfer |
| 頁 3 | 進階設定（webhook/retry policy）— **僅在完成頁 2 後解鎖** | 消除 seductive details |
| 頁 4 | 錯誤排查 — 僅顯示與用戶當前設定相關的 2–3 個錯誤碼 | 情境化，降低 extraneous |

**D. 增加 Germane Load 設計**
- 每個步驟完成後加入一句「為什麼這樣做？」的摺疊說明，鼓勵自我解釋
- 在 worked example 與用戶實作間加入一個問題：「Acme 用的是哪種 Integration 類型？你的案例應該選哪種？為什麼？」

---

## Result

```markdown
## Cognitive Load Analysis: Finlink Onboarding Tutorial

### Intrinsic Load Assessment
- Element interactivity: High
- Key interacting elements: API key 用途、來源系統憑證、目標系統憑證、Integration 類型選擇、欄位對映邏輯（5 組相依元素）
- Learner expertise level: Novice（有 ERP 操作背景，無 API 整合經驗）

### Extraneous Load Audit
| Source | Present? | Severity | Fix |
|--------|----------|----------|-----|
| Split-attention | Yes | High | 說明文字改為截圖內嵌 callout 標籤 |
| Redundancy | Yes | High | 影片字幕移除，改為關鍵詞標題卡 |
| Transient info | Yes | Med | 影片加入章節標記，可跳轉回放 |
| Seductive details | Yes | High | 進階設定移至獨立頁，完成基礎設定後解鎖 |
| Expertise reversal | No | — | 不適用（受眾為新手） |

### Load Budget
- 估算總負荷: Exceeding capacity（extraneous 為主因）
- Extraneous 削減潛力: High（全為設計缺陷，可完全修正）

### Redesign Recommendations
1. **最高優先**：第 2、3 頁截圖改為內嵌 callout，消除分割注意力；預計可釋放最大 WM 容量
2. **分頁策略**：加入 Acme Corp worked example 作為頁 1，原 12 步驟清單改為 fading 練習（頁 2）；進階設定與錯誤排查分離至後續頁面並設解鎖條件
3. **Germane load 啟動**：在 worked example 與實作間插入結構比較問題，促進 schema 遷移而非單純步驟模仿
```

**預期效果**：以 Sweller 研究中 split-attention 修正的平均效果量（d ≈ 0.6–0.9）推估，光是消除分割注意力即可顯著提升首次設定完成率；加上 worked example + fading，Day-7 啟用率目標合理設在 40–50%（需 A/B 測試驗證）。
