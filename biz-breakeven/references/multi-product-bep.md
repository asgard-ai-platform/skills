# Multi-Product Break-Even Analysis

多產品損益平衡比單一產品複雜，因為不同產品有不同的售價、變動成本與銷售比例。核心問題是：**哪個產品的 Contribution Margin 要用來除固定成本？**

答案是：加權平均 CM（Weighted-Average Contribution Margin）。

---

## 兩種計算路徑

### 路徑一：加權平均 CM per Unit（已知銷售組合比例）

適用於能以「單位」計算的產品（杯、件、個），且銷售組合穩定。

**公式：**

```
Weighted CM per Unit = Σ (CM_i × Sales Mix %_i)
BEP Total Units = Fixed Costs / Weighted CM per Unit
BEP Units for Product i = BEP Total Units × Sales Mix %_i
```

### 路徑二：加權平均 CM Ratio（多產品、單位不同質時）

適用於產品無法統一計量（例如同時賣月費訂閱與單次服務），以「收入」為共同基礎。

**公式：**

```
Weighted CM Ratio = Σ (CM Ratio_i × Revenue Mix %_i)
BEP Revenue = Fixed Costs / Weighted CM Ratio
BEP Revenue for Product i = BEP Revenue × Revenue Mix %_i
```

---

## 完整試算：手搖飲料店（三款產品）

**情境：** 一家飲料店同時賣珍珠奶茶、多肉葡萄、檸檬水。每月固定成本 NT$210,000。

### Step 1：整理單品成本結構

| 產品 | 售價 | 變動成本 | CM/杯 | CM Ratio |
|------|------|----------|-------|----------|
| 珍珠奶茶 | NT$65 | NT$28 | NT$37 | 56.9% |
| 多肉葡萄 | NT$75 | NT$35 | NT$40 | 53.3% |
| 檸檬水 | NT$45 | NT$15 | NT$30 | 66.7% |

### Step 2：確認銷售組合（Sales Mix）

根據 POS 歷史資料，三款產品的銷量比例：

| 產品 | 銷量比例（Unit Mix） | 收入比例（Revenue Mix） |
|------|---------------------|------------------------|
| 珍珠奶茶 | 50% | 47.5% |
| 多肉葡萄 | 30% | 32.8% |
| 檸檬水 | 20% | 13.1% |

> **注意**：Unit Mix ≠ Revenue Mix，因為各產品售價不同。若要用路徑二，必須用 Revenue Mix，不可誤用 Unit Mix。

### Step 3a：路徑一計算（以單位為基礎）

```
Weighted CM per Unit
= (37 × 50%) + (40 × 30%) + (30 × 20%)
= 18.5 + 12.0 + 6.0
= NT$36.5 / 杯

BEP Total Units = 210,000 / 36.5 = 5,753 杯/月

BEP by Product:
- 珍珠奶茶：5,753 × 50% = 2,877 杯
- 多肉葡萄：5,753 × 30% = 1,726 杯
- 檸檬水：  5,753 × 20% = 1,151 杯
```

### Step 3b：驗算收入是否自洽

```
BEP Revenue
= (2,877 × 65) + (1,726 × 75) + (1,151 × 45)
= 186,990 + 129,450 + 51,795
= NT$368,235 / 月
```

### Step 4：Margin of Safety

若當月實際銷售 7,000 杯（假設相同組合）：

```
Actual Revenue = (3,500 × 65) + (2,100 × 75) + (1,400 × 45)
              = 227,500 + 157,500 + 63,000
              = NT$448,000

BEP Revenue = NT$368,235

Margin of Safety = (448,000 - 368,235) / 448,000 = 17.8%
```

---

## Sales Mix 變動分析

Sales Mix 變動是多產品損益平衡最容易被忽略的風險來源。若實際組合偏離假設，BEP 會跟著移動。

### 情境比較：組合往低 CM 產品傾斜

假設某月促銷檸檬水，Unit Mix 變為：珍珠奶茶 30%、多肉葡萄 20%、檸檬水 50%：

```
New Weighted CM = (37 × 30%) + (40 × 20%) + (30 × 50%)
               = 11.1 + 8.0 + 15.0
               = NT$34.1 / 杯

New BEP = 210,000 / 34.1 = 6,158 杯/月（↑ 405 杯）
```

即使總銷量不變，因為組合移向低 CM 產品，損益平衡點上升 7%。

### 決策表：Mix 偏移的影響方向

| 組合移向 | Weighted CM | BEP Units | 獲利影響 |
|----------|-------------|-----------|----------|
| 高 CM 產品 | ↑ | ↓ | 正面 |
| 低 CM 產品 | ↓ | ↑ | 負面 |
| CM 相近產品 | 持平 | 持平 | 中性 |

---

## 三產品以上：用表格展開計算

當產品超過三種，手算容易出錯。建議用欄位展開法：

