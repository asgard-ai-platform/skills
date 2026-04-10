# Example: 台灣電商平台年度訂單量預測

## Scenario

**公司：** 好買網（HaoMai.com.tw），台灣中型 B2C 電商，主力品類為美妝與保健食品。

**需求：** 行銷部門 2025-Q4 預算規劃截止日為 2025-10-15。分析師 Amy 需要預測 2025-10-01 至 2025-12-31 每日訂單量，以利倉儲人力配置與廣告預算分配。手上有 2023-01-01 起的完整日訂單量數據（共 1,003 天），訂單量呈穩定成長趨勢，雙十一與聖誕前後有明顯峰值，週末較平日低約 15-20%。

**Amy 的問題：**
> 「我有兩年多的日訂單資料，想跑 90 天預測。雙十一跟耶誕商機我一定要抓到，ARIMA 之前試過抓不到節慶效果，有推薦的做法嗎？」

---

## Analysis

### Phase 1：Input Validation

Amy 整理出的 DataFrame（`orders.csv`）：

| ds | y |
|---|---|
| 2023-01-01 | 4,210 |
| 2023-01-02 | 3,987 |
| … | … |
| 2025-09-30 | 7,340 |

檢查清單：
- **長度：** 1,003 天 ✓（> 2 個年度季節週期）
- **缺漏值：** 2024-02-10（農曆除夕）有缺漏 → Prophet 原生容忍缺值，不需補插
- **成長型態：** y 從 ~4,200 成長至 ~7,300，約年增 15%，選 `growth='linear'`
- **異常值：** 2024-11-11 單日 18,500（雙十一）、2024-12-25 單日 14,200，為真實節慶峰值，**不刪除，以 holiday 建模**

**Gate 通過：** 格式正確，資料長度足夠。

---

### Phase 2：Core Algorithm

#### 2a. 建立 Holiday DataFrame

Amy 定義三類假日：

```python
import pandas as pd
from prophet import Prophet

# 台灣法定假日（內建）
# 額外自定義節慶
custom_holidays = pd.DataFrame({
    'holiday': [
        '雙十一', '雙十一',
        '耶誕季', '耶誕季',
        '母親節', '母親節',
    ],
    'ds': pd.to_datetime([
        '2023-11-11', '2024-11-11',
        '2023-12-24', '2024-12-24',
        '2023-05-14', '2024-05-12',
    ]),
    'lower_window': [-1, -1, -3, -3, -2, -2],   # 前幾天開始影響
    'upper_window': [1,  1,  1,  1,  1,  1],    # 後幾天延續
})
```

`lower_window=-1` 讓模型捕捉雙十一預熱日（11/10）；`upper_window=1` 捕捉隔日出貨補單。

#### 2b. 模型設定

```python
m = Prophet(
    growth='linear',
    changepoint_prior_scale=0.08,   # 略高於預設 0.05，允許成長加速
    seasonality_mode='multiplicative',  # 季節振幅隨趨勢成長
    yearly_seasonality=True,
    weekly_seasonality=True,
    holidays=custom_holidays,
)

# 加入台灣國定假日
m.add_country_holidays(country_name='TW')

m.fit(df)  # df = orders.csv 的 ds/y 欄
```

**為何選 `multiplicative`：** 雙十一峰值在 2023 年約為基準的 3.2×，2024 年成長至 3.5×；振幅與趨勢同步放大，Additive 模式會低估 2025 年峰值。

#### 2c. 產生預測

```python
future = m.make_future_dataframe(periods=92)   # 到 2025-12-31
forecast = m.predict(future)
```

---

### Phase 3：Verification

#### 交叉驗證

```python
from prophet.diagnostics import cross_validation, performance_metrics

df_cv = cross_validation(
    m,
    initial='540 days',   # 前 18 個月訓練
    period='30 days',     # 每 30 天滾動一次
    horizon='90 days',    # 評估未來 90 天
)
df_perf = performance_metrics(df_cv)
```

**結果：**

| horizon | MAPE | RMSE |
|---------|------|------|
| 7 days | 4.2% | 318 |
| 30 days | 6.1% | 467 |
| 90 days | 8.7% | 589 |

MAPE 8.7% 在 90 天 horizon 符合行銷預算規劃的可接受誤差（< 10%）。**Gate 通過。**

#### 元件目測

- **Trend：** 線性上升，2024-Q3 偵測到一個 changepoint（配合品牌重塑活動），合理
- **yearly_seasonality：** Q4 明顯高峰、Q1 農曆年後低谷，符合直覺
- **weekly_seasonality：** 週六、日較週間低 16-18%，與歷史觀察一致
- **holidays：** 雙十一效果係數 +2.8（乘積），耶誕季 +1.6，模型正確捕捉

---

### Phase 4：Output

最終結果（節錄關鍵日期）：

```json
{
  "forecasts": [
    {"ds": "2025-10-01", "yhat": 7510, "yhat_lower": 6820, "yhat_upper": 8240},
    {"ds": "2025-10-10", "yhat": 7680, "yhat_lower": 6950, "yhat_upper": 8450},
    {"ds": "2025-11-10", "yhat": 9200, "yhat_lower": 8100, "yhat_upper": 10350},
    {"ds": "2025-11-11", "yhat": 25800, "yhat_lower": 22400, "yhat_upper": 29600},
    {"ds": "2025-11-12", "yhat": 11400, "yhat_lower": 9800, "yhat_upper": 13200},
    {"ds": "2025-12-24", "yhat": 19200, "yhat_lower": 16800, "yhat_upper": 21900},
    {"ds": "2025-12-25", "yhat": 14500, "yhat_lower": 12600, "yhat_upper": 16600},
    {"ds": "2025-12-31", "yhat": 8900, "yhat_lower": 7800, "yhat_upper": 10100}
  ],
  "components": {
    "trend": "linear_upward_15pct_annual",
    "yearly_seasonality": "peak_in_november_december_trough_in_february",
    "weekly_seasonality": "weekday_16pct_above_weekend",
    "holiday_effects": {
      "雙十一": "multiplicative_x2.8",
      "耶誕季": "multiplicative_x1.6"
    }
  },
  "metadata": {
    "mape_90d": 0.087,
    "rmse_90d": 589,
    "training_days": 1003,
    "forecast_days": 92,
    "changepoints_detected": 3,
    "seasonality_mode": "multiplicative"
  }
}
```

---

## Result

**Amy 的 Q4 預測摘要：**

| 期間 | 預測日均訂單量 | 關鍵峰值 |
|---|---|---|
| 2025-10 | ~7,600 | 一般日，國慶連假略降 |
| 2025-11 | ~10,400（含雙十一） | 11/11 單日 25,800 |
| 2025-12 | ~12,100（含耶誕） | 12/24 單日 19,200 |

**行動建議：**

1. **倉儲人力：** 11/08–11/12 及 12/22–12/26 需提前 3 週備齊加班人力；單日峰值訂單量約為平日 3-4×。
2. **廣告預算：** 依 `yhat_lower` 與 `yhat_upper` 設定保守/積極兩套預算；雙十一區間寬度（±14%）反映年際波動，建議保留 15% 彈性備用金。
3. **監控觸發：** 若 11/11 實際訂單量超出 `yhat_upper`（29,600），啟動緊急補貨 SOP。

**值得注意的 Gotcha：**
- Amy 原先未加 `lower_window=-1`，導致 11/10 預熱日預測偏低 22%；加入後誤差降至 5%。
- `seasonality_mode` 從 `additive` 改為 `multiplicative` 後，雙十一峰值預測從 21,000 提升至 25,800，更接近 2024 年實際值 26,100。
