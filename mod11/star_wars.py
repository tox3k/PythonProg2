import datetime
import sqlite3
import threading
import requests
import time
BASE_URL = 'http://swapi.dev/api/people/'
DATABASE = 'sqlite3.db'

def init_db():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        try:
            cur.execute('DELETE FROM People')
            con.commit()
        except sqlite3.OperationalError:
            cur.execute('CREATE TABLE People (id INTEGER PRIMARY KEY ,name VARCHAR(255), '
                        'gender VARCHAR(255), birth_year VARCHAR(255))')
def consequent_adding():
    start = datetime.datetime.now()
    data = list({**dict(requests.get(BASE_URL + str(i)).json()), 'id': i} for i in range(1, 21))
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        for human in data:
            if 'name' in human:
                cur.execute(f'INSERT INTO People VALUES(\'{human["id"]}\' ,\'{human["name"]}\', \'{human["gender"]}\', \'{human["birth_year"]}\')')
        con.commit()
    print(f'ConsequentTime: {datetime.datetime.now() - start}')

lock = threading.Lock()
def get_and_add_person_by_request(i):
    data = dict(requests.get(BASE_URL + str(i)).json())
    with lock:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            if 'name' in data:
                cur.execute(f'INSERT INTO People VALUES(\'{i}\' ,\'{data["name"]}\', \'{data["gender"]}\', \'{data["birth_year"]}\')')
                con.commit()

def multithread_adding():
    start = datetime.datetime.now()
    threads = [threading.Thread(target=get_and_add_person_by_request, args=[i]) for i in range(1, 21)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f'Multithread time: {datetime.datetime.now() - start}')




def main():
    init_db()
    consequent_adding()
    init_db()
    multithread_adding()

if __name__ == '__main__':
    main()