```
Product  | Price | VarCost | CM   | UnitMix | Weighted CM
---------|-------|---------|------|---------|------------
A        | 65    | 28      | 37   | 0.50    | 18.50
B        | 75    | 35      | 40   | 0.30    | 12.00
C        | 45    | 15      | 30   | 0.20    |  6.00
---------|-------|---------|------|---------|------------
TOTAL    |       |         |      | 1.00    | 36.50  ← BEP 除數

BEP = Fixed Costs / 36.50
```

---

## 不能用單一產品 BEP 各自計算再相加

這是最常見的錯誤。

### 為什麼不對？

若對每個產品分別計算 BEP，再把結果加總：

```
BEP_A = 210,000 / 37 = 5,676 杯  ← 假設全部固定成本都要由 A 蓋掉
BEP_B = 210,000 / 40 = 5,250 杯  ← 同上，但固定成本被重複計算
BEP_C = 210,000 / 30 = 7,000 杯
Total = 17,926 杯  ← 嚴重高估，因固定成本被算了三次
```

**固定成本只有一份，必須由所有產品共同分攤。** 正確做法是用加權 CM 計算總 BEP，再按組合比例拆分。

---

## 固定成本可歸屬時：直接產品損益（Product-Line P&L）

若部分固定成本可直接歸屬到特定產品線（例如：某產線的專用設備折舊），可進一步計算**每條產品線的損益平衡**：

```
Product-Line BEP Units_i = Direct Fixed Costs_i / CM_i
```

共用固定成本（房租、管理薪資）仍需加權攤分，或以整體層級計算。

**警告**：這種拆法需要可靠的成本歸屬，若歸屬武斷，反而比加權法更不準確。除非有完整的 Activity-Based Costing 支撐，否則共用成本不要強行拆分。

---

## Python 試算片段

以下片段可直接在 `scripts/breakeven.py` 的 `compute()` 擴充，或獨立執行：

```python
def multi_product_bep(fixed_costs: float, products: list[dict]) -> dict:
    """
    products: list of {name, price, variable_cost, unit_mix}
    unit_mix values must sum to 1.0
    """
    assert abs(sum(p["unit_mix"] for p in products) - 1.0) < 1e-9, \
        "unit_mix must sum to 1.0"

    for p in products:
        p["cm"] = p["price"] - p["variable_cost"]
        p["cm_ratio"] = p["cm"] / p["price"]
        p["weighted_cm"] = p["cm"] * p["unit_mix"]

    weighted_cm = sum(p["weighted_cm"] for p in products)
    bep_units = fixed_costs / weighted_cm

    results = []
    for p in products:
        results.append({
            "name": p["name"],
            "bep_units": bep_units * p["unit_mix"],
            "bep_revenue": bep_units * p["unit_mix"] * p["price"],
            "cm": p["cm"],
            "cm_ratio": p["cm_ratio"],
        })

    return {
        "weighted_cm_per_unit": weighted_cm,
        "bep_total_units": bep_units,
        "bep_total_revenue": sum(r["bep_revenue"] for r in results),
        "products": results,
    }


# 使用範例
if __name__ == "__main__":
    result = multi_product_bep(
        fixed_costs=210_000,
        products=[
            {"name": "珍珠奶茶", "price": 65, "variable_cost": 28, "unit_mix": 0.50},
            {"name": "多肉葡萄", "price": 75, "variable_cost": 35, "unit_mix": 0.30},
            {"name": "檸檬水",   "price": 45, "variable_cost": 15, "unit_mix": 0.20},
        ]
    )
    import json
    print(json.dumps(result, ensure_ascii=False, indent=2))
```

**預期輸出（節錄）：**

```json
{
  "weighted_cm_per_unit": 36.5,
  "bep_total_units": 5753.42,
  "bep_total_revenue": 368219.18,
  "products": [
    {"name": "珍珠奶茶", "bep_units": 2876.71, "bep_revenue": 186986.30, ...},
    {"name": "多肉葡萄", "bep_units": 1726.03, "bep_revenue": 129452.05, ...},
    {"name": "檸檬水",   "bep_units":  1150.68, "bep_revenue":  51780.82, ...}
  ]
}
```

---

## 常見陷阱

**陷阱一：用歷史平均 Mix 套用於促銷期**
促銷活動通常改變 Sales Mix。促銷前應先估計新 Mix，重新計算 BEP，而非沿用平常數字。

**陷阱二：Revenue Mix 與 Unit Mix 混用**
路徑一（加權 CM/Unit）需用 Unit Mix；路徑二（加權 CM Ratio）需用 Revenue Mix。混用會算出錯誤的加權值。

**陷阱三：新品上市時 Mix 尚未穩定**
新產品的銷售比例在初期波動大。此時 BEP 應做敏感度分析（Mix 在合理範圍內變動時，BEP 的上下界），而非用單一 Mix 假設。

**陷阱四：把季節性波動當成 Mix 變動**
有時不是 Mix 變了，而是某產品的絕對需求有季節性。需先釐清是結構性 Mix 改變還是季節波動，才能決定要不要調整固定成本假設。
