# dictionary comprehension
#   - similar to list comprehension
#   - we need to enclose in {}
#   - default we can iterate thr keys
#   - to iterate thr values or key,val we can use values() or items() respectively

# example 1 : iterating thr k,v of dict
numbers = {'first': 1, 'second': 2, 'third': 3}
squared_nums = {k: v*v for k, v in numbers.items()}
print(f"squared_nums : {squared_nums}")

# example 2 : iterating thr list and creating dict
lst = [1, 2, 3, 4, 5, 6]
squares = {val: val**2 for val in lst}
print(f"squares : {squares}")

# example 2 : creating a dictionary from 2 strings
str1 = 'ABC'
str2 = '123'
dict1 = {str1[i]: str2[i] for i in range(0, len(str1))}
print(f"dict1 : {dict1}")  # dict1 : {'A': '1', 'B': '2', 'C': '3'}

# example 3 : all key,val to upper case
num = {'first': 'orange', 'second': 'blue', 'third': 'green'}
cap_num = {k.upper(): v.upper() for k, v in num.items()}
print(f"cap_num : {cap_num}")


# example 4 : conditional logic
num_list = list(range(1, 101))
evens_dict = {num: 'even' for num in num_list if num % 2 == 0}
print(f"evens_dict : {evens_dict}")

# example 5 : conditional logic as part of value
num_list = list(range(1, 15))
evens_dict = {num: 'even' for num in num_list if num % 2 == 0}
print(f"evens_dict : {evens_dict}")

# example 6 : conditional logic as part of value
num_list = list(range(1, 15))
evens_odds_dict = {num: ('even' if num % 2 == 0 else 'odd')
                   for num in num_list}
print(f"evens_odds_dict : {evens_odds_dict}")

# example 5 : conditional logic as part of key and value : specific key,val to upper case
num = {'first': 'orange', 'second': 'blue', 'third': 'green'}
cap_specific_num = {(k.upper() if k is 'second' else k): (v.upper() if v is 'blue' else v)
                    for k, v in num.items()}
print(f"cap_specific_num : {cap_specific_num}")
