from flask import Flask, render_template
import csv
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/register')
def register():
    return render_template('register.jinja')

@app.route('/login')
def login():
    return render_template('login.jinja')

@app.route('/users')
def username():
    users = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            user = User(fname = row[0], lname = row[1], nname = row[2], email = row[3])
            users.append(user)

    return render_template('users.jinja', users = users)



if __name__ == '__main__':
   app.run()