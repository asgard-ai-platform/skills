# 綠界 (ECPay) API Integration Guide

## Merchant Credentials

申請核准後，ECPay 提供三組憑證：

| 欄位 | 用途 | 存放位置 |
|------|------|----------|
| `MerchantID` | 識別商店 | 環境變數 |
| `HashKey` | 簽章用 | 環境變數（勿硬寫） |
| `HashIV` | 簽章用 | 環境變數（勿硬寫） |

測試環境固定值（官方公開 sandbox，可直接使用）：

```
MerchantID = 2000132
HashKey    = 5294y06JbISpM5x9
HashIV     = v77hoKGq4kWxNNIS
```

正式環境從後台取得，**不可與測試環境混用**。

---

## CheckMacValue 簽章演算法

這是 ECPay 最容易出錯的地方。**每一個 API request 和 callback 都必須計算此值。**

### 計算步驟

```
1. 將所有參數（不含 CheckMacValue 本身）照 key 的字母排序
2. 組成 QueryString 格式：key1=val1&key2=val2&...
3. 頭尾加上 HashKey 和 HashIV：
   HashKey=<HashKey>&<QueryString>&HashIV=<HashIV>
4. URL encode（小寫）
5. MD5 or SHA256（視 EncryptType 而定）
6. 轉大寫
```

### URL encode 特殊規則

ECPay 的 URL encode 與標準不同，以下字元**不 encode**：

```
- * . ! ( )
```

且空白必須編為 `%20`（不是 `+`）。

### Python 實作

```python
import hashlib
import urllib.parse

def generate_check_mac_value(params: dict, hash_key: str, hash_iv: str, encrypt_type: int = 1) -> str:
    """
    encrypt_type: 0 = MD5, 1 = SHA256
    """
    # Step 1: 排序
    sorted_params = sorted(params.items(), key=lambda x: x[0].lower())
    
    # Step 2: 組 QueryString
    query_string = "&".join(f"{k}={v}" for k, v in sorted_params)
    
    # Step 3: 加上 HashKey / HashIV
    raw = f"HashKey={hash_key}&{query_string}&HashIV={hash_iv}"
    
    # Step 4: URL encode（小寫）
    encoded = ecpay_url_encode(raw)
    
    # Step 5: 雜湊
    if encrypt_type == 0:
        result = hashlib.md5(encoded.encode("utf-8")).hexdigest()
    else:
        result = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    
    # Step 6: 大寫
    return result.upper()


def ecpay_url_encode(s: str) -> str:
    """ECPay 版 URL encode：小寫，但 - * . ! ( ) 不 encode"""
    # urllib.parse.quote 預設不 encode unreserved chars
    # ECPay 要求 safe 包含這幾個字元
    encoded = urllib.parse.quote(s, safe="-_.!~*'()")
    # ECPay 要求全小寫
    # 但只有 % 後的 hex 要小寫，urllib 預設已是大寫，需轉換
    import re
    return re.sub(r'%[0-9A-F]{2}', lambda m: m.group(0).lower(), encoded)
```

### 驗證 callback 簽章

```python
def verify_callback(params: dict, hash_key: str, hash_iv: str) -> bool:
    received_mac = params.get("CheckMacValue", "")
    
    # 移除 CheckMacValue 本身再重算
    params_without_mac = {k: v for k, v in params.items() if k != "CheckMacValue"}
    
    expected_mac = generate_check_mac_value(params_without_mac, hash_key, hash_iv)
    
    return received_mac.upper() == expected_mac.upper()
```

---

## 建立付款訂單（AIO API）

### Endpoint

```
測試：https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5
正式：https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5
```

這個 API 不是 JSON POST，是**表單 POST**，回應是 HTML 頁面（直接重導顯示）。

### 必填參數

| 參數 | 說明 | 範例 |
|------|------|------|
| `MerchantID` | 商店代號 | `2000132` |
| `MerchantTradeNo` | 訂單編號（唯一，英數字，≤20碼） | `ORD20240115001` |
| `MerchantTradeDate` | 訂單時間 | `2024/01/15 10:30:00` |
| `PaymentType` | 固定填 `aio` | `aio` |
| `TotalAmount` | 金額（整數，NT$） | `1500` |
| `TradeDesc` | 交易描述（URL encode） | `%E8%A8%82%E5%96%AE` |
| `ItemName` | 商品名稱，多品用 `#` 分隔 | `T恤#帽子` |
| `ReturnURL` | callback webhook URL（必須可公開訪問） | `https://shop.tw/ecpay/notify` |
| `ChoosePayment` | 付款方式 | 見下表 |
| `CheckMacValue` | 簽章 | 計算得出 |

### ChoosePayment 值

