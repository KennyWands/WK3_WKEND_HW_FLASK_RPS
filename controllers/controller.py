from flask import render_template, request  # ADDED
from app import app
from models.game import *
from models.player import *


@app.route("/Welcome")
def index():
  
    return render_template("index.html", title="Welcome")


@app.route("/Welcome/next_player", methods=["POST"])
def get_player_choice():
    player = Player(request.form["name"], request.form["weapon"])
    player_list.append(player)
    return render_template("Player2choice.html", title="Welcome")


@app.route("/Welcome/outcome", methods=["POST"])
def show_winner():

    player = Player(request.form["name"], request.form["weapon"])
    player_list.append(player)
    game = Game(player_list)
    if game.play() == "p1":
        return render_template("result1.html", title="Player 1 Wins", player_list =player_list)
    elif game.play() == "p2":
        return render_template("result2.html", title="Player 2 Wins", player_list =player_list)
    elif game.play() == "Draw":
         return render_template("draw.html", title="Tie", player_list =player_list)

@app.route("/Welcome", methods = ["POST"])
def again():
    player_list.clear()
    return render_template("index.html", title="Welcome")