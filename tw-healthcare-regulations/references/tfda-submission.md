# TFDA Medical Device Submission — Procedures & Requirements

**衛生福利部食品藥物管理署 (TFDA)** is the sole regulatory body for medical device market authorization in Taiwan. This reference covers the end-to-end submission process, required dossiers, and practical timelines.

---

## Step 0: Confirm You Need TFDA Approval

Before preparing any submission, confirm your product is legally a "medical device" (醫療器材) under the **醫療器材管理法** (Medical Devices Act, enacted May 2021).

A product is a medical device if it meets **any** of these criteria:

| Trigger | Example |
|---------|---------|
| Diagnoses a disease or condition | Glucose meter, AI chest X-ray reader |
| Treats, mitigates, or cures a disease | Wound care device, pacemaker |
| Monitors a physiological parameter for clinical decision-making | Pulse oximeter, ECG monitor |
| Compensates for injury/disability | Prosthetic limb, cochlear implant |

**Wellness products are NOT medical devices** if they only track general fitness (step counts, sleep duration without clinical interpretation). However, once the product's labeling or marketing claims clinical benefit, it crosses the line. TFDA classifies by **intended use**, not hardware.

When in doubt, submit a **Pre-submission Inquiry (事前諮詢)** to TFDA — free, informal, ~4-week turnaround.

---

## Step 1: Determine Device Class

Taiwan uses a 3-class system. Misclassifying down (claiming Class I when TFDA deems Class II) triggers rejection and restarts the clock.

### Classification Rules

| Class | Risk Level | Control Level | Key Test |
|-------|------------|---------------|----------|
| I | Low | General controls only | Failure unlikely to cause serious harm |
| II | Medium | General + Special controls | Failure could cause reversible harm |
| III | High | General + Special + Premarket Approval | Failure could cause irreversible harm or death |

### SaMD Classification (Software as Medical Device)

Use the **IMDRF SaMD risk matrix** as TFDA follows it:

```
State of Healthcare Situation:
  Critical (life-threatening / irreversible) → Row A
  Serious (serious deterioration) → Row B
  Non-serious → Row C

SaMD Intended Use:
  Treat/Diagnose → Column I
  Drive clinical management → Column II
  Inform clinical management → Column III

Risk Category:
  A-I → Class IV (highest, mapped to Taiwan Class III)
  A-II, B-I → Class III
  A-III, B-II, C-I → Class II
  B-III, C-II, C-III → Class I
```

**Worked Example — AI Chest X-ray Reader:**
- Situation: Identifies pneumonia (serious deterioration) → Row B
- Intended use: Assists radiologist in diagnosis → Column II
- IMDRF Category: B-II → **Taiwan Class II or III** (TFDA currently treats autonomous AI decisions as Class III; assistive tools where physician confirms → Class II)

### Reference Classification Database

TFDA publishes classified device codes at **醫療器材分類分級查詢** (TFDA website). Search by product category to find the assigned 產品分類代碼 (product classification code). This code appears on your registration certificate.

---

## Step 2: Choose the Submission Route

| Route | Applies To | Key Difference |
|-------|------------|----------------|
| **Registration (登錄)** | Class I | Self-declaration; TFDA does not review dossier before listing |
| **Technical Review (查驗登記)** | Class II | TFDA reviews technical dossier; no clinical data usually required |
| **Premarket Approval (查驗登記 — 臨床)** | Class III | Full clinical evidence required; TFDA may request additional data |
| **510(k) Equivalence Pathway** | Class II/III with FDA 510(k) | TFDA may accept FDA 510(k) clearance to reduce review burden |
| **CE Mark Reliance** | Class II/III with EU MDR CE** | Partial reliance possible; TFDA still requires Taiwan-specific docs |

**Practical note on international recognition**: TFDA participates in IMDRF but does NOT rubber-stamp foreign approvals. FDA/CE acceptance shortens review by reducing the clinical evidence burden — it does not eliminate TFDA's own dossier requirements.

---

## Step 3: Assemble the Technical Dossier

### Class I Dossier (Registration)

Submitted online via **醫療器材登錄系統 (eQMDR)**. No pre-approval needed.

