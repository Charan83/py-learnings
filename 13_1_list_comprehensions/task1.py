# task 1
list1 = ["Elie", "Tim", "Matt"]
list1_updated = [item[0] for item in list1]
print(f"list1_updated : {list1_updated}")

# task 2
nums = list(range(1, 7))
evens = [n for n in nums if n % 2 == 0]
print(f"evens : {evens}")

# task3 : intersection from 2 lists
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
answer = [val for val in lst1 if val in lst2]
print(f"answer : {answer}")

# task 4 : reverse the items in the list
names = ["Elie", "Tim", "Matt"]
reverse_names = [name[:0:-1]+name[0].lower() for name in names]
print(f"reverse_names : {reverse_names}")

# task 5 :
nums_12 = list(range(1, 101))
div_12 = [num for num in nums_12 if num % 12 == 0]
print(f"div_12 : {div_12}")

# task 6 :
str_amazing = "amazing"
no_vowels = [ch for ch in str_amazing if ch not in 'aeiou']
print(f"no_vowels : {no_vowels}")
