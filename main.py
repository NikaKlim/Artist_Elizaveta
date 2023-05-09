from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rbgvfedcsxdcfvbfgnhb'
db = SQLAlchemy(app)

login_manager = LoginManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(128), nullable=False) # Изменено на 128 символов, т.к. используется хэш
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.login

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __repr__(self):
        return f'User: {(self.login)} - {(self.password)}'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/portfolio')
@login_required
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
        password = generate_password_hash(request.form.get('password'))
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully.')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        user = User.query.filter_by(login=login).first()
        print(user)
        if user and check_password_hash(user.password, password):
            user.authenticated = True
            db.session.commit()
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            flash('Invalid login or password.')
    return render_template('login.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
