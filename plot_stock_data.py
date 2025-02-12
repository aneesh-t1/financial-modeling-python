import os
import pandas as pd
import matplotlib.pyplot as plt


def main():

    ticker = input("Input Ticker: ").strip()
    csv_filename = f"{ticker}_stock_data.csv"


    if not os.path.exists(csv_filename):
        print(f"Error: The file {csv_filename} was not found. Make sure it's in the same directory.")
        return


    try:
        stock_data = pd.read_csv(csv_filename, skiprows=2)
        print(f"Reading data from {csv_filename}")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return




    expected_columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

    if stock_data.shape[1] >= len(expected_columns):

        stock_data = stock_data.iloc[:, :6]
        stock_data.columns = expected_columns
    else:

        print("Error: CSV file does not contain the expected columns.")
        return

    try:
        stock_data["Date"] = pd.to_datetime(stock_data["Date"])
    except Exception as e:
        print(f"Error converting Date column: {e}")
        return



    # Ploting Data

    plt.figure(figsize=(10, 5))
    plt.plot(stock_data["Date"][:100], stock_data["Close"][:100], label="Close (First 100 Days)", color="red")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.title(f"{ticker} Stock Price Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()

    if os.environ.get("DISPLAY", "") == "":
        output_filename = f"{ticker}_plot.png"
        plt.savefig(output_filename)
        print(f"Plot saved as {output_filename}")
    else:
        plt.show()

main()