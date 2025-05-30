# Stock Strategy comparison project 

This project analyzes two trading strategies ("Buy at Open, Sell at Close" vs "Buy at Close, Sell at Next Open") across five major stocks (AAPL, GME, GOOGL, META, NFLX) over the period November 2024 – April 2025.
It collects real-world stock data, prepares it, saves it into a csv file, a SQLite database, performs statistical analyses (paired t-test, p-values), generates visualizations, and checks normality assumptions using QQ-plots.

## Features
1. Real-world data collection via Yahoo Finance API (yfinance)
2. Data cleaning, preparation, and validation (with regex)
3. Storage and retrieval from a SQLite database
4. QQ-plot analysis for normality checking
5. Statistical comparison of two trading strategies using paired t-tests
6. Multiple visualizations: profit plots, cumulative returns
7. Full codebase ready for local run (no external API keys needed)
8. ollama
9. Streamlit 

## Project Structure
.gitinore
code.ipynb 
README.md
requirements.txt
stocks_data.csv
stock.db
streamlit.py

## Libraries needed for the project 
can be found in requirements.txt 

## Ollama Project

## Description
This project connects to a locally running Ollama server and sends prompts to a downloaded model (e.g., Mistral).

## Requirements
- Ollama installed and running (`https://ollama.com/download`)
- Python 3
- `requests` library

## Setup
1. Install Python libraries:
```bash
pip install -r requirements.txt
pip install streamlit
run streamlit streamlit.py

## Streamlit Project 
 