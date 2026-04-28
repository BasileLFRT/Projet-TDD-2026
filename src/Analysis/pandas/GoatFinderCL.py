import pandas as pd
from src.Model.Player import Player

def find_the_goat_cl(players_df: pd.DataFrame) -> Player:
    goat_row = players_df.loc[players_df["goals"].astype(float).idxmax()]
    return Player(nom=goat_row["player_name"], birthdate=None)