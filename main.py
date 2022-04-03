from Utils.UtilsStock import getContractData
from Utils.UtilsStock import StockData

stockData = getContractData("20210309", "20220304", "TA205")
print(stockData)
for data in stockData:
    print(data)
