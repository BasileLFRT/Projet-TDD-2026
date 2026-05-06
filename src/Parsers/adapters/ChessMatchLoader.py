import csv
from src.Model.Match import Match
import pandas as pd

class ChessMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/chess/match.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=row.get("match"),
                    date=None,
                    team1=row.get("player_1"),
                    team2=row.get("player_2"),
                    score1=float(pd.to_numeric(row.get("score_player_1"), errors='coerce') or 0),
                    score2=float(pd.to_numeric(row.get("score_player_2"), errors='coerce') or 0),
                    )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = ChessMatchLoader().load_all_matches()
    for match in matches:
        print(match)