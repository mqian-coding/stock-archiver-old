from datetime import datetime
from flask import request
from .server import server


@server.route('/prices', methods=['GET'])
def get_prices():
    ticker = request.args.get('ticker')
    date = request.args.get('date')

    # Validate the parameters
    if not ticker or not date:
        return "Missing ticker or date query parameters", 400

    # Parse the date
    try:
        date_obj = datetime.strptime(date, '%y %m %d')
    except ValueError:
        return "Invalid date format. Please use 'yy mm dd'", 400

    # Process the ticker and date...
    return 'Ticker: %s, Date: %s' % (ticker, date_obj.strftime('%Y-%m-%d'))
