from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, SelectField, RadioField
from wtforms.validators import InputRequired

class WombatForm(FlaskForm):
    wombat = BooleanField("Check the box if you think Derek likes wombats: ")
    submit = SubmitField("Submit")

class ToppingForm(FlaskForm):
    """ Version 1 """
    """ topping = StringField("What is Derek's fave pizza topping?: ",
        validators=[InputRequired()])"""

    """ Version 2 """
    """ topping = SelectField("What is Derek's fave pizza topping?: ",
        # instead of giving a box where a user inputs something, 
        # - it gives a drop down mey with multiple choices.
        choices = ["anchovies", "caramel", "olives", "pineapple"],
        validators=[InputRequired()])"""

    """ Version 3 """
    topping = RadioField("What is Derek's fave pizza topping?: ",
        choices = ["anchovies", "caramel", "olives", "pineapple"],
        default = "pineapple")
    submit = SubmitField("Submit")

