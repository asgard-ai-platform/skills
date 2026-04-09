# NHI Reimbursement Application Process

Taiwan's National Health Insurance reimbursement is the central commercial lever for any healthcare product. Getting listed means access to 23 million covered lives; not getting listed means competing on self-pay in a market where patients expect coverage.

## The Two Reimbursement Tracks

NHI reimbursement splits by product type:

| Track | Products | Governing body | Price-setting mechanism |
|-------|----------|----------------|------------------------|
| **藥品 (Drugs)** | Prescription drugs, biologics, vaccines | 健保署藥物共同擬訂會議 | DET (Drug Expenditure Target) adjustment + negotiation |
| **醫療器材 (Medical devices)** | TFDA-approved devices, SaMD | 健保署 | Application + committee review + NHI fee schedule |

Both tracks require TFDA product approval **first**. Reimbursement cannot be applied for before TFDA registration is complete.

---

## Drug Reimbursement Path

### Step-by-Step Procedure

```
Step 1: TFDA 藥品許可證 obtained
         ↓
Step 2: File 健保藥品給付申請 with NHIA
         (application + dossier)
         ↓
Step 3: 藥物共同擬訂會議 (Joint Drug Committee) review
         Pharmacoeconomics review committee evaluates:
         - Clinical evidence
         - Cost-effectiveness
         - Budget impact
         ↓
Step 4: Price negotiation (for new drugs)
         NHIA proposes price based on:
         - International reference prices (IRP)
         - Comparator drug prices on NHI list
         ↓
Step 5: Inclusion in 全民健康保險藥品給付規定 (NHI Drug Benefit List)
         ↓
Step 6: Subject to periodic DET adjustment (annual review)
```

### Timeline Estimates

| Stage | Typical Duration |
|-------|-----------------|
| Application preparation | 3-6 months |
| Committee review | 6-12 months |
| Price negotiation | 3-6 months |
| **Total from TFDA approval to NHI listing** | **12-24 months** |

New molecular entities and biologics trend toward the longer end. Generic equivalents and line extensions are faster.

### International Reference Pricing (IRP)

NHIA benchmarks new drug prices against a basket of reference countries. The current basket includes:

- USA (Medicare/Medicaid published price)
- UK (NHS list price)
- Japan
- Germany
- Australia
- Canada

**How NHIA uses IRP**: The median or lowest price in the basket becomes the ceiling for initial negotiations. A drug priced at US$10,000/year in the US will not receive NT$300,000/year reimbursement in Taiwan — expect significant downward adjustment.

**Worked example — oncology drug:**

Assume a new targeted therapy:
- US WAC price: USD 8,500/month
- UK NHS negotiated: GBP 4,200/month (~USD 5,300)
- Japan approved: JPY 680,000/month (~USD 4,500)

NHIA reference band: USD 4,500–5,300/month equivalent  
After negotiation (expect 20-40% reduction from lowest reference): **~NT$100,000–130,000/month**

This is the starting point. Volume-based risk-sharing arrangements can adjust the effective price downward further.

---

## Drug Expenditure Target (DET)

DET is NHIA's mechanism for controlling total drug spend. It operates as a **volume-price trade-off**: when aggregate drug expenditure exceeds the annual budget target, prices are revised down across the board.

### DET Formula

```
Adjustment Rate = (Actual Spend - DET Budget) / Actual Spend

If Adjustment Rate > 0: prices are cut by that percentage
If Adjustment Rate ≤ 0: no adjustment (prices never go up via DET)
```

**Example:**
- DET Budget for year: NT$120 billion
- Actual drug spend: NT$126 billion
- Adjustment Rate = (126 - 120) / 126 = **4.76%**
- All NHI drug prices reduced by 4.76% in next review cycle

This is not a hypothetical — DET adjustments of 3-7% have been common. Over a 5-year period, cumulative price erosion can exceed 20%.

### Business Impact of DET

For a drug generating NT$500M/year in NHI revenue at launch:

| Year | DET Cut (assumption) | Cumulative Price | Revenue |
|------|----------------------|-----------------|---------|
| 1 | — | 100% | NT$500M |
| 2 | 4% | 96% | NT$480M |
| 3 | 5% | 91.2% | NT$456M |
| 4 | 3% | 88.5% | NT$443M |
| 5 | 4% | 85.0% | NT$425M |

Revenue erosion even with flat volume. This is the "relentless NHI price pressure" from the IRON LAW in action.

**Mitigation strategies:**
- Build volume growth projections that outpace price decline
- Negotiate risk-sharing or managed entry agreements with NHIA that lock in price for defined periods
- Pursue self-pay premium positioning for new indications rather than NHI expansion

---

## Medical Device Reimbursement Path

Medical device reimbursement follows a separate track with different pricing logic.

### Step-by-Step Procedure

```
Step 1: TFDA 醫療器材許可證 obtained
         ↓
Step 2: Determine if device has existing NHI fee code
         ├── YES → Apply for price listing under existing code
         └── NO → Apply for new procedure/device code creation
         ↓
Step 3: File application with 健保署
         Required documents:
         - TFDA certificate
         - Product specifications + clinical evidence
         - Pricing justification (cost breakdown + comparable products)
         - Budget impact analysis
         ↓
Step 4: 健保會 (National Health Insurance Committee) review
         ↓
Step 5: Listed in 全民健康保險醫療服務給付項目及支付標準
         (NHI Medical Service Benefit and Payment Schedules)
```

### NHI Fee Schedule Logic for Devices

Unlike drugs, device reimbursement is often **bundled into procedure codes** rather than separate device codes. This distinction matters for revenue modeling:

