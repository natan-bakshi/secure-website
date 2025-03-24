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
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']
        if check_characters(password1):
            if username and password1 and password2:
                if password1 == password2:
                    if not check_user(username):
                        create_user(username, password1)
                        return render_template('home.html')
                    else:
                        return "Username taken"
                return "Mismatched passwords"
            return "Please fill in all fields"
        return
    return render_template('sign_up.html')


@app.route('/Login', methods=['post', 'get'])
def log_in():
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not check_characters(password):
            error_message = "you ar very naughty"

        elif  not check_user_login(username, password):
            error_message = "The username or password is incorrect"

        else:
            return render_template('home.html')

    return render_template('log_in.html',message = error_message)




if __name__ == '__main__':
    app.run(debug=True)
