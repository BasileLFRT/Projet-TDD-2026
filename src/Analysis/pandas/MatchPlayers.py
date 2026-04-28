import pandas as pd
from src.Parsers.MatchLoader import MatchLoader
from src.Model.Sport import Sport

def show_match_players(sport: Sport):
    matches = MatchLoader().load_all_matches(sport)
    for i, match in enumerate(matches):
        print(f"{i} - {match}")
    index = int(input("Sélectionne un match (numéro) : "))
    match_choisi = matches[index]
    print(f"Match choisi : {match_choisi}")

    matches_df = pd.read_csv("./data/football_european_leagues/match.csv")
    players_df = pd.read_csv("./data/football_european_leagues/player.csv")

    player_cols = [f"home_player_{i}" for i in range(1, 12)] + [f"away_player_{i}" for i in range(1, 12)]
    match_row = matches_df[matches_df["match_api_id"] == int(match_choisi.match_id)].iloc[0]
    player_ids = [match_row[col] for col in player_cols if pd.notna(match_row[col])]
    players_in_match = players_df[players_df["player_api_id"].isin(player_ids)]

    print("\nJoueurs du match :")
    for _, player in players_in_match.iterrows():
        print(player["player_name"])