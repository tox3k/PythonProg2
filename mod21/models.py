from sqlalchemy import Column, Integer, Text, Date, Float, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from datetime import datetime
engine = create_engine('sqlite:///mod21/sqlite_python.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

    author = relationship('Authors', back_populates='id')
    receiving_books = relationship('ReceivingBooks', back_populates='book_id')
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.count}, {self.release_date}, {self.author_id}"

class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    books = relationship('Books', back_populates='author_id')
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.surname}"

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)
    receiving_books = relationship('ReceivingBooks', back_populates='student_id')
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.surname}, {self.phone}, {self.email}, {self.average_score}, {self.scholarship}"
    
    @classmethod
    def get_dormitory_students():
        return session.query(Students).filter_by(scholarship = True)
    
    @classmethod
    def get_students_by_avg(avg_score):
        return session.query(Students).filter(Students.average_score > avg_score)

class ReceivingBooks(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='SET NULL'), nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    books = relationship('Books', back_populates='id', cascade='all, delete-orphan')
    students = relationship('Students', back_populates='id')

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return == None:
            return datetime.now() - self.date_of_issue
        return self.date_of_return - self.date_of_issue
    
