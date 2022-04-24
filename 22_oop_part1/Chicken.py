class Chicken:
    total_eggs = 0

    def __init__(self, species, name, eggs=0):
        self.species = species
        self.name = name
        self.eggs = eggs

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return f"{self.name} laid {self.eggs} eggs"


c1 = Chicken(name='Alice', species='Partridge Silkie')
c2 = Chicken(name='Amelia', species='Speckled Sussex')
print(Chicken.total_eggs)
print(c1.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)
