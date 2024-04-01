import datetime
import random
import re

from flask import Flask
app = Flask(__name__)
cars_list=['Chevrolet' , 'Renault', 'Ford', 'Lada']
cats_list = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']
war_and_peace = open('static/war_and_peace.txt', 'r', encoding='UTF-8').read()
visits = 0

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars():
    global cars_list
    return ' '.join(cars_list)

@app.route('/cats')
def cats():
   return random.choice(cats_list)


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.datetime.now()
    current_time_after_hour = current_time + datetime.timedelta(hours=1)
    return f'Точное время через час будет: {current_time_after_hour}'

def get_word_list():
    return re.findall(r'[a-zA-Zа-яА-Я]+', war_and_peace)

@app.route('/get_random_word')
def get_random_word():
    return random.choice(get_word_list())


@app.route('/counter')
def counter():
    global visits
    visits += 1
    return str(visits)


if __name__ == '__main__':
    app.run(debug=True)
