#Create a new function called simple_mult_premium(). This will
# take two numbers as parameters (int or float). You will need to check for if
# both the parameters passed in are either of type "int" or "float" and return
# their multiplied value if they are. If either of them are not "int" or "float"
# return the string "Need either int or float". You can use the isinstance
# function to test the type of the parameter. Example if you were testing num_1,
# you can use code like isinstance(num_1, (int, float)) to test for int or float.
# This expression will return True if num_1 is of type int or float (passed in
# as a tuple here). You can also do this individually like below
# isinstance(num_1, int)
## Write your code below
def simple_mult_premium(num1,num2):
    # I'm using isinstance to verify if both num1 AND num2 are either int or float, then multiply if True
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1* num2
    else:
        return "Need either int or float"
