import data
import threading
from serve.server import server

TICKER_SYMBOLS = ["GOOG", "AAPL", "MSFT", "CSHI",]
FREQUENCY_IN_SECONDS = 1


def start():
    # Background Workers to log prices
    print("START: Archiving prices...")
    archive_workers = []
    for s in TICKER_SYMBOLS:
        w = threading.Thread(target=data.start_archiving, args=(s, FREQUENCY_IN_SECONDS,)).start()
        archive_workers.append(w)

    # Start the webserver
    print("START: Running the webserver...")
    server.run(debug=False, port=8000, host="localhost")
