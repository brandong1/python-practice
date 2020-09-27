class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users!"

    def logout():
        User.active_users -= 1
        return f"{self.first} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

user1 = User("Joe", "Smith", 68)
user2 = User("Bianca", "Lopez", 41)

# print(user2.full_name())
# print(user2.initials())
# print(User.display_active_users())
# user1 = User("Joe", "Smith", 68)
# user2 = User("Bianca", "Lopez", 41)
# print(User.display_active_users())

