import csv
from src.Model.Match import Match

class CS2MatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/counter_strike_2/match.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("team_1"),
                    team2=row.get("team_2"),
                    score1=int(row.get("score_team_1") or 0),
                    score2=int(row.get("score_team_2") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = CS2MatchLoader().load_all_matches()
    for match in matches:
        print(match)