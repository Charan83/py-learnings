# list comprehention
#   - generates a new list
#   - syntax : [ - for - in - ]

# list comprehension vs loops
nums = [1, 2, 3]
sq_nums = [num*num for num in nums]
print(f"nums : {nums}, sq_nums : {sq_nums}")

sq_nums_loop = []
for num in nums:
    sq_nums_loop.append(num * num)
print(f"nums : {nums}, sq_nums_loop : {sq_nums_loop}")

# list comprehension on strings
name = "Guru"
each_char = "-".join([char.upper() for char in name])
print(f"name : {name}, each_char : {each_char}")

# example 1
friends = ["guru", "prem", "hansni"]
frinds_updated = [friend[0].upper() + friend[1:] for friend in friends]
print(f"friends : {friends}, frinds_updated : {frinds_updated}")

# example 2 : on ranges
ranges_example = [num*num for num in range(1, 6)]
print(f"ranges_example : {ranges_example}")

# example 3 : with bool function
bool_example = [bool(val) for val in [0, [], '', [1, 2], 'Hello']]
print(f"bool_example : {bool_example}")

# example 4 : take list of nums and convert to list of strings
nums_list = [1, 2, 3, 4, 5, 6]
str_list = [str(num) for num in nums_list]
print(f"str_list : {str_list}")
