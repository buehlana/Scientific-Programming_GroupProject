import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import scipy.stats as stats
from datetime import datetime

st.set_page_config(layout="wide")

st.title("Stock Strategy Dashboard (Open→Close vs. Close→Next Open)")

# --- Sidebar for User Input ---
stocks = ['AAPL', 'GME', 'GOOGL', 'META', 'NFLX']
stock = st.sidebar.selectbox("Select a stock ticker", stocks, index=0)
start_date = st.sidebar.date_input("Start date", datetime(2020, 1, 1))
end_date = st.sidebar.date_input("End date", datetime(2025, 4, 25))

st.info(
    "With this dashboard, you can compare two simple trading strategies for different stocks and time periods. "
    "The strategies are: \n"
    "- **A**: Buy in the morning (Open), sell in the evening (Close)\n"
    "- **B**: Buy in the evening (Close), sell the next morning (Open)\n\n"
    "Select a ticker and a time range on the left. The plots and metrics below show the profits/losses of both strategies."
)

# --- Load data (Caching) ---
@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if df.empty:
        return df
    df = df.reset_index()
    return df

data = load_data(stock, start_date, end_date)

if data.empty:
    st.error("No data for this period/ticker!")
    st.stop()

st.write(f"**Data for {stock} from {start_date} to {end_date}** ({len(data)} rows)")
st.dataframe(data.tail())

# --- Calculate strategies ---
def calculate_strategies(df):
    df = df.sort_values(by='Date')
    df['Strategy_A'] = df['Close'] - df['Open']
    df['Strategy_B'] = df['Open'].shift(-1) - df['Close']
    df['Cumulative_A'] = df['Strategy_A'].cumsum()
    df['Cumulative_B'] = df['Strategy_B'].cumsum()
    return df

data = calculate_strategies(data)

# --- MultiIndex check ---
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# --- Debug output: Show all column names ---
st.write("Column names:", data.columns.tolist())

# --- Filter only rows without NaN in both strategies ---
valid = data.dropna(subset=['Strategy_A', 'Strategy_B'])
profits_a = valid['Strategy_A']
profits_b = valid['Strategy_B']

# --- Debug output: How many valid rows? ---
st.write(f"Valid data points after dropna: {len(profits_a)}")
st.write(valid[['Date', 'Strategy_A', 'Strategy_B']].head(10))

# --- Plots ---
tab1, tab2, tab3 = st.tabs(["Daily Profits", "Closing Prices", "Cumulative Profits"])

with tab1:
    st.subheader("Daily Profit per Strategy")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(data['Date'], data['Strategy_A'], label='Strategy A (Open→Close)')
    ax1.plot(data['Date'], data['Strategy_B'], label='Strategy B (Close→Next Open)')
    ax1.axhline(0, color='green', linestyle='--', linewidth=0.5)
    ax1.legend()
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Daily Profit ($)")
    ax1.set_title(f"{stock}: Daily Profits of Strategies")
    st.pyplot(fig1)

with tab2:
    st.subheader("Closing Price")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(data['Date'], data['Close'], color='steelblue')
    ax2.set_title(f"{stock}: Daily Closing Price")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Price ($)")
    st.pyplot(fig2)

with tab3:
    st.subheader("Cumulative Profits (summed up)")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    ax3.plot(data['Date'], data['Cumulative_A'], label='Strategy A')
    ax3.plot(data['Date'], data['Cumulative_B'], label='Strategy B')
    ax3.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    ax3.set_title(f"{stock}: Cumulative Profits")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Cumulative Return ($)")
    ax3.legend()
    st.pyplot(fig3)

# --- Statistical Analysis ---
st.subheader("Statistical Analysis: Strategy A vs. B")

# Minimum number of data points for test (e.g., 3, realistically better >= 10)
if len(profits_a) < 3:
    st.warning("Not enough data for the statistical test. "
               "Select a larger time period or a more liquid ticker.")
else:
    t_stat, p_value = stats.ttest_rel(profits_a, profits_b)
    mean_a = profits_a.mean()
    mean_b = profits_b.mean()
    st.write(f"**Mean Profit Strategy A:** {mean_a:.4f}")
    st.write(f"**Mean Profit Strategy B:** {mean_b:.4f}")
    st.write(f"**T-Statistic:** {t_stat:.4f}")
    st.write(f"**P-Value:** {p_value:.4f}")

    if p_value < 0.05:
        better = "A" if mean_a > mean_b else "B"
        st.success(f"Strategy {better} is statistically significantly better (p < 0.05)!")
    else:
        st.info("No statistically significant difference between the strategies.")

# --- Optional: Download Button ---
st.markdown("---")
st.download_button("Download data as CSV", data.to_csv(index=False), file_name=f"{stock}_strategies.csv")