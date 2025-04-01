from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, RadioField
from wtforms.validators import InputRequired, NumberRange

class CalculateForm(FlaskForm):
    calculation = StringField("Please enter in your calculation: ")
    answer = StringField("Here is your answer: ")
