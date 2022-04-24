class User:
    active_users = 0  # class variable

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users!"

    @classmethod
    def from_string(cls, data_str):
        fname, lname, age = data_str.split(',')
        return cls(fname, lname, int(age))

    def __init__(self, fname, lname, age):  # instance method
        self.fname = fname  # instance variable
        self.lname = lname
        self.age = age
        # class variable, every time a user is created its incremented and this is shared accross all users
        User.active_users += 1

    def full_name(self):  # instance method
        return f"{self.fname} {self.lname}"

    def initials(self):  # instance method
        return f"{self.fname[0]}.{self.lname[0]}"

    def likes(self, item):  # instance method
        return f"{self.fname} like {item}"

    def is_senior(self):  # instance method
        return self.age >= 65

    def birthday(self):  # instance method
        self.age += 1
        return f"you turned {self.age}yrs old!"

    def logout(self):
        User.active_users -= 1
        return f"user '{self.full_name()}' logged out "


print(f"active_users : {User.active_users}")
user1 = User('Guru', 'Charan', 39)
print(user1.is_senior(), user1.birthday(), user1.likes(
    'coding'), user1.initials(), user1.full_name())
print(f"active_users : {User.active_users}")
user2 = User('Hansni', 'Annapantula', 10)
print(user2.is_senior(), user2.birthday(), user2.likes(
    'coding'), user2.initials(), user2.full_name())
print(f"active_users : {User.active_users}")
print(user2.logout())
print(f"active_users : {User.active_users}")
print(User.display_active_users())
user3 = User.from_string("Prem,Sakhi,38")
print(user3.is_senior(), user3.birthday(), user3.likes(
    'coding'), user3.initials(), user3.full_name())
print(f"active_users : {User.active_users}")
