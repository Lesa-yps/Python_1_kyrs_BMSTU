import matplotlib.pyplot as plt
#from numpy import random

#y = [random.normal(0, 25, 100) for _ in range(50)]
y = [10, 11, 12, 13, 15, 17, 20, 23, 12, 22]

plt.hist(y, bins = 15, width = 1)
# bins на сколько разделить
plt.show()
