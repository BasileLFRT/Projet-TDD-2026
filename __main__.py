import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from src.Analysis.pandas.MatchPlayers import show_match_players
from src.Analysis.pandas.GoatFinder import find_the_goat_in_df
from src.Analysis.pandas.GoatFinderCL import find_the_goat_cl
from src.Analysis.homemade.GoatFinder import find_the_goat
from src.Parsers.parse_csv import parse_players_csv

print("Quel sport ?")
print("1 - Football")
print("2 - Basketball")
print("3 - Tennis")
sport_choice = input("Ton choix : ")

if sport_choice == "1":
    sport = Sport(nom="football")
    print("Quelle compétition ?")
    print("1 - European Leagues")
    print("2 - Champions League")
    competition_choice = input("Ton choix : ")
    if competition_choice == "1":
        competition = Competition(id=1, nom="european_leagues", sport="football", annee=2015)
    else:
        competition = Competition(id=2, nom="champions_league", sport="football", annee=2021)
elif sport_choice == "2":
    sport = Sport(nom="basketball")
    competition = None
else:
    sport = Sport(nom="tennis")
    print("Quelle compétition ?")
    print("1 - ATP")
    print("2 - WTA")
    competition_choice = input("Ton choix : ")
    if competition_choice == "1":
        competition = Competition(id=3, nom="atp", sport="tennis", annee=2024)
    else:
        competition = Competition(id=4, nom="wta", sport="tennis", annee=2024)


print("Que veux-tu faire ?")
print("1 - Voir les joueurs d'un match")
print("2 - Trouver le GOAT")
choice = input("Ton choix : ")

if choice == "1":
    show_match_players(sport, competition)
elif choice == "2":
    if competition is not None and competition.nom == "champions_league":
        players_df = pd.read_csv("./data/football_champions_league/player.csv")
        the_goat = find_the_goat_cl(players_df)
        print(f"Le GOAT est : {the_goat}")
    elif sport.nom == "basketball":
        from src.Analysis.pandas.GoatFinderBasketball import find_the_goat_basketball
        players_df = pd.read_csv("./data/basketball/player.csv")
        the_goat = find_the_goat_basketball(players_df)
        print(f"Le GOAT est : {the_goat}")
    elif sport.nom == "tennis":
        from src.Analysis.pandas.GoatFinderTennis import find_the_goat_tennis
        players_df = pd.read_csv(f"./data/tennis/{competition.nom}_players_2024.csv")
        the_goat = find_the_goat_tennis(players_df, competition.nom)
        print(f"Le GOAT est : {the_goat}")
    else:
        setting = input("Select a setting, 0=pandas-powered, 1=àlamain-powered\n")
        if setting == "0":
            players_df = pd.read_csv("./data/football_european_leagues/player.csv")
            the_goat = find_the_goat_in_df(players_df)
        else:
            players = parse_players_csv("./data/football_european_leagues/player.csv")
            the_goat = find_the_goat(players)
        print(f"Le GOAT est : {the_goat}")