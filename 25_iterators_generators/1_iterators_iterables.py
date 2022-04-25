#   iterator
#       - an object that can be iterated upon
#       - An object which returns data, one element at a time when next() is called on it.

#   iterable
#       - An object which will return an iterator when iter() is called on it

#       - Ex: any string is an iterable but not a iterator
#       - "Hello" is an iterable and when we call iter("Hello") -> retuns an iterator
#       - Then we can iterate through that iterator using next(), to get each item in the iterator until all elements are returned
#       - When there are no more items to return it will throw StopIteration

#   next()
#       - When next() is called on an iterator, the iterator will return the next item. It keeps doing until it raised StopIteration error

#   example 1
name_iterable = "Hello"
#   next(name_iterable)  # TypeError: 'str' object is not an iterator
name_iterator = iter(name_iterable)
print(next(name_iterator))  # H
print(next(name_iterator))  # e
print(next(name_iterator))  # l
print(next(name_iterator))  # l
print(next(name_iterator))  # o
try:
    print(next(name_iterator))  # StopIteration
except StopIteration:
    print("Reached end of iterator!!")

#   example 2
list_iterable = [1, 2, 3, 4]
list_iterator = iter(list_iterable)
while True:
    try:
        print(next(list_iterator))
    except StopIteration:
        print("Reached end of iterator!!")
        break
