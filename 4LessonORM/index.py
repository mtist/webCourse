from flask import Flask, render_template, request
from models import db, Person

app = Flask(__name__)
Person.filter(Person.male==True).count()


@app.route("/", methods=["GET", "POST"])
def home():
    POST = False

    if request.method == "POST":
        POST = True

    return render_template("home.html", post=POST)


if __name__ == "__main__":
    app.run(debug=True)