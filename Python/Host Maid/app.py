from flask import Flask, render_template, request, redirect
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

@app.route("/create_user", methods = ["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        user = User(name = name, description = description)
        
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("/user_list")
        except:
            return "Увы но не выйдет"
    else:
        data = {
        "title": "Создать пользователя",
        "content": "..."
        }
        return render_template("/create_user.html", data = data)
        
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
    data = {
        "title": "Список пользователей",
        "content": User.query.all()
    }
    
    return render_template("user_list.html", data = data)

@app.route("/user")
def user():
    data = {
        "title": "Пользователь",
        "content": "..."
    }
    return render_template("user.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)