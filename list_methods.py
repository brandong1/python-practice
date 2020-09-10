# index - returns the index of the specified item in the list

numbers = [5,6,7,8,9,10]

numbers.index(6) # 1
numbers.index(9) # 4

#####################

# reverse - reverse the elements of the list (in place)

numbers.reverse()
print(numbers) # [10,9,8,7,6,5]

#####################

# sort - sort the items of the list (in-place)
more_numbers = [6,4,1,2,5]
more_numbers.sort()
print(more_numbers) # [1,2,4,5,6]

#####################

# join - technicall a String method that takes an iterable argument
# concatenates a copy of the base string between each item of the iterable
# returns a new string

words = ["Coding", "Is", "Fun"]
" ".join(words) # "Coding Is Fun"