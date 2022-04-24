# python --> List
# JS --> Array

tasks = ["Install Python", "Learning Python", "Take a Break"]
# ['Install Python', 'Learning Python', 'Take a Break']
print(tasks)

# length of the list
print(len(tasks))  # 3

# converting range to list
_range = range(1, 10)
print(_range)  # range(1, 10)
range_list = list(_range)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_list)

# Accessing data in Lists
print(tasks[0])  # Install Python
print(tasks[-1])  # Take a Break

# Check if the value is in list
print("Learning Python" in tasks)  # True
if "Learning Python" in tasks:
    print("nice, it will help you.")  # nice, it will help you.

# Iterating over lists and accessing all values of a list
# - for loops
colors = ["purple", "teal", "magenta"]
for color in colors:
    print(color)

# - While loop
nums = list(range(1, 5))
print(nums)  # [1, 2, 3, 4]
i = 0
while i < len(nums):
    print(f"{i} : {nums[i]}")
    i += 1

# List methods
# - Append, Insert, Extend (can be called on instance of any list)
# append :
#   - Adds data to the end of the list
#   - Cannot add multiple values to the list, it can only add one value to the list
first_list = list(range(1, 5))
first_list.append(5)
print(first_list)  # [1, 2, 3, 4, 5]

# extend
#   - can add multiple values to the end of the list, when passes as a list
first_list.extend([6, 7, 8, 9])  # should be passed as list
print(first_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert
#   - where to insert an item in the list
insert_list = [1, 2, 3, 4]
insert_list.insert(2, 'Hi!')
# [1, 2, 'Hi!', 3, 4]
print(insert_list)
insert_list.insert(-1, 'Last-1 item')
# [1, 2, 'Hi!', 3, 'Last-1 item', 4]
print(insert_list)
insert_list.insert(len(insert_list), "last Item")
# [1, 2, 'Hi!', 3, 'Last-1 item', 4, 'last Item']
print(insert_list)

# clear
#   - removes all items from the list
items = [1, 2, 3, 4, 5]
items.clear()
print(items)  # []

# pop
#   - removes the item at a perticular position or the last item when the position is not passes
#   - returns the removed item
pop_items = [0, 1, 2, 3, 4, 5]
print(pop_items.pop())  # 5
print(pop_items)  # [0, 1, 2, 3, 4]
print(pop_items.pop(3))  # 3
print(pop_items)  # [0,1,2,4]

# remove
#   - remove the first instance of the value that is passed
#   - throws ValueError if the item is not found
remove_list = [1, 2, 3, 4, 5, 6, 7]
if 6 in remove_list:
    remove_list.remove(6)
print(remove_list)
# remove_list.remove('Hi') ValueError: list.remove(x): x not in list

# index
#   - returns the index position if the item in the list
#   - if the item is not there in the list it will throw error : ValueError
index_list = [1, 2, 1, 2, 3, 4, 5, 6, 7]
print(index_list.index(2))
print(index_list.index(2, 2))

# count
#   - returns the number of times the item is in the list
#   - if its not there, it will return 0
count_list = [1, 1, 3, 2, 4, 3, 6, 3, 32]
print(f"count of 2 in the list: {count_list.count(2)}")

# reverse
#   - reverses the list, the list is mutated, it will NOT create a copy, the same list is reversed
reverse_num_list = [1, 2, 3, 4, 5]
reverse_num_list.reverse()
# reverse_num_list : [5, 4, 3, 2, 1]
print(f"reverse_num_list : {reverse_num_list}")

reverse_str_list = ['Guru', 'Prem', 'Hans']
reverse_str_list.reverse()
# reverse_str_list : ['Hans', 'Prem', 'Guru']
print(f"reverse_str_list : {reverse_str_list}")

# sort
#   - sorts the list, the list is mutated, it will NOT create a copy, the same list is sorted
sort_list = [1, 2, 3, 4, 5, 2, 3, 4, 5]
sort_list.sort()
# sort_list : [1, 2, 2, 3, 3, 4, 4, 5, 5]
print(f"sort_list : {sort_list}")


# join
#   - string method
#   - used a lot with list
join_list = ['Coding', 'is', 'fun!']
# Coding is fun!
print(" ".join(join_list))
