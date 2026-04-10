# Example: 連鎖火鍋店訂位機器人設計

## Scenario

**公司**: 呷百二火鍋（台灣中型連鎖，15 間門市）
**背景**: 目前訂位全靠電話，每逢週末 3 位接線員接不完，放棄率高達 40%。行銷主任 Jenny 想在 LINE 官方帳號部署一個訂位機器人，目標是讓 70% 的訂位請求不需要人工介入。

**Jenny 的問題**:
> 「我們想做一個 LINE 機器人讓客人自助訂位。桌號、人數、時間都要能收集，還要能查詢或取消已有的訂位。不知道從哪裡開始？」

---

## Analysis

### Step 1 — 釐清 Intent Catalog

從呷百二的使用情境，先識別核心意圖（目標：覆蓋 80% 查詢）：

| Intent | 描述 | Example Utterances | Priority |
|--------|------|--------------------|---------|
| `make_reservation` | 新訂位 | "我要訂位"、"幫我訂週六 4 位"、"想訂桌" | H |
| `check_reservation` | 查詢現有訂位 | "我的訂位是幾點"、"確認一下我的預約" | H |
| `cancel_reservation` | 取消訂位 | "取消我的訂位"、"不去了"、"幫我取消週五" | H |
| `modify_reservation` | 修改人數或時間 | "改成 6 個人"、"可以提早到 6 點嗎" | M |
| `check_availability` | 詢問特定時段是否有位 | "週六晚上 7 點還有位嗎"、"明天有空桌嗎" | M |
| `check_hours` | 詢問營業時間 | "幾點開始"、"最晚幾點可以訂" | M |
| `check_location` | 詢問門市地點 | "大安店在哪裡"、"有沒有靠近捷運的" | L |
| `fallback` | 無法辨識 | 任何不符合以上的輸入 | H |

> **8 個 intent，涵蓋估計 90%+ 的入站訊息。先不做更細的子 intent（例如把 `modify_reservation` 再拆），等上線後從 conversation log 決定。**

---

### Step 2 — 訂位主流程（Slot Filling）

`make_reservation` 是最複雜的多輪對話，需要 4 個 slot：

| Slot | Type | Validation | 若缺失 |
|------|------|-----------|--------|
| `branch` | 字串（門市名） | 必須是 15 間門市之一 | 問「請問要訂哪一間門市？」 |
| `party_size` | 整數 1–20 | > 10 人轉人工（包廂需求） | 問「請問幾位用餐？」 |
| `date` | 日期 | 今天起 60 天內，需營業日 | 問「請問哪一天？」 |
| `time` | 時間 | 11:30–14:00 / 17:00–21:30 | 問「請問幾點鐘？」 |

**完整對話流程（Happy Path）**:

```
1. User: 「我要訂位」
2. Bot:  「好的！請問要訂哪一間門市呢？
          [信義店] [大安店] [板橋店] …（快速選單）」
3. User: 選「大安店」
4. Bot:  「請問幾位用餐？」
5. User: 「4 個人」
6. Bot:  「請問哪一天呢？」
7. User: 「這個週六」→ 系統解析為 2026-04-11
8. Bot:  「請問幾點鐘？（可選時段：12:00 / 17:30 / 18:00 / 18:30 / 19:00）」
9. User: 選「18:30」
10. Bot: 「確認一下：大安店、4 位、4/11（六）18:30。這樣對嗎？
           [確認] [修改]」
11. User: 「確認」
12. Bot:  「訂位成功！✅ 訂位編號 #A2847。
           請於用餐前 30 分鐘抵達，逾時 15 分鐘將釋出桌位。
           需要取消或修改請回傳訂位編號。」
```

**例外路徑**:
- **人數 > 10**：「10 人以上訂位需要包廂，幫您轉接門市人員 😊」→ handoff
- **時段已滿**：「18:30 已客滿，附近時段 18:00 / 19:00 是否可以？」→ 重新選時段
- **非營業日（週一）**：「大安店週一公休，請選其他日期。」

---

### Step 3 — 查詢與取消流程（Single-turn + Confirmation）

