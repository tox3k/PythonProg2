"""
На заводе "Дружба" работает очень дружный коллектив.
Рабочие работают посменно, в смене -- 10 человек.
На смену заходит 366 .

Бухгалтер завода составила расписание смен и занесла его в базу данных
    в таблицу `table_work_schedule`, но совершенно не учла тот факт,
    что все сотрудники люди спортивные и ходят на различные спортивные кружки:
        1. футбол (проходит по понедельникам)
        2. хоккей (по вторникам
        3. шахматы (среды)
        4. SUP сёрфинг (четверг)
        5. бокс (пятница)
        6. Dota2 (суббота)
        7. шах-бокс (воскресенье)

Как вы видите, тренировки по этим видам спорта проходят в определённый день недели.

Пожалуйста помогите изменить расписание смен с учётом личных предпочтений коллектива
    (или докажите, что то, чего они хотят - не возможно).
"""






"""
--------------------------------
ЗАДАНИЕ РЕШЕНО НЕПРАВИЛЬНО!!!!!!!
--------------------------------
"""

















import sqlite3
from queue import Queue
from datetime import datetime, timedelta

DAYS_COUNT = 30

days = {i: [] for i in range(DAYS_COUNT)}
day_names = ['футбол', 'хоккей', 'шахматы', 'SUP сёрфинг', 'бокс', 'Dota2', 'шах-бокс']
WORKERS_DICT = {'футбол': [], 'хоккей': [], 'шахматы': [], 'SUP сёрфинг': [], 'бокс': [], 'Dota2':[], 'шах-бокс':[]}

def init(c: sqlite3.Cursor):
    global WORKERS_DICT
    for worker in c.execute("SELECT id, preferable_sport FROM table_friendship_employees").fetchall():
        WORKERS_DICT[worker[1]].append(worker[0]) 

    WORKERS_DICT = dict(sorted(WORKERS_DICT.items(), key=lambda item: item[1]))
    

def update_work_schedule(c: sqlite3.Cursor) -> None:
    global WORKERS_DICT, DAYS_COUNT, days

    counter = 0
    group = []
    day = day_names[2]
    date = datetime.fromisoformat('2022-01-01')
    workers_work_days = {i: 0 for i in range(1, 367)}
    while True:
        for k, v in WORKERS_DICT.items():
            if len(group) == 10:
                break
            if counter > len(v) or day == k: 
                continue
            if workers_work_days[v[counter]] > 9:
                continue
            group.append(v[counter])
        counter += 1

        if all(counter > len(v) for k, v in WORKERS_DICT.items()):
            counter = 0

        if all(workers_work_days[worker] for worker in list(WORKERS_DICT.values())):
               break
        
        if len(group) == 10:
            for worker in group:
                c.execute(f'UPDATE table_friendship_schedule ORDER BY employee_id SET date=\'{date.strftime("%Y-%m-%d")}\' WHERE employee_id={worker} LIMIT 1 OFFSET {workers_work_days[worker]}')
                workers_work_days[worker] += 1


    


        



def main():
    with sqlite3.Connection('hw.db') as con:
        cur = con.cursor()
        init(cur)
        update_work_schedule(cur)


if __name__ == '__main__':
    main()

