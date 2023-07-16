import time
import yfinance as yf


def get_current_price(symbol: str, seconds: int):
    t = yf.Ticker(symbol)
    print(t.fast_info.get("lastPrice"))
    time.sleep(seconds)
