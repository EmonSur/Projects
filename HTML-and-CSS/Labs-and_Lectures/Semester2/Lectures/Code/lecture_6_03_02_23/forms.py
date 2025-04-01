from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange

# we will import one of the following depending on what the user is typing:

# box in which someone would type in some text - StringField
# box in which someone would type in a integer - IntegerField#
# for floats we will use - DecimalField
# we will need SubmitField, to submit our form

class BMIForm(FlaskForm):
    # this is object oriented programming

    weight = DecimalField("Weight in kg: ",
        validators = [InputRequired(), NumberRange(1, 1000)])
        # in the validators we will need to include which tests we want
        # these must be imported from wtforms.validators
    height = DecimalField("Height in m: ",
        validators = [InputRequired(), NumberRange(1, 3)])
    bmi = DecimalField("BMI: ")
    submit = SubmitField("Submit")


