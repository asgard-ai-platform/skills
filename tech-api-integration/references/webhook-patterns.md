# Webhook Patterns

Webhooks are reverse API calls: the provider pushes events to your server instead of you polling. The implementation looks simple — receive POST, process event — but production reliability requires handling idempotency, signature verification, async processing, and provider retry behavior correctly.

---

## How Webhooks Work

```
Provider System          Your Server
     │                        │
     │  Event occurs          │
     │  (e.g. payment)        │
     │                        │
     │─── POST /webhook ─────>│  1. Verify signature
     │    {event payload}     │  2. Return 200 immediately
     │                        │  3. Enqueue for processing
     │<── 200 OK ─────────────│
     │                        │
     │  (timeout if no 200)   │  4. Worker processes event
     │  → retries             │  5. Idempotency check
                              │  6. Business logic
```

**Critical constraint**: You must return HTTP 200 within the provider's timeout (typically 5–30 seconds). If you do slow processing synchronously, the provider will time out and retry, causing duplicate processing.

---

## Step 1: Signature Verification

Always verify the request came from the provider, not an attacker.

### HMAC-SHA256 Pattern (Most Common)

Providers (Stripe, GitHub, Shopify) sign the request body with your shared secret:

```
signature = HMAC-SHA256(secret_key, raw_request_body)
```

They send this as a header, e.g. `X-Stripe-Signature`, `X-Hub-Signature-256`.

**Verification code (Python):**

```python
import hmac
import hashlib

def verify_signature(raw_body: bytes, header_sig: str, secret: str) -> bool:
    """
    raw_body: the request body as bytes (do NOT decode first)
    header_sig: value from X-Webhook-Signature header
    secret: your shared secret from provider dashboard
    """
    expected = hmac.new(
        key=secret.encode("utf-8"),
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()
    
    # Use compare_digest to prevent timing attacks
    return hmac.compare_digest(expected, header_sig)


# In your endpoint handler:
def webhook_handler(request):
    raw_body = request.get_data()  # bytes, before any parsing
    sig = request.headers.get("X-Webhook-Signature", "")
    
    if not verify_signature(raw_body, sig, SECRET_KEY):
        return "", 401  # Reject silently (don't reveal why)
    
    payload = json.loads(raw_body)
    # ... continue
```

**Common mistakes:**
- Verifying against `request.json` or decoded body instead of raw bytes — JSON re-serialization changes whitespace and key order, breaking the signature
- Using `==` instead of `hmac.compare_digest` — timing attacks can leak the expected signature character by character
- Storing the secret in source code — use environment variables

### Stripe-Style Timestamped Signatures

Stripe includes a timestamp in the signature to prevent replay attacks:

```
X-Stripe-Signature: t=1492774577,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e77a05bd539baad0eabs8d6a...
```

Their verification checks: `abs(now - t) < 300` (5-minute window) AND signature matches `t.{raw_body}`.

If your provider uses this pattern, implement the timestamp check too.

---

## Step 2: Respond Immediately, Process Asynchronously

```python
# BAD: synchronous processing — will time out for slow operations
@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    # This takes 10 seconds — provider times out and retries
    process_order(payload)
    send_confirmation_email(payload)
    update_inventory(payload)
    return "", 200

# GOOD: enqueue and return immediately
@app.route("/webhook", methods=["POST"])
def webhook():
    raw_body = request.get_data()
    
    if not verify_signature(raw_body, request.headers.get("X-Sig"), SECRET):
        return "", 401
    
    payload = json.loads(raw_body)
    
    # Enqueue for async processing — takes <1ms
    task_queue.enqueue("process_webhook", payload)
    
    return "", 200  # Respond within milliseconds
```

**Queue options by stack:**
| Stack | Queue |
|-------|-------|
| Python | Celery + Redis/RabbitMQ |
| Node.js | Bull + Redis, or BullMQ |
| Ruby | Sidekiq |
| Go | Machinery, or native goroutine + DB queue |
| Any | Database-backed queue (see below) |

---

## Step 3: Idempotency — The Core Problem

Providers retry events when they don't receive a 200. Your handler will receive the same event 2, 3, or more times. Processing it twice must produce the same result as processing it once.

### The Idempotency Check Pattern

