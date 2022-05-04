from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'role' in kwargs and kwargs.get('role') == 'admin':
            return fn(*args, **kwargs)
        else:
            raise ValueError("Unauthorized!!")

    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!!"


print(show_secrets(1, 2, 3, role='admin'))
print(show_secrets(1, 2, 3, role='admi'))
