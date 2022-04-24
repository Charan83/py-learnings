'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

"""
return True if each value in the list is a list else false
"""


def list_check(lst):
    return all(type(item) == list for item in lst)


print(list_check([[], [1], [2, 3], (1, 2)]))
print(list_check([[], [1], [2, 3]]))
