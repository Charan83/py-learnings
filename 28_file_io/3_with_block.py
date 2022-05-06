
#   - always closes the file after the 'with' block(even if there is an error)
#   - When entering the with block internally, it will run f.__enter__()
#   - While exiting the 'with' block it will run f.__exit__(), which closes the file
with open('./readfile.txt') as file:
    print(file.read())

print(file.closed)
