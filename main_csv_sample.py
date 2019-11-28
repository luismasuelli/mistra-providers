from datetime import datetime, timedelta

from mistra.core.pricing import Candle

from mistra.providers.historical.filesystem import CSVBackTestingProvider


refdt = datetime(2019, 10, 1)
with open('/Users/luismasuelli/Downloads/EURUSD-2019-10.csv') as f:
    reader = CSVBackTestingProvider(f, refdt, Candle.constant(100001), Candle.constant(100002), price_precision=4)
    buy, sale = reader()
    print("Buy sample:", buy[refdt:refdt+timedelta(seconds=5)])
    print("Sale sample:", sale[refdt:refdt+timedelta(seconds=5)])
