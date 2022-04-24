#   about __name__ variable
#       - every file has this __name__ variable
#       - if the file is teh main file being run , for that file __name__ == "__main__"
#       - otherwise its value is the file name
#       - when another file runs as main file and then the rest of the files if they are executed then
#           __name__ == FILE_NAME (ex: __name__variable2)
#       - when we import a python module, it finds the module and then run the code inside of the module where its imported
#       - so to ignore the code to execute we need to use the check if __name__ == "__main__":

import __name__variable2


def say_hi():
    print(f"file(4__name__variable) : the value for __name__ is {__name__}")

# run this method only when we execute this file directly
# __name__ == "__main__" only when we execute this file directly


if __name__ == "__main__":
    say_hi()


__name__variable2.say_bye()
