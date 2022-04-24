#   task 1 : State Abbreviations Exercise
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}
answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# answer: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}
print(f"answer : {answer}")


#   task 2 : List to Dictionary Exercise
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer1 = {item[0]: item[1] for item in person}
# answer1 with dictionary comprehension : {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
print(f"answer1 with dictionary comprehension : {answer1}")
answer2 = {k: v for k, v in person}
# answer2 with dictionary comprehension without using index : {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
print(f"answer2 with dictionary comprehension without using index : {answer2}")
answer3 = dict(person)
# If you have a list of pairs, you can very easily turn it into a dictionary using dict : {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
print(
    f"If you have a list of pairs, you can very easily turn it into a dictionary using dict : {answer3}")


#   task 3 : Vowels Dict Exercise
vowels = 'aeiou'
answer_vowels = {}.fromkeys(vowels, 0)
# answer_vowels, {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print(f"answer_vowels, {answer_vowels}")
answer_vowels1 = {ch: 0 for ch in vowels}
# with dictionary comprehension answer_vowels1:  {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
print(f"with dictionary comprehension answer_vowels1 : {answer_vowels1}")

#   task 3 : ASCII Codes Dictionary
ascii_dict = {num: chr(num) for num in range(65, 91)}
# ASCII code dict ascii_dict: {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}
print(f"ASCII code dict ascii_dict: {ascii_dict}")
