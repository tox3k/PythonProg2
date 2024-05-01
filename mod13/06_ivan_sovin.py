"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3

BASE_SALARY = None
ALL_WORKERS_NAME = []
WORKERS_LOG = open('workers.log', 'w')

def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    global BASE_SALARY
    worker_salary = int(c.execute(f'SELECT salary FROM table_effective_manager WHERE name=\'{name}\'').fetchone()[0])
    max_len = len(max(ALL_WORKERS_NAME, key=len))

    if worker_salary * 1.1 >  BASE_SALARY:
        c.execute(f'DELETE FROM table_effective_manager WHERE name={name}')
        WORKERS_LOG.write(f'Worker with name: {name.ljust(max_len)} dismissed.\n')
    else:
        WORKERS_LOG.write(f'Worker with name: {name.ljust(max_len)} still work here.\n')



def init_base_salary(c: sqlite3.Cursor) -> None:
    global BASE_SALARY
    salary = int(c.execute('SELECT salary FROM table_effective_manager WHERE id=1').fetchone()[0])
    BASE_SALARY = salary


def init_all_workers_name(c: sqlite3.Cursor):
    global ALL_WORKERS_NAME
    workers = c.execute('SELECT name FROM table_effective_manager WHERE id <> 1').fetchall()
    all_workers_name = list(worker[0] for worker in workers)
    ALL_WORKERS_NAME = all_workers_name

def main():
    global ALL_WORKERS_NAME
    with sqlite3.Connection('hw.db') as con:
        cur = con.cursor()

        init_base_salary(cur)
        init_all_workers_name(cur)

        for name in ALL_WORKERS_NAME:
            ivan_sovin_the_most_effective(cur, name)

if __name__ == '__main__':
    main()