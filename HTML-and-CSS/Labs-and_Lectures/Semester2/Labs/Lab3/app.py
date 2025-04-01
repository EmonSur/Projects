from flask import Flask, render_template
from forms import ShiftForm, ConversionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"


@app.route("/shift", methods=["GET", "POST"])
def shift():
    form = ShiftForm()
    if form.validate_on_submit():
        plaintext = form.plaintext.data
        shift = form.shift.data

        ciphertext = ""
        for char in plaintext:
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += char
        
        form.ciphertext.data = ciphertext

    return render_template("shift_form.html", form=form,
        title="Caeser Shift Cipher")


@app.route("/conversion", methods=["GET", "POST"])
def conversion():
    form = ConversionForm()
    if form.validate_on_submit():
        original_temp_type = form.original_temp_type.data
        original_temp = form.original_temp.data
        new_temp_type = form.new_temp_type.data

        if original_temp_type == new_temp_type:
            conversion = original_temp
        if original_temp_type == "Celsius:":
            if new_temp_type == "Fahrenheit:":
                conversion = (9 / 5) * original_temp + 32
                conversion = round(conversion, 2)
            if new_temp_type == "Kelvin:":
                conversion = original_temp + 273
        if original_temp_type == "Fahrenheit:":
            if new_temp_type == "Celsius:":
                conversion = (5 / 9) * (original_temp - 32)
                conversion = round(conversion, 2)
            if new_temp_type == "Kelvin:":
                conversion = (5 / 9) * (original_temp - 32) + 273
                conversion = round(conversion, 2)
        if original_temp_type == "Kelvin:":
            if new_temp_type == "Celsius:":
                conversion = original_temp - 273
            if new_temp_type == "Fahrenheit:":
                conversion = (9 / 5) * (original_temp - 273) + 32
                conversion = round(conversion, 2)
        
        form.conversion.data = conversion

    return render_template("conversion_form.html", form=form)



