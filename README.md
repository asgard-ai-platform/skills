# Asgard Skills

開源的 **293 個 coding agent skills** 知識庫，分成 22 個主題類別。每個 skill 都是獨立的 Markdown 檔案（`SKILL.md`），遵循 [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) 規範，部分附帶純 Python 腳本做確定性計算。

[English](README.en.md)

## 概觀

本 repo 是 [Asgard AI Platform](https://github.com/asgard-ai-platform) 的**原料庫**。Skills 會與 [Asgard MCPs](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) 組合，打包成針對特定使用者情境的 [coding agent plugins](https://github.com/asgard-ai-platform)（例如台股分析師、電商營運、政策研究者）。

每個 skill 封裝的是某個明確任務的**方法論 + 判斷 + 陷阱**——那些 LLM agent 若沒有提示就會重新摸索、或直接做錯的東西。

## Repo 結構

```
.
├── {category}-{skill-name}/
│   ├── SKILL.md           ← Level 1 frontmatter + Level 2 指引
│   ├── examples/          ← （必存在，視需要填充）
│   ├── references/        ← （冗長內容外掛於此）
│   └── scripts/           ← （僅在有確定性計算腳本時出現）
└── ...
```

## 類別（22 個前綴，293 個 skills）

| 前綴 | 數量 | 主題 |
|--------|------:|-------|
| `grad-` | 87 | 研究所級理論模型（RBV、CAPM、SEM、DID…） |
| `algo-` | 62 | 演算法（PageRank、BM25、ARIMA、EOQ…） |
| `biz-` | 22 | 商學院框架（SWOT、Porter 五力、DCF…） |
| `hum-` | 9 | 人文 / 批判性推理 |
| `tw-` | 38 | 台灣在地知識（電商、股市、稅務、電子發票、金融科技…） |
| `ecom-` | 7 | 電商實務 |
| `econ-` | 6 | 經濟學基礎 |
| `meta-` | 6 | 跨領域思維模型 |
| `ops-` | 6 | 企業營運（OKR、合約審查、pitch deck…） |
| `law-` | 5 | 法律框架 |
| `pr-` | 5 | 公關 / 品牌傳播 |
| `cs-` | 4 | 客戶服務 |
| `data-` | 4 | 資料分析 |
| `mfg-` | 4 | 製造業 |
| `mkt-` | 4 | 數位行銷 |
| `soc-` | 7 | 社會科學 |
| `stat-` | 4 | 統計方法論 |
| `tech-` | 4 | 一般技術（API、prompt engineering、MCP server…） |
| `ux-` | 4 | 設計 / UX 方法論 |
| `fin-` | 2 | 金融實務（modeling、earnings） |
| `xborder-` | 2 | 跨境電商 |
| `med-` | 9 | 大眾傳播 / 新聞寫作 |

## Skill 目錄

以下列出全部 301 個 skills，依前綴分組。點擊名稱開啟其 `SKILL.md`。簡介為各 skill frontmatter `description` 的中文摘要（WHAT + WHEN）。

<details>
<summary><b><code>grad-</code></b>　研究所級理論模型（87）</summary>

- [`grad-action-research`](grad-action-research/SKILL.md) — 用 Plan-Act-Observe-Reflect 循環與參與式行動研究（PAR），在改善實務的同時生成知識。
- [`grad-affordance`](grad-affordance/SKILL.md) — 套用 Affordance 理論（Gibson 1979、Norman 1988），分析物件提供給行動者的行動可能性。
- [`grad-agenda-setting`](grad-agenda-setting/SKILL.md) — 套用議題設定理論（McCombs & Shaw），分析媒體顯著性如何轉移到公眾認知。
- [`grad-ai-ethics`](grad-ai-ethics/SKILL.md) — 套用 AI 倫理框架（公平、課責、透明、隱私），評估 AI 系統的演算法偏見、可解釋性與價值對齊。
- [`grad-ambidexterity`](grad-ambidexterity/SKILL.md) — 套用組織雙元理論，平衡探索與利用兩類活動。
- [`grad-ant`](grad-ant/SKILL.md) — 套用行動者網絡理論（Latour、Callon），追蹤人與非人 actants 如何透過轉譯形成網絡。
- [`grad-auction-theory`](grad-auction-theory/SKILL.md) — 套用拍賣理論，比較四種正典拍賣形式並評估收益等價性。
- [`grad-behavioral-finance`](grad-behavioral-finance/SKILL.md) — 套用行為財務理論，辨識系統性投資人偏誤及其對資產價格的影響。
- [`grad-blooms`](grad-blooms/SKILL.md) — 套用 Bloom 修訂版分類學，依六個認知層次分類學習目標並設計評量。
- [`grad-born-global`](grad-born-global/SKILL.md) — 套用 Born Global 框架，分析在資源限制下從創立即快速國際化的公司。
- [`grad-brand-equity`](grad-brand-equity/SKILL.md) — 套用品牌權益框架（Aaker 1991、Keller 1993），評估與建構顧客導向品牌價值。
- [`grad-business-ecosystems`](grad-business-ecosystems/SKILL.md) — 套用 Moore 商業生態系框架，分析企業如何透過誕生、擴張、權威、更新四階段共演化並佔據不同生態角色。
- [`grad-capm`](grad-capm/SKILL.md) — 套用資本資產定價模型（CAPM），估算預期報酬與評估風險報酬取捨。
- [`grad-cas`](grad-cas/SKILL.md) — 套用複雜適應系統理論，分析具有湧現、自組織、共演化與混沌邊緣動態的現象。
- [`grad-case-study`](grad-case-study/SKILL.md) — 套用 Yin 的個案研究設計，以單／多個案與三角驗證調查 how/why 問題。
- [`grad-cct`](grad-cct/SKILL.md) — 套用消費者文化理論，把消費分析為由身份、市場文化與意識形態塑造的文化實踐。
- [`grad-cognitive-load`](grad-cognitive-load/SKILL.md) — 套用認知負荷理論，依工作記憶限制管理內在、外在與相關負荷以最佳化教學設計。
- [`grad-constructivism`](grad-constructivism/SKILL.md) — 套用建構主義學習理論，依主動知識建構、鷹架與最近發展區設計教學。
- [`grad-contract-theory`](grad-contract-theory/SKILL.md) — 套用契約理論，在道德風險與逆選擇下設計誘因相容的契約。
- [`grad-coopetition`](grad-coopetition/SKILL.md) — 套用 Brandenburger & Nalebuff（1996）競合價值網框架，描繪商業關係中的合作與競爭動態。
- [`grad-critical-realism`](grad-critical-realism/SKILL.md) — 套用 Bhaskar 批判實在論，從真實／實際／經驗三層本體論、回溯性推論機制以及結構─能動性辯證分析現象。
- [`grad-cultivation`](grad-cultivation/SKILL.md) — 套用 Gerbner 涵化理論，分析長期媒體曝露如何形塑世界觀。
- [`grad-diamond`](grad-diamond/SKILL.md) — 套用 Porter 鑽石模型，分析特定產業的國家競爭優勢。
- [`grad-did`](grad-did/SKILL.md) — 套用差異中之差異（DID），比較處理組與對照組結果變化以估算因果效應。
- [`grad-digital-transformation`](grad-digital-transformation/SKILL.md) — 套用數位化、數位優化、數位轉型三層框架，診斷與規劃數位科技驅動的組織變革。
- [`grad-disruptive-innovation`](grad-disruptive-innovation/SKILL.md) — 套用 Christensen 破壞式創新理論，評估低階與新市場對在位者的威脅。
- [`grad-dual-process`](grad-dual-process/SKILL.md) — 套用雙歷程理論，診斷判斷源自快速直覺（系統一）或慢速分析（系統二），辨識相應的認知偏誤。
- [`grad-elm`](grad-elm/SKILL.md) — 套用 ELM 推敲可能性模式，依受眾推敲程度匹配訊息類型來設計說服策略。
- [`grad-embeddedness`](grad-embeddedness/SKILL.md) — 套用 Granovetter 鑲嵌理論，分析經濟行為如何鑲嵌於持續性社會關係，避免過度／不足社會化的解釋。
- [`grad-emh`](grad-emh/SKILL.md) — 套用效率市場假說（Fama 1970），以弱式、半強式、強式評估資訊在資產價格中的反映程度。
- [`grad-ethnography`](grad-ethnography/SKILL.md) — 套用民族誌方法──長期投入、參與觀察、厚描與網路民族誌──研究文化與社群。
- [`grad-event-study`](grad-event-study/SKILL.md) — 套用事件研究法，衡量公司或市場事件前後的異常報酬與累積異常報酬（CAR）。
- [`grad-fama-french`](grad-fama-french/SKILL.md) — 套用 Fama-French 三因子模型，把資產報酬分解為市場、規模與價值因子。
- [`grad-field-theory`](grad-field-theory/SKILL.md) — 套用 Bourdieu 場域理論，從場域、資本、慣習三者交互分析權力關係。
- [`grad-flow`](grad-flow/SKILL.md) — 套用心流理論，診斷最佳體驗條件，設計挑戰與技能平衡的環境以維持投入。
- [`grad-framing`](grad-framing/SKILL.md) — 套用框架理論，分析選擇、強調與排除如何形塑議題詮釋。
- [`grad-governance`](grad-governance/SKILL.md) — 套用治理理論，分析超越傳統政府的多層次、網絡式與協作治理安排。
- [`grad-grounded-theory`](grad-grounded-theory/SKILL.md) — 套用紮根理論（Glaser & Strauss），透過開放、軸心、選擇性編碼從質性資料歸納建構理論。
- [`grad-hlm`](grad-hlm/SKILL.md) — 套用階層線性模型（HLM），以隨機截距與斜率分析巢套資料，處理組內相關與跨層交互作用。
- [`grad-info-economics`](grad-info-economics/SKILL.md) — 套用資訊經濟學，診斷與補救由資訊不對稱造成的市場失靈。
- [`grad-innovation-diffusion-bass`](grad-innovation-diffusion-bass/SKILL.md) — 套用 Bass 擴散模型（1969），用創新與模仿係數預測創新採用。
- [`grad-is-success`](grad-is-success/SKILL.md) — 套用 DeLone & McLean 資訊系統成功模型，從六個相依構面評估 IS 成效。
- [`grad-mechanism-design`](grad-mechanism-design/SKILL.md) — 套用機制設計（反向賽局論），為配置問題設計誘因相容的規則。
- [`grad-meta-analysis`](grad-meta-analysis/SKILL.md) — 套用後設分析，整合多項研究的效果量、評估異質性與發表偏誤。
- [`grad-mixed-methods`](grad-mixed-methods/SKILL.md) — 用聚合、解釋順序、探索順序等策略設計與執行混合方法研究，做質量真正整合。
- [`grad-mm-theorem`](grad-mm-theorem/SKILL.md) — 套用 Modigliani-Miller 定理，分析資本結構決策並辨識融資選擇何時影響企業價值。
- [`grad-narrative`](grad-narrative/SKILL.md) — 套用敘事研究方法，從生命故事與口述歷史的結構、時間性與意義建構理解人類經驗。
- [`grad-network-economics`](grad-network-economics/SKILL.md) — 套用網絡經濟學，分析具網絡效應、臨界質量動態與平台競爭的市場。
- [`grad-oli`](grad-oli/SKILL.md) — 套用 Dunning OLI 折衷理論，依所有權、區位、內部化優勢評估外人直接投資決策。
- [`grad-org-ecology`](grad-org-ecology/SKILL.md) — 套用組織生態學（Hannan & Freeman），分析組織創立、失敗與選擇的族群層次動態。
- [`grad-panel-data`](grad-panel-data/SKILL.md) — 用固定效果、隨機效果與動態 GMM 進行追蹤資料分析，運用縱向變異並控制不可觀察異質性。
- [`grad-paradigms`](grad-paradigms/SKILL.md) — 套用 Kuhn 典範理論，以常態科學、異常、危機、革命的循環分析科學進展。
- [`grad-paradox-theory`](grad-paradox-theory/SKILL.md) — 套用 Smith & Lewis 弔詭理論，辨識並管理績效、組織、歸屬、學習四面向的組織張力。
- [`grad-pecking-order`](grad-pecking-order/SKILL.md) — 套用啄食順序理論（Myers & Majluf 1984），分析資訊不對稱如何驅動融資階層決策。
- [`grad-phenomenology`](grad-phenomenology/SKILL.md) — 套用現象學方法，含懸置（epoche）、生活經驗探究與詮釋現象學分析（IPA），揭示經驗本質。
- [`grad-platform-economics`](grad-platform-economics/SKILL.md) — 套用平台經濟學，分析網絡效應、解雞生蛋問題並設計多邊平台定價策略。
- [`grad-pls-sem`](grad-pls-sem/SKILL.md) — 套用 PLS-SEM 偏最小平方結構方程，結合反映性與形成性測量模型，最大化內生構念解釋變異。
- [`grad-policy-streams`](grad-policy-streams/SKILL.md) — 套用 Kingdon 多重源流框架，分析問題、政策、政治三流匯合如何開啟政策窗。
- [`grad-pragmatism`](grad-pragmatism/SKILL.md) — 套用實用主義哲學（Peirce、James、Dewey），把知識視為行動工具、以實際後果評價觀念、把探究當問題解決。
- [`grad-public-choice`](grad-public-choice/SKILL.md) — 套用公共選擇理論，把政治決策分析為理性自利行為。
- [`grad-real-options`](grad-real-options/SKILL.md) — 套用實質選擇權分析，為投資決策中內含的管理彈性估值。
- [`grad-sd-logic`](grad-sd-logic/SKILL.md) — 套用服務主導邏輯（Vargo & Lusch 2004）與價值共創原則，重構交換與價值創造。
- [`grad-sdt`](grad-sdt/SKILL.md) — 套用自我決定理論，沿自主性連續體分析動機品質，設計滿足三種基本心理需求的介入。
- [`grad-sem`](grad-sem/SKILL.md) — 套用結構方程模型（SEM），結合測量模型（CFA）與結構模型（路徑分析）檢驗假設的因果結構。
- [`grad-sensemaking`](grad-sensemaking/SKILL.md) — 套用 Weick 意義建構理論，分析個人與組織如何從模糊情境中建構意義。
- [`grad-servqual`](grad-servqual/SKILL.md) — 套用 SERVQUAL 模型（Parasuraman、Zeithaml、Berry 1988），從五構面衡量服務品質落差。
- [`grad-signaling`](grad-signaling/SKILL.md) — 套用 Spence（1973）訊號理論，分析資訊不對稱下行動者如何透過昂貴可信的訊號傳達私有資訊。
- [`grad-social-capital`](grad-social-capital/SKILL.md) — 套用社會資本理論（Putnam、Coleman、Bourdieu、Burt），分析網絡結構與信任如何產生價值或形成限制。
- [`grad-social-identity`](grad-social-identity/SKILL.md) — 套用社會認同理論，分析群體分類、認同與群際比較如何驅動行為、偏見與衝突。
- [`grad-sociotechnical`](grad-sociotechnical/SKILL.md) — 套用社會技術系統理論，透過社會與技術子系統的聯合最佳化來分析與設計工作系統。
- [`grad-spiral-of-silence`](grad-spiral-of-silence/SKILL.md) — 套用沈默螺旋理論（Noelle-Neumann），分析感知意見氣候如何壓抑少數意見表達。
- [`grad-strat-agency`](grad-strat-agency/SKILL.md) — 套用代理理論（Jensen & Meckling 1976），診斷主理人─代理人問題（道德風險、逆選擇）並設計治理機制以對齊利益。
- [`grad-strat-dynamic-cap`](grad-strat-dynamic-cap/SKILL.md) — 套用動態能力框架（Teece 等 1997）的感知、把握、轉化，分析企業如何在快速變動環境中調適與重組能力。
- [`grad-strat-institutional`](grad-strat-institutional/SKILL.md) — 套用制度理論（DiMaggio & Powell 1983），分析強制、模仿、規範性同形壓力如何形塑組織結構與實踐。
- [`grad-strat-kbv`](grad-strat-kbv/SKILL.md) — 套用知識基礎觀（Grant 1996）與 Nonaka & Takeuchi 的 SECI 模型，分析組織如何創造、移轉與整合知識以形成競爭優勢。
- [`grad-strat-rbv`](grad-strat-rbv/SKILL.md) — 套用資源基礎觀（Barney 1991）與 VRIO 框架，評估企業資源與能力是否形成可持續競爭優勢。
- [`grad-strat-stakeholder`](grad-strat-stakeholder/SKILL.md) — 套用 Freeman（1984）利害關係人理論與 Mitchell 等人的分類法做利害關係人分析。
- [`grad-strat-tce`](grad-strat-tce/SKILL.md) — 套用交易成本經濟學（Williamson 1975、1985），依交易特性分析市場、混合或科層的治理結構選擇。
- [`grad-strat-upper-echelons`](grad-strat-upper-echelons/SKILL.md) — 套用高階梯隊理論（Hambrick & Mason 1984），分析高階管理團隊的人口統計、經驗與價值如何形塑策略選擇與組織結果。
- [`grad-structuration`](grad-structuration/SKILL.md) — 套用 Giddens 結構化理論，分析結構的二元性──社會結構既是實踐的媒介也是其結果。
- [`grad-survey-design`](grad-survey-design/SKILL.md) — 套用嚴謹的問卷設計原則，含構念操作化、Likert 量表發展、信效度評估與共同方法變異控制。
- [`grad-sustainability`](grad-sustainability/SKILL.md) — 套用永續框架（三重底線、SDGs、ESG、循環經濟），評估策略是否平衡經濟、社會與環境三維度。
- [`grad-systematic-review`](grad-systematic-review/SKILL.md) — 依 PRISMA 框架做系統性文獻回顧，含明確檢索策略、納入排除標準、品質評估與透明合成。
- [`grad-tam-utaut`](grad-tam-utaut/SKILL.md) — 套用科技接受模型（Davis 1989）與 UTAUT（Venkatesh 等 2003），預測技術採用。
- [`grad-tpack`](grad-tpack/SKILL.md) — 套用 TPACK 框架，從技術、教學、內容知識交集評估與設計科技融入教學。
- [`grad-tpb`](grad-tpb/SKILL.md) — 套用計畫行為理論，從態度、主觀規範、知覺行為控制預測行為意圖並找出介入槓桿點。
- [`grad-uppsala`](grad-uppsala/SKILL.md) — 套用 Uppsala 國際化模型，依心理距離與經驗學習分析逐步進入國外市場。

</details>

<details>
<summary><b><code>algo-</code></b>　演算法（62）</summary>

- [`algo-ad-bidding`](algo-ad-bidding/SKILL.md) — 實作並挑選廣告出價策略，從手動 CPC 到自動 target-CPA、target-ROAS。
- [`algo-ad-budget`](algo-ad-budget/SKILL.md) — 用邊際報酬分析在多檔廣告活動間最佳化預算分配。
- [`algo-ad-ctr`](algo-ad-ctr/SKILL.md) — 從特徵建構 CTR 預測模型來估算廣告點擊率。
- [`algo-ad-gsp`](algo-ad-gsp/SKILL.md) — 實作 GSP 廣義第二價拍賣，做廣告版位分配與計價。
- [`algo-ad-vcg`](algo-ad-vcg/SKILL.md) — 實作 VCG 機制，做誘因相容（誠實出價）的廣告版位分配。
- [`algo-blockchain-basics`](algo-blockchain-basics/SKILL.md) — 說明區塊鏈基礎：分散式帳本架構、共識機制與區塊結構。
- [`algo-blockchain-smart-contract`](algo-blockchain-smart-contract/SKILL.md) — 在區塊鏈上設計與實作可自動執行的智能合約。
- [`algo-ecom-bm25`](algo-ecom-bm25/SKILL.md) — 實作 BM25 排名函數，做電商商品搜尋的相關性評分。
- [`algo-ecom-ranking`](algo-ecom-ranking/SKILL.md) — 設計多目標電商商品排序，結合相關性、轉換率與商業指標。
- [`algo-ecom-search`](algo-ecom-search/SKILL.md) — 從查詢理解到結果呈現，全鏈路優化電商搜尋相關性。
- [`algo-forecast-arima`](algo-forecast-arima/SKILL.md) — 建構 ARIMA 時間序列預測模型，含趨勢與季節性分解。
- [`algo-forecast-ensemble`](algo-forecast-ensemble/SKILL.md) — 把多個預測模型組合成 ensemble 預測以提升精度。
- [`algo-forecast-exponential`](algo-forecast-exponential/SKILL.md) — 套用指數平滑法，對時間序列做加權移動平均預測。
- [`algo-forecast-prophet`](algo-forecast-prophet/SKILL.md) — 用 Meta Prophet 對含節假日與變點的商業時序建構預測模型。
- [`algo-hr-compensation`](algo-hr-compensation/SKILL.md) — 做薪酬對標分析，把薪資定位到市場資料上。
- [`algo-hr-matching`](algo-hr-matching/SKILL.md) — 實作 Gale-Shapley 穩定配對演算法，解雙邊媒合問題。
- [`algo-hr-turnover`](algo-hr-turnover/SKILL.md) — 建構員工離職預測模型，找出流失風險與留任驅動因子。
- [`algo-mfg-cpk`](algo-mfg-cpk/SKILL.md) — 計算 Cpk 製程能力指數，評估製程是否符合規格要求。
- [`algo-mfg-doe`](algo-mfg-doe/SKILL.md) — 設計與分析因子實驗，找出顯著製程因子並最佳化參數。
- [`algo-mfg-fmea`](algo-mfg-fmea/SKILL.md) — 執行 FMEA，系統性辨識、排序並降低潛在失效模式。
- [`algo-mfg-spc`](algo-mfg-spc/SKILL.md) — 實作統計製程控制（SPC）管制圖，監控生產製程穩定度。
- [`algo-net-centrality`](algo-net-centrality/SKILL.md) — 計算網路中心性指標，找出圖中的重要節點。
- [`algo-net-community`](algo-net-community/SKILL.md) — 用 Louvain 演算法做社群偵測，找出網路中緊密連結的群組。
- [`algo-net-influence`](algo-net-influence/SKILL.md) — 解影響力最大化問題，挑選最佳種子節點達到最大資訊擴散。
- [`algo-nlp-lda`](algo-nlp-lda/SKILL.md) — 用 LDA 做主題建模，從文件集中發現潛在主題。
- [`algo-nlp-ner`](algo-nlp-ner/SKILL.md) — 實作命名實體識別（NER），辨識並分類文本中的實體。
- [`algo-nlp-similarity`](algo-nlp-similarity/SKILL.md) — 用詞彙與語意方法計算文本相似度，做匹配與去重。
- [`algo-nlp-summarization`](algo-nlp-summarization/SKILL.md) — 用抽取式與生成式方法實作文本摘要。
- [`algo-price-bundle`](algo-price-bundle/SKILL.md) — 用純綑綁、混合綑綁與消費者剩餘分析設計綑綁定價策略。
- [`algo-price-conjoint`](algo-price-conjoint/SKILL.md) — 做聯合分析（conjoint），衡量產品屬性如何驅動偏好與付費意願。
- [`algo-price-dynamic`](algo-price-dynamic/SKILL.md) — 依需求、時間與競爭，實作即時調價的動態定價策略。
- [`algo-price-elasticity`](algo-price-elasticity/SKILL.md) — 計算需求價格彈性，量化價格變動對銷量的影響。
- [`algo-price-van-westendorp`](algo-price-van-westendorp/SKILL.md) — 做 Van Westendorp 價格敏感度分析（PSM），找出可接受價格區間。
- [`algo-rank-bayesian`](algo-rank-bayesian/SKILL.md) — 用貝氏平均法結合觀測評分與先驗，對項目做排名。
- [`algo-rank-elo`](algo-rank-elo/SKILL.md) — 實作 Elo 評分系統，從成對比較結果對人或物排名。
- [`algo-rank-trueskill`](algo-rank-trueskill/SKILL.md) — 實作 TrueSkill 評分系統，做多人與隊伍制競技排名。
- [`algo-rank-wilson`](algo-rank-wilson/SKILL.md) — 計算 Wilson Score 信賴區間，依正面比例排名並做樣本數修正。
- [`algo-rec-cf`](algo-rec-cf/SKILL.md) — 實作協同過濾推薦，依使用者行為模式產生推薦。
- [`algo-rec-content`](algo-rec-content/SKILL.md) — 用內容特徵與使用者偏好剖面匹配，做內容式推薦。
- [`algo-rec-hybrid`](algo-rec-hybrid/SKILL.md) — 設計多策略混合推薦系統以提升精度。
- [`algo-rec-mf`](algo-rec-mf/SKILL.md) — 實作矩陣分解，把使用者─物品互動矩陣分解為潛在因子表示。
- [`algo-rec-session`](algo-rec-session/SKILL.md) — 從短期行為序列做 session-based 推薦，無需長期使用者剖面。
- [`algo-risk-altman-z`](algo-risk-altman-z/SKILL.md) — 計算 Altman Z-Score，從財務比率預測企業破產機率。
- [`algo-risk-benford`](algo-risk-benford/SKILL.md) — 套用 Benford 定律，分析首位數字頻率分佈來偵測資料異常。
- [`algo-risk-credit`](algo-risk-credit/SKILL.md) — 從借款人特徵建構信用評分模型，預測違約機率。
- [`algo-risk-var`](algo-risk-var/SKILL.md) — 計算 VaR（風險值），估算給定信賴水準下的最大組合損失。
- [`algo-sc-bullwhip`](algo-sc-bullwhip/SKILL.md) — 分析並降低長鞭效應──需求波動沿供應鏈上游放大的現象。
- [`algo-sc-eoq`](algo-sc-eoq/SKILL.md) — 計算經濟訂購量（EOQ），最小化總庫存成本（訂購＋持有）。
- [`algo-sc-newsvendor`](algo-sc-newsvendor/SKILL.md) — 解報童問題：在不確定需求下做單期訂購決策。
- [`algo-sc-routing`](algo-sc-routing/SKILL.md) — 解車輛路徑問題（VRP），在容量與時間限制下最佳化配送路線。
- [`algo-sc-safety-stock`](algo-sc-safety-stock/SKILL.md) — 計算安全庫存水位，緩衝需求與前置時間的不確定性。
- [`algo-seo-backlink`](algo-seo-backlink/SKILL.md) — 用 Domain Authority、Domain Rating 與信任指標評估反向連結品質。
- [`algo-seo-content`](algo-seo-content/SKILL.md) — 從關鍵字研究、內容規劃、寫作到頁面優化，執行內容 SEO 策略。
- [`algo-seo-crawl`](algo-seo-crawl/SKILL.md) — 實作網路爬蟲管線：URL 發現、抓取、解析與儲存。
- [`algo-seo-pagerank`](algo-seo-pagerank/SKILL.md) — 用隨機漫遊模型實作 PageRank，計算網頁重要性分數。
- [`algo-seo-schema`](algo-seo-schema/SKILL.md) — 用 JSON-LD 格式實作 Schema.org 結構化資料標記，強化搜尋結果呈現。
- [`algo-seo-technical`](algo-seo-technical/SKILL.md) — 優化 Core Web Vitals（LCP、INP、CLS），提升搜尋排名與使用者體驗。
- [`algo-seo-tfidf`](algo-seo-tfidf/SKILL.md) — 實作 TF-IDF 評分，衡量詞彙相對於文件語料庫的重要性。
- [`algo-social-engagement`](algo-social-engagement/SKILL.md) — 計算並對標社群媒體在不同平台與素材變體的互動率。
- [`algo-social-influence`](algo-social-influence/SKILL.md) — 用互動加權指標衡量社群影響力，超越單純的粉絲數。
- [`algo-social-sentiment`](algo-social-sentiment/SKILL.md) — 實作 VADER 情感分析，對社群媒體文本做情感評分。
- [`algo-social-virality`](algo-social-virality/SKILL.md) — 用 SIR/SIS/SEIR 倉室模型建模病毒式傳播動態。

</details>

<details>
<summary><b><code>biz-</code></b>　商學院框架（22）</summary>

- [`biz-4p-7p`](biz-4p-7p/SKILL.md) — 套用 4P/7P 行銷組合框架，設計產品、價格、通路、促銷以及服務業的人員、流程、實體證據。
- [`biz-ansoff`](biz-ansoff/SKILL.md) — 用安索夫矩陣評估市場與產品兩維度的成長策略選項。
- [`biz-bcg-matrix`](biz-bcg-matrix/SKILL.md) — 用 BCG 成長／市占矩陣分析產品或事業組合，做資源配置決策。
- [`biz-blue-ocean`](biz-blue-ocean/SKILL.md) — 套用藍海策略，透過價值創新開創無競爭的市場空間。
- [`biz-brand-positioning`](biz-brand-positioning/SKILL.md) — 發展品牌定位策略，包含定位陳述、知覺圖、品牌個性與原型分析。
- [`biz-breakeven`](biz-breakeven/SKILL.md) — 做損益兩平分析，計算覆蓋全部成本所需的銷量或營收。
- [`biz-bsc`](biz-bsc/SKILL.md) — 套用平衡計分卡（BSC），把策略轉成財務、顧客、內部流程、學習與成長四構面的可衡量目標。
- [`biz-cac-ltv`](biz-cac-ltv/SKILL.md) — 計算並分析顧客取得成本（CAC）與終身價值（LTV），評估單位經濟與行銷效率。
- [`biz-customer-journey`](biz-customer-journey/SKILL.md) — 繪製並分析顧客旅程的認知、考慮、決策、使用與倡導階段。
- [`biz-dcf`](biz-dcf/SKILL.md) — 建構現金流折現（DCF）估值模型，估算內含價值。
- [`biz-dupont`](biz-dupont/SKILL.md) — 用杜邦分析把 ROE 拆解為獲利力、效率與槓桿三項要素。
- [`biz-financial-ratios`](biz-financial-ratios/SKILL.md) — 用獲利力、流動性、槓桿、效率、估值五類比率分析財務體質。
- [`biz-lean-six-sigma`](biz-lean-six-sigma/SKILL.md) — 套用精實與六標準差原則，消除浪費並降低製程變異。
- [`biz-pestel`](biz-pestel/SKILL.md) — 用 PESTEL 框架掃描政治、經濟、社會、科技、環境與法律六面向的總體環境。
- [`biz-porters-five-forces`](biz-porters-five-forces/SKILL.md) — 用 Porter 五力框架評估產業競爭動態與吸引力。
- [`biz-pricing-strategy`](biz-pricing-strategy/SKILL.md) — 分析並設計成本加成、價值基礎、競爭、滲透與吸脂等定價策略，含心理定價技巧。
- [`biz-stp`](biz-stp/SKILL.md) — 套用 STP（市場區隔、目標市場、定位）框架制定市場策略。
- [`biz-supply-chain`](biz-supply-chain/SKILL.md) — 用 SCOR 模型分析供應鏈的計畫、採購、製造、配送與退貨流程。
- [`biz-swot`](biz-swot/SKILL.md) — 用 SWOT 分析與 TOWS 矩陣做策略規劃。
- [`biz-toc`](biz-toc/SKILL.md) — 套用限制理論（TOC），辨識並管理系統瓶頸。
- [`biz-unit-economics`](biz-unit-economics/SKILL.md) — 分析單位經濟，評估單位獲利與商業模式可擴展性。
- [`biz-value-chain`](biz-value-chain/SKILL.md) — 套用 Porter 價值鏈分析，從組織活動中找出競爭優勢來源。

</details>

<details>
<summary><b><code>hum-</code></b>　人文 / 批判性推理（9）</summary>

- [`hum-critical-thinking`](hum-critical-thinking/SKILL.md) — 用結構化批判思考──辨識主張、證據、推理鏈、隱藏假設與邏輯謬誤──嚴謹評估或建構論證。
- [`hum-dialectics`](hum-dialectics/SKILL.md) — 套用黑格爾辯證法（正─反─合），分析矛盾並產出更高層次的理解。
- [`hum-discourse`](hum-discourse/SKILL.md) — 套用論述分析，檢視語言如何在文本與溝通中建構意義、權力關係與社會現實。
- [`hum-ethics`](hum-ethics/SKILL.md) — 套用倫理學框架──義務論、效益論、德行倫理、正義論──分析道德兩難並做有原則的決策。
- [`hum-historical-analogy`](hum-historical-analogy/SKILL.md) — 用歷史類比輔助策略決策，辨識過去與當前情境的結構相似與差異。
- [`hum-narrative`](hum-narrative/SKILL.md) — 把敘事結構與故事技巧套用到品牌、商業與溝通情境。
- [`hum-rhetoric`](hum-rhetoric/SKILL.md) — 套用古典修辭學（Ethos、Pathos、Logos）分析說服性溝通並打造有效論證。
- [`hum-socratic`](hum-socratic/SKILL.md) — 套用蘇格拉底式提問──澄清、探假設、檢驗證據、轉換觀點、追問蘊涵與後設提問──以引導學習或揭露盲點。
- [`hum-source-criticism`](hum-source-criticism/SKILL.md) — 用一手／二手分類、內部／外部批判、三角驗證與假訊息辨識評估來源可信度。

</details>

<details>
<summary><b><code>tw-</code></b>　台灣在地知識（38）</summary>

- [`tw-einvoice-guide`](tw-einvoice-guide/SKILL.md) — 導入台灣電子發票系統，含平台介接、B2B/B2C 格式、載具歸戶與報稅對帳。
- [`tw-fintech-compliance`](tw-fintech-compliance/SKILL.md) — 處理台灣金融科技法規，含金管會監理、電子支付法、VASP、AML/KYC 與監理沙盒。
- [`tw-healthcare-regulations`](tw-healthcare-regulations/SKILL.md) — 處理台灣醫療法規，含健保制度、醫材分級、藥品查驗登記、遠距醫療與健康資料保護。
- [`tw-manufacturing`](tw-manufacturing/SKILL.md) — 分析台灣製造業結構，含半導體、電子、機械與石化等產業。
- [`tw-payment-integration`](tw-payment-integration/SKILL.md) — 整合台灣金流服務商，含信用卡、ATM 轉帳、超商代收與行動支付（LINE Pay、街口）。
- [`tw-retail-landscape`](tw-retail-landscape/SKILL.md) — 分析台灣零售業：超商、百貨、超市、量販與電商，含全通路趨勢。
- [`tw-startup-legal`](tw-startup-legal/SKILL.md) — 指引台灣公司登記與法務設立，含商業組織選擇、商業／公司登記與稅籍申請。
- [`tw-stock-analysis`](tw-stock-analysis/SKILL.md) — 用基本面分析台股，含 EPS、本益比、殖利率與財報檢視。
- [`tw-tax-basics`](tw-tax-basics/SKILL.md) — 處理台灣稅制，含營所稅、營業稅、綜所稅、扣繳義務與新創租稅優惠。
- [`tw-ecom-analytics-benchmarks`](tw-ecom-analytics-benchmarks/SKILL.md) — 台灣電商 KPI 基準值（CVR、ROAS、LTV、AOV、回購率）對標與診斷。
- [`tw-ecom-analytics-ga4`](tw-ecom-analytics-ga4/SKILL.md) — 為台灣電商實作 GA4 電商追蹤，含 Enhanced Ecommerce 事件與轉換設定。
- [`tw-ecom-channel-strategy`](tw-ecom-channel-strategy/SKILL.md) — 選擇台灣電商平台組合，含 DTC（91APP、Shopline、Shopify）與市集（momo、Shopee）策略。
- [`tw-ecom-compliance-consumer`](tw-ecom-compliance-consumer/SKILL.md) — 台灣消保法合規，含七天鑑賞期範圍、例外與退換貨流程。
- [`tw-ecom-compliance-cross-border`](tw-ecom-compliance-cross-border/SKILL.md) — 涉台跨境電商的稅務與法規合規，含進口稅、關稅與 B2C 申報規則。
- [`tw-ecom-compliance-pdpa`](tw-ecom-compliance-pdpa/SKILL.md) — 台灣電商個資法（PDPA）合規，含會員同意、Cookie 政策與資料保護。
- [`tw-ecom-compliance-product`](tw-ecom-compliance-product/SKILL.md) — 台灣商品法規合規，涵蓋食品（食安法）、藥品（藥事法）、化妝品的查驗登記與標示規定。
- [`tw-ecom-dtc-91app`](tw-ecom-dtc-91app/SKILL.md) — 透過 mcp-91app 整合並操作 91APP，含商品上架、會員系統與 O2O 功能。
- [`tw-ecom-dtc-shopify-localization`](tw-ecom-dtc-shopify-localization/SKILL.md) — 為台灣市場優化 Shopify 商店，含 NT$ 定價、繁體中文在地化與金流介接。
- [`tw-ecom-dtc-shopline`](tw-ecom-dtc-shopline/SKILL.md) — 透過 mcp-shopline 整合並操作 Shopline，含商品管理、訂單與促銷設定。
- [`tw-ecom-invoice-carrier`](tw-ecom-invoice-carrier/SKILL.md) — 處理台灣電子發票載具（手機條碼、自然人憑證、會員載具）與捐贈碼流程。
- [`tw-ecom-invoice-ezpay`](tw-ecom-invoice-ezpay/SKILL.md) — 透過 mcp-ezpay-einvoice 介接 ezPay（加值服務中心）開立與管理台灣電子發票。
- [`tw-ecom-invoice-universalec`](tw-ecom-invoice-universalec/SKILL.md) — 透過 mcp-universalec-e-invoice 介接汎宇電商開立台灣電子發票。
- [`tw-ecom-invoice-void`](tw-ecom-invoice-void/SKILL.md) — 在同期內作廢台灣電子發票，或開立折讓單。
- [`tw-ecom-logistics-cold-chain`](tw-ecom-logistics-cold-chain/SKILL.md) — 台灣低溫宅配（宅配通冷藏 / 黑貓低溫），含冷鏈包裝、溫層選擇與法規要求。
- [`tw-ecom-logistics-cross-border`](tw-ecom-logistics-cross-border/SKILL.md) — 台灣跨境出口物流，含承運商選擇與跨境出貨作業管理。
- [`tw-ecom-logistics-cvs`](tw-ecom-logistics-cvs/SKILL.md) — 透過台灣超商取貨（7-11 賣貨便 / 全家 / 萊爾富 / OK）出貨，含門市選擇與取貨付款設定。
- [`tw-ecom-logistics-home`](tw-ecom-logistics-home/SKILL.md) — 介接台灣宅配業者（黑貓宅急便、宅配通、新竹物流、郵局），含計費規則與時效設定。
- [`tw-ecom-marketplace-momo`](tw-ecom-marketplace-momo/SKILL.md) — 在 momo 購物網上架與操作，含商品審核流程、比價規則與廣告投放。
- [`tw-ecom-marketplace-shopee`](tw-ecom-marketplace-shopee/SKILL.md) — 經營蝦皮台灣賣場，含商品上架、促銷、閃購與 SIP（蝦皮優選）資格。
- [`tw-ecom-operations-customer-service`](tw-ecom-operations-customer-service/SKILL.md) — 台灣電商客服，含 LINE / Messenger / Email / 電話多管道整合與回覆 SOP。
- [`tw-ecom-operations-line-oa`](tw-ecom-operations-line-oa/SKILL.md) — 透過 LINE 官方帳號經營 CRM 與會員留存，含廣播成本、分眾推播與 Messaging API。
- [`tw-ecom-operations-pricing`](tw-ecom-operations-pricing/SKILL.md) — 台灣電商定價，含含稅 / 未稅呈現、尾數慣例與市集比價策略。
- [`tw-ecom-operations-promotion`](tw-ecom-operations-promotion/SKILL.md) — 執行台灣電商促銷活動（雙11、618、年中慶、雙12、週年慶、母親節），含折扣設計與 ROI 計算。
- [`tw-ecom-payment-dispute`](tw-ecom-payment-dispute/SKILL.md) — 處理台灣電商金流爭議，含信用卡退款、超商取貨付款糾紛與申訴流程。
- [`tw-ecom-payment-ecpay`](tw-ecom-payment-ecpay/SKILL.md) — 介接綠界（ECPay）金流，含信用卡、ATM、超商代碼與超商取貨付款。
- [`tw-ecom-payment-jkopay`](tw-ecom-payment-jkopay/SKILL.md) — 介接街口支付（JKOPay）電商收款，含 Web / App 流程與街口幣回饋機制。
- [`tw-ecom-payment-newebpay`](tw-ecom-payment-newebpay/SKILL.md) — 透過 mcp-newebpay 介接藍新金流（NewebPay），含多元支付方式設定。
- [`tw-ecom-payment-tappay`](tw-ecom-payment-tappay/SKILL.md) — 介接 TapPay，含 Web / iOS / Android SDK、3DS 2.0 與定期定額扣款。

</details>

<details>
<summary><b><code>ecom-</code></b>　電商實務（7）</summary>

- [`ecom-analytics`](ecom-analytics/SKILL.md) — 用 GA4 指標、轉換漏斗分析與電商核心 KPI 分析電商成效。
- [`ecom-conversational`](ecom-conversational/SKILL.md) — 在訊息平台上設計對話式電商體驗：聊天機器人流程、商品卡片與轉換策略。
- [`ecom-inventory-health`](ecom-inventory-health/SKILL.md) — 用週轉率、ABC 分類、安全庫存與缺貨／呆滯診斷分析庫存健康度。
- [`ecom-multilingual-listing`](ecom-multilingual-listing/SKILL.md) — 為跨境電商優化多語商品頁：SEO 在地化、機翻流程與文化調適。
- [`ecom-promo-roi`](ecom-promo-roi/SKILL.md) — 計算並分析促銷 ROI：增量銷售、毛利衝擊與促銷型態比較。
- [`ecom-rfm-analysis`](ecom-rfm-analysis/SKILL.md) — 從交易資料做 RFM（最近一次、頻率、金額）顧客分群。
- [`ecom-sea-strategy`](ecom-sea-strategy/SKILL.md) — 擬定東南亞電商策略：平台選擇、金流基礎建設、物流挑戰與在地化需求。

</details>

<details>
<summary><b><code>econ-</code></b>　經濟學基礎（6）</summary>

- [`econ-behavioral`](econ-behavioral/SKILL.md) — 套用行為經濟學概念──有限理性、展望理論、心理帳戶、推力理論──分析決策偏誤。
- [`econ-business-cycle`](econ-business-cycle/SKILL.md) — 分析景氣循環的擴張、頂峰、收縮、谷底階段，及其對策略與政策的意涵。
- [`econ-game-theory`](econ-game-theory/SKILL.md) — 套用基本賽局概念──Nash 均衡、優勢策略、囚徒困境──分析策略互動。
- [`econ-macro-indicators`](econ-macro-indicators/SKILL.md) — 解讀 GDP、通膨、失業、利率、匯率等總體指標，評估經濟體質與預測趨勢。
- [`econ-market-structure`](econ-market-structure/SKILL.md) — 分析完全競爭、獨占性競爭、寡占與獨占等市場結構，預測廠商行為與市場結果。
- [`econ-supply-demand`](econ-supply-demand/SKILL.md) — 用供需分析說明價格決定、市場均衡與政策介入的影響。

</details>

<details>
<summary><b><code>meta-</code></b>　跨領域思維模型（6）</summary>

- [`meta-decision-analysis`](meta-decision-analysis/SKILL.md) — 用決策矩陣、決策樹、期望值與多準則決策分析（MCDA）做結構化決策分析。
- [`meta-first-principles`](meta-first-principles/SKILL.md) — 用第一性原理思考，把問題拆到基本真理再從頭推理。
- [`meta-mental-models`](meta-mental-models/SKILL.md) — 套用跨領域思維模型晶格，提升決策品質。
- [`meta-scenario-planning`](meta-scenario-planning/SKILL.md) — 用驅動力、不確定軸與 2x2 情境矩陣做情境規劃，準備多種可能未來。
- [`meta-structured-problem`](meta-structured-problem/SKILL.md) — 用 MECE、議題樹、假設驅動法與金字塔原理做結構化問題解決。
- [`meta-systems-thinking`](meta-systems-thinking/SKILL.md) — 套用系統思考──因果迴路圖、存量流量模型、系統原型與槓桿點分析──處理具有回饋迴路與時延的組織、經濟或社會問題。

</details>

<details>
<summary><b><code>ops-</code></b>　企業營運（6）</summary>

- [`ops-business-model-canvas`](ops-business-model-canvas/SKILL.md) — 套用商業模式畫布（BMC），用九宮格描繪並評估商業模式。
- [`ops-contract-review`](ops-contract-review/SKILL.md) — 審閱商業合約，辨識責任條款、IP 歸屬、終止條款與付款條件等風險。
- [`ops-meeting-minutes`](ops-meeting-minutes/SKILL.md) — 撰寫結構化會議紀錄，含決議、行動項與後續追蹤。
- [`ops-negotiation`](ops-negotiation/SKILL.md) — 套用原則式談判（BATNA、ZOPA、哈佛談判法）準備並執行談判。
- [`ops-okr-planning`](ops-okr-planning/SKILL.md) — 設計並導入 OKR（目標與關鍵結果），跨組織層級做目標設定與策略對齊。
- [`ops-pitch-deck`](ops-pitch-deck/SKILL.md) — 建構並撰寫投資人 pitch deck：問題、解方、市場、商模、進展、團隊與財務。

</details>

<details>
<summary><b><code>law-</code></b>　法律框架（5）</summary>

- [`law-contract`](law-contract/SKILL.md) — 分析合約基礎：成立要件（要約、承諾、對價）、必要條款與常見風險區。
- [`law-gdpr-pdpa`](law-gdpr-pdpa/SKILL.md) — 分析 GDPR、台灣個資法（PDPA）及相關法規下的資料隱私合規要求。
- [`law-ip`](law-ip/SKILL.md) — 分析專利、商標、著作權與營業秘密等智慧財產權。
- [`law-irac`](law-irac/SKILL.md) — 套用 IRAC（議題、規則、適用、結論）法做結構化法律分析。
- [`law-labor`](law-labor/SKILL.md) — 分析台灣勞動基準法基礎：工時、加班、休假與終止規則。

</details>

<details>
<summary><b><code>pr-</code></b>　公關 / 品牌傳播（5）</summary>

- [`pr-crisis-communication`](pr-crisis-communication/SKILL.md) — 用 SCCT 理論與危機聲明框架，管理預防、回應、復原三階段的危機溝通。
- [`pr-crisis-response`](pr-crisis-response/SKILL.md) — 用分類、黃金時間回應、3C 危機聲明範本與聲譽復原規劃管理公關危機。
- [`pr-media-monitoring`](pr-media-monitoring/SKILL.md) — 建立並執行媒體監測，追蹤新聞、社群與線上頻道的品牌提及、情緒與聲量佔比。
- [`pr-press-release`](pr-press-release/SKILL.md) — 用倒金字塔結構、標題寫作要訣與媒體發送策略寫出有效新聞稿。
- [`pr-social-copywriting`](pr-social-copywriting/SKILL.md) — 為 Instagram、Facebook、LinkedIn、X/Twitter 寫平台優化的社群文案，含 hook、CTA 與 hashtag 策略。

</details>

<details>
<summary><b><code>cs-</code></b>　客戶服務（4）</summary>

- [`cs-analytics`](cs-analytics/SKILL.md) — 用 CSAT、NPS、CES、首次解決率與客服工單文本探勘衡量並優化客服績效。
- [`cs-chatbot-design`](cs-chatbot-design/SKILL.md) — 設計對話式 AI 聊天機器人，含意圖辨識、槽位填充、對話流與回應生成。
- [`cs-notification-strategy`](cs-notification-strategy/SKILL.md) — 設計推播與訊息策略，含通路選擇、時機優化、個人化與疲勞管理。
- [`cs-sop`](cs-sop/SKILL.md) — 設計客服營運：分層支援（L1/L2/L3）、回應範本、SLA 定義、升級流程與客訴處理。

</details>

<details>
<summary><b><code>data-</code></b>　資料分析（4）</summary>

- [`data-cohort-analysis`](data-cohort-analysis/SKILL.md) — 做世代分析（cohort），追蹤使用者行為隨時間變化、建立留存矩陣並比較世代表現。
- [`data-dashboard-design`](data-dashboard-design/SKILL.md) — 用合理的 KPI 階層、圖表選型與互動功能設計有效的資料儀表板。
- [`data-financial-analysis`](data-financial-analysis/SKILL.md) — 解讀三大財報（損益表、資產負債表、現金流量表）以評估營運體質與績效。
- [`data-sql-optimization`](data-sql-optimization/SKILL.md) — 用 EXPLAIN 分析、索引策略與常見反模式修正來優化 SQL 查詢效能。

</details>

<details>
<summary><b><code>mfg-</code></b>　製造業（4）</summary>

- [`mfg-oee-analysis`](mfg-oee-analysis/SKILL.md) — 計算並診斷整體設備效率（OEE），拆解為可用率、效能率與品質率。
- [`mfg-predictive-maintenance`](mfg-predictive-maintenance/SKILL.md) — 用感測器資料、剩餘壽命（RUL）ML 模型與 P-F 曲線框架設計預測性維護策略。
- [`mfg-production-planning`](mfg-production-planning/SKILL.md) — 用 MPS（主排程）、MRP（物料需求規劃）與產能規劃設計生產計畫。
- [`mfg-supplier-scorecard`](mfg-supplier-scorecard/SKILL.md) — 用品質、交期、價格與服務四面向的加權計分卡評估與管理供應商。

</details>

<details>
<summary><b><code>mkt-</code></b>　數位行銷（4）</summary>

- [`mkt-ab-testing`](mkt-ab-testing/SKILL.md) — 為登陸頁、EDM、廣告素材與定價設計並執行行銷 A/B 測試，含正確的測試設計與結果分析。
- [`mkt-ad-optimization`](mkt-ad-optimization/SKILL.md) — 在 Google Ads、Meta Ads、LINE LAP 上優化數位廣告活動，含出價、受眾、素材測試與 ROAS 優化。
- [`mkt-content-calendar`](mkt-content-calendar/SKILL.md) — 為多平台內容行銷建立並管理內容月曆，含編輯排程、內容類型分配與團隊流程。
- [`mkt-seo-audit`](mkt-seo-audit/SKILL.md) — 做技術與頁面 SEO 稽核，涵蓋可爬性、站速、行動友善與內容優化。

</details>

<details>
<summary><b><code>soc-</code></b>　社會科學（7）</summary>

- [`soc-cialdini`](soc-cialdini/SKILL.md) — 套用 Cialdini 六大說服原則──互惠、承諾／一致、社會證明、喜好、權威、稀缺──分析或設計影響策略。
- [`soc-cognitive-bias`](soc-cognitive-bias/SKILL.md) — 在決策情境辨識並分析確認偏誤、錨定、可得性捷思與沉沒成本謬誤等認知偏誤。
- [`soc-innovation-diffusion`](soc-innovation-diffusion/SKILL.md) — 套用 Rogers 創新擴散理論，分析新產品、想法或技術如何在族群中擴散。
- [`soc-policy-analysis`](soc-policy-analysis/SKILL.md) — 做結構化政策分析，含問題定義、方案評估與證據導向建議。
- [`soc-social-network`](soc-social-network/SKILL.md) — 套用社會網絡分析概念──節點、連結、中心性、結構洞、強弱連結──描繪並分析關係結構。
- [`soc-stakeholder`](soc-stakeholder/SKILL.md) — 做利害關係人分析：辨識、Power-Interest 矩陣分類與影響策略發展。
- [`soc-user-research`](soc-user-research/SKILL.md) — 用訪談、焦點團體、問卷與田野觀察設計並執行使用者研究。

</details>

<details>
<summary><b><code>stat-</code></b>　統計方法論（4）</summary>

- [`stat-ab-testing`](stat-ab-testing/SKILL.md) — 用樣本數計算、隨機化、頻率派與貝氏方法及序貫檢定，設計並分析嚴謹的 A/B 測試。
- [`stat-causal-inference`](stat-causal-inference/SKILL.md) — 套用因果推論方法──反事實框架、工具變數、傾向分數匹配與 DID──從觀察資料估算因果效應。
- [`stat-eda`](stat-eda/SKILL.md) — 用描述統計、視覺化與資料品質檢查做探索性資料分析（EDA）。
- [`stat-hypothesis-testing`](stat-hypothesis-testing/SKILL.md) — 做統計假設檢定，含虛無／對立假設設定、p 值、型一／型二錯誤與檢定統計量選擇。

</details>

<details>
<summary><b><code>tech-</code></b>　一般技術（4）</summary>

- [`tech-api-integration`](tech-api-integration/SKILL.md) — 指引 REST API 整合，含 HTTP 方法、認證、錯誤處理與速率限制。
- [`tech-data-pipeline`](tech-data-pipeline/SKILL.md) — 設計資料管線，含 ETL/ELT 架構、資料源整合、排程、品質檢查與資料倉儲設計。
- [`tech-mcp-server-dev`](tech-mcp-server-dev/SKILL.md) — 建構 MCP（Model Context Protocol）伺服器，含工具定義、schema 設計、認證、錯誤處理與 Claude Code 整合。
- [`tech-prompt-engineering`](tech-prompt-engineering/SKILL.md) — 除錯並強化生產級 LLM prompt：處理 prompt injection、輸出格式漂移、長上下文指令遺忘與跨模型可移植性問題。

</details>

<details>
<summary><b><code>ux-</code></b>　設計 / UX 方法論（4）</summary>

- [`ux-design-thinking`](ux-design-thinking/SKILL.md) — 套用設計思考五階段──同理、定義、發想、原型、測試──解使用者中心問題。
- [`ux-heuristic`](ux-heuristic/SKILL.md) — 用 Nielsen 十大可用性原則做使用者介面的啟發式評估。
- [`ux-jtbd`](ux-jtbd/SKILL.md) — 套用待辦工作（JTBD）框架，從功能性、情感性與社會性工作理解顧客動機。
- [`ux-lean-startup`](ux-lean-startup/SKILL.md) — 套用精實創業方法論：Build-Measure-Learn 循環、MVP、驗證式學習與 pivot 決策。

</details>

<details>
<summary><b><code>fin-</code></b>　金融實務（2）</summary>

- [`fin-earnings-summary`](fin-earnings-summary/SKILL.md) — 摘要與分析法說會：財務亮點、管理層說明、財測指引與分析師問答重點。
- [`fin-modeling`](fin-modeling/SKILL.md) — 建構三表財務模型（損益、資產負債、現金流），含營收預測、假設管理與情境分析。

</details>

<details>
<summary><b><code>xborder-</code></b>　跨境電商（2）</summary>

- [`xborder-logistics`](xborder-logistics/SKILL.md) — 為跨境電商設計物流策略，含直郵、海外倉與保稅倉模式。
- [`xborder-sea-entry`](xborder-sea-entry/SKILL.md) — 規劃東南亞市場進入：模式選擇、法規要求、文化研究與 GTM 時程。

</details>

<details>
<summary><b><code>med-</code></b>　大眾傳播 / 新聞寫作（9）</summary>

- [`med-business`](med-business/SKILL.md) — 將財報、IPO/併購、法規變動、產業趨勢等財經素材寫成新聞稿件，強制執行財務數字溯源、分析師利益揭露、證券法風險與數字治理紀律。
- [`med-culture`](med-culture/SKILL.md) — 將展覽、表演、藝術家訪談、文化政策或藝術市場素材寫成文化藝術新聞，涵蓋文化挪用稽核、原民知識保護、來源公信力辨識與翻譯/跨文化框架紀律。
- [`med-education`](med-education/SKILL.md) — 將校園政策、研究發現、學生數據、師資議題或課綱改革素材寫成教育新聞，涵蓋研究方法論紀律、人口統計查核、效應量稽核與教育法紅線。
- [`med-entertainment`](med-entertainment/SKILL.md) — 將影評、票房分析、串流報告、影展與選角等娛樂素材寫成新聞稿件，強制執行 press junket 揭露、發布禁令合規、PR-vs-news 區分與娛樂法紀律。
- [`med-health`](med-health/SKILL.md) — 將臨床研究、公衛警示、藥物核可、流行病學或健康政策素材寫成醫療健康新聞，涵蓋相對風險框架、絕對基線揭露、證據層級查核、去識別化協議與 WHO 自殺報導合規。
- [`med-international`](med-international/SKILL.md) — 將外交、跨境衝突、聯合國/多邊組織、國際發展或地緣政治素材寫成國際新聞，涵蓋境外消息原始來源查核、翻譯精準度、衝突各方平衡與來源鏈稽核。
- [`med-news-reporter`](med-news-reporter/SKILL.md) — 將使用者提供的原始素材（逐字稿、事件紀錄、數據、直接引言）寫成可發表的新聞稿件，涵蓋即時新聞、深度調查、特稿與評論四種類型，並強制執行媒體倫理與識讀自我檢核。
- [`med-political`](med-political/SKILL.md) — 將選舉、立法、政策、官方聲明、民調或政治人物側寫素材寫成政治新聞，強制執行立場標記、民調解讀紀律、誹謗/選罷法紅線與框架中立性稽核。
- [`med-sports`](med-sports/SKILL.md) — 將賽事回顧、選手側寫、聯盟/規則變動、傷病報告、交易公告、禁藥/紀律事件等運動素材寫成新聞，涵蓋世代調整數據、運動資料來源檢核、傷情揭露邊界與運動博弈敏感性。

</details>

## Skill 結構

每份 `SKILL.md` 遵循一致的模板：

```markdown
---
name: "{category}-{skill-name}"
description: "[祈使句 WHAT + WHEN，< 1024 字元，不可含 XML 角括號]"
metadata:
  category: "WP-XX Topic Label"
  tags: [...]
---

# {Skill 顯示名稱}

## Overview / Framework
## When to Use (and When NOT to Use)
## Methodology（Phase-Gate 或 Hub-and-Spoke 模式）
## IRON LAW：{非顯而易見的約束}
## Output Format
## Gotchas
## Scripts（若適用）
## References
```

## 確定性計算腳本

目前有 20 個 skills 附帶 Python 腳本（純 stdlib、無外部依賴），處理那些 LLM 常算錯的計算：

- **財務**：`biz-cac-ltv`、`biz-breakeven`、`biz-dcf`、`biz-dupont`、`biz-financial-ratios`、`biz-unit-economics`、`grad-capm`、`fin-modeling`
- **風險 / 統計**：`algo-risk-altman-z`、`algo-risk-var`、`mkt-ab-testing`、`algo-mfg-cpk`
- **供應鏈**：`algo-sc-eoq`、`algo-sc-safety-stock`、`algo-sc-newsvendor`
- **排名**：`algo-rank-wilson`、`algo-rank-elo`、`algo-rank-bayesian`
- **電商**：`ecom-rfm-analysis`、`algo-price-elasticity`
- **搜尋**：`algo-seo-tfidf`、`algo-ecom-bm25`

每個腳本都支援 `--help`、`--input <json>`、`--verify`（內建自我測試）。輸出以 JSON 印到 stdout，方便後續串接。

```bash
# 範例
python ecom-rfm-analysis/scripts/rfm_score.py --input customers.json
python biz-cac-ltv/scripts/cac_ltv.py --marketing-cost 100000 --new-customers 500 \
  --arpu 50 --gross-margin 0.70 --monthly-churn 0.05
```

## 設計原則

1. **Iron Law**：每個 skill 都定義一條非顯而易見的約束，agent 不提示就會踩雷
2. **Hub-and-Spoke**：SKILL.md 精簡（< 200 行）；冗長內容外掛到 `references/`
3. **Phase-Gate**（演算法）：明確步驟、步驟之間設驗證關卡
4. **具體驗證**：範例必須可精確計算，不接受「大概落在某範圍」
5. **不過度教學**：假設 agent 已懂基礎，只強調它會**做錯**的地方

完整設計規則與品質標準見 [`AGENTS.md`](AGENTS.md)。

## 狀態

| 階段 | 狀態 |
|-------|:-:|
| Phase 1：四個 section 共 263 個 skills 生成 | ✅ |
| Phase 1.5：自動 lint（frontmatter、長度、IRON LAW） | ✅ 293/293 |
| Phase 1.7：with/without skill 評估（4 份樣本） | ✅ 4/4 with_skill 勝 |
| Phase 2-3：品質審計（抽樣 28 份） | ✅ 14 PASS / 13 MINOR / 1 MAJOR |
| Phase 3.5：P0 + P1 修補 | ✅ |
| Phase 4：description 最佳化（phantom trigger） | ✅ |
| Tier 1 + 2 確定性腳本（共 20 支） | ✅ 全部 `--verify` 通過 |
| Plugin 打包（Phase 5） | 🟡 規劃中（[見 `TODO.md`](TODO.md)） |

## 相關 Repo

- [`asgard-ai-platform/skill-template`](https://github.com/asgard-ai-platform/skill-template) — 建立 coding agent plugin 的樣板
- [`asgard-ai-platform/mcp-*`](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) — MCP servers（資料原料）
- Plugin bundles（即將推出） — 針對特定情境的 skills + MCPs 組合

## Domain 導航

特定領域的 skill 組織索引放在 [`docs/domains/`](docs/domains/)：

- [`tw-ecommerce.md`](docs/domains/tw-ecommerce.md) — 台灣電商（平台、金流、物流、發票、法遵、營運、分析）

## 貢獻指南

請見 [`CONTRIBUTING.md`](CONTRIBUTING.md)。提交新 skill 前務必先讀 [`AGENTS.md`](AGENTS.md) 了解目錄與品質標準。

## 授權

MIT License。見 [LICENSE](LICENSE)。
