import sqlite3 as sq

DATABASE = './mod10/hw_4_database.db'

def task1():
    print('--------------task1--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute('SELECT COUNT(*) FROM salaries WHERE salary < 5000').fetchone()[0]
        print(res)

def task2():
    print('--------------task2--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute('SELECT AVG(salary) FROM salaries').fetchone()[0]
        print(res)

def task3():
    print('--------------task3--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute('''
        SELECT AVG(salary) as median FROM 
        (
        SELECT salary FROM salaries 
        ORDER BY salary 
        LIMIT 1 OFFSET 
        (SELECT COUNT(*) FROM salaries) / 2
        )        
    ''').fetchone()[0]
        print(res)

def task4():
    print('--------------task4--------------')
    with sq.Connection(DATABASE) as con:
        cur = con.cursor()
        res = cur.execute('''
                            SELECT s1.high / s2.low
                            FROM 
                            (
                            SELECT SUM(salary) AS high FROM salaries
                            ORDER BY salary DESC LIMIT (SELECT ROUND(COUNT(*) * 0.1) FROM salaries)
                            ) AS s1,

                            (
                            SELECT SUM(salary) AS low FROM salaries
                            ORDER BY salary LIMIT (SELECT ROUND(COUNT(*) * 0.9) FROM salaries)
                            ) AS s2;     
    ''').fetchone()[0]
        print(res)

def main():
    task1()
    task2()
    task3()
    task4()

if __name__ == '__main__':
    main()