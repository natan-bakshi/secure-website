import sqlite3


db_local = 'users.db'


connection = sqlite3.connect(db_local)
c = connection.cursor()


c.execute("""
CREATE TABLE IF NOT EXISTS users 
(Uid TEXT UNIQUE NOT NULL,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
) 
""")

connection.commit()
connection.close()

