# pop - remove the item at the given index in the list and resturns it
# if no index is specified, removes and returns last item in the list

first_list = [1,2,3,4]
first_list.pop() # 4
first_list.pop(1) # 2

# remove - remove first item from list whose value is x
# throws ValueError if the item is not found.