import csv
from src.Model.Match import Match
import pandas as pd

class ChessMatchLoader:
    """Classe pour charger les données de matchs d'échecs à partir d'un fichier CSV.
    
    Cette classe lit les données de matchs d'échecs à partir d'un fichier CSV et les convertit en objets Match.
    
    Utilise les colonnes match, player_1, player_2, score_player_1 et score_player_2 du fichier CSV
    """
    def load_all_matches(self) -> list[Match]:
        """Charge tous les matchs d'échecs à partir du fichier CSV et les retourne sous forme de liste de Match.
        
        Returns:
            list[Match]: Une liste d'objets Match représentant les matchs d'échecs
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé
            Exception: Pour toute autre erreur lors du chargement des données"""
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