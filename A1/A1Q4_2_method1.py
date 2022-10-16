# Algorithm and code independently designed by Shao Shi
# in my algorithm, subsets was found firstly, and the average is calculated based on them
# the subset finding algorithm is O(n*2^n)


def Sum_averages(inputList):
    subsets = Find_subsets(inputList)
    averageSum = 0
    for i in range(1, len(subsets), 1):
        averageSum += sum(subsets[i]) / len(subsets[i])
    return averageSum


def Find_subsets(inputList):
    if not inputList:
        return [[]]
    else:
        # lastSetList = Find_subsets(inputList[:-1])
        # a bug in recursive python code have occurred
        return Find_subsets(inputList[:-1]) + Setlist_append_term(Find_subsets(inputList[:-1]), inputList[-1])


def Recursive_function(inputList):
    return Find_subsets(inputList[:-1]) + Setlist_append_term(Find_subsets(inputList[:-1]), inputList[-1])


def Setlist_append_term(inputSetList, term):
    if not inputSetList:
        return [[term]]
    else:
        out = inputSetList.copy()
        for i in range(len(inputSetList)):
            out[i] += [term]
        return out
