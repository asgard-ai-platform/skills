# Example: 併購後工程師文化衝突 — TechNova 收購 ByteForge

## Scenario

TechNova（上市 SaaS 公司，600 人）於 2025 年 Q3 完成對 ByteForge（B2B 開發工具新創，80 人）的收購。六個月後，HR VP 向你描述以下症狀：

- ByteForge 工程師在 Slack 頻道仍自稱「BF team」，拒絕使用 TechNova 的統一 on-call rotation
- TechNova 工程師公開評論 ByteForge 的程式碼「太 hacky、不符合我們的 engineering standards」
- 兩組在跨組 sprint planning 中，習慣性地將 bug 歸咎給對方
- ByteForge 資深工程師流失率飆至 35%（業界平均約 12%）
- 兩組雖然坐在同一辦公室，午餐卻自動分桌，幾乎零跨組社交

HR VP 問：「這是薪酬問題嗎？還是管理風格不合？我們需要更多 team building 活動嗎？」

---

## Analysis

### Step 1 — 識別顯著社會類別

| 社會類別 | 顯著觸發因素 | 類別類型 |
|---------|------------|---------|
| TechNova 工程師 | 收購方身份、制度權威（HR 政策、on-call 系統）、人數優勢（600 vs 80） | 主類別（superordinate 嘗試失敗） |
| ByteForge 工程師 | 被收購方身份、「BF team」自稱、共同創業記憶、Slack 頻道行為 | 主類別（抵抗被吸收） |

**類別結構判斷**：這是「嵌套但衝突」情境——TechNova 試圖以「大家都是 TechNova 人」做 recategorization，但 ByteForge 群體拒絕接受，維持對立的 subgroup identity。類別邊界由制度差異（code style guidelines、on-call 規範）持續強化，而非僅靠心理認知。

顯著觸發因素清單：
- **可見標記**：Slack 頻道名稱、午餐分桌座位
- **脈絡線索**：sprint planning 中的 bug 歸咎語言
- **近期事件**：收購本身重新啟動了身份威脅

---

### Step 2 — 評估認同強度

**ByteForge 工程師**

| 維度 | 指標 | 強度 |
|------|------|------|
| 認知 | 持續使用「BF team」；說「我們的架構」 | High |
| 評價 | 認為自己的 move-fast 文化優於 TechNova 的官僚流程 | High |
| 情緒 | 創辦情感（早期員工、共同熬夜的記憶）；被「吞掉」的委屈 | Very High |
| 行為 | 拒絕採用統一 on-call；非正式午餐自動分桌 | High |

**TechNova 工程師**

| 維度 | 指標 | 強度 |
|------|------|------|
| 認知 | 「我們的 engineering standards」語言 | Medium-High |
| 評價 | 以成熟流程、規模感為傲 | Medium |
| 情緒 | 輕微優越感；對 ByteForge「破壞品質」的防衛焦慮 | Medium |
| 行為 | 公開批評程式碼品質；避免跨組社交 | Medium |

---

### Step 3 — 分析群際比較

**比較維度**：技術能力（competence）與工作文化（morality/values）

| 比較軸 | TechNova 的框架 | ByteForge 的框架 |
|-------|--------------|---------------|
| 技術品質 | 「我們有 standards，他們是 hacky」 | 「我們 ship fast，他們是官僚」 |
| 文化價值 | 「規模化需要紀律」 | 「新創精神被扼殺」 |
| 地位 | 收購方 = 更成功 | 被選中收購 = 技術被肯定，但自主權被剝奪 |

**ByteForge 的身份管理策略**：
- ~~社會流動（Social Mobility）~~：部分資深工程師正在執行此策略（→ 35% 流失率）
- **社會創造（Social Creativity）**：重新定義比較維度——「我們不是品質差，我們是敏捷」
- 部分萌芽中的**社會競爭（Social Competition）**：在 sprint planning 中公開歸咎 bug 給 TechNova

