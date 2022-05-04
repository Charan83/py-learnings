#   Example 1
""" def shout(fn):
    def wrapper(name):
        return fn(name).upper()

    return wrapper """


def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()

    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}"


print(greet('Himalaya'))


@shout
def order(main, side):
    return f"Gi, I'd like the {main}, with a side of {side}, please"


# TypeError: shout.<locals>.wrapper() takes 1 positional argument but 2 were given
# print(order("Okra Curry", "Samosa"))
#   so standard pattern to solve these args prob is to use *args, **kwargs
print(order("Okra Curry", "Samosa"))


@shout
def lol():
    return "lol"


print(lol())
