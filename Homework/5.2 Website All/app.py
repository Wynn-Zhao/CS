from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key = 'QWErghuytrerTGHjuYTGFHyt'
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    money = db.Column(db.Float)
    stocks = db.Column(db.String(120))

    def __repr__(self):
        return 'User: {}'.format(self.username)
    def __str__(self):
        return 'User: {}'.format(self.username)

    @staticmethod
    def get_by_username(username):
        users = User.query.all()
        for user in users:
            if user.username == username:
                ans = [user.username, user.password, user.email, user.money, user.stocks]
                return ans

@app.route('/', methods = ['POST', 'GET'])
def index():
    if (session.get('ans')):
        session.pop('ans', None)
    users = User.query.all()
    return render_template('index.jinja', users = users)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if (session.get('login_user')):
        return redirect(url_for('profile'))
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
                        session['ans'] = "Existing username AND you shouldn't leave anything blank"
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
            user = User(username = username, password = password, email = email, money = 0, stocks = '')
            db.session.add(user)
            db.session.commit()
            session.pop('ans', None)
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
            return render_template('login.jinja', message = 'Username does not exist!')
        else:
            if (password == user[1]):
                session['login_user'] = [user[0], user[2], user[3], user[4]]
                return redirect(url_for('profile'))
            else:
                return render_template('login.jinja', message = 'Password does not match!')
    return render_template('login.jinja')


@app.route('/profile', methods = ['POST', 'GET'])
def profile():
    if (not session.get('login_user')):
        return redirect(url_for('index'))
    user = User.query.filter_by(username = session.get('login_user')[0]).first()
    session['login_user'] = [user.id, user.username, user.money, user.stocks]
    n = 0
    message_2 = ''
    stocks_info = {}

    if not session.get('login_user')[3]:
        message_2 = "You don't have any stock in hand"
    else:
        x = session.get('login_user')[3].split('!@#$%')
        y = len(x) - 1
        n = int(y/2)
        session['stocks_name'] = []
        session['stocks_shares'] = []
        for i in range(y):
            if i%2 == 0:
                session.get('stocks_name').append(x[i])
            else:
                session.get('stocks_shares').append(x[i])
        for i in range(n):
            stocks_info[session.get('stocks_name')[i]] = float(session.get('stocks_shares')[i])

    if (request.method == 'POST'):
        if request.form.get('change'):
            change = request.form.get('amount_change')
            try:
                user = User.query.filter_by(username = session.get('login_user')[0]).first()
                if float(change) < 0 and user.money < 0 - float(change):
                    return render_template('profile.jinja', message_1 = "You know you don't have this much money in your account?", n = n)
                else:
                    user.money += float(change)
                    db.session.commit()
                    session.get('login_user')[2] = user.money
            except:
                return render_template('profile.jinja', message_1 = 'Input must be a number!', n = n)

        if request.form.get('search'):
            lnkd = request.form.get('LNKD')
            if len(lnkd) != 4:
                return render_template('profile.jinja', message_3 = 'LNKD symbol must be 4 characters', n = n)
            else:
                price = random.randint(1, 100)
                return render_template('profile.jinja', message_3 = 'Price for ' + str(lnkd) + ': ', message_3_1 = str(price), n = n)

        if request.form.get('buy'):
            lnkd_buy = request.form.get('LNKD_buy')
            shares_buy = request.form.get('shares_buy')
            try:
                float(shares_buy)
            except:
                return render_template('profile.jinja', message_4 = 'The amount money invested must be a positive number', n = n)
            if len(lnkd_buy) != 4:
                return render_template('profile.jinja', message_4 = 'LNKD symbol must be 4 characters', n = n)
            elif float(shares_buy) <= 0:
                return render_template('profile.jinja', message_4 = 'The amount money invested must be a positive number', n = n)
            elif float(shares_buy) > session.get('login_user')[2]:
                return render_template('profile.jinja', message_4 = 'You are too poor to afford this investment', n = n)
            else:
                shares_buy = float(shares_buy)
                price = random.randint(1, 100)
                shares = shares_buy / price
                user = User.query.filter_by(username = session.get('login_user')[0]).first()
                user.money -= shares_buy
                session.get('login_user')[2] = user.money
                check_1 = False
                for i in stocks_info:
                    if i == lnkd_buy:
                        check_1 = True
                        break
                if check_1:
                    user.stocks = ''
                    session['stocks_name'] = []
                    session['stocks_shares'] = []
                    stocks_info[lnkd_buy] += shares
                    for i in stocks_info:
                        session.get('stocks_name').append(i)
                        session.get('stocks_shares').append(stocks_info[i])
                        user.stocks += str(i) + '!@#$%' + str(stocks_info[i]) + '!@#$%'
                        session.get('login_user')[3] = user.stocks
                        db.session.commit()
                else:
                    user.stocks += str(lnkd_buy) + '!@#$%' + str(shares) + '!@#$%'
                    db.session.commit()
                    session.get('login_user')[3] = user.stocks
                    n += 1
                    session.get('stocks_name').append(lnkd_buy)
                    session.get('stocks_shares').append(shares)
                    stocks_info[lnkd_buy] = float(shares)
                return render_template('profile.jinja', message_4 = str(price), message_4_1 = str(shares), message_4_2 = str(lnkd_buy), n = n)


        elif request.form.get('exit'):
            session.pop('login_user', None)
            return redirect(url_for('login'))

    return render_template('profile.jinja', message_2 = message_2, n = n)



if __name__ == '__main__':
    # db.create_all()
    app.run()