instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",  
}
# Does the dictionary have a certain key?
"name" in instructor # True
"awesome" in instructor # False

# Does the dictionary have a certain value?
"Colt" in instructor.values() # True
"Nope!" in instructor.values() # False