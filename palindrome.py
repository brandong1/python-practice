# str_to_check = input("Input string to check: ")

# if str_to_check == str_to_check[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# ##########
# def reverse(str1):
#     if(len(str1) == 0):
#         return str1
#     else:
#         return reverse(str1[1 : ]) + str1[0]
    
# string = input("Please enter your own String : ")
# str1 = reverse(string)
# print("String in reverse Order :  ", str1)

# if(string == str1):
#    print("This is a Palindrome String")
# else:
#    print("This is Not a Palindrome String")

# ###########
# string = input("Please enter your own String : ")
# flag = 0

# length = len(string)
# for i in range(length):
#     if(string[i] != string[length - i - 1]):
#         flag = 1
#         break

# if(flag == 0):
#    print("This is a Palindrome String")
# else:
#    print("This is Not a Palindrome String")

###########
word = "abba"
# word = "12jfs"
def is_palindrome(word):
    len_word = len(word)//2
    for i in range(len_word):
        if word[i] != word[-1-i]:
            return False
        return True
print(is_palindrome(word))