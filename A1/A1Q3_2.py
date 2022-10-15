import A1Q3_1 as dice

# Algorithm and code independently designed by Shao Shi

Number_of_ways = list(range(10, 61, 1))
for x in range(10, 61, 1):
    Number_of_ways[x-10] = dice.Find_number_of_ways(x, 10, 6)

print(Number_of_ways)



