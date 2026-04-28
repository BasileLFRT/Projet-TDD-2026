import csv

from src.Model.Match import Match 

class FootballMatchLoader:
    @staticmethod
    def load_all_matches() -> list[Match]:
        liste_matchs = []
        with open('./data/football_european_leagues/match.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                match = Match(
                    match_id=row.get("match_api_id"),
                    date=row.get("date"),
                    team1=row.get("home_team_api_id"),
                    team2=row.get("away_team_api_id"),
                    score1=int(row.get("home_team_goal") or 0),
                    score2=int(row.get("away_team_goal") or 0),
                )
                liste_matchs.append(match)
            return liste_matchs
