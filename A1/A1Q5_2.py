import numpy as np


# Algorithm and code independently designed by Shao Shi
# This algorithm is an implementation of recursion with a memo, and is O(n)
# @parameters
# randMatrix is the random matrix created in A1Q5_1
# x is the row number of the term in the randMatrix
# y is the column number of the term in the randMatrix
# matrix_compute is the matrix for path computation
# memo is the matrix storing recursive results

def Count_path_core(x, y, matrix_compute, memo):
    if memo[x, y] != -1:
        return memo[x, y]
    else:
        if x == 0 or y == 0:
            memo[x, y] = 0
            return 0
        elif x == 1 and y == 1:
            memo[x, y] = 1
            return 1
        else:
            memo[x, y] = matrix_compute[x, y] * (
                        Count_path_core(x - 1, y, matrix_compute, memo) + Count_path_core(x, y - 1, matrix_compute,
                                                                                          memo))
            return memo[x, y]


def Count_path(randMatrix):
    randMatrix_shape = randMatrix.shape
    memo = np.zeros((randMatrix_shape[0] + 1, randMatrix_shape[1] + 1), dtype=np.int64) - 1
    matrix_compute = np.zeros((randMatrix_shape[0] + 1, randMatrix_shape[1] + 1), dtype=np.int64)
    matrix_compute[1:, 1:] = randMatrix
    return Count_path_core(randMatrix_shape[0], randMatrix_shape[1], matrix_compute, memo)
