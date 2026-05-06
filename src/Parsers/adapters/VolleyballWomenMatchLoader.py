import csv
from src.Model.Match import Match

class VolleyballWomenMatchLoader:
    """Classe pour charger les données des matchs de volley féminin à partir d'un fichier CSV.
    
    Utilise les colonnes date, country_1, country_2, set_country_1 et set_country_2 du CSV
    """
    def load_all_matches(self) -> list[Match]:
        """Charge tous les matchs de volley féminin à partir du fichier CSV et les retourne sous forme d'instances de la classe Match.
        
        Returns:
            list[Match]: Une liste d'instances de la classe Match représentant les matchs de volley féminin.
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: si des colonnes sont manquantes.
        """
        liste_matchs = []
        with open('./data/volleyball/match_women.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("country_1"),
                    team2=row.get("country_2"),
                    score1=int(row.get("set_country_1") or 0),
                    score2=int(row.get("set_country_2") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = VolleyballWomenMatchLoader().load_all_matches()
    for match in matches:
        print(match)