import matplotlib.pyplot as plt
from random import randint as ran

y = [ran(0, 12) for _ in range(100)]
print(y)

plt.hist(y, width = 1)

plt.show()
