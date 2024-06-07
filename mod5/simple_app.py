import flask
import subprocess
import os
import signal
import time

from flask import current_app


app = flask.Flask(__name__)

@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint was called!'

def start():
    out = subprocess.getoutput('lsof -i:5000')
    if out != '':
        pid = get_pid(out)
        os.kill(pid, signal.SIGINT)
        time.sleep(1)

    app.run()

def get_pid(s: str) -> int:
    return int(list(i.split()[1] for i in s.split('\n'))[1:][0])

if __name__ == '__main__':
    start()