```python
def process_webhook(payload: dict):
    event_id = payload["id"]  # Provider's unique event ID
    
    # 1. Check if already processed
    if EventLog.exists(event_id=event_id):
        logger.info(f"Skipping duplicate event {event_id}")
        return  # Idempotent: do nothing
    
    # 2. Process the event
    result = execute_business_logic(payload)
    
    # 3. Mark as processed (must be atomic with step 2 if possible)
    EventLog.create(
        event_id=event_id,
        processed_at=datetime.utcnow(),
        result=result
    )
```

**Database schema for event log:**

```sql
CREATE TABLE webhook_events (
    event_id     VARCHAR(255) PRIMARY KEY,  -- Provider's event ID
    provider     VARCHAR(50)  NOT NULL,
    event_type   VARCHAR(100) NOT NULL,
    received_at  TIMESTAMP    NOT NULL DEFAULT NOW(),
    processed_at TIMESTAMP,
    status       VARCHAR(20)  NOT NULL DEFAULT 'pending',
    payload      JSONB,
    error        TEXT
);

CREATE UNIQUE INDEX ON webhook_events (event_id);
```

### Race Condition: Two Workers Processing the Same Event

If two requests for the same event arrive simultaneously (e.g., provider retried immediately), both workers might pass the `EXISTS` check before either writes to the log.

**Solution: database-level unique constraint + optimistic approach:**

```python
def process_webhook(payload: dict):
    event_id = payload["id"]
    
    try:
        # Attempt to insert first — let DB enforce uniqueness
        EventLog.create(
            event_id=event_id,
            status="processing",
            payload=payload
        )
    except UniqueConstraintViolation:
        # Another worker already claimed this event
        logger.info(f"Duplicate event {event_id}, skipping")
        return
    
    try:
        result = execute_business_logic(payload)
        EventLog.update(event_id=event_id, status="done", result=result)
    except Exception as e:
        EventLog.update(event_id=event_id, status="failed", error=str(e))
        raise
```

The `UNIQUE` constraint on `event_id` acts as a distributed lock: only one worker can insert, others get an exception.

---

## Step 4: Handling Provider Retry Behavior

Different providers retry on different schedules. Know your provider's policy:

| Provider | Retry schedule | Max attempts |
|----------|---------------|-------------|
| Stripe | 1h, 8h, 1d, 2d, 3d | 7 over 5 days |
| GitHub | 3 retries, no delay | 4 total |
| Shopify | ~48 hours | 19 over 48h |
| Twilio | Up to 3 retries | 3 |
| SendGrid | 72 hours | Not documented |

**What triggers a retry:** receiving any non-2xx status, or a timeout (no response).

**What you should return:**

| Situation | Return | Effect |
|-----------|--------|--------|
| Success | `200 OK` | Provider marks delivered |
| Already processed (duplicate) | `200 OK` | Same — tell provider it's done |
| Invalid signature | `401` | Most providers stop retrying |
| Malformed payload you can't process | `400` | Most providers stop retrying |
| Processing failed (your bug) | `500` | Provider will retry — gives you time to fix |
| Temporarily unable to process | `503` | Provider retries — use for planned downtime |

**Do not return 200 for a signature failure** — that tells the provider the event was accepted, which obscures attacks.

---

## Step 5: Out-of-Order Event Delivery

Providers do not guarantee delivery order. You may receive `order.updated` before `order.created`.

### Pattern: Use `updated_at` to Guard State Transitions

```python
def handle_order_updated(payload):
    order_id = payload["data"]["id"]
    new_status = payload["data"]["status"]
    event_time = payload["created"]  # Unix timestamp from provider
    
    order = Order.find(order_id)
    
    if order is None:
        # order.created hasn't arrived yet — need to handle this
        # Option A: create a placeholder
        # Option B: enqueue retry after 5s
        task_queue.enqueue_in(5, "handle_order_updated", payload)
        return
    
    # Only apply if this event is newer than what we have
    if event_time <= order.last_event_at:
        logger.info(f"Skipping stale event for order {order_id}")
        return
    
    order.update(status=new_status, last_event_at=event_time)
```

### Pattern: Event Sourcing (for complex state machines)

Instead of applying each event immediately, store all events and derive current state:

