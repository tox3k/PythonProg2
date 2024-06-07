import sqlite3 as sq

DATABASE = './mod10/hw_3_database.db'

def task1():
    print('--------------task1--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        for table in ['table_1', 'table_2', 'table_3']:
            print(table + ' : ' + str(cur.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]))


def task2():
    print('--------------task2--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute('SELECT COUNT(DISTINCT value) FROM table_1')
        print(res.fetchone()[0])

def task3():
    print('--------------task3--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute("""SELECT COUNT(*) FROM
                            (SELECT value FROM table_1
                            INTERSECT
                            SELECT value FROM table_2)""").fetchone()[0]

        print(res)

def task4():
    print('--------------task4--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute("""SELECT COUNT(*) FROM(SELECT value FROM table_1
                            INTERSECT
                            SELECT value FROM table_2
                            INTERSECT
                            SELECT value FROM table_3)""").fetchone()[0]

        print(res)

def main():
    task1()
    task2()
    task3()
    task4()

if __name__ == '__main__':
    main()