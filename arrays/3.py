import numpy as np
a = np.array([1, 6, 3])
print(a)


def multiply(n):
    return n * 3


b = np.array(list(map(multiply, a)))
print(b)
