#   What we are doing when we are using decorators

#   What is happening when we are decorating a function
""" 
# when we write:
@decorator
def func(*args, **kwargs):
    pass
#   we are actually doing
fucn = decorator(func)


# when we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass


#   we are actually doing
fucn = decorator_with_args(arg)(func)
 """
