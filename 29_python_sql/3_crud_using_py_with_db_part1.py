import sqlite3

conn = sqlite3.connect("my_friends.db")

#   create cursor object
#   cursor is a temporory workspace/memory for executing sql commands, and then we can commit those using connection
cursor = conn.cursor()

sql_cmd_create_table = "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);"
sql_cmd_insert_data = "INSERT INTO friends (first_name, last_name, closeness) VALUES ('Guru', 'Charan', 10) ;"

#   Better way to write queries
data = ('Steve', 'Trwin', 9)
insert_query = "INSERT INTO friends VALUES (?, ?, ?)"
#   execute the sql cmd
#   cursor.execute(sql_cmd_create_table)
cursor.execute(sql_cmd_insert_data)
cursor.execute(insert_query, data)

#   Bulk Insert
people = [
    ("Rohit", "Sharma", 5),
    ("MS", "Dhoni", 8),
    ("Virat", "Kholi", 4),
    ("Ambati", "Rayudu", 3),
    ("Kapil", "Dev", 9)
]

#   executemany : runs the query for each item in the array
cursor.executemany("INSERT INTO friends VALUES(?, ?, ?)", people)

#   we can loop ourself, if there is some logic to be done
for person in people:
    cursor.execute("INSERT INTO friends VALUES(?, ?, ?)", person)

#   select the data
cursor.execute("SELECT * FROM friends")

#   commit changes
conn.commit()

conn.close()
