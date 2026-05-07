import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from src.Model.Match import Match

def show_match_players(matches: list[Match], sport: Sport, competition: Competition = None):
    for i, match in enumerate(matches):
        print(f"{i} - {match}")
    index = int(input("Sélectionne un match (numéro) : "))
    match_choisi = matches[index]
    print(f"Match choisi : {match_choisi}")

    if sport.nom == "tennis":
        csv_folder = "./data/tennis"
        match_file = f"{competition.nom}_matches_2024.csv"
    elif sport.nom == "volleyball":
        csv_folder = "./data/volleyball"
        match_file = "match_men.csv" if competition.nom == "volleyball_men" else "match_women.csv"
    elif sport.nom == "starcraft_2":
        csv_folder = "./data/starcraft_2"
        match_file = "match.csv"
    elif sport.nom == "chess":
        csv_folder = "./data/chess"
        match_file = "match.csv"
    elif competition is not None:
        csv_folder = f"./data/football_{competition.nom}"
        match_file = "match.csv"
    else:
        csv_folder = "./data/basketball"
        match_file = "game.csv"

    matches_df = pd.read_csv(f"{csv_folder}/{match_file}")
    if sport.nom == "tennis":
        players_df = pd.read_csv(f"{csv_folder}/{competition.nom}_players_2024.csv")
    elif sport.nom == "volleyball":
        players_df = pd.read_csv("./data/volleyball/player_men.csv" if competition.nom == "volleyball_men" else "./data/volleyball/player_women.csv")
    else:
        players_df = pd.read_csv(f"{csv_folder}/player.csv")
    
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
    elif sport.nom == "tennis":
        players_in_match = players_df[players_df["player_id"].astype(str).isin([match_choisi.team1, match_choisi.team2])]
        for _, player in players_in_match.iterrows():
            print(f"{player['name_first']} {player['name_last']}")
    
    elif sport.nom in ["chess", "starcraft_2"]:
        print(f"\nJoueurs du match :")
        print(f"  {match_choisi.team1}")
        print(f"  {match_choisi.team2}")
        return

    elif sport.nom == "volleyball":
        if competition.nom == "volleyball_men":
            players_in_match = players_df[players_df["country_code"].isin([match_choisi.team1, match_choisi.team2])]
        else:
            country_mapping = {
                "Argentina": "ARG", "Brazil": "BRA", "Canada": "CAN", "China": "CHN",
                "Dominican Republic": "DOM", "Egypt": "EGY", "France": "FRA",
                "Germany": "GER", "Italy": "ITA", "Japan": "JPN", "Kenya": "KEN",
                "Netherlands": "NED", "Poland": "POL", "Slovenia": "SLO",
                "Serbia": "SRB", "Türkiye": "TUR", "United States": "USA"
            }
            codes = [country_mapping.get(match_choisi.team1, match_choisi.team1),
                     country_mapping.get(match_choisi.team2, match_choisi.team2)]
            players_in_match = players_df[players_df["country_code"].isin(codes)]
        for _, player in players_in_match.iterrows():
            print(f"{player['name']} ({player['country_code']})")

    elif sport.nom == "badminton":
        print(f"\nJoueurs du match :")
        print(f"  {match_choisi.team1}")
        print(f"  {match_choisi.team2}")
        return

    elif sport.nom == "league_of_legends":
        matches_df = pd.read_csv("./data/league_of_legends/match.csv")
        match_row = matches_df[(matches_df["team_blue"] == match_choisi.team1) & (matches_df["team_red"] == match_choisi.team2)].iloc[0]
        print(f"\nJoueurs du match :")
        print(f"  Équipe bleue ({match_choisi.team1}) :")
        for col in ["top_team_blue", "jungle_team_blue", "mid_team_blue", "bot_team_blue", "sup_team_blue"]:
            print(f"    {col.split('_')[0]} : {match_row[col]}")
        print(f"  Équipe rouge ({match_choisi.team2}) :")
        for col in ["top_team_red", "jungle_team_red", "mid_team_red", "bot_team_red", "sup_team_red"]:
            print(f"    {col.split('_')[0]} : {match_row[col]}")

    elif sport.nom == "counter_strike_2":
        players_df = pd.read_csv("./data/counter_strike_2/player.csv")
        print(f"\nJoueurs du match :")
        print(f"  {match_choisi.team1} vs {match_choisi.team2}")
        for _, player in players_df[players_df["team"] == match_choisi.team1].iterrows():
            print(f"  {player['name']} ({player['pseudo']}) — {player['role']}")
        print()
        for _, player in players_df[players_df["team"] == match_choisi.team2].iterrows():
            print(f"  {player['name']} ({player['pseudo']}) — {player['role']}")

    else: #basketball
        players_in_match = players_df[players_df["team_id"].isin([int(match_choisi.team1), int(match_choisi.team2)])]
        for _, player in players_in_match.iterrows():
            print(f"{player['first_name']} {player['last_name']}")