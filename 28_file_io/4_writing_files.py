#   writing files
#       - we need to open the file to write in it
#       - need to specify 'w' as the second argument.(default is 'r')
#       - File is automatically created if its not there
#       - with 'w' flag every time we close and write to the file, we are overwriting the file

with open('./writefile.txt', 'w') as wfile:
    wfile.write("Writing to the file using python!\n")
    wfile.write("File is automatically created if its not there\n")
    wfile.write(
        "with 'w' flag every time we close and write to the file, we are overwriting the file")

with open('./writefile.txt', 'r') as rfile:
    print(rfile.read())
