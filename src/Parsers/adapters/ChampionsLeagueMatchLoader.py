import csv
from src.Model.Match import Match

class ChampionsLeagueMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/football_champions_league/match.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("team_home"),
                    team2=row.get("team_away"),
                    score1=int(row.get("score_team_home") or 0),
                    score2=int(row.get("score_team_away") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs