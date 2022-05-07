#   for selecting the data from the table, we want to capture the result

import sqlite3

conn = sqlite3.connect("./my_friends.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM friends")

#   Cursor object is an iterator so We can Iterate over
print("******Iterate over cursor object***********")
for c in cursor:
    print(c)    # each time we get one row as tuple : ('Guru', 'Charan', 10)

print("******Using fetchall()***********")
cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
""" [('MS', 'Dhoni', 8), ('MS', 'Dhoni', 8), ('MS', 'Dhoni', 8), ('Steve', 'Trwin', 9), ('Steve', 'Trwin', 9), ('Kapil', 'Dev', 9), ('Steve', 'Trwin', 9), ('Kapil', 'Dev', 9), ('Kapil', 'Dev', 9), ('Guru', 'Charan', 10), ('Guru', 'Charan', 10), ('Guru', 'Charan', 10), ('Guru', 'Charan', 10)] """
print(cursor.fetchall())
# the cursor will be empty,  after we iterate over it as its a generator
print(cursor.fetchall())

print("******Using fetchone()***********")
cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
#   ('MS', 'Dhoni', 8)
print(cursor.fetchone())

print("******Using fetchmany()***********")
cursor.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
#   [('MS', 'Dhoni', 8)]
print(cursor.fetchmany())
