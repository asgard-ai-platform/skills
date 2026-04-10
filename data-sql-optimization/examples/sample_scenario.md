# Example: 電商訂單儀表板查詢從 28 秒優化至 180ms

## Scenario

**公司**: Shophere（台灣中型電商平台，月活躍用戶 80 萬）

**問題描述**:
> 「我們的後台訂單報表頁面，每次打開要等 28 秒。這個頁面讓運營團隊查近 30 天的訂單，按狀態、買家、金額篩選。DB 是 PostgreSQL 14，orders 表大概 1,200 萬筆。請幫我優化。」

**原始查詢**:
```sql
SELECT 
  o.id,
  o.created_at,
  o.status,
  o.total_amount,
  u.name AS buyer_name,
  u.email AS buyer_email,
  COUNT(oi.id) AS item_count,
  SUM(oi.quantity) AS total_qty
FROM orders o
LEFT JOIN users u ON u.id = o.user_id
LEFT JOIN order_items oi ON oi.order_id = o.id
WHERE 
  YEAR(o.created_at) = 2024 
  AND MONTH(o.created_at) >= 10
  AND o.status IN ('paid', 'shipped', 'completed')
GROUP BY o.id, o.created_at, o.status, o.total_amount, u.name, u.email
ORDER BY o.created_at DESC;
```

---

## Analysis

### Step 1: EXPLAIN ANALYZE 輸出（節錄）

```
Sort  (cost=2847291.44..2850181.44 rows=1156000 width=148)
      (actual time=27843.221..28012.344 rows=423817 loops=1)
  Sort Key: o.created_at DESC
  Sort Method: external merge  Disk: 68432kB
  ->  Hash Join  (cost=284721.00..1923847.22 rows=1156000 width=148)
        (actual time=4821.332..26433.119 rows=423817 loops=1)
      Hash Cond: (oi.order_id = o.id)
      ->  Seq Scan on order_items oi  
            (cost=0.00..421832.00 rows=8436640 width=24)
            (actual time=0.021..3241.882 rows=8436640 loops=1)
      ->  Hash  (cost=248932.00..248932.00 rows=1156000 width=124)
            (actual time=4713.442..4713.443 rows=423817 loops=1)
          ->  Hash Join  (cost=84321.00..248932.00 rows=1156000 width=124)
              ->  Seq Scan on orders o
                    (cost=0.00..142832.00 rows=1156000 width=72)
                    (actual time=0.034..2841.221 rows=1156000 loops=1)
                    Filter: ((status IN ('paid','shipped','completed'))
                             AND (YEAR(created_at) = 2024)
                             AND (MONTH(created_at) >= 10))
                    Rows Removed by Filter: 11044183
              ->  Seq Scan on users u ...
```

### Step 2: 找出瓶頸

| 問題 | 細節 |
|------|------|
| **orders 全表掃描** | `YEAR(created_at)` 包裹函數，讓 index 無法使用，掃 1,200 萬筆後篩掉 1,104 萬 |
| **order_items 全表掃描** | 沒有 `order_id` 的 index，843 萬筆全掃 |
| **磁碟排序** | 結果集 42 萬筆 + GROUP BY，記憶體不夠，溢出到磁碟（68MB） |
| **SELECT \* 概念** | 雖然有指定欄位，但 JOIN users 讀了整個 user row，只用到 name/email |

### Step 3: 修正

**Fix 1 — 移除日期欄位上的函數包裝**

```sql
-- 原本（無法用 index）
WHERE YEAR(o.created_at) = 2024 AND MONTH(o.created_at) >= 10

-- 改為範圍條件（可用 index）
WHERE o.created_at >= '2024-10-01' AND o.created_at < '2025-01-01'
```

**Fix 2 — 建立 Composite Index（orders）**

```sql
-- 最常用的篩選：status + created_at（status 基數低但最先過濾）
CREATE INDEX idx_orders_status_created 
ON orders (status, created_at DESC)
WHERE status IN ('paid', 'shipped', 'completed');  -- Partial index

-- 執行時間: ~800ms（建 index，一次性成本）
```

