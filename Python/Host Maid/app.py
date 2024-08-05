from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # Айдишник
    name = db.Column(db.String(255), nullable = False)  # Имя
    description = db.Column(db.Text, default = "undefined") # Описание
    data = db.Column(db.Date, default = datetime.utcnow) # Временная метка

@app.route("/")
@app.route("/index")
def index():
    data = {
        "title": "Главная страница",
        "content": "Ченебудь"
    }
    return render_template("index.html", data = data)

@app.route("/about")
def about():
    data = {
        "title": "О нас",
        "content": "Оп оп оп"
    }
    return render_template("about.html", data = data)

@app.route("/create")
def create():
    data = {
        "title": "Создать",
        "content": "..."
    }
    return render_template("create.html", data = data)

@app.route("/edit")
def edit():
    data = {
        "title": "Редактировать",
        "content": "..."
    }
    return render_template("edit.html", data = data)

@app.route("/delete")
def delete():
    data = {
        "title": "Удалить",
        "content": "..."
    }
    return render_template("delete.html", data = data)

@app.route("/user_list")
def user_list():
    user_list = User.query.all()
    return render_template("user_list.html", data = user_list)

@app.route("/user")
def user():
    data = {
        "title": "Пользователь",
        "content": "..."
    }
    return render_template("user.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)