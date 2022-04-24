# Tuples
#   - An ordered collection or group of items (in this sence its similar to list)
#   - can hold duplicate data like lists => (1,2,3,4,3,3,3)
#   - The difference b/n tuple / list
#       - syntax : tiples () / list []
#       - tuple is immutable (we cannot change it) / lists are mutable we can add/remove items, change the value of the existing item
#       - when we try to change the item in a tuple we get TypeError
#       - methods like append / remove / clear .... which modifies are not available for tuple
#   - Why use tupes
#       - faster than lists
#       - code safer when we want that datasttructure should not be changes
#       - can be used as valid keys in a dictionary
#       - some methods return tuple like .items() of dictionary
#   - Examples
#       - months of a year (ordered list that doesn't change)
#   - 2 ways to create
#       - tuple(1, 2, 3)
#       - (1, 2, 3)

# example 1
alphabet = ('a', 'b')
print(f"is 'a' in tuple : {'a' in alphabet}")  # is 'a' in tuple : True
# accessing val from a tuple is same as list with index ex, alphabet[0]: a
print(
    f"accessing val from a tuple is same as list with index ex, alphabet[0]: {alphabet[0]}")
# using type to get the type of alphabet type(alphabet): <class 'tuple'>
print(
    f"using type to get the type of alphabet type(alphabet): {type(alphabet)}")

# example 2 : tuples as keys in dictionary
location = {
    (39.59, 35.56): 'Stockholm',
    (52.34, 23.54): 'Hyderabad',
    (34.56, 34.46): 'Paris'
}
print(f"we can use tuples as keys for a dictionary : {location}")
