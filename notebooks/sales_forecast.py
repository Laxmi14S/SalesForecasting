import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# === Step 1: Dataset Path ===
DATA_PATH = r"E:\SalesForecasting\data\stores_sales_forecasting.csv"
DATE_COL = "Order Date"

# === Step 2: Load CSV safely ===
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ Dataset not found at {DATA_PATH}")

try:
    df = pd.read_csv(DATA_PATH, encoding="latin1", parse_dates=[DATE_COL])
except Exception as e:
    raise RuntimeError(f"Error reading CSV: {e}")

print("✅ Dataset loaded successfully")
print("Columns:", df.columns.tolist())
print(df[[DATE_COL, "Sales"]].head())

# === Step 3: Clean & Prepare ===
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")  # Ensure numeric
df = df.dropna(subset=["Sales"])  # Drop rows with missing sales

# === Step 4: Monthly Aggregation ===
df_monthly = df.groupby(pd.Grouper(key=DATE_COL, freq="M"))["Sales"].sum().reset_index()
print("Monthly data prepared:")
print(df_monthly.head())

# === Step 5: Plot Historical Sales Trend ===
plt.figure(figsize=(12, 6))
plt.plot(df_monthly[DATE_COL], df_monthly["Sales"], marker="o", linestyle="-")
plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# === Step 6: ARIMA Forecasting ===
sales_series = df_monthly.set_index(DATE_COL)["Sales"]

# Simple ARIMA model (p,d,q = 1,1,1 for demo)
model = ARIMA(sales_series, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next 12 months
forecast_steps = 12
forecast = model_fit.forecast(steps=forecast_steps)

# === Step 7: Plot Actual + Forecast ===
plt.figure(figsize=(12, 6))
plt.plot(sales_series.index, sales_series, label="Actual Sales", marker="o")
plt.plot(
    pd.date_range(sales_series.index[-1] + pd.offsets.MonthBegin(),
                  periods=forecast_steps, freq="M"),
    forecast,
    label="Forecasted Sales",
    marker="o",
    linestyle="--",
    color="orange"
)
plt.title("Sales Forecast (Next 12 Months)", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
