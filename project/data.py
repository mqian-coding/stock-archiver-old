import csv
from datetime import datetime as dt
# import queue
import time
import yfinance as yf


def get_current_price(symbol: str):
    # TODO: Error handling + Context Deadline
    t = yf.Ticker(symbol)
    if t and t.fast_info:
        return t.fast_info.get("lastPrice", None)
    return None


def start_archiving(symbol: str, frequency: int):
    while True:
        today = dt.now().date()
        with open(f"./test/price_data/{symbol}_{today.year}_{today.month}_{today.day}.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "price"])
            while dt.now().date() == today:
                ts = time.time()
                row = [ts, get_current_price(symbol)]
                writer.writerow(row)
                file.flush()
                time.sleep(frequency)


# def start_backtest(q):
#     return
