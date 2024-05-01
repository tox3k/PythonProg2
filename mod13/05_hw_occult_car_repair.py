"""
В 20NN году оккультному автосалону "Чёртово колесо" исполняется ровно 13 лет.
    В честь этого они предлагает своим клиентам уникальную акцию:
    если вы обращаетесь в автосалон в пятницу тринадцатое и ваш автомобиль
    чёрного цвета и марки "Лада" или "BMW", то вы можете поменять колёса со скидкой 13%.
Младший менеджер "Чёртова колеса" слил данные клиентов в интернет,
    поэтому мы можем посчитать, как много клиентов автосалона могли воспользоваться
    скидкой (если бы они об этом знали). Давайте сделаем это!

Реализуйте функцию, c именем get_number_of_luckers которая принимает на вход курсор и номер месяца,
    и в ответ возвращает число клиентов, которые могли бы воспользоваться скидкой автосалона.
    Таблица с данными называется `table_occult_car_repair`
"""

import sqlite3
from datetime import datetime, date

def get_number_of_luckers(c: sqlite3.Cursor, month_number: int):
    month_number = str(month_number)
    data = c.execute(f'SELECT * FROM table_occult_car_repair WHERE (car_type=\'BMW\' OR car_type=\'Лада\') AND car_colour=\'чёрный\' AND timestamp LIKE \'%-{month_number.zfill(2)}-13%\'').fetchall()

    date = datetime.fromisoformat(data[0][1])
    
    if date.weekday() == 4:
        return len(data)
    else:
        return 0

def main():
    with sqlite3.Connection('hw.db') as con:
        cur = con.cursor()
        for i in range(1, 13):
            print(get_number_of_luckers(cur, i))

if __name__ == '__main__':
    main()