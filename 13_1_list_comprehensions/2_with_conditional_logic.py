# example 1 : even/odd
# if :  then it will come at the end
nums = list(range(1, 15))
evens = [num for num in nums if num % 2 == 0]
odds = [num for num in nums if num % 2 != 0]
print(f"evens : {evens}, odds : {odds}")

# example 2 : if-else
nums_if_else = list(range(1, 20))
result = [num*2 if num % 2 == 0 else num/2 for num in nums_if_else]
print(f"result : {result}")

# example 3 : if with string
with_vowels = "This is so much fun"
without_vowels = "".join([ch for ch in with_vowels if ch not in 'aeiou'])
print(f"without_vowels : {without_vowels}")

# example 4 : if-else with string
with_vowels = "This is so much fun"
without_vowels = "".join(
    [ch if ch not in 'aeiou' else '€' for ch in with_vowels])
print(f"without_vowels : {without_vowels}")
