from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Questionnaire

def parq_fail(form, field):
    answer = field.data
    if answer == 'yes':
        raise ValidationError("You answered yes to one of the first seven questions. In order to ensure your health and safety and in accordance with the National Academy of Sports Medicine's scope of practice for certified personal trainers, we cannot provide a workout to you at this time.")

class QuestionnaireForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    parq1 = StringField('parq1', validators=[DataRequired(), parq_fail])
    parq2 = StringField('parq2', validators=[DataRequired(), parq_fail])
    parq3 = StringField('parq3', validators=[DataRequired(), parq_fail])
    parq4 = StringField('parq4', validators=[DataRequired(), parq_fail])
    parq5 = StringField('parq5', validators=[DataRequired(), parq_fail])
    parq6 = StringField('parq6', validators=[DataRequired(), parq_fail])
    parq7 = StringField('parq7', validators=[DataRequired(), parq_fail])
    barbells = StringField('barbells', validators=[DataRequired()])
    dumbbells = StringField('dumbbells', validators=[DataRequired()])
    cables = StringField('cables', validators=[DataRequired()])
    levers = StringField('levers', validators=[DataRequired()])
    goal = StringField('goal', validators=[DataRequired()])
    height = IntegerField('height', validators=[DataRequired()])
    weight = IntegerField('weight', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])