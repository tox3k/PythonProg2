import requests
from flask import Flask, render_template, request
from datetime import datetime
import sys, os

app = Flask(__name__)

#Задание 1
def get_summary_rss(path):
    lines = open(path, 'r', encoding='UTF-8').readlines()[1:]
    sum = 0
    for line in lines:
        sum += int(line.split()[5])

    return sum


# Задание 2
def convert_measure(bytes):
    res = float(bytes)
    cnt = 0
    names = ['B', 'KB', 'MB', 'GB', 'TB']
    while res > 1024:
        res /= 1024
        cnt += 1

    return f'{res:.3f} {names[cnt]}'

def get_mean_size():
    data = sys.stdin.readlines()[1:]

    sum = 0
    cnt = 0
    for line in data:
        sum += float(line.split()[4])
        cnt += 1
    if cnt <= 0:
        return 0
    return sum / cnt
    return data

# Задание 3
def decrypt(code):
    decrypted_str = ''
    temp = code.strip()
    i = 0
    while temp.count('.') > 0:
        if temp[i] == '.':
            if i == len(temp) - 1:
                temp = ''
                break
            temp = temp[i + 1:]
            continue
        if i > len(temp) - 3:
            break
        if temp[i].isspace():
            continue
        if temp[i] != '.':
            if temp[i + 1] == '.':
                if temp[i + 2] == '.':
                    if i > 0:
                        temp = temp[: i] + temp[i + 2:]
                        i -= 1
                        continue
                    else:
                        temp = temp[i + 3:]
                        continue
                else:
                    temp = temp[:i + 1] + temp[i + 2:]
                    i += 1
                    continue
            else:
                i += 1
                continue

    decrypted_str = temp
    return decrypted_str

@app.route('/')
def index():
    path = '/home/andrew/Projects/advancedPython/PythonProg2/mod2/output_file.txt'
    context = {}
    context['task1'] = f'Объем потребляемой памяти: {convert_measure(get_summary_rss(path))}'
    # context['task2'] = f'{get_mean_size():.3f} B'
    context['task3'] = f'\nРасшифрованное сообщение: {decrypt(sys.stdin.read())}'
    context['task4'] = ''
    return render_template('index.html', context=context)

days = {
    0 : ['его', 'понедельника'],
    1 : ['его','вторника'],
    2 : ['ей','среды'],
    3 : ['его','четверга'],
    4 : ['ей','пятницы'],
    5 : ['ей','субботы'],
    6 : ['его','воскресенья'],
}

# Задание 4
@app.route('/hello-world/<name>')
def hello_world(name):
    day = datetime.today().weekday()
    return f'Привет ,{name}. Хорош{days[day][0]} {days[day][1]} !'
    pass

# Задание 5
@app.route('/max_number/<path:num>')
def max_number(num):
    nums = list(int(i) for i in num.split('/') if i.isdigit() or i == '-')
    return f'Наибольшее число: {sorted(nums)[-1]}'

# Задание 6
@app.route('/file-preview/<int:SIZE>/<path:RELATIVE_PATH>')
def file_preview(SIZE, RELATIVE_PATH):
    abs_path = os.path.abspath(RELATIVE_PATH)
    preview = open(abs_path, 'r').read(SIZE)
    return f'<abs_path>{abs_path}</abs_path> <result_size>{len(preview)}</result_size><br><result_text>{preview}</result_text>'


storage = {}
@app.route('/add/<date>/<int:number>', methods=['POST', 'GET'])
def save_date(date, number):
    date = datetime.fromisoformat(date)
    storage.setdefault(date.year, {}).setdefault(date.month, {}).setdefault(date.day, {})
    storage[date.year][date.month][date.day] = number
    return ''

@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year not in storage:
        storage[year] = {}
    sum = 0
    for k1, v1 in storage[year].items():
        for k2, v2 in v1.items():
            sum += v2

    return f'Сумма за {year} год: {sum} руб.'

months = {
    1:'январь',
    2:'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь',

}
@app.route('/calculate/<int:year>/<int:month>')
def calculate_year_month(year, month):
    if year not in storage:
        storage[year] = {}
    if month not in storage[year]:
        storage[year][month] = {}
    sum = 0
    for k, v in storage[year][month].items():
        sum += v

    return f'Сумма за {months[month]} месяц {year} года: {sum} руб.'

if __name__ == '__main__':
    app.run(debug=True)
