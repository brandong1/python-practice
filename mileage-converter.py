print("How many kilometers did you run today?")
kilometers = input()
miles = float(kilometers) / 1.60934
miles = round(miles, 2)
print(f"Your {kilometers}km ride was {miles} miles.")

# round(thing to round, how many decimal points)