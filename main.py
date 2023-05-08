from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = LoginManager


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

@app.route('/login')
def login():
    print(url_for('login'))
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
