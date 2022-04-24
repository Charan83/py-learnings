#   about __name__ variable
#       - every file has this __name__ variable
#       - when we run a file, for that file __name__ == "__main__"
#       -

def say_bye():
    print(f"file(__name__variable2) : the value for __name__ is {__name__}")


if __name__ == "__main__":
    say_bye()
