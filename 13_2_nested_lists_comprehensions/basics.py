# accessing items in nested lists
lst_nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lst_nested[2][1])
print(lst_nested[-1][-1])
print("***************************")
# iterating through nested lists
for inner_lst in lst_nested:
    for val in inner_lst:
        print(val)
print("***************************")
