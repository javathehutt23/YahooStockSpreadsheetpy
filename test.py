from datetime import datetime
from yahoo_earnings_calendar import YahooEarningsCalendar

yec = YahooEarningsCalendar()
# Returns the next earnings date of BOX in Unix timestamp
print(datetime.utcfromtimestamp(yec.get_next_earnings_date('AAPL')))
print((yec.get_earnings_of('box')))
# 1508716800
