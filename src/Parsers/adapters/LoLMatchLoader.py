import csv

from src.Model.Match import Match


class LoLMatchLoader:
    @staticmethod
    def load_all_matches() -> list[Match]:
        liste_matchs = []
        with open('./data/league_of_legends/match.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                match = Match(
                    match_id=row.get("gameid"),
                    date=row.get("date"),
                    team1=row.get("team_blue"),
                    team2=row.get("team_red"),
                    score1=int(row.get("kills_team_blue") or 0),
                    score2=int(row.get("kills_team_red") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs