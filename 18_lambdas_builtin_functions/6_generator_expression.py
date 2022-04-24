#   generator expressions
#       - lighter weight version of list
#       - we can't use list methods (like append, extend ....)
#       - we can use it as an intermediatory iterator, instead of converting to list we can use the generator
#       - so to pass it to any/all where we need not want a list, there we can use generators
#       - https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehensions
#       - basically use generator expression when we are iterating only once
#       - so in the case when we use any/all, its better to use generator comprehension

#   example 1
lst = list(range(90))
any_all = any(i*10 for i in lst)
print(any_all)
all_any = all(i*10 for i in lst)
print(all_any)

#   example 2


def is_all_strings(iter):
    return all(type(i) == str for i in iter)


print(is_all_strings(['a', 's']))
print(is_all_strings(['a', 's', 1]))
print(is_all_strings(['a', 's']))
