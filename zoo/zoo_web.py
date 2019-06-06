from flask import render_template
from zoo.model import *
from zoo import app


@app.route("/")
def home():
    zoo = Zoo.query.all()[0]

    data = zoo.pavilions
    return render_template("main.html", data=data)


@app.route("/pavilions")
def pavilions():
    pavilions = Pavilions.query.all()
    data = [(pavilion.id, pavilion.name, pavilion.description) for pavilion in pavilions]
    return render_template(
        "pavilions.html",
        pavilions=data
    )


@app.route("/pavilion/<id>")
def pavilion_detail(id):
    pavilion = Pavilions.query.get(int(id))
    data = (pavilion.id, pavilion.name, pavilion.description,
            [(animal.name, animal.sex, animal.age) for animal in pavilion.animals]
            )
    return render_template("pavilion.html", data=data)


@app.route("/animals")
def animals():
    data = ["Surikata", "Lev", "Zaba"]
    return render_template(
        "animals.html",
        animals=data
    )


@app.route("/shops")
def shops():
    data = ["Surikata SHOP", "Lev SHOP", "Zaba SHOP"]
    return render_template(
        "shops.html",
        shops=data
    )


if __name__ == "__main__":
    app.run(debug=True)