| Reimbursement type | How it works | Example |
|-------------------|-------------|---------|
| **Procedure-bundled** | Device cost embedded in surgical/procedure fee | Hip replacement: total procedure fee covers implant |
| **Separate device code** | Device has its own NHI code billed independently | Cardiac stent: separate code from catheterization procedure |
| **Consumable listing** | Listed as consumable with per-unit NHI price | Surgical sutures, wound dressings |

For innovative devices without a comparable procedure code, the application must create a new code — this requires demonstrating clinical differentiation and goes through a more intensive committee review.

### Cost-Effectiveness Requirement

NHIA increasingly requires Incremental Cost-Effectiveness Ratio (ICER) analysis for Class II/III devices:

```
ICER = (Cost_new - Cost_comparator) / (Outcome_new - Outcome_comparator)

Where Outcome is measured in QALYs (Quality-Adjusted Life Years)

NHIA informal threshold: NT$1,000,000-1,500,000 per QALY gained
(This threshold is not officially published but reflects committee decisions)
```

**Worked example — AI diagnostic device:**

A Class II SaMD for diabetic retinopathy screening:
- Annual cost per patient: NT$3,000 (vs. NT$1,500 for current manual screening)
- Incremental cost: NT$1,500/patient/year
- Clinical outcome: detects 15% more cases early, preventing 0.02 QALYs lost per patient

ICER = NT$1,500 / 0.02 QALY = **NT$75,000 per QALY**

This ICER is well below the informal NT$1M threshold → favorable for reimbursement consideration. The budget impact analysis (how many patients × NT$1,500 extra) still matters for affordability review.

---

## Risk-Sharing and Managed Entry Agreements (MEAs)

For high-cost products (specialty drugs, Class III devices), NHIA may offer MEAs instead of flat-rate reimbursement.

### Common MEA Structures in Taiwan

| Structure | Mechanism | When used |
|-----------|-----------|-----------|
| **Outcome-based** | Full reimbursement if patient responds; partial/no payment if not | Oncology drugs with measurable response criteria |
| **Volume cap** | Full price up to X patients; discounted beyond cap | Budget-sensitive launches |
| **Finance-based** | Simple price discount with volume commitment | Generics, established devices |
| **Coverage with evidence development** | Conditional listing while real-world data collected | Innovative SaMD, new therapeutic areas |

MEA negotiations occur **after** the committee approves the product in principle but before final listing. Expect 3-6 additional months for MEA negotiation.

---

## Reimbursement Dossier: Required Components

For drug applications:

```
1. 藥品基本資料 (Basic product data)
   - TFDA registration number
   - ATC code
   - Indication(s) for which reimbursement is sought

2. 臨床療效文獻 (Clinical efficacy evidence)
   - Pivotal clinical trials
   - Systematic reviews / meta-analyses
   - Taiwan-specific data if available (required for some categories)

3. 藥物經濟分析 (Pharmacoeconomic analysis)
   - Cost-effectiveness model
   - Budget impact analysis (5-year projection)
   - Sensitivity analysis

4. 國際價格調查 (International price survey)
   - Prices in IRP basket countries
   - Source documents (official formularies, not company data)

5. 建議給付條件 (Proposed coverage conditions)
   - Patient eligibility criteria
   - Prescriber restrictions (e.g., specialist only)
   - Diagnostic prerequisites

6. 風險管理計畫 (Risk management plan)
   - Post-market surveillance commitments
   - Pharmacovigilance plan
```

---

## Self-Pay Strategy: When NHI Reimbursement Is Not the Goal

Not every product should pursue NHI reimbursement. Self-pay (自費) positioning makes sense when:

- Product is lifestyle/wellness adjacent (grey zone — TFDA not requiring device approval)
- Margin would be unsustainable at NHI reimbursement prices
- Target patient population is concentrated in high-income segments
- Product differentiation is rapid (NHI listing process too slow for product iterations)
- Product is a companion to NHI-covered procedure but provides premium experience

**Self-pay pricing benchmark:**

In Taiwan's self-pay market, willingness-to-pay is anchored by:
- Comparison to Japan (perceived quality benchmark) — products can often price at 60-80% of Japan self-pay price
- Comparison to cosmetic procedures (reference class for elective spending): NT$30,000–200,000 is common comfort zone for medical tourism / elective procedures
- Monthly subscription ceiling for digital health apps in Taiwan consumer market: NT$300–1,200/month without NHI; NT$2,000–5,000/month for corporate B2B

---

## Common Rejection Reasons and Remedies

| Rejection reason | Remedy |
|-----------------|--------|
| Insufficient clinical evidence from Taiwan population | Budget Taiwan RWE study; use surrogate endpoints if accepted |
| ICER exceeds threshold | Restructure as MEA with outcome-based risk-sharing |
| Budget impact too high | Propose patient eligibility restrictions to narrow population |
| Pricing not aligned with IRP basket | Revisit international pricing strategy; consider tiered pricing |
| Comparable product already reimbursed at lower price | Demonstrate clinically meaningful differentiation |
| Application incomplete | Engage 法規事務顧問 (regulatory affairs consultant) for dossier review before submission |

---

## Key Contacts and Official Sources

| Resource | URL / Contact |
|----------|--------------|
| NHIA official portal | www.nhi.gov.tw |
| NHI Drug Benefit List (查詢健保藥品) | 健保署藥品查詢 |
| NHI Fee Schedule (醫療服務給付項目) | 健保署給付規定查詢 |
| DET adjustment announcements | Published in 健保署公告 each April |
| Regulatory affairs consultants | 中華民國醫療器材商業同業公會 maintains referral list |

> **Note**: This document reflects general understanding of NHIA processes as of early 2026. Taiwan's NHI reimbursement rules evolve frequently — verify current requirements at www.nhi.gov.tw or with a licensed regulatory affairs consultant before filing any application.
