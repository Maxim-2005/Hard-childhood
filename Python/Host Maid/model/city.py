from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # Айдишник
    name = db.Column(db.String(255), nullable = False)  # Имя