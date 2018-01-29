from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"


@app.route("/contact/")
@app.route("/contact/<number>")
def contact(number):
    if number == None:
        number = "88005553535"

    return "My number is " + number


if __name__ == "__main__":
    app.run(debug=True)
