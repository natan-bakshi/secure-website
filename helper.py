import sqlite3
import uuid
BAD_CHARS = {" ", "'", '"', ';', '-','--', '<', '>','/', '=', ';'}


def print_users():
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        print(user)
    connection.close()

# def check_db():
#     connection = sqlite3.connect('users.db')
#     c = connection.cursor()
#     c.execute("SELECT username FROM users WHERE username = dd%09DROP%09TABLE%09users)
#     user = c.fetchone()
#
#     connection.close()

def check_user(username):
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT username FROM users WHERE username = ?", (username,))
    user = c.fetchone()

    connection.close()

    if user:
        return True
    return False

def check_characters(string):
    if any(bad_char in string for bad_char in BAD_CHARS):
        return False
    return True


def check_user_login(username, password):

    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_password = c.fetchone()

    connection.close()

    if user_password and user_password[0] == password:
        return True
    return False


def create_user(username, password):
    connection = sqlite3.connect('users.db')
    c = connection.cursor()

    sql_execute_string = "INSERT INTO users(Uid, username, password) VALUES (?, ?, ?)"
    user_id = str(uuid.uuid4())

    c.execute(sql_execute_string, (user_id, username, password))
    connection.commit()
    connection.close()


print_users()