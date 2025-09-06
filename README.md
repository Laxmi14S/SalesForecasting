# 🛒 Sales Forecasting with Time Series (Superstore Dataset)

## 📖 Project Overview
This project demonstrates how businesses can **predict future sales trends** using time series forecasting techniques.  
The dataset is based on retail sales (Superstore dataset), and the goal is to generate **monthly forecasts** that help with:
- 📦 Inventory planning  
- 📈 Demand forecasting  
- 💰 Marketing & business decisions  


## 🛠️ Tech Stack
- **Python** (Pandas, Matplotlib, Statsmodels)  
- **ARIMA Time Series Forecasting**  
- **Excel/CSV data preprocessing**  


## 📂 Project Structure
SalesForecasting/
│── data/
│ └── stores_sales_forecasting.csv # Dataset
│── notebooks/
│ └── sales_forecast.py # Main forecasting script
│── README.md # Documentation




## ⚙️ Steps Performed
1. **Data Cleaning** → Handle missing sales, ensure correct date parsing.  
2. **Monthly Aggregation** → Convert daily sales into monthly totals.  
3. **Exploratory Data Analysis (EDA)** → Visualize historical sales trends.  
4. **ARIMA Forecasting** → Train ARIMA(1,1,1) model on monthly sales.  
5. **Forecasting Future Sales** → Generate 12-month predictions.  
6. **Visualization** → Compare actual vs forecasted sales trends.  



## 📊 Results
- **Graph 1** → Monthly Historical Sales Trend  
- **Graph 2** → Actual vs Forecasted Sales (12 months ahead)  

These insights can help retailers in **strategic planning** and **decision-making**.  

## 🚀 How to Run
```bash
# Clone the repo
git clone https://github.com/Laxmi14S/SalesForecasting.git
cd SalesForecasting

# Install dependencies
pip install pandas matplotlib statsmodels

# Run the script
python notebooks/sales_forecast.py