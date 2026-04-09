# 加值服務中心 API 整合參考

## 加值中心選擇

台灣主要的加值服務中心（電子發票 API 中介商）：

| 加值中心 | 市場定位 | 月費結構 | 備註 |
|----------|----------|----------|------|
| **綠界科技 (ECPay)** | 最廣泛，電商首選 | 依方案，部分免月費 | 同時提供金流，整合方便 |
| **藍新金流 (NewebPay)** | 電商 + 行動支付 | 依方案 | API 文件較舊，需注意版本 |
| **歐付寶 (OPay)** | 中小型電商 | 依方案 | |
| **統一超商 ibon** | 實體通路 | 依合約 | 適合實體零售 |
| **大台北瓦斯系統** | 傳產 ERP | 依合約 | B2B 多 |

**選擇原則**：若已用某加值中心處理金流，優先整合同一家的電子發票 API，減少憑證管理複雜度。

---

## 環境端點

以綠界 ECPay 為主要範例（其他加值中心結構類似）：

```
# 測試環境
https://einvoice-stage.ecpay.com.tw/B2CInvoice/{Action}

# 正式環境
https://einvoice.ecpay.com.tw/B2CInvoice/{Action}
```

財政部直連（少數大企業使用）：
```
# 測試環境
https://wwwtest.einvoice.nat.gov.tw/
# 正式環境
https://www.einvoice.nat.gov.tw/
```

---

## 認證與參數結構

### AppID 申請流程

1. 登入財政部電子發票整合服務平台 (`einvoice.nat.gov.tw`)，申請成為「開立電子發票業者」
2. 向選定的加值中心提交：統一編號、營業登記資料、預計月發票量
3. 加值中心審核後核發：`MerchantID`（商店代號）、`HashKey`、`HashIV`
4. 下載測試環境憑證（部分加值中心需要 SSL 憑證）

### 簽章產生（CheckMacValue）

所有 API 請求需附 `CheckMacValue`，防止竄改。

**綠界簽章演算法（SHA-256）：**

```python
import hashlib
import urllib.parse

def generate_check_mac_value(params: dict, hash_key: str, hash_iv: str) -> str:
    # 1. 依參數名稱字母升冪排序
    sorted_params = sorted(params.items(), key=lambda x: x[0].lower())
    
    # 2. 組合成 URL query string 格式
    raw = "&".join(f"{k}={v}" for k, v in sorted_params)
    
    # 3. 前後加上 HashKey / HashIV
    raw = f"HashKey={hash_key}&{raw}&HashIV={hash_iv}"
    
    # 4. URL encode（小寫）
    raw = urllib.parse.quote_plus(raw).lower()
    
    # 5. SHA-256 → 大寫
    return hashlib.sha256(raw.encode("utf-8")).hexdigest().upper()

# 範例
params = {
    "MerchantID": "2000132",
    "TimeStamp": "1700000000",
    "InvoiceDate": "2024-01-15",
    "SalesAmount": "1000",
}
mac = generate_check_mac_value(params, hash_key="ejCk326UnaZWKisg", hash_iv="q9jcZX8Ib9LM8wYk")
```

> **注意**：URL encode 後必須轉小寫，SHA-256 結果必須轉大寫，兩個步驟都不能省略。

---

## 核心 API：開立發票

### 端點

```
POST /B2CInvoice/Issue
Content-Type: application/x-www-form-urlencoded
```

### 必填參數

