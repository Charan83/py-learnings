#   values() : Accessing all values in a Dictionary
user_info = {
    "Student Name": "Guru",
    "Grade": 'A',
    "Score": 911,
    35: 'address'
}
for val in user_info.values():
    print(val)

#    keys() : Accessing all keys in a Dictionary
for key in user_info.keys():
    print(key)

#   items() : Accessing all key,values in a Dictionary
for key, val in user_info.items():
    print("key:{} - val:{}".format(key, val))
