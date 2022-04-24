# dictionaries
#   - dictionaries are key, value pairs and list are ordered list of elements
#   - key, value pairs
#   - keys can only be strings/numbers
#   - values can be anything

# example 1 : simple dictionary (object in js)
instructor = {
    "name": "Guru",
    "num_of_courses": 4,
    35: "apartment number"
}
print(f"instructor : {instructor}")

# example 2 : list of dictionary items
cart = [
    {
        "name": "Learning Python",
        "price": 99
    },
    {
        "name": "Learning GCP",
        "price": 999
    },
]
print(f"cart : {cart}")

# example 3 : another way to create dictionary is using dict
using_dict = dict(name="Learning JS", price=99)
print(f"using dict to create dictionary : {using_dict}")
