from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/morse", methods=["GET", "POST"])
def morse():
    # in a lab exercise we will have to fix errors 
    # - that occur if the user inputs anything not found within the dictionary
    if request.method == "GET":
        return render_template("morse_form.html")
    if request.method == "POST":
        message = request.form["message"]
        # .strip() - removes all spaces
        cleaned_message = message.strip().upper()
        morse = ""
        morse_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            " ": "/"
        }
        for character in cleaned_message:
            code = morse_dict[character]
            morse = morse + code + " "
        # this can all be done in one line using list comprehension

        return render_template("morse_response.html", 
            message=message, morse=morse)


@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    if request.method == "GET":
        return render_template("bmi_form.html", 
            weight="", height="", bmi="",error="")
    else:
        weight = request.form["weight"]
        height = request.form["height"]
        if weight == "" or height == "":
            # give the user another chance by sending the form back
            return render_template("bmi_form.html",
            weight=weight,height=height,bmi="",
            error = "Error: PLease fill in both boxes!")

        # a method of checking if the user inputted a float - discussed in Lecture 6
        # try:
        #   weight = float(weight)
        #   height = float(height)
        # except ValueError:
        #   return render_template("bmi_form.html",
        #       weight=weight,height=height,bmi="",
        #       error = "Error: PLease type a number!!")
        
        weight = float(weight)
        height = float(height)
        if weight < 1 or weight > 1000 or height < 1 or height > 1.88:
            return render_template("bmi_form.html",
                weight=weight, height=height, bmi="",
                error="Error: Please use sensible numbers!")
        bmi = weight / (height * height)
        return render_template("bmi_form.html", 
            weight=weight, height=height, bmi=bmi, error="")