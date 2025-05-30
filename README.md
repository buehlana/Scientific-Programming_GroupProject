# Stock Strategy comparison project 

This project analyzes two trading strategies ("Buy at Open, Sell at Close" vs "Buy at Close, Sell at Next Open") across five major stocks (AAPL, GME, GOOGL, META, NFLX) over the period November 2024 – April 2025.
It collects real-world stock data, prepares it, saves it into a csv file, a SQLite database, performs statistical analyses (paired t-test, p-values), generates visualizations, and checks normality assumptions using QQ-plots.

## Features
1. Real-world data collection via Yahoo Finance API (yfinance)
2. Data cleaning, preparation, and validation (with regex)
3. Local data storage as CSV and in a SQLite database
4. Computation of two trading strategies:
    Strategy A: Buy at Open → Sell at Close
    Strategy B: Buy at Close → Sell at Next Open
5. QQ-plot analysis to test normality assumptions before statistical testing
6. Statistical comparison of two trading strategies using paired t-tests
7. Multiple visualizations: profit plots, cumulative returns
8. Ollama integration to summarize statistically significant results using a local LLM
9. Interactive Streamlit dashboard for exploring strategies by stock and time range
10. No API key required, fully functional in a local Python environment 

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


## Streamlit Project 
 
## Description
This project provides a web application using Streamlit, allowing users to interactively visualize data and run Python scripts through a browser interface.

## Requirements
- Python 3
- Streamlit

## Setup
- pip install streamlit
- pip install -r requirements.txt
- streamlit run streamlit.py