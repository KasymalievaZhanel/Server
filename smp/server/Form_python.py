from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TelField


class LoginForm(FlaskForm):
    text = TextAreaField('text', validators=[DataRequired()])
    key = TelField('key')
    cript = SelectField('cript', choices=[('encrypt', 'Зашифровать'),
                        ('decrypt', 'Расшифровать'), ('hack', 'Хакнуть')])
#validators=[DataRequired()]