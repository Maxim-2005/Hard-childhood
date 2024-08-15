from datetime import datetime
from app import db
from model.difficult import Difficult


class Dish(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # Айдишник
    name = db.Column(db.String(255), nullable = False)  # Название
    description = db.Column(db.Text, default = "undefined") # Описание
    data = db.Column(db.Date, default = datetime.utcnow) # Временная метка
    difficult_id = db.Column(db.Integer, db.ForeignKey(Difficult.id), nullable = True) # Сложность приготовления