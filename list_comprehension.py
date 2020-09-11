nums = [1,2,3]
[x*10 for x in nums] # [10,20,30]

######################

numbers = [1,2,3,4,5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) # [2,4,6,8,10]

######################

name = "colt"

[char.upper() for char in name] # ['C','O','L','T']

######################

numbers = [1,2,3,4,5]

# Convert the integers into strings
string_list = [str(num) for num in numbers] 

print(string_list) # ['1','2','3','4','5']