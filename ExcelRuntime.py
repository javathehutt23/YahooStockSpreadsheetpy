import yahoo_fin.stock_info as si
import datetime as dt
from datetime import date
import pandas as pd

path = "C:/Users/harry/Documents/Python/YahooStockThing/Wilshire-5000-Stocks-New.csv"
newfile = "C:/Users/harry/Documents/Python/YahooStockThing/SortedStock.xlsx"
tickers = si.tickers_sp500()
today = date.today()
sixtydays = today + (dt.timedelta(60))
thirtydays = today + (dt.timedelta(30))
#today = today.strftime("%Y-%m-%d")
soon_df = 0
print(today + (dt.timedelta(30)))


# alternative 1

#ticker_earnings = si.get_next_earnings_date('aapl')
#print(ticker_earnings)

def refreshStockInfo():
    earning_df, soon_df = get_info_on_stock(tickers)
    with pd.ExcelWriter(newfile,mode='a', if_sheet_exists="replace") as writer:  
        earning_df.to_excel(writer, sheet_name='All Dates')
        soon_df.to_excel(writer, sheet_name="Future")

def getCurrentChosen():
    excel_data_df = pd.read_excel(newfile, sheet_name='Chosen').values.tolist()
    print(excel_data_df)
    for  tickDate in excel_data_df:
            print(tickDate)
            #earning_date = dt.datetime.]strftime(tickDate, "%d/%m/%Y")
            #print(earning_date)[
            if dt.datetime.strptime(tickDate[2], "%d/%m/%Y").date() > thirtydays:
                print(tickDate[1] + " is within 30 days of the earnings release!")



def addTickerToChosen(NewTicker):
    excel_data_df = pd.read_excel(newfile, sheet_name='Chosen')
    all_data_df = pd.read_excel(newfile, sheet_name='All Dates')
    future_data_df = pd.read_excel(newfile, sheet_name="Future")
    all = all_data_df.values.tolist()
    added = excel_data_df.values.tolist()
    future = future_data_df.values.tolist()
    allTicker = all_data_df[all_data_df['Ticker']==NewTicker].values.tolist()
    
    while True:
        print('ran')
        if(any(NewTicker in sl for sl in all)):
            if (NewTicker not in added):
                if(any(NewTicker not in sl for sl in future)):
                    a = input("This ticker is not in future Ticker dates do you want to continue or pick another? keep/change ")
                    if(a=="change"):
                        NewTicker = input("enter new ticket: ").upper().strip()
                        continue
                    if(a=="keep"):
                        added.append(allTicker[0])
                        for i in added:
                            i.pop(0)
                        df_added = pd.DataFrame(added, columns=["Ticker","Date"])
                        with pd.ExcelWriter(newfile,mode='a', if_sheet_exists="overlay") as writer:
                            df_added.to_excel(writer, sheet_name='Chosen')
                        print("Ticker has been successfully added.")
                        return False    
                else:
                    added.append(allTicker[0])
                    for i in added:
                        i.pop(0)
                    df_added = pd.DataFrame(added, columns=["Ticker","Date", "Price"])
                    with pd.ExcelWriter(newfile,mode='a', if_sheet_exists="overlay") as writer:
                        df_added.to_excel(writer, sheet_name='Chosen')
                    print("Ticker has been successfully added.")
                    return False            
            else:
                NewTicker = input("That ticker is already on the list, please enter a new one").upper().strip()
                continue
        else:
            NewTicker = input("That does no exist please enter a valid one: ").upper().strip()
            continue        
        

def deleteTickerFromChosen(Removed):
    excel_data_df = pd.read_excel(newfile, sheet_name='Chosen')
    changes = excel_data_df.values.tolist()
    while True:
        if(any(Removed in sl for sl in changes)):
            for i in changes:
                print(i)
                if (i[1]==Removed):
                    changes.remove(i)
                    break
            for i in changes:
                i.pop(0)
            changes_df = pd.DataFrame(changes, columns=["Ticker","Date"])
            with pd.ExcelWriter(newfile,mode='a', if_sheet_exists="replace") as writer:
                changes_df.to_excel(writer, sheet_name='Chosen')
            print("Ticker has been removed")
            return False
        else:
            Removed = input("That Ticker is not present in that list!, please enter a new one: ")
            continue


def get_info_on_stock():
    #y_data = yf.Tickers(company_list)
    
    earnings = []
    a=[];b=[];c=[];d=[];e=[]
    soon=[]
    for tick in tickers:
        
        a.append(tick)
        try:
            earning_date = dt.datetime.strftime(si.get_next_earnings_date(tick), "%d/%m/%Y")
            b.append(earning_date)
        #if si.get_next_earnings_date(tick) > dt.datetime.strptime(thirtydays, "%d/%m/%Y"):
            if dt.datetime.strptime(earning_date, "%d/%m/%Y").date() > sixtydays:
                price = si.get_live_price(tick)
                #print(price)
                c.append(tick)
                d.append(earning_date) 
                e.append(price)
        except:
            b.append("nan")       
    data_all ={ "Ticker": a, "Date": b }    
    data_soon={"Ticker":c, "Date": d, "Price":e}
    earnings = pd.DataFrame(data_all)
    soon = pd.DataFrame(data_soon)
    return earnings, soon
#get_info_on_stock(ticker)
#a = ticker.iat[0,0]
#seperate = a.split(',', 1)[0]

#seperate = tickers['Ticker'].tolist()
#print(seperate[:6])

#earning_df, soon_df = get_info_on_stock()
#print(earning_df)
#print(soon_df)
#soon_df = pd.Timestamp(earning_df['Date'].where((earning_df['Date'])) < pd.Timestamp(thirtydays))

#print(soon_df)
#print(si.get_earnings('aapl'))

