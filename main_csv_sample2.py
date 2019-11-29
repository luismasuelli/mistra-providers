from datetime import datetime
from mistra.core.intervals import Interval
from mistra.providers.historical.preprocessing import load


source = load('/Users/luismasuelli/Downloads/EUR-USD/2019-10/buy-01.csv', Interval.SECOND, datetime(2019, 10, 1), 108890)


print("Loaded source:", source[:])