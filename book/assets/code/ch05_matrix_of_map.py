import numpy as np


def matrix_of_T(T, n):
    cols = []
    for j in range(n):
        e = np.zeros(n)
        e[j] = 1.0
        cols.append(T(e))
    return np.column_stack(cols)


def reflect_across_y_equals_x(v):
    return np.array([v[1], v[0]])


A = matrix_of_T(reflect_across_y_equals_x, 2)
print(A)
