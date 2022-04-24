#   *args
#       - we can catch all the arguments passed in one *args variable
#       - *args is a tuple with all the arguments passed
#       - should be the last argument

#   parameters ordering
#       - parameters
#       - *args
#       - default parameters
#       - **kwargs


#   example 1
from sys import prefix


def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(f"sum(1,2,3,4,5,6) : {sum(1,2,3,4,5,6)}")


#   example 2
def contains_purple(*args):
    if "purple" in args:
        return True
    return False


print(contains_purple(25, "purple"))


#   **kwargs
#       - when we call a function with arguments like key=val, we can hold those using **kwargs
#       - **kwargs is a dictionary
#       - should be the last argument

#   example 1
def special_greeting(**kwargs):
    print(kwargs)  # {'David': 'special'}
    if 'David' in kwargs and kwargs.get('David') == 'special':
        return 'You get special greetings David!'
    return 'Who are you!!!'


print(special_greeting(David='special'))

#   example 2


def combine_words(str, **kwargs):
    print(kwargs)
    if "prefix" in kwargs:
        return f"{kwargs.get('prefix')}{str}"
    if "suffix" in kwargs:
        return f"{str}{kwargs.get('suffix')}"
    return str


print(combine_words('child', prefix='man'))
print(combine_words('child', suffix='ish'))
print(combine_words('child'))


#   parameters ordering
#       - parameters
#       - *args
#       - default parameters
#       - **kwargs

#   example 3
def display_info(a, b, *args, instructor='Guru', **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, 4, last_name='Anna', job='instructor'))
