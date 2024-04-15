import re
import sqlite3
from forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from models import init_db, DATA, get_all_books, Book, add_book, get_books_by_author, get_book_by_id

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


def _get_hmtl_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Author</th>
                </tr>
            </thead>
                <tbody>
                    {books_rows}
                </tbody>
        </table>
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template('pred_index.html', books=get_all_books())


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    if request.method == 'GET':
        return render_template('add_book.html')
    if request.method == 'POST':
        form = MyForm(request.form)
        form.validate()
        if form.validate():
            add_book(request.form['field1'], request.form['field2'])
            return all_books()
        else:
            return f'{form.errors}'

@app.route('/books/<author>')
def author_books(author):
    books = get_books_by_author(author)
    return render_template('author_books.html', author=author, books=books)

@app.route('/books/<int:id>')
def show_book(id):
    book = get_book_by_id(int(id))
    return render_template('show_book.html', book=book)

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
