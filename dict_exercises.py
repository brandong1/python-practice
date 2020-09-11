list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}
# {'CA: 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

#########################
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {key: value for key, value in person}
# {'name': 'Jared', ...}
#########################

#########################

#########################