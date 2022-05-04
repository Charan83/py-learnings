from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"printing tuple of positional args : {args}")
        print(f"printing dict of keyword args : {kwargs}")
        print(fn(*args, **kwargs))
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    return sum(args)


do_nothing(1, 2, 3, a="hi", b="bye")