```python
# Store every event
def handle_any_event(payload):
    event_id = payload["id"]
    
    if EventLog.exists(event_id=event_id):
        return  # Deduplicate
    
    EventLog.create(
        event_id=event_id,
        event_type=payload["type"],
        event_time=payload["created"],
        payload=payload
    )
    
    # Rebuild current state from all events in order
    rebuild_entity_state(payload["data"]["id"])

def rebuild_entity_state(order_id):
    events = EventLog.where(
        entity_id=order_id
    ).order_by("event_time ASC")
    
    state = {}
    for event in events:
        state = apply_event(state, event)
    
    Order.upsert(order_id, state)
```

Use event sourcing when: order matters, events can arrive late, and you need an audit trail.
Use the simpler `updated_at` guard when: state transitions are simple and late events are rare.

---

## Step 6: Error Handling and Dead Letter Queue

Some events will fail processing despite correct delivery. You need a way to retry them without waiting for the provider.

```python
def process_webhook(payload: dict):
    event_id = payload["id"]
    
    try:
        EventLog.claim(event_id, payload)  # Unique insert
    except UniqueConstraintViolation:
        return  # Duplicate
    
    try:
        execute_business_logic(payload)
        EventLog.mark_done(event_id)
    except RetryableError as e:
        # Transient failure — requeue with backoff
        attempts = EventLog.increment_attempts(event_id)
        if attempts < 5:
            delay = 2 ** attempts  # 2s, 4s, 8s, 16s, 32s
            task_queue.enqueue_in(delay, "process_webhook", payload)
            EventLog.mark_retrying(event_id)
        else:
            EventLog.mark_dead(event_id, error=str(e))
            alert_oncall(f"Webhook {event_id} dead after 5 attempts")
    except PermanentError as e:
        # Bad data, business rule violation — don't retry
        EventLog.mark_failed(event_id, error=str(e))
        logger.error(f"Permanent failure on {event_id}: {e}")
```

**Distinguish retryable vs permanent failures:**

| Error Type | Retryable? | Examples |
|------------|-----------|---------|
| Network timeout to downstream service | Yes | Database down, external API timeout |
| Database constraint violation | No | Duplicate order ID (logic bug) |
| HTTP 5xx from downstream | Yes (with limit) | Stripe API down |
| HTTP 4xx from downstream | No | Invalid data |
| Unexpected exception | Depends | Investigate before deciding |

---

## Step 7: Local Development and Testing

### ngrok for Local Testing

```bash
# Expose local port 8000 to public internet
ngrok http 8000

# Output:
# Forwarding  https://abc123.ngrok.io -> http://localhost:8000

# Register https://abc123.ngrok.io/webhook in the provider dashboard
# Provider can now send events to your local machine
```

### Replay Events Without Provider

Store raw payloads and replay them in tests:

```python
# tests/fixtures/stripe_payment_succeeded.json
{
  "id": "evt_test_123",
  "type": "payment_intent.succeeded",
  "created": 1712678400,
  "data": {
    "object": {
      "id": "pi_test_456",
      "amount": 2000,
      "currency": "usd"
    }
  }
}

# tests/test_webhook.py
def test_payment_succeeded_idempotent():
    payload = load_fixture("stripe_payment_succeeded.json")
    
    # First call — should process
    process_webhook(payload)
    assert Order.count() == 1
    
    # Second call — should be no-op
    process_webhook(payload)
    assert Order.count() == 1  # Not 2
```

---

## Decision Table: Which Pattern to Use

| Scenario | Pattern |
|----------|---------|
| Simple CRUD updates, rare duplicates | Idempotency key check before processing |
| High throughput, concurrent workers | DB unique insert as distributed lock |
| Complex state machine, order matters | Event sourcing |
| Simple state, stale event possible | `updated_at` guard |
| Processing can fail transiently | Dead letter queue with exponential backoff |
| Testing locally | ngrok + stored fixtures |
| Verifying event authenticity | HMAC-SHA256 + `compare_digest` |
| Provider has replay attacks risk | Timestamped signatures (Stripe pattern) |

---

## Checklist

- [ ] Signature verified against raw bytes, not parsed JSON
- [ ] `hmac.compare_digest` used (not `==`)
- [ ] Respond 200 within 5 seconds (async processing)
- [ ] Idempotency key stored in DB with unique constraint
- [ ] Race condition handled at DB level, not application level
- [ ] Out-of-order events handled (timestamp guard or event sourcing)
- [ ] Retryable vs permanent errors classified separately
- [ ] Dead letter queue with alerting after max retries
- [ ] Secrets in environment variables, not source code
- [ ] Raw payloads stored for debugging and replay
