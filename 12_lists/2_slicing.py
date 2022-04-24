# Slicing
#   - list[start:end:step]
#   - works in the same way for strings as well
#   - list[0:] --> will get a copy of the list, original list is not mutated/changes
#   - list[:] --> complete copy of the list( a new list ). Note : oldList is newList => false

num_list = [1, 2, 3, 4, 5]
slice_list1 = num_list[1:]
# copied list after slice: [2, 3, 4, 5]
print(f"copied list after slice : {slice_list1}")
# original list is not changes: [1, 2, 3, 4, 5]
print(f"original list is not changes : {num_list}")
# sliced list: [5], original list: [1, 2, 3, 4, 5]
print(f"sliced list : {num_list[4:]}, original list : {num_list}")

num_list_for_neg_slicing = [1, 2, 3, 4, 5]
# sliced list using negative index: [3, 4, 5], original list : [1, 2, 3, 4, 5]
print(
    f"sliced list using negative index: {num_list_for_neg_slicing[-3:]}, original list : {num_list_for_neg_slicing}")

# slicing with end param
num_list_slice_using_end_param = [1, 2, 3, 4, 5, 6]
# sliced list using end index: [1, 2, 3], original list: [1, 2, 3, 4, 5, 6]
print(
    f"sliced list using end index: {num_list_slice_using_end_param[:3]}, original list : {num_list_slice_using_end_param}")
# sliced list using end - ve index: [1, 2, 3, 4], original list: [1, 2, 3, 4, 5, 6]
print(
    f"sliced list using end -ve index: {num_list_slice_using_end_param[:-2]}, original list : {num_list_slice_using_end_param}")

# slicing with step param
num_list_slice_using_step_param = [1, 2, 3, 4, 5, 6, 7, 8]
# sliced list using end index: [1, 3, 5, 7], original list: [1, 2, 3, 4, 5, 6, 7, 8]
print(
    f"sliced list using step index: {num_list_slice_using_step_param[::2]}, original list : {num_list_slice_using_step_param}")
# sliced list using end index: [1, 3], original list : [1, 2, 3, 4, 5, 6, 7, 8]
print(
    f"sliced list using end index: {num_list_slice_using_step_param[:4:2]}, original list : {num_list_slice_using_step_param}")

# slicing with -ve step param : to reverse the order of items in the list
# sliced list using -ve step index: [8, 7, 6], original list : [1, 2, 3, 4, 5, 6, 7, 8]
print(
    f"sliced list using -ve step index: {num_list_slice_using_step_param[:4:-1]}, original list : {num_list_slice_using_step_param}")

# reversing using slice (lists / strings)
my_string = "This is fun!"
reverse_string = my_string[::-1]
# !nuf si sihT
print(reverse_string)

reverse_using_slice = ["red", "orange", "green", 1, 2, 3]
new_list = reverse_using_slice[::-1]
# [3, 2, 1, 'green', 'orange', 'red']
print(new_list)
# reverse the string in the list : der
print(f"reverse the string in the list : {new_list[-1][::-1]}")
