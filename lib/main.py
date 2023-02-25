import sqlite3

class Cat:

    all = []

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_all(self)

    
    # will add each cat instance to all when initialise this cat
    @classmethod
    def add_cat_to_all(cls, cat):
        cls.all.append(cat)

    
    # insert cat records into databse
    def save(self, cursor):
        cursor.execute(
            'INSERT INTO cats (name, breed, age) VALUES (?, ?, ?)',
            (self.name, self.breed, self.age)
        )

        # commit() to modify data for tables
        # to conform the changes made to the db
        db_connection.commit()



# connect to database and create a cursor
db_connection = sqlite3.connect("../db/pets.db")
db_cursor = db_connection.cursor()


#  create cat instances, initialise name, breed, age attributes
Cat("Maru", "scottish fold", 3)
Cat("Hana", "tortoiseshell", 1)

for cat in Cat.all:
    # execute db_cursor in save() instance method
    cat.save(db_cursor)



# create cats table first 
# sqlite> create table cats (
#    ...> id integer primary key,
#    ...> name text,
#    ...> breed text,
#    ...> age integer
#    ...> );