import pandas as pd
from src.Parsers.MatchLoader import MatchLoader
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_match_players(sport: Sport, competition: Competition = None):
    matches = MatchLoader().load_all_matches(sport, competition)
    for i, match in enumerate(matches):
        print(f"{i} - {match}")
    index = int(input("Sélectionne un match (numéro) : "))
    match_choisi = matches[index]
    print(f"Match choisi : {match_choisi}")

    if sport.nom == "tennis":
        csv_folder = "./data/tennis"
        match_file = f"{competition.nom}_matches_2024.csv"
    elif competition is not None:
        csv_folder = f"./data/football_{competition.nom}"
        match_file = "match.csv"
    else:
        csv_folder = "./data/basketball"
        match_file = "game.csv"

    matches_df = pd.read_csv(f"{csv_folder}/{match_file}")
    players_df = pd.read_csv(f"{csv_folder}/player.csv" if sport.nom != "tennis" else f"{csv_folder}/{competition.nom}_players_2024.csv")

    if competition and competition.nom == "european_leagues":
        player_cols = [f"home_player_{i}" for i in range(1, 12)] + [f"away_player_{i}" for i in range(1, 12)]
        match_row = matches_df[matches_df["match_api_id"] == int(match_choisi.match_id)].iloc[0]
        player_ids = [match_row[col] for col in player_cols if pd.notna(match_row[col])]
        players_in_match = players_df[players_df["player_api_id"].isin(player_ids)]
        for _, player in players_in_match.iterrows():
            print(player["player_name"])
    elif competition and competition.nom == "champions_league":
        players_in_match = players_df[players_df["club"].isin([match_choisi.team1, match_choisi.team2])]
        for _, player in players_in_match.iterrows():
            print(player["player_name"])
            print(player["player_name"])
    elif sport.nom == "tennis":
        players_in_match = players_df[players_df["player_id"].astype(str).isin([match_choisi.team1, match_choisi.team2])]
        for _, player in players_in_match.iterrows():
            print(f"{player['name_first']} {player['name_last']}")
    else:
        players_in_match = players_df[players_df["team_id"].isin([int(match_choisi.team1), int(match_choisi.team2)])]
        for _, player in players_in_match.iterrows():
            print(f"{player['first_name']} {player['last_name']}")