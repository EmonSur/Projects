from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, RadioField
from wtforms.validators import InputRequired, NumberRange

class ShiftForm(FlaskForm):
    plaintext = StringField("Plaintext: ",
        validators=[InputRequired()])
    shift = IntegerField("Shift: ",
        validators=[InputRequired(), NumberRange(1, 25)])
    ciphertext = StringField("Ciphertext: ")
    submit = SubmitField("Submit")

class ConversionForm(FlaskForm):
    original_temp_type = RadioField("From",
        choices = ["Fahrenheit:", "Celsius:", "Kelvin:"],
        default = "Celsius:")
    original_temp = IntegerField("", validators=[InputRequired()])
    new_temp_type = RadioField("To",
        choices = ["Fahrenheit:", "Celsius:", "Kelvin:"],
        default = "Fahrenheit:")
    conversion = IntegerField("")
    submit = SubmitField("Submit")
    
    
