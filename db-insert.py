import sqlite3


db_local = 'users.db'


connection = sqlite3.connect(db_local)
c = connection.cursor()


c.execute("""
INSERT INTO users (username, password) VALUES
('natan test', 1234)
""")

connection.commit()
connection.close()

