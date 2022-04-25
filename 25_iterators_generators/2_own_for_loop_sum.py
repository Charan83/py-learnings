from email import iterators


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            func(next(iterator))
        except:
            print("completed iterating the iterator")
            break


def my_sum(iterable):
    iterator = iter(iterable)
    total_val = 0
    while True:
        try:
            current_item = next(iterator)
            total_val += current_item
        except:
            print("completed iterating the iterator")
            break
    return total_val


my_for("hello", print)
my_for([1, 2, 3, 4, 5], lambda item: print(item * item))
sum_list = my_sum([10, 30, 40, 50])
print(f"sum_list : {sum_list}")
