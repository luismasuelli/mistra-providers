from datetime import datetime, timedelta
from mistra.providers.historical.raw.truefx import TrueFXBackTestingProvider
from mistra.providers.historical.preprocessing import dump


refdt = datetime(2019, 10, 1)
with open('/Users/luismasuelli/Downloads/EURUSD-2019-10.csv') as f:
    reader = TrueFXBackTestingProvider(f, refdt, '1.0889', '1.08891', price_precision=4)
    buy, sale = reader()
    print("Buy sample:", buy[refdt:refdt+timedelta(seconds=5)])
    print("Sale sample:", sale[refdt:refdt+timedelta(seconds=5)])


dump(buy, '/Users/luismasuelli/Downloads/EUR-USD/%Y-%m/buy-%d.csv')
dump(sale, '/Users/luismasuelli/Downloads/EUR-USD/%Y-%m/sale-%d.csv')
