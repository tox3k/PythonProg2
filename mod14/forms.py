from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField
from wtforms.validators import InputRequired


class MyForm(FlaskForm):
    field1 = StringField('title', [InputRequired('Title is empty')])
    field2 = StringField('author', [InputRequired("Author is empty")])
