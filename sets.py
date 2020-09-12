# Sets - formal mathematical sets
# Do not have duplicate values
# Elements in sets aren't ordered
# Cannot access items in a set by index

# Sets cannot have duplicates
s = set({1,2,3,4,5,5,5}) # {1,2,3,4,5}

# Accessing all values in a set:
numbers = {1,2,3,4}

for number in numbers:
    print(number)
# 1
# 2
# 3
# 4

# .add() - adds an element to a set. If the element is already in the set, the set doesn't change:
s = set([1,2,3])
s.add(4)
s # {1,2,3,4}
s.add(4)
s # {1,2,3,4} - doesn't change

# .remove() - removes a value from the set. Returns KeyError if the value is not found.
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1) # {1,2,4,5,6}

# .copy() - creates a copy of a set

# .clear() - removes everything in a set

# Suppose I teach two classes:
math_students = {"Joe", "Matthew", "Helen", "Jane"}
biology_students = {"Charlotte", "Matthew", "Oliver", "Jane"}

# To generate a set with all my unique students:
math_students | biology_students

# To generate a set with students who are in both courses:
math_students & biology_students # {"Matthew", "Jane"}