# for num in range(10): # 0-9
#     print(num)

# for num in range(10,20,2): # 10, 12, 14, 16, 18
#     print(num)

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0
 
 
# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

# OR

x = 0
 
for i in range(11,21,2):
        x += i