**威脅類型**：
- **獨特性威脅（Distinctiveness Threat）**：TechNova 強制統一工具和流程，直接消除 ByteForge 群體的可辨識性
- **地位威脅（Status Threat）**：「hacky code」評語公開否定 ByteForge 的核心能力認同
- 尚無明顯**價值威脅**，但若 TechNova 強制推行文化政策，可能升級

**關鍵診斷**：HR VP 的假設（薪酬問題、team building 不足）錯誤定位問題層次。這是群體身份威脅，team building 活動在高身份威脅情境下通常無效，甚至會因強制接觸而加劇衝突。

---

### Step 4 — 設計干預

ByteForge 群體需要**可辨識的存在感**，TechNova 需要**品質標準的完整性**，干預必須同時滿足兩者。

推薦策略組合：**Mutual Differentiation**（主）+ 局部 **Recategorization**（副）

- **避免的策略**：直接 decategorization（「忘掉 ByteForge，大家都是 TechNova」）——在高情緒認同情境下會觸發強烈反彈，加速人才流失
- **避免的策略**：純粹 team building 活動——在 equal status 條件尚未建立前的強制接觸，依據接觸假說，效果為負

---

## Result

## Social Identity Analysis: TechNova × ByteForge 後合併衝突

### Group Map
| Group | Salience Trigger | Identification Strength |
|-------|-----------------|------------------------|
| ByteForge 工程師 | 收購身份威脅、「BF team」Slack 自稱、共同創業情感 | High |
| TechNova 工程師 | 制度權威（標準、流程）、人數與地位優勢 | Medium |

### Intergroup Dynamics
- Comparison dimension: 技術能力（competence）、工作文化價值（values/morality）
- Perceived status: TechNova = 制度權威；ByteForge = 技術被低估但情感凝聚高
- Identity management strategy: ByteForge 執行 social creativity + social mobility（流失）；TechNova 維持地位優越框架
- Threat level: **高度獨特性威脅 + 中度地位威脅**（對 ByteForge）

### Behavioral Manifestations
- In-group favoritism：ByteForge 工程師互相保護、拒絕外部 on-call 義務；TechNova 工程師優先聽從本組技術判斷
- Out-group discrimination：跨組 bug 歸咎、公開批評程式碼品質、午餐社交分桌、35% 流失率（高身份認同者選擇離開而非融入）

### Intervention Recommendations

1. **制度性 Mutual Differentiation（立即，第 1–2 個月）**
   - 正式命名「ByteForge Platform Team」作為 TechNova 內部的具名子單位，而非「前 ByteForge」
   - 允許該團隊保留部分技術決策自主權（例如：自選內部工具鏈，只要對外 API 合規）
   - 目標：降低獨特性威脅，讓群體有合法的可辨識身份

2. **接觸假說條件建立（第 2–4 個月）**
   - 設計**共同目標**任務小組（跨組客戶事故 postmortem、新功能聯合 launch），而非社交 happy hour
   - 確保任務小組中 ByteForge 工程師**在技術判斷上有對等發言權**（equal status 條件）
   - 配備管理層公開背書（institutional support 條件）
   - 避免：不要先辦烤肉或 escape room，這些不符合接觸假說的有效條件

3. **Superordinate 身份建構（第 3–6 個月，待信任基礎建立後）**
   - 以**共同敵人或共同挑戰**建立 superordinate identity，例如「共同對抗 Competitor X」或「共同打贏 Enterprise 市場」
   - 避免以 TechNova 品牌本身作為 superordinate category——ByteForge 工程師視之為收購方，無法中立認同
   - 監測指標：「我們」語言是否開始跨越原始群體邊界

**對 HR VP 的直接回覆**：這不是薪酬或 team building 問題。根本機制是群體身份威脅——被收購方失去獨特性，正在用流失（social mobility）和抵抗（social creativity）回應。每一個強制統一的政策動作，都在加深這條裂縫。優先動作是給 ByteForge 群體制度性的可辨識空間，然後在 equal status 條件下創造有實質目標的跨組合作，而非社交活動。
