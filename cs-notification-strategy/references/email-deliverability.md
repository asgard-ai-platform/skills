# Email Deliverability

> 本文補充 `cs-notification-strategy` SKILL.md 中「Email 傳遞性優化」這一面向。
> 聚焦於：DNS 認證設定、寄件者信譽、內容過濾、以及退信處理流程。

---

## 為什麼 Deliverability 比 Open Rate 更根本

Open Rate 衡量「打開率」，但前提是郵件先進收件匣。若郵件進垃圾桶或被擋下，
Open Rate 永遠是 0。

```
實際到達率 (Deliverability Rate) = 成功投遞數 / 發送嘗試數
收件匣到達率 (Inbox Placement Rate) = 進入收件匣數 / 成功投遞數

兩者都要量測，缺一不可。
```

業界標準：
- Deliverability Rate ≥ 95%（否則 ESP 可能限流）
- Inbox Placement Rate ≥ 85%（低於此值需立即排查）

---

## DNS 認證三件套：SPF、DKIM、DMARC

這三項缺任何一項，主流 ESP（Gmail、Outlook）都會對你降低信任分。

### SPF（Sender Policy Framework）

在 DNS TXT record 宣告哪些 IP 允許以你的 domain 發信。

**格式範例**：
```
v=spf1 include:sendgrid.net include:amazonses.com ~all
```

| 結尾符號 | 意義 |
|---------|------|
| `-all` | Hard fail：不在列表內的 IP 一律拒收 |
| `~all` | Soft fail：標記為可疑，不直接拒收（建議初期使用） |
| `?all` | Neutral：等同沒有 SPF，不建議 |

**陷阱**：SPF 查詢次數上限為 10 次（include、redirect 各算一次）。超過 10 次，
驗證直接 fail。用 `mxtoolbox.com/spf` 或 `dmarcian.com/spf-survey` 計算實際查詢數。

### DKIM（DomainKeys Identified Mail）

ESP 為每封郵件加上私鑰簽章，收件端用 DNS 公鑰驗證。

1. 在 ESP 後台產生 DKIM key pair
2. 將公鑰以 DNS TXT record 發布：
   ```
   selector._domainkey.yourdomain.com  TXT  "v=DKIM1; k=rsa; p=<公鑰>"
   ```
3. 金鑰長度使用 **2048-bit**（1024-bit 已被主流 ESP 視為不足）

**驗證指令**：
```bash
dig TXT selector._domainkey.yourdomain.com
```

### DMARC（Domain-based Message Authentication, Reporting & Conformance）

定義 SPF/DKIM 驗證失敗時的處理政策，並設定回報 Email。

**建議漸進式部署**：
```
# 第 1 階段：監控模式（收 report，不阻擋）
v=DMARC1; p=none; rua=mailto:dmarc-reports@yourdomain.com; pct=100

# 第 2 階段：隔離模式（SPF/DKIM 失敗進垃圾桶）
v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@yourdomain.com; pct=25

# 第 3 階段：完整執行
v=DMARC1; p=reject; rua=mailto:dmarc-reports@yourdomain.com; pct=100
```

切勿跳過 `p=none` 監控階段——直接上 `p=reject` 可能誤殺合法的第三方代送郵件
（如 CRM、客服系統）。

### 一次性確認清單

```
□ SPF record 存在且查詢次數 ≤ 10
□ DKIM 2048-bit，DNS 已發布公鑰
□ DMARC 已設定且在收 rua 回報
□ 有在讀 DMARC 週報（否則設了等於沒設）
□ Return-Path domain 與 From domain 一致（避免 alignment 失敗）
```

---

## 寄件者信譽（Sender Reputation）

信譽由三個維度組成：IP 信譽、Domain 信譽、內容信譽。

### IP 信譽

