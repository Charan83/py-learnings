'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!


def reverse_string_using_slice(str):
    return str[::-1]


def reverse_string_using_reversed_join(str):
    # reversed(str) returns --> <reversed object at 0x1087d2dd0>
    # convert to string using join()
    return ''.join(reversed(str))


def reverse_string_using_for_loop(str):
    rev_str = ''
    for ch in str:
        rev_str = ch + rev_str
    return rev_str


print(reverse_string_using_slice('charan'))
print(reverse_string_using_reversed_join('charan'))
print(reverse_string_using_for_loop('charan'))
