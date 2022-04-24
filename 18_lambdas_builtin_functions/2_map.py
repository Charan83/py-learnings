#   map
#       - standard function that acceppts 2 arguments
#           - function
#           - iterable (like ., lists, strinigs, dictionaries, sets, tuples)
#       - we can pass lambda function for the function argument,
#           which will run for each value in the iterable.
#       - returns a map object which can be converted into other datastructures
#       - once we iterate over the map, the map will be empty


#   example : 1
nums = [1, 2, 3, 4, 5, 6]
double = map(lambda num: 2*num, nums)
# [2, 4, 6, 8, 10, 12] # when we convert to list it iterates, so the map becomes empty
# print(list(double))
for item in double:
    print(item)
print(list(double))  # []


#   example : 2
def decrement_list(num_list):
    return list(map(lambda num: num-1, num_list))


result1 = decrement_list([1, 2, 3])
print(f"result1 : {result1}")
