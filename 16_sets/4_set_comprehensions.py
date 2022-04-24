# set comprehension
#   - similar to dictionary comprehension but it will have only one val and not key,val

# example 1
set1 = {1, 2, 3, 4, 5, 6, 7}
set_even = {num for num in set1 if num % 2 == 0}
# set_even : {2, 4, 6}, type of set_even : <class 'set'>
print(f"set_even : {set_even}, type of set_even : {type(set_even)}")
dict_even = {num: num for num in set1 if num % 2 == 0}
# dict_even : {2: 2, 4: 4, 6: 6}, type of dict_even : <class 'dict'>
print(f"dict_even : {dict_even}, type of dict_even : {type(dict_even)}")


# example 2
set2 = {num**2 for num in range(1, 9)}
print(f"set2 : {set2}")

# example 3
set3 = {ch for ch in 'hello'}
# as its set the values come out of set comprehension will only stay in set if its unique: {'e', 'l', 'h', 'o'}
print(
    f"as its set the values come out of set comprehension will only stay in set if its unique: {set3}")

# example 4 : how many unique vowels are there in a string
str1 = "Gurucharan"
vowels_count = len({ch for ch in str1 if ch in 'aeiou'})
print(f"unique vowels count in the given string using set : {vowels_count}")
