from copy import copy


class Human:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __repr__(self):
        return f"Human named : {self.fname} {self.lname} aged {self.age}"

    # + will refer to this __add__
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(fname="Hansni", lname="Annapantula", age=0)
        raise ValueError("other should be an instance of Human")

    # * will refer to this __mul__
    def __mul__(self, times):
        if isinstance(times, int):
            return [copy(self) for item in range(times)]
        raise ValueError("times should be an integer")


g = Human('Guru', 'Annapantula', 39)
s = Human('Sakhi', "Annapantula", 38)
print(g)
nb = g + s
print(s)
print(nb)
m = g * 2
print(m)
print(m[0] is m[1])
