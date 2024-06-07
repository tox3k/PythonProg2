"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import subprocess
import re
app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    out = subprocess.check_output('uptime').decode('utf-8')
    
    time = re.search('up\s*\d*:\d+', out).group(0)[2:]

    return f'Current uptime: {time}'


if __name__ == '__main__':
    app.run(debug=True)
