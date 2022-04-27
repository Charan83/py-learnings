def get_multiples(num=1, times=10):
    for t in range(1, times+1):
        yield num * t


evens = get_multiples(2, 10)

print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))


default_times = get_multiples()
print(next(default_times))
print(next(default_times))
print(next(default_times))
print(next(default_times))
print(next(default_times))
print(next(default_times))
