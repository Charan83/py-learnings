#   generators
#       - generators are iterators, and are subset of iterators (every generator is an iterator but not every iterator is a generator)
#       - genrators can be created
#           - using generator functions(a way to create generator which is an iterator) which uses yield keyword
#               - uses yield
#               - can yield multiple times
#               - when invoked, return a generator
#           - Generators can also be created with generator expression
#               - uses return
#               - returns once only
#               - when invoked, return the return value

#   example 1 : first generator
def count_up_to(max):
    count = 1
    while count <= max:
        # in any function when we keep an yield it will return a generator object
        # yield will keep the most recent val in the memory(not all values are kep in the memory), retun the val when next(<generator obj>) is called on the generator obj and pause until the next time it is called again
        yield count
        count += 1


generator_object = count_up_to(5)
print(generator_object)  # <generator object count_up_to at 0x10c0edd20>
# generator_object we can't execute a generator object as its not callable, its an object (generator object)
# we can call next and pass the generator object
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))

#   Note: generator function return generator object which is an iterator
