import random


# Algorithm and code independently designed by Shao Shi

def Random_integer(N):
    rand_list = [0 for i in range(N)]
    for i in range(N):
        rand_list[i] = random.randint(0, 10)

    return rand_list
