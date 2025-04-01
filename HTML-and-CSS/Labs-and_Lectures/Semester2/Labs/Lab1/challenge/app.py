from flask import Flask, render_template
from random import choice

app = Flask(__name__)

@app.route("/rps15/<player>")
def rps(player):
    rps15 = ["rock","fire","Scissors","snake","human","tree","wolf","sponge","paper","air","water","dragon","devil","lightning","gun"]
    computer = choice(rps15)
    
    pos = rps15.index(player)
    rps15 = rps15[pos:pos+1] + rps15[pos+1:] + rps15[:pos]

    if player == computer:
        outcome = "It's a draw"  
    elif rps15.index(computer) < 8:
        outcome = "Player wins"
    elif rps15.index(computer) >= 8 and rps15.index(computer) < 15:
        outcome = "Computer wins"
    
    return render_template("rps.html", player=player, computer=computer, outcome=outcome)