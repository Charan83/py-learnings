'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

"""
    accepts a string
    returns a dictionary with the keys as the vowels and values as the count of times that vowel appear in the string
"""


def vowel_count(str):
    str = str.lower()
    return {ch: str.count(ch) for ch in str if ch in 'aeiou'}


print('strstr'.count('s'))
print(vowel_count('Gurucharan'))
print(vowel_count('awesome'))
print(vowel_count('Elie'))
