#   all
#       - returns true : if all elements of the iterable are truthy
#       - returns true : if the iterable is empty

#   example 1
lst_falsy = [0, 1, 2, 3, 4]
print(all(lst_falsy))  # false : as 0 is a falsy value in the iterable
lst_true = [1, 2, 3, 4]
print(all(lst_true))  # false : as 0 is a falsy value in the iterable

people = ['Charlie', 'Cody', 'Chris', 'Kate']
people_with_c = [person for person in people if person[0] == 'C']
print(all(person[0] == 'C' for person in people_with_c))


#   any
#       - returns true :  if anu element of the iterable is truthy.
#       - returns false :if the iterable is empty
print(f"any([0, 0, 0, 1, 0]) : {any([0, 0, 0, 1, 0])}")
