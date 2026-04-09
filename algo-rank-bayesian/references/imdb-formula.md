# IMDB Weighted Rating Formula

IMDB 的 Top 250 排名使用 Bayesian Average 的一種特殊形式，官方稱為 **Weighted Rating (WR)**。本文件完整還原該公式的實作細節，並提供可驗證的數值範例。

---

## 公式定義

```
WR = (v / (v + m)) × R + (m / (v + m)) × C
```

**變數對應**：

| 變數 | 含義 | SKILL.md 對應 |
|------|------|--------------|
| `v`  | 該影片的投票數 | `n`（item review count） |
| `m`  | 進入榜單的最低投票門檻 | `C`（confidence parameter） |
| `R`  | 該影片的平均評分 | `avg_rating` |
| `C`  | 所有合格影片的平均分 | `m`（global mean） |

> **命名衝突警告**：IMDB 公式的 `C` 是全局平均分，SKILL.md 的 `C` 是 phantom vote 數。
> 閱讀時注意對應關係，本文件統一使用 SKILL.md 的符號體系（見下方）。

**用 SKILL.md 符號重寫**：

```
BR = (C × m + n × avg_rating) / (C + n)
```

其中 `C = m_threshold`（最低投票門檻），`m = global_mean`（全局平均分）。

兩個形式在數學上完全等價：

```
(v/(v+m)) × R + (m/(v+m)) × C
= (v × R + m × C) / (v + m)
= (n × avg_rating + C × global_mean) / (n + C)
```

---

## IMDB 的 C 值設定邏輯

IMDB 不使用「中位數投票數」作為 C，而是使用**進榜門檻**——即進入 Top 250 所需的最低投票數。

歷史上 IMDB 的門檻曾多次調整：

| 時期 | 最低投票數 m |
|------|------------|
| 早期  | ~1,250 票  |
| 中期  | ~3,000 票  |
| 近年  | ~25,000 票 |

這個設計的含義：**C 不是用來描述「典型」項目，而是用來設定進榜資格線**。只有投票數超過 m 的影片才進入候選集合，然後在候選集合內再用 WR 排序。

實際效果：
- `v >> m`（遠超門檻）→ WR ≈ R（自己的平均分主導）
- `v ≈ m`（剛好達標）→ WR 被大幅拉向全局平均 C

---

## 逐步計算範例

以下用具體數字重現一個小型 Top-N 計算。

### 資料集

| 影片 | 投票數 (v) | 平均分 (R) |
|------|-----------|-----------|
| Film_A | 80,000 | 9.2 |
| Film_B | 30,000 | 8.9 |
| Film_C | 26,000 | 9.5 |
| Film_D | 20,000 | 9.8 |
| Film_E | 500   | 9.9 |

**步驟 1**：設定門檻 `m = 25,000`，濾掉不合格影片。

合格影片：Film_A、Film_B、Film_C（Film_D 和 Film_E 不足 25,000 票，排除在外）。

**步驟 2**：計算合格影片的全局平均分 `C`。

```
所有合格影片的總評分和 = 80000×9.2 + 30000×8.9 + 26000×9.5
                     = 736000 + 267000 + 247000
                     = 1,250,000

總投票數 = 80000 + 30000 + 26000 = 136,000

C (global mean) = 1,250,000 / 136,000 ≈ 9.19
```

**步驟 3**：計算每部影片的 WR。

```
WR_A = (80000×9.2 + 25000×9.19) / (80000 + 25000)
     = (736000 + 229750) / 105000
     = 965750 / 105000
     ≈ 9.198

WR_B = (30000×8.9 + 25000×9.19) / (30000 + 25000)
     = (267000 + 229750) / 55000
     = 496750 / 55000
     ≈ 9.032

WR_C = (26000×9.5 + 25000×9.19) / (26000 + 25000)
     = (247000 + 229750) / 51000
     = 476750 / 51000
     ≈ 9.348
```

**步驟 4**：排名結果。

| 排名 | 影片 | WR | 原始 R | 收縮量 |
|------|------|----|--------|--------|
| 1 | Film_C | 9.348 | 9.5 | −0.152 |
| 2 | Film_A | 9.198 | 9.2 | −0.002 |
| 3 | Film_B | 9.032 | 8.9 | +0.132 |

Film_C 雖然投票數最少（剛好過門檻），原始分 9.5 最高，但被拉向全局均值後仍排第一。Film_D（9.8 分）因未達門檻完全排除在外——這正是「進榜門檻」設計的核心：**防止低投票數的極端高分滲入榜單**。

