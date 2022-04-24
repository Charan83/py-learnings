#   zip
#       - makes an iterator that aggregates elements from each of the iterabkes
#       - returns an iterator of tuples, where the i-th tuple contains the ith element from each of the argument sequences or iterables
#       - the iterator stops when the shortest inpur iterable is exhausted

first_zip = zip([1, 2, 3], [4, 5, 6])
print(first_zip)  # zip object of tuples <zip object at 0x1020b2740>
print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]
print(dict(first_zip))  # {}, once iterated the zip object is empty

second_zip = zip([1, 2, 3], [4, 5, 6])
print(dict(second_zip))  # {1: 4, 2: 5, 3: 6}


third_zip = zip(['hi', 'hello', 'namaskar'], [
                1, 2, 3, 44, 55], [4, 5, 6, 7, 8])
print(list(third_zip))  # [('hi', 1, 4), ('hello', 2, 5), ('namaskar', 3, 6)]

#   un-packing list of tuples to pass on to zip
tuple_list = [(1, 4), (2, 5), (3, 6)]
fourth_zip = zip(*tuple_list)  # zip((1, 4), (2, 5), (3, 6))
print(list(fourth_zip))


#   example 1: complex
midterm_scores = [80, 91, 78]
final_scores = [98, 89, 53]
students = ['dan', 'ang', 'kate']

students_scores = dict(
    zip(students, [max(t) for t in zip(midterm_scores, final_scores)]))
print(students_scores)  # {'dan': 98, 'ang': 91, 'kate': 78}


# example 2 : interleaving strings
def interleave(str1, str2):
    # list(zip(str1, str2)) # [('h', 'h'), ('i', 'a')]
    return ''.join([t[0] + t[1] for t in list(zip(str1, str2))])


print(interleave('hi', 'ha'))
print(interleave('aaa', 'zzz'))

# example 3 : triple_and_filter
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''


def triple_and_filter(num_list):
    return [num*3 for num in num_list if num % 4 == 0]


print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))


# example 4 : extract_full_name
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


def extract_full_name(dict_list):
    # return list(name.get("first") + ' ' + name.get("last") for name in dict_list)
    return list(map(lambda name: f"{name.get('first')} {name.get('last')}", dict_list))


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
