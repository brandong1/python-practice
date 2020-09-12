# Unnecessary else on line 5:
def is_odd_number(num):
    if val % 2 != 0:
        return True
    else:
        return False 

# Better version:
def is_odd_number(num):
    if val % 2 != 0:
        return True
    return False 

