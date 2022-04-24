#   module
#       - a module is just a python file
#       - import code from built-in module
#           - https://docs.python.org/3/py-modindex.html
#           - these are built in, so no need to install then we can directly import them and use
#               - ex: import random (https://docs.python.org/3/library/random.html#module-random)
#               - then we can use as, random.randint(), random.choice()
#           - alias the module
#               - ex: import ramdom as rand
#               - rand.randint(), rand.choice()
#           - importing parts of a module (recommended : only import what you need)
#               - from random import choice


from keyword import iskeyword
from math import sqrt
import random as rand
import random
from random import choice as choi
#   example 1: built-in modules
print(random.choice(['Guru', 'Prem', 'Hansni']))
print(random.shuffle(['Guru', 'Prem', 'Hansni']))

#   example 2: built-in modules with alias
print(rand.choice(['Guru', 'Prem', 'Hansni']))
print(rand.shuffle(['Guru', 'Prem', 'Hansni']))

#   example 3: import what you needed
print(choi(['Guru', 'Prem', 'Hansni']))

#   exercise 1:
# Import the math module:
# Use math.sqrt  to find the square root of 15129 and save it to variable called answer:
print(sqrt(15129))


#   exercise 2:


def contains_keyword(*args):
    return any(iskeyword(arg) for arg in args)


print(contains_keyword("hello", "Goodbye"))
print(contains_keyword("hello", "Goodbye", "def"))
print(contains_keyword("hello", "Goodbye", "if"))
