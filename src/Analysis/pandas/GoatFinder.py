import pandas as pd

from src.Model.Player import Player


def find_the_goat_in_df(players: pd.DataFrame) -> Player:
    matches_df = pd.read_csv("./data/football_european_leagues/match.csv")

    home_cols = [f"home_player_{i}" for i in range(1, 12)]
    away_cols = [f"away_player_{i}" for i in range(1, 12)]

    home_wins = matches_df[matches_df["home_team_goal"] > matches_df["away_team_goal"]]
    away_wins = matches_df[matches_df["away_team_goal"] > matches_df["home_team_goal"]]

    wins_count = {}
    for _, row in home_wins.iterrows():
        for col in home_cols:
            pid = row[col]
            if pd.notna(pid):
                wins_count[int(pid)] = wins_count.get(int(pid), 0) + 1

    for _, row in away_wins.iterrows():
        for col in away_cols:
            pid = row[col]
            if pd.notna(pid):
                wins_count[int(pid)] = wins_count.get(int(pid), 0) + 1

    goat_id = max(wins_count, key=wins_count.get)
    goat_row = players[players["player_api_id"] == goat_id].iloc[0]

    goats = players[players["player_api_id"] == goat_id]
    if not len(goats) == 1:
        raise ValueError("There can only be one GOAT")
    the_goat: pd.Series = goats.iloc[0]
    return Player(nom=the_goat["player_name"], birthdate=None)