some_list[start:end:step] # start is inclusive, end is exclusive
# step is the interval to count. example, step 2 counts every other number

first_list = [1,2,3,4]

first_list[1:] # [2,3,4]

first_list[3:] # [4]

first_list[:2] # [1,2]

first_list[:4] # [1,2,3,4]

first_list[1:3] # [2,3]

first_list[2][::-1] # TypeError: 'int' object is not subscriptable

second_list = ['one','two','three']
second_list[1][::-1] # 'owt'