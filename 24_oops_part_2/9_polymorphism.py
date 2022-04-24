#   polymorpphism
#       - an object can take on many(poly) forms(morph)
#       - two imp practical application of polymorphism
#           - the same class method works in a different way for different classes (method overwriting)
#               - ex: __repr__()
#           - the same mehod with in the class works different for different kinds of objects (method overloading)
#               - ex: len('string'), len([1,2,3,4])

class Animal:
    def speak(self):
        raise NotImplementedError("subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "woof woof"


class Cat(Animal):

    def speak(self):
        return "meow meow"

    def display(self, str):
        print(str)

    def display(self, lst):
        print(lst)


class Fish(Animal):
    pass


c = Cat()
print(c.speak())
c.display('speaking')
c.display([1, 2, 3])

f = Fish()
f.speak()
a = Animal()
a.speak()
