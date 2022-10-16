from scipy.special import comb


# Algorithm and code independently designed by Shao Shi

def Combination(n, m):
    # a very slow implementation of combination computation
    # not used in this question
    # choose m element in a set of n numbers
    if m == n:
        return 1
    elif m == 1:
        return n
    else:
        return Combination(n - 1, m - 1) + Combination(n - 1, m)


def Sum_averages(inputList):
    averageSum = 0
    n = len(inputList)
    listSum_over_n = sum(inputList) / n
    for i in range(n):
        # averageSum = Combination(n, i + 1) * listSum_over_n
        averageSum += comb(n, i + 1) * listSum_over_n
    return averageSum
