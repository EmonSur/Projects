from flask import Flask, render_template
from forms import WombatForm, ToppingForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"


@app.route("/wombat", methods=["GET", "POST"])
def wombat():
    form = WombatForm()
    outcome = ""
    if form.validate_on_submit():
        wombat = form.wombat.data
        if wombat == True:
            outcome = "Wrong! Derek hates combats."
        else:
            outcome = "Yes, he hates the little feckers."
    return render_template("wombat_form.html", 
        form=form, 
        outcome=outcome, 
        title="Wombat Preferences!")


@app.route("/topping", methods=["GET", "POST"])
def topping():
    form = ToppingForm()
    outcome = ""
    if form.validate_on_submit():
        topping = form.topping.data
        if topping == "anchovies":
            outcome = "Wrong! Well done."
        else:
            outcome = "Wrong. Try again.."
    return render_template("topping_form.html", 
        title = "Pizza Preferences!",
        form=form, 
        outcome=outcome)

