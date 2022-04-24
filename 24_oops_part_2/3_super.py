#   super()
#       - refers to the parent class
#       - when we print the object of a class it will run the __repr__() method
#           - if the class doesn't have that method it will look for the parent class for that method and run it
#           - if the parent also doesn't have __repr__() then it goes further up in the class hirarchy until it finds it or it will run the __repr__() from object class

class Animal:
    def __init__(self, name, species) -> None:
        self._name = name
        self._species = species

    def __repr__(self) -> str:
        return f"{self.name} is a {self.species}"

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, species, breed, toy) -> None:
        # super() --> refers to the base/parent class
        super().__init__(name, species)
        self._breed = breed
        self._toy = toy

    #
    def __repr__(self) -> str:
        return f"{self.name} is a {self.species}, its breed is {self.breed} and has a toy {self.toy}"

    @property
    def breed(self):
        return self._breed

    @property
    def toy(self):
        return self._toy


blue = Cat('Blue', 'Cat', 'Scottish Fold', 'String')
print(blue)
blue.make_sound('meow')
