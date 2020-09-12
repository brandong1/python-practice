{x**2 for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Identify if a string contains all the vowels:
string = "sequoia"
len({char for char in string if char in 'aeiou'}) == 5 # True