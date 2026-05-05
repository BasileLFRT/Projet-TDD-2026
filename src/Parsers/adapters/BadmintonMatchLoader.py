# src/Parsers/adapters/BadmintonMatchLoader.py
import csv
from src.Model.Match import Match

class BadmintonMatchLoader:
    """Classe permettant de charger les données des matchs de badminton à partir d'un fichier CSV.

    Lit les données du fichier 'match.csv' lié au badminton et en crée des instances de Match
    en utilisant les colonnes: date, player_1, player_2.
    Les scores sont initialisés à 0 par défaut.
    """
    def load_all_matches(self) -> list[Match]:
        """ Lit le fichier CSV de badminton et en liste les matchs

        Returns:
            list[Match]: Une liste d'instances Match qui sont les matchs chargés
        
        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé
        """
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