# Write a function called frequency that accepts a list and a search term and returns the number of times the search term appears in the list.

'''
frequency([1,2,3,4,4,4], 4) # 3
'''

def frequency(list, search_term):
    return list.count(search_term)