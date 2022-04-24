# Dictionary unpacking
#   - using ** as an argument, for dictionary unpacking

# Example 1
def display_names(first, second):
    print(f"{first}, {second}")


# for unpacking it should have same keys
names = {"first": 'prem', "second": "sakhi"}
display_names('Guru', 'charan')
# TypeError: display_names() missing 1 required positional argument: 'second'
# display_names(names)
display_names(**names)
