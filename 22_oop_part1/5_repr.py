#   __repr__
#       - when we print the object it will print whatever is returned from __repr__ method
#       - Also when we convert to string as well __repr__ method is called


from tkinter import N


class Movie:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.name}'s running time is {self.duration} min"


m1 = Movie('Tammudu', 180)
# before having the __repr__ method in the class, it will print as <__main__.Movie object at 0x10daaeef0>
# after __repr__ method : Tammudu's running time is 180 min
print(m1)
# before having the __repr__ method in the class, it will print as <__main__.Movie object at 0x10daaeef0>
# after __repr__ method : Tammudu's running time is 180 min
print(str(m1))
