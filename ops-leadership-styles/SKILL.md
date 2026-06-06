---
name: "ops-leadership-styles"
description: "Leadership-style decision framework combining transformational, transactional, servant, situational, and authentic leadership into a situation-based decision tree. Use for diagnosing leadership challenges, succession planning, change management, crisis response, taking over a new team, or generational-gap issues. Triggers: 『該用什麼領導風格』『怎麼帶這個團隊』『接班交棒』『危機領導』『年輕員工不吃這一套』『威權還是授權』『轉型領導』『僕人領導』『情境領導』『真誠領導』. For Taiwan EMBA leadership courses (台大／政大／師大), executive self-diagnosis, and succession-leadership style. 9-box/人才盤點/繼任規劃工具: use `ops-talent-strategy`."
metadata:
  category: "WP-09 商學院—管理"
  tags: ["leadership", "transformational", "transactional", "servant-leadership", "situational-leadership", "authentic-leadership", "emba"]
  audience: "台灣 EMBA 在職學員、高階經理人"
---

# 領導風格決策工具（Leadership Styles Decision Framework）

## 定位

沒有「最好的」領導風格，只有「最合當下情境」的風格。本 skill 提供五種主流領導風格的情境選用決策樹，協助 EMBA 學員：
1. 診斷個案中領導者的風格與其情境契合度
2. 自我診斷慣用風格與可能盲點
3. 產出可操作的風格切換行動清單

**與相近 Asgard skill 的邊界**：
- `grad-social-identity`、`grad-sdt`、`grad-sensemaking` — 單一學理深挖
- 本 skill — **情境選用工具箱**，不深挖單一理論

## 何時使用

**觸發條件**
- 個案中領導者面臨「要威權或授權」、「要強硬或同理」的抉擇
- 接班交棒、組織變革、危機應變、併購整合
- 跨世代團隊（Z 世代 vs. 資深員工）領導挑戰
- EMBA 領導課程個案分析作業

**不適用**
- 組織文化整體變革 → 用 `ops-org-behavior`（Schein）
- 團隊發展階段 → 用 `ops-org-behavior`（Tuckman）
- 策略層面領導（CEO 層級戰略） → 用 `grad-strat-upper-echelons`

## IRON LAW — 領導風格的三條鐵律

```
IRON LAW 1：情境決定風格，非個性決定風格
宣稱「我就是僕人式領導者」是自我設限。
成熟領導者能在 24 小時內從「危機指揮官」切換到「教練」角色。
```

```
IRON LAW 2：風格切換須顯性溝通
突然改變風格會讓部屬困惑（「老闆今天怎麼這樣」）。
切換前必須說明：為何此情境需要這個風格、持續多久、結束後回到什麼狀態。
```

```
IRON LAW 3：下屬成熟度是最重要的情境變數
同一事件，面對資深員工 vs. 新人須用不同風格。
Hersey-Blanchard 情境領導的核心不是「領導者本身」，而是「部屬準備度」。
```

## Rationalization Table — 當 Claude 想「本案例外」時，先自問

| 可能想 | 但 Iron Law 仍適用，因為 |
|---|---|
| 「主角自稱『我是僕人式領導者』，分析就以此為前提」 | 自稱 ≠ 實踐；情境測試才能判斷風格是否合宜，不能把自我標籤當結論前提 |
| 「時間緊迫，風格切換來不及顯性溝通」 | 緊迫才更要溝通；否則部屬誤判老闆人格改變，信任損耗大於效率節省 |
| 「個案沒描述部屬成熟度，就省略 Hersey-Blanchard」 | 無資料仍須標註「以下建議假設部屬準備度為 R2／R3」，並說明若實際不同應如何調整 |

## 五種領導風格對照

