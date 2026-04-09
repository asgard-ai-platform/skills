# AML/KYC Implementation Checklist — Taiwan Fintech

> **Governing laws**: 洗錢防制法 (Money Laundering Control Act), 資恐防制法 (Counter-Terrorism Financing Act), and FSC-issued implementation regulations. This checklist follows the risk-based approach required by FATF and adopted by Taiwan's 法務部調查局.

---

## 1. KYC Level Decision Tree

Assign every customer to a KYC tier **before** onboarding:

```
START
  │
  ├─ Is the customer a PEP (政治上重要人物) or their family/associate?
  │     YES → Enhanced KYC (mandatory, no exceptions)
  │
  ├─ Is the customer from an FATF high-risk jurisdiction?
  │     YES → Enhanced KYC
  │
  ├─ Is the expected monthly transaction volume > NT$500,000?
  │     YES → Standard KYC (minimum); review for Enhanced
  │
  ├─ Will the customer hold stored value (e-wallet balance)?
  │     YES → Standard KYC
  │
  ├─ Pass-through payments only AND transaction < NT$30,000/day?
  │     YES → Simplified KYC permissible
  │
  └─ Default → Standard KYC
```

**Re-tier triggers**: re-assess KYC tier whenever: (a) transaction volume rises above the threshold, (b) geographic patterns change, (c) suspicious activity is detected, or (d) annually for dormant accounts.

---

## 2. Simplified KYC (低風險客戶)

**When eligible**: pass-through payments, transaction < NT$30,000/day, domestic user, no PEP indicators.

| Data point | Acceptable source |
|------------|-------------------|
| Full name (姓名) | Self-declared |
| National ID number (身分證字號) | Self-declared; validate check digit |
| Date of birth | Self-declared |
| Mobile number | OTP verification |

**Identity validation (minimum)**:

1. Run National ID number through check-digit algorithm (see §7 below).
2. Verify mobile number is not flagged on telecom fraud blacklist (165 反詐騙 API if available, or Twilio Lookup).
3. Screen name + DOB against 制裁名單 (see §5).

**Stored value limit**: NT$10,000 balance cap applies to simplified-tier users under 電子支付機構管理條例.

---

## 3. Standard KYC (一般客戶)

**When required**: e-wallet accounts, any stored value, P2P transfers, transaction volume > NT$30,000/day.

### 3a. Identity Document Collection

| Customer type | Primary document | Secondary document |
|---------------|-----------------|-------------------|
| ROC citizen (本國人) | 中華民國身分證 (both sides) | optional |
| Foreign national (外國人) | 居留證 (ARC/APRC) | Passport (data page) |
| Corporate (法人) | 公司登記謄本 (< 3 months old) | 負責人身分證 |

**Liveness check (活體驗證)**: for digital onboarding, a selfie-with-ID or video liveness check is required. Acceptable methods:
- Certified eKYC providers (e.g., TWID, iSunFa)
- Bank-account micro-deposit binding (bind to a verified bank account; account holder name must match)

### 3b. Additional Data Required

- Residential address (居住地址) — verified via correspondence or utility bill (< 6 months)
- Occupation (職業) — self-declared; used for source-of-funds plausibility
- Source of funds (資金來源): one of `{salary, business income, investment, inheritance, other}`

### 3c. Verification Steps

```
Step 1: OCR / manual entry of ID document data
Step 2: Check-digit validation of ID number
Step 3: JCIC (聯合徵信中心) or equivalent — confirm ID not reported lost/stolen
          → If JCIC API unavailable: require bank account binding as proxy
Step 4: Sanctions screening (see §5)
Step 5: PEP screening (see §6)
Step 6: Adverse media check (manual or vendor API)
Step 7: Record result + timestamp; store document image encrypted
```

---

## 4. Enhanced KYC (高風險客戶)

**Triggers**: PEP status, high-risk jurisdiction, transaction patterns inconsistent with stated occupation, or manual escalation.

