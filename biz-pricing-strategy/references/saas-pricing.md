# SaaS Pricing Models

SaaS pricing differs from one-time product pricing in one fundamental way: the customer pays repeatedly, so **the price must justify renewal at every billing cycle**, not just at the moment of purchase. This shifts the pricing question from "what is this worth?" to "what is this worth *every month*?"

---

## The Five SaaS Pricing Models

| Model | Structure | Best Fit | Revenue Predictability |
|-------|-----------|----------|------------------------|
| **Per-seat (per-user)** | Fixed price × number of users | Collaboration tools, productivity software | High |
| **Flat-rate** | One price for everything | Simple product, uniform customer base | High |
| **Usage-based (consumption)** | Pay per API call, GB, transaction | Infrastructure, APIs, data pipelines | Low–Medium |
| **Tiered** | Fixed price per tier (feature-gated) | Products with clear usage segments | High |
| **Freemium** | Free base + paid upgrade | High viral coefficient, self-serve growth | Low (depends on conversion) |

These are not mutually exclusive. Most mature SaaS products combine them — e.g., tiered plans where each tier has a per-seat price up to a seat cap, then usage-based overages.

---

## Model Selection Decision Framework

```
Is your product's value tied to a countable resource (API calls, storage, messages)?
  YES → Usage-based is honest and aligns incentives. Consider hybrid (flat base + usage overage).
  NO ↓

Do your customers have very different usage levels (1-seat freelancer vs 200-seat enterprise)?
  YES → Per-seat or tiered. Flat-rate will either overprice small customers or underprice large ones.
  NO ↓

Is viral/word-of-mouth adoption important to your growth model?
  YES → Freemium. Calculate whether you can afford the free tier (see Freemium Math below).
  NO → Tiered with a clear feature ladder.
```

### Per-Seat vs Usage-Based: The Core Tradeoff

**Per-seat** aligns with how buyers budget (headcount is a known quantity). It creates a ceiling on expansion revenue per account — you can only earn more by adding seats.

**Usage-based** aligns revenue with value delivery. It expands naturally as customers grow. But it creates **revenue volatility**: a customer who reduces usage next month costs you MRR without churning. Forecasting is harder.

Rule of thumb: if your product's value is primarily about *enabling* a person (communication, project management, writing), go per-seat. If it's primarily about *processing* something (data, transactions, API calls), go usage-based.

---

## Tier Architecture: Designing the Feature Ladder

The goal of a tier structure is to route each customer segment to the tier that maximizes their perceived value while capturing a fair share of it.

### The Three-Tier Template

Most SaaS products use three named tiers. The names themselves communicate positioning:

```
Starter / Basic / Free     ←  Acquisition tier (low or zero cost)
Pro / Growth / Standard    ←  Primary revenue tier (target 60–70% of paying customers)
Business / Team / Plus     ←  Expansion tier (upsell target)
Enterprise                 ←  Optional fourth tier, sold not bought
```

### Feature Gating Principles

**Gate by outcome, not by feature count.** Customers shouldn't feel punished — they should feel that the higher tier solves a bigger problem.

| Effective Gates | Ineffective Gates |
|----------------|-------------------|
| Number of team members / workspaces | Number of templates (feels arbitrary) |
| Automation / API access | Color themes |
| Advanced analytics / reporting | Export to CSV |
| SSO / SAML / audit logs (for Enterprise) | Priority support (often hollow) |
| Data retention period | Storage (unless storage is the product) |

**The limit gate pattern**: Starter gets X of something; Pro gets unlimited. Customers feel the limit naturally as they grow.

Example — project management SaaS:
```
Starter  NT$99/user/month   → 5 active projects, no automation
Pro      NT$299/user/month  → Unlimited projects, automation, reporting
Business NT$499/user/month  → Everything in Pro + SSO, admin controls, audit log
```

### Applying the Decoy Effect (from parent SKILL.md)

The decoy tier is usually **Starter** — priced close enough to Pro that upgrading feels obvious, but limited enough that power users feel genuinely constrained.

The Business tier serves as a **price anchor** for Pro: NT$299 feels reasonable when NT$499 exists. This is why Enterprise pricing is often not shown publicly — showing an extreme anchor on the pricing page cheapens lower tiers.

**Decoy test**: Ask "would a reasonable new customer look at Starter, intend to stay on Starter, but then feel nudged to upgrade within 30-90 days?" If yes, the decoy is working. If Starter is good enough for most customers forever, you've mis-tiered.

---

## Freemium Math

Freemium is not "free pricing" — it's a **customer acquisition channel**. The economics work only if the cost to serve free users is covered by the conversion revenue.

### Freemium Unit Economics Formula

```
Freemium CAC = (Cost to serve N free users for 1 month) / (N × conversion rate)
```

Compare this to your blended CAC from paid channels.

