#   __init__
#       - Classes in python have a special __init__ method, which gets called everytime you create an instance of the class
#       - Well almost everytime in a class we need __init__ method.
#       - In few cases, when a class only holds methods and no data, you wouldn't need an __init__ method in that case
#   self :
#       - refers to specific instance of the class
#       - always will be the first parameter in the __init__ method


class User:
    def __init__(self, first_name, last_name):
        # self : refers to specific instance of the class
        print(f"A new user is created! {self}")
        self.fname = first_name
        self.lname = last_name


user1 = User('Rohit', 'Sharma')
user2 = User('MS', 'Dhoni')
print(user1)  # <__main__.User object at 0x10a0fa7a0>
print(type(user1))
print(user2.fname, user2.lname)


#   Example : social media comments
class Comment:
    def __init__(self, uname, text, likes=0):
        self.username = uname
        self.text = text
        self.likes = likes


c1 = Comment('Guru', "sooo cute", 10)
print(f"{c1.username} posted a text '{c1.text}' and got '{c1.likes}'")
