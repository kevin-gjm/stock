from datetime import datetime


class StockData:
    def __init__(self, date, contract, ySettle, tOpen, tHigh, tLow, tEnd, tSettle, tRaiseFall1, tRaiseFall2, tVolume,
                 tOpenInterest, tChange, tTurnover):
        self.date = datetime.strptime(date, "%Y%m%d")
        self.contract = contract
        self.ySettle = float(ySettle)
        self.tOpen = float(tOpen)
        self.tHigh = float(tHigh)
        self.tLow = float(tLow)
        self.tEnd = float(tEnd)
        self.tSettle = float(tSettle)
        self.tRaiseFall1 = float(tRaiseFall1)
        self.tRaiseFall2 = float(tRaiseFall2)
        self.tVolume = float(tVolume)
        self.tOpenInterest = float(tOpenInterest)
        self.tChange = float(tChange)
        self.tTurnover = float(tTurnover)


def decodeOneLine(date, line =[]):
    stockdata = StockData(date,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12])
    print(vars(stockdata))
    return stockdata


class UtilsStock:
    def __init__(self, date, folder):
        self.date = date
        self.filename = date + ".txt"
        self.folder = folder

    def getStockData(self, contract):
        print("Get " + contract + "from" + self.filename)
        self.readContractData(contract)

    def readContractData(self, contract):
        with open(self.folder + self.filename, encoding='utf-8') as fp:
            lines = fp.readlines()
        for line in lines:
            if '|' in line and contract in line:
                decodeOneLine(self.date,line.replace(',','').split('|'))

