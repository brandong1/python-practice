# Return a new list with the string "Your instructor is " + each value in the array, but only if the value is less than five characters:

names = ['Lassie', 'Colt', 'Rusty']

list(map(lambda name: f"Your instructor is {name}",
    filter(lambda value: len(value) < 5, names)))

# List comprehension with same example as above

names = ['Lassie', 'Colt', 'Rusty']

[f"Your instructor is {name}" for name in names if len(name) < 5]