### 4a. Additional Data Required (on top of Standard)

- Detailed source of wealth (財富來源): supporting documents (pay stubs, company financials, asset sale contracts)
- Purpose of account (開戶目的): specific business use case, not just "payment"
- Beneficial owner (實際受益人): for corporate accounts, identify any natural person owning ≥ 25% or exercising effective control
- Expected transaction profile: estimated monthly volume, average transaction size, counterparties

### 4b. Approval Process

- EDD (Enhanced Due Diligence) must be approved by a **senior compliance officer** — not automated.
- Document the approval rationale in the customer file.
- Review frequency: **every 6 months** (vs. 12 months for Standard, 24 months for Simplified).

### 4c. PEP Handling

PEP = 政治上重要人物 as defined in 洗錢防制法 §7:

- Senior government officials (minister level and above)
- Legislators, judges, senior military officers
- SOE executives
- Senior officials of international organizations
- Immediate family (spouse, parents, children, siblings) and known close associates

**PEP policy**: EDD + senior approval + continuous monitoring + **no** automated payment clearing (manual review queue for transactions > NT$50,000).

---

## 5. Sanctions Screening

Screen **every customer** at onboarding and **continuously** against:

| List | Description | Update frequency |
|------|-------------|-----------------|
| 法務部調查局 — 制裁名單 | Taiwan domestic sanctions | Daily (pull via official CSV or API) |
| OFAC SDN List | US Treasury, applies to USD-touched transactions | Daily |
| UN Consolidated List | UN Security Council sanctions | Check weekly |
| EU Consolidated List | Applies if any EUR flows | Check weekly |

**Fuzzy matching rule**: flag any name similarity score ≥ 80% (Jaro-Winkler or equivalent). Do NOT use exact-string match only — transliteration variants will slip through.

**Hit resolution process**:
1. Flag → freeze account action
2. Compliance reviews within 1 business day
3. True match → report to 法務部調查局 within **10 business days** (洗錢防制法 §10)
4. False positive → document dismissal rationale and unfreeze

---

## 6. Transaction Monitoring (持續監控)

### 6a. Rule-Based Triggers (minimum required)

| Rule | Threshold | Action |
|------|-----------|--------|
| Single transaction cash equivalent | > NT$500,000 | CTR (大額通貨交易報告) |
| Aggregated transactions (same day, same customer) | > NT$500,000 | CTR |
| Single transfer to/from foreign account | > NT$500,000 | CTR |
| Structuring pattern | Multiple transactions just below NT$500,000 within 3 days | STR review |
| Velocity anomaly | > 3× customer's 30-day average volume | Alert |
| Geographic anomaly | Transaction origin country differs from KYC address | Alert |
| Dormant account reactivation | No activity > 6 months, then sudden large transaction | Alert |
| Round-number pattern | ≥ 5 round-number transactions in 7 days | Alert |

### 6b. CTR vs STR — Key Distinction

| Report type | Chinese name | Threshold | Deadline | Recipient |
|-------------|-------------|-----------|----------|-----------|
| CTR | 大額通貨交易報告 | ≥ NT$500,000 cash equivalent | **5 business days** after transaction | 法務部調查局 |
| STR | 可疑交易報告 | No threshold — based on suspicion | **10 business days** after detection | 法務部調查局 |

**STR is judgment-based**: there is no monetary floor. If a NT$1,000 transaction pattern is suspicious (e.g., smurfing), file an STR. Failure to file when suspicion exists is a compliance violation regardless of amount.

### 6c. STR Filing — Step-by-Step

```
1. Alert triggered (automated rule or staff report)
2. Level 1 review: AML analyst (48 hours)
   - Document: what triggered, what was found, why suspicious
   - Decision: escalate / dismiss with rationale
3. Level 2 review: Chief Compliance Officer (48 hours)
   - Final decision to file STR or dismiss
4. If filing:
   a. Complete 申報書 via 法務部調查局 洗錢防制系統 (online portal)
   b. Do NOT tip off customer (tipping-off offense under 洗錢防制法 §10-1)
   c. Log filing internally: date, reference number, reviewing officer
5. Retain STR record + supporting evidence: 5 years
```

