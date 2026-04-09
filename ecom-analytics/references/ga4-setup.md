# GA4 E-Commerce Tracking Setup

## What This Covers

Step-by-step implementation of GA4 e-commerce event tracking for online stores. Covers GTM-based setup (recommended), direct gtag implementation, and validation. Assumes you already have a GA4 property created.

---

## Setup Path Decision

```
Do you use Google Tag Manager?
├── YES → Follow GTM path (Sections 1–3)
└── NO  → Follow gtag.js path (Section 4)

Do you use a platform (Shopify / WooCommerce)?
├── YES → Use native integration first (Section 5), then verify with Section 6
└── NO  → Custom implementation via GTM or gtag
```

---

## Section 1: GTM Container Setup

### 1.1 Create the GA4 Configuration Tag

In GTM:
1. **Tags → New → Google Tag**
2. Tag ID: `G-XXXXXXXXXX` (your GA4 Measurement ID)
3. Trigger: **All Pages**
4. Name: `GA4 - Configuration`

This tag must fire on every page before any event tags.

### 1.2 Variable: GA4 Measurement ID

Create a **Constant** variable named `{{GA4 Measurement ID}}` with value `G-XXXXXXXXXX`. Reference it in all subsequent tags — changing the ID in one place updates all tags.

---

## Section 2: E-Commerce Data Layer

GA4 e-commerce requires a `dataLayer.push()` call at each funnel stage. The data layer must be pushed **before** GTM reads it.

### 2.1 Data Layer Item Object Structure

Every item in the `items` array must follow this schema:

```javascript
{
  item_id: "SKU_12345",          // REQUIRED: your internal SKU
  item_name: "Classic T-Shirt",  // REQUIRED
  item_brand: "Acme",
  item_category: "Apparel",
  item_category2: "Tops",        // subcategory (optional, up to category5)
  item_variant: "Blue / L",
  price: 29.99,                  // unit price, no currency symbol
  quantity: 1,
  index: 0,                      // position in list (0-indexed)
  item_list_name: "Search Results",
  item_list_id: "search_results"
}
```

**Critical**: `price` must be a number, not a string. `"29.99"` will be ignored in revenue calculations.

### 2.2 Event Push Templates

#### view_item (Product Detail Page)

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null }); // Clear previous ecommerce object
dataLayer.push({
  event: "view_item",
  ecommerce: {
    currency: "USD",
    value: 29.99,
    items: [{
      item_id: "SKU_12345",
      item_name: "Classic T-Shirt",
      item_category: "Apparel",
      price: 29.99,
      quantity: 1
    }]
  }
});
```

#### add_to_cart

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_to_cart",
  ecommerce: {
    currency: "USD",
    value: 59.98,       // price × quantity
    items: [{
      item_id: "SKU_12345",
      item_name: "Classic T-Shirt",
      price: 29.99,
      quantity: 2
    }]
  }
});
```

#### begin_checkout

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "begin_checkout",
  ecommerce: {
    currency: "USD",
    value: 59.98,
    coupon: "SAVE10",   // empty string if no coupon
    items: [ /* full cart items array */ ]
  }
});
```

#### add_payment_info

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "add_payment_info",
  ecommerce: {
    currency: "USD",
    value: 59.98,
    payment_type: "credit_card",  // "paypal", "apple_pay", etc.
    items: [ /* full cart items array */ ]
  }
});
```

#### purchase (Order Confirmation Page)

```javascript
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: "purchase",
  ecommerce: {
    transaction_id: "T_12345",    // REQUIRED, must be unique
    currency: "USD",
    value: 53.98,                 // revenue after discount, before tax+shipping
    tax: 4.50,
    shipping: 5.99,
    coupon: "SAVE10",
    items: [{
      item_id: "SKU_12345",
      item_name: "Classic T-Shirt",
      price: 26.99,               // discounted unit price
      quantity: 2
    }]
  }
});
```

**`value` definition**: This is the field GA4 uses for revenue reporting. Decide at the start whether `value` = revenue before or after tax/shipping — and be consistent. Most stores use **pre-tax, pre-shipping** so that `tax` and `shipping` remain separable. Do not change this convention mid-stream or revenue trends will break.

---

## Section 3: GTM Tags for Each Event

### 3.1 One Tag Per E-Commerce Event

For each event (`view_item`, `add_to_cart`, etc.), create a GTM tag:

- **Tag type**: Google Analytics: GA4 Event
- **Configuration Tag**: `{{GA4 - Configuration}}`
- **Event Name**: `add_to_cart` (must match exactly)
- **Ecommerce**: ✅ Send Ecommerce data → Data Layer

The "Send Ecommerce data → Data Layer" checkbox reads the `ecommerce` object directly from the data layer. You do not need to map individual parameters manually.

### 3.2 Triggers

| Event | Trigger Type | Condition |
|-------|-------------|-----------|
| `view_item` | Custom Event | Event name = `view_item` |
| `add_to_cart` | Custom Event | Event name = `add_to_cart` |
| `begin_checkout` | Custom Event | Event name = `begin_checkout` |
| `add_payment_info` | Custom Event | Event name = `add_payment_info` |
| `purchase` | Custom Event | Event name = `purchase` |

Custom Event triggers match the `event` key in the `dataLayer.push()` call.

---

## Section 4: Direct gtag.js Implementation (No GTM)

Add to `<head>` on every page:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Then fire events directly:

```javascript
// add_to_cart example
gtag("event", "add_to_cart", {
  currency: "USD",
  value: 29.99,
  items: [{
    item_id: "SKU_12345",
    item_name: "Classic T-Shirt",
    price: 29.99,
    quantity: 1
  }]
});
```

