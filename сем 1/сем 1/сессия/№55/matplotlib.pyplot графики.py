import matplotlib.pyplot as plt, math as m

plt.figure(1)

x = [i for i in range(0, 400, 5)]

y1 = [m.sin(m.radians(i)) for i in x]
y2 = [m.cos(m.radians(i)) for i in x]
plt.plot(x, y1, '-.', color = 'red', linewidth = 3, marker = 'v')
plt.plot(x, y2, '*', color = 'blue', linewidth = 5)
plt.title('$График$ №1')
plt.xlabel('ось Х')
plt.ylabel('ось У')
plt.grid(True)
plt.axis([-10, 410, -1.2, 1.2])
plt.legend(['$sinx$', '$cosx$'], loc = 'upper center')



plt.figure(2)

x = [i for i in range(-200, 200, 4)]

plt.subplot(2,2,1)
plt.title('$График$ №1')
plt.xlabel('ось Х')
plt.ylabel('ось У')
plt.grid(False)
y3 = [i ** 2 for i in x]
plt.axis([x[0] -10, x[-1] + 10, min(y3) - 500, max(y3) + 500])
plt.plot(x, y3, '.', color = 'green', linewidth = 10)
plt.legend(['$x$ ** 2'], loc = 'upper center')

plt.subplot(2,2,2)
plt.title('$График$ №2')
plt.xlabel('ось Х')
plt.ylabel('ось У')
plt.grid(True)
y4 = [i * 2 for i in x]
plt.axis([x[0] -10, x[-1] + 10, y4[0] - 10, y4[-1] + 10])
plt.plot(x, y4, '--', color = 'yellow', linewidth = 0.5, marker = 'o')
plt.legend(['$x$ * 2'], loc = 'upper left')

plt.subplot(2,1,2)
plt.title('$График$ №3')
plt.xlabel('ось Х')
plt.ylabel('ось У')
plt.grid(True)
x.extend(range(200, 300, 4))
y5 = [m.cos(m.radians(i)) for i in x]
plt.yticks(list(range(round(min(y5)), round(max(y5)) + 1)), ['Минус Адын', 'Нуль', 'Адын'])
plt.axis([min(x) - 10, max(x) + 10, min(y5) - 0.1, max(y5) + 1])
plt.plot(x, y5, '+', color = 'violet', linewidth = 2)
plt.legend(['$cosx$'], loc = 'upper center')

plt.show()
