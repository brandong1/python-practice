class Student():
    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course.")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found!")

    def __str__(self):
        return f"First Name: {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"

courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java', 'rails', 'c']
brandon = Student("brandon", "green", courses_1)
john = Student("john", "doe", courses_2)

print(brandon.first_name, brandon.last_name, brandon.courses)
brandon.add_course("swift")
brandon.add_course("python")
brandon.remove_course("python")
brandon.remove_course("c++")

print(brandon.first_name, brandon.last_name, brandon.courses)

print(brandon)
print(john)
# brandon green ['python', 'rails', 'javascript']
print(john.first_name, john.last_name, john.courses)
# john doe ['java', 'rails', 'c']