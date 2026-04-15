import csv

from src.Model.match import Match 

liste_matchs = []

with open('./data/football_european_leagues/match.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        match = Match(
            match_id=row.get("match_api_id"),
            date=row.get("date"),
            home_team=row.get("home_team_api_id"),
            away_team=row.get("away_team_api_id"),
            home_score=int(row.get("home_team_goal") or 0),
            away_score=int(row.get("away_team_goal") or 0),
        )
        liste_matchs.append(match)

        print(match)