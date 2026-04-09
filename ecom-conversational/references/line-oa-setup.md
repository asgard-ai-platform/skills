# LINE Official Account 設定指南

## 帳號類型選擇

LINE OA 分三種認證等級，影響功能與費用：

| 類型 | 申請條件 | 搜尋可見 | 官方認證徽章 |
|------|---------|---------|------------|
| 未認證帳號 | 任何人可申請 | 否 | 否 |
| 認證帳號 | 需提交營業登記 | 是 | 藍色盾牌 |
| 優質帳號 | LINE 邀請制 | 是 | 綠色盾牌 |

**決策規則**：電商業者一律申請認證帳號。未認證帳號無法被搜尋，等同放棄自然流入。

## 訊息方案費用計算

LINE OA 採「免費額度 + 超量計費」模式（2024 年台灣方案）：

| 方案 | 月費 | 每月免費訊息 | 超量單價 |
|------|------|------------|---------|
| 輕用量 | 免費 | 500 則 | 無法加購（封頂） |
| 基礎 | NT$888 | 4,000 則 | NT$0.20/則 |
| 進階 | NT$2,888 | 25,000 則 | NT$0.15/則 |

**計算公式**：

```
月訊息成本 = 月費 + MAX(0, 月發送量 - 免費額度) × 超量單價
```

**實際案例**：好友數 2,000 人，每月發 3 次廣播（觸及率 60%）：

```
每次廣播觸及 = 2,000 × 60% = 1,200 人
月發送量 = 1,200 × 3 = 3,600 則

輕用量方案：超過 500 則上限，訊息無法送出 → 不可用
基礎方案：NT$888 + (3,600 - 4,000) = NT$888（未超量）
進階方案：NT$2,888（大幅超出，浪費）

→ 選基礎方案
```

**升級觸發點**：當 `月發送量 > 4,000 則` 且 `超量費用 > NT$2,000` 時，升進階方案更划算。

臨界點計算：
```
4,000 + X 則使用基礎 = NT$888 + X × 0.20
25,000 則使用進階 = NT$2,888

888 + X × 0.20 = 2,888
X = 10,000

→ 月發送量超過 14,000 則時，升進階方案。
```

## 帳號建立流程

### Step 1：申請認證帳號

