from flask import Flask, render_template, session, redirect, request, url_for, g
from flask_session import Session
from database import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash 
from forms import RegistrationForm, LoginForm, ReviewForm, ResetPasswordForm, ReviewsForm, BookingsForm, EmployeeLoginForm, AnimalsForm, ViewBookingsForm, DaysOffForm, DonationForm, AdminRegistrationForm, AdminLoginForm, DeleteReviewForm, DeleteEmployeeInfoForm, DeleteAnimalInfoForm, AddNewEmployeeInfoForm, AddNewAnimalInfoForm
from functools import wraps


app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def logged_in_admin():
    g.admin = session.get("admin_id", None)

@app.before_request
def logged_in_employee():
    g.employee = session.get("employee_id", None)

@app.before_request
def logged_in_user():
    g.user = session.get("user_id", None)

    

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

def employee_login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.employee is None:
            return redirect(url_for("employee_login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

def admin_login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.admin is None:
            return redirect(url_for("admin_login", next=request.url))
        return view(*args, **kwargs)
    return wrapped_view


@app.route("/")
def index():
    db = get_db()
    reviews = db.execute("SELECT * FROM reviews ORDER BY review_id DESC LIMIT 3;")
    return render_template("index.html", reviews=reviews)

@app.route("/about_page")
def about_page():
    db = get_db()
    reviews = db.execute("SELECT * FROM reviews ORDER BY review_id DESC LIMIT 3;")
    return render_template("about_page.html", reviews=reviews)


@app.route("/contact_page")
def contact_page():
    db = get_db()
    reviews = db.execute("SELECT * FROM reviews ORDER BY review_id DESC LIMIT 3;")
    return render_template("contact_page.html", reviews=reviews)


@app.route("/admin_page")
@admin_login_required
def admin_page():
    db = get_db()
    requests = db.execute("SELECT * FROM requests_off; ")
    return render_template("admin_page.html", requests=requests)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    # the following code use to remove the old password, user_id and security info if the user tries to reset their password
    if request.referrer == url_for("reset_password", _external=True):
        user_id = request.args.get("user_id")
        db = get_db()
        db.execute("""DELETE FROM users
         WHERE user_id = ? ;""", (user_id, ))
        db.commit()

    if form.validate_on_submit():
        user_id = form.user_id.data
        security_q = form.security_q.data
        security_ans = form.security_ans.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                    WHERE user_id = ? ;""", (user_id,)).fetchone()
        if possible_clashing_user is not None:
            form.user_id.errors.append("This User Id has already been taken")
        else:
            db.execute("""INSERT INTO users (user_id, security_q, security_ans, password)
                                VALUES (?, ?, ?, ?) ;""", (user_id, security_q, security_ans, generate_password_hash(password))) 
            db.commit() 
            return redirect(url_for("login"))

    return render_template("register.html", form=form)

@app.route("/admin_register", methods=["GET", "POST"])
def admin_register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        admin_id = form.admin_id.data
        security_q = form.security_q.data
        security_ans = form.security_ans.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        possible_clashing_admin = db.execute("""SELECT * FROM admins
                                    WHERE admin_id = ? ;""", (admin_id,)).fetchone()
        if possible_clashing_admin is not None:
            form.admin_id.errors.append("This User Id has already been taken")
        else:
            db.execute("""INSERT INTO admins (admin_id, security_q, security_ans, password)
                                VALUES (?, ?, ?, ?) ;""", (admin_id, security_q, security_ans, generate_password_hash(password))) 
            db.commit() 
            return redirect(url_for("admin_login"))

    return render_template("admin_register.html", form=form)

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        security_q = form.security_q.data
        security_ans = form.security_ans.data
        db = get_db()
        existing_user = db.execute("""SELECT * FROM users
                                    WHERE user_id = ? ;""", (user_id,)).fetchone()
        if existing_user is None:
            form.user_id.errors.append("User Id is incorrect. Check your spelling again.")
        q = db.execute("""SELECT * FROM users
                                    WHERE user_id = ? ;""", (user_id,)).fetchone()
        right_q = q["security_q"]
        right_ans = q["security_ans"]
        if (right_q != security_q) or (right_ans != security_ans):
            form.security_ans.errors.append("Error: Either the security question or answer is wrong.")
        else:
            message = "Please reset your password!"
            return redirect(url_for("register", user_id=user_id, message=message))

    return render_template("reset_password.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        db = get_db()
        possible_clashing_user = db.execute("""SELECT * FROM users
                                    WHERE user_id = ? ;""", (user_id,)).fetchone()
        
        if possible_clashing_user is None:
            form.user_id.errors.append("No such user id exists!")
        elif not check_password_hash(possible_clashing_user["password"], password):
            form.password.errors.append("Incorrect Password!")
        else:
            session.clear()
            session["user_id"] = user_id
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("index")
            return redirect(next_page)

    return render_template("login.html", form=form)

@app.route("/employee_login", methods=["GET", "POST"])
def employee_login():
    form = EmployeeLoginForm()
    if form.validate_on_submit():
        employee_id = form.employee_id.data
        code = form.code.data
        db = get_db()
        employee_exists = db.execute("""SELECT * FROM employee_info
                                    WHERE employee_id = ? ;""", (employee_id,)).fetchone()
        right_code = employee_exists["code"]
        if employee_exists is None:
            form.employee_id.errors.append("No such employee id exists!")
        elif right_code != code:
            form.employee_id.errors.append("Incorrect Code!")
        else:
            session.clear()
            session["employee_id"] = employee_id
            return redirect(url_for("employee_page", employee_id=employee_id))

    return render_template("employee_login.html", form=form)

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin_id = form.admin_id.data
        password = form.password.data
        db = get_db()
        possible_clashing_admin = db.execute("""SELECT * FROM admins
                                    WHERE admin_id = ? ;""", (admin_id,)).fetchone()
        
        if possible_clashing_admin is None:
            form.admin_id.errors.append("No such admin id exists!")
        elif not check_password_hash(possible_clashing_admin["password"], password):
            form.password.errors.append("Incorrect Password!")
        else:
            session.clear()
            session["admin_id"] = admin_id
            next_page = url_for("admin_page", admin_id=admin_id)
            return redirect(next_page)

    return render_template("admin_login.html", form=form)


@app.route("/employee_page", methods=["GET", "POST"])
@employee_login_required
def employee_page():
    form = DaysOffForm()
    employee_id = request.args.get('employee_id')
    db = get_db()
    employee = db.execute("""SELECT * FROM employee_info
                                WHERE employee_id = ? ;""", (employee_id,)).fetchone()
    if form.validate_on_submit():
        date_begin = form.date_begin.data
        date_end = form.date_end.data
        reason = form.reason.data
        name = employee["name"]
        db.execute("""INSERT INTO requests_off (employee_id, name, date_begin, date_end, reason)
                    VALUES (?, ?, ?, ?, ?) ;""", (employee_id, name, date_begin, date_end, reason))
        db.commit()

        form.reason.data = ""
    return render_template("employee_page.html", form=form, employee=employee)


@app.route("/animals",  methods=["GET", "POST"])
def animals():
    form = AnimalsForm()
    db = get_db()
    animals = db.execute("""SELECT * FROM animals;""")
    if form.validate_on_submit():
        habitats = form.habitats.data
        db = get_db()
        if habitats == "All Habitats":
            animals = db.execute("""SELECT * FROM animals;""").fetchall()
        else:
            animals = db.execute("""SELECT * FROM animals
                                    WHERE habitat = ? ;""", (habitats, ))
    return render_template("animals.html", form=form, animals=animals)


@app.route("/review", methods=["GET", "POST"])
@login_required
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        name = form.name.data
        review = form.review.data
        stars = form.stars.data
        db = get_db()
        db.execute("""INSERT INTO reviews (name, review, stars, user_id)
                    VALUES (?, ?, ?, ?) ;""", ( name, review, stars, g.user)) 
        db.commit() 

        # clear form
        form.name.data = ""
        form.review.data = ""
        form.stars.data = ""
        message = "Thank you for submitting your review!"
        return render_template("review.html", form=form, message=message)
    return render_template("review.html", form=form)

@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    form = ReviewsForm()
    db = get_db()
    reviews = db.execute("SELECT * FROM reviews ORDER BY review_id DESC;")
    if form.validate_on_submit():
        options = form.options.data
        if options == "Newest Reviews":
            reviews = db.execute("SELECT * FROM reviews ORDER BY review_id DESC;")
        if options == "Oldest Reviews":
            reviews = db.execute("SELECT * FROM reviews ORDER BY review_id;")
        if options == "Highest Ratings":
            reviews = db.execute("SELECT * FROM reviews ORDER BY stars DESC;")
        if options == "Lowest Ratings":
            reviews = db.execute("SELECT * FROM reviews ORDER BY stars;")
    return render_template("reviews.html", form=form, reviews=reviews)

@app.route("/donate", methods=["GET", "POST"])
@login_required
def donate():
    form = DonationForm()
    if form.validate_on_submit():
        name = form.name.data
        donation_amount = form.donation_amount.data
        db = get_db()
        db.execute("""INSERT INTO donations (user_id, name, donation_amount)
                    VALUES (?, ?, ?) ;""", (g.user, name, donation_amount)) 
        db.commit()

        form.name.data = ""
        
        message = "Thank you for your donation!"
        return render_template("donate.html", form=form, message=message)
    return render_template("donate.html", form=form)


@app.route("/bookings", methods=["POST", "GET"])
@login_required
def bookings():
    form = BookingsForm()
    if request.referrer == url_for("view_bookings", _external=True):
        action = request.args.get('action')
        if action == 'delete':
            user_id = request.args.get("user_id")
            db = get_db()
            db.execute("""DELETE FROM users
                        WHERE user_id = ? ;""", (user_id, ))
            db.commit()

    if form.validate_on_submit():
        name = form.name.data
        adult_tickets = form.adult_tickets.data
        child_tickets = form.child_tickets.data
        booking_date = form.booking_date.data
        total_cost = adult_tickets * 22.50 + child_tickets * 14.65
        form.total_cost.data = total_cost
        db = get_db()
        db.execute("""INSERT INTO bookings (user_id, name, adult_tickets, child_tickets, booking_date, total_cost)
                    VALUES (?, ?, ?, ?, ?, ?) ;""", (g.user, name, adult_tickets, child_tickets, booking_date, total_cost)) 
        db.commit()
        
        message = "Purchase Successful! Thank you for booking with us"
        return render_template("bookings.html", form=form, message=message)
    return render_template("bookings.html", form=form)

@app.route("/view_bookings", methods=["POST", "GET"])
def view_bookings():
    form = ViewBookingsForm()
    if form.validate_on_submit():
        name = form.name.data
        user_id = form.user_id.data
        db = get_db()
        booking = db.execute("""SELECT name FROM bookings
                                    WHERE user_id = ? ;""", (user_id, )).fetchone()
        right_name = booking["name"]
        if name == right_name:
            bookings = db.execute("""SELECT * FROM bookings
                                    WHERE user_id = ? ;""", (user_id, )).fetchall()  
            return render_template("view_bookings.html", form=form, bookings=bookings)
        else:
            form.user_id.errors.append("Either the name under the booking or user_id is Incorrect!")    
    return render_template("view_bookings.html", form=form)

@app.route("/delete_review", methods=["POST", "GET"])
@admin_login_required
def delete_review():
    form = DeleteReviewForm()
    if form.validate_on_submit():
        review_id = request.args.get("review_id")
        db = get_db()
        db.execute("""DELETE FROM reviews
                    WHERE review_id = ? ;""", (review_id, ))
        db.commit()
        message = "This review has been deleted."
        return render_template("update_reviews.html", form=form, message=message)
    return render_template("update_reviews.html", form=form)

@app.route("/add_employee_info", methods=["POST", "GET"])
@admin_login_required
def add_employee_info():
    form = AddNewEmployeeInfoForm()
    if form.validate_on_submit():
        employee_id = form.employee_id.data
        code = form.code.data
        name = form.name.data
        dob = form.dob.data
        job = form.job.data
        start_date = form.start_date.data
        db = get_db()
        db.execute("""INSERT INTO employee_info (employee_id, code, name, dob, job, start_date)
                    VALUES (?, ?, ?, ?, ?, ?) ;""", (employee_id, code, name, dob, job, start_date)) 
        db.commit()
        message = "This Employee's Info has been added."
        return render_template("add_employee_info.html", form=form,  message=message)
    return render_template("add_employee_info.html", form=form)

@app.route("/delete_employee_info", methods=["POST", "GET"])
@admin_login_required
def delete_employee_info():
    form = DeleteEmployeeInfoForm()   
    if form.validate_on_submit():
        employee_id = form.employee_id.data
        db = get_db()
        db.execute("""DELETE FROM employee_info
                    WHERE employee_id = ? ;""", (employee_id, ))
        db.commit()
        message = "This Employee's Info has been deleted."
        return render_template("delete_employee_info.html", form=form, message=message)
        
    return render_template("delete_employee_info.html",  form=form)


@app.route("/delete_animal_info", methods=["GET", "POST"])
@admin_login_required
def delete_animal_info():
    form = DeleteAnimalInfoForm()
    if form.validate_on_submit():
        animal_id = form.animal_id.data
        db = get_db()
        animal_exists = db.execute("""SELECT * FROM animals
                                        WHERE animal_id = ? ;""", (animal_id,)).fetchone()
        if animal_exists is not None:
            db.execute("""DELETE FROM animals
                        WHERE animal_id = ? ;""", (animal_id, ))
            db.commit()


            message = "This Animal's Info has been deleted."
            return render_template("delete_animal_info.html",  
                                   form=form, message=message)
        else:
            form.animal_id.errors.append("This is not one of our animals! Please check your spelling.")
    return render_template("delete_animal_info.html",  form=form)

@app.route("/add_animal_info", methods=["GET", "POST"])
@admin_login_required
def add_animal_info():
    form = AddNewAnimalInfoForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        gender = form.gender.data
        dob = form.dob.data
        arrival = form.arrival_date.data
        habitat = form.habitat.data
        db = get_db()
        animal_exists = db.execute("""SELECT * FROM animals
                                        WHERE name = ? ;""", (name,)).fetchone()
        if animal_exists is not None:
            db.execute("""INSERT INTO animals (name, species, gender, dob, arrival, habitat)
                        VALUES (?, ?, ?, ?, ?, ?) ;""", (name, species, gender, dob, arrival, habitat)) 
            db.commit()
            
            message = "Update Successful! You Have Successfully added a new animal!",
            return render_template("add_animal_info.html",  
                                   form=form, message=message)
        else:
            form.name.errors.append("This is not one of our animals! Please check your spelling.")

    return render_template("add_animal_info.html", form=form)


@app.route("/logout")
def logout():
    session.clear()
    return redirect( url_for("index"))