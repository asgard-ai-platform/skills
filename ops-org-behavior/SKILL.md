---
name: "ops-org-behavior"
description: "Integrated organizational-behavior diagnostic toolkit across three layers: individual motivation (Maslow/Herzberg/McGregor/McClelland/SDT), team dynamics (Tuckman), and organizational culture (Schein three levels, Hofstede). Use for diagnosing a new team, case-study OB problems, culture change, motivation failure, team stagnation, or cross-cultural management. Triggers: 『團隊士氣低』『怎麼激勵』『文化怎麼改』『新團隊怎麼帶』『加薪沒效果』『公司的文化』『跨國團隊管不動』『Maslow』『Herzberg』『Tuckman』『Schein』『Hofstede』. For Taiwan EMBA OB/HR/cross-cultural courses (陽交／清大／師大). Single-theory deep dives: use Asgard `grad-sdt`, `grad-social-identity`, `grad-sensemaking`."
metadata:
  category: "WP-09 商學院—管理"
  tags: ["org-behavior", "motivation", "maslow", "herzberg", "sdt", "tuckman", "schein", "hofstede", "culture", "emba"]
  audience: "台灣 EMBA 在職學員、高階經理人、HR 主管"
---

# 組織行為診斷工具箱（Organizational Behavior Toolkit）

## 定位

EMBA 個案最常問的不是「哪個理論最好」，而是「這家公司／這個團隊到底卡在哪」。本 skill 把 OB 三大支柱（**動機**、**團隊**、**文化**）整合成一條診斷線，協助學員：

1. 分層診斷（個人動機 → 團隊動態 → 組織文化）
2. 避免「只用 Maslow 打天下」的框架偏食
3. 產出可操作的介入清單（誰、做什麼、何時檢視）

**與相近 Asgard skill 的邊界**：
- `grad-sdt` — 自我決定論單一深挖（內在／外在動機、三大心理需求）
- `grad-social-identity` — 群體身份認同理論
- `grad-sensemaking` — Weick 組織意義建構
- `grad-flow` — Csikszentmihalyi 心流
- **本 skill** — **整合式診斷工具箱**，不取代上述理論深度，而是在個案分析時先用本 skill 決定「該深挖哪一個理論」

## 何時使用

**觸發條件**
- 新任主管接手團隊、需要快速診斷
- 個案中出現「士氣低」「離職潮」「加薪無效」「變革受阻」等症狀
- 組織文化整合（併購後、新舊事業部）
- 跨國／跨世代團隊管理
- EMBA OB／HR／領導課程個案作業

**不適用**
- 領導者個人風格診斷 → 用 `ops-leadership-styles`
- 單一動機理論深挖 → 用 Asgard `grad-sdt` 等
- 人才盤點與繼任規劃（策略人資）→ 用 `ops-talent-strategy`（待開發）
- 薪酬設計技術細節 → 用 Asgard `algo-hr-compensation`

## IRON LAW — 組織行為診斷的三條鐵律

```
IRON LAW 1：症狀在個人層，根因常在文化層
「員工不積極」可能是動機問題（個人層），
更可能是「努力沒用」的組織故事（文化層）。
診斷必須三層都走，不能只停在抱怨最大聲的那一層。
```

```
IRON LAW 2：Herzberg 的不對稱性
薪水、環境、關係 = 保健因子（缺 → 不滿；有 → 不會滿足）
成就感、認可、成長 = 激勵因子（缺 → 不會不滿；有 → 真滿足）
加薪解決不了成就感問題。反之亦然。
```

```
IRON LAW 3：文化改不動是因為只改了表層
Schein 三層次：人造物（看得到） → 信奉價值（寫在牆上） → 基本假設（沒人說的）。
90% 的「文化改造」只改了前兩層，
真正卡住的是沒人敢討論的基本假設（「我們這行本來就⋯」）。
```

## Rationalization Table — 當 Claude 想「本案例外」時，先自問

