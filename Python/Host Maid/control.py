from flask import render_template, request, redirect
from app import app, db
from model.user import User
from model.city import City


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

# Создание строки в таблице
@app.route("/create_user", methods = ["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        city_id = request.form["city_id"]
        user = User(name = name, description = description, city_id = city_id)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("/user/" + str(user.id))
        except:
            return "Увы но не выйдет"
    else:
        data = {
            "title": "Создать пользователя",
            "city": City.query.all()
        }
        return render_template("create_user.html", data = data)


# Обновление данных в таблице
@app.route("/user/<int:id>/update", methods = ["GET", "POST"])
def user_update(id):
    user = User.query.get(id)
    if request.method == "POST":
        user.name = request.form["name"]
        user.description = request.form["description"]
        user.city_id = request.form["city_id"]
        try:
            db.session.commit()
            return redirect("/user/" + str(uesr.id))
        except:
            return "Увы но не выйдет"
    else:
        data = {
            "title": "Редактировать пользователя",
            "user": user,
            "city": City.query.all()
        }
        return render_template("user_update.html", data = data)


# Удаление данных из таблицы
@app.route("/user/<int:id>/delete")
def delete(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect("/user_list")
    except:
        return "Увы но не выйдет"

# Чтение таблицы
@app.route("/user_list")
def user_list():
    data = {
        "title": "Список пользователей",
        "content": User.query.all()
    }
    return render_template("user_list.html", data = data)

@app.route("/user/<int:id>")
def user(id):
    user = User.query.get(id)
    user.city_id = City.query.get(user.city_id).name
    data = {
        "title": "Пользователь",
        "user": user
    }
    return render_template("user.html", data = data)