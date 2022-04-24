#   filter
#       - lambda runs for each value in the iterable (same as map)
#       - returns filter object which can be converted to other iterables
#       - The filter object contains only the values that return true to the lambda function

#   example 1:

lst = list(range(1, 10))
evens = list(filter(lambda i: i % 2 == 0, lst))
print(f"evens : {evens}")


#   example 2:
users = [
    {"username": "sam", "tweets": ["I love coding", "I love cake"]},
    {"username": "Rohit", "tweets": ["I love batting", "I love catching"]},
    {"username": "Dhoni", "tweets": []},
    {"username": "Prudvi", "tweets": ["I love coding", "I love cake"]},
    {"username": "Ishan", "tweets": []},
]

in_active_users = list(filter(lambda o: not o["tweets"], users))
print(f"in_active_users : {in_active_users}")

in_active_users_list_comprehension = [
    user for user in users if not user["tweets"]]
print(
    f"in_active_users_list_comprehension : {in_active_users_list_comprehension}")


# example 3:
def remove_nagatives(num_list):
    return list(filter(lambda num: num >= 0, num_list))
    # return [num for num in num_list if num >= 0] # using list comprehension


result_list_comprehension = remove_nagatives([-1, 3, 4, -99])
print(f"result_list_comprehension : {result_list_comprehension}")
