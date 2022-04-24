#   sorted
#       - list.sort() --> this will sort the original list
#       - list.sort() -> is a list specific method
#       - sorted --> will retuns a new list which is sorted. do not change the original list
#       - sorted: we can pass even a tuple as well, though it will return a list after sort

#   Example 1 : sorted on list
lst1 = [1, 2, 6, 7, 8, 3, 4, 5]
sorted_list = sorted(lst1, reverse=True)
# lst1 : [1, 2, 6, 7, 8, 3, 4, 5], sorted_list : [8, 7, 6, 5, 4, 3, 2, 1]
print(f"lst1 : {lst1}, sorted_list : {sorted_list}")

#   Example 2 : sorted on tuple
tuple1 = (1, 2, 6, 7, 8, 3, 4, 5)
print(f"tuple1 : {tuple1}, sorted(tuple1) : {sorted(tuple1)}")


# Example 3 :
users = [
    {"username": "sam", "tweets": [
        "I love coding", "I love cake", "I love batting", "I love catching"]},
    {"username": "Rohit", "tweets": ["I love batting", "I love catching"]},
    {"username": "Dhoni", "tweets": []},
    {"username": "Prudvi", "tweets": [
        "I love coding", "I love cake", "hi", "Bye"]},
    {"username": "Ishan", "tweets": []},
]

sorted_by_tweets = sorted(
    users, key=lambda user: len(user["tweets"]), reverse=True)
print(f"sorted_by_tweets : {sorted_by_tweets}")

sorted_by_username = sorted(
    users, key=lambda user: len(user["username"]))
print(f"sorted_by_username : {sorted_by_username}")
