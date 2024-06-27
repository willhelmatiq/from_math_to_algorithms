import time

import numpy as np
from matplotlib import pyplot as plt

from SLE.generate_matrix import random_matrix


# gaussian elimination
def gaussian_elimination(A, b):
    A = A.tolist()
    b = b.tolist()
    extend_matrix(A, b)
    # forward
    for i in range(0, len(A) - 1):
        swap_rows_if_needed(A, i, i)
        for j in range(i + 1, len(A)):
            if A[j][i] == 0:
                continue
            alpha = A[j][i] / A[i][i]
            for k in range(i, len(A[0])):
                A[j][k] = A[j][k] - (A[i][k] * alpha)
    # backward
    for i in range(len(A) - 1, -1, -1):
        A[i][len(A[0]) - 1] = A[i][len(A[0]) - 1] / A[i][i]
        A[i][i] = A[i][i] / A[i][i]
        for j in range(i - 1, -1, -1):
            if A[j][i] == 0:
                continue
            alpha = A[j][i] / A[i][i]
            A[j][i] = A[j][i] - alpha * A[i][i]
            A[j][len(A[0]) - 1] = A[j][len(A[0]) - 1] - alpha * A[i][len(A[0]) - 1]

    return get_vector_from_extended_matrix(A)


def swap_rows_if_needed(A, i0, j0):
    if A[i0][j0] == 0:
        i_swap = i0
        while i_swap < len(A):
            if A[i_swap][j0] != 0:
                break
            i_swap += 1
        for j in range(0, len(A[0])):
            temp = A[i0][j]
            A[i0][j] = A[i_swap][j]
            A[i_swap][j] = temp


def extend_matrix(A, b):
    for i in range(0, len(A)):
        A[i].append(b[i])


def get_vector_from_extended_matrix(A):
    result = []
    for i in range(0, len(A)):
        result.append(A[i][len(A[0]) - 1])
    return result

matrix_size = []
distances = []
residuals = []
times = []

# experiments
for i in range(3, 101):
    A = random_matrix(-10, 10, i, False)
    x = np.arange(1, i+1)
    b = A @ x
    # print(b)
    start_time = time.time()
    x_from_gauss = gaussian_elimination(A, b)
    computing_time = time.time() - start_time

    distance = np.sqrt(np.sum((x - x_from_gauss) ** 2))
    residual = np.sqrt(np.sum((A @ x_from_gauss - b) ** 2))

    matrix_size.append(i)
    distances.append(distance)
    residuals.append(residual)
    times.append(computing_time)

    print(f"Iteration: {i}, Distance: {distance}, Residual: {residual}, Time: {computing_time}")

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(matrix_size, distances, label='Distance', color='blue')
plt.xlabel('Matrix Size')
plt.ylabel('Distance')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(matrix_size, residuals, label='Residual', color='green')
plt.xlabel('Matrix Size')
plt.ylabel('Residual')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(matrix_size, times, label='Time', color='red')
plt.xlabel('Matrix Size')
plt.ylabel('Time (s)')
plt.legend()

plt.tight_layout()
plt.show()




