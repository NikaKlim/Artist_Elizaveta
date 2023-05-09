from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rbgvfedcsxdcfvbfgnhb'
db = SQLAlchemy(app)


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


@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    username = ''
    password = 0
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        print(username, password)

    if username == 'Artist' and password == '1111':
        message = "Correct username and password"
    else:
        message = "Wrong username or password"

    return render_template('login.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
