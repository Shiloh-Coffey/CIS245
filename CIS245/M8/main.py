# Stock Ticker Search
# Author: R. Dillard Coffey

# Dictionary of stocks with ticker symbols and current prices
stocks = {
    "AAPL": 150.25,
    "GOOGL": 2750.50,
    "AMZN": 3400.75,
    "MSFT": 290.60,
    "TSLA": 750.80,
    "NFLX": 550.40,
    "FB": 330.10,
    "NVDA": 680.90,
    "AMD": 110.25,
    "INTC": 55.75
}

# Ask user to enter a ticker symbol
ticker_symbol = input("Enter a ticker symbol: ")

# Search the dictionary for the ticker symbol
if ticker_symbol in stocks:
    print(
        f"Ticker Symbol: {ticker_symbol}\nStock Price: ${stocks[ticker_symbol]:.2f}"
    )
else:
    print("Ticker symbol not found.")
