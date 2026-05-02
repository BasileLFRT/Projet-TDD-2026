import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from src.Analysis.pandas.MatchPlayers import show_match_players
from src.Analysis.pandas.GoatFinder import find_the_goat_in_df
from src.Analysis.pandas.GoatFinderCL import find_the_goat_cl
from src.Analysis.pandas.PlayerMatches import show_player_matches
from src.Analysis.pandas.PlayerProfile import show_player_profile
from src.Analysis.homemade.GoatFinder import find_the_goat
from src.Analysis.pandas.GoatFinderBasketball import find_the_goat_basketball
from src.Analysis.pandas.GoatFinderTennis import find_the_goat_tennis
from src.Analysis.pandas.BestMatch import show_best_match
from src.Analysis.pandas.TeamMatches import show_team_matches
from src.Analysis.pandas.TeamRanking import show_team_ranking
from src.Analysis.pandas.BestTeam import show_best_team
from src.Analysis.pandas.PlayerComparison import show_player_comparison
from src.Analysis.PlayerSearch import PlayerSearch
from src.Parsers.PlayerLoader import PlayerLoader
from src.Parsers.parse_csv import parse_players_csv
from src.Parsers.MatchLoader import MatchLoader

print("Quel sport ?")
print("1 - Football")
print("2 - Basketball")
print("3 - Tennis")
choix_sport = input("Ton choix : ")

if choix_sport == "1":
    sport = Sport(nom="football")
    print("Quelle compétition ?")
    print("1 - European Leagues")
    print("2 - Champions League")
    competition_choice = input("Ton choix : ")
    if competition_choice == "1":
        competition = Competition(id=1, nom="european_leagues", sport="football", annee=2015)
    else:
        competition = Competition(id=2, nom="champions_league", sport="football", annee=2021)
elif choix_sport == "2":
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

matches = MatchLoader().load_all_matches(sport, competition)

if competition and competition.nom == "european_leagues":
    matches_df = pd.read_csv("./data/football_european_leagues/match.csv")
elif competition and competition.nom == "champions_league":
    matches_df = pd.read_csv("./data/football_champions_league/match.csv")
elif sport.nom == "tennis":
    matches_df = pd.read_csv(f"./data/tennis/{competition.nom}_matches_2024.csv")
else:
    matches_df = pd.read_csv("./data/basketball/game.csv")

if competition is not None and competition.nom == "champions_league":
    players_df = pd.read_csv("./data/football_champions_league/player.csv")
elif competition is not None and competition.nom == "european_leagues":
    players_df = pd.read_csv("./data/football_european_leagues/player.csv")
elif sport.nom == "tennis":
    players_df = pd.read_csv(f"./data/tennis/{competition.nom}_players_2024.csv")
else:
    players_df = pd.read_csv("./data/basketball/player.csv")

print("Qu'est-ce que tu veux regarder ?")
print("1 - Matchs")
print("2 - Joueurs")
print("3 - Stats")
choix_regarder = input("Ton choix : ")

#Matchs
if choix_regarder == "1":
    print("Qu'est-ce que tu veux faire?")
    print("1 - Voir les matchs")
    print("2 - Voire les matchs d'une équipe")
    print("3 - Voir le meilleur match")
    choix_match = input("Ton choix : ")

    if choix_match == "1":
        show_match_players(matches, sport, competition)
    elif choix_match == "2":
        print("Comment est-ce que tu veux trouver l'équipe ?")
        print("1 -Taper un nom")
        print("2 - Choisir dans la liste")
        choix_recherche_equipe = input("Ton choix : ")
        show_team_matches(matches_df, sport, competition, choix_recherche_equipe)
    elif choix_match == "3":
        show_best_match(matches_df, sport, competition)

#Joueurs
elif choix_regarder == "2":
    print("Qu'est-ce que tu veux faire?")
    print("1 - Voir les matchs dans lesquels un joueur a joué")
    print("2 - Voir le profil d'un joueur")
    print("3 - Comparer deux joueurs")
    choix_joueur = input("Ton choix : ")

    if choix_joueur in ["1", "2"]:
        print("Comment veux-tu trouver le joueur ?")
        print("1 - Rentrer un nom")
        print("2 - Choisir dans la liste")
        choix_recherche = input("Ton choix : ")

        if choix_recherche == "1":
            from src.Analysis.PlayerSearch import PlayerSearch
            search_string = input("Nom du joueur : ")
            # convertir players_df en liste de Player pour PlayerSearch
            from src.Parsers.PlayerLoader import PlayerLoader
            players_list = PlayerLoader().load_all_players(sport, competition)
            results = PlayerSearch().filter_players_by_full_name(players_list, search_string)
            for i, p in enumerate(results):
                print(f"{i} - {p.nom}")
            index = int(input("Ton choix : "))
            # filtrer players_df sur le joueur choisi
            players_df = players_df[players_df.apply(
                lambda row: results[index].nom in str(row.values), axis=1
            )]

        if choix_joueur == "1":
            show_player_matches(players_df, matches, sport, competition)
        elif choix_joueur == "2":
            show_player_profile(players_df, sport, competition)

    elif choix_joueur == "3":
        players_list = PlayerLoader().load_all_players(sport, competition)
        print("Joueur 1")
        for i, p in enumerate(players_list):
            print(f"{i} - {p.nom}")
        index = int(input("Ton choix : "))
        joueur_1 = players_list[index]

        print("Joueur 2")
        for i, p in enumerate(players_list):
            print(f"{i} - {p.nom}")
        index = int(input("Ton choix : "))
        joueur_2 = players_list[index]

        if sport.nom == "basketball":
            index_1 = players_df[(players_df["first_name"] + " " + players_df["last_name"]) == joueur_1.nom].index[0]
            index_2 = players_df[(players_df["first_name"] + " " + players_df["last_name"]) == joueur_2.nom].index[0]
        else:
            index_1 = players_df[players_df.apply(lambda row: joueur_1.nom in str(row.values), axis=1)].index[0]
            index_2 = players_df[players_df.apply(lambda row: joueur_2.nom in str(row.values), axis=1)].index[0]

        show_player_comparison(players_df, matches_df, sport, competition, index_1, index_2)

#Stats
elif choix_regarder == "3":
    print("Qu'est-ce que tu veux faire ?")
    print("1 - Trouver le GOAT")
    print("2 - Trouver la meilleure équipe")
    print("3 - Voir le classement des équipes")
    choix_stats = input("Ton choix : ")

    if choix_stats == "1":
        if competition is not None and competition.nom == "champions_league":
            the_goat = find_the_goat_cl(players_df)
        elif sport.nom == "basketball":
            the_goat = find_the_goat_basketball(players_df)
        elif sport.nom == "tennis":
            the_goat = find_the_goat_tennis(players_df, competition.nom)
        else:
            setting = input("Choisis, 0=pandas, 1=à_la_main\n")
            if setting == "0":
                the_goat = find_the_goat_in_df(players_df)
            else:
                players = parse_players_csv("./data/football_european_leagues/player.csv")
                the_goat = find_the_goat(players)
        print(f"Le GOAT est : {the_goat}")
    elif choix_stats == "2":
        show_best_team(matches_df, sport, competition)
    elif choix_stats == "3":
        show_team_ranking(matches_df, sport, competition)
