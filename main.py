from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rbgvfedcsxdcfvbfgnhb'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)

    def __repr__(self):

        return f'User: {(self.login)} - {(self.password)}'

user = User(login='Artist', password='1122')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/portfolio')
def portfolio():
    print(url_for('portfolio'))
    return render_template("portfolio.html")


@app.route('/biography')
def biography():
    print(url_for('biography'))
    return render_template("biography.html")


@app.route('/order')
def order():
    print(url_for('order'))
    return render_template("order.html")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        user = User(login=login, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            print(url_for('register'))
            flash(f'Login or password is not correct - {login} - {password}: {user}')
            return redirect('/')
        except:
            print("Something wrong")
            return render_template('register.html')

    else:
        return render_template('register.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    if login and password:
        user = User.query.filter_by(login=login).first()
        flash(f'Login or password is not correct - {user}')
        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')
            return redirect(next_page)
        else:
            flash(f'Login or password is not correct - {login} - {password}: {user}')
    else:
        flash('Please enter login and password')
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
