from functools import wraps


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
            raise ValueError("Too many arguments!")

        return fn(*args, **kwargs)

    return wrapper


@ensure_fewer_than_three_args
def add_all(*args):
    return sum(args)


print(add_all(1, 2))
print(add_all(1, 2, 3))
