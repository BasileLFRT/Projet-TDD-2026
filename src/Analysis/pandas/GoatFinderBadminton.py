import pandas as pd
from src.Model.Player import Player

def find_the_goat_badminton(players_df: pd.DataFrame, matches_df: pd.DataFrame) -> Player:
    wins_count = {}
    for _, row in matches_df.iterrows():
        winner = row["winner"]
        if pd.notna(winner):
            wins_count[winner] = wins_count.get(winner, 0) + 1

    goat_name = max(wins_count, key=wins_count.get)
    goat_row = players_df[players_df["name"] == goat_name]

    if len(goat_row) == 0:
        return Player(nom=goat_name, birthdate=None)

    return Player(nom=goat_row.iloc[0]["name"], birthdate=None)