months = ('Jan', 'Feb', 'Mar', 'Apr')
# looping thr tuple
#   - same as list, we can use 'for' or 'while'

# example 1 : for loop
for month in months:
    print(f"month : {month}")

# example 2 : while loop to loop from last item to first
index = len(months) - 1
while index >= 0:
    print(months[index])
    index = index - 1

# example 3 : tuples methods
#   - tuples have only 2 methods
#       - count : returns the count of the item in question
#       - index : gets the index of the item in question (first index position if its a dublicate item)
tuple_methods = (1, 2, 3, 3, 3, 4, 5)
# count of the number 3 in tuple_methods : 3
print(f"count of the number 3 in tuple_methods : {tuple_methods.count(3)}")
# index position of the number 3 in tuple_methods: 2
print(
    f"index position of the number 3 in tuple_methods : {tuple_methods.index(3)}")


# example 4 : slicing on tuples
tuple_slicing = (1, 2, 3, 4, 5, 6, 7)
slice1 = tuple_slicing[:5]
# tuple_slicing : (1, 2, 3, 4, 5, 6, 7), slice1 : (1, 2, 3, 4, 5)
print(f"tuple_slicing : {tuple_slicing}, tuple_slicing[:5] : {slice1}")
# tuple_slicing : (1, 2, 3, 4, 5, 6, 7), tuple_slicing[2:] : (3, 4, 5, 6, 7)
print(
    f"tuple_slicing : {tuple_slicing}, tuple_slicing[2:] : {tuple_slicing[2:]}")
# tuple_slicing : (1, 2, 3, 4, 5, 6, 7), tuple_slicing[:-1] : (1, 2, 3, 4, 5, 6)
print(
    f"tuple_slicing : {tuple_slicing}, tuple_slicing[:-1] : {tuple_slicing[:-1]}")
# tuple_slicing : (1, 2, 3, 4, 5, 6, 7), tuple_slicing[:-1] : (7,)
print(
    f"tuple_slicing : {tuple_slicing}, tuple_slicing[-1:] : {tuple_slicing[-1:]}")
