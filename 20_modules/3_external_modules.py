#   importing external modules
#       - ex : https://pypi.org/project/pytest/
#       - external modules are first downloaded and installed using pip
#           - python3 -m pip install pytest
#           - python3 -m pip install termcolor
#           - dir(termcolor)
#           - python3 --> help(termcolor)

from termcolor import colored
from pyfiglet import figlet_format

print(dir(colored))
# help(termcolor)
to_print = colored(
    "Hi there!", color="magenta", on_color='on_cyan', attrs=["blink"])
print(to_print)


#   exercise 1 : using pyfiglet
#       - python3 -m pip install pyfiglet

#       - help(pyfiglet)
msg = input("what message do you want to print? ")
msg_color = input("what color? ")
figlet_text = figlet_format(msg)
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan")
if msg_color not in valid_colors:
    msg_color = "green"
colored_text = colored(figlet_text, color=msg_color)
print(colored_text)
