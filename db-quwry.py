import sqlite3


db_local = 'users.db'


connection = sqlite3.connect(db_local)
c = connection.cursor()


c.execute("""
SELECT * FROM users
""")

info = c.fetchall()
for user in info:
    print(user)

connection.commit()
connection.close()

