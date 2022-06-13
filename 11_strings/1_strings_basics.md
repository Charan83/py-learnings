# String 
- are ordered sequesnces
- can use indexing and slicing to grab sub-sections of the string
- In Python both positve and negative index are allowed
  - [-1] : last character in the string
  - [1] : first character in the string
- slicing : [start, stop, step]
  - stop is not including
- \n : newline
- \t : tab
- len : length of string

# Indexing and Slicing with Strings
```py
my_string = "hello World"
print(my_string[-1]) # d

print(my_string[6:]) # World
print(my_string[:5]) # hello
print(my_string[2:5]) # llo
my_new_str = my_string[::] # cloning the string
print(my_string is my_new_str) 
print(my_string == my_new_str)
print(f"my_new_str : {my_new_str}")
my_new_str = "change String"
print(f"my_new_str after change: {my_new_str}")
print(f"my_string : {my_string}")

# Reverse the string [::-1]
print(my_string[::-1]) # dlroW olleh

# Ex :String Slicing
str = "tinker"
print(str[1:4])
```

# String Properties and Methods
## String are immutable 
- cannot be changed after its created
- when we assign a new val to string, it will create a completely new string object
