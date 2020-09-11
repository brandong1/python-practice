instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",  
}

for value in instructor.values():
    print(values) # "Colt", True, 4, "Python"

for key, value in instructor.items():
    print(key,value) 
    # "name": "Colt",
    # "owns_dog": True,
    # "num_courses": 4,
    # "favorite_language": "Python"

####################

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0

for value in donations.values():
    total_donations += value
print(total_donations)

total_donations = sum(donations.values())