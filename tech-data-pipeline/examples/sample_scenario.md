# Example: E-Commerce Order Analytics Pipeline

## Scenario

**公司**: Kova Commerce — 台灣中型電商，月訂單量約 15 萬筆  
**提問者**: 後端工程師 Daniel，被 data team 要求提供每日訂單報表

> 「我們現在 data analyst 每天早上要手動跑 SQL 從 MySQL production DB 撈訂單資料，然後貼到 Google Sheets 做報表。每次都怕把 prod DB 打掛，而且資料常常對不上。我想幫他們建一個自動化的流程，把資料送到 BigQuery，讓他們直接在 Looker Studio 看報表。我們有 MySQL 訂單 DB、一個 Shopify 店面、還有 Stripe 付款記錄。」

**關鍵限制**:
- 工程人力：1 人（Daniel 兼職）
- 預算：低（不想付 Fivetran $$$）
- Freshness 需求：每日報表，data analyst 每天 9am 前要看到前一天資料
- Volume：訂單 table 約 500 萬筆，每日新增 ~5,000 筆

---

## Analysis

### Step 1: 確認 Sources & Destinations

| Source | Type | 挑戰 |
|--------|------|------|
| MySQL `orders` DB (GCP Cloud SQL) | Database | 不能打 prod DB，需 incremental |
| Shopify (商品、庫存) | REST API | Rate limit 2 req/s，需 pagination |
| Stripe (付款狀態) | REST API + Webhooks | 非同步狀態更新，需 reconciliation |

Destination: BigQuery `kova_dw` dataset  
Serve: Looker Studio dashboard

### Step 2: 確認 Freshness 需求

- 報表需求：Daily，analyst 9:00 AM 看資料
- SLA：BigQuery data ready by **08:30 AM**
- 因此：pipeline 排程 **02:00 AM**，給 6.5 小時緩衝

→ **不需要 real-time**，batch daily 足夠，複雜度大幅降低。

### Step 3: 選擇架構

**ETL vs ELT 判斷**:
- 已有 BigQuery → 選 **ELT**
- 原始資料先 load 進 BigQuery staging，再用 dbt SQL transform
- Daniel 一人維護，dbt 比 Airflow 學習成本低

**Orchestration 判斷**:
- 只有 3 個 source，排程簡單 → **不用 Airflow**
- 選 **Prefect Cloud（免費 tier）** + dbt Cloud（免費 tier）
- Shopify / Stripe → 評估後選 **Airbyte Cloud**（免費 tier 支援這兩個 connector，省去自建 API 爬蟲）
- MySQL → Cloud SQL → BigQuery 用 **BigQuery Data Transfer Service**（原生支援，零維護）

### Step 4: 設計 Quality Checks

| Stage | Check | Threshold | Alert |
|-------|-------|-----------|-------|
| Extract (MySQL) | Row count vs yesterday | ±30%（週末波動大） | Slack `#data-alerts` |
| Extract (MySQL) | `order_id` null | 0 nulls allowed | Slack |
| Extract (Shopify) | Schema validation | `product_id`, `sku` 必填欄位存在 | Slack |
| Load (BigQuery staging) | Freshness | `_extracted_at` < 6 hr ago | Slack |
| Transform (dbt) | Uniqueness | `orders.order_id` 不重複 | dbt test |
| Transform (dbt) | Referential integrity | `order_items.product_id` 在 `products` 中存在 | dbt test |
| Transform (dbt) | Range check | `order_amount` between 1 and 500,000 TWD | dbt test |

**Idempotency 設計**:
- MySQL 用 `WHERE updated_at >= DATE_SUB(CURDATE(), INTERVAL 1 DAY)` incremental extract
- BigQuery load 用 `MERGE`（upsert），partition by `order_date`
- 若重跑前一天，結果相同

---

## Result