**Worked example:**
- Monthly server + support cost per free user: NT$15
- Free users in cohort: 1,000
- Conversion rate (free → paid within 90 days): 4%
- Average paid plan: NT$299/month

```
Monthly cost to serve 1,000 free users = NT$15,000
Converted users = 1,000 × 4% = 40
Freemium CAC = NT$15,000 / 40 = NT$375 per converted customer
```

If your paid acquisition CAC (Google Ads, sales) is NT$2,000, freemium at NT$375 CAC is excellent. If it's NT$200 (strong SEO, viral loop), freemium may not be worth the infrastructure cost.

### Conversion Rate Benchmarks

Industry averages are noisy and product-specific, but rough guidance:

| Product type | Typical free→paid conversion |
|-------------|------------------------------|
| Developer tools / technical SaaS | 5–15% |
| B2B collaboration / productivity | 3–8% |
| Consumer SaaS | 1–5% |
| Infrastructure / API | 10–25% (trial model) |

**Warning**: A 1% conversion rate is not a failure if free users are also a referral engine. Model the referral-adjusted CAC.

### The Freemium Trap

If free tier is too generous, customers have no reason to upgrade. Common signs:
- Free users stay on free for 12+ months without hitting limits
- Support volume from free users exceeds revenue contribution
- Paid features are "nice to have" but free tier covers 80% of use cases

Fix: tighten the free tier limits or deepen the paid feature differentiation — do not lower the paid price as the first response.

---

## Expansion Revenue: The SaaS Pricing Multiplier

One-time product pricing ends at the sale. SaaS pricing compounds through **expansion revenue** — additional revenue from existing customers via upsell, cross-sell, and seat growth.

### Net Revenue Retention (NRR)

NRR measures whether your revenue base is growing or shrinking from existing customers alone, independent of new customer acquisition.

```
NRR = (MRR start + Expansion MRR − Contraction MRR − Churned MRR) / MRR start × 100%
```

| NRR | Interpretation |
|-----|---------------|
| > 120% | Excellent — existing customers are funding growth |
| 100–120% | Good — customer base self-sustaining |
| 90–100% | Acceptable — some churn/contraction, offset by expansion |
| < 90% | Problem — pricing or product-market fit issue |

**Why this matters for pricing design**: a pricing model that enables NRR > 100% means the company can grow revenue even with zero new customers. This is only possible if the pricing architecture **expands with customer success** — per-seat grows as teams hire; usage-based grows as customers process more; tiered grows as customers hit limits and upgrade.

### Designing for Expansion

Build expansion triggers into the pricing structure before launch:

| Expansion lever | How to design it in |
|----------------|---------------------|
| Seat growth | Per-seat or per-user pricing |
| Usage growth | Usage-based overages or step-up tiers |
| Feature adoption | Feature-gated upgrades with in-product prompts |
| Department expansion | Multi-workspace / multi-team pricing |
| Compliance / security needs | Enterprise tier with SSO, audit, SLA |

The worst outcome is a customer who grows significantly (more users, more usage, more revenue for them) but pays you the same flat fee. Value-based pricing (from parent SKILL.md) is the solution: tie the price to the metric that scales with customer success.

---

## SaaS Price Sensitivity: Willingness to Pay by Segment

B2B SaaS buyers think in ROI, not sticker price. The question they're asking is not "is NT$299 cheap?" but "does this save us more than NT$299/month per user?"

### The Value Metric Frame

For each customer segment, identify the **value metric**: the unit of outcome your product delivers.

| SaaS category | Value metric | Pricing implication |
|---------------|-------------|---------------------|
| Project management | Hours saved per user | Per-user pricing justified by productivity ROI |
| Email marketing | Revenue per send / open rate | % of revenue or per-subscriber |
| Customer support | Tickets resolved / agent | Per-agent seat |
| Analytics | Decisions improved / queries run | Usage-based or per-seat (analyst) |
| E-signature | Contracts signed | Per-document or per-seat |

When you can quantify the value metric, you can calculate the **value-to-price ratio** (V/P). Target V/P ratio of 10:1 for B2B SaaS: if the product saves NT$3,000/user/month, NT$299/user/month is credible. NT$1,500/user/month may stall sales even if technically justified.

### SMB vs Enterprise Pricing

Do not use the same pricing page for both. SMBs self-serve and need transparent pricing with instant credit card checkout. Enterprise needs custom quotes, procurement processes, and negotiation room.

Typical structure:
```
SMB tiers (NT$X–NT$Y/user/month):  published, self-serve
Enterprise:                         "Contact sales" — custom contract, annual commitment
```

Enterprise deals typically carry a 30–60% premium over the equivalent per-seat cost on the public pricing page, justified by SLA, onboarding, custom integrations, and security review.

**Do not publish Enterprise pricing.** The moment you anchor Enterprise at NT$999/user, you've created a ceiling expectation. Sales needs room to price NT$1,500–NT$2,000/user for large, complex accounts.

