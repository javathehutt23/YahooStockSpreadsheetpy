import ExcelRuntime


def interaction():
    while True:
        first = input("update stock dates, get current tickers, change selected tickers or remove Tickers? ").lower().strip()
        if first=="update" or first== "u":
            ExcelRuntime.refreshStockInfo()
            continue
        if first=="change" or first=="c":
            second = input("enter ticker (e.g. aapl) ")
            second=second.upper().strip()
            ExcelRuntime.addTickerToChosen(second.upper().strip())
            continue
        if first == "get" or first=="g":
            ExcelRuntime.getCurrentChosen()
            continue
        if first == "remove" or first=="r":
            second = input("Please enter the ticker to be removed ")
            ExcelRuntime.deleteTickerFromChosen(second.upper().strip())
            continue
        else:
            print("Invalid input, Try again")
            continue

interaction()