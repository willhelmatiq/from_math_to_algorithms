import math

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return 3 * x ** 3 - 2 * x + 5 * math.sin(x)


a = 0
b = 10
n = 15  # number of points to build interpolation polynomial
k = 500
m = 15  # power of interpolation polynomial/ also includes in combinations of trigonometric functions
x_vals = np.linspace(a - 1, b + 1, k)
y_vals = [f(x) for x in x_vals]

x_points = np.linspace(a, b, n)
y_points = [f(x) for x in x_points]

# approximation with polynomial
A = np.zeros((n, m + 1))


def m_row(x, m):
    row = []
    term = 1
    for i in range(m + 1):
        row.append(term)
        term *= x
    return row


for i in range(n):
    A[i] = m_row(x_points[i], m)  # Use x_points instead of x_vals

B = A.T @ A
r = A.T @ y_points
coeffs = np.linalg.solve(B, r)


# print(c)

def y_for_polynom_power_m(coefficients, x_vals):
    y_vals_poly = [0 for _ in range(len(x_vals))]
    for i in range(len(x_vals)):
        x = 1
        for j in range(len(coefficients)):
            y_vals_poly[i] += coefficients[j] * x
            x *= x_vals[i]
    return y_vals_poly


y_vals_poly = y_for_polynom_power_m(coeffs, x_vals)

# approximation with trigonometric functions
C = np.zeros((n, 2 * m + 1))


def m_row_trig(x, m):
    row = [1]  # First element is 1 (corresponding to the constant term)
    for i in range(1, m + 1):
        row.append(math.sin(i * x))
        row.append(math.cos(i * x))
    return row


for i in range(n):
    C[i] = m_row_trig(x_points[i], m)  # Use x_points instead of x_vals

B_trig = C.T @ C
r_trig = C.T @ y_points
coeffs_trig = np.linalg.solve(B_trig, r_trig)


def y_for_trig(coeffs_trig, x_vals):
    y_vals_trig = [0 for _ in range(len(x_vals))]
    for i in range(len(x_vals)):
        for j in range(len(coeffs_trig)):
            if j == 0:
                y_vals_trig[i] += coeffs_trig[j]
            else:
                if j % 2 != 0:
                    y_vals_trig[i] += coeffs_trig[j] * math.sin((j // 2 + 1) * x_vals[i])
                else:
                    y_vals_trig[i] += coeffs_trig[j] * math.cos((j // 2) * x_vals[i])
    return y_vals_trig


y_vals_trig = y_for_trig(coeffs_trig, x_vals)

# Plotting the original function and the polynomial approximation
plt.plot(x_vals, y_vals, label='Original Function')
plt.plot(x_vals, y_vals_poly, label='Polynomial Approximation')
plt.plot(x_vals, y_vals_trig, label='Trigonometric Approximation')
plt.scatter(x_points, y_points, color='red', label='Sample Points')
plt.legend()
plt.show()
