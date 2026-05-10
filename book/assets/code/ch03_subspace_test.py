import numpy as np


def in_plane(v, tol=1e-10):
    return abs(v[0] + v[1] + v[2]) < tol


def sample_plane():
    x = np.random.randn()
    y = np.random.randn()
    return np.array([x, y, -x - y])


ok = True
for _ in range(200):
    u = sample_plane()
    v = sample_plane()
    a, b = np.random.randn(), np.random.randn()
    ok = ok and in_plane(a * u + b * v)

print("closure test passed:", ok)
