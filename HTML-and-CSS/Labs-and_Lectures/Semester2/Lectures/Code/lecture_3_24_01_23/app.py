from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/greet_by_name/<name>")
def send_greeting_by_name(name):
    return render_template("greet1.html" , name=name)

@app.route("/greet_multilingual/<language>")
def send_greeting_in_language(language):
    hello_dict = {"en": "Hello", "fr": "Bonjour", "es": "Hola"}
    '''Long version
    if language in hello_dict:
    greeting = hello_dict[language]
    else:
    greeting = "Hi"'''
    #Short version
    greeting = hello_dict.get(language, "Hi")
    return render_template("greet2.html", greeting=greeting)

@app.route("/bye")
@app.route("/byebye/<name>")
@app.route("/farewel1/<name>")
def send_parting_by_name(name=None):
    return render_template("bye.htm?", name-name)

@app.route("/could_it_be_me")
def send_lotto_numbers():
    list_of_numbers = []
    for i in range(0, 6):
        n = randint(1, 47)
        list_of_numbers.append(n)
    return render_template("lotto.html",list_of_numbers=list_of_numbers)