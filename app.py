from flask import Flask, render_template
from flask import request, redirect, url_for
import sqlite3
import uuid


BAD_CHARS = {' ', "'", '"', ';', '--', '<', '>','/', '='}
app = Flask(__name__)

import sqlite3

def print_users():
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for user in users:
        print(user)
    connection.close()


def check_user(username):
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT username FROM users WHERE username = ?", (username,))
    user = c.fetchone()

    connection.close()

    if user:
        return True
    return False

def check_user_login(username, password):
    if any(bad_char in password for bad_char in BAD_CHARS):
        return "Password contains invalid characters"

    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user_password = c.fetchone()

    connection.close()

    if user_password and user_password[0] == password:
        return True
    return False


def create_user(username, password):
    if any(bad_char in password for bad_char in BAD_CHARS):
        return "Password contains invalid characters"

    connection = sqlite3.connect('users.db')
    c = connection.cursor()

    sql_execute_string = "INSERT INTO users(Uid, username, password) VALUES (?, ?, ?)"
    user_id = str(uuid.uuid4())

    c.execute(sql_execute_string, (user_id, username, password))
    connection.commit()
    connection.close()



@app.route('/')
@app.route('/wellcome')
def wellcome_page():
    return render_template('wellcome.html')


@app.route('/SignUp', methods=['post', 'get'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if username and password1 and password2:
            if password1 == password2:
                if not check_user(username):
                    create_user(username, password1)
                    return render_template('home.html')
                else:
                    return "Username taken"
            return "Mismatched passwords"
        return "Please fill in all fields"
    return render_template('sign_up.html')


@app.route('/Login', methods=['post', 'get'])
def log_in():
    print(request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_user_login(username, password):
            return render_template('home.html')
        return "Incorrect username or password"
    else:
        return render_template('log_in.html')



# def query_contact_details():
#     connie = sqlite3.connect(db_locale)
#     c = connie.cursor()
#     c.execute("""
#     SELECT * FROM contact_details
#     """)
#     student_data = c.fetchall()
#     return student_data


if __name__ == '__main__':
    app.run(debug=True)
