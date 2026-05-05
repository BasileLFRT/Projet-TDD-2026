import pandas as pd
from src.Model.Player import Player

def find_the_goat_starcraft(players_df: pd.DataFrame, matches_df: pd.DataFrame) -> Player:
    wins = matches_df[matches_df["score_player_1"] > matches_df["score_player_2"]]["player_1"].value_counts()
    wins2 = matches_df[matches_df["score_player_2"] > matches_df["score_player_1"]]["player_2"].value_counts()
    all_wins = wins.add(wins2, fill_value=0)
    goat_name = all_wins.idxmax()
    goat_row = players_df[players_df["name"] == goat_name]
    if len(goat_row) == 0:
        return Player(nom=goat_name, birthdate=None)
    return Player(nom=goat_row.iloc[0]["name"], birthdate=goat_row.iloc[0].get("birthdate"))