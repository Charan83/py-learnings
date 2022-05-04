from functools import wraps


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''I AM WRAPPER FUNCTION'''
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)

    return wrapper


@log_function_data
def add(x, y):
    '''Adds two numbers together.'''
    return x+y


""" 
you are about to call add
Here's the documentation: Adds two numbers together. 
50
"""
print(add(30, 20))

""" 
I AM WRAPPER FUNCTION
wrapper 
"""
#   - to get the proper metadata for the add function
#   - we have to use wraps from functools
#   - after using wraps see below the meta data printed
""" 
Adds two numbers together.
add 
"""
print(add.__doc__)
print(add.__name__)
# help(add)