| 可能想 | 但 Iron Law 仍適用，因為 |
|---|---|
| 「個案描述離職率高，就從動機層分析切入完事」 | 必須三層全走（個人／團隊／文化）；只停個人層 = 誤診，至少標註哪一層資料不足 |
| 「老闆只有加薪預算，就建議加薪」 | 仍要點明：加薪屬保健因子，解除不滿但不等於激勵；成就感缺口需另一組介入 |
| 「Basic Assumptions 太難挖，寫到 Espoused Values 就收尾」 | 挖不到也要在結論標註「基本假設層為推論性」；跳過此層 = 殘缺診斷 |

## 三層診斷框架

```
┌─────────────────────────────────────────────────┐
│ Layer 3：組織文化（Schein／Hofstede）              │
│   問：這裡的「基本假設」是什麼？                    │
│   工具：Schein 三層次、Hofstede 六維、文化網絡分析   │
└─────────────────────────────────────────────────┘
                      ↑ 形塑
┌─────────────────────────────────────────────────┐
│ Layer 2：團隊動態（Tuckman／Belbin）                │
│   問：團隊在哪個發展階段？角色是否完整？              │
│   工具：Tuckman 五階段、Belbin 團隊角色             │
└─────────────────────────────────────────────────┘
                      ↑ 形塑
┌─────────────────────────────────────────────────┐
│ Layer 1：個人動機（Maslow／Herzberg／SDT 等）        │
│   問：個別成員「為何而戰」？「為何不戰」？           │
│   工具：Maslow、Herzberg、McGregor、McClelland、SDT │
└─────────────────────────────────────────────────┘
```

**診斷順序**：由下而上（先聽個別成員聲音 → 觀察團隊互動 → 推敲背後文化）。
**介入順序**：由上而下（文化不改，下層徒勞）或雙管齊下。

## Layer 1：個人動機工具

### Maslow 需求層次
由低到高：**生理 → 安全 → 愛與歸屬 → 尊重 → 自我實現**。

**EMBA 常見誤用**：以為現代員工都在「自我實現」層。實際上：
- 製造業作業員：常卡在「安全」層（擔心裁員、職災）
- 新創員工：薪水低但自我實現動機強
- 中高階主管：卡在「尊重」層（權力、地位）

### Herzberg 雙因子
**保健因子（Hygiene）**：薪酬、工作環境、公司政策、同儕關係、督導品質
→ 缺乏 → **不滿**；充足 → **不會不滿**（但不等於滿足）

**激勵因子（Motivator）**：成就感、被認可、工作本身、責任、成長
→ 缺乏 → **不會有動力**；充足 → **真正激勵**

**用法**：員工抱怨 → 分類是保健還是激勵 → 對症下藥。
**台灣情境**：老闆常誤判，以為加薪可以補「成就感不足」。

### McGregor X/Y 理論
- **X 理論**：假設員工天生懶惰、需嚴格控制
- **Y 理論**：假設員工天生有責任感、需環境支持

**自證預言效應**：主管的假設會形塑員工行為。X 理論用久了，員工真的變 X。

### McClelland 三需求
| 需求 | 特徵 | 適任角色 |
|---|---|---|
| 成就需求（nAch） | 挑戰目標、自我超越 | 業務、創業、專案主管 |
| 權力需求（nPow） | 影響他人、掌控資源 | 高階主管、政治人物 |
| 歸屬需求（nAff） | 和諧關係、被接納 | 客服、HR、團隊協作 |

**用法**：關鍵職位配置、職涯輔導、激勵設計因人而異。

### SDT（自我決定論）精要
三大心理需求：**自主（Autonomy）、勝任（Competence）、連結（Relatedness）**。
滿足 → 內在動機；未滿足 → 外在動機取代（容易疲乏）。

深度討論請用 Asgard `grad-sdt`。

## Layer 2：團隊動態工具

### Tuckman 團隊發展五階段

| 階段 | 特徵 | 領導介入 |
|---|---|---|
| Forming（形成） | 客氣、觀望、依賴領導 | 提供明確目標、角色 |
| Storming（風暴） | 衝突、權力鬥爭、抵制 | **不要壓抑**，引導建設性衝突 |
| Norming（規範） | 共識形成、工作規則建立 | 放手授權、強化團隊儀式 |
| Performing（表現） | 高度自主、創意產出 | 做教練、支持而非指導 |
| Adjourning（解散） | 專案結束、人員異動 | 儀式化告別、知識沉澱 |

