import matplotlib.pyplot as plt

plt.figure(1)

x = [4, 7, 6, 6, 5, 6, 5, 3, 2,2, 3, 2, 1, 4, 4, 3, 5, 4, 4, 4, 5, 5, 3, 3, 4]
y = [1, 3, 4, 5, 5, 4, 5, 5, 5, 4, 5, 4, 3, 1, 2, 2.3, 2.3, 2, 3, 4, 4, 3, 3, 4, 4]

plt.title('$График$ №X')
plt.xlabel('ось Х')
plt.ylabel('ось Y')
plt.grid(True)
#plt.xticks(x, ['a', 'b', 'c', 'd', 'f'])
plt.axis([min(x) - 0.1, max(x) + 0.1, min(y) - 0.1, max(y) + 0.1])

plt.plot(x, y, '--', color = 'blue', linewidth = 1, marker = 'v', label = 'фига')

x1 = [3.5, 4.5]
y1 = [3.5, 3.5]

plt.plot(x1, y1, '*', color = 'green', linewidth = 10, label = 'глазки')

plt.legend(loc = 'upper right')

plt.show()
