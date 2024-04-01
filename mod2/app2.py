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
    data = sys.stdin.readlines()

    return data

@app.route('/')
def index():
    path = 'output_file.txt'
    context = {}
    context['task1'] = f'Объем потребляемой памяти: {convert_measure(get_summary_rss(path))}'
    context['task2'] = f'HI{get_mean_size()}'
    context['task3'] = ''
    context['task4'] = ''
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
