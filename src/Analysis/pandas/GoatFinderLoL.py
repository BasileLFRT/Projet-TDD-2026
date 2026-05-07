import pandas as pd
from src.Model.Player import Player

def find_the_goat_lol(players_df: pd.DataFrame, matches_df: pd.DataFrame) -> Player:
    wins_count = {}
    for _, row in matches_df.iterrows():
        winner = row["winner"]
        player_cols = ["top_team_blue", "jungle_team_blue", "mid_team_blue", "bot_team_blue", "sup_team_blue",
                       "top_team_red", "jungle_team_red", "mid_team_red", "bot_team_red", "sup_team_red"]
        if row["team_blue"] == winner:
            winning_cols = ["top_team_blue", "jungle_team_blue", "mid_team_blue", "bot_team_blue", "sup_team_blue"]
        else:
            winning_cols = ["top_team_red", "jungle_team_red", "mid_team_red", "bot_team_red", "sup_team_red"]
        for col in winning_cols:
            pseudo = row[col]
            if pd.notna(pseudo):
                wins_count[pseudo] = wins_count.get(pseudo, 0) + 1

    goat_pseudo = max(wins_count, key=wins_count.get)
    goat_row = players_df[players_df["pseudo"] == goat_pseudo]

    if len(goat_row) == 0:
        return Player(nom=goat_pseudo, birthdate=None)
    return Player(nom=goat_row.iloc[0]["name"], birthdate=goat_row.iloc[0].get("birthdate"))