from A1Q5_1 import Matrix_generator
from A1Q5_2 import Count_path

# Algorithm and code independently designed by Shao Shi

N = 10
M = 8
loop = 1000
path_count = 0

for i in range(loop):
    path_count += Count_path(Matrix_generator(N, M))
print(path_count/loop)