**Fix 3 — 建立 order_items.order_id Index**

```sql
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
-- 已有 FK 通常自動建，但此環境未建
```

**Fix 4 — 改寫查詢，移除 GROUP BY 膨脹**

```sql
SELECT 
  o.id,
  o.created_at,
  o.status,
  o.total_amount,
  u.name   AS buyer_name,
  u.email  AS buyer_email,
  oi.item_count,
  oi.total_qty
FROM orders o
JOIN users u ON u.id = o.user_id
JOIN (
  SELECT order_id, COUNT(*) AS item_count, SUM(quantity) AS total_qty
  FROM order_items
  GROUP BY order_id
) oi ON oi.order_id = o.id
WHERE 
  o.created_at >= '2024-10-01' 
  AND o.created_at < '2025-01-01'
  AND o.status IN ('paid', 'shipped', 'completed')
ORDER BY o.created_at DESC
LIMIT 500 OFFSET 0;
```

> 補加 `LIMIT 500` — 原查詢一次撈 42 萬筆，前端只顯示 50 筆/頁，這是 Missing Pagination 問題。

### Step 4: 驗證 EXPLAIN ANALYZE

```
Limit  (cost=1243.82..1488.34 rows=500 width=148)
       (actual time=178.443..180.221 rows=500 loops=1)
  ->  Sort  (cost=1243.82..2487.64 rows=497528 width=148)
            (actual time=178.221..178.883 rows=500 loops=1)
      Sort Method: top-N heapsort  Memory: 198kB
      ->  Hash Join  (cost=83421.00..124832.00 rows=423817 width=148)
            (actual time=24.332..142.119 rows=423817 loops=1)
          ->  Index Scan using idx_orders_status_created on orders o
                (actual time=0.043..84.221 rows=423817 loops=1)
                Index Cond: (status IN ('paid','shipped','completed')
                             AND created_at >= '2024-10-01'
                             AND created_at < '2025-01-01')
          ->  HashAggregate on order_items subquery
                (actual time=18.441..19.332 rows=423817 loops=1)
                  ->  Index Scan using idx_order_items_order_id
```

---

## Result

```markdown
# Query Optimization: Shophere 訂單報表儀表板

## Slow Query
```sql
SELECT o.id, o.created_at, o.status, o.total_amount,
       u.name, u.email, COUNT(oi.id), SUM(oi.quantity)
FROM orders o
LEFT JOIN users u ON u.id = o.user_id
LEFT JOIN order_items oi ON oi.order_id = o.id
WHERE YEAR(o.created_at) = 2024 AND MONTH(o.created_at) >= 10
  AND o.status IN ('paid', 'shipped', 'completed')
GROUP BY o.id, ...
ORDER BY o.created_at DESC;
```
- Execution time: 28,012ms
- Rows scanned: orders 12,000,000 / order_items 8,436,640（全表）
- Problem: `YEAR()`/`MONTH()` 函數包裹導致 index 失效；order_items 缺 FK index；無分頁一次撈 42 萬筆

## Fix Applied
1. 將日期條件改為範圍比較（移除函數包裹）
2. 建立 `idx_orders_status_created` Partial Composite Index
3. 建立 `idx_order_items_order_id` Index
4. 查詢加上 `LIMIT 500 OFFSET 0`（配合前端分頁）
5. order_items 聚合移至子查詢，避免 GROUP BY 擴展到 orders + users 所有欄位

## Result
- Execution time: 28,012ms → 180ms（**99.4% 改善**）
- Rows scanned: 20,436,640 → 423,817（orders index scan）+ 相關 order_items
- 磁碟排序消除（Top-N heapsort，記憶體 198kB）
- 寫入成本影響：新增 2 個 index，INSERT/UPDATE 稍有額外成本，可於離峰建立
```
