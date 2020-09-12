# We can use * as an argument to a function to "unpack" values

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num

    print(total)

nums = (1,2,3,4,5,6)
sum_all_values(*nums)