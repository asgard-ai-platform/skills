# Chatbot NLU Design Patterns for Conversational Commerce

## Intent Taxonomy

Every e-commerce chatbot needs a consistent intent map before writing a single response. Below is a proven three-tier taxonomy. Tiers exist because matching depth differs: Tier 1 intents are high-frequency and high-confidence; Tier 3 intents are rare and should almost always escalate to human.

```
Tier 1 — Transactional (bot handles fully)
  order.track          "我的訂單到哪了"
  order.cancel         "我要取消訂單"
  product.price        "這個多少錢"
  product.stock        "有沒有貨"
  faq.shipping         "幾天到"
  faq.return_policy    "怎麼退貨"
  faq.store_hours      "幾點營業"

Tier 2 — Advisory (bot assists, may escalate)
  product.recommend    "幫我推薦適合送禮的"
  product.compare      "這兩款有什麼差別"
  order.modify         "訂單能改地址嗎"
  cart.recover         "我剛剛選的東西在哪"

Tier 3 — Sensitive (bot triages, human closes)
  complaint.defect     "收到壞掉的"
  complaint.missing    "包裹不見了"
  complaint.charge     "被多扣錢"
  vip.negotiation      "能不能打折"
```

**Decision rule for new intents**: if expected monthly volume < 50 utterances, skip bot handling — build a clean handoff message instead. Under-trained intents hurt containment rate more than having a smaller intent set.

---

## Entity Extraction Cheat Sheet

Intents tell you *what* the user wants; entities tell you *about what*. For e-commerce, these five entity types cover ~90% of conversations:

| Entity Type | Examples | Extraction Method |
|-------------|----------|------------------|
| `product_id` | "SKU-8821"、商品編號 | Regex: `[A-Z]{2,5}-\d{3,6}` |
| `order_id` | "#123456"、訂單號碼 | Regex: `#?\d{5,10}` |
| `color_variant` | "黑色"、"深藍" | Keyword list (per catalog) |
| `size_variant` | "XL"、"25cm"、"大號" | Keyword list + normalization |
| `price_range` | "1000以下"、"2000到3000" | Regex + parser |

### Slot-Filling Pattern

When an intent requires entities that weren't provided, fill slots conversationally — do NOT ask for everything at once:

```
User: "我要查訂單"  ← intent = order.track, order_id = MISSING

Bot: "好的！請告訴我您的訂單編號（格式：#數字），
     或輸入下單時使用的手機號碼。"

User: "#987654"   ← order_id = 987654

Bot: [查詢後回覆] "訂單 #987654 目前在「配送中」，
     預計明天下午送達。"
```

**Rule**: maximum two clarifying questions before offering "幫你轉給客服人員" escape hatch. Three-question loops are a trust killer.

---

## Confidence Threshold Framework

NLU models return a confidence score per intent. The threshold you set directly controls the containment rate vs CSAT tradeoff.

```
Score ≥ 0.80  → Execute intent directly
Score 0.55–0.79 → Disambiguation prompt (show top 2 guesses as buttons)
Score < 0.55  → Fallback flow
```

### Disambiguation Prompt Template

```
"您是想問：
 👉 [訂單出貨狀態]
 👉 [退換貨流程]
 
 還是想聯絡客服？"
```

Present as **buttons**, not free text. Buttons eliminate re-parsing and reduce loop risk.

### Tuning the Threshold

Plot your training data on this grid and adjust cutoffs monthly:

```
           Correct    Wrong
High conf     ✓✓✓       ✗    ← keep threshold here
Mid conf       ✓✓      ✗✗    ← disambiguation zone
Low conf        ✓     ✗✗✗   ← always fallback
```

Target: high-confidence zone should cover ≥ 55% of production messages. If it doesn't, you have an intent coverage gap, not a threshold problem.

---

## Fallback Flow Design

The fallback is the most underdesigned part of most chatbots. A bad fallback ("抱歉我聽不懂，請重新輸入") loops until the user rage-quits.

### Three-Strike Fallback

```
Strike 1 (first failed match):
  "不好意思，我好像沒能理解您的意思 🙁
   請問您是想詢問以下哪個方向？"
  [按鈕: 訂單查詢 | 商品問題 | 退換貨 | 其他]

Strike 2 (second consecutive failed match):
  "讓我換個方式幫您——
   您可以直接告訴我訂單編號或商品名稱，
   或是選擇：[找客服人員]"

Strike 3 (third consecutive failed match):
  → 強制轉人工，無需用戶再做選擇
  "我來幫您轉接客服人員，稍等一下～"
  [觸發 handoff.initiate]
```

**Critical**: reset strike counter when user sends *any* recognized intent. Strikes are per-confusion-streak, not per-session.

---

## Dialogue State Machine

Each conversation is a state machine. Treating it as a flat Q&A is the #1 cause of context loss.

### Minimal State Object

```json
{
  "session_id": "abc123",
  "user_id": "line_uid_xxx",
  "current_flow": "product.recommend",
  "slots": {
    "category": "保養品",
    "budget_max": 1500,
    "occasion": "生日禮物"
  },
  "cart": ["SKU-441", "SKU-882"],
  "strike_count": 0,
  "last_intent": "product.recommend",
  "handoff_requested": false
}
```

**Persistence requirement**: state must survive at least 24 hours of inactivity. LINE/WhatsApp conversations are async — users message at 11pm and reply the next morning. A stateless bot that forgets the context is worse than starting over, because it makes the user repeat themselves.

### Flow Transition Rules

