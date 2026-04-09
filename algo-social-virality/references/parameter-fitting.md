# Parameter Fitting for Viral Spread Models

估計 β（傳播率）與 γ（恢復率）是所有 SIR/SIS/SEIR 模型中最脆弱的步驟。以下提供三種實用方法，以及從早期資料估計參數的完整流程。

---

## 核心公式回顧

SIR 模型的 R0 與參數關係：

```
R0 = β / γ

β = 每單位時間內，一個感染者傳播給一個易感者的機率
γ = 每單位時間內，感染者「恢復」（停止分享）的率
```

平均感染期（content 的「分享壽命」）：

```
D = 1 / γ
```

若你知道典型分享壽命，就直接得到 γ；剩下的是估計 β。

---

## 方法 A：指數成長期線性回歸（最實用）

當 I 很小（I << N），SIR 模型的感染方程式近似為：

```
dI/dt ≈ (β - γ) · I
```

這是純指數成長。對兩邊取 log：

```
ln(I(t)) ≈ ln(I₀) + r · t

其中 r = β - γ（早期成長率）
```

**步驟：**

1. 取前 T_early 個時間點（感染者 < 10% N 的時段）
2. 計算 `ln(累積分享數)` 對 t 做線性回歸
3. 斜率即為 `r = β - γ`
4. 用獨立估計的 γ 解出 β

**Python 範例：**

```python
import numpy as np

# 早期分享數（每小時）: 小時 1-8
t = np.array([1, 2, 3, 4, 5, 6, 7, 8])
I = np.array([10, 18, 31, 52, 90, 155, 268, 455])

log_I = np.log(I)
coeffs = np.polyfit(t, log_I, deg=1)
r = coeffs[0]          # 早期成長率
I0_est = np.exp(coeffs[1])

print(f"r = {r:.4f}")  # β - γ
print(f"I0 ≈ {I0_est:.1f}")
```

**範例數值：**
- 輸入：如上資料
- 輸出：r ≈ 0.543
- 若假設 γ = 0.2（平均 5 小時分享壽命），則 β ≈ 0.743
- R0 = 0.743 / 0.2 ≈ **3.7**

**適用條件：** 早期資料點 ≥ 5 個，且 R0 > 1（有明顯成長趨勢）。

---

## 方法 B：最小平方擬合 ODE（完整資料）

當你有整段傳播曲線（從起點到峰值甚至下降段），用數值最佳化直接擬合 ODE。

**目標函式：**

```
minimize Σ (I_observed(t) - I_model(t; β, γ))²
over (β, γ)
```

**Python 完整範例：**

```python
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize

# 觀測資料（時間點, 活躍分享者數）
t_obs = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
I_obs = np.array([10, 18, 32, 55, 88, 130, 170, 195, 190, 165, 130, 90, 55])
N = 10000

def sir_model(y, t, beta, gamma, N):
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dR]

def objective(params):
    beta, gamma = params
    if beta <= 0 or gamma <= 0:
        return 1e10
    y0 = [N - I_obs[0], I_obs[0], 0]
    sol = odeint(sir_model, y0, t_obs, args=(beta, gamma, N))
    I_model = sol[:, 1]
    return np.sum((I_model - I_obs) ** 2)

# 初始猜測：用方法 A 的結果
result = minimize(objective, x0=[0.5, 0.2],
                  method='Nelder-Mead',
                  options={'xatol': 1e-6, 'fatol': 1e-6})

beta_fit, gamma_fit = result.x
R0_fit = beta_fit / gamma_fit

print(f"β = {beta_fit:.4f}")
print(f"γ = {gamma_fit:.4f}")
print(f"R0 = {R0_fit:.2f}")
```

**注意事項：**
- 初始猜測值影響收斂，建議先跑方法 A 取得 β 初值
- 若 I 的數量級差異大，改用 `np.sum((np.log(I_model+1) - np.log(I_obs+1))**2)` 作為目標函式

---

## 方法 C：從先驗知識直接設定（無資料時）

當你沒有現成擴散資料，靠歷史基準值設定參數。

### γ 的估計（分享壽命）

