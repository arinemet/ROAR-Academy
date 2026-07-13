import numpy as np

one = np.array([[6., -9., 1.],
                [4., 24., 8.]])

print(2 * one)

two = np.array([[1., 0.],
                [0., 1.]])

print(two @ one)

one = np.array([[4., 3.],
                [3., 2.]])
two = np.array([[-2., 3.],
                [3., -4.]])

print(one @ two)