```markdown
# Data Pipeline Design: Kova Commerce Order Analytics

## Sources & Destinations
| Source | Type | Destination | Freshness | Volume |
|--------|------|-----------|-----------|--------|
| MySQL orders (Cloud SQL) | Database | BQ `staging.orders` | Daily | ~5,000 rows/day |
| Shopify products/inventory | REST API | BQ `staging.shopify_products` | Daily | ~200 rows/day |
| Stripe payments | REST API | BQ `staging.stripe_payments` | Daily | ~5,000 rows/day |

## Architecture
- Pattern: **ELT**
- Extract/Load: BigQuery Data Transfer (MySQL) + Airbyte Cloud (Shopify, Stripe)
- Transform: **dbt Cloud** (SQL in BigQuery)
- Orchestration: **Prefect Cloud** (trigger dbt after extract completes)
- Quality: dbt tests + Prefect quality check tasks → Slack alerts

## Pipeline Diagram
```
MySQL (Cloud SQL) ──[BQ Data Transfer]──┐
Shopify API       ──[Airbyte Cloud]─────┼──→ BQ staging → [dbt transform] → BQ mart → Looker Studio
Stripe API        ──[Airbyte Cloud]─────┘
                                         ↑
                         [Prefect: quality checks + orchestration]
                         [dbt tests: uniqueness, refs, ranges]
                         [Slack alerts on failure]
```

## Quality Checks
| Stage | Check | Threshold | Alert |
|-------|-------|-----------|-------|
| Extract | Row count delta | ±30% vs 7-day avg | Slack `#data-alerts` |
| Extract | `order_id` null count | = 0 | Slack |
| Load | Freshness (`_extracted_at`) | < 6 hours | Slack |
| Transform | `orders.order_id` unique | dbt unique test | dbt Cloud alert |
| Transform | `order_amount` range | 1–500,000 TWD | dbt range test |
| Transform | `order_items.product_id` ref | exists in products | dbt ref test |

## Schedule
| Pipeline | Frequency | Start Time | SLA |
|----------|-----------|-----------|-----|
| MySQL extract | Daily | 02:00 AM | Staging ready by 03:00 AM |
| Airbyte sync (Shopify + Stripe) | Daily | 02:00 AM | Staging ready by 04:00 AM |
| dbt transform | Daily | 04:30 AM | Triggered after staging complete |
| Looker Studio data | Daily | — | Available by **08:30 AM** ✓ |
```

### 工具清單與月成本估算

| 工具 | 用途 | 成本 |
|------|------|------|
| BigQuery Data Transfer | MySQL → BQ | 免費 |
| Airbyte Cloud | Shopify + Stripe → BQ | 免費 tier |
| dbt Cloud | SQL transform + tests | 免費 tier (1 developer) |
| Prefect Cloud | Orchestration | 免費 tier |
| BigQuery storage + query | 儲存與查詢 | ~$5–15/月 |

**總計**: < $15/月，vs Fivetran ~$500+/月

### 第一週行動清單

1. **Day 1**: 設定 BigQuery Data Transfer，從 Cloud SQL 同步 `orders` table 到 `staging.orders`
2. **Day 2**: 設定 Airbyte Cloud，連接 Shopify + Stripe，驗證資料出現在 BQ staging
3. **Day 3–4**: 寫 dbt models：`mart.dim_products`、`mart.fact_orders`、`mart.fact_payments`；加 dbt tests
4. **Day 5**: 設定 Prefect flow，串接 dbt run + quality checks → Slack 通知
5. **Day 6**: 在 Looker Studio 建基本報表，讓 analyst 驗收
6. **Day 7**: 監控第一週執行，確認每天 8:30 前資料就緒

### Gotcha 提醒（針對此案）

- **MySQL incremental**: 用 `updated_at` 而非 `created_at` — 退款、狀態更新會改 `updated_at`，只看 `created_at` 會漏掉
- **Stripe 非同步**: Stripe payment 狀態可能在付款後 24 小時才 settle，報表需對 analyst 說明「昨日付款數」不等於「昨日成功收款數」
- **Backfill**: Airbyte 支援 historical sync；MySQL 若需補跑，調整 BQ Data Transfer 的 `start_time` 參數即可，不會產生重複（MERGE 保護）
