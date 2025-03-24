from flask import Flask, render_template
from flask import request
from helper import *

app = Flask(__name__)


@app.route('/')
@app.route('/wellcome')
def wellcome_page():
    return render_template('wellcome.html')


@app.route('/SignUp', methods=['post', 'get'])
def sign_up():
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if not check_characters(username):
            error_message = "Unauthorized characters"
        elif not username and password1 and password2:
            error_message = "Please fill in all fields"
        elif not password1 == password2:
            error_message = "Mismatched passwords"
        elif check_user(username):
            error_message = "Username taken"
        else:
            print("well done")
            create_user(username, password1)
            return render_template('home.html')

    return render_template('sign_up.html', message = error_message)


@app.route('/Login', methods=['post', 'get'])
def log_in():
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not check_characters(username):
            error_message = "you are very naughty"

        elif not check_user_login(username, password):
            error_message = "The username or password is incorrect"

        else:
            return render_template('home.html')

    return render_template('log_in.html',message = error_message)


if __name__ == '__main__':
    app.run(debug=True)
