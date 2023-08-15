from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    date_birth = DateField('Дата рождения')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6),
                                                   Regexp('((?=.*\d)(?=.*[a-z]).)',
                                                          message='Пароль должен имметь 1 букву и 1 цифру')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
