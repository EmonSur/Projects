from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField,  PasswordField, RadioField, TextAreaField, SelectField, IntegerField, DateField
from wtforms.validators import InputRequired, EqualTo, NumberRange

class RegistrationForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    security_q = SelectField("Pick a Security Question:",
                            choices = ["Mother's Maiden Name", "Childhood Best-friends Name", 
                                       "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer: ", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password:", 
        validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit ✓")

class AdminRegistrationForm(FlaskForm):
    admin_id = StringField("Admin Id:", validators=[InputRequired()])
    security_q = SelectField("Pick a Security Question:",
                            choices = ["Mother's Maiden Name", "Childhood Best-friends Name", 
                                       "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer: ", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password:", 
        validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit ✓")

class ResetPasswordForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    security_q = SelectField("Pick a Security Question:",
                            choices = ["Mother's Maiden Name", "Childhood Best-friends Name", 
                                       "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer: ", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class LoginForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class AdminLoginForm(FlaskForm):
    admin_id = StringField("Admin Id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    review = TextAreaField('Review', validators=[InputRequired()], render_kw={'rows': 5, 'style': 'resize:none;'})
    stars = SelectField('Rating', choices=[('1', '★'), ('2', '★★'), ('3', '★★★'), ('4', '★★★★'), ('5', '★★★★★'), 
                                           ('6', '★★★★★★'), ('7', '★★★★★★★'), ('8', '★★★★★★★★'), ('9', '★★★★★★★★★'), ('10', '★★★★★★★★★★')], validators=[InputRequired()])
    submit = SubmitField('Submit ✓')

class ReviewsForm(FlaskForm):
    options = RadioField("Order Reviews By:", choices=["Newest Reviews", "Oldest Reviews", "Highest Ratings ↑", "Lowest Ratings ↓"],
                         default="Newest Reviews")
    submit = SubmitField("Submit ✓")

class AnimalsForm(FlaskForm):
    habitats = RadioField("Our animals by their Habitat:", choices=["All Habitats", "The African Savanna", "The Himalayan Highlands", 
                                                                    "The South-American Exhibit", "The Freezing Antarctic", "The Australian Outback"],
                         default="All Habitats",)
    submit = SubmitField("Submit ✓")

class BookingsForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    adult_tickets = IntegerField("Adult tickets", validators=[InputRequired(), NumberRange(min=0)])
    child_tickets = IntegerField("Child Tickets", validators=[InputRequired(), NumberRange(min=0)])
    booking_date = DateField("Booking Date", validators=[InputRequired()])
    total_cost = StringField("Total Cost")
    submit = SubmitField("Purchase")

class ViewBookingsForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    name = StringField("Name:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class EmployeeLoginForm(FlaskForm):
    employee_id = StringField("Employee Id:", validators=[InputRequired()])
    code = IntegerField("Login Code:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class DaysOffForm(FlaskForm):
    date_begin = DateField("What is the start date of your days off?", validators=[InputRequired()])
    date_end = DateField("What is the end date of your days off?", validators=[InputRequired()])
    reason = StringField("Please supply the reason(s) for your request:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class DonationForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    donation_amount = IntegerField("Please Enter Your desired Donation Amount", validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField("Submit ✓")

class DeleteReviewForm(FlaskForm):
    review_id = IntegerField("Review Id", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class DeleteAnimalInfoForm(FlaskForm):
    animal_id = IntegerField("Animal Id:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class DeleteEmployeeInfoForm(FlaskForm):
    employee_id = IntegerField("Employee Id:", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class AddNewEmployeeInfoForm(FlaskForm):
    employee_id = IntegerField("Employee Id:", validators=[InputRequired()])
    code = IntegerField("Code:", validators=[InputRequired()])
    name = StringField("Name:", validators=[InputRequired()])
    dob = DateField("Date of Birth:", validators=[InputRequired()])
    start_date = DateField("Start Date:", validators=[InputRequired()])
    job = StringField("Job: ", validators=[InputRequired()])
    submit = SubmitField("Submit ✓")

class AddNewAnimalInfoForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    species = StringField("Species:", validators=[InputRequired()])
    gender = StringField("Gender:", validators=[InputRequired()])
    dob = DateField("Date of Birth:", validators=[InputRequired()])
    arrival_date = DateField("Date of Arrival to Zoo: ", validators=[InputRequired()])
    habitat = SelectField("Habitat:", choices=[ "The African Savanna", "The Himalayan Highlands", 
                                              "The South-American Exhibit", "The Freezing Antarctic", "The Australian Outback"],
                         default="All Habitats",)
    submit = SubmitField("Submit ✓")

    