| 值 | 付款方式 |
|----|---------|
| `Credit` | 信用卡（含分期、一次付清） |
| `WebATM` | 網路 ATM（使用者直接轉帳） |
| `ATM` | ATM 虛擬帳號（系統產生帳號，用戶自行轉） |
| `CVS` | 超商代碼繳費 |
| `BARCODE` | 超商條碼繳費 |
| `ALL` | 顯示全部選項讓用戶選 |
| `LinePay` | LINE Pay |
| `ApplePay` | Apple Pay（僅限 Safari） |

### Python 建立訂單範例

```python
import datetime
import requests

def create_ecpay_order(order_id: str, amount: int, items: list[str]) -> str:
    """回傳 ECPay 付款頁面 HTML（直接輸出給瀏覽器）"""
    
    params = {
        "MerchantID": MERCHANT_ID,
        "MerchantTradeNo": order_id,          # 唯一，最長20碼
        "MerchantTradeDate": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        "PaymentType": "aio",
        "TotalAmount": amount,
        "TradeDesc": "線上商店訂單",
        "ItemName": "#".join(items),           # 多品用 # 分隔
        "ReturnURL": "https://shop.tw/ecpay/notify",    # webhook
        "ClientBackURL": "https://shop.tw/order/done",  # 付款後返回頁
        "ChoosePayment": "ALL",
        "EncryptType": 1,                       # SHA256
    }
    
    params["CheckMacValue"] = generate_check_mac_value(params, HASH_KEY, HASH_IV)
    
    # 建立 HTML 表單並自動送出
    html = '<form id="ecpay" action="{url}" method="post">'.format(
        url="https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5"
    )
    for key, value in params.items():
        html += f'<input type="hidden" name="{key}" value="{value}">'
    html += '</form><script>document.getElementById("ecpay").submit();</script>'
    
    return html
```

### ATM 虛擬帳號額外參數

使用 `ChoosePayment=ATM` 時，必須加上：

| 參數 | 說明 | 預設 |
|------|------|------|
| `ExpireDate` | 繳費期限（天數） | 3（最大60） |

ATM 的付款通知**不是即時的**。用戶轉帳後，ECPay 約 **5~30 分鐘**確認後才打 callback。

### CVS 超商代碼額外參數

| 參數 | 說明 | 預設 |
|------|------|------|
| `StoreExpireDate` | 繳費期限（分鐘） | 10080（7天，最大43200） |
| `Desc_1` 到 `Desc_4` | 超商收據備註（選填） | — |

CVS 金額限制：**NT$30 ~ NT$20,000**。超過需改用 ATM。

---

## Webhook（ReturnURL）處理

### ECPay 打回來的 POST body 範例

```
MerchantID=2000132
&MerchantTradeNo=ORD20240115001
&StoreID=
&RtnCode=1
&RtnMsg=Succeeded
&TradeNo=2401151030000001
&TradeAmt=1500
&PaymentDate=2024/01/15 10:35:22
&PaymentType=Credit_CreditCard
&PaymentTypeChargeFee=41
&TradeDate=2024/01/15 10:30:00
&SimulatePaid=0
&CustomField1=
&CheckMacValue=ABCD1234...
```

`RtnCode=1` 代表付款成功，**其他值都是失敗或待處理**。

### Webhook handler（Django 範例）

```python
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

@csrf_exempt
def ecpay_notify(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    
    # ECPay POST 是 form-encoded
    params = dict(request.POST)
    params = {k: v[0] for k, v in params.items()}  # QueryDict 轉 dict
    
    # Step 1: 驗簽
    if not verify_callback(params, HASH_KEY, HASH_IV):
        return HttpResponse("0|Error", content_type="text/plain")
    
    trade_no = params["MerchantTradeNo"]
    rtn_code = params["RtnCode"]
    ecpay_trade_no = params["TradeNo"]
    
    # Step 2: 冪等處理（重複 callback 不重複處理）
    order = Order.objects.select_for_update().get(trade_no=trade_no)
    if order.status == "paid":
        return HttpResponse("1|OK", content_type="text/plain")
    
    # Step 3: 更新狀態
    if rtn_code == "1":
        order.status = "paid"
        order.ecpay_trade_no = ecpay_trade_no
        order.save()
        # 觸發後續流程（出貨通知等）
        trigger_fulfillment(order)
    else:
        order.status = "payment_failed"
        order.save()
    
    # Step 4: 必須回應 "1|OK"，否則 ECPay 會重試
    return HttpResponse("1|OK", content_type="text/plain")
```

**關鍵**：callback 必須回傳 `1|OK`（純文字），否則 ECPay 最多重試 **6 次**，間隔為 1 小時。

### ATM 的兩段式 callback

ATM 付款有**兩個** URL：

| 參數 | 時機 | 用途 |
|------|------|------|
| `ReturnURL` | 用戶轉帳後、ECPay 確認入帳 | 訂單標記為已付款（主要） |
| `PeriodReturnURL` | 定期定額每次扣款 | 訂閱用 |