| 內容類型 | 典型分享壽命 | γ（每小時） |
|---------|------------|------------|
| Twitter/X 熱門話題 | 2-6 小時 | 0.17 - 0.50 |
| Instagram Reel | 12-24 小時 | 0.04 - 0.08 |
| YouTube 影片（趨勢期） | 2-5 天 | 0.008 - 0.021 |
| LinkedIn 貼文 | 3-7 天 | 0.006 - 0.014 |
| 新聞事件（社群討論） | 1-3 天 | 0.014 - 0.042 |

選定 γ 後，D = 1/γ 就是模型中的「平均活躍分享時長」。

### β 的估計（傳播率）

β 難以直接觀測，通常透過 R0 假設來反推：

```
β = R0 × γ
```

R0 的典型範圍（social content）：

| 情境 | R0 | 備註 |
|------|----|------|
| 普通貼文，自然擴散 | 0.5 - 0.9 | 通常不會爆發 |
| 有一定受眾的內容 | 1.0 - 1.5 | 緩慢成長 |
| 強 KOL 推波 + 時事 | 2.0 - 4.0 | 典型病毒式擴散 |
| 極端事件 / meme | 5.0 - 10.0 | 罕見，短暫爆發 |

**流程：**

```
1. 判斷內容類型 → 查表得 γ
2. 評估 R0 情境 → 計算 β = R0 × γ
3. 帶入 SIR 模型做情境模擬（worst/base/best case）
```

---

## 選擇哪種方法

```
有早期資料（前 5-10 個時間點）且 R0 > 1？
  → 方法 A（快速，適合即時預測）

有完整曲線資料（含峰值或下降段）？
  → 方法 B（最準確，事後分析）

無現成資料，做規劃或情境分析？
  → 方法 C（先驗假設，必須做敏感度分析）
```

---

## 敏感度分析（必做）

R0 的微小變動對最終感染人數影響非線性，**參數不確定時務必跑多情境**。

```python
import numpy as np

def final_size_approx(R0):
    """
    SIR 模型最終感染比例的近似解（transcendental equation 數值解）
    z = 1 - exp(-R0 * z)
    """
    z = 0.5  # 初始猜測
    for _ in range(1000):
        z_new = 1 - np.exp(-R0 * z)
        if abs(z_new - z) < 1e-10:
            break
        z = z_new
    return z

scenarios = [
    ("保守", 0.8),
    ("基準", 1.5),
    ("樂觀", 2.5),
    ("爆發", 4.0),
]

print(f"{'情境':8} {'R0':6} {'最終感染比例':12}")
print("-" * 30)
for name, R0 in scenarios:
    if R0 > 1:
        z = final_size_approx(R0)
    else:
        z = 0.0  # 低於閾值，趨近於零
    print(f"{name:8} {R0:6.1f} {z*100:10.1f}%")
```

**輸出：**

```
情境     R0     最終感染比例
------------------------------
保守      0.8          0.0%
基準      1.5         58.3%
樂觀      2.5         89.2%
爆發      4.0         98.1%
```

這張表說明了 IRON LAW 的實際意義：R0 從 0.8 到 1.5 是「無爆發」到「58% 覆蓋」的分水嶺，不是線性關係。

---

## 常見陷阱

**累積 vs 活躍分享者混淆**

方法 A 的 I(t) 必須是**活躍分享者**（當前正在傳播），不是累積分享數。若你只有累積資料：

```
I(t) ≈ cumulative(t) - cumulative(t - D)

其中 D = 1/γ（分享壽命的整數近似）
```

**資料太少時不要用方法 B**

少於 5 個資料點時，ODE 擬合會 overfit。β 和 γ 可以各自很大或很小，只要 R0 相同，擬合誤差都接近。這時用方法 A 或 C 更穩健。

**平台演算法加速**

β 本質上是「暴露 → 分享」的轉換率。若平台推薦演算法在 t=3 之後大力推播，β 在早期和晚期可能不一樣。若你觀察到成長率突然加速，考慮用**分段 β**（t < t_boost 用 β₁，之後用 β₂）。

**時間單位要一致**

若 γ 用「每天」定義，β 也必須是「每天」。混用小時和天是最常見的計算錯誤。建議統一用小時（社群內容）或天（較慢擴散的內容）。
