from operator import truediv


def get_unlimited_multiples(num=1):
    times = 1
    while True:
        yield num * times
        times += 1


sevens = get_unlimited_multiples(7)
seven_list = [next(sevens) for i in range(15)]
print(seven_list)

ones = get_unlimited_multiples()
one_list = [next(ones) for i in range(20)]
print(one_list)
