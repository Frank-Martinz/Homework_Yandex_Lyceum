from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Работа/Job', validators=[DataRequired()])
    work_size = IntegerField("Время/Time", validators=[DataRequired()])
    team_lead = IntegerField('Главный/Team leader', validators=[DataRequired()])
    collaborators = StringField('Напарники/Collaborators', default='')
    is_finished = BooleanField('Работа выполнена или нет/ Work is done or not')
    submit = SubmitField('Создать работу')
