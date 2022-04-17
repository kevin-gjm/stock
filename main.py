from Utils.UtilsStock import getContractData
import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

x = np.arange(0., 5., 0.2)
# 红色破折号, 蓝色方块 ，绿色三角块
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.show()
queue = []
stockData = getContractData("20210309", "20220304", "TA203")
for s in stockData:
    print(s.date)
    print(s.tEnd)
    queue.append(s.tEnd)
    if len(queue) == 20:

        del queue[0]

