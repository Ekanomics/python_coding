# pip install yfinance

import yfinance as yf

symbol = input("enter the stock symbol: ").upper()

stock = yf.Ticker(symbol)

try:
    price = stock.history(period="id")["Close"].iloc[-1]

    print(f"Current price of {symbol}: ${price:.2f}")

except IndexError:
    print("Invalid stock symbol or data not available")


