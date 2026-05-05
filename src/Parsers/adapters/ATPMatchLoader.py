import csv
from src.Model.Match import Match

class ATPMatchLoader:
    """Classe permettant de charger les données des matchs ATP à partir d'un fichier CSV.
    
    Lit les données du fichier 'atp_matches_2024.csv' et en crée des instances de Match
    en utilisant les colonnes: match_num, tourney_date, winner_id, loser_id.
    Les scores des matchs sont initiés à 0 par défaut
    """
    def load_all_matches(self) -> list[Match]:
        """ Lit le fichier CSV ATP et en liste les matchs
        
        Returns:
            list[Match]: Une liste d'instances Match qui sont les matchs chargés
        
        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé"""
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