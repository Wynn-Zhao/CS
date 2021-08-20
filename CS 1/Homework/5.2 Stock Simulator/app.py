from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from utils import check_password, decode_stocks_dict, stock_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
app.secret_key = 'QWErghuytrerTGHjuYTGFHyt'
 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    money = db.Column(db.Float)
    stocks = db.Column(db.String(120))

    def __repr__(self):
        return 'User: {}'.format(self.username)
    def __str__(self):
        return 'User: {}'.format(self.username)

    def get_stocks(self):
        stocks_list = self.stocks.split('!@#$%')
        stocks_dict = {}
        for i in range(0, len(stocks_list) - 2, 2):
            stocks_dict[stocks_list[i]] = stocks_list[i+1]
        return stocks_dict

    @staticmethod
    def get_by_username(username):
        users = User.query.all()
        for user in users:
            if user.username == username:
                ans = [user.username, user.password, user.email, user.money, user.stocks]
                return ans


@app.route('/', methods = ['POST', 'GET'])
def index():
    users = User.query.all()
    return render_template('index.jinja', users = users)

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if (session.get('login_user')):
        return redirect(url_for('portfolio'))
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
        ans = 'Welcome'
        if (len(username) == 0 or len(password) == 0 or len(repassword) == 0 or len(email) == 0):
            ans = "Don't be lazy, please! You can't leave anything at blank"
            check = True
            blank = True
        if password != repassword:
            check = True
            not_match = True
            if blank:
                ans = "Password doesn't match AND you shouldn't leave anything blank"
            else:
                ans = "Password doesn't match!"
        for user in users:
            if (user.username):
                if user.username == username:
                    check = True
                    both = True
                    if blank and not_match:
                        ans = "Are you kidding me? Password doesn't match AND existing username AND you shouldn't leave anything blank"
                    elif blank:
                        ans = "Existing username AND you shouldn't leave anything blank"
                    elif not_match:
                        ans = "Existing username AND you shouldn't leave anything blank"
                    else:
                        ans = 'Existing username'
                if user.email == email:
                    check = True
                    if both and blank and not_match:
                        ans = "Unbelieveable! Password doesn't match AND existing username AND email AND you shouldn't leave anything blank"
                        break
                    elif both and blank:
                        ans= "Existing username AND email AND you shouldn't leave anything blank"
                    elif both and not_match:
                        ans = "Existing username AND email AND password doesn't match"
                    elif blank and not_match:
                        ans = "Password doesn't match AND existing email AND you shouldn't leave anything blank"
                    elif both:
                        ans = "Existing username AND email"
                    elif blank:
                        ans = "Existing email AND you shouldn't leave anything blank"
                    elif not_match:
                        ans = "Existing email AND password doesn't match"
                    else:
                        ans = 'Existing email'
        if check:
            return render_template('register.jinja', ans = ans)
        else:
            if check_password(password):
                user = User(username = username, password = password, email = email, money = 0, stocks = '')
                db.session.add(user)
                db.session.commit()
                session.pop('ans', None)
                return redirect(url_for('login'))
            else:
                ans = 'Password must include 7 ~ 20 elements, at least 1 number, 1 capital letter, and 1 lower-case letter'
                return render_template('register.jinja', ans = ans)
    return render_template('register.jinja', ans = ans)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if (session.get('login_user')):
        return redirect(url_for('portfolio'))
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.get_by_username(username)
        if (not user):
            return render_template('login.jinja', message = 'Username does not exist!')
        else:
            if (password == user[1]):
                # username
                session['login_user'] = user[0] 
                return redirect(url_for('portfolio'))
            else:
                return render_template('login.jinja', message = 'Password does not match!')
    return render_template('login.jinja')

@app.route('/find_stock', methods = ['GET', 'POST'])
def find_stock():
    user = User.query.filter_by(username = session.get('login_user')).first()
    if request.method == 'POST':
        if request.form.get('search'):
            ticker = request.form.get('find_ticker')
            stock = stock_data(ticker)
            if not stock:
                return render_template('find_stock.jinja', user = user, message = 'not_exist')
            else:
                return render_template('find_stock.jinja', user = user, info = stock['INFO'])
                # return render_template('stock.jinja', user = user, stock = stock)
                # TODO: I don't know why this would work though ... 
    else:
        return render_template('find_stock.jinja', user = user)

