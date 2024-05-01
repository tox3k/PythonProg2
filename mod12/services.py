from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/timestamp/<stamp>')
def timestamp(stamp):
    return f'{datetime.fromtimestamp(float(stamp))}'

def main():
    app.run()

if __name__ == '__main__':
    main()