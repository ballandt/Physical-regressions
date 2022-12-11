import numpy as np

points = [
]


def f(xi):
    return np.array([ele[1] - xi[0] * np.e ** (xi[1] * ele[0]) - xi[2] for ele in points])


def Df(xi):
    return np.array([[-np.e**(xi[1] * ele[0]), -xi[0] * ele[0] * np.e ** (xi[1] * ele[0]), -1] for ele in points])


x = np.array([-1, -1, 1])

for i in range(50):
    Dfi = Df(x)
    fi = f(x)
    delta = np.linalg.solve(Dfi.T @ Dfi, -Dfi.T @ fi)
    t = 1
    while np.linalg.norm(f(x + t*delta))**2 > np.linalg.norm(f(x))**2:
        t /= 2
    x = x + t*delta

print(x)