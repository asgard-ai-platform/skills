# Example: 外送平台手續費戰爭

## Scenario

**FoodRocket** 與 **MealGo** 是台灣市占率最高的兩大外送平台，各佔約 40% 市場。雙方近期都在考慮是否調降對餐廳的抽成比例（目前均為 30%），以搶奪更多餐廳加盟、擴大供給端優勢。

FoodRocket 策略長提問：

> 「MealGo 下週要開董事會，市場傳言他們在考慮把抽成砍到 25%。我們要不要搶先宣布？還是等他們動？這場抽成戰打下去對我們有利嗎？」

---

## Analysis

### Step 1 — 定義賽局要素

**Players**
- Player 1：FoodRocket
- Player 2：MealGo

**Strategies**（各有兩個選項）
- Hold：維持 30% 抽成
- Cut：調降至 25% 抽成

**Payoffs（月度營業利益，單位：百萬 NTD）**

抽成從 30% 降至 25%，每筆訂單讓利約 NT$15（以平均客單價 NT$300 估算）。目前 FoodRocket 月處理訂單 800 萬筆；MealGo 750 萬筆。

| 情境 | 餐廳加盟誘因 | FoodRocket 利潤 | MealGo 利潤 |
|------|------------|----------------|-------------|
| 雙方 Hold | 無差異，維持現狀 | 120 | 110 |
| FoodRocket Cut，MealGo Hold | FR 搶走 MealGo 約 15% 餐廳供給，訂單量+12%，但讓利壓縮毛利 | 105 | 75 |
| FoodRocket Hold，MealGo Cut | MG 搶走 FR 約 15% 餐廳，FR 訂單量-10% | 78 | 108 |
| 雙方 Cut | 餐廳無差異，市場回到原點，雙方同時承受讓利 | 88 | 80 |

### Step 2 — 建立 Payoff Matrix

|  | **MealGo: Hold** | **MealGo: Cut** |
|---|---|---|
| **FoodRocket: Hold** | (120, 110) | (78, 108) |
| **FoodRocket: Cut** | (105, 75) | **(88, 80)** |

### Step 3 — 尋找優勢策略

**FoodRocket 的最佳應對：**
- 若 MealGo Hold → FR Cut 得 105 vs Hold 得 120 → **Hold 優**
- 若 MealGo Cut → FR Cut 得 88 vs Hold 得 78 → **Cut 優**

FoodRocket **無絕對優勢策略**（best response 隨 MealGo 決策而變）。

**MealGo 的最佳應對：**
- 若 FR Hold → MG Cut 得 108 vs Hold 得 110 → **Hold 微優**
- 若 FR Cut → MG Cut 得 80 vs Hold 得 75 → **Cut 優**

MealGo 同樣**無絕對優勢策略**。

### Step 4 — 找出 Nash Equilibrium

逐格檢查：

| 格子 | FR 有誘因偏離？ | MG 有誘因偏離？ | NE？ |
|------|--------------|--------------|------|
| (Hold, Hold) = (120, 110) | 否（120 > 105） | 否（110 > 108） | **✓ NE** |
| (Cut, Hold) = (105, 75) | 是（切回 Hold 得 120） | — | ✗ |
| (Hold, Cut) = (78, 108) | 是（切到 Cut 得 88） | — | ✗ |
| (Cut, Cut) = (88, 80) | 是（切回 Hold 得 120，若 MG 不動） | 是（切回 Hold 得 110） | ✗（不穩定） |

> **Nash Equilibrium：(Hold, Hold) = (120, 110)**

這不是 Prisoner's Dilemma——雙方在此賽局中 **Hold 是協調均衡**，雙方都沒有單邊偏離的動機。

### Step 5 — Pareto 分析

(Hold, Hold) = (120, 110) 已是 Pareto 最優：沒有任何一種結果能讓其中一方更好而不損害另一方。

### Step 6 — 風險評估（Risk Dominance）

若 FoodRocket 誤判 MealGo 一定會 Cut（例如傳言屬實），則 FR 的最佳應對是 Cut（88 > 78）。此時會觸發 **(Cut, Cut)** 的次優均衡，雙方月利潤合計損失 62M NTD。

---

## Result

```markdown
# Game Theory Analysis: 外送平台抽成策略

## Game Setup
- Players: FoodRocket, MealGo
- Strategies: Hold（30%）/ Cut（25%）
- Type: 同步賽局（Simultaneous）

## Payoff Matrix

|  | MealGo: Hold | MealGo: Cut |
|---|---|---|
| FoodRocket: Hold | (120, 110) | (78, 108) |
| FoodRocket: Cut | (105, 75) | (88, 80) |

## Analysis
- 優勢策略：雙方均無絕對優勢策略
- Nash Equilibrium：(Hold, Hold) = (120, 110)
- Pareto 最優？是 — NE 已是最佳集體結果

## Strategic Implications

1. **FoodRocket 不應搶先降價**：NE 在 (Hold, Hold)，主動 Cut 只會讓利，
   除非 MealGo 確定會 Cut 才值得跟進。

2. **傳言是關鍵風險**：若市場誤信 MealGo 必然降價，可能引發
   自我實現的抽成戰，雙方滑入 (Cut, Cut) 次優均衡。

3. **應對建議**：
   - 觀望 48 小時，等待 MealGo 董事會結果
   - 若 MealGo 宣布 Cut，立即跟進（Cut 的 88 > Hold 的 78）
   - 主動放出「不打抽成戰」訊號，有助於穩定在 (Hold, Hold) 協調點
   - 長期：投資餐廳端非價格差異化（物流速度、數據工具），
     降低抽成比率作為競爭武器的有效性
```

**底線**：這場賽局的 NE 對 FoodRocket 有利——維持現狀即最優。真正的風險是**資訊不對稱與傳言**扭曲雙方的預期，把協調均衡推向抽成戰。策略長應優先管理市場預期，而非搶先出手。