**關鍵洞見**：**跳過 Storming 的團隊不會直達 Performing**。老闆迴避衝突 → 團隊停留在偽 Norming（表面和諧、私下抱怨）。

### Belbin 九種團隊角色（摘要）
**思考型**：Plant（點子王）、Monitor Evaluator（分析師）、Specialist（專家）
**行動型**：Shaper（推進者）、Implementer（執行者）、Completer Finisher（完成者）
**人際型**：Coordinator（協調者）、Teamworker（和事佬）、Resource Investigator（資源探員）

**用法**：診斷團隊角色缺口（例如全是 Implementer，缺 Plant → 創新乏力）。

## Layer 3：組織文化工具

### Schein 三層次

```
1. Artifacts（人造物） ── 看得到、聽得到
   辦公室設計、穿著、儀式、語言、故事
   → 容易觀察，容易誤解

2. Espoused Values（信奉價值） ── 寫下來、說出口
   使命願景、核心價值、公開承諾
   → 可能只是表面，對內未必實踐

3. Basic Assumptions（基本假設） ── 沒人質疑
   「我們這行就是要加班」「老闆說了算」「新人不能挑戰前輩」
   → 真正決定行為，但極難改變
```

**EMBA 常見誤區**：個案作業只寫 Artifacts + Espoused Values，不敢挖 Basic Assumptions。

### Hofstede 文化六維度

| 維度 | 兩端 | 台灣典型得分 |
|---|---|---|
| 權力距離 | 低／高 | 高（58） |
| 個人主義／集體主義 | 集體／個人 | 集體（17） |
| 陽剛／陰柔 | 陰柔／陽剛 | 中（45） |
| 不確定性規避 | 低／高 | 中高（69） |
| 長期／短期導向 | 短／長 | 長期（93） |
| 放任／約束 | 約束／放任 | 約束（49） |

**用法**：
- 台商進軍東南亞／歐美 → 對照母國文化差異
- 外商入台 → 預判管理摩擦點
- 避免將 Hofstede 當「國籍 = 性格」的刻板印象，僅作組織設計參考

### Cameron & Quinn 競爭價值框架（CVF）
四類文化：**氏族（Clan）、創新（Adhocracy）、市場（Market）、科層（Hierarchy）**。
OCAI 問卷可量化現況與目標落差。

## 診斷工作流程

> 根據個案性質跳過不適用步驟；以下為完整候選路徑，非必跑清單。

```
Step 1：蒐集症狀與觀察
  - 訪談（個別成員 3–5 位）
  - 觀察（會議、辦公室動線、溝通模式）
  - 檔案（離職率、投入度調查、獎懲紀錄）

Step 2：分層歸因
  - Layer 1：這位成員的抱怨是保健還是激勵？卡在 Maslow 哪一層？
  - Layer 2：團隊停留在哪個 Tuckman 階段？角色是否完整？
  - Layer 3：哪些 Artifacts／Espoused Values 反映什麼 Basic Assumptions？

Step 3：找出槓桿點
  - 低成本高影響：通常在 Layer 1–2
  - 根本解：通常在 Layer 3（但耗時 1–3 年）

Step 4：介入清單
  - 立即（本週）：通常是保健因子或 Tuckman 介入
  - 中期（3–6 個月）：激勵因子設計、團隊角色調整
  - 結構性（12 個月+）：文化改造、儀式重塑

Step 5：設檢視指標
  - 離職率、投入度、NPS、文化調查
  - 每季回測，避免「改完就忘」
```

## Output Format

