def colorize(text, color):
    colors = ('red', 'yellow', 'green')
    if type(text) is not str:
        raise TypeError(f"'{text}' text must be an instance of str")
    if color not in colors:
        raise ValueError(f"{color} must be choosed from {colors}")
    print(f"'{text}' is printing in {color}")


colorize('error message', 'red')
colorize('error message', 'reds')
colorize(2, 'red')
