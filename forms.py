from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField


class UserForm(FlaskForm):
    name = StringField('Name')
    opt1 = BooleanField('Opt 1')
    opt2 = BooleanField('Opt 2')
    opt3 = BooleanField('Opt 3')
    language = SelectField('Language', choices=['JavaScript', 'PHP', 'Python'])