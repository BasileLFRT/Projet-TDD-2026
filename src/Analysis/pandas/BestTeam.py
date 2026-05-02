import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_best_team(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None):
    if sport.nom == "tennis":
        raise ValueError("Pas d'équipes au tennis")

    wins = {}

    if competition and competition.nom == "european_leagues":
        for _, row in matches_df.iterrows():
            home = row["home_team_api_id"]
            away = row["away_team_api_id"]
            wins.setdefault(home, 0)
            wins.setdefault(away, 0)
            if int(row["home_team_goal"] or 0) > int(row["away_team_goal"] or 0):
                wins[home] += 1
            elif int(row["away_team_goal"] or 0) > int(row["home_team_goal"] or 0):
                wins[away] += 1

        best_id = max(wins, key=wins.get)
        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        team_name = teams_df[teams_df["team_api_id"] == best_id].iloc[0]["team_long_name"]
        print(f"\nMeilleure équipe : {team_name} ({wins[best_id]} victoires)")

    elif competition and competition.nom == "champions_league":
        for _, row in matches_df.iterrows():
            home = row["team_home"]
            away = row["team_away"]
            wins.setdefault(home, 0)
            wins.setdefault(away, 0)
            if int(row["score_team_home"] or 0) > int(row["score_team_away"] or 0):
                wins[home] += 1
            elif int(row["score_team_away"] or 0) > int(row["score_team_home"] or 0):
                wins[away] += 1

        best = max(wins, key=wins.get)
        print(f"\nMeilleure équipe : {best} ({wins[best]} victoires)")

    else:  # basketball
        for _, row in matches_df.iterrows():
            home = row["team_id_home"]
            away = row["team_id_away"]
            wins.setdefault(home, 0)
            wins.setdefault(away, 0)
            if row["pts_home"] > row["pts_away"]:
                wins[home] += 1
            elif row["pts_away"] > row["pts_home"]:
                wins[away] += 1

        best_id = max(wins, key=wins.get)
        teams_df = pd.read_csv("./data/basketball/team.csv")
        team_name = teams_df[teams_df["id"] == best_id].iloc[0]["full_name"]
        print(f"\nMeilleure équipe : {team_name} ({wins[best_id]} victoires)")