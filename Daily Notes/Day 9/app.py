from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
app.secret_key = 'QWErghuytrerTGHjuYTGFHyt'

class User:
    def __init__(self, username, password, first_name, last_name):
        self.username = username #username
        self.password = password # password
        self.first_name = first_name # String
        self.last_name = last_name # String

    def add(self):
        #TODO: check if user in database
        with open('users.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.username, self.password, self.first_name, self.last_name])


    @staticmethod
    def get_by_username(username):
        with open('users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (len(row) != 0):
                    if (username == row[0]):
                        user = User(row[0], row[1], row[2], row[3])
                        return user
            return None

    @staticmethod
    def all():
        users = []
        with open('users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                users.append(User(row[0], row[1], row[2],row[3]))
        return users

class Twit:
    def __init__(self, owner, content):
        self.owner = owner #owner-> User
        self.content = content # String
        

    @staticmethod
    def get_by_owner(owner):
        twits = []
        with open('twits.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (len(row) != 0):
                    if (owner == row[0]):
                        twit = Twit(row[0], row[1])
                        twits.append(twit)
            return twits

    @staticmethod
    def add(username, content):
        with open('twits.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([username, content])


# <------ Pages BEGIN -------->

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        uname = request.form.get('username')
        pswd = request.form.get('password')
        user = User.get_by_username(uname)
        if (not user):
            render_template('login.jinja')
        else:
            if (pswd == user.password):
                session['user'] = [user.username, user.first_name, user.last_name]
                return redirect(url_for('profile'))
    return render_template('login.jinja')

@app.route('/register', methods = ['GET', 'POST'])
def register():

    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        user = User(username, password, fname, lname)
        user.add()
        return redirect(url_for('login'))
        
    return render_template('register.jinja')

@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    if (not session.get('user')):
        return redirect(url_for('index'))


    uname = session.get('user')[0]
    twits = Twit.get_by_owner(uname)
    
    if (request.method == 'POST'):
        content = request.form.get('content')
        Twit.add(uname,content)
        return redirect(url_for('profile'))

    return render_template('profile.jinja', twits = twits)

@app.route('/users')
def users():
    if (not session.get('user')):
        return redirect(url_for('index'))
    all_users = User.all()
    return render_template('users.jinja', users = all_users)

@app.route('/users/<username>')
def user(username):
    if (not session.get('user')):
        return redirect(url_for('index'))
    my_user = User.get_by_username(username)
    twits = Twit.get_by_owner(my_user.username)
    return render_template('user.jinja', twits = twits, user = my_user)

@app.route('/logout')
def logout():
    if (not session.get('user')):
        return redirect(url_for('index'))
    session['user'] = None
    return redirect(url_for('index'))
# <------ Pages END -------->

if __name__ == '__main__':
    app.run()