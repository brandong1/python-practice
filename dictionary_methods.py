# clear - clears all keys and values in a dicitonary
d = dict(a=1,b=2,c=3)
d.clear()
d # {}

# copy - makes a clone of a dictionary
d = dict(a=1,b=2,c=3)
c = d.copy()
c # {'a': 1, 'b': 2, 'c': 3}
c == d # True. Equal in values
c is d # False. Same data, different object in memory

# fromkeys - creates key-value pairs from comma separated values:
{}.fromkeys("a","b") # {'a': 'b'}
{}.fromkeys(["email"], "unknown") # {"email": "unknown"}
{}.fromkeys("a",[1,2,3,4,5]) # {"a": [1,2,3,4,5]}

# get - retrieves a key in an object and return None instead of a KeyError if the key does not exist:
d = dict(a=1,b=2,c=3)
d['a'] # 1
d.get('a') # 1
d['name'] # KeyError
d.get('name') # None