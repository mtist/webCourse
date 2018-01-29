
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/user/<user>/<year>")
def hello_user(user, year):
    return "Hello, {0}, you are {1} years old".format(user, year)

if __name__ == "__main__":
    app.run()
