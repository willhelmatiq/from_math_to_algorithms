import numpy as np
import matplotlib.pyplot as plt
import math


def f(x: float) -> float:
    return 3 * x ** 2 - 5 * x + 2 + math.sin(3*x)*5


def interpolation_polynomial(coeffs: np.ndarray, x: float) -> float:
    res = 0
    x_cur = 1
    for i in range(len(coeffs)):
        res += x_coeff[i] * x_cur
        x_cur *= x
    return res


a = -2
b = 3

n = 20

x_vector = [a + i * (b - a) / n for i in range(n + 1)]
y_vector = [f(x) for x in x_vector]

print(x_vector)
print(y_vector)

A = np.zeros((n + 1, n + 1))
for i in range(n + 1):
    for j in range(n + 1):
        A[i, j] = x_vector[i] ** j
# print(A)

x_coeff = np.linalg.solve(A, y_vector)
print(x_coeff)

plt.plot(x_vector, y_vector, 'o')

x_plot = np.linspace(a, b, 100)
plt.plot(x_plot, [f(x) for x in x_plot])


y_plot = [interpolation_polynomial(x_coeff, x) for x in x_plot]
plt.plot(x_plot, y_plot)

plt.show()
