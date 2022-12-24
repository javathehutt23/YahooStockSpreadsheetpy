import numpy as np 
import pandas as pd
import yfinance as yf
import datetime as dt
from datetime import date
from openpyxl import Workbook

path = "C:/Users/harry/Documents/Python/YahooStockThing/Wilshire-5000-Stocks-New.csv"
newfile = "C:/Users/harry/Documents/Python/YahooStockThing/SortedStock.xlsx"
ticker = pd.read_csv(path)
today = date.today()
thirtydays = today + (dt.timedelta(30))
#today = today.strftime("%Y-%m-%d")
soon_df = 0
print(today + (dt.timedelta(30)))

def get_info_on_stock(company_list):
    #stock = yf.Ticker(ticker1)

    # Get overview of company
    #print(stock.info)
    y_data = yf.Tickers(company_list)
    sym = list(y_data.tickers.values())
    earnings = []
    for symbol in sym:
        
        #calendar = date.fromtimestamp(symbol.calendar)
        earnings.append(symbol.calendar)
        
        #print("nan read")
            #earnings.append(symbol.calendar)
        #print(symbol.calendar)
       
    earning_df = pd.concat(earnings)[pd.concat(earnings).index == 'Earnings Date']
    earning_df['Value'] = earning_df['Value'].fillna(value=earning_df.iloc[:,0])

    #earnings_list = earning_df['Value'].tolist()
    #print(earnings_list)

    #for i in earning_df['Value']:
        #print((i.to_pydatetime().date()) - today)
        #if (((((i.to_pydatetime().date())- today).days)) > 30 ):
            #print('ran')
            #earning_df = earning_df.set_index('Value')
            #data.head()
            #earning_df=earning_df.drop(earning_df.index[i])
            #print(data)
    
    earning_df['Value']
    earning_df.index = company_list #replace the index with symbols
    #soon_df = earning_df['Value'].where((earning_df['Value']) < pd.Timestamp(thirtydays))
    #earning_df = earning_df['Value'].where((earning_df['Value']) > pd.Timestamp(thirtydays))

    return earning_df.astype(str), #soon_df.astype(str)

#get_info_on_stock(ticker)
#a = ticker.iat[0,0]
#seperate = a.split(',', 1)[0]

seperate = ticker['Ticker'].tolist()
#print(seperate[:6])

earning_df = get_info_on_stock(seperate[:10])
#print(soon_df)
print(earning_df)

#with pd.ExcelWriter(newfile, mode='a', engine='openpyxl') as writer:
   
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    #earning_df.to_excel(writer, sheet_name="current", encoding='utf-8', index=False, engine='openpyxl')
    #soon_df.to_excel(writer, sheet_name="soon", encoding='utf-8', index=False, engine='openpyxl')