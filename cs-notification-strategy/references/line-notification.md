# LINE Notification 實作指南

## LINE 在台灣的基本格局

LINE 在台灣的月活躍用戶滲透率約 95%，遠超 email（約 60% 日常使用率）與 push notification（iOS opt-in 約 50-60%）。但高滲透率不代表可以濫用——LINE Official Account (OA) 的封鎖成本極低，用戶一旦封鎖即永久失聯。

**關鍵數字**（2024 年台灣市場參考值）：

| 指標 | LINE OA | Email | Push |
|------|---------|-------|------|
| 開封率 | 55-70% | 15-25% | 5-15% |
| 點擊率 | 10-20% | 2-5% | 1-3% |
| 封鎖率（每次傳送） | 0.1-0.3% | N/A（退訂） | 0.1-0.5%（opt-out） |
| 封鎖後可恢復 | 否 | 是（重新訂閱） | 是（重新開啟） |

封鎖不可逆是 LINE 與其他管道最根本的差異，所有頻率與內容決策都必須以此為前提。

---

## LINE OA 訊息類型與費用結構

LINE OA 分兩大訊息類型，費用邏輯截然不同：

### 1. 群發訊息（Broadcast）

向所有好友或分眾群組一次送出。**按則計費**，超出免費額度後每則約 NT$0.2-0.5（依方案）。

適用情境：
- 促銷活動、新品上市
- 週報/月報
- 品牌公告

**費用試算公式**：

```
月費用 = Max(0, 群發則數 × 好友數 - 免費額度) × 單價

範例：
- 方案：輕用量（免費額度 500 則）
- 好友數：3,000 人
- 每月傳送：2 次群發
- 群發則數 = 2 × 3,000 = 6,000 則
- 超額 = 6,000 - 500 = 5,500 則
- 費用 = 5,500 × NT$0.2 = NT$1,100/月
```

### 2. 一對一訊息（Chat / Reply API）

用戶主動傳訊後，OA 在 **7 天內回覆**不計費（Reply Token）。超過 7 天或主動推送使用 Push API，按則計費。

適用情境：
- 訂單狀態更新（用戶下單後觸發）
- 客服對話
- 個人化通知（行為觸發）

**重要限制**：Reply Token 僅能使用一次，不能存起來之後再用。

---

## 訊息格式選擇框架

LINE 支援多種訊息格式，選錯格式是開發者最常見的浪費。

### 格式決策樹

```
需要用戶點擊操作？
├── 否 → Text Message（純文字，適合通知類）
└── 是 → 有幾個選項？
         ├── 1-4 個 → Quick Reply（附在任何訊息底部的快速回覆按鈕）
         ├── 1 個主要 CTA → Bubble（單一 Flex Message）
         └── 多張輪播 → Carousel（多個 Bubble 橫向滑動）

有圖片需求？
├── 單張大圖 + 1 個連結 → Image Map
├── 單張圖 + 按鈕 → Flex Message（Image Box + Button）
└── 純圖片 → Image Message（無法追蹤點擊）
```

### 各格式效能比較

| 格式 | 點擊率範圍 | 製作成本 | 最適場景 |
|------|-----------|---------|---------|
| Text | 5-10% | 低 | 交易通知、OTP、提醒 |
| Image | 3-7% | 低 | 品牌宣傳（無需追蹤） |
| Flex Message | 12-25% | 高 | 訂單卡片、商品推薦 |
| Carousel | 15-30%（整體） | 高 | 多商品、多文章 |
| Quick Reply | 20-40%（回應率） | 中 | 問卷、選擇引導 |

---

## Flex Message 訂單通知範本

以下是電商「訂單已出貨」通知的 Flex Message JSON 結構，可直接作為起點修改：

```json
{
  "type": "flex",
  "altText": "您的訂單 #{{order_id}} 已出貨 🚚",
  "contents": {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "訂單已出貨",
          "color": "#FFFFFF",
          "weight": "bold",
          "size": "lg"
        }
      ],
      "backgroundColor": "#27ACB2"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {"type": "text", "text": "訂單編號", "color": "#aaaaaa", "size": "sm", "flex": 2},
            {"type": "text", "text": "#{{order_id}}", "size": "sm", "flex": 3, "align": "end"}
          ]
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {"type": "text", "text": "物流單號", "color": "#aaaaaa", "size": "sm", "flex": 2},
            {"type": "text", "text": "{{tracking_number}}", "size": "sm", "flex": 3, "align": "end"}
          ]
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {"type": "text", "text": "預計到貨", "color": "#aaaaaa", "size": "sm", "flex": 2},
            {"type": "text", "text": "{{estimated_date}}", "size": "sm", "flex": 3, "align": "end"}
          ]
        }
      ],
      "spacing": "md"
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "button",
          "style": "primary",
          "action": {
            "type": "uri",
            "label": "追蹤包裹",
            "uri": "https://your-domain.com/orders/{{order_id}}/tracking?utm_source=line&utm_medium=oa&utm_campaign=shipment"
          }
        }
      ]
    }
  }
}
```

