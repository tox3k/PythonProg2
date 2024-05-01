from multiprocessing.pool import ThreadPool, Pool
import datetime
import sqlite3
import threading
import requests
import time

BASE_URL = 'https://www.swapi.tech/api/people/'
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

lock = threading.Lock()
def get_and_add_person_by_request(i):
    data = dict(requests.get(BASE_URL + str(i)).json())
    if 'result' in data and 'properties' in data['result']:
        data = data['result']['properties']
    with lock:
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            if 'name' in data:
                cur.execute(f'INSERT INTO People VALUES(\'{i}\' ,\'{data["name"]}\', \'{data["gender"]}\', \'{data["birth_year"]}\')')
                con.commit()


def pool_adding():
    print('Pool started!')
    start = datetime.datetime.now()
    with Pool(processes=20) as pool:
        it = pool.map(get_and_add_person_by_request, range(1, 21))
    
    print(f'Pool time: {datetime.datetime.now() - start}')



def thread_pool_adding():
    print('Thread pool started!')
    start = datetime.datetime.now()
    with ThreadPool(processes=20) as thread_pool:
        it = thread_pool.map(get_and_add_person_by_request, range(1, 21))
    
    print(f'Thread pool time: {datetime.datetime.now() - start}')




def main():
    init_db()
    thread_pool_adding()
    init_db()
    pool_adding()

if __name__ == '__main__':
    main()