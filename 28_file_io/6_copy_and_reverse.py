from asyncore import read


def copy(src, dest):
    with open(src) as read_file:
        data = read_file.read()
    with open(dest, 'w') as wfile:
        wfile.write(data)


def copy_and_reverse(src, dest):
    with open(src) as file:
        data = file.read()

    with open(dest, 'w') as wfile:
        wfile.write(data[::-1])

    with open(dest) as rfile:
        print(rfile.read())


if __name__ == '__main__':
    copy('./readfile.txt', './copyfile.txt')
    copy_and_reverse('./readfile.txt', './copyandreversefile.txt')
