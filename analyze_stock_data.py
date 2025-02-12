import pandas as pd

ticker = input("Input Ticker: ")
stock_data = pd.read_csv(f"{ticker}_stock_data.csv", skiprows = 2) # Removing extra labels which is messing up format

stock_data.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

stock_data["Date"] = pd.to_datetime(stock_data["Date"])

# print(stock_data.head())

stock_data["Daily Return"] = stock_data["Close"].pct_change() # calculates the daily return as a percentage, new column created

stock_data["Daily Return"] = stock_data["Daily Return"].apply(lambda x: f"{x:.3%}" if pd.notnull(x) else "N/A")

print(stock_data.head())