#   pdb : python debugger
#       - its a module that we have to import (like random)
#       - so we need to : import pdb
#       - and then : pdb.set_trace()

#   common pdb commands:
#       - l --> list
#       - n --> next line
#       - p --> print
#       - c --> continue -finishes debugging


#   example 1
import pdb
import re
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)


#   example 2
def add_numbers(n1, n2, n3, n4):
    import pdb
    pdb.set_trace()
    return n1+n2+n3+n4


print(add_numbers(1, 2, 3, 4))
