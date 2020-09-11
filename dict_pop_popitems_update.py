# pop - takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
d = dict(a=1,b=2,c=3)
d.pop() # TypeError: pop expected at least 1 argument..
d.pop('a') # 1
d # {'b': 2, 'c': 3}
d.pop('e') # KeyError

# popitem - removes a random key in a dictionary:
d = dict(a=1,b=2,c=3,d=4,e=5)
d.popitem() # ('d', 4)
d.popitem('a') # TypeError: popitem() take no arguments

# update - update keys and values with another set of k,v
first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

second.update(first)
second # {'a': 1, 'b': 2, 'c': 3 ...}

# overwrite existing key
second['a'] = "AMAZING"

# update again
second.update(first) # second # {'a': 1, 'b': 2, 'c': 3 ...}
second.update({}) # does nothing