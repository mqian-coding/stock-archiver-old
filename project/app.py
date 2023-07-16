import data

TICKER_SYMBOL = "MSFT"
FREQUENCY = 1


def start():
    start_worker()


def start_worker():
    while True:
        data.get_current_price(TICKER_SYMBOL, FREQUENCY)