1. 前往 [LINE Business ID](https://account.line.biz/login) 以個人 LINE 帳號登入
2. 選「建立 LINE 官方帳號」→ 帳號類別選「一般企業」
3. 填寫基本資料後，進入 LINE Official Account Manager（OA Manager）
4. 左側選單「帳號設定」→「認證申請」，上傳：
   - 公司登記證明（商業登記或公司執照）
   - 負責人身分證正面
   - 主要商品或服務說明（200 字以內）

審核時間：3-10 個工作天。審核中帳號仍可正常使用，但不顯示認證徽章。

### Step 2：基本設定

進入 OA Manager 後，依序完成：

**帳號資料**
- 大頭貼：800×800px，品牌 logo（避免文字太小）
- 背景圖片：1080×878px
- 狀態消息：24 字以內，放目前促銷或服務時間（例：「週一至六 10:00-20:00 線上客服」）

**隱私設定**
- 好友加入時：設定「自動回覆」或「Webhook」（二選一，不可同時）
- 若使用 chatbot，**必須關閉 LINE 內建自動回覆**，改用 Webhook，否則 bot 回覆與內建自動回覆會撞車

### Step 3：Rich Menu 設定

Rich Menu 是 OA 的導航核心，出現在聊天視窗底部。

**尺寸規格**：

| 版型 | 寬 × 高 | 格數選項 |
|------|---------|---------|
| 大版 | 2500 × 1686px | 2、3、4、6 格 |
| 小版 | 2500 × 843px | 2、3、4、6 格 |

**建議格局（電商用 6 格大版）**：

```
┌─────────────┬─────────────┬─────────────┐
│  🛍️ 商品目錄  │  📦 我的訂單  │  🎁 優惠活動  │
├─────────────┼─────────────┼─────────────┤
│  ❓ 常見問題  │  💬 聯絡客服  │  👤 會員中心  │
└─────────────┴─────────────┴─────────────┘
```

每個格子設定一個「動作」：
- **文字**：發送預設文字給 chatbot（例：點「商品目錄」→ 發送「#商品目錄」）
- **連結**：開啟 LIFF 或外部網址
- **折疊**：隱藏 Rich Menu（少用）

**用文字動作而非直接跳連結的理由**：chatbot 可記錄用戶觸發了哪個選單項目，方便分析；直接連結無法追蹤。

## Webhook 串接

若要接 chatbot（自建或第三方），需設定 Webhook。

**設定路徑**：OA Manager → 「訊息設定」→「Webhook」→ 輸入你的 Webhook URL → 「驗證」

LINE 要求 Webhook URL：
- HTTPS（TLS 1.2+）
- 有效憑證（不接受自簽）
- 回應時間 < 1 秒（LINE 等待逾時後不重試）

**驗證流程**：LINE 發送一個 `{"events":[]}` 的 POST 請求，你的伺服器必須回 `200 OK`。

基本 Webhook 處理範例（Python / Flask）：

```python
from flask import Flask, request, abort
import hmac, hashlib, base64, json

app = Flask(__name__)
CHANNEL_SECRET = "your_channel_secret"
CHANNEL_ACCESS_TOKEN = "your_channel_access_token"

def verify_signature(body: bytes, signature: str) -> bool:
    expected = base64.b64encode(
        hmac.new(CHANNEL_SECRET.encode(), body, hashlib.sha256).digest()
    ).decode()
    return hmac.compare_digest(expected, signature)

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data()

    if not verify_signature(body, signature):
        abort(400)

    events = json.loads(body)["events"]
    for event in events:
        if event["type"] == "message" and event["message"]["type"] == "text":
            handle_text(event)

    return "OK", 200

def handle_text(event):
    text = event["message"]["text"]
    reply_token = event["replyToken"]
    # 你的 bot 邏輯
    reply(reply_token, f"收到：{text}")
```

**安全注意事項**：永遠驗證 `X-Line-Signature`。不驗證的 Webhook 等同公開 API，任何人都能偽造 LINE 事件。

## LIFF（LINE Front-end Framework）

LIFF 讓你在 LINE 內開啟自訂網頁，外觀融入 LINE 介面，可直接取得用戶 LINE UID。

**使用時機**：
- 商品詳情頁（比 Flex Message 呈現更多資訊）
- 結帳頁（LINE Pay 整合）
- 會員資料填寫表單

**建立 LIFF App**：

1. 進入 [LINE Developers Console](https://developers.line.biz/)
2. 選你的 Provider → 建立或選擇 Channel（類型：LINE Login）
3. 左側「LIFF」→「Add」→ 填入：
   - LIFF App 名稱
   - Size：`Full`（全螢幕）/ `Tall`（3/4）/ `Compact`（半高）
   - Endpoint URL：你的 HTTPS 網頁

建立後取得 LIFF ID（格式：`1234567890-xxxxxxxx`），LIFF URL 格式：

```
https://liff.line.me/{liff-id}
```

**在 LIFF 內取得用戶 UID**：

```javascript
import liff from '@line/liff';

await liff.init({ liffId: 'your-liff-id' });

if (!liff.isLoggedIn()) {
  liff.login();
}

const profile = await liff.getProfile();
console.log(profile.userId);   // LINE UID，用來與 OA 好友記錄對應
console.log(profile.displayName);
```

## LINE Pay 整合

LINE Pay 是台灣轉換率最高的 in-chat 付款方式，適合 LIFF 結帳頁。

**申請條件**：需有認證 OA + 完成 LINE Pay 商家申請（獨立審核，約 2 週）

**付款流程**：

```
1. 用戶在 LIFF 確認訂單
2. 你的後端呼叫 LINE Pay Request API → 取得 paymentUrl
3. 前端 redirect 到 paymentUrl（在 LINE 內開啟原生付款頁）
4. 用戶付款完成 → LINE Pay redirect 回你的 confirmUrl
5. 你的後端呼叫 LINE Pay Confirm API → 完成扣款
6. 傳送訂單確認 Flex Message 給用戶
```

**測試環境**：LINE Pay 提供 Sandbox，測試時用 Sandbox Channel ID/Secret，URL 改為 `https://sandbox-api-pay.line.me`。

## 常見錯誤與排查

| 錯誤 | 原因 | 解法 |
|------|------|------|
| Webhook 驗證失敗 | 伺服器回應非 200，或憑證問題 | 確認 HTTPS 憑證有效、伺服器可從外部訪問 |
| 訊息發送但用戶沒收到 | 用戶封鎖 OA 或未加好友 | 檢查好友狀態 API |
| Rich Menu 不顯示 | 沒有設為「預設選單」 | OA Manager 確認選單狀態為「使用中」 |
| 自動回覆與 bot 衝突 | 未關閉 LINE 內建回覆 | OA Manager → 訊息設定 → 停用自動回覆與 Greeting 訊息 |
| Reply Token 失效 | Reply Token 只能用一次且 30 秒內有效 | 收到 event 後立即回覆；需主動發訊用 Push API |
| 月訊息超量 | 未估算廣播觸及量 | 使用上方費用公式提前估算；考慮分批廣播 |

## 好友數成長策略

**線下導流**：
- 收銀台放「加好友享折扣」QR code 立牌
- 包裝內附 QR code 卡片（回購誘因）

**線上導流**：
- 廣告用「點擊加好友」目標，比「點擊網站」的 CPA 低 30-50%（實際因產業不同）
- 官方網站放加好友 Banner，觸發條件：停留 > 30 秒或加入購物車時

**注意**：好友數虛高無意義。封鎖率 > 20% 代表歡迎訊息或後續訊息干擾性太強，應先改善內容品質而非繼續買流量。

封鎖率計算：
```
封鎖率 = 封鎖人數 / 歷史加好友總人數 × 100%
淨好友數 = 加好友總數 - 封鎖人數 - 解除好友人數
```
