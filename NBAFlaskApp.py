from flask import Flask, render_template
from pymongo import MongoClient

# Below three lines are used to connect to existing local database containing stats on current nba players
# for 2019-2020 season
client = MongoClient('mongodb://localhost:27017/')

NBADatabase = client['NBADatabase']

NBACollection = NBADatabase['NBAPLAYERS']

# current list of player attributes which are stored on the database
playerAttributes = ["name", "minutes", "FG%", "FGA", "3Pt%", "3PtA", "FT%", "FTA"]

app = Flask(__name__)


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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def index_hello():
    return "Hello, hello!"


@app.route('/player/<playerfirst>_<playerlast>')
def player_profile(playerfirst, playerlast):
    player = " ".join([playerfirst.capitalize(), playerlast.capitalize()])
    playerquery = {"name": player}
    playerdoc = NBACollection.find_one(playerquery)
    playerstats = Player(playerdoc[playerAttributes[0]], playerdoc[playerAttributes[1]], playerdoc[playerAttributes[2]],
                         playerdoc[playerAttributes[3]], playerdoc[playerAttributes[4]], playerdoc[playerAttributes[5]],
                         playerdoc[playerAttributes[6]], playerdoc[playerAttributes[7]])
    return playerstats.__str__()


@app.route('/<int:year>/<playername>/<stats>')
def year_player_stats(year, playername, stats):
    return year + " " + playername + " " + stats
