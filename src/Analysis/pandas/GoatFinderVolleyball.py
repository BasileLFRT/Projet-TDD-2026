import pandas as pd
from src.Model.Player import Player
from src.Model.Competition import Competition

def find_the_goat_volleyball(players_df: pd.DataFrame, matches_df: pd.DataFrame, competition: Competition) -> Player:
    wins = {}

    if competition.nom == "volleyball_men":
        team1_col, team2_col = "country_code_1", "country_code_2"
    else:
        team1_col, team2_col = "country_1", "country_2"

    for _, row in matches_df.iterrows():
        t1 = row[team1_col]
        t2 = row[team2_col]
        s1 = int(row["set_country_1"] or 0)
        s2 = int(row["set_country_2"] or 0)
        wins[t1] = wins.get(t1, 0) + (1 if s1 > s2 else 0)
        wins[t2] = wins.get(t2, 0) + (1 if s2 > s1 else 0)

    goat_country = max(wins, key=wins.get)
    country_players = players_df[players_df["country_code"] == goat_country]

    if len(country_players) == 0:
        return Player(nom=goat_country, birthdate=None)

    goat_row = country_players.iloc[0]
    return Player(nom=goat_row["name"], birthdate=goat_row.get("birth_date"))