```
Any state + "找人工" keyword  → handoff.initiate (override)
Any state + strike_count ≥ 3  → handoff.initiate (override)
product.recommend + all slots filled → product.show_results
product.show_results + "買這個" → cart.add → checkout.begin
checkout.begin + payment_confirmed → order.confirm → post_purchase.schedule
```

Override rules fire regardless of current flow — they act as escape hatches.

---

## Product Card Spec

Product cards are the core commerce touchpoint. Every card must include exactly four elements:

```
┌─────────────────────────────┐
│  [Product Image — 1:1 ratio]│
│                             │
│  商品名稱（≤ 30 字）          │
│  NT$1,280                   │
│  ★ 4.8 (312 則評價)          │
│                             │
│  [加入購物車]  [了解更多]     │
└─────────────────────────────┘
```

**Rules**:
- Image is mandatory — cards without images have ~40% lower tap-through rate
- Price must be the final price (after discount); list price may show as strikethrough
- Maximum two CTA buttons per card; primary action on the left
- In LINE: use Flex Message; in Instagram: use Product Tag + quick reply buttons

### Carousel Limits

| Platform | Max Cards | Recommended |
|----------|-----------|-------------|
| LINE Flex Carousel | 12 | 3–5 |
| Facebook Messenger | 10 | 3–4 |
| WhatsApp List | 10 rows | N/A (list, not card) |

Show 3 cards by default. If user asks "還有沒有別的" → show next 3. Never dump all 12 at once.

---

## Worked Example: Gift Recommendation Flow

This trace shows the full Help → Trust → Recommend → Convert sequence from the IRON LAW.

```
[Entry point: user clicks "找禮物" in Rich Menu]

Bot: "要幫誰挑禮物呀？😊"
     [女友 | 媽媽 | 朋友 | 同事 | 其他]

User: [點選「女友」]
  → slots.recipient = "女友"

Bot: "預算大概多少呢？"
     [500以下 | 500–1500 | 1500–3000 | 3000以上]

User: [點選「1500–3000」]
  → slots.budget_min = 1500, slots.budget_max = 3000

Bot: "她平常喜歡？"
     [保養彩妝 | 包包配件 | 居家生活 | 美食甜點 | 不確定]

User: [點選「保養彩妝」]
  → slots.category = "保養彩妝"
  → trigger: product.recommend (all slots filled)

Bot: "根據你說的，這幾款很多人送過女友都超好評 💝"
     [顯示 3 張 Product Card，價格 NT$1,680–NT$2,480]

User: "第一個看起來不錯，有送禮包裝嗎？"
  → intent = product.gift_wrap (Tier 2)

Bot: "有的！加購禮盒包裝 NT$80，
     結帳時可以勾選，還可以附上手寫卡。
     要加入購物車嗎？"
     [加入購物車 | 再看看其他]

User: [點選「加入購物車」]
  → cart.add SKU-441
  → checkout.begin

Bot: "已加入 🛍️ 要直接結帳嗎？
     現在用 LINE Pay 結帳，運費免費喔！"
     [前往結帳 | 繼續購物]
```

Total messages: 8 (bot) + 5 (user). Decision buttons eliminate open-ended ambiguity at every step while still feeling like a conversation, not a form.

---

## Containment Rate Calculation

```
Containment Rate = (Sessions resolved by bot) / (Total sessions) × 100%

"Resolved" = session ended without human handoff AND
             user did not re-contact within 2 hours on the same issue
```

### Decompose by Intent Tier

Track containment separately per tier to find optimization targets:

```
Tier 1 target: ≥ 90%  (FAQ should almost never need humans)
Tier 2 target: ≥ 60%  (advisory needs fallback path)
Tier 3 target:   0%   (always human — don't optimize, just triage fast)

Overall target: 60–70%
```

If overall containment is below 60%:
1. Check Tier 1 containment first — low Tier 1 means NLU training data is thin
2. Check fallback rate — if > 25% of messages hit fallback, extend intent coverage
3. Check strike-3 triggers — if > 15% of sessions hit strike-3, slot-filling questions are too hard

---

## Human Handoff Protocol

Handoff is not failure — it is a designed outcome. A clean handoff preserves the conversation context so the human agent does not ask the user to repeat themselves.

### Handoff Payload

When transferring to human, pass:

```json
{
  "user_id": "line_uid_xxx",
  "trigger": "complaint.defect",
  "conversation_summary": "用戶反映收到 SKU-441 商品外包裝破損，訂單 #987654，下單日 2026-04-07",
  "full_transcript": [...],
  "slots": { "order_id": "987654", "product_id": "SKU-441", "issue": "破損" },
  "priority": "high"
}
```

### Handoff Message to User

```
"我幫您轉接專人客服，對方已收到您的情況說明，
不需要重複說明一次。

通常 5 分鐘內會回覆您，謝謝您的耐心等候 🙏"
```

**Do not** say "我幫您轉接至客服人員，請稍後" and then go silent for 20 minutes. Set a realistic SLA and state it explicitly.

---

## Anti-Patterns

| Anti-Pattern | What It Looks Like | Fix |
|---|---|---|
| **Infinite loop fallback** | Bot asks same clarification 5 times | Three-strike rule + forced handoff |
| **Form masquerading as chat** | "請輸入您的：1.姓名 2.電話 3.訂單編號" | One slot per turn, conversational phrasing |
| **Premature product push** | First message is a product promo | Follow Help → Trust → Recommend → Convert sequence |
| **Stateless session** | Bot forgets cart after 10-minute gap | Persist state ≥ 24 hours |
| **Missing escape hatch** | No path to human for any intent | Every flow must have "找客服" option visible within 2 turns |
| **Confidence overfit** | Threshold set so high that 70% of messages go to fallback | Calibrate threshold monthly against production logs |
