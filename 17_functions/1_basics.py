# funtions :
#   - use 'def' to define a function
#   - use 'return' to return from a function
#   - we can have default parameters def square(num = 2):
#   - we can use keyword arguments
#       - when calling a function. so we can pass arguments in different order
#       - Also useful when we pass a dict to a function and unpacking its values
#   - inside a function if you want to look for a global variable you need to mention explicitly by using 'global' keyword only when you try to change the variable value. You can still access it without using 'global'
#   - 'nonlocal' used in inner function to reference a variable in the outer function
#   - for documentation use triple double quotes """doc string"""
#       - ex : random.randint.__doc__

from random import random
#   example 1 : defining a function
#   - we use def
# Define your make_noise function below


def make_noise():
    """prints noise string!!"""
    print("I'm making noizeeeeee!")


# Then, call make_noise once:
make_noise()
print(make_noise.__doc__)  # doc string


#   example 2 : returning value from a function
#   - using return


def heads_or_tails():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(f"heads_or_tails() : {heads_or_tails()}")


#   example 3 : returning list from a function
def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]


# generate_evens() : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
print(f"generate_evens() : {generate_evens()}")

#   example 4 : where is it wrong
# Without adding any new lines of code, make count_dollar_signs work as intended


def count_dollar_signs(word):
    count = 0
    for char in word:  # "dsf$dfsdf$$$"
        if char == '$':
            count += 1
    return count  # proper indentation, it should return after loop as corrected


#   example 5 : default parameters and keyword arguments
def full_name(first='Guru', last='Charan'):
    return f"{first} {last}"


print(f"full_name() : {full_name()}")
print(
    f"full_name(last='Sakhi', first='Prem') : {full_name(last='Sakhi', first='Prem')}")
