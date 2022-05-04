from time import time


def speed_test(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time taken : {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_num_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_num_list():
    return sum([x for x in range(90000000)])


""" Executing sum_num_gen
Time taken: 3.7460360527038574
4049999955000000
Executing sum_num_list
Time taken: 5.235959053039551
4049999955000000 """
print(sum_num_gen())
print(sum_num_list())
