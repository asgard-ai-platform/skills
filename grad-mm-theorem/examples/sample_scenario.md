# Example: CloudMesh 槓桿重組決策分析

## Scenario

CloudMesh Inc. 是一家 B2B SaaS 公司，專注於企業雲端資源管理，年收入 $180M，EBITDA $54M（margin 30%）。目前資本結構為全股本融資，企業估值 $810M（約 15x EBITDA）。

CFO 正在評估是否發行 $200M 長期債券（利率 5.5%），所得資金用於股票回購。他的問題：

> 「我們的競爭對手 NetStack 的 D/E 是 0.8x，我們是 0。投資銀行說加槓桿可以提升每股價值，但 board 擔心財務風險。資本結構真的重要嗎？我們的最佳槓桿比率是多少？」

**公司背景：**
- 企業所得稅率 Tc = 21%
- 無息負債（unlevered）成本 R0 = 9.2%
- 現有股本 $810M，無負債（D = 0）
- EBITDA 波動性低（SaaS 訂閱模式，NRR 118%）
- 未動用現金 $95M，FCF yield 穩定

---

## Analysis

### Step 1 — State MM Propositions

**基準情境（無稅 MM）：**

若市場完美，VL = VU，融資決策不影響企業價值。CloudMesh 加 $200M 債不會改變 $810M 的企業價值，每股價值不變。

**引入稅盾（MM 1963）：**

VL = VU + Tc × D

若假設 $200M 為永久債務：

```
VL = $810M + 0.21 × $200M
VL = $810M + $42M
VL = $852M
```

稅盾淨增值：**$42M**，約佔當前企業價值的 **5.2%**。

**Proposition II — 加槓桿後的股本成本：**

```
Re = R0 + (D/E)(R0 - Rd)
Re = 9.2% + (200/652)(9.2% - 5.5%)
Re = 9.2% + 0.307 × 3.7%
Re = 9.2% + 1.14%
Re ≈ 10.34%
```

股本成本從 9.2% 升至 10.34%，反映財務槓桿風險。

---

### Step 2 — Identify Market Imperfections

| 市場不完美項目 | 對 CloudMesh 的評估 | 量級 | 方向 |
|---|---|---|---|
| 企業稅盾 | Tc=21%，$200M 永久債，PV=$42M | 中 | 有利於舉債 |
| 破產成本 | SaaS 訂閱模式，客戶黏性高，NRR 118%，財務困境觸發門檻遠 | 低 | 有利於股本 |
| 代理成本 | FCF 豐沛、未動用現金 $95M；Jensen(1986) 指出債務有紀律效果 | 低-中 | 有利於舉債 |
| 資訊不對稱 | 公開上市公司，分析師覆蓋充分；pecking order 效應較弱 | 低 | 中性 |
| 個人稅（Miller 1977） | 美國股東稅率參差，部分抵銷企業稅盾 | 低-中 | 削減稅盾優勢 |

**主要結論：** CloudMesh 的市場不完美以「稅盾優勢」為主，破產成本極低，代理成本適中。淨效果偏向適度舉債。

---

### Step 3 — Tradeoff Framework

財務困境成本估計：

- 學術研究顯示財務困境成本約為企業價值的 10-20%
- CloudMesh 若企業價值 $852M，財務困境成本上限約 $85-170M
- 現有 EBITDA $54M，利息覆蓋率（ICR）= 54 / (200 × 5.5%) = 54 / 11 = **4.9x**（健康水位，通常 ≥ 3x 即安全）

邊際稅盾效益 vs 邊際破產成本：

```
負債水位     稅盾 PV    財務困境 PV（估）    淨效益
$0M         $0M        $0M                  $0M
$100M       $21M       ~$3M                 +$18M
$200M       $42M       ~$8M                 +$34M  ← 建議範圍
$350M       $74M       ~$30M                +$44M
$500M       $105M      ~$75M                +$30M  ← 效益遞減
$650M       $137M      ~$145M               -$8M   ← 超越最適點
```

最適負債估計落在 $200–$350M 之間。

---

### Step 4 — Compute WACC Impact

**現狀（全股本）：**

```
WACC = (E/V)Re = 100% × 9.2% = 9.20%
```

**加 $200M 債後（VL = $852M）：**

```
E = $852M - $200M = $652M
D/V = 200/852 = 23.5%
E/V = 652/852 = 76.5%

WACC = (0.765 × 10.34%) + (0.235 × 5.5% × (1-0.21))
WACC = 7.91% + (0.235 × 4.345%)
WACC = 7.91% + 1.02%
WACC = 8.93%
```

WACC 從 9.20% 降至 **8.93%**，下降 27 bps。以 $810M 企業價值計算，等同提升估值約 3-4%（粗估）。

---

## Result

## Capital Structure Analysis: CloudMesh Inc.

### Current Structure
| Metric | Value |
|--------|-------|
| Debt (D) | $0M |
| Equity (E) | $810M |
| D/E Ratio | 0.00x |
| WACC | 9.20% |

### Post-Recap Structure (proposed)
| Metric | Value |
|--------|-------|
| Debt (D) | $200M |
| Equity (E) | $652M |
| D/E Ratio | 0.31x |
| WACC | 8.93% |
| Tax Shield PV | +$42M |
| Estimated Distress Cost PV | ~$8M |
| Net Value Created | **+$34M** |

### MM Imperfections Present
| Imperfection | Magnitude | Direction |
|-------------|-----------|-----------|
| Tax shield (Tc=21%, perpetual $200M) | Medium — $42M PV | Favors debt |
| Bankruptcy costs (SaaS, NRR 118%, ICR 4.9x) | Low — ~$8M PV | Favors equity |
| Agency costs (FCF discipline) | Low-Medium | Marginally favors debt |
| Information asymmetry | Low | Neutral |

### Recommendation

**建議採行 $200M 股票回購融資方案。**

1. 稅盾效益明確可量化（$42M），而 CloudMesh 的訂閱模式使財務困境成本極低（估 $8M），淨效益約 **+$34M**。
2. 利息覆蓋率 4.9x 遠高於安全門檻，D/E 0.31x 在 SaaS 同業屬保守。NetStack 0.8x D/E 不能直接類比，須確認其 EBITDA 波動性。
3. **Gotcha 提醒：** Tc × D = $42M 假設負債永久存在；若 CloudMesh 計劃 5 年後贖回，實際稅盾 PV 需折現，約降至 $28–32M，仍為正值。
4. 個人稅（Miller 1977）可能削減 20-30% 的稅盾優勢，但不改變方向性結論。
5. 建議上限為 $300–350M 負債（D/E ≈ 0.45x），超過此水位邊際破產成本開始加速，WACC 效益遞減。
