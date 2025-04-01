from flask import Flask, render_template
from random import choice, randint

app = Flask(__name__)

@app.route("/rps/<player>")
def rps(player):
    rps = ["rock", "scissors", "paper"]
    rand_rps = choice(rps)
    outcome = ""

    if player == rand_rps:
        outcome = "It's a draw"
    if (player == "rock" and rand_rps == "paper") or (player == "paper" and rand_rps == "scissors") or (player == "scissors" and rand_rps == "rock"):
        outcome = "Computer wins!"
    if (rand_rps == "rock" and player == "paper") or (rand_rps == "paper" and player == "scissors") or (rand_rps == "scissors" and player == "rock"):
        outcome = "Player wins!"

    return render_template("rps.html", player=player, rand_rps=rand_rps, outcome=outcome)

@app.route("/could_it_be_me")
def send_lotto_numbers():
    list_of_numbers = []

    i = 0
    while i < 6:
        n = randint(1, 47)
        if list_of_numbers.count(n) == 0:
            list_of_numbers.append(n)
        else:
            i -= 1
        i += 1
    return render_template("lotto.html",list_of_numbers=list_of_numbers)