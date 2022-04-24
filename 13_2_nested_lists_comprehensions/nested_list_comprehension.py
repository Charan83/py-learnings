# example 1 : iterating thr nested list and printing
nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(val) for val in inner_lst] for inner_lst in nested_lst]

# example 2 : creating a nested loop
nested_lst1 = [val for val in range(1, 6)]
print(f"nested_lst1 : {nested_lst1}")
nested_lst2 = [[val for val in range(1, 6)] for val in range(1, 6)]
print(f"nested_lst1 : {nested_lst2}")

# example 2 : creating a nested loop with if-else
tic_tac = [["X" if val %
            2 == 0 else 'O' for val in range(1, 10)] for val in range(1, 4)]
print(f"tic_tac : {tic_tac}")
