import numpy as np


# Algorithm and code independently designed by Shao Shi

def Matrix_generator(N, M):
    matrix_out = np.random.randint(2, size=(N, M))
    matrix_out[[0, -1], [0, -1]] = 1
    return matrix_out
