import csv
from src.Model.Match import Match

class BasketballMatchLoader:
    """Classe permettant de charger les données des matchs de basketball à partir d'un fichier CSV.

    Lit les données du fichier 'game.csv' lié au basketball et en crée des instances de Match
    en utilisant les colonnes: game_id, game_date, team_id_home, team_id_away, pts_home, pts_away.
    Les scores sont extraits des colonnes pts_home et pts_away, avec une valeur par défaut de 0
    """
    def load_all_matches(self) -> list[Match]:
        """ Lit le fichier CSV de basketball et en liste les matchs
        
        Returns:
            list[Match]: Une liste d'instances Match qui sont les matchs chargés
        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé
        """
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