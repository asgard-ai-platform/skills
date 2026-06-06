# SPA 關鍵條款模板

> **重要聲明**：本模板為概念性範本，實際合約必須由合格律師依台灣或適用司法管轄之法律撰寫與審核。M&A 合約金額重大，學員不可逕以本模板作為正式合約使用。

## SPA（Share Purchase Agreement）基本結構

```
1. Definitions（定義）
2. Purchase and Sale（交易主體）
3. Purchase Price（對價與調整）
4. Closing（交割）
5. Representations and Warranties（陳述與保證）
6. Covenants（承諾事項）
7. Conditions Precedent（先決條件）
8. Indemnification（賠償）
9. Termination（終止）
10. Miscellaneous（雜項，含管轄、仲裁）
```

## 第一部分：對價與調整

### 基本對價結構

```
Total Purchase Price = Base Purchase Price
                     + Working Capital Adjustment
                     − Net Debt
                     − Transaction Expenses
                     + Earn-out Payments
```

### Working Capital 調整

**目的**：確保交割日目標公司有正常營運資金

**機制**
1. 約定 Target Working Capital（通常過去 12 月平均）
2. 交割日 Closing WC 估算
3. 交割後 60–90 天精算
4. 差額按元計算，以現金補正

**條款範例**
> 「交割日目標公司之 Net Working Capital 若低於 Target Working Capital（NT$ X），買方得就差額減少 Purchase Price；若高於 Target Working Capital，買方應就差額增加 Purchase Price。」

### Net Debt 調整

**Net Debt 定義**（需合約明確）
- Total Debt = Bank Loans + Bonds + Finance Lease + Other Interest-bearing Liabilities
- Cash = Cash and Cash Equivalents（排除限制用途）
- Net Debt = Total Debt − Cash

**爭議點**
- 受限現金是否算
- 應付股利、關係人借款
- 退休金未提撥

### Earn-out 條款

**結構範例**
> 「賣方得依下列條件取得 Earn-out 對價：
>
> (a) 2026 年度目標公司經審計 EBITDA 若達 NT$ X 億，賣方得取得 NT$ Y 億；若未達但高於 NT$ Z 億，按比例計算。
>
> (b) 2027 年度同上。
>
> (c) Earn-out 期間，目標公司之會計方法、關鍵經理人（定義於附件 A）之留任、關鍵客戶（前五大）之合約延續為計算基礎。
>
> (d) 任一年度發生下列情事，本條適用減免或重新計算：公司重大重組、併購、強制性會計政策變動。
>
> (e) 爭議解決：由三方（買方、賣方、獨立會計師）協商；無法達成者由獨立會計師仲裁，其決定為終局。」

**Earn-out 常見陷阱與防範**

| 陷阱 | 買方角度 | 賣方角度 |
|---|---|---|
| 會計操縱 | 限制會計政策變動 | 保護合理營業決策 |
| 重大投資影響 EBITDA | 約定加回或排除 | 約定加回或排除 |
| 關鍵人離職 | 綁定留任 | 保護離職權利 |
| 整合影響 | 允許合理調整 | 限制過度整合 |

## 第二部分：Representations and Warranties（R&W）

### R&W 的三大功能

1. **資訊揭露**：強制賣方揭露
2. **估值保護**：R&W 不實觸發賠償
3. **風險分配**：已知風險 vs. 未知風險

### R&W 類別與樣本語言

**基本 R&W（Fundamental Representations）**
- 無時效、無上限
- 涵蓋：組織存續、授權、股權完整、無衝突

樣本：
> 「賣方具有完全之能力與權限簽訂並履行本協議。本協議經正式授權簽訂，構成賣方有效、合法、可強制執行之義務。」

**業務 R&W（Business Representations）**
- 有時效（通常 18–24 月）
- 有上限（交易金額 10–25%）

**財務 R&W 範例**
> 「目標公司截至 2025 年 12 月 31 日之經審計財務報表：
> (a) 依一般公認會計原則編製
> (b) 公允表達公司之財務狀況與營運成果
> (c) 無重大遺漏或不實」

**合約 R&W 範例**
> 「附件 X 所列重大合約：
> (a) 均為有效、合法、可強制執行
> (b) 無任何一方違約
> (c) 除附件 Y 所載外，不因 Change of Control 而終止或加速」

**訴訟 R&W 範例**
> 「除附件 Z 所揭露者外，目標公司無：
> (a) 進行中之訴訟、仲裁或行政程序
> (b) 已知可能發生之訴訟
> (c) 違反重大行政命令或判決」

### 特別 R&W（Specific Representations）

針對 DD 發現設計，範例：

**環安衛特別保證**
> 「目標公司越南二廠 2023 年 X 月之環保違規案：
> (a) 已於交割日前 30 日內完成改善
> (b) 罰款已完全繳納
> (c) 無任何後續責任
> 本 R&W 上限為 NT$ 5,000 萬，時效至交割後 3 年」

**稅務特別保證**
> 「目標公司及其子公司之跨境移轉定價文件：
> (a) 已依各地稅法要求完整備置
> (b) 無主管機關爭議或調查
> 本 R&W 無上限（限稅務機關追繳金額），時效依法定時效」

