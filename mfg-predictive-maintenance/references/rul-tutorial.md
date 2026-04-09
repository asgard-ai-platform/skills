# LSTM-Based RUL Prediction — Worked Tutorial

This document walks through building a Remaining Useful Life (RUL) predictor using an LSTM
network on multivariate sensor time series. It uses the NASA CMAPSS turbofan dataset as a
concrete reference, but the pattern applies to any run-to-failure sensor data.

---

## Problem Setup

**Given:** A sequence of sensor readings from equipment startup until failure.

**Goal:** At any point during operation, predict how many cycles/hours remain before failure.

```
Time →
[s1, s2, ..., sk] [s1, s2, ..., sk] ... [s1, s2, ..., sk] ● FAILURE
 t=1                t=2                   t=T

RUL at t = T - t
RUL at T = 0
```

RUL is a **decreasing label**: at cycle 1 it equals (total life − 1); at the last cycle before
failure it equals 0.

---

## Data Shape Assumptions

| Variable | Symbol | Example |
|----------|--------|---------|
| Number of training engines | N | 100 |
| Sensor channels per timestep | k | 14 |
| Sequence window length | W | 30 cycles |
| Max RUL cap (see below) | RUL_max | 125 cycles |

Raw input shape per training sample: `(W, k)` → label: scalar RUL

---

## Step 1: Compute RUL Labels

```python
import pandas as pd

def add_rul(df: pd.DataFrame, rul_cap: int = 125) -> pd.DataFrame:
    """
    df must have columns: engine_id, cycle, [sensor cols...]
    Adds column 'rul' (capped).
    """
    max_cycle = df.groupby("engine_id")["cycle"].max().rename("max_cycle")
    df = df.join(max_cycle, on="engine_id")
    df["rul"] = df["max_cycle"] - df["cycle"]
    # Cap: very-new equipment has identical behavior to "125 cycles from failure"
    df["rul"] = df["rul"].clip(upper=rul_cap)
    df.drop(columns="max_cycle", inplace=True)
    return df
```

**Why cap RUL?** Early in equipment life, the sensor signal does not yet encode any
degradation information. Without capping, the model is forced to learn a distinction
(cycle 1 vs cycle 50) that the sensors cannot support, which worsens test-set RMSE.
A cap of 125–150 cycles is standard for CMAPSS; adjust based on your P-F interval
(from the parent skill) — a sensor that detects degradation 200 cycles out should use
a cap ≥ 200.

---

## Step 2: Normalize Sensors

Use **training-set statistics only**. Never normalize using the full dataset (leaks test
info into training).

```python
from sklearn.preprocessing import MinMaxScaler

SENSOR_COLS = ["s2","s3","s4","s7","s8","s9","s11","s12",
               "s13","s14","s15","s17","s20","s21"]  # CMAPSS useful sensors

scaler = MinMaxScaler()
train_df[SENSOR_COLS] = scaler.fit_transform(train_df[SENSOR_COLS])
test_df[SENSOR_COLS]  = scaler.transform(test_df[SENSOR_COLS])   # transform only
```

Drop constant sensors first (sensors with zero variance across training data contribute
noise, not signal).

```python
from sklearn.feature_selection import VarianceThreshold
vt = VarianceThreshold(threshold=0.01)
vt.fit(train_df[ALL_SENSOR_COLS])
SENSOR_COLS = [c for c, keep in zip(ALL_SENSOR_COLS, vt.get_support()) if keep]
```

---

## Step 3: Build Sliding Windows

```python
import numpy as np

def make_windows(df: pd.DataFrame,
                 sensor_cols: list[str],
                 window: int = 30) -> tuple[np.ndarray, np.ndarray]:
    X_list, y_list = [], []
    for _, engine_df in df.groupby("engine_id"):
        engine_df = engine_df.sort_values("cycle")
        sensors = engine_df[sensor_cols].values
        rul     = engine_df["rul"].values
        for i in range(len(sensors) - window + 1):
            X_list.append(sensors[i : i + window])   # shape (W, k)
            y_list.append(rul[i + window - 1])        # label at end of window
    return np.array(X_list, dtype=np.float32), np.array(y_list, dtype=np.float32)

X_train, y_train = make_windows(train_df, SENSOR_COLS, window=30)
# X_train.shape: (num_windows, 30, 14)
```

---

## Step 4: LSTM Architecture

A two-layer LSTM with dropout is a solid baseline. Don't start with Transformers or
attention — LSTM is mature, debuggable, and performs competitively on datasets of this
size.

```python
import torch
import torch.nn as nn

class RUL_LSTM(nn.Module):
    def __init__(self, input_size: int, hidden_size: int = 64,
                 num_layers: int = 2, dropout: float = 0.2):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout,
        )
        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
        )

    def forward(self, x):
        # x: (batch, seq_len, input_size)
        out, _ = self.lstm(x)
        last    = out[:, -1, :]   # take only the last timestep
        return self.fc(last).squeeze(-1)
```

**Architecture rationale:**

| Choice | Reason |
|--------|--------|
| `batch_first=True` | Matches NumPy window shape `(N, W, k)` |
| Last timestep only | We predict RUL at the end of the window, not at each step |
| hidden_size=64 | Enough capacity for 14 sensors; bigger rarely helps on CMAPSS |
| Two layers | Captures both short-term fluctuations and longer trend |

---

## Step 5: Training Loop

