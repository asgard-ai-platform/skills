我沒有可用的檔案寫入工具，直接輸出 markdown 內容：

---

# Example: Stripe 訂閱帳單整合

## Scenario

**公司背景**：PocketPay 是一家台北的 B2B SaaS 新創，提供中小企業費用管理平台，月費制訂閱。後端工程師 Jason 負責串接 Stripe API 處理訂閱扣款，上線前兩週，他在 staging 環境遇到以下問題：

1. 建立訂閱時偶爾收到 `401 Unauthorized`，但 API key 確認是對的
2. Stripe Webhook 在測試時觸發兩次相同事件，導致發票被建立兩份
3. 列出所有客戶訂閱時，只拿到前 100 筆，共 340 筆客戶

Jason 問：「這些問題怎麼解決？我應該怎麼規劃整個整合架構？」

---

## Analysis

### 步驟一：先讀文件，確認問題根因

**問題 1 — 401 Unauthorized**

Stripe 有兩組 API key：
- `sk_test_...`：只在 Test mode 有效
- `sk_live_...`：只在 Live mode 有效

Jason 的 staging 環境混用了 live key 呼叫 test endpoint（或反過來）。Stripe 的 auth 是 **Bearer Token**，放在 `Authorization: Bearer sk_test_xxx` header。

根本原因：環境變數 `STRIPE_SECRET_KEY` 在 CI/CD pipeline 中被覆寫成 live key，而 staging 的 base URL 仍指向 test mode。

**修正**：key 與 mode 必須一致；staging 永遠使用 `sk_test_` 開頭的 key，並用 `STRIPE_ENV=test` 環境變數明確標示，CI pipeline 分離 staging / production secrets。

---

**問題 2 — Webhook 觸發兩次，建立重複發票**

Stripe 的 Webhook 保證「至少一次（at-least-once）」投遞。網路不穩時同一事件會重送。Jason 的 handler 每次收到 `invoice.payment_succeeded` 就直接建立發票，沒有去重機制。

根本原因：違反 Gotcha「Webhook reliability — handler 必須冪等」。

**修正**：在資料庫建立 `processed_stripe_events` 表，以 `stripe_event_id`（`evt_xxx`）為 unique key：

```python
def handle_invoice_payment_succeeded(event):
    event_id = event["id"]  # e.g. "evt_1Nz9Kx2eZvKYlo2C..."
    
    # 先查有沒有處理過
    if ProcessedEvent.exists(event_id):
        return  # 重複事件，直接忽略
    
    with db.transaction():
        create_invoice(event["data"]["object"])
        ProcessedEvent.create(event_id)
```

---

**問題 3 — 只拿到前 100 筆**

Stripe 預設每次回傳最多 100 筆（`limit=100`），超過需要分頁。回應包含 `has_more: true` 與最後一筆的 `last_id`，需用 `starting_after` 參數繼續拉。

根本原因：違反 Gotcha「Pagination — 只拿第一頁」。

**修正**：

```python
def list_all_subscriptions():
    subscriptions = []
    last_id = None
    
    while True:
        params = {"limit": 100}
        if last_id:
            params["starting_after"] = last_id
        
        page = stripe.Subscription.list(**params)
        subscriptions.extend(page["data"])
        
        if not page["has_more"]:
            break
        last_id = page["data"][-1]["id"]
    
    return subscriptions  # 全部 340 筆
```

---

### 步驟二：整理完整整合架構

PocketPay 使用的 Stripe 端點：

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/customers` | POST | 建立新客戶 |
| `/v1/subscriptions` | POST | 建立訂閱 |
| `/v1/subscriptions/{id}` | PATCH | 升降方案 |
| `/v1/subscriptions` | GET | 列出所有訂閱（需分頁） |
| `/v1/webhook_endpoints` | — | 接收 `invoice.payment_succeeded`, `customer.subscription.deleted` |

Rate limit：Stripe 預設 **100 req/s**（live mode），test mode 更低。PocketPay 月底批次對帳時可能觸發，需加 token bucket 控流。

---

### 步驟三：錯誤處理矩陣

| 錯誤 | Stripe 回應 | 我們的處理 |
|------|-------------|-----------|
| 401 | `invalid_api_key` | 停止，alert 工程師，不重試 |
| 402 | `card_declined` | 通知客戶，不重試 |
| 429 | `rate_limit` | 讀 `Retry-After` header，等待後重試，最多 5 次 |
| 500/503 | Stripe 服務錯誤 | Exponential backoff：2s → 4s → 8s，最多 3 次 |
| Webhook 驗簽失敗 | — | 回 400，記錄 IP，不處理 payload |

Webhook 必須用 `stripe.Webhook.construct_event()` 驗證簽名，防止偽造請求。

---

## Result

```markdown
# API Integration Plan: Stripe Subscriptions

## API Overview
- Base URL: https://api.stripe.com/v1
- Auth: Bearer Token（sk_test_* for staging, sk_live_* for production）
- Rate limit: 100 req/s (live mode)
- Documentation: https://stripe.com/docs/api

## Endpoints Used
| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| /customers | POST | 建立客戶 | Bearer |
| /subscriptions | POST | 建立訂閱 | Bearer |
| /subscriptions/{id} | PATCH | 升降方案 | Bearer |
| /subscriptions | GET | 列出所有訂閱（分頁） | Bearer |

## Error Handling
| Error | Response | Our Action |
|-------|----------|-----------|
| 401 invalid_api_key | Unauthorized | 立即停止，alert 工程師 |
| 402 card_declined | Payment failed | 通知客戶付款失敗，不重試 |
| 429 rate_limit | Too Many Requests | 等 Retry-After 秒數，最多重試 5 次 |
| 503 Service Unavailable | Stripe 宕機 | Exponential backoff 最多重試 3 次 |

## Key Design Decisions
- Webhook handler 用 `processed_stripe_events` 表去重（idempotency key = evt_id）
- Subscription 列表使用 cursor-based pagination（starting_after）
- 所有 API key 存 AWS Secrets Manager，不入 source code
- staging 環境鎖定只允許 sk_test_ prefix，CI 用不同 secret group

## Implementation Timeline
| Phase | Task | Duration |
|-------|------|----------|
| 1 | Auth 設定 + 建立客戶 / 訂閱基本 call | 2 天 |
| 2 | Webhook handler + idempotency 去重 | 2 天 |
| 3 | 分頁列表 + 錯誤處理 + retry logic | 2 天 |
| 4 | Staging 端對端測試 + 監控 alert 設定 | 1 天 |
```