```markdown
# 組織行為診斷：{個案／團隊名稱}

## 一、症狀摘要
（3–5 條可觀察現象，避免價值判斷）

## 二、Layer 1 — 個人動機分析
### 關鍵成員畫像
| 成員 | Maslow 所在層 | 主要訴求（Herzberg） | McClelland 主導需求 |
|---|---|---|---|
| A | ... | ... | ... |

### 動機失靈點
（為何現行激勵措施無效？）

## 三、Layer 2 — 團隊動態分析
- 目前 Tuckman 階段：{...}
- 卡點：{...}
- 角色缺口（Belbin）：{...}

## 四、Layer 3 — 組織文化分析
### Schein 三層
- Artifacts：{...}
- Espoused Values：{...}
- Basic Assumptions（最難看到的）：{...}

### Hofstede／CVF 觀察（可選）
{跨文化或類型對照}

## 五、診斷結論
- 主要卡點在哪一層？
- 各層之間如何互相強化？
- 根因假設（可證偽）

## 六、介入清單
### 立即（本週）
### 中期（3–6 個月）
### 結構性（12 個月+）

## 七、檢視指標
（如何知道有效？）

## 八、限制與風險
- 本診斷的資料侷限
- 介入的副作用（例如 Storming 可能加劇短期衝突）
```

## Examples

### 正確應用
**個案**：某科技業台商併購日本同業後，台日團隊整合 18 個月仍衝突不斷，日方工程師離職率 28%。

**分層診斷**：
- Layer 1：日方工程師 Herzberg 激勵因子（成就感、認可）缺乏 — 台方會議以中文為主、日方被邊緣化
- Layer 2：團隊卡在 Storming，但被台方主管壓抑（「不要把家務事公開」）
- Layer 3：
  - Artifacts：雙語 email 政策、混合儀式
  - Espoused Values：「One Team」
  - Basic Assumptions：台方「以速度取勝」、日方「以品質取勝」，兩套假設從未公開對齊

**介入**：
- 立即：關鍵會議全英文、設立日方代表每週發言制度
- 中期：舉辦「衝突對話工作坊」讓 Storming 公開化
- 結構性：共同制定「新公司的第三套文化」，而非台方同化日方

**正確之處**：三層都挖、介入配比合理、承認 Basic Assumptions 的根本性。

### 錯誤應用
- 只用 Maslow 解釋「日方離職」→ 停在個人層，忽略文化斷層
- 把日方文化歸為「日本人就是這樣」→ Hofstede 被誤用為國籍刻板印象
- 推出「One Team」口號卻不改基本假設 → 只動 Espoused Values，三層不對齊
- 壓制 Storming 求表面和諧 → Tuckman 卡關，假 Norming

## Gotchas

- **分層錯置**：把文化問題當動機問題（加薪解決「沒人敢說真話」） → 錢花了、問題沒解
- **Maslow 過時論的過度糾正**：Maslow 不是鐵律，但仍是有用的分類工具；完全棄用反而讓學員失去共通語言
- **Herzberg 測錯因子**：「我們公司薪水不高，可是大家很有成就感所以留下來」→ 很多時候是倖存者偏差，離職的人才是被保健因子逼走的
- **Tuckman 誤診**：把「沉默」當 Norming（其實可能是 Forming 的觀望或 Storming 的壓抑）
- **Schein Basic Assumptions 挖不出來**：需要時間與心理安全感，一次訪談問不到；個案作業可坦承「假設層為推論性結論」
- **Hofstede 國籍化**：「日本人都是長期導向」是錯誤使用，文化維度是群體統計傾向，不是個人標籤
- **文化改造的耐性**：承諾 6 個月改文化 = 保證失敗。基本假設至少要 18–36 個月。短期只能改儀式與制度
- **個案作業字數限制下的取捨**：5000 字以內先走完三層「輪廓」，再選一層深挖，優於單層窮盡

## References

- 動機理論比較與實證研究演進 → 見 `references/motivation-theories.md`
- Schein 組織文化三層次深度解析 → 見 `references/schein-culture.md`
- 台灣／東亞企業文化與 Hofstede 應用筆記 → 見 `references/tw-culture-context.md`
- 各校 EMBA OB／HR 課程取向筆記 → 見 `references/emba-ob-courses.md`
- 延伸：Asgard `grad-sdt`（SDT 深挖）、`grad-social-identity`（社會認同）、`grad-sensemaking`（意義建構）、`grad-flow`（心流）、`algo-hr-turnover`（離職預測）、`ops-leadership-styles`（本 repo，領導風格）
