# PCI DSS Compliance Checklist for Taiwan PSP Integrations

PCI DSS (Payment Card Industry Data Security Standard) applies to any system that stores, processes, or transmits cardholder data. This file helps you determine your scope and the minimum actions required.

---

## Step 1 — Determine Your Scope (This Changes Everything)

The single most important PCI decision: **do you touch raw card data?**

| Integration Pattern | Card Data Contact | Your PCI Level |
|--------------------|------------------|----------------|
| PSP-hosted payment page (redirect) | Never — customer enters card on PSP's page | **SAQ A** (lightest) |
| PSP inline iframe / hosted fields | Card data stays in PSP iframe, never hits your server | **SAQ A-EP** (moderate) |
| Your own payment form → PSP API | Raw PAN hits your server before PSP | **SAQ D** (heaviest) |
| Storing card numbers in your DB | You store PANs | **SAQ D + annual QSA audit** |

**Recommendation for Taiwan startups**: Always use PSP-hosted redirect (綠界/NewebPay/TapPay all support this). You drop from 300+ controls (SAQ D) to ~14 controls (SAQ A).

---

## Step 2 — Identify Which SAQ Applies

SAQ = Self-Assessment Questionnaire. You self-certify annually.

### SAQ A — PSP-Hosted Redirect (Most Common in Taiwan)

**Eligibility criteria (must meet ALL):**
- Card transactions fully outsourced to a PCI DSS–validated third-party PSP
- Your site does not receive, transmit, or store cardholder data
- Your payment page redirects to PSP or loads PSP-hosted iframe
- No electronic cardholder data storage on any system in your environment

**綠界/藍新/TapPay all qualify you for SAQ A** when using their redirect flow.

**SAQ A has 14 requirements.** Full checklist in Step 3.

### SAQ A-EP — JavaScript-Based Hosted Fields

**Eligibility criteria:**
- You use a PSP-provided JavaScript widget that posts card data directly to PSP
- Your page loads the payment fields but card data never transits your server
- Applies to TapPay's SDK-based integration, or any "direct post" pattern

**SAQ A-EP has ~130 requirements** — still much lighter than SAQ D but requires a vulnerability scan.

### SAQ D — Avoid If Possible

You land here if your server ever receives a raw card number (PAN). This requires:
- All 12 PCI DSS requirement domains
- Quarterly external vulnerability scans by an ASV (Approved Scanning Vendor)
- Annual penetration test
- File integrity monitoring
- Formal security policies

If you're considering SAQ D, reconsider your architecture first.

---

## Step 3 — SAQ A Checklist (PSP Redirect Flow)

This is the checklist for the most common Taiwan integration pattern: redirect to 綠界/藍新/TapPay payment page.

### Requirement 2 — Do Not Use Vendor-Supplied Defaults

- [ ] Change all default passwords on servers, routers, and admin panels
- [ ] Disable unnecessary services/ports on your web server
- [ ] Remove or disable default accounts that are not needed (e.g., default MySQL `root` login from remote)

**Concrete check:**
```bash
# Confirm no default SSH password auth (use key-based only)
grep "PasswordAuthentication" /etc/ssh/sshd_config
# Should return: PasswordAuthentication no
```

### Requirement 6 — Develop and Maintain Secure Systems

- [ ] All software (OS, PHP/Node/Python runtime, frameworks) is on supported versions receiving security patches
- [ ] Apply security patches within 1 month of release for critical vulns; within 3 months for others
- [ ] Your payment redirect page is free of XSS and injection vulnerabilities

**Minimum patch cadence table:**

| Component | Critical Patch SLA | High Patch SLA |
|-----------|-------------------|----------------|
| OS (Ubuntu/RHEL) | 7 days | 30 days |
| Web framework (Laravel/Next.js) | 14 days | 30 days |
| Database (MySQL/Postgres) | 14 days | 30 days |
| SSL/TLS library (OpenSSL) | 7 days | 14 days |

### Requirement 8 — Identify and Authenticate Access

- [ ] Unique user IDs for every person with access to your server/admin dashboard — no shared accounts
- [ ] Passwords for admin accounts: minimum 12 characters, complexity required
- [ ] MFA enabled on all admin interfaces (your hosting panel, server SSH)
- [ ] Lock out accounts after 6 failed login attempts; unlock only after 30 minutes or admin action
- [ ] Review and revoke access for departed employees within 24 hours

### Requirement 9 — Restrict Physical Access

- [ ] If using a physical server or office: lock the server room
- [ ] If using cloud (AWS/GCP/Azure): your cloud provider handles the physical datacenter — document this

