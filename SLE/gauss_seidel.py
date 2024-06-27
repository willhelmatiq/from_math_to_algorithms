import time

import numpy as np
from matplotlib import pyplot as plt

from SLE.generate_matrix import random_matrix, hilbert_matrix


def gauss_seidel_step(A, b, x0):
    A = A.tolist()
    b = b.tolist()
    extend_matrix(A, b)
    x_next = [0] * len(A)
    for i in range(0, len(A)):
        row_sum = 0
        for j in range(0, len(A)):
            if (i != j):
                row_sum += A[i][j] * x0[j]
        x_next[i] = (A[i][len(A)] - row_sum) / A[i][i]
        x0[i] = x_next[i]
    return x_next

def extend_matrix(A, b):
    for i in range(0, len(A)):
        A[i].append(b[i])

def gauss_seidel_algorithm(n, A, b, x0):
    x = x0
    for i in range(0, n):
        x = gauss_seidel_step(A, b, x)

matrix_size = []
distances = []
residuals = []
times = []

# experiments
MAX_ITERACTION = 500

#random matrices with diagonal dominance
for i in range(3, 101):
    A = random_matrix(-10, 10, i, True)
    x = np.arange(1, i + 1)
    b = A @ x

    start_time = time.time()
    x_0 = 2 * b
    for j in range(MAX_ITERACTION):
        x_0 = gauss_seidel_step(A, b, x_0)
    computing_time = time.time() - start_time

    distance = np.sqrt(np.sum((x - x_0) ** 2))
    residual = np.sqrt(np.sum((A @ x_0 - b) ** 2))

    matrix_size.append(i)
    distances.append(distance)
    residuals.append(residual)
    times.append(computing_time)

    print(f"Iteration: {i}, Distance: {distance}, Residual: {residual}, Time: {computing_time}")

matrix_size_hilbert = []
distances_hilbert = []
residuals_hilbert = []
times_hilbert = []

#Hilbert matrices
for i in range(3, 101):
    A = hilbert_matrix(i)
    x = np.arange(1, i + 1)
    b = A @ x

    start_time = time.time()
    x_0 = 2 * b
    for j in range(MAX_ITERACTION):
        x_0 = gauss_seidel_step(A, b, x_0)
    computing_time = time.time() - start_time

    distance = np.sqrt(np.sum((x - x_0) ** 2))
    residual = np.sqrt(np.sum((A @ x_0 - b) ** 2))

    matrix_size_hilbert.append(i)
    distances_hilbert.append(distance)
    residuals_hilbert.append(residual)
    times_hilbert.append(computing_time)

    print(f"Iteration: {i}, Distance: {distance}, Residual: {residual}, Time: {computing_time}")

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(matrix_size, distances, label='Distance', color='blue')
plt.plot(matrix_size, distances_hilbert, label='Distance Hilbert matrix', color='green')
plt.xlabel('Matrix Size')
plt.ylabel('Distance')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(matrix_size, residuals, label='Residual', color='blue')
plt.plot(matrix_size, residuals_hilbert, label='Residual Distance Hilbert matrix', color='green')
plt.xlabel('Matrix Size')
plt.ylabel('Residual')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(matrix_size, times, label='Time', color='blue')
plt.plot(matrix_size, times_hilbert, label='Time Distance Hilbert matrix', color='green')
plt.xlabel('Matrix Size')
plt.ylabel('Time (s)')
plt.legend()

plt.tight_layout()
plt.show()
