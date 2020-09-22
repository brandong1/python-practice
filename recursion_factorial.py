# Factorial - if n = 5 or 5! then 5 x 4 x 3 x 2 x 1 = 120
# n! = n x (n-1)! or factorial(n) = n x factorial(n-1) for n > 0
# 5! = 5 x 4!
# factorial(5) = 5 x factorial(4)

def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)

z = 0 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")
z = 1 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")
z = 5 # expecting 120
print(f"The value of {z}! is {factorial_recur(z)}")