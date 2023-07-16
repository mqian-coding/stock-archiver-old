import time
import yfinance as yf


def get_current_price(symbol: str):
    t = yf.Ticker(symbol)
    return [str(time.time()), t.fast_info.get("lastPrice")]
