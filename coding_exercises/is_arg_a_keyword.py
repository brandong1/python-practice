# Define a function that accepts any number of string arguments. 
# Return True if ANY of the strings are Python keywords, otherise return False.


import keyword

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False