**注意** `altText` 欄位：這是在對話列表預覽與推播通知顯示的文字。若寫成 "Flex Message" 這種無意義文字，用戶不會點開。務必寫有資訊量的內容（如上範例包含訂單號與狀態）。

---

## 分眾（Audience）設定

LINE OA 原生支援以下分眾方式，直接在 LINE Official Account Manager 設定，不需要額外開發：

| 分眾類型 | 來源 | 適用情境 |
|---------|------|---------|
| 年齡/性別/地區 | LINE 用戶屬性 | 地區性活動、性別相關商品 |
| 加入時間 | OA 系統 | 新用戶歡迎序列 |
| 互動行為 | 點過特定 URL、傳過特定關鍵字 | 再行銷、興趣分群 |
| 上傳自訂名單 | 電話號碼或 LINE UID CSV | CRM 整合、VIP 名單 |

**自訂名單上傳的匹配邏輯**：

```
輸入：電話號碼（需為該 LINE 帳號綁定的電話）
LINE 內部比對 → 回傳 matched / unmatched 數量
注意：LINE 不會告訴你哪支電話對應哪個 UID（隱私保護）
典型匹配率：50-70%（台灣用戶中有綁定電話者比例）
```

若要做更細緻的個人化（如「您購物車中的商品」），需透過 Messaging API 取得用戶 `userId` 並與自家 CRM 綁定。

---

## LINE Messaging API 綁定流程

將 LINE 用戶與自家系統用戶綁定，是個人化通知的前提。

### 綁定流程（以 LIFF 為例）

```
用戶在 LINE 中點擊 LIFF 連結
        ↓
LIFF 頁面載入，呼叫 liff.init()
        ↓
liff.getProfile() 取得 userId、displayName
        ↓
前端將 userId + 自家 token/session 送到後端
        ↓
後端寫入 DB: user_line_bindings(user_id, line_uid, created_at)
        ↓
之後發送個人化通知時：
  SELECT line_uid FROM user_line_bindings WHERE user_id = ?
  呼叫 Push API: POST /v2/bot/message/push
    { "to": line_uid, "messages": [...] }
```

### LIFF 前端綁定程式碼片段

```javascript
import liff from '@line/liff';

async function bindLineAccount(userToken) {
  await liff.init({ liffId: process.env.LIFF_ID });
  
  if (!liff.isLoggedIn()) {
    liff.login();
    return;
  }
  
  const profile = await liff.getProfile();
  
  const response = await fetch('/api/line/bind', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      lineUserId: profile.userId,
      displayName: profile.displayName,
      userToken: userToken  // 自家系統的認證 token
    })
  });
  
  if (response.ok) {
    // 綁定成功，可顯示確認訊息
    liff.closeWindow();
  }
}
```

**安全注意**：後端必須驗證 `userToken` 的有效性後才能寫入綁定關係，否則任何人可以偽造請求綁定他人的 LINE 帳號。

---

## 頻率上限與封鎖率控制

LINE 封鎖是不可逆的。以下是根據封鎖率訊號調整頻率的決策表：

| 封鎖率（單次傳送後） | 判斷 | 行動 |
|---------------------|------|------|
| < 0.1% | 健康 | 維持現況 |
| 0.1-0.3% | 可接受，需監控 | 審查本次內容是否相關 |
| 0.3-0.5% | 警示 | 下次傳送前審查頻率與內容相關性 |
| > 0.5% | 危險 | 立即降低頻率，重新審視分眾策略 |
| > 1% | 緊急 | 暫停傳送，全面審查 |

### 頻率上限建議（台灣電商情境）

```
交易型訊息（訂單、出貨、付款）：無上限，即時觸發
──────────────────────────────
行為觸發（棄購提醒、價格下降）：每事件最多 1-2 則
──────────────────────────────
行銷型群發：
  一般促銷：最多 2 次/週
  重大活動（雙 11、週年慶）：可提高至 3-4 次/週，但前後各降回正常
  平日：建議 1 次/週或以下
──────────────────────────────
品牌內容（文章、影片）：最多 1 次/週
```

### 封鎖率計算方式

LINE OA Manager 後台直接顯示「封鎖數」，但要計算**每次傳送的封鎖率**需要手動記錄：

