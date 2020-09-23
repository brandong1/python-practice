str_to_check = input("Input string to check: ")

if str_to_check == str_to_check[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")