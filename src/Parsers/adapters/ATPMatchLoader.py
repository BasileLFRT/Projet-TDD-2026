import csv
from src.Model.Match import Match

class ATPMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/tennis/atp_matches_2024.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=row.get("match_num"),
                    date=row.get("tourney_date"),
                    team1=row.get("winner_id"),
                    team2=row.get("loser_id"),
                    score1=0,
                    score2=0,
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = ATPMatchLoader().load_all_matches()
    for match in matches:
        print(match)