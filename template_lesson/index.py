from flask import Flask, render_template

#templates - название папки для шаблонов

app = Flask(__name__)

authors = [
    {
        'name': 'Тененбаум',
        'books_count': 3
    },
    {
        'name': 'Флэнеген',
        'books_count': 2
    },
    {
        'name': 'Самерфилд',
        'books_count': 5
    },

]

@app.route('/')
def home():

    return render_template('home.html')


@app.route('/books/')
def books():
    context = {
        'author': 'Тененбаум',
        'books': [
            {
                'title': 'Архитектура компьютера',
                'pages': 820
            },
            {
                'title': 'Компьютерные сети',
                'pages': 1020
            },
            {
                'title': 'Игра Эндера',
                'pages': '300'
            },
        ]
    }
    return render_template('books.html', **context)

@app.route('/my/')
def my():
    return render_template('my.html')

@app.route('/authors/')
def authors():
    authors = {
        'Tenenbaum':  {
            'author': 'Тененбаум',
            'books': 5,
            'genre': 'Компьютерная литература'
        },
        "Scott Card": {
            'author': 'Орсон Скотт Кард',
            'books': 32,
            'genre': 'science fiction'
        },
        "MagaUchHoz": {
            'author': 'Мага с учхоза',
            'books': 'infinity',
            'genre': 'all genres'
        }
    }
    return render_template('authors.html', **authors)

@app.route('/contact/')
@app.route('/contact/<phone>')
def contact(phone=None):
    if phone is None:
        phone = '656565'
    return 'Мой телефон ' + phone


if __name__ == '__main__':
    app.run(debug=True, port=8001)