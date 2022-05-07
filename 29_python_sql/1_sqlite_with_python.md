#   Open existing DB and create Table
#       - .open dogs_db.db
#       - CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);
#       - .tables

#   Creating DB and a Table
#       - sqlite3 cats_db.db
#       - CREATE TABLE cats (name TEXT, breed TEXT, age INTEGER);

#   Inserting into a table from a file (2_basic.sql)
#       - to run the sql commands in the file, use '.read <2_basic.sql>

#   Connecting to a DB with Python
#       - https://docs.python.org/3/library/sqlite3.html#module-sqlite3
#       - we can use the python module sqlite3 which comes by default with python
#       - import sqlite3 --> create connection to the DB --> create a cursor object on that connection --> and call the execute method
