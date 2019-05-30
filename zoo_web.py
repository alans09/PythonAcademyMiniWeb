from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask("Zoo")
Bootstrap(app)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/pavilions")
def pavilions():
    data = ["Vodny pavilon", "Piesocny pavilon"]
    return render_template(
        "pavilions.html",
        pavilions=data
    )

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
    app.run(host="0.0.0.0", port=80, debug=True)
