from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList, EmailField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DepartmentsForm(FlaskForm):
    title = StringField('Департамент/department', validators=[DataRequired()])
    chief = IntegerField('Шеф/chief', validators=[DataRequired()])
    members = StringField('Участники/members', validators=[DataRequired()])
    email = EmailField('Электронная почта/email', validators=[DataRequired()])
    submit = SubmitField('Добавить')
