import csv
import data
import time

TICKER_SYMBOL = "ATVI"
FREQUENCY_IN_SECONDS = 1


def start():
    log_prices(TICKER_SYMBOL, FREQUENCY_IN_SECONDS)


def log_prices(symbol: str, frequency: int):
    with open(f"./test/price_data/{symbol}_{str(time.time())}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "price"])
        while True:
            row = data.get_current_price(TICKER_SYMBOL)
            print(f"CURRENT: {row}")
            writer.writerow(row)
            file.flush()
            time.sleep(frequency)
