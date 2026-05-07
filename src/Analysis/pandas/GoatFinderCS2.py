import pandas as pd
from src.Model.Player import Player

def find_the_goat_cs2(players_df: pd.DataFrame, matches_df: pd.DataFrame) -> Player:
    wins_count = {}
    for _, row in matches_df.iterrows():
        if int(row["score_team_1"]) > int(row["score_team_2"]):
            winner = row["team_1"]
        else:
            winner = row["team_2"]
        wins_count[winner] = wins_count.get(winner, 0) + 1

    goat_team = max(wins_count, key=wins_count.get)
    goat_players = players_df[players_df["team"] == goat_team]

    if len(goat_players) == 0:
        return Player(nom=goat_team, birthdate=None)
    return Player(nom=goat_players.iloc[0]["name"], birthdate=goat_players.iloc[0].get("birthdate"))