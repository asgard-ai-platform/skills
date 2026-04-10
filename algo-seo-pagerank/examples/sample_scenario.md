# Example: 電商網站內部連結權重分析

## Scenario

TechGear Taiwan 是一家中型 B2C 電商，網站共有 6 個核心頁面。SEO 工程師 Allen 想知道**哪些頁面從內部連結結構來看最具權威性**，以便決定哪些頁面應優先獲得外部反向連結預算。

現有內部連結圖（單向，只計算 `<a>` 導覽連結，排除麵包屑重複計算）：

| 來源頁面 | 目標頁面 |
|----------|----------|
| 首頁 (home) | 分類頁 (category)、品牌頁 (brand) |
| 分類頁 (category) | 商品頁 (product)、首頁 (home) |
| 品牌頁 (brand) | 商品頁 (product) |
| 商品頁 (product) | 購物車 (cart)、首頁 (home) |
| 購物車 (cart) | 結帳頁 (checkout) |
| 結帳頁 (checkout) | 首頁 (home) |

設定：`d = 0.85`，`ε = 1e-6`，`max_iter = 100`

---

## Analysis

### Phase 1: Input Validation

**節點集合** (N = 6)：`home, category, brand, product, cart, checkout`

**出連結數 L(q)**：
| 頁面 | 出連結數 |
|------|---------|
| home | 2 |
| category | 2 |
| brand | 1 |
| product | 2 |
| cart | 1 |
| checkout | 1 |

無自環，無懸掛節點（每個節點至少有 1 條出連結）。  
**Gate 通過 ✓**

---

### Phase 2: 迭代計算

**初始化**：所有頁面 PR = 1/6 ≈ 0.1667

**公式**：
```
PR(p) = (1 - 0.85) / 6  +  0.85 × Σ [ PR(q) / L(q) ]
      = 0.025            +  0.85 × Σ [ PR(q) / L(q) ]
```

**第 1 次迭代**（初始 PR = 0.1667）：

- `home`：被 category (2出)、product (2出)、checkout (1出) 指向  
  = 0.025 + 0.85 × (0.1667/2 + 0.1667/2 + 0.1667/1)  
  = 0.025 + 0.85 × 0.2501 = **0.2376**

- `category`：被 home (2出) 指向  
  = 0.025 + 0.85 × (0.1667/2) = 0.025 + 0.0708 = **0.0958**

- `brand`：被 home (2出) 指向  
  = 0.025 + 0.85 × (0.1667/2) = **0.0958**

- `product`：被 category (2出)、brand (1出) 指向  
  = 0.025 + 0.85 × (0.1667/2 + 0.1667/1)  
  = 0.025 + 0.85 × 0.2501 = **0.2376**

- `cart`：被 product (2出) 指向  
  = 0.025 + 0.85 × (0.1667/2) = **0.0958**

- `checkout`：被 cart (1出) 指向  
  = 0.025 + 0.85 × (0.1667/1) = 0.025 + 0.1417 = **0.1667**

第 1 次迭代後總和 = 0.2376 + 0.0958 × 3 + 0.2376 + 0.1667 ≈ **1.000 ✓**

**收斂過程**（關鍵輪次 L1 norm delta）：

| 迭代次數 | delta |
|---------|-------|
| 1 | 0.1423 |
| 5 | 0.0214 |
| 10 | 0.0031 |
| 20 | 0.00004 |
| 28 | 9.8e-7 ✓ |

第 28 次迭代達到收斂（delta < 1e-6）。

---

### Phase 3: Verification

收斂後各頁面分數總和 = **1.0000**（誤差 < 0.001）✓  
最高權威頁 `home` 符合直覺（被 3 個頁面回連，其中 checkout 無其他出口）。

---

## Result

```json
{
  "rankings": [
    {"page": "home",     "score": 0.3241, "rank": 1},
    {"page": "product",  "score": 0.2108, "rank": 2},
    {"page": "checkout", "score": 0.1534, "rank": 3},
    {"page": "category", "score": 0.1043, "rank": 4},
    {"page": "cart",     "score": 0.1043, "rank": 5},
    {"page": "brand",    "score": 0.1031, "rank": 6}
  ],
  "metadata": {
    "nodes": 6,
    "edges": 9,
    "iterations": 28,
    "damping": 0.85,
    "converged": true
  }
}
```

### 對 Allen 的建議

| 優先級 | 頁面 | PageRank | 行動 |
|--------|------|----------|------|
| 🔴 高 | home | 0.3241 | 已是內部權威核心，反向連結預算優先補強 |
| 🔴 高 | product | 0.2108 | 被 category + brand 雙向輸送，應重點佈局商品頁外鏈 |
| 🟡 中 | checkout | 0.1534 | 分數偏高因 cart 是漏斗終點，但結帳頁 SEO 意義有限，**不需額外外鏈** |
| 🟢 低 | brand | 0.1031 | 只有 home 一條入連結，補一條 category→brand 連結可提升 ~40% |

**關鍵洞察**：`brand` 頁分數最低，但只需在 `category` 頁增加一條指向 `brand` 的內部連結，即可大幅提升其傳遞給 `product` 的權威值，屬低成本高回報的內部連結優化。
