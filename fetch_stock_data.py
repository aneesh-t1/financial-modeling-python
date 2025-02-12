import yfinance as yf
import pandas as pd

# This will get data for a stock (can be historical)
ticker = input("Input Ticker: ")
stock_data = yf.download(ticker, start = "2023-01-01", end = "2024-01-01", timeout = 60)

stock_data.to_csv(f"{ticker}_stock_data.csv")

print(f"Downloaded {ticker} stock data and saved it as {ticker}_stock_data.csv")