**智財特別保證**
> 「附件 A 所列核心專利：
> (a) 為目標公司合法擁有
> (b) 無第三人主張權利
> (c) 在適用法規下有效並持續有效至至少交割後 5 年
> (d) 無侵害第三人權利之情事」

## 第三部分：Indemnification（賠償機制）

### 基本架構

```
觸發：R&W 不實 或 特別事項發生

計算：Loss = Direct Damages + Consequential Damages（定義）

限制：
  De Minimis（單件門檻）
  Basket（累積門檻）：Tipping 或 Deductible
  Cap（上限）
  Survival Period（時效）

程序：
  Notice（通知期限）
  Defense（控制權）
  Settlement（和解權）
```

### De Minimis（單件門檻）

**目的**：避免小額爭議

**範例**：NT$ 300 萬以下不列入計算

### Basket（累積門檻）

**類型**
- **Tipping Basket**：累積超過門檻後，從 0 元全額賠償
- **Deductible Basket**：累積超過門檻後，僅賠超出部分

**範例**：Deductible Basket NT$ 2,000 萬
- 累積損失 1,800 萬 → 不賠
- 累積損失 2,500 萬 → 賠 500 萬

### Cap（上限）

**層級設計**
```
基本 R&W：            無上限（限交易金額）
特別保證（環安衛）：  NT$ 5,000 萬
特別保證（訴訟）：    NT$ 1.2 億
一般 R&W：           交易金額 15%
Fraud 例外：          無上限
```

### Survival Period（時效）

| R&W 類別 | 典型時效 |
|---|---|
| 基本 R&W（Title, Authority） | 永久或法定時效 |
| 一般 R&W | 18–24 月 |
| 稅務 R&W | 法定追徵時效（台灣 5–7 年） |
| 環安衛 R&W | 3–5 年或更長 |
| 勞動 R&W | 2–3 年 |

## 第四部分：Conditions Precedent（先決條件）

### 必要先決條件

1. 主管機關核准（公平會、投審會、經濟部併購、海外同等機關）
2. 主要客戶 CoC 同意
3. R&W 於交割日仍為真實
4. 無重大不利變動（Material Adverse Change, MAC）
5. 賣方履行交割前義務
6. 特定 DD 發現之補救完成

### MAC（Material Adverse Change）條款

**定義爭議大**，通常包含：
- 財務重大惡化
- 法規重大變動
- 關鍵合約終止

**通常排除**：
- 總體經濟變動
- 產業一般變動
- 戰爭、天災（除非影響大於同業）

## 第五部分：Covenants（承諾事項）

### Pre-Closing Covenants（交割前）

**賣方義務**
- 正常營運（Ordinary Course）
- 重大事項需經買方同意
- 提供資訊存取
- 主動揭露重大變動

**禁止行為**
- 重大資本支出
- 重大借款
- 重大資產處分
- 關鍵人員異動
- 股利派發（超過正常）

### Post-Closing Covenants（交割後）

**賣方義務**
- 競業禁止（5 年、指定區域）
- 挖角禁止（24–36 月）
- 保密義務
- 協助過渡

**買方義務**
- 支付對價
- 維持目標公司營運（earn-out 期間）
- 關鍵人員留任安排

## 第六部分：Termination（終止條款）

### 可終止情境

1. 雙方同意終止
2. 長時期後條件未滿足（通常 6–12 月）
3. 重大違約
4. 主管機關明確否決

### 終止費（Break Fee / Termination Fee）

**情境**
- 買方無故終止
- 賣方接受更好 offer（Go-Shop）
- 主管機關否決（Reverse Break Fee）

**金額**：交易金額 1–5%

## 第七部分：爭議解決

### 仲裁 vs. 訴訟

**仲裁優勢**
- 保密
- 程序彈性
- 國際認可（New York Convention）
- 終局性

**仲裁機構**
- 跨境：SIAC（新加坡）、HKIAC（香港）、ICC（巴黎）
- 台灣：中華民國仲裁協會
- 選擇考量：中立性、雙方律師熟悉度、成本

### 管轄法律

**常見選擇**
- 跨境：新加坡法、英國法、紐約州法
- 國內：台灣法

**選擇考量**
- 法律成熟度
- 雙方熟悉度
- M&A 判例豐富度

## 常見談判重點

### 對價相關
- Working Capital Target 定義
- Net Debt 細項
- Earn-out 指標與公式
- Escrow 金額與期限

### R&W 相關
- 時效長短
- Cap 金額
- 特別保證範圍
- 知悉基準（Knowledge Qualifier）

### 賠償相關
- Basket 類型（Tipping vs. Deductible）
- De Minimis 金額
- Defense 控制權（誰主導訴訟）

### 先決條件相關
- MAC 定義
- 主管機關範圍
- 時限（Outside Date）
- 第三方同意範圍

## R&W 保險（R&W Insurance）

### 功能

- 取代或補強賣方賠償
- 降低 Escrow 金額
- 降低買賣雙方摩擦
- 延長時效

### 成本

- 保費：交易金額 2–4%
- 上限：通常 10–20% 交易金額
- Retention（自付額）：交易金額 0.5–1%

### 近年趨勢

- 大型交易標配
- 台灣案量快速增加
- 保險公司對 DD 要求高
