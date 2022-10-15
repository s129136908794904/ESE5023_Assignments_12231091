import numpy as np


# Algorithm and code independently designed by Shao Shi
# This algorithm is an implementation of recursion with a memo
# @parameters
# x is the target number of sum
# diceCount is the number of dices
# faceCount is the number of faces of each dice, each face have an integer value from 1 to faceCount

def Find_number_of_ways(x, diceCount, faceCount):
    core_memo = np.zeros((x + 1, diceCount + 1), dtype=np.int64) - 1  # create a memo to store recursive results
    return core(x, diceCount, faceCount, core_memo)


def core(x, diceCount, faceCount, core_memo):
    pathCount = 0
    if diceCount < 0 or x < 0:
        pathCount = 0
    elif diceCount == 0 and x == 0:
        pathCount = 1
    else:
        if core_memo[x][diceCount] != -1:  # search for result in memo
            return core_memo[x][diceCount]
        else:
            for i in range(1, faceCount + 1):
                pathCount += core(x - i, diceCount - 1, faceCount, core_memo)
        core_memo[x][diceCount] = pathCount
    return pathCount
