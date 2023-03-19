from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterForm(FlaskForm):
    login = StringField('Login/email', validators=[DataRequired()])
    password = PasswordField('Password/Пароль', validators=[DataRequired()])
    password_again = PasswordField('Repeat password/Повторите пароль', validators=[DataRequired()])
    surname = StringField('Surname/Фамилия', validators=[DataRequired()])
    name = StringField('Name/Имя', validators=[DataRequired()])
    age = IntegerField('Age/Возраст', validators=[DataRequired()])
    position = StringField('Position/Должность', validators=[DataRequired()])
    speciality = StringField('Speciality/Профессия', validators=[DataRequired()])
    address = StringField('Address/Адрес', validators=[DataRequired()])
    city_from = StringField('City/Город', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
