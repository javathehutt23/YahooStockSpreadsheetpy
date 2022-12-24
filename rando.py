import yahoo_fin.stock_info as si
import datetime as dt
from datetime import date

a=[];b=[]
ticker = si.tickers_nifty50()
for tick in ticker:
        
        a.append(tick)
        try:
            earning_date = dt.datetime.strftime(si.get_next_earnings_date(tick), "%d/%m/%Y")
            b.append(earning_date)
        except:
            b.append("nan")
        

print(len(a))
print(len(b))