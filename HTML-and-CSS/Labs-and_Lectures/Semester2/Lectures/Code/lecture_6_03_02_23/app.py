from flask import Flask, render_template
from forms import BMIForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"


@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    form = BMIForm()

    # next line first checks if the request is "POST"
    # them checks if all the data is valid - else the form is sent again
    if form.validate_on_submit():
        weight = form.weight.data
        height = form.height.data
        bmi = weight / (height * height)
        form.bmi.data = bmi #form.bmi.data needs to be on the RHS for this to work
    return render_template("bmi_form.html", form=form)

