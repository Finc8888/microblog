from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired#проверка заполненности поля

class LoginForm(FlaskForm):
    """
    Для каждого поля объект создается как переменная класса в классе LoginForm.
    Каждому полю присваивается описание или метка в качестве первого аргумента.

    """
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
