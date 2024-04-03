from flask import Flask, render_template
import sys

app = Flask(__name__)

def get_summary_rss(path):
    lines = open(path, 'r', encoding='UTF-8').readlines()[1:]
    sum = 0
    for line in lines:
        sum += int(line.split()[5])

    return sum

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

@app.route('/')
def index():
    path = '/home/user/PycharmProjects/PythonProg2/mod2/output_file.txt'
    context = {}
    context['task1'] = f'Объем потребляемой памяти: {convert_measure(get_summary_rss(path))}'
<<<<<<< HEAD
    context['task2'] = f'{get_mean_size()}'
=======
    context['task2'] = f'{get_mean_size()} B'
>>>>>>> c68d01ca672a7efbf4dd229b3d3cc645d0db6f8a
    context['task3'] = ''
    context['task4'] = ''
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
