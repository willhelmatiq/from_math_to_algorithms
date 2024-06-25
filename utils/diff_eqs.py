import matplotlib.pyplot as plt
import numpy as np


def g(x: float, y: float):
    return (1 + 1.0 / x) * y


x0 = 0.5
h = 0.01
y0 = 0.5 * np.exp(0.5)

T = 5
n = int((T - x0) / h)
y = y0
x = x0

y_values = [y0]
for i in range(n):
    y = y + h * g(x0 + h*i, y)
    y_values.append(y)

x_values = np.linspace(x0, T, n+1)
y_exact = x_values * np.exp(x_values)

plt.plot(x_values, y_exact, 'g-', label ='Exact solution')
plt.plot(x_values, y_values, 'r-', label ='Euler method')
plt.legend()
plt.show()
