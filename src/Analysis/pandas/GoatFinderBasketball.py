import pandas as pd
from src.Model.Player import Player

def find_the_goat_basketball(players_df: pd.DataFrame) -> Player:
    games_df = pd.read_csv("./data/basketball/game.csv")

    home_wins = games_df[games_df["pts_home"] > games_df["pts_away"]]
    away_wins = games_df[games_df["pts_away"] > games_df["pts_home"]]

    wins_count = {}
    for _, row in home_wins.iterrows():
        tid = row["team_id_home"]
        wins_count[tid] = wins_count.get(tid, 0) + 1
    for _, row in away_wins.iterrows():
        tid = row["team_id_away"]
        wins_count[tid] = wins_count.get(tid, 0) + 1

    goat_team_id = max(wins_count, key=wins_count.get)
    goats = players_df[players_df["team_id"] == goat_team_id]

    if len(goats) == 0:
        raise ValueError("Aucun joueur trouvé")

    goat_row = goats.iloc[0]
    return Player(nom=f"{goat_row['first_name']} {goat_row['last_name']}", birthdate=None)