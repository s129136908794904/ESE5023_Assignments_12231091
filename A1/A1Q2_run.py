from A1Q2 import my_list

# Algorithm and code independently designed by Shao Shi

N = 100
listN = list(range(-1, -N-1, -1))
# print(listN)
for i in range(0, N, 1):
    listN[i] = my_list(i+1)

print(listN)
