# Tuple - an ordered collection or grouping of items
# Immutable. Cannot be changed.

# Faster than lists - Tuple is stored in single block of memory. List = two blocks of memory

numbers = (1,2,3,4)

# Tuples can be used as keys in dictionaries:
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "NY Office",
    (37.7749, 122.4194): "San Francisco Office",
}

# .items() returns a tuple

# Built-in methods:

# count - returns the number of times a value appears in a tuple:
x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

# index - returns the index at which a value is found
t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError... not in tuple
t.index(3) # 2 - only the first matching index is returned
