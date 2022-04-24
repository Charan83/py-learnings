# Tuple Unpacking
#   - using * as an argument to a function to 'unpack' the values
nums_tuple = (1, 2, 3, 4, 5, 6, 7)
nums_list = [1, 2, 3, 4, 5, 6, 7]


def unpacking_tuple(*args):  # nums_tuple = (1, 2, 3, 4, 5, 6, 7)
    # unpacking_tuple : args : (1, 2, 3, 4, 5, 6, 7)
    print(f"unpacking_tuple : args : {args}")
    total = 0
    for num in args:
        total += num
    print(total)


def unpacking_list(*args):  # nums_list = [1, 2, 3, 4, 5, 6, 7]
    # unpacking_list : args : (1, 2, 3, 4, 5, 6, 7)
    print(f"unpacking_list : args : {args}")
    total = 0
    for num in args:
        total += num
    print(total)


# TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
# unpacking_tuple(nums_tuple)

unpacking_tuple(*nums_tuple)  # using '*' in the argument
unpacking_list(*nums_list)  # using '*' in the argument
