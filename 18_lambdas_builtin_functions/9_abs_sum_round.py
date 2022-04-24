#   abs
#       - returns an absolute value of a number
#       - the argument may be an integer / floating point number
#   math.fabs (need to import math)
#       - always retuns a floating val which is absolute
print(abs(-35.33), abs(33), abs(-29))
# print(abs('error'))  # TypeError


#   sum
#       - takes an iterable and an optional start (start default = 0)
#       - returns the sum of start and the items of an iterable from left to right and returns the total
# passing list as iterable and with/without start
print(sum([1, 2, 3, 4]), sum([1, 2, 3, 4], 10))
print(sum((1, 2, 3, 4)))  # tuple iterable
print(sum({1, 2, 3, 4}))  # set iterable


#   round
#       - returns number rounded to n digits precision after decimal point
#       - if precision to number of digits is not passed or None, it will take it retuns nearest integer
print(round(12.345423, 2), round(12.5434532))


#   example 1
def max_magnitude(num_list):
    return max(abs(num) for num in num_list)


max_mag = max_magnitude([300, 20, -900])
print(max_mag)


print((abs(num) for num in [300, 20, -900]))


#   example 2
def sum_even_values(*args):
    return sum((num for num in args if num % 2 == 0), 0)


print(sum_even_values(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(sum_even_values(1, 3, 5, 7, 9))


#   example 3
def sum_floats(*args):
    return sum((num for num in args if type(num) == float), 0)


print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1, 2, 3, 4, 5))
