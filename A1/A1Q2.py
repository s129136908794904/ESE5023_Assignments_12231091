from math import ceil


# Algorithm and code independently designed by Shao Shi
# This algorithm is an implementation of recursion with a memo
# @parameters
# x is the index of the desired term

def my_list(x):
    memo = list(range(-1, -x - 1, -1))
    return core(x, memo)


def core(x, memo):
    if memo[x - 1] >= 0:
        return memo[x - 1]
    else:
        if x == 1:
            memo[0] = 1
            return 1
        else:
            memo[x - 1] = core(ceil(x / 3), memo) + 2 * x
            return memo[x - 1]
