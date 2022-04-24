class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_type="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Father:
    def __init__(self, eye_color="blue", hair_color="blond", hair_type="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Child(Mother, Father):
    """ def __init__(self):
        super().__init__() """

    def __repr__(self) -> str:
        return f"{self.eye_color}, {self.hair_color}, {self.hair_type}"


child = Child()
print(child)