| 行為 | 對 IP 信譽的影響 |
|------|---------------|
| 高退信率（> 5%） | 嚴重負面，ESP 可能封 IP |
| 高投訴率（> 0.1%） | 嚴重負面 |
| 突然大量發信（IP Warming 未做） | 中度負面 |
| 長期穩定、低退信、低投訴 | 正面累積 |

**IP Warming 排程（新 IP 或長時間未發信的 IP）**：

```
第 1 天：    200 封
第 2 天：    500 封
第 3 天：  1,000 封
第 4 天：  2,000 封
第 5 天：  5,000 封
第 6 天： 10,000 封
第 7 天： 20,000 封
第 2 週：每日翻倍，直到目標量
```

原則：每個區間的退信率若 > 2%，停止增量，先清理名單再繼續。

### Domain 信譽（比 IP 信譽更持久）

Gmail 和 Outlook 都已將 Domain 信譽的權重拉高到與 IP 相當甚至更高。
Domain 信譽不會因為換 IP 而重置。

提升 Domain 信譽的核心行為：
1. 只發給**明確 opt-in** 的用戶
2. 維持**退訂機制暢通**（1-click unsubscribe，2024 年 Gmail 強制要求）
3. 用戶**與郵件互動**（開啟、點擊）是最強的正向信號

### 監控工具

| 工具 | 用途 | 費用 |
|------|------|------|
| Google Postmaster Tools | Gmail 的 IP/Domain 信譽、垃圾郵件率 | 免費 |
| Microsoft SNDS | Outlook/Hotmail 的 IP 狀態 | 免費 |
| MXToolbox | 綜合 DNS、blacklist 檢查 | 免費/付費 |
| GlockApps / Litmus | Inbox Placement 實際測試 | 付費 |

**必做**：Google Postmaster Tools 的「垃圾郵件率」欄位——Gmail 的官方要求是
**< 0.10%**，超過 0.30% 會開始大規模進垃圾桶。

---

## 名單衛生（List Hygiene）

差的名單是 Deliverability 最常見的破壞者。

### 退信分類與處理

```
Hard Bounce（永久無法投遞）
  └─ 原因：地址不存在、domain 不存在
  └─ 處理：立即從名單移除，永不重試

Soft Bounce（暫時無法投遞）
  └─ 原因：信箱滿、伺服器暫時拒收
  └─ 處理：重試 3 次（間隔 24h），仍失敗後移除

Complaint（用戶按「這是垃圾郵件」）
  └─ 處理：立即退訂，永不再發行銷信
  └─ 工具：設定 Feedback Loop（FBL）接收投訴通知
```

**退信率門檻**：

| 退信率 | 狀態 | 行動 |
|-------|------|------|
| < 2% | 健康 | 維持現狀 |
| 2–5% | 警告 | 清理非活躍名單 |
| > 5% | 危險 | 暫停發信，做名單清理 |
| > 10% | 緊急 | ESP 可能暫停帳戶 |

### 活躍度重啟流程（Re-engagement）

對於 **90 天未開信** 的用戶，執行以下流程再清理：

```
第 1 封（第 0 天）：「我們想念你」— 主題吸引人，突顯用戶利益
第 2 封（第 7 天）：提供具體好處（折扣、新功能）
第 3 封（第 14 天）：「這是最後一封，不想收請按此退訂」

三封都無反應 → 從主動行銷名單移除
```

**不要**對死名單強發——每次發信都在消耗 Domain 信譽。

---

## 內容過濾：避免觸發垃圾郵件判定

### 高風險內容模式

| 模式 | 說明 |
|------|------|
| 全大寫標題 | `FREE SHIPPING TODAY!!!` |
| 過多驚嘆號 | 每句結尾都用 `!` |
| 垃圾郵件關鍵字 | `click here`、`earn money`、`winner`、`guaranteed` |
| 圖片佔比 > 80% | 文字過少，過濾器無法判斷內容 |
| 缺少純文字版本 | 只有 HTML，沒有 plain text 備援 |
| 隱藏文字 | 白色文字在白色背景（用於塞關鍵字） |
| 連結縮短服務 | bit.ly 等被大量濫用，信譽差 |