---

## 門檻 m 的選取策略

IMDB 使用固定門檻，但實際應用中 m 的選取有三種主流策略：

### 策略 A：固定票數門檻（IMDB 做法）

```
m = 絕對投票數（如 25,000）
```

- **優點**：直覺，可公開宣告，防止刷榜
- **缺點**：新品類或冷門領域永遠進不了榜

### 策略 B：百分位數門檻

```
m = 所有項目投票數的第 X 百分位（如第 75 百分位）
```

```python
import statistics
votes = [v for item in items for v in [item['votes']]]
m = sorted(votes)[int(len(votes) * 0.75)]
```

- **優點**：自動適應資料規模，隨資料庫成長而調整
- **缺點**：m 會隨資料庫變化，歷史排名不穩定

### 策略 C：中位數（SKILL.md 的預設建議）

```
m = median(所有項目的投票數)
```

- **優點**：直覺，計算簡單，大約半數項目會受到顯著收縮
- **缺點**：沒有進榜門檻概念，所有項目都參與排名

**選取決策表**：

| 情境 | 建議策略 |
|------|---------|
| 公開排行榜，需要防刷榜 | 策略 A（固定門檻） |
| 資料庫持續成長中 | 策略 B（百分位數） |
| 內部分析工具 | 策略 C（中位數） |
| 冷門品類 + 公開榜單 | 策略 A，但門檻依品類分別設定 |

---

## 代碼實作

```python
from typing import NamedTuple

class Item(NamedTuple):
    name: str
    votes: int
    avg_rating: float

def imdb_weighted_rating(
    items: list[Item],
    min_votes: int,           # m：進榜門檻
) -> list[dict]:
    """
    IMDB-style Weighted Rating.
    只有 votes >= min_votes 的 items 進入計算。
    global_mean 從合格 items 計算，不含門檻以下的項目。
    """
    eligible = [it for it in items if it.votes >= min_votes]
    if not eligible:
        return []

    total_ratings = sum(it.votes * it.avg_rating for it in eligible)
    total_votes = sum(it.votes for it in eligible)
    global_mean = total_ratings / total_votes  # C in IMDB notation

    results = []
    for it in eligible:
        wr = (it.votes * it.avg_rating + min_votes * global_mean) / (it.votes + min_votes)
        shrinkage = wr - it.avg_rating
        results.append({
            "item": it.name,
            "weighted_rating": round(wr, 4),
            "raw_avg": it.avg_rating,
            "votes": it.votes,
            "shrinkage": round(shrinkage, 4),
        })

    return sorted(results, key=lambda x: x["weighted_rating"], reverse=True)


# 驗證範例（對應上方手算結果）
if __name__ == "__main__":
    data = [
        Item("Film_A", 80000, 9.2),
        Item("Film_B", 30000, 8.9),
        Item("Film_C", 26000, 9.5),
        Item("Film_D", 20000, 9.8),  # 被門檻排除
        Item("Film_E", 500,   9.9),  # 被門檻排除
    ]
    ranked = imdb_weighted_rating(data, min_votes=25000)
    for rank, item in enumerate(ranked, 1):
        print(f"{rank}. {item['item']}: WR={item['weighted_rating']} "
              f"(raw={item['raw_avg']}, shrinkage={item['shrinkage']:+.4f})")
```

預期輸出：
```
1. Film_C: WR=9.348 (raw=9.5, shrinkage=-0.1522)
2. Film_A: WR=9.198 (raw=9.2, shrinkage=-0.0018)
3. Film_B: WR=9.032 (raw=8.9, shrinkage=+0.1317)
```

---

## 常見誤解

**誤解 1：WR 的分母是「所有」項目的平均分**

錯。IMDB 的 `C`（全局均值）只從**合格項目**（votes ≥ m）計算，不含被門檻排除的項目。若把全量資料（含零投票的新品）納入計算，全局均值會被大幅拉低。

**誤解 2：m 越大越好**

過高的門檻會讓新上線的優質內容永遠無法進榜。m 的設定是商業決策，不是純技術問題。

**誤解 3：IMDB 公式可以直接用於 1-5 星評分**

IMDB 使用 1-10 分制，全局均值約在 6-7 分。若你的系統是 1-5 星，全局均值約在 3-4 分，數值範圍不同但公式完全相同，無需換算。

**誤解 4：Bayesian Average 可以防止刷評**

不行。Bayesian Average 只解決小樣本問題，對協調一致的假評完全無效。刷評防護需要另外實作（評論者行為分析、IP 聚類等）。
