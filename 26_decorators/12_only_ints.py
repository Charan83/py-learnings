from functools import wraps
from tkinter import E


def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError(
                "Please only invoke with integers. Looks like you have passed kwargs")
        elif not all(type(arg) == int for arg in args):
            raise ValueError(
                "Please only invoke with integers. Looks like you have passed other data types")
        return fn(*args, **kwargs)

    return wrapper


@only_ints
def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, name='Guru'))
print(add(1, 2, 3, 4, 5, 'e'))
