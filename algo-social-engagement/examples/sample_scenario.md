# Example: 台灣美妝品牌 Instagram 季度互動率分析與基準比較

## Scenario

**Lumière Cosmetics** 是一家台灣中型美妝品牌，Instagram 帳號有 48,000 名追蹤者。社群經理 Fiona 在 2026 年 Q1 結束後，被主管要求提交互動率報告，並回答：「我們的表現是否優於同業？」

Fiona 從 Instagram Insights 匯出 30 篇貼文資料（2026/01/01–2026/03/31），格式如下：

| 貼文類型 | 篇數 | 總按讚 | 總留言 | 總分享 | 總觸及（Reach） | 發布時粉絲數 |
|---------|------|--------|--------|--------|--------------|------------|
| 產品圖文 | 14 | 18,200 | 1,540 | 380 | 312,000 | 47,500 |
| Reel 短影音 | 10 | 32,400 | 2,890 | 1,240 | 520,000 | 47,800 |
| 活動限時優惠 | 6 | 4,100 | 890 | 120 | 98,000 | 48,000 |

主管補充：「另外我看到競品 @glow_daily 的貼文按讚都很高，感覺他們互動率比我們好，你確認一下。」@glow_daily 公開資料：粉絲 22,000，最近 10 篇貼文平均按讚 680、留言 45、分享 12，無 Insights 存取權（無觸及數）。

---

## Analysis

### Phase 1：輸入驗證 & 分母確認

**Lumière（自家帳號）**：有 Instagram Insights，可使用 **ER by Reach**（最精確）。  
**@glow_daily（競品）**：僅有公開數據，只能使用 **ER by Followers**。

> IRON LAW 觸發：兩者分母不同，**不可直接比較數字**。需轉換為同一基準或明確標注差異。

Reel 短影音與圖文貼文的互動行為不同（Reel 的「分享」代表更高承諾），需分群計算，不混合平均。

---

### Phase 2：核心計算

#### Lumière — ER by Reach（各貼文類型）

**產品圖文（14 篇）**
```
總互動 = 18,200 + 1,540 + 380 = 20,120
ER by Reach = 20,120 / 312,000 × 100% = 6.45%
平均每篇 ER = 6.45%（已是跨 14 篇加總，單篇平均需÷14再個別算）
```

實際每篇平均：
- 平均觸及 = 312,000 / 14 = 22,286
- 平均互動 = 20,120 / 14 = 1,437
- 平均 ER by Reach = 1,437 / 22,286 × 100% = **6.45%**

**Reel 短影音（10 篇）**
```
總互動 = 32,400 + 2,890 + 1,240 = 36,530
平均觸及 = 520,000 / 10 = 52,000
平均互動 = 36,530 / 10 = 3,653
平均 ER by Reach = 3,653 / 52,000 × 100% = 7.03%
```

加權互動（share=3×, comment=2×, like=1×）：
```
加權互動 = 32,400×1 + 2,890×2 + 1,240×3 = 32,400 + 5,780 + 3,720 = 41,900
加權 ER = (41,900/10) / 52,000 × 100% = 8.06%
```
→ Reel 的加權 ER 明顯高於基礎 ER，說明分享比例高，內容擴散力強。

**活動限時優惠（6 篇）**
```
總互動 = 4,100 + 890 + 120 = 5,110
平均觸及 = 98,000 / 6 = 16,333
平均互動 = 5,110 / 6 = 852
平均 ER by Reach = 852 / 16,333 × 100% = 5.21%
```

#### Lumière — 整體跨類型平均 ER by Reach

```
總互動 = 20,120 + 36,530 + 5,110 = 61,760
總觸及 = 312,000 + 520,000 + 98,000 = 930,000
整體 ER by Reach = 61,760 / 930,000 × 100% = 6.64%
```

#### Lumière — ER by Followers（供跨帳號比較用）

```
發布時平均粉絲 ≈ 47,767（三段加權平均估算）
整體 ER by Followers = 61,760 / (47,767 × 30) × 100%
= 61,760 / 1,433,010 × 100% = 4.31%
```

#### @glow_daily — ER by Followers（競品）

```
平均互動 = 680 + 45 + 12 = 737（每篇）
ER by Followers = 737 / 22,000 × 100% = 3.35%
```

---

### Phase 3：驗證 & 基準比較

**台灣美妝產業 Instagram 基準（2026 Q1）：**

| 分母 | 產業中位數 | 優秀水準（前 25%） |
|------|-----------|-----------------|
| ER by Reach | 4.2% | > 7.0% |
| ER by Followers | 1.8% | > 3.5% |

| 帳號 | ER by Followers | 帳號規模 | 評估 |
|------|----------------|---------|------|
| Lumière（自家） | 4.31% | 4.8 萬 | 優秀（前 25%） |
| @glow_daily（競品） | 3.35% | 2.2 萬 | 良好（前 40%） |

> 注意：@glow_daily 帳號規模約為 Lumière 的 46%。小帳號 ER by Followers 天然偏高，3.35% 對 2.2 萬粉絲帳號屬正常範圍；Lumière 以 4.8 萬粉絲維持 4.31% 實屬難得。

**Reel vs 圖文 ER by Reach 差異**（7.03% vs 6.45%）落差不大，但加權 ER（8.06% vs ~6.8%）顯示 Reel 的分享行為更活躍。

**異常值檢查**：無任何貼文 ER > 20%，資料合理。

---

## Result

```json
{
  "metrics": {
    "avg_er_by_reach": 6.64,
    "avg_er_by_followers": 4.31,
    "median_er_by_reach": 6.45,
    "top_post_type_er": 7.03,
    "weighted_er_reels": 8.06
  },
  "benchmark": {
    "platform": "instagram",
    "industry": "beauty_taiwan",
    "benchmark_er_by_followers": 1.8,
    "percentile": "top_25pct",
    "competitor_er_by_followers": 3.35,
    "competitor_account_size": 22000
  },
  "metadata": {
    "posts_analyzed": 30,
    "period": "2026-Q1",
    "denominator_self": "reach",
    "denominator_competitor": "followers",
    "note": "Cross-account comparison uses ER by followers only. Direct reach comparison not possible for competitor."
  }
}
```

**給 Fiona 的結論摘要：**

1. **自家表現優秀**：整體 ER by Reach 6.64%，高於台灣美妝產業優秀門檻（7.0% 以 reach 計；Lumière 達到此水準）。
2. **競品比較要謹慎**：@glow_daily ER by Followers 3.35% 低於 Lumière 的 4.31%，且其帳號規模更小（小帳號天然 ER 較高），**Lumière 實際上優於競品**，主管的直覺有誤。
3. **Reel 擴散力最強**：加權 ER 8.06%，分享比例高，建議 Q2 增加 Reel 佔比。
4. **活動貼文 ER 最低**（5.21% by Reach）：優惠訊息的觸及轉換效率較差，考慮改用 Story 或限時動態傳遞促銷，保留 Feed 給品牌內容。