Required documents:
1. Product Chinese name and English name
2. Intended use statement (中文適應症)
3. Product specification (材質、尺寸、規格)
4. Manufacturing site information (address, QMS certification if applicable)
5. Labeling (Chinese-language draft)
6. Self-declaration of conformity

Timeline: 1–2 months (mostly administrative processing)

---

### Class II Technical Dossier

Submit via TFDA's **eQMDR** portal. Required sections:

```
Section 1 — Administrative Documents
  ├── Application form (TFDA 格式)
  ├── Agent authorization letter (if foreign manufacturer)
  ├── Manufacturing site license / ISO 13485 certificate
  └── Power of attorney

Section 2 — Device Description
  ├── Product description (intended use, principles of operation)
  ├── Classification justification with predicate/reference device
  └── Technical specifications

Section 3 — Design & Engineering Evidence
  ├── Design verification & validation (V&V) summary
  ├── Risk management file (per ISO 14971)
  ├── Electrical safety test reports (IEC 60601 series for electrical devices)
  ├── Biocompatibility (ISO 10993 for patient-contact materials)
  └── Software documentation (IEC 62304 if SaMD)

Section 4 — Performance Data
  ├── Bench testing results
  ├── Animal study data (if applicable)
  └── Clinical literature review OR clinical data (if required by TFDA)

Section 5 — Labeling
  ├── Chinese IFU (Instructions for Use)
  └── Label artwork

Section 6 — Post-Market Surveillance Plan
```

**IEC 62304 Requirement for SaMD**: If any software component contributes to clinical decisions, the full IEC 62304 software lifecycle documentation is mandatory. This includes architecture design, unit testing, integration testing, and anomaly tracking. TFDA reviewers increasingly request this even for Class II SaMD.

---

### Class III Technical Dossier

Includes everything in Class II, plus:

```
Section 7 — Clinical Evidence
  ├── Clinical investigation report (ICH E6 GCP-compliant)
  │   OR
  ├── Clinical literature + substantial equivalence justification
  └── Post-market clinical follow-up (PMCF) plan

Section 8 — Special Controls Compliance
  └── Specific to device type (TFDA guidance documents)
```

**Clinical Investigation in Taiwan**:
- Must be conducted at TFDA-recognized clinical trial sites
- Requires Institutional Review Board (IRB) approval first
- Site qualification typically takes 3–6 months
- GCP inspection by TFDA is common for high-risk devices
- Budget: NT$5M–NT$20M+ depending on indication and patient enrollment

---

## Step 4: Submit and Track

### Submission Portal: eQMDR

All Class II/III submissions go through **https://eqmdr.fda.gov.tw** (TFDA's online portal). Steps:

1. Create corporate account as 醫療器材商
2. Fill 申請書 online form, upload dossier PDFs
3. Pay submission fee (see below)
4. Receive 受理文號 (acceptance number) within 5 business days
5. TFDA assigns a 審查員 (reviewer); contact via the portal's messaging system

### Review Stages

```
Submission → Administrative Completeness Check (行政審查) → 10 business days
    ↓
Technical Review (技術審查) → 90-180 calendar days (Class II)
                             → 180-360 calendar days (Class III)
    ↓
Deficiency Letters (補正通知) → You have 60 days to respond per letter
    ↓ (may loop 2-3 times)
Approval → Issue 許可證 (Registration Certificate)
```

**Deficiency letter management**: TFDA typically issues 1–3 rounds of queries. Each query letter pauses the review clock. Average Class II submissions see 1–2 rounds. Respond with a **response matrix** table (question → answer → document reference) to reduce back-and-forth.

---

## Step 5: Fees

| Device Class | Application Fee |
|--------------|----------------|
| Class I (Registration) | NT$1,600 |
| Class II (Domestic manufacturer) | NT$17,000 |
| Class II (Foreign manufacturer) | NT$25,000 |
| Class III (Domestic manufacturer) | NT$42,000 |
| Class III (Foreign manufacturer) | NT$60,000 |
| Amendment (post-approval change) | NT$5,000–NT$15,000 |

*Fees are set by TFDA fee schedule and subject to revision. Verify at time of submission.*

---

## Step 6: Post-Approval Obligations

