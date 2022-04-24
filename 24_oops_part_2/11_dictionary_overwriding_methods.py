class GrumpyDict(dict):
    def __repr__(self) -> str:
        print("YOU ARE PRINTING GRUMPY DICTIONARY!!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT IS MISSING IN THIS DICTIONARY")

    def __setitem__(self, key, val) -> None:
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK OK CHANGING SOON !!")
        super().__setitem__(key, val.upper())

    def __contains__(self, __o: object) -> bool:
        print("CHECKING IF THE ITEM IS IN DICT")
        return super().__contains__(__o)


gd = GrumpyDict({"first": "Guru", "animal": "Dog"})
print(gd)
gd["NOKEY"]
gd["newkey"] = "new value"
print(gd)
print("first" in gd)
