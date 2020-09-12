# *args represents any number of arguments

def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total

sum_all_values(1,2,3) # 6
sum_all_values(1,2,3,4,5) # 15