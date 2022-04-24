'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

"""accept a list, and return a new list with every second value removed"""


def remove_every_other(lst):
    return lst[::2]


print(remove_every_other([1, 2, 3, 4, 5]))
print(remove_every_other([5, 1, 2, 4, 1]))
print(remove_every_other([1]))
