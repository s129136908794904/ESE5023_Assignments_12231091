from matplotlib import pyplot as plt
from A1Q4_1 import Random_integer
import A1Q4_2_method1
import A1Q4_2_method2
# Algorithm and code independently designed by Shao Shi
# in method1, calculating loop = 100 have an intensive running time requirement, but it is correct
# the reason is that, in my algorithm, subsets was found firstly, and the average is calculated based on them
# the subset finding algorithm is O(n*2^n)
# method2 used some tricky mathematical simplification to avoid the problem in method1

loop = 100
xList = list(range(1, loop + 1, 1))
yList = list(range(1, loop + 1, 1))

'''
# method1: find subsets and get sum
for N in range(1, loop + 1, 1):
    randList = Random_integer(N)
    Total_sum_averages = A1Q4_2.Sum_averages(randList)
    yList[N-1] = Total_sum_averages
plt.plot(xList, yList)
plt.show()
'''
# method2: find subsets and get sum
for N in range(1, loop + 1, 1):
    randList = Random_integer(N)
    Total_sum_averages = A1Q4_2_method2.Sum_averages(randList)
    yList[N-1] = Total_sum_averages
plt.plot(xList, yList)
plt.show()


