import pandas as pd
from src.Model.Sport import Sport
from src.Analysis.pandas.MatchPlayers import show_match_players
from src.Analysis.pandas.GoatFinder import find_the_goat_in_df
from src.Analysis.homemade.GoatFinder import find_the_goat
from src.Parsers.parse_csv import parse_players_csv

sport = Sport(nom="football")

print("Que veux-tu faire ?")
print("1 - Voir les joueurs d'un match")
print("2 - Trouver le GOAT")
choice = input("Ton choix : ")

if choice == "1":
    show_match_players(sport)
elif choice == "2":
    setting = input("Select a setting, 0=pandas-powered, 1=àlamain-powered\n")
    if setting == "0":
        players_df = pd.read_csv("./data/football_european_leagues/player.csv")
        the_goat = find_the_goat_in_df(players_df)
    else:
        players = parse_players_csv("./data/football_european_leagues/player.csv")
        the_goat = find_the_goat(players)