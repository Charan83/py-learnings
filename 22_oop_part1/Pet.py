class Pet:
    pet_count = 0
    allowed_pets = ['cat', 'dog', 'fish']

    def __init__(self, name, breed):
        if breed not in Pet.allowed_pets:
            raise ValueError(
                f"pets bread should be one amoung {Pet.allowed_pets}. Your input breed is '{breed}'")
        self.name = name
        self.breed = breed
        Pet.pet_count += 1


try:
    cat = Pet('snow', 'cat')
    dog = Pet('fire', 'dog')
    tiget = Pet('air', 'tiger')
except ValueError as err:
    print(f"ValueError : {err}")
finally:
    Pet.allowed_pets.append('monkey')
    monkey = Pet('bounce', 'monkey')
    print(f"Total pet count = {Pet.pet_count}")
