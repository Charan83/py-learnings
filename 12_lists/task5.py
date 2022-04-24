instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
# Added items to list : ['Colt', 'Blue', 'Lisa']
print(f"Added items to list : {instructors}")

# removing the last item from the list - Lisa
print(f"removing the last item from the list - {instructors.pop()}")
# list after removing the last item : ['Colt', 'Blue']
print(f"list after removing the last item : {instructors}")

# removing the first item from the list : Colt
print(f"removing the first item from the list : {instructors.pop(0)}")
# list after removing the first item : ['Blue']
print(f"list after removing the first item : {instructors}")

{instructors.insert(0, 'Done')}
# after adding 'Done' at position 0 to the list: ['Done', 'Blue']
print(f"after adding 'Done' at position 0 to the list : {instructors}")
