file = open('./readfile.txt')

# --> cursor is at the end of the file now. So if we try to read again it will be empty.
text = file.read()

print(text)

# python reads file using cursor. After the file is read, the curson is at the end of the file.
print(file.read())
