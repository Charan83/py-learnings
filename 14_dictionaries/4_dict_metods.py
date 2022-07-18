user_info_clear = {
    "Student Name": "Guru",
    "Grade": 'A',
    "Score": 911,
    35: 'address'
}

# clear()
#   - clears the dictionary
print(f"dictionary method : clear()")
print(f"Before clear() on user_info_clear : {user_info_clear}")
user_info_clear.clear()
print(
    f"clear() removes all key, values from dictionary, 'user_info_clear' : {user_info_clear}")

# copy()
#   - creates a new copy of the dictionary
#   - original dictionary doesn't change
print(f"dictionary method : copy()")
user_info_copy = {
    "Student Name": "Guru",
    "Grade": 'A',
    "Score": 911,
    35: 'address'
}
user_info_copied = user_info_copy.copy()
print(f"user_info_copied : {user_info_copied}")

# is
#   - can be used for checking, if after copying[copy()] do both the variables refer to the same object? --> NO
#   - '==' will tell if both the objects have same values (similar to : '==' is JS)
print(f"check if its the same object in the memory : is")
print(user_info_copy == user_info_copied)
#   - 'is' will tell if both are same objects in the memory or different (similar to : '===' is JS)
print(user_info_copy is user_info_copied)

# fromkeys()
#   - creates keys-value pairs from comma separated values of iterable (list, strings)
#   - first argument if its iterable then each item in the iterable is the key and will be assigned the value(2nd param)
#   - will be called on a dictionary
#   - creates a new copy of dictionary and the original dict is not modified
print(f"dictionary method : fromkeys()")
# example 1
from_keys1 = {}.fromkeys("a", "b")
print(f"from_keys1 : {from_keys1}")  # from_keys1 : {'a': 'b'}

# example 2 : dict on which we are calling this method is not changed
dict_wont_change = {"name": "Guru"}
# dict_wont_change : {'name': 'Guru'}, from_keys2 : {'email': 'unknown', 'phone no': 'unknown'}
from_keys2 = dict_wont_change.fromkeys(["email", "phone no"], "unknown")
print(f"dict_wont_change : {dict_wont_change}, from_keys2 : {from_keys2}")

# example 3 : each iterable item is assigned the value
# from_keys4 : {'e': 'unknown', 'm': 'unknown', 'a': 'unknown', 'i': 'unknown', 'l': 'unknown'}
from_keys3 = {}.fromkeys("email", "unknown")
print(f"from_keys3 : {from_keys3}")

# example 4 : using dict
from_keys4 = dict.fromkeys("email", "unknown")
# from_keys4 : {'e': 'unknown', 'm': 'unknown', 'a': 'unknown', 'i': 'unknown', 'l': 'unknown'}
print(f"from_keys4 : {from_keys4}")

# example 5 : using range
from_keys5 = dict.fromkeys(range(1, 11), "unknown")
# from_keys5 : {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}
print(f"from_keys5 : {from_keys5}")


# get()
#   - retrives the value for that key
#   - If the key is not there it will return 'None' and will not throw 'KeyError'
#   - earlier we are using 'in' to check if there is key in list of values from dict.keys() as dict['no_key] will throw KeyError
print(f"*****dictionary method : get()*****")
dict1 = dict(a=1, b=2, c=3)
print(dict1['a'])  # 1
print(dict1.get('a'))  # 1
print(dict1.get('no_key'))  # returns 'None'
# print(dict1['no_key']) --> KeyError

# pop()
#   - pops the item(key,val pair) whose key is passed(key should be passed (mandatory) or we get TypeError)
#   - returns the value for the key
#   - KeyError if non existing key is passed
print(f"*****dictionary method : pop()*****")
dict2 = dict(a=1, b=2, c=3)
# d.pop() --> key should be passed (mandatory) or we get TypeError
print(dict2.pop('c'))  # 3
# print(dict2.pop('error'))  # KeyError
print(dict2)

# popitem()
#   - removed random item(key,value pair) from the dictionary
#   - no need to pass argument
#   - retuns the key,val pair that is removed
print(f"*****dictionary method : popitem()*****")
dict3 = dict(a=1, b=2, c=3)
print(f"dict3.popitem() : {dict3.popitem()}")  # ('c', 3)
print(f"dict3.popitem() : {dict3.popitem()}")  # ('b', 2)
print(f"dict3 : {dict3}")  # {'a': 1}

# update()
#   - add/update items from the passed list to the base dict
#   - passed dict is not changed
#   - base dict : if keys are present in passed dict and base dict then the values are updated in the base dict
#   - if we pass empty dict, it will not remove the items from the base dict
print(f"*****dictionary method : update()*****")
passing_dict = dict(a=10, b=20, c=30)
base_dict = dict(a=1, d=2, e=3)
base_dict.update(passing_dict)
base_dict.update({})  # passing empty dict will not remove the items
print(f"passing_dict : {passing_dict}, base_dict : {base_dict}")
