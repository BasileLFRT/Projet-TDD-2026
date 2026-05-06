import csv
from src.Model.Match import Match

class WTAMatchLoader:
    """Charge les données de matchs de Tennis féminin à partir d'un fichier CSV et les convertit en objets Match.
    
    utilise les colonnes match_num, tourney_date, winner_id, loser_id pour créer les objets Match,
    issues du fichier wta_matches_2024.csv de tennis"""
    def load_all_matches(self) -> list[Match]:
        """Lit le fichier CSV et crée une liste d'objets Match à partir des données.
        
        Returns:
            list[Match]: Une liste d'objets Match représentant les matchs chargés depuis le
            
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes attendues ne sont pas présentes dans le CSV."""
        liste_matchs = []
        with open('./data/tennis/wta_matches_2024.csv', newline='') as csvfile:
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
    matches = WTAMatchLoader().load_all_matches()
    for match in matches:
        print(match)