@app.route('/stock/<ticker>', methods = ['GET', 'POST'])
def stock(ticker):
    user = User.query.filter_by(username = session.get('login_user')).first()
    stocks = user.get_stocks()
    stock = stock_data(ticker)
    if request.method == 'POST':
        if request.form.get('buy'):
            shares_buy = request.form.get('amount_trade')
            try:
                shares_buy = float(shares_buy)
            except:
                return render_template('stock.jinja', user = user, stock = stock, message = 'Input must be a positive number')
            if shares_buy <= 0:
                return render_template('stock.jinja', user = user, stock = stock, message = 'Input must be a positive number')
            payment = stock['PRICE_BUY']*shares_buy
            if user.money < payment:
                return render_template('stock.jinja', user = user, stock = stock, message = 'You cannot afford this investment')
            try:
                stocks[ticker] = float(stocks[ticker]) + shares_buy
            except:
                stocks[ticker] = shares_buy
            user.stocks = decode_stocks_dict(stocks)
            user.money -= payment
            db.session.commit()
            return render_template('stock.jinja', user = user, stock = stock, message = 'Investment succeed! You invested ' + str(payment) + '$ to buy ' + str(shares_buy) + ' shares of ' + str(ticker) + ' at ' + str(stock['PRICE_BUY']) + '$/shares')

        if request.form.get('sell'):
            shares_sell = request.form.get('amount_trade')
            try:
                shares_sell = float(shares_sell)
                payment = stock['PRICE_SELL']*price
            except:
                return render_template('stock.jinja', user = user, stock = stock, message = 'Input must be a positive number')
            try:
                if float(stocks[ticker]) >= shares_sell:
                    stocks[ticker] = float(stocks[ticker]) - shares_sell
                else:
                    return render_template('stock.jinja', user = user, stock = stock, message = "You only have " + str(stocks[ticker]) + ", can't sell " + str(shares_sell) + ' amount of shares')
            except:
                return render_template('stock.jinja', user = user, stock = stock, message = str(ticker) + " is not in your portfolio")
            user.stocks = decode_stocks_dict(stocks)
            user.money += payment
            db.session.commit()
            return render_template('stock.jinja', user = user, stock = stock, message_sell = 'Trade succeed! You get ' + str(payment) + '$ by selling ' + str(shares_sell) + ' shares of ' + str(ticker) + ' at ' + str(stock['PRICE_SELL']) + '$/shares')

    return render_template('stock.jinja', user = user, stock = stock)

@app.route('/exit')
def exit():
    session.clear()
    return redirect(url_for('login'))

@app.route('/portfolio')
def portfolio():
    if (not session.get('login_user')):
        return redirect(url_for('index'))
    user = User.query.filter_by(username = session.get('login_user')).first()
    stocks = user.get_stocks()
    return render_template('portfolio.jinja', user = user, stocks=stocks)

@app.route('/finance', methods = ['POST', 'GET'])
def finance():
    user = User.query.filter_by(username = session.get('login_user')).first()
    
    if (request.method == 'POST'):
        if request.form.get('change'):
            change = request.form.get('amount_change')
            # TODO: An issue with sending message to jinja
            try:
                if float(change) < 0 and user.money < 0 - float(change):
                    return render_template('finance.jinja', message_1 = "You know you don't have this much money in your account?", n = n)
                else:
                    user.money += float(change)
                    db.session.commit()
                    if float(change) < 0:
                        return render_template('finance.jinja', message_2 = 'Withdraw succeed! You withdraw ' + str(change) + '$ and your account has ' + str(user.money) + '$ left')
                    elif float(change) > 0:
                        return render_template('finance.jinja', message_2 = 'Deposit succeed! You deposit ' + str(change) + '$ and your account has ' + str(user.money) + 'now')
                    else:
                        return render_template('finance.jinja', message_2 = 'So you basically did nothing')
            except:
                return render_template('finance.jinja', user = user, message_1 = 'Input must be a number!')
    return render_template('finance.jinja', user = user)
    


if __name__ == '__main__':
    # db.create_all()
    app.run()