Receiving a 許可證 is not the end. Ongoing obligations:

| Obligation | Requirement |
|------------|-------------|
| 許可證 renewal | Every 5 years; requires post-market surveillance data |
| Adverse event reporting | Serious adverse events: 7 days; Others: 30 days to TFDA |
| Field safety corrective actions (FSCA) | Notify TFDA before executing recall |
| Manufacturing site changes | Prior approval required |
| Labeling changes | Prior approval if affecting safety/intended use |
| Annual QMS audit | ISO 13485 certificate must remain valid |

**Vigilance system**: Report via **醫療器材不良事件通報系統** (TFDA portal). Failure to report is a criminal offense under 醫療器材管理法 §68.

---

## Special Track: Foreign Manufacturer Without Taiwan Entity

Foreign companies without a Taiwan legal entity must appoint a **醫療器材商 (licensed medical device agent)** who:

- Holds a valid 醫療器材商許可執照
- Signs as the 申請人 on all TFDA submissions
- Takes legal responsibility for post-market obligations
- Typically charges 5–15% of Taiwan revenue as agent fee, or a flat annual retainer NT$100K–NT$500K

The foreign manufacturer signs an **授權書 (authorization letter)** notarized and apostilled in the country of manufacture.

---

## Worked Example: Class II Blood Glucose Monitor (BGM)

**Scenario**: A Singapore-based company wants to sell a Bluetooth BGM with companion app in Taiwan.

**Step 1 — Classification**:
- BGM hardware → Class II (product code: E-type 血糖計)
- Companion app → If it only displays readings, wellness product, no TFDA approval needed. If it calculates insulin dose adjustments → SaMD Class II or III.

**Step 2 — Dossier**:
- ISO 15197:2013 accuracy data (required for BGM)
- IEC 60601-1 + IEC 60601-1-2 (EMC)
- ISO 10993-1 biocompatibility (for lancet/test strip patient contact)
- IEC 62304 if app is co-submitted as SaMD
- CE Mark (EU MDR) → submit as supporting evidence to reduce clinical data burden

**Step 3 — Timeline**:
```
Month 1:    Appoint Taiwan agent, prepare dossier
Month 2-3:  Submit to TFDA via eQMDR
Month 4:    Administrative review complete, technical review begins
Month 7-9:  Deficiency letter round 1 → respond within 60 days
Month 10-14: Approval, receive 許可證
```

**Step 4 — Fees**:
- Foreign manufacturer: NT$25,000 submission fee
- Agent retainer: NT$150,000/year (typical for Class II)

**Step 5 — NHI strategy decision**:
- BGM strips are NHI-reimbursed for diagnosed diabetic patients
- Apply for 健保給付 after 許可證 is issued (separate NHIA process; see `references/nhi-reimbursement.md`)

---

## Key Regulatory Contacts

| Function | Contact |
|----------|---------|
| Device classification questions | 醫療器材組 第一科/第二科/第三科 |
| SaMD / AI device inquiries | TFDA 數位健康科技辦公室 |
| Pre-submission meeting request | eQMDR portal → 申請諮詢 |
| Post-market vigilance | 安全監視及查核組 |

**TFDA main office**: 11561 台北市南港區昆陽街161-2號

---

## Common Rejection Reasons

1. **Intended use mismatch**: Labeling claims differ from what the testing data supports. Keep intended use statement narrow and exactly matched to validated indications.
2. **Missing IEC 62304 for SaMD**: Submitting SaMD without software lifecycle documentation. TFDA increasingly requires this even when not explicitly listed in guidance.
3. **Foreign test reports without accreditation**: Lab reports from non-TAF or non-ILAC accredited labs may be rejected. Use ISO 17025-accredited labs.
4. **Incomplete risk management file**: Submitting a risk register without residual risk evaluation or benefit-risk conclusion per ISO 14971:2019.
5. **Chinese IFU errors**: Incorrect translation of contraindications or missing mandatory warnings triggers deficiency letters. Have a medical translator with regulatory experience review before submission.
6. **Outdated predicate device**: Citing a predicate that has been withdrawn or reclassified. Verify predicate is still on TFDA's valid list before submitting.