---

## Annual vs Monthly Billing: The Cash Flow Decision

Always offer annual billing with a discount. The standard discount is 15–20% (equivalent to 2 free months).

```
Annual plan value = Monthly × 12 × (1 − discount)
Example: NT$299/month × 12 × 0.83 = NT$2,978/year (vs NT$3,588 monthly)
```

Why this matters for pricing design:
1. **Cash flow**: annual billing provides capital upfront
2. **Churn reduction**: annual customers churn at 1/4 the rate of monthly customers (they have to make an active renewal decision once, not twelve times)
3. **Commit signal**: annual customers are more invested; they onboard more thoroughly

Make annual the **default selection** on the pricing page, with monthly as the alternative. The psychological default drives a meaningful % of customers to annual without reading the fine print.

---

## Worked Example: Pricing a B2B SaaS for Taiwan SMBs

**Product**: AI meeting notes tool for Taiwanese SMBs  
**Market**: Companies with 5–100 employees, Chinese-speaking users

### Step 1: Three Anchors

```
Cost floor: NT$80/user/month
  (AI inference cost + storage + customer support allocation)

Competitor reference:
  Otter.ai: ~NT$450/user/month (USD pricing, converted)
  Fireflies.ai: ~NT$380/user/month
  Local alternative: none at feature parity

Customer ceiling: NT$600/user/month
  (Based on 25 SMB interviews: 1 meeting/day × 20 min saved × NT$300/hr wage = NT$1,800/user/month value)
  (Target V/P ratio 3:1 for SMB — they're more price-sensitive than enterprise)
```

### Step 2: Tier Design

```
Starter   Free
  → 3 meetings/month, 30-min limit
  → Freemium acquisition channel

Pro       NT$249/user/month (annual: NT$2,490/year)
  → Unlimited meetings, full transcripts, action item extraction
  → Primary revenue tier

Team      NT$399/user/month (annual: NT$3,990/year)
  → Pro + team analytics, shared workspace, admin controls
  → Upsell for managers / ops teams
```

**Decoy check**: Starter is genuinely limited (3 meetings/month is enough for a trial, not a workflow). Pro at NT$249 is well below the NT$380–450 competitor range, creating a clear value signal. Team at NT$399 looks affordable next to competitors' base pricing.

### Step 3: Freemium Economics Check

```
Cost to serve 1 free user/month: NT$80 (at cost floor)
Target conversion rate: 6% (meeting tool category, product-led growth)
Conversion timeline: 90 days

For a cohort of 500 free users:
  Monthly cost = 500 × NT$80 = NT$40,000
  90-day total cost = NT$120,000
  Converted = 500 × 6% = 30 users
  Freemium CAC = NT$120,000 / 30 = NT$4,000

Acceptable if LTV > NT$4,000 × 3 = NT$12,000
  Pro plan annual = NT$2,490; need ~5 year retention to justify
  → Freemium may not work at NT$80/user cost floor unless conversion exceeds 10%
  → Consider limiting free tier to reduce serving cost (e.g., 1 meeting/week, lower quality transcript)
```

This math is the reason many SaaS products degrade free tier over time — not anticompetitive behavior, but unit economics forcing a rebalance.

### Step 4: NRR Design

```
Expansion levers built into pricing:
  - Adding team members → more seats → linear MRR growth
  - Team plan upgrade when manager joins → seat × price increase
  - Annual upgrade (15% discount but 12× upfront commitment)

Target NRR: 105%
  Achieved if: average account grows from 2.5 seats to 2.8 seats within 12 months
  (This is a modest assumption — 0.3 additional users per account over a year)
```

---

## Common SaaS Pricing Mistakes

**Setting per-seat price below cost floor after applying team discounts.** If you offer "50% off for teams of 10+", model the new effective per-seat price against your cost structure. A NT$299 plan discounted 50% for 10 seats = NT$1,495/month. At NT$80/user cost floor, cost is NT$800/month. Margin holds. But if cost floor is NT$160/user (larger AI inference), cost = NT$1,600 > revenue.

**Annual discount too deep.** 30–40% annual discount is common in hyper-competitive markets but destroys ARR predictability. 15–20% is standard; 25% maximum unless you have evidence it materially improves conversion rate.

**Free tier that cannibalizes paid.** If free users can export data, integrate with third-party tools, or invite unlimited collaborators, there's no forcing function to upgrade. Gate these specifically on paid tiers.

**Charging per seat for a product used by one person on behalf of many.** A social media scheduling tool used by one marketing manager for a 50-person company should not be priced per employee — it should be priced per workspace or per connected social account (usage metric).

**Ignoring price-tier cognitive load.** More than 4 public tiers creates analysis paralysis. If you need more segments, hide them behind "Compare all plans" or use an interactive pricing calculator rather than a static table.