| 參數 | 類型 | 說明 | 範例值 |
|------|------|------|--------|
| `MerchantID` | string | 商店代號 | `2000132` |
| `RelateNumber` | string | **商店自訂訂單號**，需唯一 | `ORD20240115001` |
| `CustomerID` | string | 買方統編（B2B）；B2C 留空 | `12345678` 或空字串 |
| `CustomerIdentifier` | string | 同上（B2B）；消費者留空 | |
| `CustomerName` | string | 買方名稱 | `王小明` |
| `CustomerEmail` | string | 寄送電子發票用 | `user@example.com` |
| `CarrierType` | string | 載具類型（見下表） | `3J0001` |
| `CarrierNum` | string | 載具號碼 | `/ABC1234` |
| `Print` | int | 是否列印：`0` 否、`1` 是 | `0` |
| `Donation` | int | 捐贈：`0` 否、`1` 是 | `0` |
| `LoveCode` | string | 捐贈碼（`Donation=1` 時填） | `168` |
| `SalesAmount` | int | **含稅**總金額（整數，新台幣） | `1050` |
| `TaxType` | string | 稅別（見下表） | `1` |
| `TaxRate` | int | 稅率（整數） | `5` |
| `TaxAmount` | int | 稅額 | `50` |
| `Items` | JSON array | 品項明細（見下方） | |
| `InvType` | string | 發票類型：`07` 一般稅額 | `07` |
| `vat` | int | `1` 含稅、`0` 未稅 | `1` |
| `TimeStamp` | int | Unix timestamp | `1700000000` |
| `CheckMacValue` | string | 簽章 | |

### 載具類型代碼

| `CarrierType` 值 | 載具 | `CarrierNum` 格式 |
|-----------------|------|------------------|
| `""` (空字串) | 無載具（紙本或會員） | 空字串 |
| `1` | 會員載具（業者自定義） | 業者自訂格式 |
| `2` | 自然人憑證 | 2 英文字母 + 14 位數字 |
| `3` | 手機條碼 | `/` + 7 碼英數字（共 8 碼） |

### 品項 Items 格式

```json
[
  {
    "ItemSeq": 1,
    "ItemName": "商品A",
    "ItemCount": 2,
    "ItemWord": "個",
    "ItemPrice": 500,
    "ItemTaxType": "1",
    "ItemAmount": 1000,
    "ItemRemark": ""
  }
]
```

- `ItemAmount` = `ItemCount × ItemPrice`（含稅）
- 所有品項 `ItemAmount` 加總必須等於 `SalesAmount`（否則 API 回傳錯誤）

### 稅別代碼

| `TaxType` | 說明 |
|-----------|------|
| `1` | 應稅（一般 5%）|
| `2` | 零稅率 |
| `3` | 免稅 |
| `9` | 混合稅率（同張發票含不同稅率品項）|

### 完整請求範例（Python）

```python
import requests
import time
import json
from urllib.parse import urlencode

MERCHANT_ID = "2000132"
HASH_KEY = "ejCk326UnaZWKisg"
HASH_IV  = "q9jcZX8Ib9LM8wYk"
API_URL  = "https://einvoice-stage.ecpay.com.tw/B2CInvoice/Issue"

items = [
    {
        "ItemSeq": 1,
        "ItemName": "商品A",
        "ItemCount": 2,
        "ItemWord": "個",
        "ItemPrice": 500,
        "ItemTaxType": "1",
        "ItemAmount": 1000,
        "ItemRemark": "",
    }
]

params = {
    "MerchantID":          MERCHANT_ID,
    "RelateNumber":        "ORD20240115001",
    "CustomerID":          "",
    "CustomerIdentifier":  "",
    "CustomerName":        "王小明",
    "CustomerAddr":        "",
    "CustomerPhone":       "",
    "CustomerEmail":       "user@example.com",
    "ClearanceMark":       "",
    "Print":               "0",
    "Donation":            "0",
    "LoveCode":            "",
    "CarrierType":         "3",
    "CarrierNum":          "/ABC1234",
    "TaxType":             "1",
    "SalesAmount":         "1050",
    "InvoiceRemark":       "",
    "Items":               json.dumps(items),
    "InvType":             "07",
    "vat":                 "1",
    "TimeStamp":           str(int(time.time())),
}

params["CheckMacValue"] = generate_check_mac_value(params, HASH_KEY, HASH_IV)

response = requests.post(API_URL, data=params)
result = response.json()

# 成功回應
# {
#   "RtnCode": 1,
#   "RtnMsg": "開立發票成功",
#   "InvoiceNo": "AB12345678",
#   "InvoiceDate": "2024-01-15",
#   "RandomNumber": "1234"
# }
```

