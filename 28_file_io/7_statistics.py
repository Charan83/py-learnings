def statistics(file_name):
    with open(file_name) as file:
        line_list = file.readlines()
        no_of_lines = len(line_list)
        no_of_words = sum(len(line.split(" ")) for line in line_list)

        file.seek(0)
        no_of_char = len(file.read())

        return dict(lines=no_of_lines, words=no_of_words, characters=no_of_char)


if __name__ == "__main__":
    data = statistics('./writefile.txt')
    print(data)
