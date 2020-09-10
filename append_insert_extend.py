# append - add item to the end of a list
# append only takes on argument
data = [1,2,3]
data.append("purple") # [1,2,3,"purple"]

# extend - add to the end of a list all values passed
a_list = [1,2,3,4]
a_list.extend([5,6,7,8])
print(a_list) # [1,2,3,4,5,6,7,8]

# insert - insert an item at a given position
first_list = [1,2,3,4]
first_list.insert(2, "Hi!")
print(first_list) # [1,2,"Hi!", 3,4]

first_list.insert(-1, "The end")
print(first_list) # [1,2,"Hi!",3,"The end", 4]
