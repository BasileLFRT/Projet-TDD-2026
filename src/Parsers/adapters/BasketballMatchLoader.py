import csv
from src.Model.Match import Match

class BasketballMatchLoader:
    def load_all_matches(self) -> list[Match]:
        liste_matchs = []
        with open('./data/basketball/game.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=row.get("game_id"),
                    date=row.get("game_date"),
                    team1=row.get("team_id_home"),
                    team2=row.get("team_id_away"),
                    score1=int(row.get("pts_home") or 0),
                    score2=int(row.get("pts_away") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = BasketballMatchLoader().load_all_matches()
    for match in matches:
        print(match)