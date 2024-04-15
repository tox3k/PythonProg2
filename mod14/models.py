import sqlite3

from flask import Flask
from typing import List, Dict

DATABASE = 'table_books.db'

DATA = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.', 'views_count' : 0},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville', 'views_count' : 0},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy', 'views_count' : 0},
]


class Book:
    def __init__(self, id: int, title: str, author: str, views_count: int):
        self.id = id
        self.title = title
        self.author = author
        self.views_count = views_count

    def __getitem__(self, item):
        return getattr(self, item)

def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        # Если таблицы нет, создаем ее и заполняем
        if not exists:
            exists = cursor.executescript(
                "CREATE TABLE 'table_books'"
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author, views_count INTEGER NOT NULL DEFAULT 0)'
            )
            cursor.executemany(
                'INSERT INTO table_books'
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
                #Делаем записи
            )


def get_all_books() -> List[Dict]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE table_books SET views_count=views_count+1')
        cursor.execute('SELECT * from table_books')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]
        #Объединяем данные из БД, создаем из кортежа объект нашего класса

def add_book(title, author) -> None:
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(f'INSERT INTO table_books(title, author) VALUES(\'{title}\', \'{author}\')')
        cur.close()
        con.commit()

def get_books_by_author(author):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE table_books SET views_count=views_count+1 WHERE author=\'{author}\'')
        cursor.execute(f'SELECT * from table_books WHERE author=\'{author}\'')
        all_books = cursor.fetchall()
        conn.commit()
        cursor.close()
        return [Book(*row) for row in all_books]

def get_book_by_id(id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'UPDATE table_books SET views_count=views_count+1 WHERE id=\'{id}\'')
        cursor.execute(f'SELECT * from table_books WHERE id=\'{id}\'')
        book_params = cursor.fetchone()
        conn.commit()
        cursor.close()
        return Book(*book_params)

if __name__ == '__main__':
    init_db(DATA)

