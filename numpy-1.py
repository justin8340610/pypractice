import numpy as np

def table(m , n):
    arr = []
    for i in range(1, m+1):
        arr.append([1*i, 2*i, 3*i, 4*i, 5*i])
    return np.array(arr)

def test():
    arr = table(4, 5)
    print(arr)
    print(arr.ndim)
    print(arr.shape)

def table1(m, n):
    arr = [[i*j for j in range(1, n+1) for i in range(1, m+1)]]
    return np.array(arr)
test()