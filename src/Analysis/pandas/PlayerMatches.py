import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_player_matches(players_df, matches, sport: Sport, competition: Competition = None):
    if sport.nom == "tennis":
        players_df["full_name"] = players_df["name_first"] + " " + players_df["name_last"]
        for i, row in players_df.iterrows():
            print(f"{i} - {row['full_name']}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        player_row = players_df.iloc[index]
        player_id = str(player_row["player_id"])
        matches_df = pd.read_csv(f"./data/tennis/{competition.nom}_matches_2024.csv")
        player_matches = matches_df[
            (matches_df["winner_id"].astype(str) == player_id) |
            (matches_df["loser_id"].astype(str) == player_id)
        ]
        for _, match in player_matches.iterrows():
            print(f"{match['tourney_date']} | {match['tourney_name']} | {match['winner_id']} vs {match['loser_id']} | {match['score']}")

    elif competition and competition.nom == "european_leagues":
        for i, row in players_df.iterrows():
            print(f"{i} - {row['player_name']}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        player_id = players_df.iloc[index]["player_api_id"]
        matches_df = pd.read_csv("./data/football_european_leagues/match.csv")
        player_cols = [f"home_player_{i}" for i in range(1, 12)] + [f"away_player_{i}" for i in range(1, 12)]
        player_matches = matches_df[matches_df[player_cols].isin([player_id]).any(axis=1)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['home_team_api_id']} {match['home_team_goal']} - {match['away_team_goal']} {match['away_team_api_id']}")

    elif competition and competition.nom == "champions_league":
        for i, row in players_df.iterrows():
            print(f"{i} - {row['player_name']}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        club = players_df.iloc[index]["club"]
        matches_df = pd.read_csv("./data/football_champions_league/match.csv")
        player_matches = matches_df[(matches_df["team_home"] == club) | (matches_df["team_away"] == club)]
        for _, match in player_matches.iterrows():
            print(f"{match['date']} | {match['team_home']} {match['score_team_home']} - {match['score_team_away']} {match['team_away']}")

    else:  # basketball
        players_df["full_name"] = players_df["first_name"] + " " + players_df["last_name"]
        for i, row in players_df.iterrows():
            print(f"{i} - {row['full_name']}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        team_id = int(players_df.iloc[index]["team_id"])
        matches_df = pd.read_csv("./data/basketball/game.csv")
        player_matches = matches_df[(matches_df["team_id_home"] == team_id) | (matches_df["team_id_away"] == team_id)]
        for _, match in player_matches.iterrows():
            print(f"{match['game_date']} | {match['team_id_home']} {match['pts_home']} - {match['pts_away']} {match['team_id_away']}")