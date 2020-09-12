'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(l):
    if l:
        return l[-1] # if l exists, return the last (-1) element
    else:
        return None