| 風格 | 核心主張 | 代表人物／研究 | 強項情境 | 弱項情境 |
|---|---|---|---|---|
| 轉型領導 | 願景驅動、激發認同 | Bass & Avolio | 組織變革、新創啟動 | 日常作業、例行執行 |
| 交易領導 | 獎懲明確、目標管理 | Burns、Bass | 生產線、業務團隊 | 創新、知識工作 |
| 僕人領導 | 服務部屬、支持成長 | Greenleaf | 專業人才、知識工作者 | 需要快速決斷的危機 |
| 情境領導 | 依部屬準備度切換 | Hersey & Blanchard | 混合成熟度團隊 | 團隊成熟度極端一致 |
| 真誠領導 | 自我認知、價值一致 | George、Avolio | 信任修復、文化轉型 | 需要戰術性彈性時 |

## 情境決策樹

```
Q1：組織當前面臨的是「變革」還是「執行」？
  ├─ 變革（轉型、重組、新事業）
  │   └─ Q2：員工對變革的抗拒程度？
  │       ├─ 高：轉型領導 + 真誠領導
  │       └─ 低：轉型領導
  └─ 執行（日常營運、目標達成）
      └─ Q3：工作性質？
          ├─ 例行、可量化：交易領導
          └─ 創意、知識工作：僕人領導

Q4：團隊成熟度一致嗎？
  ├─ 差異大 → 情境領導（對不同成員切換）
  └─ 一致
      ├─ 成熟度高 → 授權（delegating）
      ├─ 中高 → 支持（supporting）
      ├─ 中低 → 輔導（coaching）
      └─ 低 → 指示（directing）

Q5：組織信任水準？
  ├─ 低（近期有事件損害信任）→ 真誠領導優先，其他風格無效
  └─ 高 → 依 Q1–Q4 結論
```

## 五種風格深入

### 轉型領導（Transformational）
**四大面向（Bass 的 4I）**
1. **Idealized Influence（理想化影響）**：成為道德榜樣
2. **Inspirational Motivation（激勵激發）**：傳達願景
3. **Intellectual Stimulation（智能激發）**：鼓勵質疑現狀
4. **Individualized Consideration（個別關懷）**：因材施教

**操作檢查清單**
- 是否清楚傳達「為何而戰」？
- 是否允許部屬質疑老方法？
- 是否記得每位直屬的職涯目標？

### 交易領導（Transactional）
**三核心**：
- Contingent Reward（績效掛鉤獎酬）
- Management by Exception – Active（主動監督）
- Management by Exception – Passive（問題發生後才介入）

**台灣適配**：製造業、業務部門、經銷體系運作良好。過度使用會扼殺創新。

### 僕人領導（Servant）
**Greenleaf 核心提問**：「我的部屬在我的領導下，是否變得更健康、更聰明、更獨立、更可能自己也成為僕人式領導者？」

**十大特質**（Spears 整理）：傾聽、同理、療癒、覺察、說服、概念化、遠見、管家、承諾成長他人、社群建構

**陷阱**：可能被誤認為軟弱或缺乏決斷力；危機時切勿獨守此風格。

### 情境領導（Situational - Hersey-Blanchard）
**四象限**（依部屬準備度 R1–R4）

| 準備度 | 能力 | 意願 | 建議風格 |
|---|---|---|---|
| R1 | 低 | 低 | S1 指示（Telling） |
| R2 | 低 | 高 | S2 推銷（Selling） |
| R3 | 高 | 低 | S3 參與（Participating） |
| R4 | 高 | 高 | S4 授權（Delegating） |

**實務應用**：同一主管對新人用 S1、對老鳥用 S4，避免「一視同仁」的陷阱。

### 真誠領導（Authentic - George）
**四要素**
1. 自我認知（Self-awareness）
2. 關係透明（Relational transparency）
3. 平衡處理（Balanced processing）
4. 內在化道德（Internalized moral perspective）

**台灣情境**：家族企業二代接班、創辦人卸任後重建信任時特別有效。

## 分析流程

> 根據個案性質跳過不適用步驟；以下為完整候選路徑，非必跑清單。

