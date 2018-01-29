from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/books/")
def books():
    book_name = "Архитектура компьютера"
    return render_template("books.html", bname = book_name)


@app.route("/contact/")
@app.route("/contact/<number>")
def contact(number):
    if number == None:
        number = "88005553535"

    return "My number is " + number


if __name__ == "__main__":
    app.run(debug=True)
