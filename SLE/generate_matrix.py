import numpy as np


def random_matrix(a, b, n, is_diagonally_dominant):
    r_matrix = a + (b - a) * np.random.rand(n, n)
    if is_diagonally_dominant:
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                if i != j:
                    temp_sum += abs(r_matrix[i,j])
            r_matrix[i,i] = np.random.choice([1, -1]) * (abs(r_matrix[i,i]) + abs(temp_sum))
    return r_matrix


def hilbert_matrix(n):
    j_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            j_matrix[i, j] = 1 / (i + j + 1)
    return j_matrix
