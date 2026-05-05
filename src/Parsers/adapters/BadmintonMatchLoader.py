# src/Parsers/adapters/BadmintonMatchLoader.py
import csv
from src.Model.Match import Match

class BadmintonMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/badminton/match.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("player_1"),
                    team2=row.get("player_2"),
                    score1=0,
                    score2=0,
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = BadmintonMatchLoader().load_all_matches()
    for match in matches:
        print(match)