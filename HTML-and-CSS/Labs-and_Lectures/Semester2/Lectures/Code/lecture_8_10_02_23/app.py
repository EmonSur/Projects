from flask import Flask, render_template 
from database import get_db, close_db
from forms import BandForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

# this line closes the database when the route is finished 
# - this is done automatically, we don't need to include this in our functions
app.teardown_appcontext(close_db)

@app.route("/all_gigs")
def all_gigs():
    db = get_db()
    gigs= db.execute("""SELECT * FROM gigs;""").fetchall()
    # when we print out a database, e.g. gigs, what comes back is a list of dictionaries
    # - each dictionary will consist of a row of the database, with the keys of the entries being the column names or "attributes" of the database
    return render_template("gigs.html", gigs=gigs)

@app.route("/future_gigs")
def future_gigs():
    db = get_db()
    gigs = db.execute("""SELECT * FROM gigs
                        WHERE gig_date >= DATE('now');""").fetchall()
    return render_template("gigs.html", gigs=gigs)

@app.route("/future_gigs_by_band", methods=["GET", "POST"])
def future_gigs_by_band():
    form = BandForm()
    gigs = None
    if form.validate_on_submit(): 
        band=form.band.data
        db = get_db()
        gigs = db.execute("""SELECT * FROM gigs
                            WHERE gig date >= DATE('now') AND band ?""", (band,) ).fetchall()
    return render_template("gigs_by_band.html", form=form, gigs=gigs)
    