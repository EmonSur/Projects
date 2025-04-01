from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class BandForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    submit = SubmitField("Submit")

class GigForm(FlaskForm):
    band = StringField("Band:", validators=[InputRequired()])
    gig_date = DateField("Date:", validators=[InputRequired()])
    submit = SubmitField("Submit")