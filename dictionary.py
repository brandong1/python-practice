instructor = {
  "name": "Colt",
  "owns_dog": True,
  "num_courses": 4,
  "favorite_language": "Python",  
}

instructor["name"] # "Colt"
instructor["subject"] # KeyError

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + ' ' + artist["last"]
print(full_name) # Neil Young

###################
# using format()
artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"],artist["last"])

###################

#f string
artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"