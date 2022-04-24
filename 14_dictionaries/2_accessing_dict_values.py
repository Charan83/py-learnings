instructor = {
    "name": "Guru",
    "num_of_courses": 4,
    35: "apartment number"
}

#   - we access the values almost in the same way as list
#   - but here instead of index, we use key
print(f"The value for key 'name' is : {instructor['name']}")

#   - we get KeyError, when we look for a key that doesn't exists
print(
    f"Error when we look for something that doesn't exists : {instructor['names']}")