The structure is identical to the data layer objects — only the wrapper differs.

---

## Section 5: Platform-Specific Notes

### Shopify

Shopify's native GA4 integration (via **Online Store → Preferences → Google Analytics**) fires `purchase` on the thank-you page but often **misses** `add_to_cart` and `begin_checkout`. Verify in DebugView before assuming full funnel coverage.

For complete funnel tracking on Shopify, use the **Google & YouTube channel app** or implement custom theme snippets + GTM via Shopify's `theme.liquid`.

The `transaction_id` from Shopify is the order number (`#1234`). Strip the `#` if downstream systems expect numeric IDs.

### WooCommerce

Use the **WooCommerce Google Analytics Integration** plugin or **GTM4WP**. GTM4WP pushes all standard e-commerce events automatically once configured; it is the most reliable method for WooCommerce.

Verify that WooCommerce's tax settings match your `value` convention. WooCommerce can push prices inclusive or exclusive of tax depending on store settings.

---

## Section 6: Validation

### 6.1 GA4 DebugView

1. Install **Google Analytics Debugger** Chrome extension
2. Enable it → extension fires events to DebugView in real time
3. In GA4: **Admin → DebugView**
4. Walk through your funnel: browse a product, add to cart, begin checkout, complete a test purchase

In DebugView, confirm:
- Each event appears with correct name
- `ecommerce` parameter is populated (click event → expand parameters)
- `value` shows a number, not `(not set)`
- `transaction_id` on `purchase` is unique per order

### 6.2 GTM Preview Mode

Before publishing:
1. GTM → **Preview** → enter your store URL
2. Walk through the funnel
3. In the Tag Assistant panel, check each event tag fired **once** at the correct step
4. Confirm no double-fires (purchase tag should fire exactly once per order)

### 6.3 Common Validation Failures

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `value` = `(not set)` in GA4 | `price` passed as string | Cast to `parseFloat()` |
| Purchase event fires twice | Tag fires on page refresh + on load | Add de-duplication: store `transaction_id` in sessionStorage; skip push if already sent |
| `items` array missing | Data layer push fires before cart data is available | Move push to after cart API call resolves |
| Revenue inflated | `value` includes tax+shipping | Standardize: `value = subtotal`, use `tax` and `shipping` fields separately |
| Checkout funnel broken in GA4 | `begin_checkout` not firing | Confirm trigger fires on checkout page load, not just button click |

### 6.4 Duplicate Purchase Prevention

The most damaging data quality issue in GA4 e-commerce. Implement this on your order confirmation page:

```javascript
(function() {
  const orderId = "{{ order.id }}"; // inject from backend
  const storageKey = "ga4_sent_" + orderId;

  if (!sessionStorage.getItem(storageKey)) {
    dataLayer.push({ ecommerce: null });
    dataLayer.push({
      event: "purchase",
      ecommerce: {
        transaction_id: orderId,
        // ... rest of event
      }
    });
    sessionStorage.setItem(storageKey, "1");
  }
})();
```

GA4 itself does **not** deduplicate by `transaction_id` — if you send two `purchase` events with the same ID, both are counted.

---

## Section 7: GA4 Property Configuration for E-Commerce

After tracking is firing, configure the property itself:

### 7.1 Mark as E-Commerce Property

**Admin → Property → Reporting Identity** — ensure "Blended" or "Observed" is selected (not "Device-based") for cross-device attribution.

### 7.2 Enable Google Signals

**Admin → Property → Data Settings → Google Signals** → Activate

Required for:
- Cross-device reporting
- Remarketing audiences in Google Ads
- Demographics data

### 7.3 Set Reporting Time Zone and Currency

**Admin → Property Settings**

- Time zone: set to your business time zone (affects when day boundaries fall in reports)
- Currency: set to your store's transaction currency

If `purchase` events use `currency: "USD"` but the property is set to `TWD`, GA4 will attempt currency conversion using daily exchange rates. This introduces noise. Keep them consistent.

### 7.4 Link to Google Ads

**Admin → Product Links → Google Ads Links**

Required to:
- Import GA4 conversions into Google Ads (use `purchase` as primary conversion)
- Enable auto-tagging (`gclid` parameter) for accurate paid traffic attribution
- Build remarketing lists from GA4 audiences

### 7.5 Configure Conversion Events

**Admin → Events** → find `purchase` → toggle **Mark as conversion**

Also mark `begin_checkout` and `add_to_cart` as conversions if you want funnel visibility in Google Ads. These are called **micro-conversions** and help with Smart Bidding signal volume during low-purchase periods.

---

## Section 8: Funnel Exploration in GA4

Once data is flowing, use **Explore → Funnel Exploration** to visualize the funnel described in SKILL.md.

### Configuration

| Step | Event | Filter |
|------|-------|--------|
| 1 | `view_item` | — |
| 2 | `add_to_cart` | — |
| 3 | `begin_checkout` | — |
| 4 | `purchase` | — |

Set **Funnel type** to "Open" (users can skip steps and re-enter). "Closed" funnels require sequential completion and significantly undercount real conversion paths.

Set the **window** to 30 days minimum — a purchase cycle can span multiple sessions.

### Reading the Output

The funnel shows absolute counts and step-by-step drop-off percentages. Map these to the SKILL.md framework:

```
view_item → add_to_cart:   Engagement signal (product-market fit, pricing, images)
add_to_cart → begin_checkout: Intent signal (trust, urgency, distraction)
begin_checkout → purchase:  Friction signal (payment options, form complexity, shipping cost)
```

Segment the funnel by **Device Category** immediately. Mobile drop-off at checkout is typically 2–3× desktop — if you don't segment, the average masks where effort should go.
