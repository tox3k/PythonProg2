"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3
from datetime import datetime, timedelta
from threading import Semaphore, Thread

THREADS_COUNT = 16

sem = Semaphore(THREADS_COUNT)
all_nums = []
temp_nums = []

def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    query = f'SELECT temperature_in_celsius FROM table_truck_with_vaccine WHERE truck_number=\'{truck_number}\' ORDER BY timestamp'
    c.execute(query)
    data = list(i[0] for i in c.fetchall())
    flag_counter = 0
    for i in range(len(data) - 2):
        if data[i] < 16 or data[i] > 20:
            flag_counter += 1
            if flag_counter >= 3:
                return True
        else:
            flag_counter = 0
    return False


def check():
    """
        target-метод для многопоточного выполнения
    """
    global temp_nums
    c = sqlite3.Cursor(sqlite3.Connection('hw.db'))
    while True:
        with sem:
            if len(temp_nums) > 0:
                num = temp_nums[0]
            else:
                break
            temp_nums.pop(0)
            res = check_if_vaccine_has_spoiled(c, num)
            if res:
                print(num)
    c.close()


def multithread_check_all():
    start = datetime.now()
    print(f'Multithread started at: {start}')
    global all_nums, temp_nums

    cur = sqlite3.Cursor(sqlite3.Connection('hw.db'))
    all_nums = list(i[0] for i in cur.execute('SELECT DISTINCT truck_number FROM table_truck_with_vaccine').fetchall())
    cur.close()
    temp_nums = [] + all_nums
    threads = [Thread(target=check) for _ in range(THREADS_COUNT)]
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    print(f'Multithread time: {datetime.now() - start}')
    
def singlethread_check_all():
    start = datetime.now()
    print(f'Singlethread started at: {start}')
    global all_nums
    cur = sqlite3.Cursor(sqlite3.Connection('hw.db'))

    for num in all_nums:
        r = check_if_vaccine_has_spoiled(cur, num)
        if r == True:
            print(num)
    
    print(f'Singlethread time: {datetime.now() - start}')

    


def main():
    multithread_check_all()    
    singlethread_check_all()
if __name__ == '__main__':
    main()
