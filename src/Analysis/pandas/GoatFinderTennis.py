import pandas as pd
from src.Model.Player import Player

def find_the_goat_tennis(players_df: pd.DataFrame, competition_nom: str) -> Player:
    if competition_nom == "atp":
        matches_df = pd.read_csv("./data/tennis/atp_matches_2024.csv")
    else:
        matches_df = pd.read_csv("./data/tennis/wta_matches_2024.csv")

    wins_count = matches_df["winner_id"].value_counts()
    goat_id = str(wins_count.idxmax())

    goats = players_df[players_df["player_id"].astype(str) == goat_id]
    if len(goats) == 0:
        raise ValueError("Joueur introuvable")

    goat_row = goats.iloc[0]
    return Player(nom=f"{goat_row['name_first']} {goat_row['name_last']}", birthdate=None)