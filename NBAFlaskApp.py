from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import datetime

# Below three lines are used to connect to existing local database containing stats on current nba players
# for 2019-2020 season
client = MongoClient('mongodb://localhost:27017/')

NBADatabase = client['NBADatabase']

NBACollection = NBADatabase['NBAPLAYERS']

# current list of player attributes which are stored on the database
playerAttributes = ["name", "minutes", "FG%", "FGA", "3Pt%", "3PtA", "FT%", "FTA"]

app = Flask(__name__)
# use set FLASK_ENV=development to turn on the debugger


class Player:
    def __init__(self, name, minutes, fieldGoalPercentage, fieldGoalsAttempted, threePtPercentage, threesPerGame,
                 freeThrowPercentage, freeThrowsAttempted):
        self.name = name
        self.minutes = minutes
        self.fieldGoalsAttempted = fieldGoalsAttempted
        self.threePtPercentage = threePtPercentage
        self.threesPerGame = threesPerGame
        self.freeThrowsAttempted = freeThrowsAttempted
        self.freeThrowPercentage = freeThrowPercentage
        self.fieldGoalPercentage = fieldGoalPercentage

    def __str__(self):
        return "Name: " + self.name + "\n Minutes Per Game: " + str(self.minutes) + "\n Field Goals Attempted: " \
               + str(self.fieldGoalsAttempted) + "\nField Goal Percentage: " + str(
            self.fieldGoalPercentage) + "\n Free Throws " \
               + "Attempted: " + str(self.fieldGoalsAttempted) + "\n Free Throw Percentage: " + str(
            self.freeThrowPercentage)


@app.route("/" , methods=["GET"])
def index():
    my_header = "NBA Player Analysis" # Look at index.html to examine how the placeholder is used in header
    return render_template("index.html", my_header=my_header)

# Below is a good example of how to use conditionals in html as well as dynamic variables in html
@app.route("/hello")
def index_hello():
    now = datetime.datetime.now()
    indep_day = now.month == 7 and now.day == 4
    dogs = ["Bruce", "Frannie", "Maverick"]
    return render_template("conditional.html", indep_day=indep_day, dogs=dogs)


# Use for simple links back to index page
@app.route("/more")
def more():
    return render_template("more.html")


# Below is used to search for player stats
@app.route("/player", methods=["POST"])
def player():
    name = str(request.form.get("fname")).title()

    return redirect(url_for('player_profile', player=name))


# Use <<datatype>:<variablename>> in the app route to specify type for variables in dynamic routes
@app.route('/player/<string:player>')
def player_profile(player):
    #player = " ".join([playerfirst.capitalize(), playerlast.capitalize()])
    playerquery = {"name": player}
    playerdoc = NBACollection.find_one(playerquery)
    playerstats = Player(playerdoc[playerAttributes[0]], playerdoc[playerAttributes[1]], playerdoc[playerAttributes[2]],
                         playerdoc[playerAttributes[3]], playerdoc[playerAttributes[4]], playerdoc[playerAttributes[5]],
                         playerdoc[playerAttributes[6]], playerdoc[playerAttributes[7]])
    return playerstats.__str__()


@app.route('/<int:year>/<playername>/<stats>')
def year_player_stats(year, playername, stats):
    return year + " " + playername + " " + stats
