class Human:
    def __init__(self, fname, lname, age):
        self._fname = fname
        self._lname = lname
        self._age = age

    def __repr__(self):
        return f"{self.fname} {self.lname}, age is {self.age} "

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def age(self):
        return self._age

    @fname.setter
    def fname(self, val):
        if type(val) != str:
            raise ValueError("fname should be a string")
        self._fname = val

    @lname.setter
    def lname(self, val):
        if type(val) != str:
            raise ValueError("lname should be a string")
        self._lname = val

    @age.setter
    def age(self, val):
        if val <= 0:
            raise ValueError(
                f"age should be greater than 0 but you passed {val}")
        self._age = val


h1 = Human('Guru', 'Charan', 39)
print(h1.age, h1.fname, h1.lname)
h1.age = 40
print(h1)
h1.age = -40
