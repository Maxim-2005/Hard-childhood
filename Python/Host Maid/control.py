from flask import render_template, request, redirect
from app import app, db
from model.dish import Dish
from model.difficult import Difficult


@app.route("/")
@app.route("/index")
def index():
    data = {
        "title": "Главная страница",
        "content": ""
    }
    return render_template("index.html", data = data)

@app.route("/about")
def about():
    data = {
        "title": "О нас",
        "content": ""
    }
    return render_template("about.html", data = data)

# Создание строки в таблице
@app.route("/dish_add", methods = ["GET", "POST"])
def dish_add():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        difficult_id = request.form["difficult_id"]
        dish = Dish(name = name, description = description, difficult_id = difficult_id)
        try:
            db.session.add(dish)
            db.session.commit()
            return redirect("/dish/" + str(dish.id))
        except:
            return "Увы но не выйдет"
    else:
        data = {
            "title": "Добавить блюдо",
            "difficult": Difficult.query.all()
        }
        return render_template("dish_add.html", data = data)


# Обновление данных в таблице
@app.route("/dish/<int:id>/update", methods = ["GET", "POST"])
def dish_update(id):
    dish = Dish.query.get(id)
    if request.method == "POST":
        dish.name = request.form["name"]
        dish.description = request.form["description"]
        dish.difficult_id = request.form["difficult_id"]
        try:
            db.session.commit()
            return redirect("/dish/" + str(dish.id))
        except:
            return "Увы но не выйдет"
    else:
        data = {
            "title": "Редактировать блюда",
            "dish": dish,
            "difficult": Difficult.query.all()
        }
        return render_template("dish_update.html", data = data)


# Удаление данных из таблицы
@app.route("/dish/<int:id>/delete")
def dish_delete(id):
    dish = Dish.query.get_or_404(id)
    try:
        db.session.delete(dish)
        db.session.commit()
        return redirect("/dish_list")
    except:
        return "Увы но не выйдет"

# Чтение таблицы
@app.route("/dish_list")
def dish_list():
    data = {
        "title": "Список пользователей",
        "content": Dish.query.all()
    }
    return render_template("dish_list.html", data = data)

@app.route("/dish/<int:id>")
def dish(id):
    dish = Dish.query.get(id)
    dish.difficult = Difficult.query.get(dish.difficult_id).name
    data = {
        "title": "Блюдо",
        "dish": dish
    }
    return render_template("dish.html", data = data)