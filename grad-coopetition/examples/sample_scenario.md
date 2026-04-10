# Example: TensorScale vs. the AI Inference Stack

## Scenario

**TensorScale**（虛構，台灣 AI 推論晶片新創，2025 年 Series C，估值 $12 億美元）正在制定 2026 年市場策略。其旗艦晶片 TS-X1 在 LLM 推論工作負載的性價比上優於 NVIDIA H100 約 2.2 倍，但市場佔有率不足 3%。

執行長向策略團隊提問：「我們應該怎麼看待 NVIDIA？他們是我們的天花板，還是我們可以合作的夥伴？AWS 買我們的晶片，但他們自己也在做 Trainium——這到底是什麼關係？」

---

## Analysis

### Step 1: Map the Value Net

**中心節點**：TensorScale（TS-X1 推論晶片）

| 角色 | 玩家 | 雙重角色說明 |
|------|------|------------|
| **Customers** | AWS、Azure、GCP、CoreWeave、Lambda Labs | AWS 同時是客戶（採購 TS-X1）且是競爭者（自研 Trainium）|
| **Suppliers** | TSMC（晶圓製造）、Quanta（板卡組裝）、NVIDIA（CUDA 生態間接依賴） | NVIDIA 不直接供應，但其軟體標準事實上控制了 TensorScale 的互操作性成本 |
| **Competitors** | NVIDIA（H100/B200）、AMD（MI300X）、AWS Trainium、Google TPU | 純競爭維度：爭奪同一推論工作負載預算 |
| **Complementors** | PyTorch / vLLM / TensorRT-LLM 開源社群、Anthropic / Mistral / Meta AI（模型開發商）、MLPerf 基準維護者 | 他們的模型與框架跑在 TS-X1 上越流暢，TS-X1 的市場價值越高 |

**關鍵雙重角色識別**：
- **NVIDIA**：競爭者（搶訂單）＋間接「規則制定者」（CUDA 生態決定軟體移植成本）→ 在 Tactics 層可利用
- **AWS**：客戶（貢獻 2025 年 38% 營收）＋競爭者（Trainium 在 AWS 內部侵蝕 TS-X1 訂單）
- **Meta AI**：互補者（Llama 模型優化版跑在 TS-X1 上）＋潛在客戶（自建推論叢集）

---

### Step 2: Assess Added Value

**定義「遊戲總價值」**：AI 推論基礎設施市場 2026 年預估規模 $420 億美元（Gartner 估計）

| 玩家 | 加入時的總價值 | 退出時的總價值 | Added Value | 評估 |
|------|-------------|-------------|------------|------|
| **TensorScale** | $420B | $415B（H100 填補，但成本+30%）| **~$5B** | 中；可替代，但替代成本顯著 |
| **NVIDIA** | $420B | $210B（推論效能崩潰，市場萎縮）| **~$210B** | 極高；幾乎不可替代 |
| **AWS（作為客戶）** | $420B | $378B（失去最大部署渠道）| **~$42B** | 高；但 TensorScale 單一客戶集中風險過高 |
| **vLLM 社群** | $420B | $390B（推論吞吐量下降，採用速度降低）| **~$30B** | 高；免費貢獻但影響巨大 |

**結論**：TensorScale 的 Added Value 偏低——因為 NVIDIA 可替代它，且缺乏軟體護城河。策略的核心目標是**提升自身 Added Value**，而非直接與 NVIDIA 正面競爭。

---

### Step 3: Apply PARTS Framework

| Lever | Current State（2025 Q4） | Recommended Change（2026） |
|-------|------------------------|--------------------------|
| **Players** | 市場由 NVIDIA 主導；獨立雲（CoreWeave、Lambda Labs）規模仍小 | 主動扶植獨立雲成長（提供優惠定價、聯合行銷）；吸引 Mistral、Cohere 等模型廠成為 design partner，增加互補者節點 |
| **Added Value** | TS-X1 成本優勢真實存在，但軟體移植成本吃掉 40% 優勢 | 推出 **TS Inference Runtime（TIR）**：一層 CUDA 相容 API，讓現有 PyTorch 模型零改動跑在 TS-X1；目標：將移植成本降至 $0，使 2.2× 優勢全數落地 |
| **Rules** | CUDA 是事實標準；MLPerf 基準由大廠主導定義 | 聯合 AMD、Intel Habana 共同提案 **Open Inference Standard（OIS）**，將評測重點從訓練吞吐量移向「推論美元效率」——TensorScale 的強項 |
| **Tactics** | TensorScale 避談 NVIDIA，市場感知為「另一個挑戰者」 | 公開宣示 **NVIDIA 相容策略**（合作信號），消除客戶的轉換疑慮；同時悄悄深化與 Meta AI 的模型優化合作，建立差異化壁壘 |
| **Scope** | 聚焦雲端資料中心推論 | 將遊戲擴大到**邊緣推論**（車載、工業 IoT）——NVIDIA 在此市場佈局分散，TensorScale 的低功耗設計有結構優勢；在邊緣市場建立灘頭，反向增強雲端品牌 |

