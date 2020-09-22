import random
import runtime_demos

def create_random_list(size, max_val):
    random_list = []
    for num in range(size):
        random_list.append(random.randint(1,max_val))

    return random_list

size = int(input("What size list do you want to create? ")) # cast as int
max = int(input("What is the max value of the range? "))

print(create_random_list(size, max))