user_info = {
    "Student Name": "Guru",
    "Grade": 'A',
    "Score": 911,
    35: 'address'
}

#   checking key exists
if 'Grade' in user_info:
    print(f"Grade key exists : {user_info['Grade']}")
if 'Grades' in user_info:  # This condition is failed
    print(f"Grades key DOES NOT exists! : {user_info['Grades']}")

#   checking val exists
if 'Guru' in user_info.values():
    print(
        f"The Value 'Guru' Exists and the Student name is : {user_info['Student Name']}")
