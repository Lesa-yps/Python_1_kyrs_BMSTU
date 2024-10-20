import matplotlib.pyplot as plt

plt.subplot(1,2,1)
x = [1, 2, 3, 4, 5]
x1 = ['one', 'two', 'tree', 'four', 'five'] # заголовки
colors1 = ['red', 'blue', 'green', 'violet', 'yellow'] 
plt.pie(x, labels = x1, shadow = True, colors = colors1) # тень

plt.subplot(1,2,2)
y = [341, 5, 145, 45, 210]
explode1  = [0, 0, 0.1, 0.3, 0] # выдвижение
plt.pie(y, explode = explode1, startangle = 100, autopct = '%1.2f%%') # цифры написать в процентах
# startangle - поворот на градусы [0, 360]
plt.show()
