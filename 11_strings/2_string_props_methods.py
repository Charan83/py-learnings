# String are immutable 
#   - cannot be changed after its created
#   - when we assign a new val to string, it will create a completely new string object

str = "stRing propeRties aNd metHods"
print(str.upper())
print(str.lower())
str_split = str.split() # default split by whitespace ' '
print(f"str_split : {str_split}")