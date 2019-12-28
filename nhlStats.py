import numpy
import matplotlib.pyplot as plt
import datetime
from sportsreference.nhl.teams import Teams
from sportsreference.nhl.roster import Player
from sportsreference.nhl.boxscore import Boxscores, Boxscore

def generatePlayerString(name):
    """
    Generates player string 
    """
    # generate list of player first/last names
    name = name.lower()
    name_list = name.split(' ')
    
    # generate and return player string
    ply_str = name_list[len(name_list)-1][:5].lower()  # gets last name (accounts for multiple first names)
    ply_str += name_list[0][:2].lower()  # gets first name
    ply_str += '01'
    return ply_str


def generateDateString(date):
    """
    Takes datetime object and converts into date string
    Format: "MM-DD-YYYY"
    """
    date_str = date.strftime("%m-%d-%Y")
    return date_str


def getPlayerObject(name):
    """
    Generates player string and retrieves player object
    returns: Player object
    """
    name_str = generatePlayerString(name)
    player_obj = Player(name_str)
    return player_obj


def getTeamObject(abbreviation, year):
    """
    Uses year argument and team abbreviation to retrieve team object
    Returns: team object from specified year
    """
    teams = Teams(year)
    return teams(abbreviation.upper())


def getBoxscoreGames(date):
    """Generates the boxscores of the games held on a specific date
    Parameters:
    date (datetime): datetime object for date of games
    Returns:
    dict: boxscores of the games held on the given date
    """
    # generate date string
    dt_str = generateDateString(dt)

    # get boxscore as dict
    boxscore = Boxscores(dt)
    scores = boxscore.games[dt_str]
    return scores


# choose date for game
dt = datetime.datetime(2019, 12, 23)

# get boxscores on date
scores = getBoxscoreGames(dt)

# get specific boxscore
game = Boxscore(scores[0]['boxscore'])

# get player name to check
am = getPlayerObject("Patrice Bergeron")

print(am.team_abbreviation)

