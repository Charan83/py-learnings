#   seek()
#       - to move the cursor we use seek

file = open('./readfile.txt')

print(file.read())  # read() : read the entire file
print(file.read())

# move the cursor now and then read
file.seek(10)
print(file.read())

file.seek(0)
print(file.read())

file.seek(0)
print(file.readlines())  # read entire file and each line an item in a list

file.close()  # manually close the file
# error trying to access with the files after closing
# ValueError: I/O operation on closed file.
if not file.closed:  # file.closed => True / False
    file.read()
