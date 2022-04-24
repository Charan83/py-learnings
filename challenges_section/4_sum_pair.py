'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

"""accept a list and a number,  and return first pair of numbers that sum to the number passed to the function"""


def sum_pairs(lst, target):
    already_visited = set()
    for item in lst:
        difference = target - item
        if difference in already_visited:
            return [difference, item]
        already_visited.add(item)
        print(already_visited)
    return []


""" print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
print(sum_pairs([11, 20, 4, 92, 80, 8], 100)) """
print(sum_pairs([11, 21, 4, 92, 80, 8], 100))
