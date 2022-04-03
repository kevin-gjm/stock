import os
from datetime import datetime, timedelta

DATA_PATH = "data/"


class StockData:
    def __init__(self):
        self.tVolume = None
        self.tRaiseFall2 = None
        self.tRaiseFall1 = None
        self.tSettle = None
        self.tOpenInterest = None
        self.tChange = None
        self.tTurnover = None
        self.tEnd = None
        self.tLow = None
        self.tHigh = None
        self.tOpen = None
        self.date = None
        self.contract = None
        self.ySettle = None

    def init(self, date, contract, ySettle, tOpen, tHigh, tLow, tEnd, tSettle, tRaiseFall1, tRaiseFall2, tVolume,
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
        return self

class UtilsStock:
    def __init__(self, date, folder):
        self.date = date
        self.filename = date + ".txt"
        self.folder = folder

    def getStockData(self, contract):
        # print("Get " + contract + "from" + self.filename)
        return self.readContractData(contract)

    def readContractData(self, contract):
        path = self.folder + self.filename
        if not os.path.exists(path):
            print("File not exist: " + path)
            return
        with open(path, encoding='utf-8') as fp:
            lines = fp.readlines()
        for line in lines:
            if '|' in line and contract in line:
                return decodeOneLine(self.date, line.replace(',', '').split('|'))


def decodeOneLine(date, line=[]):
    stockdata = StockData().init(date, line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                          line[9], line[10], line[11], line[12])
    # print(vars(stockdata))
    return stockdata


def getContractData(startDate, endDate, contract):
    startTime = datetime.strptime(startDate, "%Y%m%d")
    endTime = datetime.strptime(endDate, "%Y%m%d")
    currentDate = startTime.date()
    contractData = []
    while currentDate <= endTime.date():
        tDate = currentDate.strftime("%Y%m%d")
        stockfile = UtilsStock(tDate, DATA_PATH)
        data = stockfile.getStockData(contract)
        if data is not None:
            contractData.append(data)
        currentDate = currentDate + timedelta(days=1)
    return contractData