### 建議的 HTML 結構

```html
<!-- 圖文比例建議：60% 文字 / 40% 圖片 -->
<!-- 主要 CTA 用文字按鈕，不要純圖片 -->
<!-- 每封信只有 1-2 個 CTA，不要超連結氾濫 -->

<table width="600" cellpadding="0" cellspacing="0">
  <tr>
    <td style="font-family: Arial, sans-serif; font-size: 16px; color: #333333;">
      <!-- 正文放在這裡 -->
    </td>
  </tr>
  <tr>
    <td>
      <!-- 1-click unsubscribe 必須存在 -->
      <a href="{unsubscribe_url}">退訂</a>
    </td>
  </tr>
</table>
```

### Gmail 2024 年強制要求（批量發信者 > 5,000/天）

1. **SPF 或 DKIM** 至少一項通過（兩項都過更好）
2. **DMARC** 政策至少為 `p=none`
3. **1-click unsubscribe**（RFC 8058，`List-Unsubscribe-Post` header）
4. 退訂後 **48 小時內**生效
5. 垃圾郵件率維持 **< 0.10%**

```
List-Unsubscribe: <https://yourdomain.com/unsubscribe?token={token}>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```

---

## ESP 選擇與設定考量

| ESP | 適合場景 | Taiwan 支援 |
|-----|---------|-----------|
| SendGrid | 大量行銷信 + 交易信混合 | 有台灣 IP pool |
| Amazon SES | 低成本、高量、自行管理信譽 | 需自己做 IP Warming |
| Mailchimp | 中小型行銷，介面友善 | 無台灣 IP，速度稍慢 |
| Postmark | 專注交易信，信譽極佳 | 好，延遲低 |

**交易信和行銷信應分開發送**（不同 IP、不同 subdomain）。
原因：行銷信信譽下降不應影響訂單確認、密碼重設等高優先級交易信。

```
行銷信：  marketing.yourdomain.com
交易信：  mail.yourdomain.com 或 transactional.yourdomain.com
```

---

## 快速診斷流程

收到 Deliverability 問題時，按以下順序排查：

```
1. 確認 DNS 認證
   └─ SPF/DKIM/DMARC 是否全部通過？
   └─ 工具：mail-tester.com 發一封測試信，看分數和報告

2. 確認是否在黑名單
   └─ mxtoolbox.com/blacklists.aspx
   └─ 若在黑名單：申請移除，同時找出被列入原因

3. 查看 Google Postmaster Tools
   └─ Domain/IP 信譽是否為 HIGH？
   └─ 垃圾郵件率是否 < 0.10%？

4. 確認退信率
   └─ 過去 30 天 Hard Bounce > 2%？ → 清理名單
   └─ 過去 30 天 Complaint > 0.10%？ → 降低頻率，改善內容

5. 測試 Inbox Placement
   └─ GlockApps 或 Mail-Tester 實際投遞測試
   └─ 確認哪些 ESP（Gmail/Outlook/Yahoo）有問題

6. 內容審查
   └─ 用 SpamAssassin 或 mail-tester.com 檢查 Spam Score
   └─ 目標：< 3.0 分（滿分 10，越低越好）
```

---

## 數字速查

| 指標 | 健康值 | 警戒值 | 危險值 |
|------|--------|--------|--------|
| Deliverability Rate | ≥ 98% | 95–97% | < 95% |
| Inbox Placement Rate | ≥ 90% | 85–89% | < 85% |
| Hard Bounce Rate | < 1% | 1–2% | > 2% |
| Spam Complaint Rate | < 0.05% | 0.05–0.10% | > 0.10% |
| Unsubscribe Rate/send | < 0.2% | 0.2–0.5% | > 0.5% |
| SpamAssassin Score | < 2.0 | 2.0–3.0 | > 3.0 |
