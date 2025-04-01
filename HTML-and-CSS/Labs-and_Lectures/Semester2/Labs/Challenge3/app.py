from flask import Flask, render_template
from forms import CalculateForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    form = CalculateForm()
    if form.validate_on_submit():
        calculation = form.calculation.data

        queue = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        operators = ["+", "-", "*", "/"]
        stack = []
        for character in calculation:
            if int(character) in numbers:
                queue.append(character)
            if character in operators:
                stack.append(character)
            


    return render_template("calculate.html", form=form)


