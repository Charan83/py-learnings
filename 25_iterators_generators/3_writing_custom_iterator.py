#   creating and iterator like the range class
#       - range returns an iterator, thats why we are able to loop through using for loop

class Counter:
    def __init__(self, start, end) -> None:
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for c in Counter(1, 10):
    print(c)

#   - in the for loop Counter(1, 10) --> calls __init__ first
#   - then for loop will create an iterator = iter(Counter(1,10))
#   - next(iterator) will be called until it raises StopIteration error
