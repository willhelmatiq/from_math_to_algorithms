A = [[5, 2, 1],
     [3, 10, 3],
     [1, 2, 4]]

b = [8, 16, 7]

x0 = [8, 16, 7]

A1 = [[3, 1, 1],
     [1, 2, 1],
     [1, -1, 3]]

b1 = [5, 4, 3]

x01 = [0, 1, 2]


def jacoby_step(A, b, x0):
    extend_matrix(A, b)
    x_next = [0] * len(A)
    for i in range (0, len(A)):
        row_sum = 0
        for j in range (0, len(A)):
            if (i != j):
                row_sum += A[i][j] * x0[j]
        x_next[i] = (A[i][len(A)] - row_sum) / A[i][i]
    return x_next



def extend_matrix(A, b):
    for i in range(0, len(A)):
        A[i].append(b[i])


def jacoby_iteration_algorithm(n, A, b, x0):
    x = x0
    for i in range(0, n):
        x = jacoby_step(A, b, x)
        print(x)


jacoby_iteration_algorithm(50, A1, b1, x01)