```
1. 診斷情境：組織任務／員工成熟度／信任水準／變革強度
2. 走決策樹：得出建議風格（可能多於一個）
3. 評估現任領導者：
   - 慣用風格是什麼？
   - 與建議風格的落差？
   - 切換成本（個人改變難度、組織理解成本）
4. 產出行動清單：
   - 立即可做（本週）
   - 中期發展（3–6 個月）
   - 結構性（換人、授權、外聘教練）
5. 連回 EMBA 作業主題（個案分析／自我領導診斷）
```

## Output Format

```markdown
# 領導風格診斷：{領導者／個案}

## 一、情境診斷
| 情境變數 | 觀察 | 啟示 |
|---|---|---|
| 當前任務 | {變革／執行} | ... |
| 員工成熟度 | {R1–R4 混合？} | ... |
| 信任水準 | {高／中／低} | ... |
| 變革強度 | {漸進／破壞式} | ... |

## 二、建議風格（依決策樹）
- 主風格：{轉型／交易／僕人／情境／真誠}
- 輔助風格：{...}
- 理由：{扣回情境診斷}

## 三、現狀落差分析
- 領導者慣用風格：
- 與建議風格的 gap：
- 切換難度：

## 四、行動建議
### 立即行動（本週）
### 中期發展（3–6 個月）
### 結構性調整

## 五、風險與限制
- 風格切換可能引發的副作用
- 不適合此情境的其他風格
```

## Examples

### 正確應用
**情境**：台灣某傳產家族企業，創辦人（72 歲）交棒給二代（48 歲），員工資深化、制度鬆散，近期出現採購弊案。

**決策樹走法**：
- Q1：變革（世代交替）
- Q2：員工抗拒高（資深員工懷疑二代能力）
- Q5：信任水準低（弊案衝擊）
- **建議：真誠領導為主 + 轉型領導為輔**

**行動清單**：
- 立即：二代公開坦承「我不如父親熟悉產業，但我承諾透明與廉潔」
- 中期：建立獨立稽核、重塑採購流程、辦全員共識營
- 結構性：升任一位資深副總擔任變革大使，避免二代直接與老臣對撞

**正確之處**：扣回情境變數，而非直接套用「接班一定要真誠領導」。

### 錯誤應用
- 只寫「此情境應使用轉型領導」→ 違反 Iron Law 1、2，沒有情境診斷也沒有切換路徑
- 套用 Hersey-Blanchard 卻不評估部屬準備度 → 違反 Iron Law 3，工具空轉
- 危機個案建議使用僕人領導 → 混淆情境，危機需要決斷而非純粹服務

## Gotchas

- **「我就是 X 風格」的自我設限**：EMBA 學員常自我標籤化。風格是工具不是身份；任何風格過度使用都有副作用。
- **情境領導的「準備度」判斷易失準**：主管常把自己喜歡的員工評為 R4、不喜歡的評為 R1，導致制度空轉。必須搭配 360 度評估。
- **轉型領導 × 台灣工廠文化**：現場員工需要的是明確規則與獎懲，過度「激勵願景」會被視為「老闆說夢話」。配比要抓好。
- **僕人領導的「偽服務」陷阱**：有些主管口頭說服務部屬、實際上高度監控 → 反噬信任。須配合授權行為。
- **真誠領導的「表演真誠」**：學了這套後「表演脆弱」、「包裝弱點」會被員工識破。真誠無法演，只能練。
- **世代差異不是萬靈藉口**：把年輕員工難帶一律歸因於「世代問題」，迴避了「情境領導未落實」的核心缺陷。

## References

- 五種風格理論發展史與實證研究 → 見 `references/leadership-theory-evolution.md`
- 台灣家族企業接班與領導風格切換 → 見 `references/tw-family-business-succession.md`
- 各校 EMBA 領導課程取向筆記 → 見 `references/emba-leadership-courses.md`
- 延伸：Asgard `grad-upper-echelons`（高階梯隊理論，CEO 層級）、`grad-sdt`（自我決定論）
