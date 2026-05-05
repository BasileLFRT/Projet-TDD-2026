import csv
from src.Model.Match import Match

class VolleyballMenMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/volleyball/match_men.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("country_code_1"),
                    team2=row.get("country_code_2"),
                    score1=int(row.get("set_country_1") or 0),
                    score2=int(row.get("set_country_2") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = VolleyballMenMatchLoader().load_all_matches()
    for match in matches:
        print(match)