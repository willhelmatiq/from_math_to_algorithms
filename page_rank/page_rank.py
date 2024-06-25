import numpy as np


def build_transition_matrix(adj_list):
    n = len(adj_list)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(len(adj_list[i])):
            A[adj_list[i], i] = 1/ len(adj_list[i])
    print(A)
    return A

adj_list = [
    [1],
    [0, 2, 3],
    [3],
    [4],
    [1]
]

adj_list_1 = [
    [1],
    [0, 5],
    [5],
    [2],
    [1, 3],
    [2, 4]
]

A = build_transition_matrix(adj_list_1)

# A = np.array([[0, 1 / 3, 0, 0, 0],
#               [1, 0, 0, 0, 1],
#               [0, 1 / 3, 0, 0, 0],
#               [0, 1 / 3, 1, 0, 0],
#               [0, 0, 0, 1, 0]
#               ])
#
n = A.shape[0]

alpha = 0.85
eps = 0.0001

B = alpha * A + (1 - alpha) / n * np.ones((n, n))

print(f"B is stochastic: {np.allclose(B.sum(axis=0), np.ones(n))}")

x0 = np.array([1/n for _ in range(n)])
print(f"x0 = {x0}")

x = B @ x0
iter = 1
while not np.linalg.norm(x - x0) < eps:
    x0 = x
    x = B @ x0
    iter += 1

print(f"x = {x}; iter = {iter}")

sum = 0
for i in range(len(x0)):
    sum += x0[i]

print(sum)
