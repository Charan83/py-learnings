# sets
#   - NO order
#   - NO duplicates
#   - collection of items
#   - can't access the items in set using index, as they are not in order
#   - like combination of list & dictionary features
#       - no order like dict, and syntax like dict use {}
#       - no key, val pairs like list
#

# example
set1 = set({1, 2, 3, 4, 4, 4, 4})
print(f"set1 : {set1}")  # set1 : {1, 2, 3, 4}

set2 = {1, 'a', 2, 3, 45, 2.3, 4, 4}
# set2 : {1, 2, 3, 4, 2.3, 'a', 45}
print(f"set2 : {set2}")
print(f"4 in set2 : {4 in set2}")  # 4 in set2 : True
# set2[2]  # will throw TypeError: 'set' object is not subscriptable

# example looping
set_loop = {1, 2, 3, 4, 5, 5, 5, 5}
for item in set_loop:
    print(item)  # 1 2 3 4 5

# example : find the unique countries of users
user_countries = ['India', 'Sweden', 'Sweden',
                  'India', 'USA', 'UK', 'USA', 'France']
# converting list into set to get the usique user countries : {'Sweden', 'USA', 'India', 'France', 'UK'}
print(
    f"converting list into set to get the usique user countries : {set(user_countries)}")
# converting list into set to get the usique user countries and converting back to list : ['Sweden', 'USA', 'India', 'France', 'UK']
print(
    f"converting list into set to get the usique user countries and converting back to list : {list(set(user_countries))}")

# converting list into set and get the count of number of unique countries users are from using 'len' : 5
print(
    f"converting list into set and get the count of number of unique countries users are from using 'len' : {len(list(set(user_countries)))}")
print(
    f"converting list into set and get the count of number of unique countries users are from using 'len' : {len((set(user_countries)))}")
