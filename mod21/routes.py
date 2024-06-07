import models
from flask import Flask, request, Response
from datetime import datetime, timedelta
from sqlalchemy.exc import NoResultFound
import json

app = Flask(__name__)

@app.route('/get-all-books', methods=['GET'])
def get_all_books():
    return models.session.query(models.Books).all()

@app.route('/get-debtors', methods=['GET'])
def get_debtors():
    debtors_id = models.session.query(models.ReceivingBooks).filter(datetime.now() - models.ReceivingBooks.date_of_issue > timedelta(days=14))
    return models.session.query(models.ReceivingBooks).filter(models.ReceivingBooks.student_id in debtors_id).all()

@app.route('/issue-book', methods=['POST'])
def issue_book():
    data = json.loads(request.data)
    book_id = data['book_id']
    student_id = data['student_id']
    rcv_model = models.ReceivingBooks(
        book_id = book_id,
        student_id = student_id,
        date_of_issue = datetime.now()
    )
    models.session.add(rcv_model)
    models.session.commit()

    return Response(status=200)

@app.route('/return-book', methods=['POST'])
def return_book():
    model = models.ReceivingBooks
    data = json.loads(request.data)
    data = json.loads(request.data)
    book_id = data['book_id']
    student_id = data['student_id']
    try:
        models.session.query(model).filter(model.book_id == book_id, model.student_id == student_id).update({model.date_of_return: datetime.now()})
        return Response(status=201)
    except NoResultFound:
        print(f'Студент {student_id}  не брал книгу {book_id}')
        return Response(status=404)


def main():
    models.Base.metadata.create_all(models.engine)
    app.run(debug=True)

if __name__ == '__main__':
    main()