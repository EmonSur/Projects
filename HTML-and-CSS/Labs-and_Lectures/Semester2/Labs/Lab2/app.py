from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/spy", methods=["GET", "POST"])
def spy():
    if request.method == "GET":
        return render_template("spy_form.html")
    else:
        given_name = request.form["given_name"]
        family_name = request.form["family_name"]
        return render_template("spy_response.html", 
            given_name=given_name, family_name=family_name)

@app.route("/morse", methods=["GET", "POST"])
def morse():
    # in a lab exercise we will have to fix errors 
    # - that occur if the user inputs anything not found within the dictionary
    if request.method == "GET":
        return render_template("morse_form.html")
    if request.method == "POST":
        message = request.form["message"]

        cleaned_message = message.strip()
        morse = ""
        morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D":"-..", "E":".", "F":"..-.",
            "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--",
            "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
            "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "1":".----",
            "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...",
            "8":"---..", "9":"----.", "0":"-----", " ": "/"
        }

        if cleaned_message == "":
            return render_template("morse_form.html",
            error = "Error: You have forgotten to type in your message. Please try again!")

        cleaned_message = message.strip().upper()

        for character in cleaned_message:
            if character not in morse_dict:
                return render_template("morse_form.html",
                    error = "Error: An unacceptable character has been input; only numbers and letter from the latin alphabet can be inputted.")
            code = morse_dict[character]
            morse = morse + code + " "
        # this can all be done in one line using list comprehension

        return render_template("morse_response.html", 
            message=message, morse=morse)


@app.route("/lengths", methods=["GET", "POST"])
def lengths():
    if request.method == "GET":
        return render_template("lengths_form.html", 
            inches="", centimetres="",error="")
    else:
        inches = request.form["inches"]
        centimetres = request.form["centimetres"]

        if  centimetres == "" and inches == "":
            return render_template("lengths_form.html",
                error="Error: Please fill in a box!")
        if centimetres != "" and inches != "":
            return render_template("lengths_form.html",
                inches=inches, centimetres=centimetres,
                error="Error: Don't fill in both boxes!")

        if centimetres != "":
            centimetres = float(centimetres)
            inches = centimetres / 2.54
        if inches != "":
            inches = float(inches)
            centimetres = inches * 2.54

        return render_template("lengths_form.html", 
            inches=inches, centimetres=centimetres, error="")