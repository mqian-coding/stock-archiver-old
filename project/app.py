import data
import threading


TICKER_SYMBOLS = ["GOOG", "AAPL", "MSFT"]
FREQUENCY_IN_SECONDS = 1


def start():
    # Background Workers to log prices
    archive_workers = []
    for s in TICKER_SYMBOLS:
        w = threading.Thread(target=data.start_archiving, args=(s, FREQUENCY_IN_SECONDS,)).start()
        archive_workers.append(w)