> If you're on AWS/GCP/Azure/Hinet Cloud, physical requirement 9 is largely handled by the cloud provider under their PCI DSS certification. Keep a copy of their Attestation of Compliance (AOC) — auditors will ask for it.

### Requirement 12 — Maintain an Information Security Policy

- [ ] A written security policy exists (even a 1-page doc counts for SAQ A)
- [ ] Policy reviewed annually
- [ ] All employees with system access have read and acknowledged the policy
- [ ] Incident response plan exists: who to call if there's a breach, within what timeframe

**Minimal policy template (SAQ A):**
```
Security Policy — [Company Name] — v1.0 — [Date]

1. Access Control: Unique accounts for all staff. MFA on all admin systems.
2. Patch Management: Critical patches within 14 days, others within 30 days.
3. Incident Response: Security incidents reported to [Name] within 24 hours.
   Suspected card data breach: notify PSP and acquiring bank within 72 hours.
4. Third-Party PSP: We use [PSP Name] for all card processing. We do not
   store, transmit, or process card numbers ourselves.
5. Annual Review: This policy reviewed each [month] by [Name/Role].

Signed: ___________________  Date: ___________
```

---

## Step 4 — SSL/TLS Requirements

Applies regardless of SAQ level.

### Minimum TLS Configuration

- [ ] TLS 1.2 minimum on all payment-adjacent endpoints; TLS 1.3 preferred
- [ ] TLS 1.0 and 1.1 **disabled** (deprecated by PCI DSS v4.0, required off by March 2025)
- [ ] SSL 2.0 and 3.0 disabled
- [ ] Weak cipher suites disabled

**Test your TLS config:**
```bash
# Quick test with openssl
openssl s_client -connect yourdomain.com:443 -tls1_1
# Should return: handshake failure (meaning TLS 1.1 is correctly rejected)

# Or use ssllabs.com — aim for grade A or A+
```

**Acceptable cipher suites (whitelist):**
```
TLS_AES_128_GCM_SHA256          (TLS 1.3)
TLS_AES_256_GCM_SHA384          (TLS 1.3)
TLS_CHACHA20_POLY1305_SHA256    (TLS 1.3)
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256   (TLS 1.2)
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384   (TLS 1.2)
```

**Forbidden cipher suites:**
```
TLS_RSA_WITH_RC4_*              (RC4 forbidden)
TLS_*_WITH_DES_*                (DES forbidden)
TLS_*_WITH_3DES_*               (3DES forbidden since PCI DSS 3.2.1)
TLS_RSA_WITH_AES_*              (No forward secrecy — avoid)
```

**Nginx config snippet:**
```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384;
ssl_prefer_server_ciphers on;
ssl_session_timeout 10m;
ssl_session_cache shared:SSL:10m;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

---

## Step 5 — Webhook Signature Verification

This is the one PCI-adjacent control most Taiwan developers skip. **Always verify the PSP's callback signature before trusting the payment result.**

### 綠界 (ECPay) CheckMacValue Verification

ECPay signs callbacks using HMAC-SHA256 (or SHA1 for legacy). Verify before updating order status:

```python
import hashlib
import urllib.parse

def verify_ecpay_callback(params: dict, hash_key: str, hash_iv: str) -> bool:
    """
    Verify ECPay callback CheckMacValue.
    params: dict of all callback parameters (including CheckMacValue)
    """
    received_mac = params.pop("CheckMacValue", None)
    if not received_mac:
        return False

    # Step 1: Sort parameters alphabetically (case-insensitive)
    sorted_params = sorted(params.items(), key=lambda x: x[0].lower())

    # Step 2: Build query string
    raw = "&".join(f"{k}={v}" for k, v in sorted_params)

    # Step 3: Prepend HashKey, append HashIV
    raw = f"HashKey={hash_key}&{raw}&HashIV={hash_iv}"

    # Step 4: URL encode (lowercase)
    raw = urllib.parse.quote_plus(raw).lower()

    # Step 5: SHA256 hash, uppercase
    computed_mac = hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()

    return computed_mac == received_mac.upper()
```

**NEVER skip this check.** Without it, an attacker can POST a fake "payment successful" callback to your webhook and get goods/services for free.

### 藍新 (NewebPay) Verification

NewebPay uses AES-256-CBC encryption for its callback data:

```python
from Crypto.Cipher import AES
import hashlib
import json

def decrypt_newebpay_trade_info(
    trade_info: str,
    hash_key: str,
    hash_iv: str
) -> dict:
    key = hash_key.encode("utf-8")
    iv = hash_iv.encode("utf-8")
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(bytes.fromhex(trade_info))
    
    # Remove PKCS7 padding
    pad_len = decrypted[-1]
    decrypted = decrypted[:-pad_len]
    
    # Parse query string result
    return dict(urllib.parse.parse_qsl(decrypted.decode("utf-8")))

