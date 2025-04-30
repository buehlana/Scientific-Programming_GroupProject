# Phase 7
# Build a Streamlit dashboard: Input: stock ticker, date range Output: charts, metrics, LLM insight

import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
from PIL import Image

image = Image.open("return_comparison.png")



# Set the title of the app
st.title("Stock Price Analysis Dashboard")
st.write("This dashboard allows you to analyze stock prices and strategies.")
# Sidebar for user input
st.sidebar.header("User Input")
# Stock ticker input
stock_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
# Date range input
start_date = st.sidebar.date_input("Start Date", datetime(2024, 11, 1))
end_date = st.sidebar.date_input("End Date", datetime(2025, 4, 1))
# Convert date inputs to string
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
# Start application
st.write(f"Analyzing data for {stock_ticker} from {start_date_str} to {end_date_str}")
# Filter data based on user input


