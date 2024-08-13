from datetime import datetime
from app import db
from model.city import City


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # Айдишник
    name = db.Column(db.String(255), nullable = False)  # Имя
    description = db.Column(db.Text, default = "undefined") # Описание
    data = db.Column(db.Date, default = datetime.utcnow) # Временная метка
    city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable = True) # Ключ города