```
封鎖率 = (本次傳送後累計封鎖數 - 上次傳送後累計封鎖數) / 本次傳送有效好友數

範例：
- 上次傳送後封鎖累計：1,200 人
- 本次傳送後封鎖累計：1,243 人
- 本次傳送好友數：9,800 人
- 本次封鎖率 = (1,243 - 1,200) / 9,800 = 0.44%  ← 進入警示區
```

---

## A/B 測試在 LINE OA 的限制

LINE OA Manager 內建 A/B 測試功能有限，通常只能測試「訊息內容」，無法測試傳送時間或細緻分眾。若需要嚴謹的 A/B 測試，需透過 Messaging API 自行實作：

### 自行實作 A/B 測試步驟

1. **分組**：從綁定名單中隨機抽樣，確保 A/B 兩組屬性相近（加入時間、過去購買行為）
2. **傳送**：在相同時間窗（±5 分鐘內）分別用 Multicast API 傳送
3. **追蹤**：在訊息中的 URL 加入不同 UTM 參數（`utm_content=variant_a` vs `variant_b`）
4. **評估**：以 72 小時後的點擊率或轉換率為準，避免「早晨開手機」效應干擾

```python
# 最小可行的 A/B 分組邏輯
import hashlib

def assign_variant(line_user_id: str, experiment_id: str) -> str:
    """
    基於 line_user_id 和實驗 ID 穩定分組
    同一用戶在同一實驗中永遠得到同一組別
    """
    key = f"{line_user_id}:{experiment_id}"
    hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
    return "A" if hash_value % 2 == 0 else "B"
```

**最小樣本數**（用於開封率/點擊率測試）：

```
若預期效果差異 d = 5 個百分點（如 10% vs 15%）
顯著性水準 α = 0.05，檢定力 1-β = 0.8

所需樣本數（每組）≈ 16 × σ² / d²
σ² = p(1-p)，p 取兩組平均值

以點擊率 12.5% 為基準：
σ² = 0.125 × 0.875 = 0.109
n = 16 × 0.109 / 0.0025 ≈ 700 人/組

實際建議：每組至少 1,000 人，以應對 LINE 用戶活躍度不均
```

---

## 常見錯誤與對應修正

### 錯誤 1：把行銷訊息包裝成交易訊息

**症狀**：每次訂單出貨通知都附帶「順便看看我們的新品」。  
**後果**：用戶開始忽略出貨通知，交易型訊息開封率從 80% 降至 40%。  
**修正**：交易訊息只含交易資訊。行銷訊息獨立傳送，明確標示是促銷。

### 錯誤 2：altText 無意義

**症狀**：`"altText": "訊息通知"` 或 `"altText": "Flex Message"`。  
**後果**：通知欄顯示無意義文字，用戶不知道要不要點開，開封率損失 20-30%。  
**修正**：altText 必須包含關鍵資訊，如 `"您的訂單 #12345 已於今日出貨"`。

### 錯誤 3：忽略台灣時區

**症狀**：用 UTC 時間排程，導致凌晨 2 點傳送促銷訊息。  
**後果**：即時封鎖率飆升至 2% 以上。  
**修正**：所有排程統一用 `Asia/Taipei`（UTC+8），在 Messaging API 中明確設定。

### 錯誤 4：Re-engagement 時傳太多

**症狀**：90 天未互動的用戶，一次送 3 則「我們想念你」訊息。  
**後果**：這批用戶的封鎖率是正常用戶的 5-10 倍。  
**修正**：沉睡用戶只傳 1 則，且必須是明確高價值訊息（大折扣、專屬優惠）。若 1 則無效，接受流失而非繼續騷擾。

### 錯誤 5：未設定 Webhook 接收封鎖事件

**症狀**：用戶封鎖 OA 後，系統持續嘗試對其傳送訊息，每次都收到 API 錯誤但未處理。  
**後果**：浪費費用，且累積錯誤可能觸發 LINE 的速率限制。  
**修正**：Webhook 監聽 `follow`/`unfollow` 事件，`unfollow` 時在 DB 中標記 `line_active = false`，傳送前先過濾。

```python
# Webhook 處理 unfollow 事件
@app.route('/webhook/line', methods=['POST'])
def line_webhook():
    events = request.json.get('events', [])
    for event in events:
        if event['type'] == 'unfollow':
            line_uid = event['source']['userId']
            db.execute(
                "UPDATE user_line_bindings SET active = false, unfollowed_at = NOW() WHERE line_uid = %s",
                (line_uid,)
            )
    return 'OK', 200
```
