nested_list = [[1,2,3], [4,5,6], [7,8,9]] # like an "array of arrays" in Ruby

nested_list[0][1] # 2
nested_list[1][-1] # 6

for l in nested_list:
    for val in l:
        print(val)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

####################

answer = [[i for i in range(0,3)] for num in range(0,3)]

####################

# To generate the following using a nested list comprehension:

[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ]

answer = [[i for i in range(0,10)] for num in range(0,10)]