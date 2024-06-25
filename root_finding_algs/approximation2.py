import numpy as np
import matplotlib.pyplot as plt
import math


def f(x: float) -> float:
    # return 3 * x ** 2 - 5 * x + 2
    return 3 * x - 1


a = -2
b = 3
n = 5
m = 2

x_vector = [a + i * (b - a) / n for i in range(n + 1)]
y_vector = [f(x) + 5 * (np.random.random() - 0.5) for x in x_vector]

print(x_vector)
print(y_vector)

# A = np.zeros((n + 1, m + 1))
# for i in range(n + 1):
#     for j in range(m + 1):
#         A[i][j] = x_vector[i] ** j
# print(A)

A = np.zeros((n + 1, m + 1))
for i in range(n + 1):
    A[i][0] = math.sin(x_vector[i])
    A[i][1] = math.cos(x_vector[i])
    A[i][2] = math.sin(2 * x_vector[i])
    A[i][3] = math.cos(2 * x_vector[i])

print(A)

x_coeff = np.linalg.solve(A.T @ A, A.T @ y_vector)
print(x_coeff)

plt.plot(x_vector, y_vector, 'o')

x_plot = np.linspace(a - 0.5, b + 0.5, 100)
plt.plot(x_plot, [f(x) for x in x_plot])


# def approximation_with_poly(coeffs: np.ndarray, x: float) -> float:
#     return coeffs[0] * math.sin(x) + coeffs[1] * math.cos(x) + coeffs[]


plt.show()
