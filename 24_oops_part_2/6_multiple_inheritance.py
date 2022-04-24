class Aquatic():
    def __init__(self, name) -> None:
        print("Aquatic __init__")
        self._name = name

    @property
    def name(self):
        return self._name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"Im {self.name} of the sea"


class Ambulatory:
    def __init__(self, name) -> None:
        print("Ambulatory __init__")
        self._name = name

    @property
    def name(self):
        return self._name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"Im {self.name} of the land"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin __init__")
        # will only call the __init__ of the first class Ambulatory, passed inthe list
        super().__init__(name)
        Aquatic.__init__(self, name)  # we need to call manually, if its needed


jaws = Aquatic('Jaws')
lassie = Ambulatory('Lassie')
captain_cook = Penguin('Captain Cook')
""" 
Jaws Jaws is swimming Im Jaws of the sea
Lassie Lassie is walking Im Lassie of the land
Captain Cook Captain Cook is swimming Captain Cook is walking Im Captain Cook of the land 
"""
print(jaws.name, jaws.swim(), jaws.greet())
print(lassie.name, lassie.walk(), lassie.greet())
print(captain_cook.name, captain_cook.swim(),
      captain_cook.walk(),
      captain_cook.greet())  # Im Captain Cook of the land, it takes the method from Ambulatory as its the first one the in the inheritance list that we passed to Penguin
