#   inheritance
#       - Cat inherits from Animal,
#           - class Cat(Animal)


class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    pass


animal = Animal()
cat = Cat()
animal.make_sound("animal sound")
print(f"animal is cool : {animal.cool}")
print(f"animal isinstance of object ? {isinstance(animal,object)}")
print(f"animal isinstance of Animal ? {isinstance(animal,Animal)}")
cat.make_sound("cat sound")
print(f"cat is cool : {cat.cool}")
print(f"cat isinstance of object ? {isinstance(cat, object)}")
print(f"cat isinstance of Animal ? {isinstance(cat, Animal)}")
print(f"cat isinstance of Cat ? {isinstance(cat, Cat)}")
