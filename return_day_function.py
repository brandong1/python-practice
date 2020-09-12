# Write a function that takes in one parameter (a number from 1-7) and returns the day of the week.
# If the number is less than 1 or greater than 7, return None.

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def return_day(num):
    if num > 0 and num <= len(days):
        return days[num - 1]
    else:
        None