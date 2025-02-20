from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def getf():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<html>'+'<br>'.join(lst) + '<br><html>'

@app.route('/image_mars')
def image():
    return '<title>Привет, Марс!</title>'+ '<h1> Жди нас, Марс! </h1>' + "<img src='static/images/IMAGE 2025-02-20 19:10:30.jpg'/>" + '<p> Вот она какая, красная планета. </p>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
