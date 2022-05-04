#   Higher Order Functions
#       - is a function which accepts a function as an argument(we can pass funcs as args to other funcs)
#       - returns a function from another function

#   Example : we can pass funcs as args to other funcs

def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total


def square(x):
    return x*x


print(sum(3, square))