### 成功回應欄位

| 欄位 | 說明 |
|------|------|
| `RtnCode` | `1` = 成功；其他 = 錯誤碼 |
| `InvoiceNo` | MOF 分配的發票號碼（字軌+號碼，共 10 碼） |
| `InvoiceDate` | 發票日期（`yyyy-MM-dd`）|
| `RandomNumber` | 4 位隨機碼（兌獎用，**務必儲存**）|

**`InvoiceNo` + `InvoiceDate` + `RandomNumber` 三者必須一起儲存到資料庫。** 兌獎和作廢都需要這三個值。

---

## 核心 API：作廢發票

### 端點

```
POST /B2CInvoice/Invalid
```

### 參數

| 參數 | 說明 |
|------|------|
| `InvoiceNo` | 發票號碼 |
| `InvoiceDate` | 發票日期 |
| `Reason` | 作廢原因（中文，最多 20 字）|
| `TimeStamp` | Unix timestamp |
| `CheckMacValue` | 簽章 |

### 作廢限制

- **只能在同期別（bimonthly period）內作廢**
- 台灣發票期別：1-2 月、3-4 月、5-6 月、7-8 月、9-10 月、11-12 月
- 跨期別需改用「折讓單」（`Allowance` API），流程更複雜

```python
def get_invoice_period(date: str) -> str:
    """回傳發票期別，例如 '11301' 代表 113 年 1-2 月"""
    from datetime import datetime
    d = datetime.strptime(date, "%Y-%m-%d")
    roc_year = d.year - 1911
    period = (d.month - 1) // 2 + 1  # 1~6
    return f"{roc_year:03d}{period:02d}"

# 判斷是否可以直接作廢
def can_void(invoice_date: str, today: str) -> bool:
    return get_invoice_period(invoice_date) == get_invoice_period(today)
```

---

## 核心 API：查詢發票

```
POST /B2CInvoice/GetIssue

params: MerchantID, RelateNumber (商店訂單號), TimeStamp, CheckMacValue
```

回應包含 `InvoiceNo`、`InvoiceStatus`（`1`=有效、`2`=作廢）、金額等。

**使用時機**：發票開立後，系統未正確接收回應（timeout、網路中斷），用 `RelateNumber` 查詢確認是否已開立。

---

## 手機條碼驗證 API

在 POS 或結帳頁面掃描消費者手機條碼後，**必須先驗證條碼是否有效**，再開立發票。

### 端點

```
POST /B2CInvoice/CheckBarcode
```

### 參數

| 參數 | 說明 |
|------|------|
| `BarCode` | 手機條碼（`/` + 7 碼，共 8 碼）|

### 回應

```json
{
  "RtnCode": 1,
  "RtnMsg": "查詢成功",
  "IsExist": "Y"
}
```

- `IsExist: "Y"` → 條碼有效，可開立
- `IsExist: "N"` → 條碼無效，應提示消費者重新掃描或改用其他方式

**不要跳過這個驗證步驟**。若直接開立使用無效條碼的發票，消費者的發票不會歸戶，發票獎金也無法通知。

---

## 捐贈碼驗證 API

```
POST /B2CInvoice/CheckLoveCode

params: LoveCode (3-7 位數字)
```

回應：`IsExist: "Y"` / `"N"`。

同樣須在開立前驗證，避免捐給不存在的機構。

---

## 常見錯誤碼

