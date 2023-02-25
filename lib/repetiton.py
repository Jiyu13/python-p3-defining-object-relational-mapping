# 1. import sqlite3
import sqlite3

# 2. connect to database and create a cursor
db_connecttion = sqlite3.connect(db/pets.db)
db_cursor = db_connection.cursor()


# 3. Write CREATE queries and execute them with cursor
cats_query = "CREATE TABLE IF NOT EXISTS cats(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)"
owners_query = "CREATE TABLE IF NOT EXISTS owners(id INTEGER PRIMARY KEY, name TEXT)"
db_cursor.execute(cats_query)
db_cursor.execute(owners_query)


# insert new cats and owners into these tables suing .execute() built-in method
db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Maru', 'scottish fold', 3)")

db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Hana', 'tortoiseshell', 1)")