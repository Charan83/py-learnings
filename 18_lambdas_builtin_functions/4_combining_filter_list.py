#   Combining filter and map

#   example 1:

names = ["Lassie", "Colt", "Rusty"]
result_lst = list(map(lambda i: f"Your instructor is {i}", filter(
    lambda name: len(name) >= 5, names)))
print(f"result_lst : {result_lst}")
# doing the same with list comprehension
result_list_comprehension = [
    f"Your instructor is {name}" for name in names if len(name) >= 5]
print(f"result_list_comprehension : {result_list_comprehension}")
