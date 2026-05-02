import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_team_matches(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None):
    if competition and competition.nom == "european_leagues":
        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        for i, row in teams_df.iterrows():
            print(f"{i} - {row['team_long_name']}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_id = teams_df.iloc[index]["team_api_id"]
        team_matches = matches_df[(matches_df["home_team_api_id"] == team_id) | (matches_df["away_team_api_id"] == team_id)]
        for _, match in team_matches.iterrows():
            print(f"{match['date']} | {match['home_team_api_id']} {int(match['home_team_goal'])} - {int(match['away_team_goal'])} {match['away_team_api_id']}")

    elif competition and competition.nom == "champions_league":
        teams = sorted(set(matches_df["team_home"].tolist() + matches_df["team_away"].tolist()))
        for i, team in enumerate(teams):
            print(f"{i} - {team}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team = teams[index]
        team_matches = matches_df[(matches_df["team_home"] == team) | (matches_df["team_away"] == team)]
        for _, match in team_matches.iterrows():
            print(f"{match['date']} | {match['team_home']} {int(match['score_team_home'])} - {int(match['score_team_away'])} {match['team_away']}")

    elif sport.nom == "tennis":
        raise ValueError("Pas d'équipes au tennis")

    else:  # basketball
        teams_df = pd.read_csv("./data/basketball/team.csv")
        for i, row in teams_df.iterrows():
            print(f"{i} - {row['full_name']}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_id = teams_df.iloc[index]["id"]
        team_matches = matches_df[(matches_df["team_id_home"] == team_id) | (matches_df["team_id_away"] == team_id)]
        for _, match in team_matches.iterrows():
            print(f"{match['game_date']} | {match['team_id_home']} {int(match['pts_home'])} - {int(match['pts_away'])} {match['team_id_away']}")