---

### Step 4: Design Co-opetition Strategy

**對象：NVIDIA**
- **合作**：接受 CUDA 生態現實，投資 TIR 相容層；與 NVIDIA DGX Cloud 共存（不同工作負載）
- **競爭**：針對純推論場景（非訓練）的預算，主打 TCO 優勢
- **邊界規則**：技術交流僅限公開 API；絕不向 NVIDIA 透露 TS-X1 的微架構細節或客戶名單

**對象：AWS**
- **合作**：維持 AWS Marketplace 上架；聯合發布 TS-X1 on EC2 的基準測試白皮書
- **競爭**：主動開發 AWS 的競對雲（Azure ML、GCP Vertex）上的優化版，避免單一客戶依賴
- **邊界規則**：AWS 的採購合約不包含獨家條款；路線圖資訊提前 90 天而非 180 天

**對象：vLLM / Meta AI（互補者）**
- **合作**：全力投入；指派 3 名工程師常駐 vLLM 開源社群；資助 Meta Llama 在 TS-X1 上的官方優化
- **競爭**：不適用——互補者越強，TensorScale 越強
- **邊界規則**：貢獻的優化 kernel 開源，但 TIR 的底層排程演算法保持閉源

---

## Result

```markdown
# Co-opetition Analysis: TensorScale（TS-X1 推論晶片，2026 策略）

## Value Net Map
- Customers: AWS（38% 營收）、Azure、GCP、CoreWeave、Lambda Labs
  → AWS 雙重角色：客戶 ＋ Trainium 競爭者
- Suppliers: TSMC、Quanta
- Competitors: NVIDIA H100/B200（主要）、AMD MI300X、AWS Trainium、Google TPU
  → NVIDIA 雙重角色：競爭者 ＋ 事實上的規則制定者（CUDA 標準）
- Complementors: PyTorch/vLLM 社群、Anthropic/Mistral/Meta AI（模型廠）、MLPerf
  → Meta AI 雙重角色：互補者 ＋ 潛在大客戶

## Added Value Assessment
| Player | Added Value | Leverage |
|--------|-------------|----------|
| TensorScale | ~$5B（中；可被替代）| Low—需透過 TIR 提升至 High |
| NVIDIA | ~$210B | Extreme |
| AWS（客戶角色）| ~$42B | High |
| vLLM 社群 | ~$30B | High（且免費）|

## PARTS Analysis
| Lever | Current State | Recommended Change |
|-------|---------------|-------------------|
| Players | NVIDIA 獨大；獨立雲渺小 | 扶植 CoreWeave 等獨立雲；引入模型廠為 design partner |
| Added Value | 2.2× 性價比被移植成本稀釋 | 推出 TIR 相容層，移植成本歸零 |
| Rules | CUDA 為事實標準 | 聯合提案 OIS，將評測軸移向推論美元效率 |
| Tactics | 市場感知模糊 | 公開宣示 NVIDIA 相容（降客戶疑慮）+ 悄悄深化 Meta Llama 優化（差異壁壘）|
| Scope | 僅雲端資料中心 | 擴入邊緣推論市場，NVIDIA 此處佈局分散 |

## Co-opetition Strategy
- **與 NVIDIA**：合作於 API 相容性 ｜ 競爭於推論專用預算 ｜ 邊界：微架構與客戶名單絕不共享
- **與 AWS**：合作於 Marketplace 曝光 ｜ 競爭於多雲佈局（主動服務 Azure/GCP）｜ 邊界：無獨家條款、路線圖提前 90 天
- **與 vLLM/Meta AI**：全面合作，無競爭維度 ｜ 邊界：優化 kernel 開源，TIR 排程演算法閉源
```

**核心洞察**：TensorScale 的最大錯誤是把 NVIDIA 純粹視為敵人。真正的槓桿在於**改變遊戲規則**——透過 TIR 讓 CUDA 生態為 TS-X1 背書，透過 OIS 將評測標準移向己方優勢，透過互補者（vLLM、Meta AI）放大自身的 Added Value。直接與 NVIDIA 正面競爭，等同在對方設計的遊戲裡輸掉。
