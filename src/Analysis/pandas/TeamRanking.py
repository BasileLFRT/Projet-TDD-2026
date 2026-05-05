import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_team_ranking(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None):
    if sport.nom in ["chess", "badminton", "starcraft_2", "tennis"]:
        raise ValueError("Fonctionnalité non disponible car sport individuel")

    ranking = {}

    if competition and competition.nom == "european_leagues":
        for _, row in matches_df.iterrows():
            home = row["home_team_api_id"]
            away = row["away_team_api_id"]
            home_goals = int(row["home_team_goal"] or 0)
            away_goals = int(row["away_team_goal"] or 0)
            ranking.setdefault(home, 0)
            ranking.setdefault(away, 0)
            if home_goals > away_goals:
                ranking[home] += 3
            elif away_goals > home_goals:
                ranking[away] += 3
            else:
                ranking[home] += 1
                ranking[away] += 1

        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        sorted_teams = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        print("\nClassement des équipes :")
        for i, (team_id, points) in enumerate(sorted_teams[:20]):
            team_row = teams_df[teams_df["team_api_id"] == team_id]
            team_name = team_row.iloc[0]["team_long_name"] if len(team_row) > 0 else str(team_id)
            print(f"  {i+1}. {team_name} — {points} pts")

    elif competition and competition.nom == "champions_league":
        for _, row in matches_df.iterrows():
            home = row["team_home"]
            away = row["team_away"]
            home_goals = int(row["score_team_home"] or 0)
            away_goals = int(row["score_team_away"] or 0)
            ranking.setdefault(home, 0)
            ranking.setdefault(away, 0)
            if home_goals > away_goals:
                ranking[home] += 3
            elif away_goals > home_goals:
                ranking[away] += 3
            else:
                ranking[home] += 1
                ranking[away] += 1

        sorted_teams = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        print("\nClassement des équipes :")
        for i, (team_name, points) in enumerate(sorted_teams[:20]):
            print(f"  {i+1}. {team_name} — {points} pts")

    else:  # basketball
        for _, row in matches_df.iterrows():
            home = row["team_id_home"]
            away = row["team_id_away"]
            ranking.setdefault(home, 0)
            ranking.setdefault(away, 0)
            if row["pts_home"] > row["pts_away"]:
                ranking[home] += 1
            elif row["pts_away"] > row["pts_home"]:
                ranking[away] += 1

        teams_df = pd.read_csv("./data/basketball/team.csv")
        sorted_teams = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        print("\nClassement des équipes :")
        for i, (team_id, wins) in enumerate(sorted_teams[:20]):
            team_row = teams_df[teams_df["id"] == team_id]
            team_name = team_row.iloc[0]["full_name"] if len(team_row) > 0 else str(team_id)
            print(f"  {i+1}. {team_name} — {wins} victoires")