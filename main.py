import os

from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///painting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')

db = SQLAlchemy(app)



class Painting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image= db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Work {self.title} - {self.text}'


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/portfolio')
def portfolio():
    paints = Painting.query.order_by(Painting.title).all()
    return render_template("portfolio.html", data=paints, os_path_join=os.path.join)


@app.route('/biography')
def biography():
    print(url_for('biography'))
    return render_template("biography.html")


@app.route('/order')
def order():
    print(url_for('order'))
    return render_template("order.html")

@app.route('/contact')
def contact():
    print(url_for('contact'))
    return render_template("contact.html")

@app.route('/add_new', methods=['POST', 'GET'])
def add_new():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        image= request.files['image']
        print(image)
        filename = secure_filename(image.filename)
        print(filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(image_path)
        image.save(image_path)
        print(image)
        image_path = os.path.basename(image_path)
        print(image_path)
        image_path = 'static/uploads/'+image_path
        print(image_path)
        paint = Painting(title=title, text=text, image=image_path)
        try:
            db.session.add(paint)
            db.session.commit()
            return render_template('portfolio.html')
        except:
            return 'Something wrong'

    else:
        return render_template('add_new.html')


if __name__ == "__main__":
    app.run(debug=True)
