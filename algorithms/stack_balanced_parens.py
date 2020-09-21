# Use a stack to check whether or not a string has balanced usage of parenthesis.
# Time: O(n^2)
# (), ()(), (({[]})) <- Balanced
# ((), )) <- Not Balanced

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True 
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack() # would need to create this class in separate file
    is_balanced = True 
    index = 0

    while index < len(paren_string):
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False