| `RtnCode` | 說明 | 處理方式 |
|-----------|------|----------|
| `1` | 成功 | — |
| `10000048` | `RelateNumber` 重複 | 訂單號已開過發票，先查詢再決定是否重開 |
| `10000049` | 字軌號碼不足 | **立即向財政部申請補充字軌**，這是最危急狀況 |
| `10000052` | 金額不符（品項加總 ≠ 總金額）| 檢查 `ItemAmount` 加總 |
| `10000060` | 手機條碼格式錯誤 | 確認格式為 `/` + 7 碼英數（區分大小寫）|
| `10000066` | 超過作廢時限 | 改用折讓單流程 |
| `10000085` | `CheckMacValue` 錯誤 | 檢查簽章算法，特別是 URL encode 大小寫 |
| `10100009` | AppID / 憑證問題 | 聯繫加值中心確認帳號狀態 |

---

## 字軌（號碼段）管理

這是最容易被忽略、後果最嚴重的環節。

### 字軌申請流程

1. 登入財政部平台 → 「字軌號碼申請」
2. 填寫申請期別（bimonthly）和預計發票量
3. 審核通常 1-3 工作天
4. 核准後字軌自動同步到加值中心

### 監控剩餘字軌

```python
# 綠界查詢剩餘字軌 API
POST /B2CInvoice/GetWordSetting

# 回應包含每個字軌的 StartNo, EndNo, UsedNo
# 剩餘量 = EndNo - UsedNo

def remaining_invoices(start: int, end: int, used: int) -> int:
    return end - (start + used - 1)

# 建議：剩餘量低於 500 張時自動告警
ALERT_THRESHOLD = 500
```

**建議在每日排程中加入字軌剩餘量監控，並在達到閾值時發送 Slack / Email 告警。** 字軌用盡就完全無法開立發票，且申請需要 1-3 天。

---

## 每日對帳流程

### 財政部平台查詢 API（直連）

加值中心通常也提供「批次查詢」或「對帳報表」功能，但最終以財政部平台為準。

對帳邏輯：

```python
from datetime import date, timedelta

def daily_reconciliation(issued_by_system: list[dict], issued_by_mof: list[dict]):
    """
    issued_by_system: 系統資料庫中當日開立的發票
    issued_by_mof: 從財政部 / 加值中心拉取的當日發票清單
    """
    system_set = {inv["invoice_no"] for inv in issued_by_system}
    mof_set    = {inv["invoice_no"] for inv in issued_by_mof}
    
    only_in_system = system_set - mof_set  # 系統有但 MOF 沒有 → 開立失敗但系統記錄了
    only_in_mof    = mof_set - system_set  # MOF 有但系統沒有 → 嚴重，需立即調查
    
    if only_in_system:
        alert(f"以下發票系統有記錄但 MOF 未收到：{only_in_system}")
    
    if only_in_mof:
        alert(f"嚴重：MOF 有以下發票但系統無記錄：{only_in_mof}")
    
    return {
        "matched": len(system_set & mof_set),
        "only_in_system": list(only_in_system),
        "only_in_mof": list(only_in_mof),
    }
```

`only_in_mof` 的情況通常代表：網路 timeout 後系統未正確處理回應，但 MOF 已登記。用 `GetIssue` API 逐筆核對，更新系統記錄。

---

## 環境切換檢查清單

從測試環境切換到正式環境時，容易漏改的設定：

```python
# config.py
ENVIRONMENT = "production"  # "staging" | "production"

ECPAY_CONFIG = {
    "staging": {
        "merchant_id": "2000132",
        "hash_key": "ejCk326UnaZWKisg",
        "hash_iv":  "q9jcZX8Ib9LM8wYk",
        "api_base": "https://einvoice-stage.ecpay.com.tw",
    },
    "production": {
        "merchant_id": "<正式商店代號>",
        "hash_key": "<正式 HashKey>",
        "hash_iv":  "<正式 HashIV>",
        "api_base": "https://einvoice.ecpay.com.tw",
    },
}

config = ECPAY_CONFIG[ENVIRONMENT]
```

切換前確認：
- [ ] `MerchantID` 已換成正式代號
- [ ] `HashKey` / `HashIV` 已換成正式金鑰
- [ ] API base URL 已指向正式環境
- [ ] 正式字軌已申請並核准
- [ ] 資料庫連線指向正式環境（避免測試資料混入）
