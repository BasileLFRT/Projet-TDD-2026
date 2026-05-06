import csv

from src.Model.Match import Match


class StarcraftMatchLoader:
    """Charge les données de matchs de Starcraft à partir d'un fichier CSV.
    
    On utilise des colonnes du fichier CSV :
    - date: la date du match
    - player_1: le nom du premier joueur
    - player_2: le nom du second joueur
    - score_player_1: le score du premier joueur
    - score_player_2: le score du second joueur
    """
    @staticmethod
    def load_all_matches() -> list[Match]:
        """Charge tous les matchs de Starcraft à partir du fichier CSV 
        et les retourne sous forme de liste d'instances de Match.
        
        Returns:
            list[Match]: une liste d'instances de Match représentant les matchs chargés.
        
        Raises:
            FileNotFoundError: si le fichier CSV n'est pas trouvé.
            csv.Error: si une erreur se produit lors de la lecture du fichier
            ValueError: si les données du CSV ne sont pas au format attendu.
        """
        liste_matchs = []
        with open('./data/starcraft_2/match.csv', 'r') as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader):
                match = Match(
                    match_id=i,
                    date=row.get("date"),
                    team1=row.get("player_1"),
                    team2=row.get("player_2"),
                    score1=1 if row.get("score_player_1") == "W" else (0 if row.get("score_player_1") == "L" else int(row.get("score_player_1") or 0)),
                    score2=1 if row.get("score_player_2") == "W" else (0 if row.get("score_player_2") == "L" else int(row.get("score_player_2") or 0)),
                )
                liste_matchs.append(match)
        return liste_matchs