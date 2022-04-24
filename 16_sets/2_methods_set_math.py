set1 = {1, 2, 3, 4, 5, 5, 5, 5}
# add()
set1.add(6)
# {1, 2, 3, 4, 5, 6}
print(set1)

# remove()
set1.remove(5)
print(f"set1 after removing 5 : {set1}")
# set1.remove(15)  # KeyError: 15

# discard()
set1.discard(15)
# set1 after trying to remove not existing item 15, from set using discard will not throw error(unlike how it throws when we try to use remove()): {1, 2, 3, 4, 6}
print(
    f"set1 after trying to remove not existing item 15, from set using discard will not throw error(unlike how it throws when we try to use remove()): {set1}")

# copy()
set2 = set1.copy()
print(set2)
# set1 == set2: True
print(f"set1 == set2 : {set1 == set2}")
# set1 is set2: False
print(f"set1 is set2 : {set1 is set2}")

# clear()
clear_set = {1, 2, 3, 4, 5}
# set before clearing: {1, 2, 3, 4, 5},  after clearing: None, set()
print(
    f"set before clearing : {clear_set},  after clearing : {clear_set.clear()}, {clear_set}")


# set Math : intersection / union / symmetric_difference
rcb_team = {'Virat', 'Fah', 'Padikal', 'Match1', 'Match2'}
csk_team = {'Dhoni', 'Jaddu', 'Bravo', 'Match1', 'Match2'}
# Union : {'Virat', 'Match2', 'Match1', 'Dhoni', 'Padikal', 'Bravo', 'Jaddu', 'Fah'}
print(f"Union : {rcb_team | csk_team}")
# Intersection: {'Match2', 'Match1'}
print(f"Intersection : {rcb_team & csk_team}")
