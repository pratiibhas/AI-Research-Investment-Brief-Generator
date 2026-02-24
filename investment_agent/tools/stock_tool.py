from google.adk.tools import Tool
import yfinance as yf
import numpy as np


def fetch_stock_data(symbol: str) -> dict:
    """
    Fetch stock data and compute basic metrics.

    Args:
        symbol (str): Stock ticker symbol (e.g., HDFCBANK.NS)

    Returns:
        dict: Financial metrics.
    """
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1mo")

    if hist.empty:
        return {"error": "No data found for symbol."}

    current_price = hist["Close"].iloc[-1]
    start_price = hist["Close"].iloc[0]

    returns = (current_price - start_price) / start_price
    volatility = np.std(hist["Close"].pct_change().dropna())

    return {
        "current_price": round(float(current_price), 2),
        "30_day_return_percent": round(float(returns * 100), 2),
        "volatility": round(float(volatility), 4),
    }


fetch_stock_data = Tool.from_function(fetch_stock_data)