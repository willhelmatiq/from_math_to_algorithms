import numpy as np
import matplotlib.pyplot as plt

M = [[1, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 1],
      [0, 0, 0, 0, 1, 2, 4, 8],
      [0, 1, 2, 3, 0, -1, -2, -3],
      [0, 0, 2, 6, 0, 0, -2, -6],
      [0, 0, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 12]]

b = [0, 1, 1, 0, 0, 0, 0, 0]

spline_coeff = np.linalg.solve(M, b)
print(spline_coeff)

knots = [0, 1, 2]

def spline(coeffs: list, knots: list, x: float) -> float:
    i = 1
    if x < knots[0]:
        i = 0
    elif knots[-1] <= x:
        i = len(knots) - 1
    else:
        while knots[i] < x:
            i += 1
    return coeffs[(i-1) * 4] + coeffs[(i-1) * 4 + 1] * x + coeffs[(i-1) * 4 + 2] * (x**2) + coeffs[(i-1)*4+3]*(x**3)

print(spline(list(spline_coeff), knots, 1))

x_plot = np.linspace(0, 2, 100)
y_plot = [spline(list(spline_coeff), knots, x) for x in x_plot]
plt.plot(x_plot, y_plot)
plt.show()
