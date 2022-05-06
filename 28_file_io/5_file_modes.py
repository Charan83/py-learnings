#   file modes
#       - https://docs.python.org/3/library/functions.html
#       - https://docs.python.org/3/library/functions.html#open
#       - 'r' : open for reading(default)
#       - 'w' : open for writing, truncating the file first
#       - 'a' : open for writing, appending to the end of file if it exists


with open('./appentext.txt', 'a') as appenfile:
    appenfile.write("To append data to a file use 'a' as second argument\n")
    appenfile.write("Existing content in the file is not lost\n")

with open('./appentext.txt', 'a') as appenfile:
    appenfile.write(
        "This is to show appen will not remove the previous data in the file\n")
    appenfile.write("Hence Proved!!!\n")
