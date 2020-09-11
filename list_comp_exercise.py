# Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]

# Given a list [1,2,3,4,5,6], create a variable called answer2, which is a list of all the even values.

answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 

######################

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

######################

# For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.

answer = [val for val in range(1,101) if val % 12 == 0]


answer = [char for char in "amazing" if char not in "aeiou"]