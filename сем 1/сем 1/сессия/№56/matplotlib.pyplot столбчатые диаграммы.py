import matplotlib.pyplot as plt
from random import randint as ran

x = list(range(10))
y = [ran(-20, 20) for i in range(10)]

plt.bar(x, y)

plt.show()
