from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, RadioField, TextAreaField, SelectField, IntegerField, DateField
from wtforms.validators import InputRequired, EqualTo, NumberRange, Length, Regexp, ValidationError

def validate_password(form, field):
    password = field.data
    if (len(password) < 8 or not any(char.isupper() for char in password) or
        not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or
        not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password)):
        raise ValidationError("Password must be at least 8 characters long and include an uppercase letter, "
                              "a lowercase letter, a digit, and a special character.")

class RegistrationForm(FlaskForm):
    user_id = StringField("User Id:", validators=[
        InputRequired(), 
        Length(min=5, max=20, message="User ID must be between 5 and 20 characters."),
        Regexp('^[A-Za-z0-9_.-]+$', message="User ID can only contain letters, numbers, dots, hyphens, and underscores.")
    ])
    security_q = SelectField("Pick a Security Question:",
                             choices=["Mother's Maiden Name", "Childhood Best-friends Name", 
                                      "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer:", validators=[InputRequired(), Length(min=3, message="Answer must be at least 3 characters long.")])
    password = PasswordField("Password:", validators=[InputRequired(), validate_password])
    password2 = PasswordField("Confirm Password:", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit ✓")

class AdminRegistrationForm(FlaskForm):
    admin_id = StringField("Admin Id:", validators=[
        InputRequired(), 
        Length(min=5, max=20, message="Admin ID must be between 5 and 20 characters."),
        Regexp('^[A-Za-z0-9_.-]+$', message="Admin ID can only contain letters, numbers, dots, hyphens, and underscores.")
    ])
    security_q = SelectField("Pick a Security Question:",
                             choices=["Mother's Maiden Name", "Childhood Best-friends Name", 
                                      "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer:", validators=[InputRequired(), Length(min=3, message="Answer must be at least 3 characters long.")])
    password = PasswordField("Password:", validators=[InputRequired(), validate_password])
    password2 = PasswordField("Confirm Password:", validators=[InputRequired(), EqualTo("password")])
    submit = SubmitField("Submit ✓")

class ResetPasswordForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    security_q = SelectField("Pick a Security Question:",
                             choices=["Mother's Maiden Name", "Childhood Best-friends Name", 
                                      "Name of Primary School", "Favourite Movie"])
    security_ans = StringField("Security Question Answer:", validators=[InputRequired(), Length(min=3, message="Answer must be at least 3 characters long.")])
    submit = SubmitField("Submit ✓")

class LoginForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired(), validate_password])
    submit = SubmitField("Submit ✓")

class AdminLoginForm(FlaskForm):
    admin_id = StringField("Admin Id:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired(), validate_password])
    submit = SubmitField("Submit ✓")

class ReviewForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    review = TextAreaField('Review', validators=[InputRequired(), Length(min=10, max=1000, message="Review must be between 10 and 1000 characters.")], render_kw={'rows': 5, 'style': 'resize:none;'})
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
                         default="All Habitats")
    submit = SubmitField("Submit ✓")

class BookingsForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    adult_tickets = IntegerField("Adult tickets", validators=[InputRequired(), NumberRange(min=0, message="Adult tickets must be 0 or more.")])
    child_tickets = IntegerField("Child Tickets", validators=[InputRequired(), NumberRange(min=0, message="Child tickets must be 0 or more.")])
    booking_date = DateField("Booking Date", validators=[InputRequired()])
    total_cost = StringField("Total Cost")
    submit = SubmitField("Purchase")

class ViewBookingsForm(FlaskForm):
    user_id = StringField("User Id:", validators=[InputRequired()])
    name = StringField("Name:", validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    submit = SubmitField("Submit ✓")

class EmployeeLoginForm(FlaskForm):
    employee_id = StringField("Employee Id:", validators=[InputRequired(), Length(min=5, max=20, message="Employee ID must be between 5 and 20 characters.")])
    code = IntegerField("Login Code:", validators=[InputRequired(), NumberRange(min=1000, max=9999, message="Login code must be a 4-digit number.")])
    submit = SubmitField("Submit ✓")

class DaysOffForm(FlaskForm):
    date_begin = DateField("What is the start date of your days off?", validators=[InputRequired()])
    date_end = DateField("What is the end date of your days off?", validators=[InputRequired()])
    reason = StringField("Please supply the reason(s) for your request:", validators=[InputRequired(), Length(min=10, max=300, message="Reason must be between 10 and 300 characters.")])
    submit = SubmitField("Submit ✓")

class DonationForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    donation_amount = IntegerField("Please Enter Your desired Donation Amount", validators=[InputRequired(), NumberRange(min=1, message="Donation amount must be greater than 0.")])
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
    code = IntegerField("Code:", validators=[InputRequired(), NumberRange(min=1000, max=9999, message="Code must be a 4-digit number.")])
    name = StringField("Name:", validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    dob = DateField("Date of Birth:", validators=[InputRequired()])
    start_date = DateField("Start Date:", validators=[InputRequired()])
    job = StringField("Job:", validators=[InputRequired(), Length(min=2, max=50, message="Job title must be between 2 and 50 characters.")])
    submit = SubmitField("Submit ✓")

class AddNewAnimalInfoForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired(), Length(min=3, max=50, message="Name must be between 3 and 50 characters.")])
    species = StringField("Species:", validators=[InputRequired(), Length(min=3, max=50, message="Species must be between 3 and 50 characters.")])
    gender = StringField("Gender:", validators=[InputRequired(), Length(min=1, max=10, message="Gender must be between 1 and 10 characters.")])
    dob = DateField("Date of Birth:", validators=[InputRequired()])
    arrival_date = DateField("Date of Arrival to Zoo:", validators=[InputRequired()])
    habitat = SelectField("Habitat:", choices=["The African Savanna", "The Himalayan Highlands", 
                                                "The South-American Exhibit", "The Freezing Antarctic", "The Australian Outback"],
                         default="The African Savanna")
    submit = SubmitField("Submit ✓")
