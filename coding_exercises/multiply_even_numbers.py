# This function accepts a list of numbers and returns the product of all even numbers in the list

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(list):
    total = 1
    for val in list:
        if val % 2 == 0:
            total = total * val
    return total
