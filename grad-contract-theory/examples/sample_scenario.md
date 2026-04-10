# Example: SaaS Sales Rep Compensation Design at Meridian Analytics

## Scenario

Meridian Analytics（B2B SaaS，年營收 $40M）正在重新設計企業銷售代表的薪酬結構。現行方案是固定底薪 $120K，季度達標後支付 $30K 獎金。問題：資深 AE（account executives）抱怨獎金設計不公平，且有多位明星業務在達標後明顯放慢腳步（ratchet 效應嫌疑）。Head of Sales 委託分析：現行合約是否存在激勵扭曲？應如何重設計？

附加資訊：
- AE 同時負責 **新簽** (new logo) 與 **續約/擴充** (expansion)，後者較難量化
- 銷售周期 3–9 個月，業績雜訊大（epsilon 大）
- 公司有留人壓力：競爭對手挖角底薪 $140K

## Analysis

### Step 1 — Classify the Information Problem

**類型：Moral hazard + multi-tasking**

| 維度 | 說明 |
|------|------|
| 隱藏行動 | Meridian 無法觀察 AE 分配多少時間在 new logo vs. expansion |
| 信號雜訊 | 季度業績 = 真實努力 + 市場波動，R² 低 |
| 多任務扭曲 | 獎金僅綁 new logo ARR，expansion 努力被犧牲 |

Principal = Meridian（風險中立）  
Agent = AE（風險趨避，效用函數 u(w) = w − c(e)，c'' > 0）  
隱藏變數 = 努力分配向量 e = (e_new, e_expansion)

---

### Step 2 — Specify Constraints

**現行合約隱含的約束分析：**

| 約束 | 現行狀態 | 問題 |
|------|----------|------|
| IC (new logo) | 達標前成立；達標後 IC 失效 | 二元獎金在達標後誘因歸零 |
| IC (expansion) | **未設計**，expansion 無激勵 | Holmstrom multi-tasking 定理：可測任務被過度激勵，不可測任務被忽略 |
| IR / PC | $120K 底薪 < 競爭對手 $140K | 留才 IR 約束趨緊，公司需支付額外租金 |
| Limited Liability | AE 無法支付負獎金 | LL binding，agent 保留資訊租金 |

**Ratchet 效應診斷：**  
季度達標後放慢 → 確認。現行合約是靜態的，但 Meridian 在制定明年配額時會參考今年業績。理性 AE 的最優策略：Q3 達標後把 pipeline 推到 Q1，避免抬高基準線。

---

### Step 3 — Solve the Optimal Contract

#### 3a. 處理 Multi-tasking（Holmstrom-Milgrom 1991）

Holmstrom-Milgrom 多任務定理：若任務 2（expansion）難以測量，  
最佳合約**降低**任務 1（new logo）的激勵強度，而非提高。

→ 不能只靠調高 new logo 提成率解決問題。

**解法：建立 composite performance index**

```
Performance Score = 0.60 × (New ARR / Quota) + 0.40 × (Net Revenue Retention)
```

- New ARR quota：基於 territory potential，與歷史業績部分脫鉤（解 ratchet）
- NRR（Net Revenue Retention）：由 CS 共同認定，12 個月滾動計算
- 兩個信號都 informative about 整體努力，符合 Holmstrom informativeness principle

#### 3b. 用連續獎金曲線取代二元閾值

**現行（binary bonus）：**
- < 100% quota → $0 獎金
- ≥ 100% quota → $30K 獎金

**新設計（piecewise linear，保留 LL）：**

| Performance Score | 獎金計算 |
|-------------------|----------|
| 0% – 50% | $0（底薪保護，LL binding） |
| 50% – 100% | $0.40 × (score − 50%) × $100K = 每1%得$400 |
| 100% – 150% | 加速器 2×：每1%得$800，上限$60K |
| > 150% | 無上限，持續 $600/1%（防止過度冒險） |

**底薪調整：** 提至 $130K（縮小與競爭對手 $140K 的差距，確保 IR 約束不破）

#### 3c. 解 Ratchet 效應

配額設定改為：
- 70% 權重：territory-based model（客戶數 × ARPU × 滲透率）
- 30% 權重：前兩年業績滾動平均

這使配額主要由可觀察的 territory 特徵決定，減少 AE 策略性壓低表現的誘因。

---

### Step 4 — Assess Completeness and Renegotiation

**合約完整性：**  
銷售合約屬於**不完全合約**（incomplete contract）— 無法預先規定所有市場狀況（競爭對手降價、客戶預算凍結）。

Hart 殘餘控制權建議：  
- 賦予 AE 在「特殊情境」（force majeure clause）申請配額調整的權利，需主管核准
- 此設計讓 AE 的關係性投資（客戶關係）受到保護，鼓勵長期導向

**Renegotiation-proofness：**  
連續獎金曲線 + NRR 指標讓合約在期中難以被策略性重談，因為兩個信號都是連續更新的。

---

## Result

```markdown
## Contract Design Analysis: Meridian Analytics AE Compensation

### Information Problem
- **Type**: Moral hazard + Multi-tasking
- **Principal**: Meridian Analytics (risk-neutral)
- **Agent**: Account Executives (risk-averse)
- **Hidden variable**: Effort allocation between new logo acquisition vs. expansion/retention

### Constraints
| Constraint              | Expression                                         | Binding? |
|-------------------------|----------------------------------------------------|----------|
| Incentive Compatibility | AE prefers (e_new, e_expansion) > shirking          | Fails post-quota under current design |
| Participation (IR)      | E[w] ≥ $140K outside option                        | Tight; requires $130K base |
| Limited Liability       | w(x) ≥ 0 for all outcomes                          | Yes — clamps downside |

### Optimal Contract Structure
- **Fixed component**: $130K base salary（+$10K vs. current，protect IR）
- **Variable component**: Piecewise linear bonus on composite score (60% New ARR / 40% NRR)；range $0–$60K standard，uncapped accelerator above 150%
- **Informativeness**: Both new ARR and NRR are informative signals of the full effort vector; using only new ARR violates the informativeness principle for expansion effort

### First-Best vs. Second-Best Gap
- **First-best outcome**: AE exerts optimal effort on both tasks; principal observes effort directly and pays fixed wage; zero efficiency loss
- **Second-best distortion**: AE still bears income risk (NRR has noise from macro churn); expansion effort slightly under-incentivized vs. first-best due to measurement lag
- **Welfare loss**: Estimated 8–12% of potential expansion ARR per year, offset by elimination of post-quota sandbagging (~15% pipeline shift observed in Q3 data)

### Recommendation
1. **Adopt composite score** immediately for Q3 cycle — NRR data already exists in Salesforce/Gainsight
2. **Transition bottom 20% AEs** on enhanced PIP track (LL still holds, no clawbacks)
3. **Decouple quota from personal history** — territory model reduces ratchet incentive within 2 quarters
4. **Add relational contract layer**: quarterly calibration meeting where AE can flag territory anomalies (incomplete contract residual control)
5. **Monitor for crowding-out**: if NRR improves but new logo drops >10%, rebalance composite weights
```

**預期效果：**
- 消除 Q3 pipeline sandbagging，預估 Q4 新簽提升 $1.2–1.8M
- Expansion ARR 隨 NRR 激勵提升，預估 net dollar retention 從 108% → 113%
- AE 流失率下降（IR 約束滿足），招募成本節省約 $200K/year
