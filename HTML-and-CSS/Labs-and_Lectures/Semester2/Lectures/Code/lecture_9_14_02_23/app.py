from flask import Flask, render_template
from database import get_db, close_db
from forms import BandForm, GigForm, RegistrationForm
from datetime import datetime

# this is a function that takes in strings - a changes into random characters - this may be used to keep safe passwords
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"
app.teardown_appcontext(close_db)

@app.route("/all_gigs")
def all_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs;""").fetchall()
    return render_template("gigs.html", gigs=gigs)


@app.route("/future_gigs")
def future_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs
                        WHERE gig_date >= DATE('now');""").fetchall()

    # if we want to order by date, we should include at the end ORDER BY gig_date

    return render_template("gigs_by_band.html", gigs=gigs)

@app.route("/future_gigs_by_band", methods={"GET", "POST"})
def future_gigs_by_band():
    form = BandForm()
    gigs = None
    if form.validate_on_submit():
        band = form.band.data
        db = get_db()
        gigs = db.execute("""SELECT * FROM gigs
                            WHERE gig_date >= DATE('now')
                            AND band = ?;""", (band,) ).fetchall()
    return render_template("gigs_by_band.html", form=form, gigs=gigs)

@app.route("/insert_gig", methods={"GET", "POST"})
def insert_gig():
    form = GigForm()
    message = ""
    if form.validate_on_submit():
        band = form.band.data
        gig_date = form.gig_date.data

        # the following checks to see if the user inputted date is in the future - to do this datetime must be imported
        if gig_date <= datetime.now().date():
            form.gig_date.errors.append("Date must be in the future.")

        else:
            db = get_db()

            # the following code checks to see if a gig is already taking place on the user inputted date - will there be a clash?
            clashing_gig = db.execute("""SELECT * FROM gigs
                                        WHERE gig_date = ?;""", (gig_date,)).fetchone() # fetches one instead of all, as seen before
            if clashing_gig is not None:
                form.gig_date.errors.append("This gig clashes with another")

            else:
                gigs = db.execute("""INSERT INTO gigs (band, gig_date)
                                    VALUES (?, ?);""", (band, gig_date)) 
                                    # The values being inserted are in a tuple - for tuples are values found within brackets, separated by commas
                                    # - if a tuple only contains one value, we must have a comma after the value

                db.commit() # if you are changing a table in a database, this line must be included for the change to be taken into effect
                # - nothing will change in the database if this is omitted
                message = "New gig successfully inserted!"
    return render_template("insert_gig.html", form=form, message=message)


@app.route("/register", methods={"GET", "POST"})
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        password = form.password.data
        password2 = form.password2.data
        db = get_db()
        clashing_user = db.execute("""SELECT * FROM users
                                    WHERE user_id= ?;""", (user_id,)).fetchone()
        
        if clashing_user is not None:
            form.user_id.errors.append("This User Id has already been taken")
        else:
            db.execute("""INSERT INTO users (user_id, password)
                                VALUES (?, ?);""", (user_id, generate_password_hash(password))) 
            db.commit() 
            return "Unfinished (redirect to login)"
    return render_template("register.html", form=form)