def verify_newebpay_sha(trade_info: str, trade_sha: str, hash_key: str, hash_iv: str) -> bool:
    raw = f"HashKey={hash_key}&{trade_info}&HashIV={hash_iv}"
    computed = hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()
    return computed == trade_sha.upper()
```

---

## Step 6 — Idempotent Webhook Handler

PCI DSS Requirement 6 (secure development) + operational reality: PSPs retry callbacks. Your handler must be idempotent.

```python
def handle_payment_callback(trade_no: str, payment_status: str, amount: int):
    """
    Idempotent payment callback handler.
    trade_no: your order ID
    """
    order = Order.query.filter_by(trade_no=trade_no).first()
    
    if order is None:
        logger.error(f"Unknown trade_no: {trade_no}")
        return "OK"  # Return OK to prevent PSP from retrying indefinitely
    
    # IDEMPOTENCY CHECK: Already processed?
    if order.payment_status == "paid":
        logger.info(f"Duplicate callback for {trade_no}, ignoring")
        return "OK"  # Already handled, PSP just retrying
    
    if payment_status == "1":  # ECPay success code
        if order.amount != amount:
            logger.error(f"Amount mismatch for {trade_no}: expected {order.amount}, got {amount}")
            # Do NOT mark as paid — potential fraud
            return "OK"
        
        order.payment_status = "paid"
        order.paid_at = datetime.utcnow()
        db.session.commit()
        trigger_fulfillment(order)
    
    return "OK"
```

**Key rules:**
1. Return `"OK"` (or `"1|OK"` for ECPay) in all cases — if you return an error, PSP will retry
2. Check current status before updating — never double-fulfill
3. Verify the amount matches your order record

---

## Step 7 — Annual Self-Assessment Checklist

Run through this once per year for SAQ A compliance:

**Infrastructure**
- [ ] All server OS versions checked — no EOL systems (e.g., Ubuntu 18.04 reached EOL April 2023)
- [ ] TLS configuration re-tested with ssllabs.com
- [ ] All admin passwords rotated in the past 12 months
- [ ] Access list reviewed: revoke accounts for people who left

**Code**
- [ ] Webhook signature verification still present and tested
- [ ] Idempotency logic tested with duplicate callbacks
- [ ] Dependencies scanned for known CVEs (e.g., `npm audit`, `pip-audit`, `composer audit`)
- [ ] No card numbers logged anywhere — grep your log files: `grep -r "[0-9]\{13,16\}" /var/log/`

**Documentation**
- [ ] Security policy updated and re-signed
- [ ] PSP's current AOC (Attestation of Compliance) on file — download from ECPay/NewebPay merchant portal annually
- [ ] Incident response contacts still accurate

**Third-Party Validation**
- [ ] Confirm your PSP is still on the PCI DSS list of validated service providers: [Visa Global Registry](https://www.visa.com/splisting/), [Mastercard SDP](https://www.mastercard.us/en-us/business/overview/safety-and-security/security-recommendations/site-data-protection-PCI/merchants/service-provider-directory.html)

---

## Common Mistakes That Fail PCI Audits

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| Logging full order payloads including card-adjacent fields | Log inspection may reveal sensitive data | Scrub logs: never log `CardNo`, `CVV`, full PAN |
| Using the same MerchantID in test and production | Prod keys in test environment = scope expansion | Separate accounts; never use prod credentials in dev/staging |
| Not rotating HashKey/HashIV after a suspected breach | Compromised keys allow forged callbacks | Rotate immediately if breach suspected; document rotation procedure |
| Storing `TradeNo` without ensuring uniqueness | ECPay rejects duplicate TradeNos; dev teams reuse them | Use UUID or `order_id + timestamp` pattern |
| HTTP fallback on payment callback endpoint | PSP may send callback to HTTP; man-in-the-middle possible | Force HTTPS with HSTS; reject HTTP on callback URL |
| Not validating the `RtnCode`=1 (ECPay) before fulfilling | Code 800 = ATM account issued, not paid yet | Check exact success codes for each payment type in PSP docs |

---

## PCI DSS Version Note

PCI DSS v4.0 became the only active standard as of **March 31, 2024**. v3.2.1 is retired. Key changes affecting Taiwan merchants:

- **Requirement 6.4.3 / 12.3.2**: Scripts loaded on payment pages must be authorized and integrity-checked (applies to SAQ A-EP and SAQ D; SAQ A merchants using full redirect are exempt)
- **Requirement 8.3.6**: Password minimum length increased to 12 characters (previously 8)
- **Requirement 10.7**: Failures of critical security controls must be detected and responded to promptly
