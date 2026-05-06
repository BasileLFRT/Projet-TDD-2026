import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_player_matches(players_df, matches, sport: Sport, competition: Competition = None):
    if sport.nom == "tennis":
        players_df["full_name"] = players_df["name_first"] + " " + players_df["name_last"]
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['full_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        player_row = players_df.loc[index]
        player_id = str(player_row["player_id"])
        matches_df = pd.read_csv(f"./data/tennis/{competition.nom}_matches_2024.csv")
        player_matches = matches_df[
            (matches_df["winner_id"].astype(str) == player_id) |
            (matches_df["loser_id"].astype(str) == player_id)
        ]
        for _, match in player_matches.iterrows():
            print(f"{match['tourney_date']} | {match['tourney_name']} | {match['winner_id']} vs {match['loser_id']} | {match['score']}")

    elif competition and competition.nom == "european_leagues":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['player_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        player_id = players_df.loc[index]["player_api_id"]
        matches_df = pd.read_csv("./data/football_european_leagues/match.csv")
        player_cols = [f"home_player_{i}" for i in range(1, 12)] + [f"away_player_{i}" for i in range(1, 12)]
        player_matches = matches_df[matches_df[player_cols].isin([player_id]).any(axis=1)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['home_team_api_id']} {match['home_team_goal']} - {match['away_team_goal']} {match['away_team_api_id']}")

    elif competition and competition.nom == "champions_league":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['player_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        club = players_df.loc[index]["club"]
        matches_df = pd.read_csv("./data/football_champions_league/match.csv")
        player_matches = matches_df[(matches_df["team_home"] == club) | (matches_df["team_away"] == club)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['team_home']} {match['score_team_home']} - {match['score_team_away']} {match['team_away']}")

    elif sport.nom == "starcraft_2":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        player_name = players_df.loc[index]["pseudo"]
        matches_df = pd.read_csv("./data/starcraft_2/match.csv")
        player_matches = matches_df[(matches_df["player_1"] == player_name) | (matches_df["player_2"] == player_name)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['player_1']} {int(match['score_player_1'])} - {int(match['score_player_2'])} {match['player_2']}")

    elif sport.nom == "chess":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        player_name = players_df.loc[index]["name"]
        matches_df = pd.read_csv("./data/chess/match.csv")
        player_matches = matches_df[(matches_df["player_1"] == player_name) | (matches_df["player_2"] == player_name)]
        for _, match in player_matches.iterrows():
            print(f"Round {match['round']} | {match['player_1']} {match['score_player_1']} - {match['score_player_2']} {match['player_2']}")

    elif sport.nom == "volleyball":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']} ({row['country_code']})")
            index = int(input("Sélectionne un joueur (numéro) : "))
        country = players_df.loc[index]["country_code"]
        if competition.nom == "volleyball_men":
            team1_col, team2_col = "country_code_1", "country_code_2"
            matches_df = pd.read_csv("./data/volleyball/match_men.csv")
            country_key = country  # codes courts, pas besoin de mapping
        else:
            team1_col, team2_col = "country_1", "country_2"
            matches_df = pd.read_csv("./data/volleyball/match_women.csv")
            country_mapping = {
                "ARG": "Argentina", "BRA": "Brazil", "CAN": "Canada", "CHN": "China",
                "DOM": "Dominican Republic", "EGY": "Egypt", "FRA": "France",
                "GER": "Germany", "ITA": "Italy", "JPN": "Japan", "KEN": "Kenya",
                "NED": "Netherlands", "POL": "Poland", "SLO": "Slovenia",
                "SRB": "Serbia", "TUR": "Türkiye", "USA": "United States"
            }
            country_key = country_mapping.get(country, country)
        player_matches = matches_df[(matches_df[team1_col] == country_key) | (matches_df[team2_col] == country_key)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match[team1_col]} {int(match['set_country_1'])} - {int(match['set_country_2'])} {match[team2_col]}")

    elif sport.nom == "badminton":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        player_name = players_df.loc[index]["name"]
        matches_df = pd.read_csv("./data/badminton/match.csv")
        player_matches = matches_df[(matches_df["player_1"] == player_name) | (matches_df["player_2"] == player_name)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['tournament']} | {match['player_1']} vs {match['player_2']} | {match['game_1_score']} {match['game_2_score']} {match['game_3_score'] if pd.notna(match['game_3_score']) else ''}")

    else:  # basketball
        players_df["full_name"] = players_df["first_name"] + " " + players_df["last_name"]
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['full_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        team_id = int(players_df.loc[index]["team_id"])
        matches_df = pd.read_csv("./data/basketball/game.csv")
        player_matches = matches_df[(matches_df["team_id_home"] == team_id) | (matches_df["team_id_away"] == team_id)]
        for _, match in player_matches.iterrows():
            print(f"{match['game_date']} | {match['team_id_home']} {match['pts_home']} - {match['pts_away']} {match['team_id_away']}")