ATM 在訂單建立時還會打一次 `ReturnURL`，`RtnCode=2`，代表**虛擬帳號已產生，等待繳款**（不是付款成功）。

```python
ATM_PENDING_CODES = {
    "2": "虛擬帳號已產生，等待繳款",
}
PAYMENT_SUCCESS_CODE = "1"
```

---

## 查詢訂單狀態（主動查詢 API）

不要只靠 webhook，每日應執行對帳任務主動查詢。

### Endpoint

```
測試：https://payment-stage.ecpay.com.tw/Cashier/QueryTradeInfo/V5
正式：https://payment.ecpay.com.tw/Cashier/QueryTradeInfo/V5
```

### 參數

```python
def query_trade_info(merchant_trade_no: str) -> dict:
    params = {
        "MerchantID": MERCHANT_ID,
        "MerchantTradeNo": merchant_trade_no,
        "TimeStamp": str(int(datetime.datetime.now().timestamp())),
    }
    params["CheckMacValue"] = generate_check_mac_value(params, HASH_KEY, HASH_IV)
    
    resp = requests.post(
        "https://payment-stage.ecpay.com.tw/Cashier/QueryTradeInfo/V5",
        data=params
    )
    
    # 回應也是 QueryString 格式
    result = dict(urllib.parse.parse_qsl(resp.text))
    return result
```

回應欄位 `TradeStatus`：

| 值 | 意義 |
|----|------|
| `0` | 交易未完成 |
| `1` | 付款成功 |
| `2` | 交易失敗 |
| `10200095` | ATM 繳費期限已過 |

---

## 退款 API

### 信用卡退款

```
Endpoint（正式）：https://payment.ecpay.com.tw/CreditDetail/DoAction
```

| 參數 | 說明 |
|------|------|
| `MerchantID` | 商店代號 |
| `MerchantTradeNo` | 原始訂單編號 |
| `TradeNo` | ECPay 的交易編號（從 webhook 取得） |
| `Action` | `R`=全額退款、`E`=部分退款 |
| `TotalAmount` | 退款金額（部分退款時必填） |

```python
def refund_credit_card(merchant_trade_no: str, ecpay_trade_no: str, amount: int = None) -> dict:
    params = {
        "MerchantID": MERCHANT_ID,
        "MerchantTradeNo": merchant_trade_no,
        "TradeNo": ecpay_trade_no,
        "Action": "R" if amount is None else "E",
    }
    if amount is not None:
        params["TotalAmount"] = amount
    
    params["CheckMacValue"] = generate_check_mac_value(params, HASH_KEY, HASH_IV)
    
    resp = requests.post(
        "https://payment.ecpay.com.tw/CreditDetail/DoAction",
        data=params
    )
    result = dict(urllib.parse.parse_qsl(resp.text))
    
    # RtnCode=1 為成功
    return result
```

**ATM 和 CVS 退款沒有 API**。必須：
1. 取得客戶銀行帳號（客服流程）
2. 人工匯款
3. 在系統標記退款完成

---

## 常見錯誤代碼

| RtnCode | 錯誤訊息 | 原因與處理 |
|---------|---------|-----------|
| `10200047` | CheckMacValue error | 簽章錯誤，檢查排序、encode 邏輯 |
| `10200073` | MerchantTradeNo has been used | 訂單編號重複，產生新的 TradeNo |
| `10200075` | Order amount error | 金額為 0 或格式錯誤 |
| `10200095` | Payment period has expired | ATM 繳費期限過，訂單已失效 |
| `10200248` | IP is not allowed | 未將伺服器 IP 加入 ECPay 後台白名單 |

---

## 沙盒測試信用卡

| 卡號 | 有效期限 | CVV | 用途 |
|------|---------|-----|------|
| `4311952222222222` | 任意未來年月 | 任意 | 一般成功交易 |
| `4311952222222230` | 任意未來年月 | 任意 | 模擬 3DS 驗證 |
| `4311952222222206` | 任意未來年月 | 任意 | 模擬交易失敗 |

測試 ATM：訂單建立後，後台可手動模擬繳款，不需真的轉帳。

---

## MerchantTradeNo 設計建議

ECPay 要求 TradeNo **全域唯一且不超過 20 碼**，退款後若需重新付款必須用新號。

```
格式：{前綴}{日期}{流水號}
範例：ORD240115001234
     └─ 3碼 ─┘ 6碼 ─┘ 6碼 ─┘ = 15碼
```

若系統有多個服務需付款（訂單、加購、運費補收），可在前綴區分：

```
ORD240115000001   ← 一般訂單
ADD240115000001   ← 加購
SHP240115000001   ← 補收運費
```

不要用資料庫自增 ID 作為 TradeNo，容易撞號且暴露訂單量。
