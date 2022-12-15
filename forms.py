from flask_wtf import FlaskForm
from wtforms import BooleanField, FormField, SelectField, StringField


class CuisineForm(FlaskForm):
    class Meta:
        # Don't add a CSRF token to this "sub-form"
        csrf = False
    
    @classmethod
    def add_checkboxes(cls, data):
        for name, value in data:
            setattr(cls, name, BooleanField(name, default=value))


class UserForm(FlaskForm):
    name = StringField('Name')
    language = SelectField('Language', choices=['JavaScript', 'PHP', 'Python'])
    # (cuisines will be added dynamically)

    @classmethod
    def add_cuisines_fields(cls, cform):
        cls.cuisines = FormField(cform)
