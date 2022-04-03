from Utils.UtilsStock import getContractData

stockData = getContractData("20210309", "20220304", "TA203")
for s in stockData:
    print(s.date)
