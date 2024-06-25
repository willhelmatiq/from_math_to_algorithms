A = [[1, 1, 1],
     [1, 1, 2],
     [3, -1, 1]]
b = [3, 4, 3]

A1 = [[1, 2, 3],
      [3, 5, 7],
      [1, 3, 4]]

b1 = [3, 0, 1]

A2 = [[2, -1, 3, -5],
      [1, -1, -5, 0],
      [3, -2, -2, -5],
      [7, -5, -9, -10]]

b2 = [1, 2, 3, 8]

A3 = [[1, 0, 0, 0, 0, 0, 0, 0],
      [1, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 1],
      [0, 0, 0, 0, 1, 2, 4, 8],
      [0, 1, 2, 3, 0, -1, -2, -3],
      [0, 0, 2, 6, 0, 0, -2, -6],
      [0, 0, 2, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 2, 12]]

b3 = [0, 1, 1, 0, 0, 0, 0, 0]


def gaussian_elimination(A, b):
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

    print(get_vector_from_extended_matrix(A))


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


gaussian_elimination(A, b)