**`check_reservation`**（單輪，需身份確認）:
```
User: 「查詢我的訂位」
Bot:  「請輸入訂位編號或手機號碼末 4 碼：」
User: 「2847」
Bot:  「找到了！#A2847 — 大安店，4位，4/11 18:30。
        [取消訂位] [修改訂位] [結束]」
```

**`cancel_reservation`**（強制 Confirmation，防誤觸）:
```
User: 「取消我的訂位」
Bot:  「請輸入訂位編號：」
User: 「A2847」
Bot:  「確認取消：大安店 4/11 18:30，4位。取消後無法恢復。
        [確定取消] [不取消]」
User: 「確定取消」
Bot:  「已取消 #A2847。期待下次光臨 🙏」
```

---

### Step 4 — Fallback 策略

```
第 1 次 fallback:
  Bot: 「抱歉沒聽懂 😅 我可以幫您：
         [訂位] [查詢訂位] [取消訂位] [門市資訊]」

第 2 次 fallback（連續）:
  Bot: 「讓我幫您轉接真人客服，稍等一下！」
       → 轉 LINE 客服帳號 or 留下電話回撥
```

---

### Step 5 — 指標目標設定

| Metric | 目標 | 計算方式 |
|--------|------|---------|
| Intent accuracy | > 88% | 前 1,000 筆對話人工抽樣驗證 |
| Containment rate | > 70% | 不觸發 handoff 的對話 / 總對話 |
| Fallback rate | < 12% | fallback intent 觸發次數 / 總訊息 |
| Reservation completion | > 65% | 進入 `make_reservation` 後成功完成 / 啟動 |
| CSAT | > 4.2/5 | 訂位完成後推送 1 題評分 |

---

## Result

```markdown
# Chatbot Design: 呷百二火鍋 LINE 訂位機器人

## Intent Catalog
| Intent | Description | Example Utterances | Priority |
|--------|-------------|-------------------|---------|
| make_reservation | 新訂位（多輪 slot filling） | "我要訂位", "幫我訂週六 4 位" | H |
| check_reservation | 查詢現有訂位 | "我的訂位是幾點", "確認預約" | H |
| cancel_reservation | 取消訂位（需 confirmation） | "取消我的訂位", "不去了" | H |
| modify_reservation | 修改人數或時間 | "改成 6 個人", "可以提早嗎" | M |
| check_availability | 詢問特定時段是否有位 | "週六 7 點還有位嗎" | M |
| check_hours | 詢問營業時間 | "幾點開始", "最晚幾點" | M |
| check_location | 詢問門市地點 | "大安店在哪裡" | L |
| fallback | 無法辨識的輸入 | — | H |

## Dialogue Flows

### make_reservation（主流程）
1. User: 「我要訂位」
2. Bot: 問門市（快速選單）
3. User: 選門市
4. Bot: 問人數
5. User: 回答人數（>10 → handoff）
6. Bot: 問日期
7. User: 回答日期
8. Bot: 問時間（僅顯示有空位的時段）
9. User: 選時間
10. Bot: 確認摘要 + [確認]/[修改]
11. User: 確認
12. Bot: 訂位成功 + 編號

### cancel_reservation
1. User: 「取消訂位」
2. Bot: 要求訂位編號
3. User: 提供編號
4. Bot: 顯示訂位詳情 + 二次確認
5. User: 確定取消
6. Bot: 取消成功

## Fallback Strategy
- 第 1 次 miss：重新導引 + 快速選單（4 個主要功能）
- 第 2 次連續 miss：轉真人客服

## Metrics Targets
| Metric | Target |
|--------|--------|
| Intent accuracy | > 88% |
| Containment rate | > 70% |
| Fallback rate | < 12% |
| Reservation completion | > 65% |
| CSAT | > 4.2/5 |
```

**三個上線前必做的事**:
1. 用 **真實門市員工以外的 10+ 位真實客人** 做 UAT，記錄他們第一句話的措辭（這就是 training data 的來源）
2. 把 `check_availability` 接到即時訂位系統，否則機器人顯示「有位」但系統沒位，會傷害信任
3. 設定 conversation log 每週 review 排程，前三個月每週看 50 筆失敗對話，每次更新 training data
