from flask import Flask, render_template, request
from models import db, Person

app = Flask(__name__)


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form.get('name', 'default_name')
        year = request.form.get('year', 1990)
        male = request.form.get('male', False)
        Person.create(name=name, year=year, male=male)

    return render_template("post.html")


@app.route("/list/")
def person():
    persons = Person.select()
    return render_template('person.html', persons=persons)


if __name__ == '__main__':
    app.run(debug=True)
