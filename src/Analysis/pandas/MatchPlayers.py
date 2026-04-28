import pandas as pd
from src.Parsers.MatchLoader import MatchLoader
from src.Model.Competition import Competition

def show_match_players(competition: Competition):
    matches = MatchLoader().load_all_matches(competition)
    for i, match in enumerate(matches):
        print(f"{i} - {match}")
    index = int(input("Sélectionne un match (numéro) : "))
    match_choisi = matches[index]
    print(f"Match choisi : {match_choisi}")

    matches_df = pd.read_csv(f"./data/football_{competition.nom}/match.csv")
    players_df = pd.read_csv(f"./data/football_{competition.nom}/player.csv")

    if competition.nom == "european_leagues":
        player_cols = [f"home_player_{i}" for i in range(1, 12)] + [f"away_player_{i}" for i in range(1, 12)]
        match_row = matches_df[matches_df["match_api_id"] == int(match_choisi.match_id)].iloc[0]
        player_ids = [match_row[col] for col in player_cols if pd.notna(match_row[col])]
        players_in_match = players_df[players_df["player_api_id"].isin(player_ids)]
    else:
        players_in_match = players_df[players_df["club"].isin([match_choisi.team1, match_choisi.team2])]

    print("\nJoueurs du match :")
    for _, player in players_in_match.iterrows():
        print(player["player_name"])