```python
from torch.utils.data import DataLoader, TensorDataset

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
EPOCHS = 50
LR     = 1e-3
BATCH  = 256

dataset = TensorDataset(
    torch.from_numpy(X_train),
    torch.from_numpy(y_train),
)
loader = DataLoader(dataset, batch_size=BATCH, shuffle=True)

model     = RUL_LSTM(input_size=len(SENSOR_COLS)).to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
criterion = nn.MSELoss()

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for xb, yb in loader:
        xb, yb = xb.to(DEVICE), yb.to(DEVICE)
        pred = model(xb)
        loss = criterion(pred, yb)
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        total_loss += loss.item() * len(xb)
    if epoch % 10 == 0:
        rmse = (total_loss / len(dataset)) ** 0.5
        print(f"Epoch {epoch:3d}  Train RMSE: {rmse:.2f}")
```

`clip_grad_norm_` prevents exploding gradients, which is common when sensor data has
occasional spikes.

---

## Step 6: Evaluation Metrics

Use **two metrics**, not just RMSE:

### RMSE (Root Mean Squared Error)

```
RMSE = sqrt( mean( (RUL_pred - RUL_true)^2 ) )
```

Target: < 20 cycles on CMAPSS FD001. Raw gradient-boosted baselines typically land at
~25–30; a tuned LSTM should reach 15–18.

### NASA Scoring Function (asymmetric penalty)

Predicting failure *too late* is worse than predicting it *too early* — you want to
penalize late predictions more heavily.

```
d = RUL_pred - RUL_true

Score = sum(
    exp(-d/13) - 1    if d < 0   (early prediction)
    exp( d/10) - 1    if d >= 0  (late prediction)
)
```

The asymmetry (13 vs 10) encodes the domain truth: a false alarm costs you one
unnecessary inspection; a missed alarm costs you an unplanned failure event.

```python
def nasa_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    d = y_pred - y_true
    scores = np.where(d < 0, np.exp(-d / 13) - 1, np.exp(d / 10) - 1)
    return float(scores.sum())
```

Lower score = better. A model with excellent RMSE but poor NASA score is systematically
predicting late — a dangerous model in production.

---

## Step 7: Test-Set Prediction (One Label Per Engine)

At test time, CMAPSS provides sensor sequences that stop at some unknown point *before*
failure. You receive one label per engine: the true RUL at the moment the sequence ends.

```python
def predict_engine(engine_df: pd.DataFrame,
                   model: nn.Module,
                   sensor_cols: list[str],
                   window: int = 30) -> float:
    model.eval()
    engine_df = engine_df.sort_values("cycle")
    sensors = engine_df[sensor_cols].values
    if len(sensors) < window:
        # Pad with the first row if sequence too short
        pad = np.repeat(sensors[[0]], window - len(sensors), axis=0)
        sensors = np.vstack([pad, sensors])
    # Use last `window` cycles
    x = sensors[-window:][np.newaxis, ...]   # (1, W, k)
    x = torch.from_numpy(x.astype(np.float32)).to(DEVICE)
    with torch.no_grad():
        rul_pred = model(x).item()
    return max(rul_pred, 0.0)   # RUL cannot be negative
```

---

## Worked Numbers: CMAPSS FD001

| Phase | RMSE | NASA Score |
|-------|------|------------|
| Threshold baseline (mean RUL) | 57.8 | 33,000 |
| Random Forest (window features) | 24.3 | 8,200 |
| LSTM (this tutorial, default params) | 16.1 | 2,400 |
| LSTM + attention (not covered here) | 13.8 | 1,900 |

These are representative, not reproduced from a specific paper. Your production dataset
will differ; use these as sanity-check benchmarks, not targets.

---

## Hyperparameter Sensitivity

Run a simple grid before over-engineering:

| Parameter | Default | Try Also | Impact |
|-----------|---------|----------|--------|
| `window` | 30 | 20, 50 | High — must cover P-F interval |
| `hidden_size` | 64 | 32, 128 | Medium |
| `rul_cap` | 125 | 100, 150 | High — shifts label distribution |
| `dropout` | 0.2 | 0.1, 0.3 | Low–medium |
| `lr` | 1e-3 | 5e-4 | Low (Adam is robust) |

Window length is the most impactful parameter and should be set based on your equipment's
known P-F interval. If vibration monitoring gives you a 2-week warning window and you
sample every 15 minutes, your window should be roughly `2 × 24 × 4 = 192` timesteps.

---

## When LSTM Is the Wrong Choice

| Situation | Better Approach |
|-----------|----------------|
| < 20 run-to-failure examples | Weibull/exponential degradation model |
| No failure labels at all | Anomaly detection (Autoencoder on normal data) |
| < 6 months of data collected | Threshold alerts, defer ML |
| Need interpretability for compliance | Gradient Boosting with engineered features |
| Deployment on edge device (limited RAM) | 1D-CNN (faster inference, smaller footprint) |

LSTM earns its complexity only when you have: (a) multiple complete run-to-failure cycles,
(b) time-series sensor data with temporal dependencies across 10+ timesteps, and (c)
enough data that a 64-unit LSTM won't overfit (rough rule: ≥ 500 training windows).

---

## Deployment Checklist

- [ ] Scaler (`MinMaxScaler`) serialized alongside the model — applying wrong normalization
  at inference is a silent, common error
- [ ] Model outputs clipped to `[0, RUL_max]` — raw LSTM output can go negative or above cap
- [ ] Alert threshold defined: at what predicted RUL do you trigger a work order? (Not zero —
  you need lead time for parts procurement)
- [ ] Monitoring: log predicted RUL daily per asset; a sudden drop of > 20% in one reading
  warrants investigation of sensor health, not immediate shutdown
- [ ] Retrain schedule: models trained on 2023 data degrade if operating conditions shift
  (new operators, process changes, seasonal temperature); retrain annually or when RMSE
  on recent data exceeds your baseline by > 20%
