from main import app, db, user


with app.app_context():
    db.create_all()