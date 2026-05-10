import numpy as np


def coords(B, v):
    return np.linalg.solve(B, v)


B = np.array([[1.0, 1.0],
              [1.0, -1.0]])
v = np.array([3.0, 1.0])

c = coords(B, v)
print("coordinates:", c)
print("reconstruction:", B @ c)
