from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from Black_Jack import Card, Deck, Player, Game
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key = 'QWErghuytrerTGHjuYTGFHyt'
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    money = db.Column(db.Integer)

    def __repr__(self):
        return 'User: {}'.format(self.username)
    def __str__(self):
        return 'User: {}'.format(self.username)

    @staticmethod
    def get_by_username(username):
        users = User.query.all()
        for user in users:
            if user.username == username:
                ans = [user.username, user.password, user.email, user.money]
                return ans

@app.route('/', methods = ['POST', 'GET'])
def index():
    if (session.get('ans')):
        session.pop('ans', None)
    users = User.query.all()
    return render_template('index.jinja', users = users)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        email = request.form.get('email')

        check = False
        blank = False
        not_match = False
        both = False
        users = User.query.all()
        session['ans'] = 'Welcome'
        if (len(username) == 0 or len(password) == 0 or len(repassword) == 0 or len(email) == 0):
            session['ans'] = "Don't be lazy, please! You can't leave anything at blank"
            check = True
            blank = True
        if password != repassword:
            check = True
            not_match = True
            if blank:
                session['ans'] = "Password doesn't match AND you shouldn't leave anything blank"
            else:
                session['ans'] = "Password doesn't match!"
        for user in users:
            if (user.username):
                if user.username == username:
                    check = True
                    both = True
                    if blank and not_match:
                        session['ans'] = "Are you kidding me? Password doesn't match AND existing username AND you shouldn't leave anything blank"
                    elif blank:
                        session['ans'] = "Existing username AND you shouldn't leave anything blank"
                    elif not_match:
                        session['ans'] = "Password doesn't match AND you shouldn't leave anything blank"
                    else:
                        session['ans'] = 'Existing username'
                if user.email == email:
                    if both and blank and not_match:
                        session['ans'] = "Unbelieveable! Password doesn't match AND existing username AND email AND you shouldn't leave anything blank"
                        break
                    elif both and blank:
                        session['ans']= "Existing username AND email AND you shouldn't leave anything blank"
                    elif both and not_match:
                        session['ans'] = "Existing username AND email AND password doesn't match"
                    elif blank and not_match:
                        session['ans'] = "Password doesn't match AND existing email AND you shouldn't leave anything blank"
                    elif both:
                        session['ans'] = "Existing username AND email"
                    elif blank:
                        session['ans'] = "Existing email AND you shouldn't leave anything blank"
                    elif not_match:
                        session['ans'] = "Existing email AND password doesn't match"
                    else:
                        check = True
                        session['ans'] = 'Existing email'
        if check:
            return redirect(url_for('register'))
        else:
            user = User(username = username, password = password, email = email, money = 0)
            db.session.add(user)
            db.session.commit()
            session.pop('ans', None)
            session.pop('login_user, None')
            return redirect(url_for('login'))
    return render_template('register.jinja')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if (session.get('login_user')):
        return redirect(url_for('profile'))
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.get_by_username(username)
        if (not user):
            render_template('login.jinja')
        else:
            if (password == user[1]):
                session['login_user'] = [user[0], user[2], user[3]]
                return redirect(url_for('profile'))
            else:
                return redirect(url_for('login'))
    return render_template('login.jinja')


@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    if (not session.get('login_user')):
        return redirect(url_for('index'))
    if (request.method == 'POST'):
        player = Player()
        game = Game(player)
        # TODO: the following function doesn't work
        if request.form.get('change'):
            change = request.form.get('amount_change')
            try:
                user = User.query.filter_by(username = session.get('login_user')[0]).first()
                user.money += int(change)
                session.commit()
            except:
                session['error'] = 'Input must be integer'
                return redirect(url_for('profile'))
        elif request.form.get('exit'):
            session.pop('login_user', None)
            return redirect(url_for('login'))
        elif request.form.get('add'):
            session["cards"] = game.turn()
        # elif request.form.get('done'):
         
    return render_template('profile.jinja')


# db.create_all() : Delete after first time use
if __name__ == '__main__':
    app.run()