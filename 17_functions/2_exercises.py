#   Ex1
'''
product(2,2) # 4
product(2,-2) # -4
'''

# define product below:


from tkinter.messagebox import NO


def product(num1, num2):
    return num1 * num2


#   Ex2
'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
days_of_week = {1: "Sunday", 2: "Monday", 3: "Tuesday",
                4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}


def return_day(week_day_num):
    week_day = days_of_week.get(week_day_num)
    if week_day:
        return week_day
    return None


print(f"return_day(41) # None : {return_day(41)}")
print(f"return_day(7) # Saturday : {return_day(7)}")


#   Ex 3
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(lst):
    if not lst:                # len(lst) == 0:  empty list is falsy value
        return None
    return lst[len(lst)-1]


print(f"last_element([1,2,3]) # 3 : {last_element([1,2,3])}")
print(f"last_element([]) # None : {last_element([])}")


#   Ex 4
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(num1, num2):
    if num1 == num2:
        return 'Numbers are equal'
    elif num1 > num2:
        return 'First is greater'
    else:
        return 'Second is greater'


print(f"number_compare(1,1) # Numbers are equal: {number_compare(1,1)}")


#   Ex5
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# define single_letter_count below:


def single_letter_count(word, char):
    return word.upper().count(char.upper())


print(single_letter_count("Hello World", "h"))
print(single_letter_count("Hello World", "z"))


#   Ex6
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:


def multiple_letter_count(str):
    return {ch: str.count(ch) for ch in str}


print(multiple_letter_count("awesome"))


#   Ex7
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation():
    pass