---

## 7. Taiwan National ID Check-Digit Algorithm

Use this to catch typos before hitting any external service:

```python
def validate_tw_id(id_str: str) -> bool:
    """
    Validates a Taiwan National ID number (身分證字號).
    Format: 1 letter + 9 digits (e.g., A123456789)
    """
    id_str = id_str.strip().upper()
    if len(id_str) != 10:
        return False

    letter_map = {
        'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,
        'I':34,'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,
        'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,
        'Y':31,'Z':33
    }

    if id_str[0] not in letter_map:
        return False
    if not id_str[1:].isdigit():
        return False

    code = letter_map[id_str[0]]
    digits = [code // 10, code % 10] + [int(c) for c in id_str[1:]]
    # weights: 1,9,8,7,6,5,4,3,2,1,1
    weights = [1,9,8,7,6,5,4,3,2,1,1]
    total = sum(d * w for d, w in zip(digits, weights))
    return total % 10 == 0


# Examples:
# validate_tw_id("A123456789") → True  (standard test vector)
# validate_tw_id("A123456788") → False
# validate_tw_id("F131104093") → True
```

**Note**: This validates format and check digit only. It does NOT confirm the ID is issued to a real person or that it is not lost/stolen. Always follow up with JCIC or bank-binding verification.

---

## 8. Record Retention Requirements

| Record type | Retention period | Format |
|-------------|-----------------|--------|
| KYC documents (ID images, forms) | 5 years after account closure | Encrypted storage; accessible to compliance |
| Transaction records | 5 years after transaction date | Immutable audit log |
| CTR filings | 5 years | Archive with 調查局 reference number |
| STR filings | 5 years | Archive; do NOT disclose to customer |
| Risk assessment decisions | 5 years | Include rationale and approving officer |
| Sanctions screening results | 5 years | Include hit/dismiss rationale |

**Deletion policy**: do not delete KYC records to comply with GDPR/PDPA requests if a legal hold or AML retention obligation applies. AML obligations take precedence; note the conflict in the customer record.

---

## 9. High-Risk Jurisdiction List (reference)

FATF's current "call for action" (黑名單) and "increased monitoring" (灰名單) jurisdictions require Enhanced KYC. As of 2024:

**Black list (拒絕往來 or EDD + senior approval + case-by-case):**
- DPRK (North Korea)
- Iran
- Myanmar

**Grey list (EDD required):** check FATF website for current list — changes quarterly. Recent additions/removals include Bulgaria, Cameroon, Vietnam (verify current status).

**Taiwan-specific risk**: China (中國) is treated as a high-risk jurisdiction for AML purposes in Taiwan due to separate regulatory concerns. Apply Enhanced KYC for customers or beneficial owners with PRC residency or domicile.

---

## 10. Common Implementation Mistakes

- **Exact-name sanctions matching**: "Wang Wei" ≠ "Wang, Wei" ≠ "王威" — use transliteration-aware fuzzy matching with a configurable threshold.
- **One-time screening only**: sanctions lists update daily. Continuous re-screening of the existing customer base is mandatory, not just at onboarding.
- **Tipping off**: never tell a customer their account is frozen due to STR review. Freeze silently; communicate only after 調查局 clears the case or instructs otherwise.
- **Corporate KYC stops at the entity**: you must identify **natural person** beneficial owners (≥ 25% or effective control) for all corporate accounts. Shell company chains must be traced to a human.
- **Relying solely on bank-account binding for identity**: bank binding confirms the person holds that account, not that their identity documents are genuine. For Standard KYC and above, document verification is still required.
- **Treating sandbox as AML-exempt**: the regulatory sandbox exempts you from licensing. It does **not** exempt you from AML/CFT obligations. File CTRs and STRs from day one of sandbox operation.
